# Source: https://code.kx.com/q/learn/python/examples/string/

Title: Q versions of Python string programming examples| Documentation for kdb+ and q

URL Source: https://code.kx.com/q/learn/python/examples/string/

Markdown Content:
String programs[¶](https://code.kx.com/q/learn/python/examples/string/#string-programs "Permanent link")
--------------------------------------------------------------------------------------------------------

From  GeeksforGeeks [Python Programming Examples](https://www.geeksforgeeks.org/python-programming-examples/)

Follow links to the originals for more details on the problem and Python solutions.

[Is string a palindrome?](https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/)[¶](https://code.kx.com/q/learn/python/examples/string/#is-string-a-palindrome "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A string is a palindrome if it matches its reversal.

```
def isPal(str):
    r = range(0, len(str))
    lst = [str[i] for i in r]
    tsl = [str[-(i+1)] for i in r]
    return lst == tsl
```

```
>>> isPal("malayalam")
True
```

```
q){x~reverse x} "malayalam"
1b
```

[Sort characters](https://www.geeksforgeeks.org/sort-string-characters/)[¶](https://code.kx.com/q/learn/python/examples/string/#sort-characters "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> ''.join(sorted('bbccdefbbaa'))
'aabbbbccdef'
```

```
q)asc "bbccdefbbaa"
`s#"aabbbbccdef"
```

[Reverse words in a string](https://www.geeksforgeeks.org/reverse-words-in-a-given-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#reverse-words-in-a-string "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> s = "i like this program very much"

>>> words = s.split(' ')
>>> " ".join([words[-(i+1)] for i in range(0, len(words))])
'much very program this like i'
```

```
q)s: "i like this program very much"

q)" " sv reverse " " vs s
"much very program this like i"
```

Q keywords [`vs`](https://code.kx.com/q/ref/vs/) and [`sv`](https://code.kx.com/q/ref/sv/) split and join strings.

[Remove `i`th character from string](https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/)[¶](https://code.kx.com/q/learn/python/examples/string/#remove-ith-character-from-string "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> s = 'GeeksforGeeks'

>>> "".join([s[i] for i in range(0, len(s)) if i!=2])
'GeksforGeeks'
```

In q, `til count x` returns all the indexes of list `x`.

```
q)s:"GeeksforGeeks"

q)s (til count s) except 2
"GeksforGeeks"
```

[Is string a substring of another?](https://www.geeksforgeeks.org/python-check-substring-present-given-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#is-string-a-substring-of-another "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> s = "geeks for geeks"

>>> s.find('geek')!= -1
True
>>> s.find('goon')!= -1
False
```

In q, the [`like`](https://code.kx.com/q/ref/like/) keyword provides basic pattern matching.

```
q)s:"geeks for geeks"

q)s like "*geek*"
1b
q)s like "*goon*"
0b
```

[Even-length words in a string](https://www.geeksforgeeks.org/python-program-to-print-even-length-words-in-a-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#even-length-words-in-a-string "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> s = "This is a python language"

>>> [wrd for wrd in s.split(" ") if 0 == len(wrd) % 2]
['This', 'is', 'python', 'language']
```

```
q)s: "This is a python language"

q){x where 0=(count each x)mod 2} " " vs s
"This"
"is"
"python"
"language"
```

`" " vs` splits the string into a list of words. In the lambda, `count each x` is a vector of their lengths.

[String contains all the vowels?](https://www.geeksforgeeks.org/python-program-to-accept-the-strings-which-contains-all-vowels/)[¶](https://code.kx.com/q/learn/python/examples/string/#string-contains-all-the-vowels "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> s = 'geeks for geeks'

>>> all(["aeiou"[i] in s.lower() for i in range(0,5)])
False
```

```
q)s: "geeksforgeeks"

