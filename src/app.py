import logging

from pythontools.utilities import CustomLogger

my_logger = CustomLogger('my_logger', logging.DEBUG)


def main():
    my_logger.debug('HI')
    my_logger.info("Hello")
    my_logger.error("Help")


if __name__ == '__main__':
    main()
