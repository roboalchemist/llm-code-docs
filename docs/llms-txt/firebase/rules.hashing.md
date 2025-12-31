# Source: https://firebase.google.com/docs/reference/rules/rules.hashing.md.txt

# Namespace: hashing

# [rules](https://firebase.google.com/docs/reference/rules/rules).hashing

namespace static

Globally available hashing functions. These functions are accessed
using the `hashing.` prefix.

## Methods

### crc32

static

crc32(bytes_or_string) returns [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes)

Compute a hash using the CRC32 algorithm.

|                                                                                                                                         #### Parameter                                                                                                                                         ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bytes_or_string | (non-null [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) or non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)) Bytes sequence (declared with b prefix), or string. For strings, the UTF-8 encoding is used. |

Returns

:   `non-null `[rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) hash value as a Bytes sequence.

### crc32c

static

crc32c(bytes_or_string) returns [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes)

Compute a hash using the CRC32C algorithm.

|                                                                                                                                         #### Parameter                                                                                                                                         ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bytes_or_string | (non-null [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) or non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)) Bytes sequence (declared with b prefix), or string. For strings, the UTF-8 encoding is used. |

Returns

:   `non-null `[rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) hash value as a Bytes sequence.

### md5

static

md5(bytes_or_string) returns [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes)

Compute a hash using the MD5 algorithm.

|                                                                                                                                         #### Parameter                                                                                                                                         ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bytes_or_string | (non-null [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) or non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)) Bytes sequence (declared with b prefix), or string. For strings, the UTF-8 encoding is used. |

Returns

:   `non-null `[rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) hash value as a Bytes sequence.

### sha256

static

sha256(bytes_or_string) returns [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes)

Compute a hash using the SHA-256 algorithm.

|                                                                                                                                         #### Parameter                                                                                                                                         ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bytes_or_string | (non-null [rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) or non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)) Bytes sequence (declared with b prefix), or string. For strings, the UTF-8 encoding is used. |

Returns

:   `non-null `[rules.Bytes](https://firebase.google.com/docs/reference/rules/rules.Bytes) hash value as a Bytes sequence.