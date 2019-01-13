from sniffer.api import file_validator, runnable
import os


@file_validator
def py_files(filename):
    return (filename.endswith('.py')
            and not os.path.basename(filename).startswith('.'))


@runnable
def execute_nose(*args):
    return os.system("make") == 0  # TODO
