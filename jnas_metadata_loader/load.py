import glob
import os

from jnas_metadata_loader.jnas_metadata import JnasMetadataList
from jnas_metadata_loader.jnas_text import JnasTextList


def load_from_paths(jnas_paths):
    return JnasMetadataList.create(jnas_paths)


def load_from_directory(jnas_directory_path):
    paths = frozenset(glob.iglob(os.path.join(jnas_directory_path, '*/*/*/*.wav')))
    return load_from_paths(paths)


def load_original_text_from_paths(text_paths):
    return JnasTextList.create(text_paths)


def load_original_text_from_directory(jnas_directory_path):
    paths = frozenset(glob.iglob(os.path.join(jnas_directory_path, 'OriginalText/*/*/*.txt')))
    return load_original_text_from_paths(paths)
