import os
from collections import UserList
from itertools import groupby
from typing import NamedTuple, List


class JnasText(NamedTuple):
    words: List[str]
    type: str  # KANJI or KATAKANA or ROMAJI
    unmarked: bool
    news_or_atr: str  # N or B
    sen_id: str  # three-character or 01-53
    subset: str  # A-J or 001-150 or P01-P05

    @property
    def text(self):
        return ''.join(self.words)

    @property
    def text_with_space(self):
        return ' '.join(self.words)


class JnasTextList(UserList):
    @staticmethod
    def create(paths):
        metas = []
        for path in paths:
            path_parts = path.split('/')
            news_or_atr = 'N' if path_parts[-2][:2] == 'NP' else 'B'
            for line in open(path).read().splitlines():
                line_parts = line.split(' ')

                if news_or_atr == 'N':
                    words = line_parts[3:]
                    sen_id = line_parts[0]
                else:
                    words = line_parts[1:]
                    sen_id = line_parts[0][1:3]

                meta = JnasText(
                    words=words,
                    type=path_parts[-3],
                    unmarked='unmarked' in path_parts[-2],
                    news_or_atr=news_or_atr,
                    sen_id=sen_id,
                    subset=path_parts[-1].split('_')[0],
                )
                metas.append(meta)
        return JnasTextList(metas)

    def _subset(self, attribute, obj):
        return JnasTextList(filter(lambda d: getattr(d, attribute) == obj, self))

    def _subsets(self, attribute):
        key = lambda d: getattr(d, attribute)
        return {
            key: JnasTextList(value)
            for key, value in groupby(JnasTextList(sorted(self, key=key)), key)
        }