q)all "aeiou" in lower s
0b
```

`"aeiou" in` returns a list of flags, which [`all`](https://code.kx.com/q/ref/all-any/) aggregates.

[Count matching characters in two strings](https://www.geeksforgeeks.org/python-count-the-number-of-matching-characters-in-a-pair-of-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#count-matching-characters-in-two-strings "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> str1 = 'aabcddekll12@'
>>> str2 = 'bb22ll@55k'

>>> len(set(str1) & set(str2))
5
```

```
q)str1: "aabcddekll12@"
q)str2: "bb22ll@55k"

q)count distinct str1 inter str2
5
```

In Python `set()` discards duplicate characters from each string. The q `inter` keyword is _list_ intersection, not set intersection; `distinct` discards any duplicates.

[Remove duplicates from a string](https://www.geeksforgeeks.org/remove-duplicates-given-string-python/)[¶](https://code.kx.com/q/learn/python/examples/string/#remove-duplicates-from-a-string "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> "".join(set("geeksforgeeks"))
'krgefso'
```

Q is a vector language. It has a keyword for this.

```
q)distinct "geeksforgeeks"
"geksfor"
```

The q keyword preserves order. The Python solution can be adapted to do the same.

```
>>> from collections import OrderedDict
>>> "".join(OrderedDict.fromkeys("geeksforgeeks"))
'geksfor'
```

[String contains special characters?](https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/)[¶](https://code.kx.com/q/learn/python/examples/string/#string-contains-special-characters "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> sc = '[@_!#$%^&*()<>?/\\|}{~:]'
>>> any([c in sc for c in set("Geeks$for$Geeks")])
True
>>> any([c in sc for c in set("Geeks for Geeks")])
False
```

```
q)sc:"[@_!#$%^&*()<>?/\\|}{~:]"   / special characters
q)any sc in "Geeks$For$Geeks"
1b
q)any sc in "Geeks For Geeks"
0b
```

[Random strings until a given string is generated](https://www.geeksforgeeks.org/python-program-match-string-random-strings-length/)[¶](https://code.kx.com/q/learn/python/examples/string/#random-strings-until-a-given-string-is-generated "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
import string 
import random 
import time 

possibleCharacters = string.ascii_lowercase + string.digits + \
                     string.ascii_uppercase + ' ., !?;:'

# string to be generated 
t = "geek"

attemptThis = ''.join(random.choice(possibleCharacters) 
                                for i in range(len(t))) 
attemptNext = '' 

completed = False
iteration = 0

while completed == False: 
    print(attemptThis) 

    attemptNext = '' 
    completed = True

    # Fix the index if matches with 
    # the strings to be generated 
    for i in range(len(t)): 
        if attemptThis[i] != t[i]: 
            completed = False
            attemptNext += random.choice(possibleCharacters) 
        else: 
            attemptNext += t[i] 

    iteration += 1
    attemptThis = attemptNext 
    time.sleep(0.1) 

print("Target matched after " +
    str(iteration) + " iterations")
```

```
q)show pc:.Q.a,.Q.A,"0123456789 ., !?;:"    / possible characters
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ., !?;:"

q)tryfor:{i:where x<>y; @[y; i; :; count[i]?pc]}
q)s: tryfor["geek";] scan "    "
q)count s                                   / number of iterations
174
```

The binary q function `tryfor` first finds where string `x` varies from `y`, then [replaces](https://code.kx.com/q/ref/amend/ "Amend At operator @") those letters with random picks from `pc`. Projecting `tryfor` onto `"geek"` yields a unary function.

```
q)tryfor["geek";] " e k"
"veIk"
```

Keyword [`scan`](https://code.kx.com/q/ref/over/) applies `tryfor["geek";]` successively until the result stops changing, i.e. it finds a match.

The initial state is a string of blanks. `scan` returns the result of every iteration.

```
q)10 -10#\:s  / first and last 10 results
"    " "Czks" "T3cC" "d,s " "8pyi" ";DDG" "DVmh" "8Xoc" "JI!q" "q.NC"
"geeZ" "geef" "geeo" "gee9" "gee3" "geen" "gee," "geeR" "geeu" "geeN"
```

[Split and join a string](https://www.geeksforgeeks.org/python-program-split-join-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#split-and-join-a-string "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> '-'.join("Geeks for Geeks".split(' '))
'Geeks-for-Geeks'
```

