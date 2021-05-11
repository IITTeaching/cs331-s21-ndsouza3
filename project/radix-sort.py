import urllib
import requests
class buckets:
  def __init__(self,lst,num):
    #defines a dictionairy container for all items
    self.buckets = {}
    self.emptyBucket = []
    #creates individual buckets for all bytes
    for i in range(0,256):
      self.buckets[i] = []
    #puts item into proper bucket, including if the item has no existing character at the position
    for word in lst:
      if num >= len(word):
        self.emptyBucket.append(word)
      else:
        self.buckets[word[num]].append(word)
    #removes all unused buckets
    keysToCheck = list(self.buckets.keys())
    for key in keysToCheck:
      if self.buckets[key] == []:
        del self.buckets[key]

  def asList(self):
    ans = self.emptyBucket
    for i in self.buckets:
      ans += self.buckets[i].asList()
    return ans

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    return radix(book_to_words(book_url)).asList()
    pass
def radix(str,num=0):
  if len(str) == 0:
    return
  b = buckets(str,num)
  for i in b.buckets:
    b.buckets[i] = radix(b.buckets[i],num + 1)
  return b
