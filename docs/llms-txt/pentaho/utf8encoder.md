# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/dashboard/utf8encoder.md

# Utf8Encoder

## cdf.dashboard. Utf8Encoder

Static

Auxiliary UTF-8 encoder.

**AMD Module**

```
require(["cdf/dashboard/Utf8Encoder"], function(Utf8Encoder) { /* code goes here */ });
```

\*\*Source:\*\*dashboard/Utf8Encoder.js, line 72

\*\*See also:\*\*<http://www.webtoolkit.info/javascript\\_utf8.html>

## Methods

| Name                                                          | Description                                                                          |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| encode\_prepare(s) : `string`                                 | Prepares a UTF-8 string to be used in Opera or Internet Explorer.                    |
| encode\_prepare\_arr(value) : `string` \| `array` \| `number` | Prepares an array containing UTF-8 strings to be used in Opera or Internet Explorer. |

## Methods Details

| **encode\_prepare**(s) : `string`                                                                                               |                      |                        |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------- |
| <p>Prepares a UTF-8 string to be used in Opera or Internet Explorer.</p><p>\*\*Source:\*\*dashboard/Utf8Encoder.js, line 88</p> |                      |                        |
| Name                                                                                                                            | Default Value        | Summary                |
| s : `string`                                                                                                                    |                      | String to be prepared. |
| Name                                                                                                                            | Description          |                        |
| `string` \| `null`                                                                                                              | The prepared string. |                        |

| **encode\_prepare\_arr**(value) : `string` \| `array` \| `number`                                                                                   |                     |                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------- |
| <p>Prepares an array containing UTF-8 strings to be used in Opera or Internet Explorer.</p><p>\*\*Source:\*\*dashboard/Utf8Encoder.js, line 107</p> |                     |                       |
| Name                                                                                                                                                | Default Value       | Summary               |
| value : `string` \| `array` \| `number`                                                                                                             |                     | Value to be prepared. |
| Name                                                                                                                                                | Description         |                       |
| `string` \| `array` \| `number`                                                                                                                     | The prepared value. |                       |
