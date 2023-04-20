ts = ["ከ","አ","ዛ","ው","ን","ት"," ","ማ","ሊ","ያ","ው","ያ","ን"," ","ለ","ሚ","ቀ","ር","ቡ","ላ","ቸ","ው"]

from text_utils import TextCleaner
import pandas as pd
tss = TextCleaner()
tss(ts)
indexes = []
def load_dictionary( path):
        csv = pd.read_csv(path, header=None,keep_default_na=False).values
        word_index_dict = {word: index for word, index in csv}
        return word_index_dict

word_index_dictionary = load_dictionary('word_index_dict.txt')

for char in ts:
    try:
        indexes.append(word_index_dictionary[char])
    except KeyError:
        print(char)
print(word_index_dictionary.keys())