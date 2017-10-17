import glob
import os

from .jnas_metadata import JnasMetadataList


def _get_paths(jnas_dir):
    return frozenset(glob.iglob(os.path.join(jnas_dir, '*/*/*/*.wav')))


def load_from_paths(jnas_paths):
    return JnasMetadataList.create(jnas_paths)


def load_from_directory(jnas_directory_path):
    paths = _get_paths(jnas_directory_path)
    return load_from_paths(paths)
