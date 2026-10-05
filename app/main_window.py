from __future__ import annotations

from typing import Optional

import vlc

from .models import Channel


class VideoPlayer:
    def __init__(self, parent_widget) -> None:
        self.parent_widget = parent_widget
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.current_channel: Optional[Channel] = None

    def attach(self) -> None:
        try:
            self.player.set_hwnd(int(self.parent_widget.winId()))
        except Exception:
            self.player.set_xwindow(int(self.parent_widget.winId()))

    def play_channel(self, channel: Channel) -> None:
        self.current_channel = channel
        media = self.instance.media_new(channel.url)
        self.player.set_media(media)
        self.player.play()

    def play(self) -> None:
        if self.player:
            self.player.play()

    def pause(self) -> None:
        if self.player:
            self.player.pause()

    def stop(self) -> None:
        if self.player:
            self.player.stop()

    def toggle_fullscreen(self) -> None:
        if self.parent_widget.isFullScreen():
            self.parent_widget.showNormal()
        else:
            self.parent_widget.showFullScreen()

    def set_volume(self, level: int) -> None:
        self.player.audio_set_volume(level)
