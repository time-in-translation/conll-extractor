# -*- coding: utf-8 -*-

import click

from .determiners.extract import process_single as process_determiners
from .nouns.extract import process_single as process_nouns
from .prepositions.extract import process_single as process_prepositions
from .core.constants import DETERMINERS, NOUNS, PREPOSITIONS, DEFINITE, INDEFINITE, NUMBER
from .core.utils import convert_filename


@click.command()
@click.argument('extractor', type=click.Choice([DETERMINERS, NOUNS, PREPOSITIONS]))
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--definiteness', type=click.Choice([DEFINITE, INDEFINITE]),
              help='If set, limit the definiteness of noun phrases to definite or indefinite')
@click.option('--deprel', type=str,
              help='If set, filter based on the dependency relation of the noun.')
@click.option('--number', type=click.Choice(NUMBER),
              help='If set, filter based on the number of the noun.')
@click.option('--contracted', is_flag=True,
              help='Whether to extract contracted (e.g. ins Auto) or uncontracted (e.g. in das Auto) PPs.')
@click.option('--filter_pps', is_flag=True,
              help='Whether to filter the PPs based on a list of preposition-noun combinations.')
def cli(extractor, files, definiteness=None, deprel=None, number=None, contracted=False, filter_pps=False):
    resulting_extractor = None
    kwargs = dict()
    if extractor == DETERMINERS:
        resulting_extractor = process_determiners
        kwargs['definiteness'] = definiteness
    if extractor == NOUNS:
        resulting_extractor = process_nouns
        kwargs['deprel'] = deprel
        kwargs['number'] = number
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
