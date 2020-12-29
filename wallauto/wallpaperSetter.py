import pathlib
import platform
import os
import subprocess


class WallpaperSetter:

    @classmethod
    def selector(cls, image_path):
        """ Select method according to operative system. """
        system = platform.system().lower()
        if 'linux' in system:
            cls._linux(image_path)
        elif 'win' in system:
            cls._windows(image_path)
        else:
            cls._mac(image_path)

    @staticmethod
    def _linux(image_path):
        """ Method for Linux. """
        desktop = os.environ['XDG_CURRENT_DESKTOP'].lower()
        image_path = pathlib.Path(image_path).absolute()
        if 'gnome' in desktop:
            subprocess.run([
                'gsettings',
                'set',
                'org.gnome.desktop.background',
                'picture-uri',
                f'file://{str(image_path)}'
            ])

    @staticmethod
    def _mac(image_path):
        """ Method for Mac. """
        subprocess.run([
            'osascript',
            '-e',
            ('\'tell application "Finder" to set desktop picture '
             f'to POSIX file "{str(image_path)}"\'')
        ])

    @staticmethod
    def _windows(image_path):
        """ Method for Windows. """
        # TODO:  <29-12-20, Fernando Cruz> #
        # Check if this command works
        subprocess.run([
            'reg',
            'add',
            r'"HKEY_CURRENT_USER\Control Panel\Desktop"',
            '/v',
            'Wallpaper',
            '/t',
            'REG_SZ',
            '/f',
            '/d',
            f'{str(image_path)}'
        ])
        subprocess.run([
            'RUNDLL32.EXE',
            'user32.dll,',
            'UpdatePerUserSystemParameters'
        ])
