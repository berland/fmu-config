# -*- coding: utf-8 -*-
"""Script for converting the global config to various flavours of suiteble
flavours."""

from __future__ import division, print_function, absolute_import

import argparse
import sys
import os.path

import fmu.config as fmu_config

from fmu.config import _version

__version__ = _version.get_versions()['version']


def _do_parse_args(args):

    if args is None:
        args = sys.argv[1:]
    else:
        args = args

    usetxt = 'fmuconfig ... '

    parser = argparse.ArgumentParser(
        description='Configure from FMU global master',
        usage=usetxt
    )

    # positional:
    parser.add_argument('config',
                        type=str,
                        help=('Input global config master file name '
                              'on YAML format'))

    parser.add_argument('--mode',
                        dest='mode',
                        default='ipl',
                        type=str,
                        help='Mode for conversion: "ipl" etc...')

    parser.add_argument('--rootname',
                        dest='rootname',
                        default='global_variables',
                        type=str,
                        help='Root of file name')

    parser.add_argument('--destination',
                        dest='destination',
                        type=str,
                        help='Destination folder (for actual values)')

    parser.add_argument('--template',
                        dest='template',
                        type=str,
                        help='Template folder (for files with <xxxx> values)')

    parser.add_argument('--tool',
                        dest='tool',
                        default='rms',
                        type=str,
                        help='Tool section to apply, e.g. rms or eclipse')

    if len(args) < 2:
        parser.print_help()
        print('QUIT')
        raise SystemExit

    args = parser.parse_args(args)
    return args


def main(args=None):
    """The fmuconfigrunner is a script that takes ..."""

    args = _do_parse_args(args)

    cfg = fmu_config.ConfigParserFMU()

    print('OK {}'.format(cfg))

    if isinstance(args.config, str):
        if not os.path.isfile(args.config):
            raise IOError('Input file does not exist')
        cfg.parse(args.config)

    if args.mode == 'ipl':
        print('Mode is IPL')
        cfg.to_ipl(rootname=args.rootname, destination=args.destination,
                   template=args.template, tool=args.tool)

    if args.mode == 'yaml':
        print('Mode is YAML')
        cfg.to_yaml(rootname=args.rootname, destination=args.destination,
                    template=args.template, tool=args.tool)


if __name__ == '__main__':
    main()