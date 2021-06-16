""" Entry point. """

import sys

from wallauto.bin.config import config_commands


def help_commands(arguments = {}):
    """ shows help """
    title = """
╦ ╦┌─┐┬  ┬  ┌─┐┌─┐┌─┐┌─┐┬─┐  ┌─┐┬ ┬┌┬┐┌─┐┌┬┐┌─┐┌┬┐┌─┐
║║║├─┤│  │  ├─┘├─┤├─┘├┤ ├┬┘  ├─┤│ │ │ │ ││││├─┤ │ ├─┤
╚╩╝┴ ┴┴─┘┴─┘┴  ┴ ┴┴  └─┘┴└─  ┴ ┴└─┘ ┴ └─┘┴ ┴┴ ┴ ┴ ┴ ┴
"""
    print(title)

    for key, value in arguments.items():
        print(f'{key}\t{value["description"]}')

    print('\nEnjoy and share this program :)')


def selector():
    """ Selects de commands. """

    main_arguments = {
        'conf': {
            'description': 'Creates directories, config files and database.',
            'command': config_commands,
        }
    }

    argument = None

    try:
        argument = sys.argv[1]
    except IndexError:
        help_commands(main_arguments)
        sys.exit()

    if argument in main_arguments:
        option = main_arguments[argument]
        option['command']()
    else:
        help_commands(main_arguments)

if __name__ == '__main__':
    selector()
