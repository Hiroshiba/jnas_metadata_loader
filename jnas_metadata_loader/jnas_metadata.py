import os
from collections import UserList
from itertools import groupby
from typing import NamedTuple


class JnasMetadata(NamedTuple):
    path: str
    news_or_atr: str  # N or B
    sex: str  # M or F
    text_id: str  # 001-150 or P01-P05
    sen_id: str  # three-character or 01-53
    mic: str  # HS or DT
    subset: str = ''  # None or A-J

    @property
    def sp_code(self):
        return self.sex + self.text_id


class JnasMetadataList(UserList):
    @staticmethod
    def create(paths):
        metas = []
        for path in paths:
            filename = os.path.splitext(path.split('/')[-1])[0]
            news_or_atr = filename[0]
            if news_or_atr == 'N':
                meta = JnasMetadata(
                    path=path,
                    news_or_atr=news_or_atr,
                    sex=filename[1],
                    text_id=filename[2:-6],
                    sen_id=filename[-6:-3],
                    mic=filename[-2:],
                )
            elif news_or_atr == 'B':
                meta = JnasMetadata(
                    path=path,
                    news_or_atr=news_or_atr,
                    sex=filename[1],
                    text_id=filename[2:-6],
                    subset=filename[-6],
                    sen_id=filename[-5:-3],
                    mic=filename[-2:],
                )
            else:
                raise ValueError('unkown metadata: ' + path)
            metas.append(meta)
        return JnasMetadataList(metas)

    def _subset(self, attribute, obj):
        return JnasMetadataList(filter(lambda d: getattr(d, attribute) == obj, self))

    def _subsets(self, attribute):
        key = lambda d: getattr(d, attribute)
        return {
            key: JnasMetadataList(value)
            for key, value in groupby(JnasMetadataList(sorted(self, key=key)), key)
        }

    def subset_news_or_atr(self, obj):
        return self._subset('news_or_atr', obj)

    def subset_sex(self, obj):
        return self._subset('sex', obj)

    def subset_text_id(self, obj):
        return self._subset('text_id', obj)

    def subset_sen_id(self, obj):
        return self._subset('sen_id', obj)

    def subset_mic(self, obj):
        return self._subset('mic', obj)

    def subset_subset(self, obj):
        return self._subset('subset', obj)

    def subset_sp_code(self, obj):
        return self._subset('sp_code', obj)

    def subsets_news_or_atr(self):
        return self._subsets('news_or_atr')

    def subsets_sex(self):
        return self._subsets('sex')

    def subsets_text_id(self):
        return self._subsets('text_id')

    def subsets_sen_id(self):
        return self._subsets('sen_id')

    def subsets_mic(self):
        return self._subsets('mic')

    def subsets_subset(self):
        return self._subsets('subset')

    def subsets_sp_code(self):
        return self._subsets('sp_code')
