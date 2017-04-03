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
    def cli(self, save=None):
        # get mem net
        import memorynetwork

        # build
        model = memorynetwork.MemNet(save)


# executable
if __name__ == '__main__':

    # get fire
    from fire import Fire

    # run
    Fire(ChatBot())
