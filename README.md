This is the (unofficial) library for loading [JNAS](http://research.nii.ac.jp/src/JNAS.html) metadata.

## Install

```bash
pip install git+https://github.com/Hiroshiba/jnas_metadata_loader
```

## Usage

```python
from jnas_metadata_loader import load_from_directory

path_to_jnas = "/path/to/JNAS"
metadatas = load_from_directory(path_to_jnas)

print(metadatas[0])
# JnasMetadata(path='/path/to/JNAS/WAVES_HS/F051/NP/NF051067_HS.wav', news_or_atr='N', sex='F', text_id='051', sen_id='067', mic='HS', subset='')
```

## Tips
You can get subsets easily like this:

```python
# get the subsets that are from speaker 'M001'
m001_metadatas = metadatas.subset_sp_code('M001')

print(m001_metadatas[0])
# JnasMetadata(path='/path/to/JNAS/WAVES_DT/M001/PB/BM001A10_DT.wav', news_or_atr='B', sex='M', text_id='001', sen_id='10', mic='DT', subset='A')
```

## License

MIT License, see [LICENSE](./LICENSE).
