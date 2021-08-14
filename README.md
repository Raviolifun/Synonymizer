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

Works with manual inputs or .txt files. Inclusion of other file types may be considered in the future.
Additionally, I plan to add a picking mode for how well the synonym matches in context, but this is far down the line.

Current development is going towards a gui interface in qt with fbs as a installer.
<br/><br/>

#### Lesson's Learned
- Do everything using the venv created by PyCharm, it is much easier
- You must use python 3.5 or 3.6 when using the non-payed version of fbs
<br/><br/>

#### Links useful during dev:
https://doc.qt.io/qt-5/qmlfirststeps.html <br/>
https://github.com/mherrmann/fbs-tutorial <br/>
https://nsis.sourceforge.io/Main_Page <br/>
