import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
    """
    This method should sort input list lst of elements of some type T.

    Elements of the list are compared using function compare that takes two
    elements of type T as input and returns -1 if the left is smaller than the
    right element, 1 if the left is larger than the right, and 0 if the two
    elements are equal.
    """
    nlst = []
    for i in lst:
        for newIndex in range(len(nlst)):
            if compare(i,nlst[newIndex]) == -1:
                nlst.insert(newIndex,i)
                break
            elif newIndex == len(nlst) - 1:
                nlst.append(i)
        if len(nlst) == 0:
            nlst.append(i)
    return nlst

def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    """
    This method search for elem in lst using binary search.

    The elements of lst are compared using function compare. Returns the
    position of the first (leftmost) match for elem in lst. If elem does not
    exist in lst, then return -1.
    """
    upper = len(lst) - 1
    lower = 0
    while upper >= lower:
        i = ((upper + lower) // 2)
        if compare(lst[i],elem) == 1:
            upper = i - 1
        elif compare(lst[i],elem) == -1:
            lower = i + 1
        elif compare(lst[i],elem) == 0:
            while (i > 0 and compare(lst[i],elem) == 0):
              i-= 1
            return i + 1
    return -1;
    pass

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():

    def __init__(self, document, k):
        """
        Initializes a prefix searcher using a document and a maximum
        search string length k.
        """
        self.lst = []
        self.k = k
        for i in range(len(document)):
            if (i+k >= len(document)):
                self.lst.append(document[i:len(document)])
            else:
                self.lst.append(document[i:i+k])
        strcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
        self.lst = mysort(self.lst,strcmp)
        pass

    def search(self, q):
        """
        Return true if the document contains search string q (of

        length up to n). If q is longer than n, then raise an
        Exception.
        """
        nLst = []
        for i in self.lst:
            if len(i) >= len(q):
                nLst.append(i[0:len(q)])
        strcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
        if len(q) > self.k:
            raise Exception("string too long")
        return mybinsearch(nLst, q, strcmp) != -1
        pass

# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():

    def __init__(self, document: str):
        """
        Creates a suffix array for document (a string).
        """
        self.document = document
        self.suffixArray = list(range(0,len(document)-1))
        suffixCompare = lambda x,y: 1 if self.document[x:] > self.document[y:] else(-1 if self.document[x:] < self.document[y:] else 0)
        self.suffixArray = mysort(self.suffixArray,suffixCompare)
        pass


    def positions(self, searchstr: str):
        """
        Returns all the positions of searchstr in the documented indexed by the suffix array.
        """
        newSuffix = []
        for i in self.suffixArray:
          if not (len(self.document[i:]) >= len(searchstr)):
            newSuffix.append(i)

        suffixCompare = lambda x,y: 1 if(self.document[x:x+len(searchstr)] > y) else(-1 if self.document[x:x+len(searchstr)] < y else 0)

        return [mybinsearch(self.suffixArray, searchstr,suffixCompare)]
        pass

    def contains(self, searchstr: str):
        """
        Returns true if searchstr is contained in document.
        """
        return self.positions(searchstr) != [-1]
        pass

# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby-Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
<<<<<<< HEAD
<<<<<<< HEAD
    pos = s.positions("Moby Dick")
    posset = set(pos)
    tc.assertTrue(posset == {427} or posset == {427,428}  or posset == {428})
=======
    posset = set(s.positions("Moby-Dick"))
    tc.assertEqual(posset, {355, 356})

>>>>>>> 510e22a975f6dab2cb5e6d567c1e36a37e3e9033
=======
    posset = set(s.positions("Moby-Dick"))
    tc.assertEqual(posset, {355, 356})

>>>>>>> 2573057ee0687ca1d030418a45f8c6166d9a90b2

#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