```
q)"-"sv " " vs "Geeks for Geeks"
"Geeks-for-Geeks"
```

[String is a binary?](https://www.geeksforgeeks.org/python-check-if-a-given-string-is-binary-string-or-not/)[¶](https://code.kx.com/q/learn/python/examples/string/#string-is-a-binary "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> all([c in "01" for c in '01010101010'])
True
```

```
q)all "01010101010" in "01"
1b
```

[Uncommon words from two strings](https://www.geeksforgeeks.org/python-program-to-find-uncommon-words-from-two-strings/)[¶](https://code.kx.com/q/learn/python/examples/string/#uncommon-words-from-two-strings "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
import collections
# words that occur once only in string s
def singles(s):
    c = collections.Counter(s.split(' '))
    return[e[0] for e in c.items() if e[1]==1]

def uncommonWords(s1, s2):
    sw1 = singles(s1)
    sw2 = singles(s2)
    return [w for w in sw1+sw2 if not w in set(sw1)&set(sw2)]
```

```
>>> s1 = 'Greek for geeks'
>>> s2 = 'Learning from the the geeks'
>>> uncommonWords(s1, s2)
['Greek', 'for', 'Learning', 'from']
```

```
singles:{
  c:count each group`$" "vs x;
  key[c] where value[c]=1 }

uncommonWords:{
  sx:singles x;
  sy:singles y;
  (sx,sy) except sx inter sy }
```

```
q)s1:"Greek for geeks"
q)s2:"Learning from the the geeks"
q)uncommonWords[s1;s2]
`Greek`for`Learning`from
```

[Permute a string](https://www.geeksforgeeks.org/permutations-of-a-given-string-using-stl/)[¶](https://code.kx.com/q/learn/python/examples/string/#permute-a-string "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
from itertools import permutations 
>>> [''.join(w) for w in permutations('ABC')]
['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
```

```
p:{$[x=2;(0 1;1 0);raze(til x)(rotate')\:(x-1),'.z.s x-1]}
permutations:{x p count x}
```

```
q)permutations "ABC"
"CAB"
"CBA"
"ABC"
"BAC"
"BCA"
"ACB"
```

