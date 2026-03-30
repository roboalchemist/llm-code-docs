# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dns-txt-entry-iterator.md

Represents an iterator for TXT record entries (key/value pairs). 

The data fields in this structure are intended for use by OpenThread core and caller should not read or change them. 

## Public Attributes

### mPtr

```
const void* otDnsTxtEntryIterator::mPtr
```

### mData

```
uint16_t otDnsTxtEntryIterator::mData[2]
```

### mChar

```
char otDnsTxtEntryIterator::mChar[OT_DNS_TXT_KEY_ITER_MAX_LENGTH+1]
```