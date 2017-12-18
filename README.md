# Chinese Segment #

- - -

## What is this?

This is a Chinese segmentation tools with GUI which can segment Chinese sentences into words.

Chinese is a language without word boundary.Therefore, Chinese word segmentation is a fundamental task for Chinese Natural Language
Processing(Chinese NLP).Chinese text is different from an alphabetic text,e.g.,an English text,in that it is composed of character strings
from a large character set. Word segmentation aims to promote this advancement to the word level.Only with words being segmented, can other

NLP tasks such as part-of-speech(POS)tagging, syntactic analysis, semantic analysis are made possible.

## How to use?

To run this program, you need to check you python version(we only support python 3.5+). Also a [Tkinter package](http://wiki.python.org/moin/TkInter) is needed.

To run the GUI program, use
`py -3 UI.pyw`

You can input a Chinese text into the input Text then just push the segment button,then the our program will do the sgementation for you.

Or you can choose to segment a file and save the results into an output file.

Also, you can upload your own Lexicon and change the rules of our program.
