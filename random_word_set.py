#------------------------------------------------------------------
# There is a list of words in http://learncodethehardway.org/words.txt
# Give tne number of words from user input and make a list of random
# words from the site.
#--------------------------------------------------------------------

from urllib import urlopen #to download information from web
import random 

WORD_URL = "http://learncodethehardway.org/words.txt"
words = []
 
for w in urlopen(WORD_URL).readlines():
  words.append(w.strip())

user_word_count = int(raw_input("Enter a number > "))

while not user_word_count in range(1, len(words) + 1):
  user_word_count = int(raw_input("> "))

result = random.sample(words, user_word_count)
print result
random.shuffle(result)

print "Your list of words are: ", result



















