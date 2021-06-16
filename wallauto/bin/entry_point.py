""" Entry point. """

import sys

from wallauto.bin.config import config_commands

title = """
╦ ╦┌─┐┬  ┬  ┌─┐┌─┐┌─┐┌─┐┬─┐  ┌─┐┬ ┬┌┬┐┌─┐┌┬┐┌─┐┌┬┐┌─┐
║║║├─┤│  │  ├─┘├─┤├─┘├┤ ├┬┘  ├─┤│ │ │ │ ││││├─┤ │ ├─┤
╚╩╝┴ ┴┴─┘┴─┘┴  ┴ ┴┴  └─┘┴└─  ┴ ┴└─┘ ┴ └─┘┴ ┴┴ ┴ ┴ ┴ ┴
"""

def selector():
    """ Selects de commands. """

    main_arguments = {
        'conf': {
            'description': 'Creates directories, config files and database.',
            'command': config_commands,
        }
    }

    def help():
        print(title)

    argument = None

    try:
        argument = sys.argv[1]
    except IndexError:
        help()

    if argument in main_arguments:
        option = main_arguments[argument]
        option['command']()
    else:
        help()

if __name__ == '__main__':
    selector()
