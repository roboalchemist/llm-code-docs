# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dns-txt-entry.md

Represents a TXT record entry representing a key/value pair (RFC 6763 - section 6.3). 

The string buffers pointed to by `mKey` and `mValue` MUST persist and remain unchanged after an instance of such structure is passed to OpenThread (as part of `otSrpClientService` instance).

An array of `otDnsTxtEntry` entries are used in `otSrpClientService` to specify the full TXT record (a list of entries). 

## Public Attributes

### mKey

```
const char* otDnsTxtEntry::mKey
```

**Description:** The TXT record key string.

**Details:** If `mKey` is not NULL, then it MUST be a null-terminated C string. The entry is treated as key/value pair with `mValue` buffer providing the value.

- The entry is encoded as follows:  
  - A single string length byte followed by "key=value" format (without the quotation marks).  
  - In this case, the overall encoded length must be 255 bytes or less.
- If `mValue` is NULL, then key is treated as a boolean attribute and encoded as "key" (with no `=`).
- If `mValue` is not NULL but `mValueLength` is zero, then it is treated as empty value and encoded as "key=".

If `mKey` is NULL, then `mValue` buffer is treated as an already encoded TXT-DATA and is appended as is in the DNS message.

### mValue

```
const uint8_t* otDnsTxtEntry::mValue
```

**Description:** The TXT record value or already encoded TXT-DATA (depending on `mKey`).

### mValueLength

```
uint16_t otDnsTxtEntry::mValueLength
```

**Description:** Number of bytes in `mValue` buffer.