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


# classes
class ChatBot(object):
    """Interface to be used with fire module."""
    def qa(self, save=None):
        # get mem net
        import memorynetwork as memnet

        # check save val
        save = True if save is not None else False
        if save:
            print memnet.colortxt('Model will be saved', 'red')

        # build
        model = memnet.MemNet(save)


# executable
if __name__ == '__main__':

    # get fire
    from fire import Fire

    # run
    Fire(ChatBot())
