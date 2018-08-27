"""Example main method."""
from argparse import ArgumentParser
import logging

logger = logging.getLogger(__name__)


def logging_conf(logger, debug=False, verbose=False):
    level = logging.DEBUG if debug else logging.INFO

    if verbose:
        from logging import StreamHandler
        handler = StreamHandler()
        handler.setLevel(level)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger


def get_args():
    parser = ArgumentParser('example project')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def main():
    args = get_args()
    logging_conf(logger, args.debug, args.verbose)
    logger.info('Hello world!')
    logger.debug('Hey! you use debug param!')
    print('If you don\'t see logger messages try to execute with -dv params')
