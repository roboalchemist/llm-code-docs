# Source: https://docs.snowflake.com/en/sql-reference/functions/upper.md

Categories:
:   [String & binary functions](../functions-string.md) (Case Conversion)

# UPPER

Returns the input string with all characters converted to uppercase.

## Syntax

```sqlsyntax
UPPER( <expr> )
```

## Arguments

`expr`
:   The string expression.

## Returns

This function returns a value of type VARCHAR.

## Examples

```sqlexample
SELECT v, UPPER(v) FROM lu;
```

```output
+----------------------------------+----------------------------------+
|                v                 |             upper(v)             |
+----------------------------------+----------------------------------+
|                                  |                                  |
| 1č2Щ3ß4Ę!-?abc@                  | 1Č2Щ3SS4Ę!-?ABC@                 |
| AaBbCcDdEeFfGgHhIiJj             | AABBCCDDEEFFGGHHIIJJ             |
| KkLlMmNnOoPpQqRrSsTt             | KKLLMMNNOOPPQQRRSSTT             |
| UuVvWwXxYyZz                     | UUVVWWXXYYZZ                     |
| ÁáÄäÉéÍíÓóÔôÚúÝý                 | ÁÁÄÄÉÉÍÍÓÓÔÔÚÚÝÝ                 |
| ÄäÖößÜü                          | ÄÄÖÖSSÜÜ                         |
| ÉéÀàÈèÙùÂâÊêÎîÔôÛûËëÏïÜüŸÿÇçŒœÆæ | ÉÉÀÀÈÈÙÙÂÂÊÊÎÎÔÔÛÛËËÏÏÜÜŸŸÇÇŒŒÆÆ |
| ĄąĆćĘęŁłŃńÓóŚśŹźŻż               | ĄĄĆĆĘĘŁŁŃŃÓÓŚŚŹŹŻŻ               |
| ČčĎďĹĺĽľŇňŔŕŠšŤťŽž               | ČČĎĎĹĹĽĽŇŇŔŔŠŠŤŤŽŽ               |
| АаБбВвГгДдЕеЁёЖжЗзИиЙй           | ААББВВГГДДЕЕЁЁЖЖЗЗИИЙЙ           |
| КкЛлМмНнОоПпРрСсТтУуФф           | ККЛЛММННООППРРССТТУУФФ           |
| ХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя           | ХХЦЦЧЧШШЩЩЪЪЫЫЬЬЭЭЮЮЯЯ           |
| [NULL]                           | [NULL]                           |
+----------------------------------+----------------------------------+
```

UPPER supports [collation](../collation.md) specifications. This UPPER example
specifies collation with the `tr` (Turkish) locale:

```sqlexample
SELECT UPPER('i' COLLATE 'tr');
```

```output
+-------------------------+
| UPPER('I' COLLATE 'TR') |
|-------------------------|
| İ                       |
+-------------------------+
```
