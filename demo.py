"""
Demo script: dataset loading
"""

__author__  = "Cedric De Boom"
__date__    = "2017 December 7th"


# All datasets represented as a string
DATASETS = ['finnish', 'linux', 'music', 'shakespeare']

# Select the dataset, e.g. 'finnish'
dataset = DATASETS[0]

# Process the characters
data = open('datasets/' + dataset + '.txt', 'r').readlines()
if dataset != 'music':
    data = ''.join(data)
    chars = list(set(data))
else:
    data = [list(x.strip().split(' ') + ['\n']) for x in data]
    data = [item for sublist in data for item in sublist]
    chars = list(set(data))

# Calculate dataset and vocabulary size
data_size, vocab_size = len(data), len(chars)
print ('Vocabulary size = ' + str(vocab_size) + '; total data size = ' + str(data_size))

# Create dictionaries to map from and to character:token_index
# These dictionaries can be used during training and sampling
char_to_ix = { ch:i for i,ch in enumerate(chars) }
ix_to_char = { i:ch for i,ch in enumerate(chars) }
