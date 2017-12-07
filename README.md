# Datasets for character-level RNN training
This repository includes four datasets that can be used to train and evaluate character-level (RNN-based) language models.
The datasets are very diverse and should cover a wide range of linguistic characteristics.

If you use any of these datasets in your research, please cite:
> De Boom C., Demeester T., Dhoedt B.: "Character-level Recurrent Neural Networks in Practice: Comparing Training and Sampling Schemes". Neural Computing and Applications (2018). To appear.

## Dataset details
* __English__: we compiled all plays by William Shakespeare from Project Gutenberg in one dataset. The plays follow each other in random order. The total number of characters is 6,347,705 with 85 unique characters.
* __Finnish__: the Finnish language is very different from English. We gathered all texts from Finnish playwrights Juhani Aho and Eino Leino through Project Gutenberg. This results in a dataset of 10,976,530 characters, of which 106 are unique.
* __Linux__: we saved all C code from the Linux kernel (see <http://github.com/torvalds/linux/tree/master/kernel>) and gathered the files together. On November 22 2016, the entire kernel contained 6,546,665 characters, and 97 of them are unique.
* __Music__: we created this dataset by extracting music notes from MIDI files. When notes are played simultaneously in the MIDI file, we extract them from low to high, so that we obtain a single sequence of subsequent notes. We downloaded all piano compositions by Bach, Beethoven, Chopin and Haydn from Classical Archives, removed duplicate compositions, and gathered a dataset of 1,553,852 notes, of which there are 90 unique ones.
