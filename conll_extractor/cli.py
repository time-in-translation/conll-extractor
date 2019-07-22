# -*- coding: utf-8 -*-

import click

from .indefinites.extract import process_single as process_indefinites
from .prepositions.extract import process_single as process_prepositions
from .core.utils import convert_filename


# Extractor types
INDEFINITES = 'indefinites'
PREPOSITIONS = 'prepositions'


@click.command()
@click.argument('extractor', type=click.Choice([INDEFINITES, PREPOSITIONS]))
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--contracted', is_flag=True,
              help='Whether to extract contracted (e.g. ins Auto) or uncontracted (e.g. in das Auto) PPs.')
@click.option('--filter_pps', is_flag=True,
              help='Whether to filter the PPs based on a list of preposition-noun combinations.')
def cli(extractor, files, contracted=False, filter_pps=False):
    resulting_extractor = None
    kwargs = dict()
    if extractor == INDEFINITES:
        resulting_extractor = process_indefinites
    elif extractor == PREPOSITIONS:
        resulting_extractor = process_prepositions
        kwargs['contracted'] = contracted
        kwargs['filter_pps'] = filter_pps

    if not resulting_extractor:
        raise click.ClickException('Unknown extractor type')
    if not files:
        raise click.BadArgumentUsage('No files provided')

    for in_file in files:
        click.echo('Extracting {} from {}...'.format(extractor, in_file))
        out_file = convert_filename(in_file)
        resulting_extractor(in_file, out_file, **kwargs)

    click.echo('Finished!')


if __name__ == '__main__':
    cli()
