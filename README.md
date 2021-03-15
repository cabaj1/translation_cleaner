# translation_cleaner
Python / shell script to clean up json translation files. It searches the whole project on your keys and clean them.

## Limits

* The script is only tested on json files where the json file only has unique keys and their translations like
```
{
  "madeby": "mds",
  "country": "Belgium",
  "pythonExperience": "starter",
  ...
}
```
* The script does not detect string interpolation
* The script does not detect the difference between code and key references (like key 'Save' and the method onSave(), it will see it is a found key)
* The script does not detect being part of a larger keyname (like 'translation' and 'translation_cleaner', translation is part of translation_cleaner so it is a found key)
* The script needs a shell environment.

## How to run

1) Clone repository
2) Open ReplaceAll.py and on line 6. Set your own path to your own translation.json file.
3) Do the same for ReplaceSelected.py but this time on line 10.
4) Open RemoveUnusedTranslationKeys.sh. On line 1, set your path to the project you want it to run through.
5) Save the files
6) Run ReplaceAll.py
7) Manually double check to confirm that they can indeed be deleted
8) Replace your translation file with output.json and rename output.json
