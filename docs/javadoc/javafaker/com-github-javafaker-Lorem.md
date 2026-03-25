Package com.github.javafaker

## Class Lorem

- java.lang.Object

- 

  - com.github.javafaker.Lorem

- 

---

```
public class Lorem
extends java.lang.Object
```

- 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor
Description

`protected `
`Lorem​(Faker faker)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`char`
`character()`
 

`char`
`character​(boolean includeUppercase)`
 

`java.lang.String`
`characters()`
 

`java.lang.String`
`characters​(boolean includeUppercase)`
 

`java.lang.String`
`characters​(int fixedNumberOfCharacters)`
 

`java.lang.String`
`characters​(int fixedNumberOfCharacters,
          boolean includeUppercase)`
 

`java.lang.String`
`characters​(int fixedNumberOfCharacters,
          boolean includeUppercase,
          boolean includeDigit)`
 

`java.lang.String`
`characters​(int minimumLength,
          int maximumLength)`
 

`java.lang.String`
`characters​(int minimumLength,
          int maximumLength,
          boolean includeUppercase)`
 

`java.lang.String`
`characters​(int minimumLength,
          int maximumLength,
          boolean includeUppercase,
          boolean includeDigit)`
 

`java.lang.String`
`fixedString​(int numberOfLetters)`

Create a string with a fixed size.

`java.lang.String`
`paragraph()`
 

`java.lang.String`
`paragraph​(int sentenceCount)`
 

`java.util.List<java.lang.String>`
`paragraphs​(int paragraphCount)`
 

`java.lang.String`
`sentence()`

Create a sentence with a random number of words within the range 4..10.

`java.lang.String`
`sentence​(int wordCount)`

Create a sentence with a random number of words within the range (wordCount+1)..(wordCount+6).

`java.lang.String`
`sentence​(int wordCount,
        int randomWordsToAdd)`

Create a sentence with a random number of words within the range (wordCount+1)..(wordCount+randomWordsToAdd).

`java.util.List<java.lang.String>`
`sentences​(int sentenceCount)`
 

`java.lang.String`
`word()`
 

`java.util.List<java.lang.String>`
`words()`
 

`java.util.List<java.lang.String>`
`words​(int num)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Lorem

```
protected Lorem​(Faker faker)
```

  - 

### Method Detail

    - 

#### character

```
public char character()
```

    - 

#### character

```
public char character​(boolean includeUppercase)
```

    - 

#### characters

```
public java.lang.String characters()
```

    - 

#### characters

```
public java.lang.String characters​(boolean includeUppercase)
```

    - 

#### characters

```
public java.lang.String characters​(int minimumLength,
                                   int maximumLength)
```

    - 

#### characters

```
public java.lang.String characters​(int minimumLength,
                                   int maximumLength,
                                   boolean includeUppercase)
```

    - 

#### characters

```
public java.lang.String characters​(int minimumLength,
                                   int maximumLength,
                                   boolean includeUppercase,
                                   boolean includeDigit)
```

    - 

#### characters

```
public java.lang.String characters​(int fixedNumberOfCharacters)
```

    - 

#### characters

```
public java.lang.String characters​(int fixedNumberOfCharacters,
                                   boolean includeUppercase)
```

    - 

#### characters

```
public java.lang.String characters​(int fixedNumberOfCharacters,
                                   boolean includeUppercase,
                                   boolean includeDigit)
```

    - 

#### words

```
public java.util.List<java.lang.String> words​(int num)
```

    - 

#### words

```
public java.util.List<java.lang.String> words()
```

    - 

#### word

```
public java.lang.String word()
```

    - 

#### sentence

```
public java.lang.String sentence()
```

Create a sentence with a random number of words within the range 4..10.

Returns:
a random sentence

    - 

#### sentence

```
public java.lang.String sentence​(int wordCount)
```

Create a sentence with a random number of words within the range (wordCount+1)..(wordCount+6).

Parameters:
`wordCount` - 
Returns:
a random sentence

    - 

#### sentence

```
public java.lang.String sentence​(int wordCount,
                                 int randomWordsToAdd)
```

Create a sentence with a random number of words within the range (wordCount+1)..(wordCount+randomWordsToAdd).
 
 Set `randomWordsToAdd` to 0 to generate sentences with a fixed number of words.

Parameters:
`wordCount` - 
`randomWordsToAdd` - 
Returns:
a random sentence

    - 

#### sentences

```
public java.util.List<java.lang.String> sentences​(int sentenceCount)
```

    - 

#### paragraph

```
public java.lang.String paragraph​(int sentenceCount)
```

    - 

#### paragraph

```
public java.lang.String paragraph()
```

    - 

#### paragraphs

```
public java.util.List<java.lang.String> paragraphs​(int paragraphCount)
```

    - 

#### fixedString

```
public java.lang.String fixedString​(int numberOfLetters)
```

Create a string with a fixed size. Can be useful for testing
 validator based on length string for example

Parameters:
`numberOfLetters` - size of the expected String
Returns:
a string with a fixed size