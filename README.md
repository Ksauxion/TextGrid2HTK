# TextGrid2HTK
A script that converts TextGrid files to HTK format (lab or Audacity txt)

## Requirements
----------------------
You'll need praat-textgrids to run this script.
You can install it by running
```
pip install praat-textgrids
```
or
```
pip install -r requirements.txt
```

## How to use?
----------------------
This script converts all TextGrid files in current directory and subdirectories to HTK format.
You can run it by using
```
python TextGrid2HTK.py [-h] [-t [TIER]] [-f [FORMAT]] [-c CONVERTER] [-cl] [-l]
```
where
```-h``` is help.__
```-t``` or ```--tier```is tier you want to export. Default is ```phones```.<br >
```-f``` or ```--format```is export format (lab or txt). Default is ```lab```.<br >
```-c``` or ```--converter```is converter. There's one built-in called ```sil_and_br```, which converts pauses and breaths to HTK format. You can specify the converter file, which is text document where entries and its replacements are separated by comma. You can see and example in ```converter_example.txt```. Default is ```None```.<br >
```-cl``` or ```--clean```is cleaner. It cleans numbers from source entries. Default is ```False```.<br >
```-l``` or ```--low```is lower capitalization function. Default is ```False```.<br >
