# Source: https://docs.snowflake.com/en/sql-reference/functions/initcap.md

Categories:
:   [String & binary functions](../functions-string.md) (Case Conversion)

# INITCAP

Returns the input string with the first letter of each word in uppercase and the subsequent letters in lowercase.

## Syntax

```sqlsyntax
INITCAP( <expr> [ , '<delimiters>' ] )
```

## Arguments

`expr`
:   The string expression.

`'delimiters'`
:   A string of one or more characters that INITCAP uses as separators for words in the input expression:

    * If `delimiters` isn’t specified, any of the following characters in the input expressions are
      treated as word separators:

      ```output
      <whitespace> ! ? @ " ^ # $ & ~ _ , . : ; + - * % / | \ [ ] ( ) { } < >
      ```
    * If `delimiters` is specified, the specified value overrides all of the characters listed above.

    Supports any UTF-8 characters, including whitespace characters, and is case-sensitive.

    Must be enclosed in single quotes, for example `', '` (delimiters in this example are `,` and blank spaces).

    When specified as an empty string (that is, `''`), INITCAP ignores all delimiters, including whitespace characters,
    in the input expression. The input expression is treated as a single, continuous word. The resulting output is
    a string with the first character capitalized (if the first character is a letter) and all other letters in lowercase.

## Returns

This function returns a value of type VARCHAR.

## Collation details

Arguments with collation specifications currently aren’t supported.

## Examples

This example provides various outputs in different languages using the default delimiters:

```sqlexample
SELECT v, INITCAP(v) FROM testinit;
```

```output
+---------------------------------+---------------------------------+
| C1                              | INITCAP(C1)                     |
|---------------------------------+---------------------------------|
| The Quick Gray Fox              | The Quick Gray Fox              |
| the sky is blue                 | The Sky Is Blue                 |
| OVER the River 2 Times          | Over The River 2 Times          |
| WE CAN HANDLE THIS              | We Can Handle This              |
| HelL0_hi+therE                  | Hell0_Hi+There                  |
| νησί του ποταμού                | Νησί Του Ποταμού                |
| ÄäÖößÜü                         | Ääöößüü                         |
| Hi,are?you!there                | Hi,Are?You!There                |
| to je dobré                     | To Je Dobré                     |
| ÉéÀàè]çÂâ ÊêÎÔô ÛûËÏ ïÜŸÇç ŒœÆæ | Ééààè]Çââ Êêîôô Ûûëï Ïüÿçç Œœææ |
| ĄąĆ ćĘęŁ łŃńÓ óŚśŹźŻż           | Ąąć Ćęęł Łńńó Óśśźźżż           |
| АаБб ВвГгД дЕеЁёЖ жЗзИиЙй       | Аабб Ввггд Дееёёж Жззиийй       |
| ХхЦц ЧчШш ЩщЪъ ЫыЬь ЭэЮ юЯя     | Ххцц Ччшш Щщъъ Ыыьь Ээю Юяя     |
| NULL                            | NULL                            |
+---------------------------------+---------------------------------+
```

These examples specify delimiters using the `delimiters` argument:

```sqlexample
SELECT INITCAP('this is the new Frame+work', '') AS initcap_result;
```

```output
+----------------------------+
| INITCAP_RESULT             |
|----------------------------|
| This is the new frame+work |
+----------------------------+
```

```sqlexample
SELECT INITCAP('iqamqinterestedqinqthisqtopic','q') AS initcap_result;
```

```output
+-------------------------------+
| INITCAP_RESULT                |
|-------------------------------|
| IqAmqInterestedqInqThisqTopic |
+-------------------------------+
```

```sqlexample
SELECT INITCAP('lion☂fRog potato⨊cLoUD', '⨊☂') AS initcap_result;
```

```output
+------------------------+
| INITCAP_RESULT         |
|------------------------|
| Lion☂Frog potato⨊Cloud |
+------------------------+
```

```sqlexample
SELECT INITCAP('apple is僉sweetandballIsROUND', '僉a b') AS initcap_result;
```

```output
+-------------------------------+
| INITCAP_RESULT                |
|-------------------------------|
| aPple Is僉SweetaNdbaLlisround |
+-------------------------------+
```