Function `p` defines permutations of order  recursively. ([`.z.s`](https://code.kx.com/q/ref/dotz/#zs-self) allows a lambda to refer to itself.) `permutations` uses them to index its argument.

```
q)p 2
0 1
1 0
q)p 3
2 0 1
2 1 0
0 1 2
1 0 2
1 2 0
0 2 1
```

Reading Room: [It’s more fun to permute](https://code.kx.com/q/learn/reading/strings/#its-more-fun-to-permute) for a non-recursive algorithm

[URLs from string](https://www.geeksforgeeks.org/python-check-url-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#urls-from-string "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
import re 

def findUrls(string): 
    rx = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(rx, string)
```

```
>>> s = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
>>> findUrls(s)
['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/']
```

```
findUrls:{
  begins:{y~count[y]#x};                            / x begins with y?
  c:(x ss "http")_x;                                / candidate substrings
  c:c where any c begins\:/:("http://";"https://"); / continue as URLs?
  {(x?" ")#x}each c }                               / take each up to space
```

```
q)s: "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/"
q)findUrls s
"https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles"
"http://www.geeksforgeeks.org/"
```

The published Python solution relies on a non-trivial RegEx to match any URL. (It also fails.)

The q solution [looks for](https://code.kx.com/q/ref/ss/ "string search") substring `"http"` and tests candidates to see whether they begin URLs.

Combining the iterators [Each Left and Each Right `\:/:`](https://code.kx.com/q/ref/maps/#each-left-and-each-right) allows us to test each of the candidate substrings in `c` against both `http://` and `https://`.

[Rotate a string](https://www.geeksforgeeks.org/string-slicing-python-rotate-string/)[¶](https://code.kx.com/q/learn/python/examples/string/#rotate-a-string "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`def rotate(s,n): return ''.join([s[(i+n)%len(s)] for i in range(0, len(s))])`

```
>>> rotate("GeeksforGeeks",2)
'eksforGeeksGe'
>>> rotate("GeeksforGeeks",-2)
'ksGeeksforGee'
```

```
q)2 rotate "GeeksforGeeks"
"eksforGeeksGe"
q)-2 rotate "GeeksforGeeks"
"ksGeeksforGee"
```

[Empty string by recursive deletion?](https://www.geeksforgeeks.org/string-slicing-python-check-string-can-become-empty-recursive-deletion/)[¶](https://code.kx.com/q/learn/python/examples/string/#empty-string-by-recursive-deletion "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
def checkEmpty(string, sub): 
    if len(string)== 0: 
        return False
    while (len(string) != 0): 
        index = string.find(sub) 
        if (index ==(-1)): 
            return False
        string = string[0:index] + string[index + len(sub):]            
    return True
```

```
>>> checkEmpty("GEEGEEKSSGEK", "GEEKS")
False
>>> checkEmpty("GEEGEEKSKS", "GEEKS")
True
```

```
q)0=count ssr[;"GEEKS";""] over "GEEGEEKSSGEK"
0b
q)0=count ssr[;"GEEKS";""] over "GEEGEEKSKS"
1b
```

Projected onto two arguments (as `ssr[;"GEEKS";""]`) ternary string-replacement keyword [`ssr`](https://code.kx.com/q/ref/ss/#ssr) is a unary function.

The [`over`](https://code.kx.com/q/ref/over/) keyword applies a unary function successively until the result stops changing.

It remains only to count the characters in the result of the last iteration.

If `over` gives an unexpected result, the matter is usually clarified by replacing it with `scan`, which performs the same computation but returns the result of each iteration.

```
q)ssr[;"GEEKS";""] scan "GEEGEEKSSGEK"
"GEEGEEKSSGEK"
"GEESGEK"
q)ssr[;"GEEKS";""] scan "GEEGEEKSKS"
"GEEGEEKSKS"
"GEEKS"
""
```

[Scrape and find ordered words](https://www.geeksforgeeks.org/scraping-and-finding-ordered-words-in-a-dictionary-using-python/)[¶](https://code.kx.com/q/learn/python/examples/string/#scrape-and-find-ordered-words "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> url = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"
>>> words = requests.get(url).content.decode("utf-8").split()
>>> len(words)
25104
>>> lists = [list(w.lower() for w in words]
>>> ow = [words[i] for i in range(0, len(words)) if lists[i] == sorted(lists[i])]
>>> len(ow)
422
```

```
q)url: "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"
q)words:system"curl ",url
q)count words
25104
q)ow:words where{x~asc x}each lower words
q)count ow
422
```

A q string is just a list of characters and can be sorted as it is.

[Find possible words](https://www.geeksforgeeks.org/possible-words-using-given-characters-python/)[¶](https://code.kx.com/q/learn/python/examples/string/#find-possible-words "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
>>> d = ["go", "bat", "me", "eat", "goal", "boy", "run"]
>>> tray = list("eobamgl")

>>> [w for w in d if all([c in tray for c in w])]
['go', 'me', 'goal']
```

```
q)d:string`go`bat`me`eat`goal`boy`run           / dictionary
q)tray: "eobamgl"

q)d where all each d in\:tray
"go"
"me"
"goal"
```

* * *

[Dictionary examples](https://code.kx.com/q/learn/python/examples/dict/)
