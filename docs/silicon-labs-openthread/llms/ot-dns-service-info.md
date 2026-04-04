# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dns-service-info.md

Provides info for a DNS service instance. 

## Public Attributes

### mTtl

```
uint32_t otDnsServiceInfo::mTtl
```

**Description:** Service record TTL (in seconds).

### mPort

```
uint16_t otDnsServiceInfo::mPort
```

**Description:** Service port number.

### mPriority

```
uint16_t otDnsServiceInfo::mPriority
```

**Description:** Service priority.

### mWeight

```
uint16_t otDnsServiceInfo::mWeight
```

**Description:** Service weight.

### mHostNameBuffer

```
char* otDnsServiceInfo::mHostNameBuffer
```

**Description:** Buffer to output the service host name (can be NULL if not needed).

### mHostNameBufferSize

```
uint16_t otDnsServiceInfo::mHostNameBufferSize
```

**Description:** Size of `mHostNameBuffer`.

### mHostAddress

```
otIp6Address otDnsServiceInfo::mHostAddress
```

**Description:** The host IPv6 address. Set to all zero if not available.

### mHostAddressTtl

```
uint32_t otDnsServiceInfo::mHostAddressTtl
```

**Description:** The host address TTL.

### mTxtData

```
uint8_t* otDnsServiceInfo::mTxtData
```

**Description:** Buffer to output TXT data (can be NULL if not needed).

### mTxtDataSize

```
uint16_t otDnsServiceInfo::mTxtDataSize
```

**Description:** On input, size of `mTxtData` buffer. On output number bytes written.

### mTxtDataTruncated

```
bool otDnsServiceInfo::mTxtDataTruncated
```

**Description:** Indicates if TXT data could not fit in `mTxtDataSize` and was truncated.

### mTxtDataTtl

```
uint32_t otDnsServiceInfo::mTxtDataTtl
```

**Description:** The TXT data TTL.