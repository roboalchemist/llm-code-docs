# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/url.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/url.md

# Source: https://docs.pinot.apache.org/functions-1/url.md

# Url

Returns the url-encoded or url-decoded string of the input string with UTF\_8 encoding, formatting details see [java.net.URLEncoder](https://docs.oracle.com/javase/8/docs/api/java/net/URLEncoder.html)

## Signature

> encodeUrl(string)
>
> decodeUrl(string)

## Usage Examples

```sql
SELECT concat('https://www.google.com/search?q=', encodeUrl('key1=val1 key2=45% key3=#47'),'') AS encoded
FROM ignoreMe
```

| encoded                                                                 |
| ----------------------------------------------------------------------- |
| <https://www.google.com/search?q=key1%3Dval1+key2%3D45%25+key3%3D%2347> |

```sql
SELECT decodeUrl('https://www.google.com/search?q=key1%3Dval1+key2%3D45%25+key3%3D%2347') AS decoded
FROM ignoreMe
```

| decoded                                                       |
| ------------------------------------------------------------- |
| <https://www.google.com/search?q=key1=val1> key2=45% key3=#47 |
