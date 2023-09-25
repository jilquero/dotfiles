from libqtile import widget, qtile, bar
from .theme import colors
from .path import home_dir
from scripts import storage
import subprocess
import socket
import os


myTerm = "alacritty"        # My terminal of choice
myBrowser = "firefox"       # My browser of choice


def init_widgets_defaults():
    return dict(
        font='Source Code Pro Medium',
        fontsize=12,
        padding=5)


def init_separator():
    return widget.Sep(
        size_percent=60,
        margin=5,
        linewidth=2,
        background=colors[1],
        foreground="#555555")


def nerd_icon(nerdfont_icon, fg_color):
    return widget.TextBox(
        font="Iosevka Nerd Font",
        fontsize=15,
        padding=8,
        text=nerdfont_icon,
        foreground=fg_color,
        background=colors[1])


def init_edge_spacer():
    return widget.Spacer(
        length=5,
        background=colors[1])


widget_defaults = init_widgets_defaults()
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        init_edge_spacer(),
        widget.Image(
            filename="~/.config/qtile/icons/python.png",
            background=colors[1],
            margin=3,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(
                    'j4-dmenu'
                ),
                'Button3': lambda: qtile.cmd_spawn(
                    f'{myTerm} -e vim {home_dir}/.config/qtile/config.py'
                )
            }
        ),
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=15,
            foreground=colors[2],
            background=colors[1],
            borderwidth=4,
            highlight_method="text",
            this_current_screen_border=colors[6],
            active=colors[4],
            inactive=colors[2]
        ),
        init_separator(),
        nerd_icon(
            "  ",
            colors[6]
        ),
        widget.TextBox(
            text='100%',
            foreground=colors[2],
            background=colors[1]
        ),
        nerd_icon(
            "墳",
            colors[3]
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[1]
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background=colors[1]
        ),

        # Center bar

        nerd_icon(
            "",
            colors[7]
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[1]
        ),
        init_separator(),
        nerd_icon(
            "﬙",
            colors[3]
        ),
        widget.CPU(
            format="{load_percent}%",
            foreground=colors[2],
            background=colors[1],
            update_interval=2,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
            }
        ),
        nerd_icon(
            "",
            colors[4]
        ),
        widget.Memory(
            measure_mem='G',
            format="{MemUsed:.0f}{mm}",
            foreground=colors[2],
            background=colors[1],
            update_interval=2,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
            }
        ),
        nerd_icon(
            "",
            colors[6]
        ),
        widget.GenPollText(
            foreground=colors[2],
            background=colors[1],
            update_interval=5,
            func=lambda: storage.diskspace('FreeSpace'),
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(f"{myTerm} -e btop")
            }
        ),
        init_separator(),
        nerd_icon(
            "",
            colors[4]
        ),
        widget.GenPollText(
            foreground=colors[2],
            background=colors[1],
            update_interval=5,
            func=lambda: subprocess.check_output(
                f"{home_dir}/.config/qtile/scripts/num-installed-pkgs").decode("utf-8"),
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                myTerm + ' -e sudo pacman -Syu')},
        ),

        # Left Side of the bar

        widget.Spacer(
            length=bar.STRETCH,
            background=colors[1]
        ),
        nerd_icon(
            "",
            colors[4]
        ),
        widget.Net(
            format="{down} ↓↑ {up}",
            foreground=colors[2],
            background=colors[1],
            update_interval=2,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn("def-nmdmenu")
            }
        ),
        init_separator(),
        nerd_icon(
            "",
            colors[7]
        ),
        widget.Clock(
            format='%b %d-%Y',
            foreground=colors[2],
            background=colors[1]
        ),
        nerd_icon(
            "",
            colors[8]
        ),
        widget.Clock(
            format='%H:%M %p',
            foreground=colors[2],
            background=colors[1]
        ),
        widget.Systray(
            background=colors[1]
        ),
        init_edge_spacer()
    ]
    return widgets_list


def init_primary_widgets():
    primary_widgets = init_widgets_list()
    return primary_widgets


def init_secondary_widgets():
    secondary_widgets = init_widgets_list()
    del secondary_widgets[-2]
    return secondary_widgets
