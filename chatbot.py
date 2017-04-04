#!/usr/bin/env python

"""
Author: John D. Anderson
Email: jander43@vols.utk.edu
Description:
    A simple command line interface (CLI) chatbot written with keras and fire.
Usage:
    chatbot cli
    chatbot help
"""

# libs
import getpass
import memorynetwork as memnet

# globals
USERNAME = getpass.getuser()
MACHINE = 'chatbot'
PROMPT = memnet.colortxt('{0}@{1}: '.format(USERNAME, MACHINE))
HALTING = memnet.colortxt('\nShutting down chatbot ...', 'red')


# classes
class ChatBot(object):
    """Interface to be used with fire module."""
    def __init__(self):
        # cache model
        self.model = None

    def qa(self, save=None):
        # check save val
        save = True if save is not None else False
        if save:
            print memnet.colortxt('Model will be saved', 'red')

        # build
        self.model = memnet.MemNet(save)

        # run cli
        self._chatbot_cli()

    def _chatbot_cli(self):
        """Run interactive prompt."""
        # start loop
        while 1:
            # get question
            try:
                question = raw_input(PROMPT)

            except EOFError:
                memnet.sys.exit(HALTING)

            except KeyboardInterrupt:
                print '\n'
                continue


# executable
if __name__ == '__main__':

    # get fire
    from fire import Fire

    # run
    Fire(ChatBot())
