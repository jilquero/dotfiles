from .path import qtile_path
from os import path
# from os.path import exists
from libqtile import lazy


def load_colors():
    return [["#282a36", "#282a36"],  # color 0 | bg
            ["#282a36", "#282a36"],  # color 1 | bg
            ["#f8f8f2", "#f8f8f2"],  # color 2 | fg
            ["#ff5555", "#ff5555"],  # color 3 | red
            ["#50fa7b", "#50fa7b"],  # color 4 | green
            ["#f1fa8c", "#f1fa8c"],  # color 5 | yellow
            ["#bd93f9", "#bd93f9"],  # color 6 | blue
            ["#ff79c6", "#ff79c6"],  # color 7 | magenta
            ["#8be9fd", "#8be9fd"],  # color 8 | cyan
            ["#bbbbbb", "#bbbbbb"]]  # color 9 | white


if __name__ == "settings.theme":
    colors = load_colors()
