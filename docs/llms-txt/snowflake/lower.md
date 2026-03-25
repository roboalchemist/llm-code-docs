# Source: https://docs.snowflake.com/en/sql-reference/functions/lower.md

Categories:
:   [String & binary functions](../functions-string.md) (Case Conversion)

# LOWER

Returns the input string with all characters converted to lowercase.

## Syntax

```sqlsyntax
LOWER( <expr> )
```

## Arguments

`expr`
:   The string expression.

## Returns

This function returns a value of type VARCHAR.

## Examples

Convert strings in several different languages and character sets to lowercase:

```sqlexample
SELECT v, LOWER(v) FROM lu;
```

```output
+----------------------------------+----------------------------------+
|                v                 |             lower(v)             |
+----------------------------------+----------------------------------+
|                                  |                                  |
| The Quick Gray Fox               | the quick gray fox               |
| LAUGHING ALL THE WAY             | laughing all the way             |
| OVER the River 2 Times           | over the river 2 times           |
| UuVvWwXxYyZz                     | uuvvwwxxyyzz                     |
| ÁáÄäÉéÍíÓóÔôÚúÝý                 | ááääééííóóôôúúýý                 |
| ÄäÖößÜü                          | ääöößüü                          |
| ÉéÀàÈèÙùÂâÊêÎîÔôÛûËëÏïÜüŸÿÇçŒœÆæ | ééààèèùùââêêîîôôûûëëïïüüÿÿççœœææ |
| ĄąĆćĘęŁłŃńÓóŚśŹźŻż               | ąąććęęłłńńóóśśźźżż               |
| ČčĎďĹĺĽľŇňŔŕŠšŤťŽž               | ččďďĺĺľľňňŕŕššťťžž               |
| АаБбВвГгДдЕеЁёЖжЗзИиЙй           | ааббввггддееёёжжззиийй           |
| КкЛлМмНнОоПпРрСсТтУуФф           | ккллммннооппррссттууфф           |
| ХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя           | ххццччшшщщъъыыььээююяя           |
| [NULL]                           | [NULL]                           |
+----------------------------------+----------------------------------+
```

LOWER supports [collation](../collation.md) specifications. This LOWER example
specifies collation with the `tr` (Turkish) locale:

```sqlexample
SELECT LOWER('I' COLLATE 'tr');
```

```output
+-------------------------+
| LOWER('I' COLLATE 'TR') |
|-------------------------|
| ı                       |
+-------------------------+
```
