# -*- coding: utf-8 -*-

import click

from .indefinites.extract import process_single
from .prepositions.extract import process_single
from .core.utils import convert_filename


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--needs_determiner', is_flag=True)
@click.option('--filter_prepositions', is_flag=True)
def cli(files, needs_determiner=False, filter_prepositions=False):
    for in_file in files:
        out_file = convert_filename(in_file)
        process_single(in_file, out_file, needs_determiner=needs_determiner, filter_prepositions=filter_prepositions)


if __name__ == '__main__':
    cli()
