from collections import UserList
from dataclasses import dataclass
from itertools import groupby
from typing import List


@dataclass
class JnasText:
    words: List[str]
    type: str  # KANJI or KATAKANA or ROMAJI
    unmarked: bool
    news_or_atr: str  # N or B
    sex: str  # M or F
    text_id: str  # 001-150 or P01-P05
    sen_id: str  # three-character or 01-53
    post: str  # None or A or B
    subset: str  # None or A-J

    @property
    def text(self):
        return "".join(self.words)

    @property
    def text_with_space(self):
        return " ".join(self.words)

    @property
    def sp_code(self):
        return self.sex + self.text_id + self.post


class JnasTextList(UserList):
    @staticmethod
    def create(paths):
        metas = []
        for path in paths:
            path_parts = path.split("/")
            news_or_atr = "N" if path_parts[-2][:2] == "NP" else "B"
            for line in open(path).read().splitlines():
                line_parts = line.split(" ")

                if path_parts[-4] == "OriginalText":
                    if news_or_atr == "N":
                        words = line_parts[3:]
                        sen_id = line_parts[0]
                        text_id = path_parts[-1].split("_")[0]
                        subset = ""
                    else:
                        words = line_parts[1:]
                        sen_id = line_parts[0][1:3]
                        subset = path_parts[-1].split("_")[0]
                        text_id = ""
                    sex = ""
                    post = ""
                else:
                    words = line_parts[1:]
                    name = line_parts[0]
                    sex = name[1]
                    text_id = name[2:5]
                    post = name[5:-3]
                    if news_or_atr == "N":
                        subset = ""
                        sen_id = name[-3:]
                    else:
                        subset = name[-3]
                        sen_id = name[-2:]

                meta = JnasText(
                    words=words,
                    type=path_parts[-3],
                    unmarked="unmarked" in path_parts[-2],
                    sex=sex,
                    text_id=text_id,
                    news_or_atr=news_or_atr,
                    sen_id=sen_id,
                    post=post,
                    subset=subset,
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

    def subset_type(self, obj):
        return self._subset("type", obj)

    def subset_unmarked(self, obj):
        return self._subset("unmarked", obj)

    def subset_news_or_atr(self, obj):
        return self._subset("news_or_atr", obj)

    def subset_sex(self, obj):
        return self._subset("sex", obj)

    def subset_text_id(self, obj):
        return self._subset("text_id", obj)

    def subset_sen_id(self, obj):
        return self._subset("sen_id", obj)

    def subset_post(self, obj):
        return self._subset("post", obj)

    def subset_subset(self, obj):
        return self._subset("subset", obj)

    def subsets_type(self):
        return self._subsets("type")

    def subsets_unmarked(self):
        return self._subsets("unmarked")

    def subsets_news_or_atr(self):
        return self._subsets("news_or_atr")

    def subsets_sex(self):
        return self._subsets("sex")

    def subsets_text_id(self):
        return self._subsets("text_id")

    def subsets_sen_id(self):
        return self._subsets("sen_id")

    def subsets_post(self):
        return self._subsets("post")

    def subsets_subset(self):
        return self._subsets("subset")
