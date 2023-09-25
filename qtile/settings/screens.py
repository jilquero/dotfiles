import os
from libqtile import bar
from libqtile.config import Screen
from .widgets import init_primary_widgets
from .widgets import init_secondary_widgets


def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                widgets=init_primary_widgets(),
                size=35,
                opacity=0.9,
                margin=[5, 10, 0, 10]
            )
        )
    ]

    connected_monitors = len(os.popen(
        "xrandr --listmonitors | grep '+' | awk {'print $4'}").read().splitlines())

    if connected_monitors == 1:
        return screens

    for _ in range(1, connected_monitors):
        screens.append(
            Screen(
                top=bar.Bar(
                    widgets=init_secondary_widgets(),
                    size=35,
                    opacity=0.9,
                    margin=[5, 10, 0, 10]
                )
            )
        )

    return screens


screens = init_screens()
