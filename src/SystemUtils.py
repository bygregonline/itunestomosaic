import sys
import platform
import datetime
import psutil
import getpass
import os
import cpuinfo

from termcolor import colored
from sys import stdout


"""

TODOD
"""



class Welcome:



    """

    TODO
    """
    @staticmethod
    def printWelcome(logo, version='beta', color_d='blue', color_out='magenta', attributes2=['bold']):
        print(logo)
        print(colored('+------------------------------------------+', color_out))
        print(colored('beerware software.', color_d, attrs=attributes2))
        s = getpass.getuser() + '@' + platform.node()

        print(colored('Computer:            ', color_d, attrs=attributes2), colored(s, color_out))
        print(colored('Script:              ', color_d, attrs=attributes2), colored(Welcome.getScript(), color_out))
        print(colored('Api version:         ', color_d, attrs=attributes2), colored(sys.api_version, color_out))

        print(colored('Path:                ', color_d, attrs=attributes2), colored(sys.executable, color_out))
        print(colored('Native Compiler:     ', color_d, attrs=attributes2), colored(platform.python_compiler(), color_out))
        print(colored('Architecture:        ', color_d, attrs=attributes2), colored(platform.processor(), color_out))
        s = platform.machine() + '  ' + platform.system() + ' Kernel version ' + platform.release()
        print(colored('Kernel:              ', color_d, attrs=attributes2), colored(s, color_out))

        print(
        colored('CPU Info:            ', color_d, attrs=attributes2), colored(cpuinfo.get_cpu_info()['brand'], color_out))


        print(colored('Python Version:      ', color_d, attrs=attributes2), colored(platform.python_version(), color_out))
        print(
        colored('Processors:          ', color_d, attrs=attributes2), colored(psutil.cpu_count(logical=False), color_out))
        print(colored('Terminal:            ', color_d, attrs=attributes2), colored(Welcome.getTerminal(), color_out))
        print(colored('User:                ', color_d, attrs=attributes2), colored(getpass.getuser(), color_out))
        print(colored('Current process:     ', color_d, attrs=attributes2), colored(psutil.Process().pid, color_out))
        print(colored('Code version:        ', color_d, attrs=attributes2), colored(version, color_out))
        mem = psutil.virtual_memory()

        print(
        colored('Total Memory:        ', color_d, attrs=attributes2), colored(Welcome.sizeof_fmt(mem.total), color_out))

        print(colored('Available Memory:    ', color_d, attrs=attributes2),
              colored(Welcome.sizeof_fmt(mem.available), color_out))
        print(
        colored('Free Memory:         ', color_d, attrs=attributes2), colored(Welcome.sizeof_fmt(mem.free), color_out))
        print(
        colored('Used Memory:         ', color_d, attrs=attributes2), colored(Welcome.sizeof_fmt(mem.used), color_out))
        print(colored('Active Memory:       ', color_d, attrs=attributes2),
              colored(Welcome.sizeof_fmt(mem.active), color_out))
        print(colored('Inactive Memory:     ', color_d, attrs=attributes2),
              colored(Welcome.sizeof_fmt(mem.inactive), color_out))
        print(
        colored('Wired Memory:        ', color_d, attrs=attributes2), colored(Welcome.sizeof_fmt(mem.wired), color_out))

        print(colored('Current path:        ', color_d, attrs=attributes2), colored(os.getcwd(), color_out))

        print(colored('Current date:        ', color_d, attrs=attributes2), colored(datetime.datetime.now(), color_out))
        print(colored('Current time:        ', color_d, attrs=attributes2), colored(datetime.datetime.now(), color_out))
        print(colored('+------------------------------------------+', color_out))





    """

    TODO
    """
    @staticmethod
    def printValues(args, color_d='blue', color_out='magenta', attributes2=['bold']):
        print(colored('Image to process:    ', color_d, attrs=attributes2), colored(args['image'], color_out))
        print(colored('Music library path:  ', color_d, attrs=attributes2), colored(args['mp3_dir'], color_out))
        print(colored('Output file:         ', color_d, attrs=attributes2), colored(args['output'], color_out))
        print(colored('Enlargement factor   ', color_d, attrs=attributes2), colored(args['enl'], color_out))
        print(colored('tile resolution      ', color_d, attrs=attributes2), colored(args['tmr'], color_out))
        print(colored('tile size            ', color_d, attrs=attributes2), colored('%iX%ipx' % (args['tsize'] , args['tsize']), color_out))
        print(colored('+------------------------------------------+', color_out))





    """
    
    
    
    """

    @staticmethod
    def getScript():
        l = psutil.Process().cmdline()
        if len(l)==1:
            return l[0]
        else:
            return l[1]


    """
    
    """
    @staticmethod
    def getTerminal():
        aux = 'Terminal not found'
        try:
            aux = os.ttyname(sys.stdout.fileno()).split(sep='/')[-1]
        except Exception as e:
            pass

        return aux

    #
    #
    #
    #
    #   / ____/ / / / | / / ____/
    #  / /_  / / / /  |/ / /
    # / __/ / /_/ / /|  / /___
    # /_/    \____/_/ |_/\____/
    #
    """
    
    """

    @staticmethod
    def sizeof_fmt(num, suffix='B'):
        for unit in [' ', ' Ki', ' Mi', ' Gi', ' Ti', ' Pi', ' Ei', ' Zi']:
            if abs(num) < 1024.0:
                return "%3.2f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)


    """
    
    """
    @staticmethod
    def showAdvance(msg='', total=10, i=1, outMessage=''):
        s = '[%s] %d %% ' + msg + '%s\r'
        stdout.write(s % (Welcome.advance(int(i / (total / 10)), 10), int(i / (total / 100)), outMessage))
        stdout.flush()

    """
    
    """
    @staticmethod
    def advance(i, m):
        return '#' * i + ' ' * (m - i)