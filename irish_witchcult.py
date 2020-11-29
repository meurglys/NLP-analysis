from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text of choice here
text = open("Irish Witchcraft and Demonology by St. John D. Seymour.txt", encoding="utf-8").read().lower()

# sentence and word tokenize text here
tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenized sentence here
tokenized_sentence = tokenized_text[15]
#print("tokenized text: " + str(tokenized_sentence))

# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = []

# create a for loop through each word tokenized sentence here
for i in tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(i))
  
# store and print any part-of-speech tagged sentence here
pos_tagged_sentence = pos_tagged_text[15]
#print("part-of-speech text: " + str(pos_tagged_sentence))

# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = []
vp_chunked_text = []

# create a for loop through each pos-tagged sentence here
for i in pos_tagged_text:
  # chunk each sentence and append to lists here
  np_chunked_text.append(np_chunk_parser.parse(i))
  vp_chunked_text.append(vp_chunk_parser.parse(i))

# store and print the most common NP-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)

# store and print the most common VP-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
