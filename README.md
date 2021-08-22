Synonymizer
====================

Spice Up Your Sentences, Make Them Incomprehensible!
---------------------

A program that replaces all words in a given text with synonyms.

Allows certain words like "a" and "it" from being converted due to abbreviations.
Currently does not use context to determine synonym choice.
Whether this is a feature or flaw depends greatly on what the user wants to accomplish.
I personally love using this to make silly sentences, so the latter is preferred.
There is also an antonym mode where it attempts to find an antonym for every word in the sentence.
This is typically more successful due to less options being available to choose from.

Works with manual inputs, .txt files. or .docx files. Inclusion of other file types may be considered in the future.

[EXE Download](https://sourceforge.net/projects/synonymizer/files/ThesaurusPlusSetup.exe/download)

Windows will likely complain about it being a virus (fair enough).
I suggest whitelisting the installer and the program folder once installed.

However, if you don't like that, feel free to build yourself by running "fbs installer" in the consol of the root directory.
The installer exe will appear in a folder called target.
If you just want to run the gui, you can also just do "fbs run" in the consol of the root directory to start the gui.
<br/><br/>

#### Lesson's Learned
- Do everything using the venv created by PyCharm, it is much easier
- You must use python 3.5 or 3.6 when using the non-payed version of fbs
<br/><br/>

#### Links useful during dev:
https://doc.qt.io/qt-5/qmlfirststeps.html <br/>
https://github.com/mherrmann/fbs-tutorial <br/>
https://nsis.sourceforge.io/Main_Page <br/>
