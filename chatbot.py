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
import os
import sys
import getpass
import termcolor
import memorynetwork as memnet


# funcs
def colortxt(txt, cval='yellow'):
    """Wraps termcolor method."""
    return termcolor.colored(txt, cval)


# classes
class ChatModel(memnet.MemNet):
    """Controller and Interface for MemNet() class."""
    def __init__(self, save, modname='chatbot.h5'):
        # store model
        self.model = None

        # check if model exists
        if os.path.exists(modname):
            print (colortxt('Loading model ...', 'red'))
            # TODO: write code to load model
            return None
        else:
            # prompt user to build model?
            answer = raw_input(colortxt('No model found. Build one? [Y/n]: '))
            if answer == 'Y':
                # warn
                print (colortxt('Building model ...', 'red'))
                # commence building
                self.model = self.build_model(save, modname)
            else:
                # gotta exit
                sys.exit()


class ChatBot(object):
    """Interface to be used with fire module."""
    def __init__(self):
        # cache model
        self._chatbot = None

        # user messages
        self._prompt = colortxt('{0}@chatbot: '.format(getpass.getuser()))
        self._halt = colortxt('\nShutting down chatbot ...', 'red')

    def qa(self, save=None):
        # check save val
        save = True if save is not None else False
        if save:
            print colortxt('Model will be saved', 'red')

        # build
        self._chatbot = ChatModel(save)

        # run cli
        self.chatbot_cli()

    def _chatbot_cli(self):
        """Run interactive prompt."""
        # start loop
        while 1:
            # get question
            try:
                question = raw_input(self._prompt)

            except EOFError:
                sys.exit(self._halt)

            except KeyboardInterrupt:
                print '\n'
                continue


# executable
if __name__ == '__main__':

    # get fire
    from fire import Fire

    # run
    Fire(ChatBot())
