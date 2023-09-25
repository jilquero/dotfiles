from .groups import group_names
from libqtile import hook
from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
                         "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
    d[group_names[1]] = ["Atom", "Subl", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
                         "atom", "subl", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
    d[group_names[2]] = []
    # d[group_names[2]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
    #          "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
    d[group_names[3]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
                         "inkscape", "nomacs", "ristretto", "nitrogen", "feh", "Gimp", "gimp",
                         "libreoffice", ]
    d[group_names[4]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
                         "virtualbox manager", "virtualbox machine", "vmplayer", ]
    d[group_names[5]] = ["Evolution", "Geary", "Mail", "Thunderbird",
                         "evolution", "geary", "mail", "thunderbird", "discord", "caprine", ]
    d[group_names[6]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
                         "spotify", "pragha", "clementine", "deadbeef", "audacious", "cmus", ]
    d[group_names[7]] = ["Vlc", "vlc", "Mpv", "mpv", ]
    #d[group_names[8]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld", "obs",]
    #d[group_names[9]] = ["bruh", "idk", "what", "to", "put", "in", "here",]

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)
