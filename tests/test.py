import json
import os
import unittest

from jnas_metadata_loader import load_from_paths


class Test(unittest.TestCase):
    def test_all_path(self):
        paths = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'wav_paths.json')))
        jnas_list = load_from_paths(paths)

        text_id_list = ['{:03d}'.format(i + 1) for i in range(150)] + \
                       ['P{:02d}'.format(i + 1) for i in range(5)] + \
                       ['{:03d}{}'.format(i, ab) for i in [139, 140, 141, 142, 143, 144, 145, 146] for ab in 'AB']

        sen_id_list = ['{:02d}'.format(i + 1) for i in range(53)] + \
                      ['{:03d}'.format(i + 1) for i in range(200)]

        sp_code_list = [sex + text_id for sex in 'MF' for text_id in text_id_list]

        for jnas in jnas_list:
            assert jnas.news_or_atr in ['N', 'B'], str(jnas)
            assert jnas.sex in ['M', 'F'], str(jnas)
            assert jnas.mic in ['HS', 'DT'], str(jnas)
            assert jnas.text_id in text_id_list, str(jnas)
            assert jnas.sen_id in sen_id_list, str(jnas)
            assert jnas.subset in ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], str(jnas)
            assert jnas.sp_code in sp_code_list, str(jnas)


if __name__ == '__main__':
    unittest.main()
