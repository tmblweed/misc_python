#given two words in a list, find the shortest distance between them

list_of_words = ["the", "quick", "brown", "fox", "quick"]
word_dictionary = dict()
value_list = []

#create a diconary of key value pairs, where the key is the word and the value is position of the word
for key,value in enumerate(list_of_words):
	word_dictionary.setdefault(value, []).append(key)


#get the position of the word you're looking for
val1 = word_dictionary.get("quick")
val2 = word_dictionary.get("fox")

#check to see if the word appears more than once 
if len(val1) == 1:
	print abs(val1[0] - val2[0])
else:
	for i in range(len(val1)): 	#if the word apears more than once, add the distances to a list
		value_list.append(abs(val1[i]-val2[0]))
		

shortest_dist = sorted(value_lis) #sort the list and grab the first one, that will be the shortest 
print shortest_dist[0]
