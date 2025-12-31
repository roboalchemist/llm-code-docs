# Source: https://firebase.google.com/docs/reference/rules/rules.Bytes.md.txt

# Interface: Bytes

# [rules](https://firebase.google.com/docs/reference/rules/rules).Bytes

interface static

Type representing a sequence of bytes.

Byte literals are specified using a `b` declaration prefix followed by
bytes represented as a sequence of characters, two-place hexadecimal
values (for example, `b'\x0F'`, not `b'\xF'`), or three-place octal
values (for example, `b'\000'`, not `b'\0'`). Character sequences are
interpreted as UTF-8 encoded strings.  

```scilab
// These are all equal to decimal 42.
b'*'
b'\x2A'
b'\052'

// These are all equivalent
b'â¬' // 3-byte UTF-8 encoded string
b'\342\202\254'
b'\xE2\x82\xAC'
```

Functions for the Bytes type are provided to aid comparison of byte
sequences represented as Base64url- and hexadecimal-encoded strings.

## Methods

### size

size() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Returns the number of bytes in a Bytes sequence.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the number of bytes.

#### Example

    b'\xFF\xFF'.size() == 2
    b'a'.size() == 1
    b'â¬'.size() == 3 // 3-byte UTF-8 encoded string

### toBase64

toBase64() returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Returns the Base64-encoded string corresponding to the provided Bytes
sequence.

Base64 encoding is performed per the
[base64url specification](https://tools.ietf.org/html/rfc4648#page-7).

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) a Base64-encoded string.

#### Example

    b'\xFB\xEF\xBE'.toBase64() == '----'

### toHexString

toHexString() returns [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

Returns the hexadecimal-encoded string corresponding to the provided Bytes
sequence.

Returns

:   `non-null `[rules.String](https://firebase.google.com/docs/reference/rules/rules.String) a hexadecimal-encoded string.

#### Example

    b'\x2A'.toHexString() == '2A'
    b'**'.toHexString() == '2A2A'
    b'â¬'.toHexString() == 'E282AC'