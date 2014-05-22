#------------------------------------------------------------------
# There is a list of words in http://learncodethehardway.org/words.txt
# Give tne number of words from user input and make a list of random
# words from the site.
#--------------------------------------------------------------------

from urllib import urlopen #to download information from web
import random 

def wordset(user_word_count):

  WORD_URL = "http://learncodethehardway.org/words.txt"
  words = []
 
  for w in urlopen(WORD_URL).readlines():
    words.append(w.strip())

  result = random.sample(words, user_word_count)
  random.shuffle(result)

  return result




















