from argparse import ArgumentParser
from re import match
from typing import Text


from we.piple.core.constant import environments , spaces
from we.piple.core.util.configuration_util import SubparserBuilder

@SubparserBuilder
def build_subparsers(subparsers) -> list[ArgumentParser]:
    """
    Build subparser for tasks in this module
    :param subparsers: A subparser object from argparse.ArgumentParser.add_subparsers()
    :return: list of ArgumentParser
    """

    def parse_batch(s: Text) -> Text:
        if match(r'(load|[0-9]{8})' , s):
            return s
        raise ValueError(f"Invalid Batch Format ::: {s}")

    parsers : list[ArgumentParser] = []
    parser: ArgumentParser

    config_help_desc = "Configuration File:"

    task = "we.piple.contact_info.task.raw.ci_autoloader_task"
    parser = subparsers.add_parser(task)
    parser.set_defaults(command=task)
    _CONFIG = "--config"
    _ENV = "--env"
    _SPACE = "--space"
    _BUCKET = "--bucket"
    _CATALOG = "--catalog"
    _BATCH_ID = "--batch-id-column"
    _BATCHES = "--batches"
    parser.add_argument(_CONFIG,help=config_help_desc)
    parser.add_argument('-e', _ENV, choices=environments,required=True , help='Environment')
    parser.add_argument('-p', _SPACE, choices=spaces,required=True , help='Space')
    parser.add_argument('-b', _BUCKET, help='Bucket')
    parser.add_argument('-c', _CATALOG,  help='Catalog')
    parser.add_argument('-I', _BATCH_ID, default='contact_info' , help='Environment')
    parser.add_argument('-n', _BATCHES, type=int , default=1, help='No of batches to load')
    parsers.append(parser)

    return parsers






