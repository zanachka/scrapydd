import sys
import scrapydd.main
import scrapydd.scheduleutil
import scrapydd.agent
import scrapydd.ssl_gen

usage = '''
usage: scrapydd {command} [options]
Available commands:
    server:         run scrapydd server.
    agent:          run scrapydd agent.
    cert:           make certs.
    add_schedule:   add a schedule to spider.

use scrapydd {command} --help for further help.
'''

def main():
    argv = sys.argv
    if len(argv) == 1:
        print 'No command specified.'
        print_commands()
        sys.exit(1)
        return
    cmd = argv[1]
    if cmd == 'agent':
        scrapydd.agent.run(argv)
    elif cmd == 'server':
        scrapydd.main.run(argv)
    elif cmd == 'add_schedule':
        scrapydd.scheduleutil.add_schedule()
    elif cmd == 'cert':
        scrapydd.ssl_gen.run(argv[2:])
    elif cmd == '--help':
        print_commands(argv)
    elif cmd == '--version' or cmd == '-v':
        print_version()
    else:
        print 'Invalid command.'
        print_commands()

def print_commands():
    print(usage)

def print_version():
    print('scrapydd version:', scrapydd.__version__)

if __name__ == '__main__':
    main()