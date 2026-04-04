# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dns-record-info.md

Represents info for a record in an `otDnsRecordResponse`. 

This struct is used as input to `otDnsRecordResponseGetRecordInfo()`. 

## Public Attributes

### mNameBuffer

```
char* otDnsRecordInfo::mNameBuffer
```

**Description:** Buffer to output the name (MUST NOT be NULL).

### mNameBufferSize

```
uint16_t otDnsRecordInfo::mNameBufferSize
```

**Description:** Size of `mNameBuffer`.

### mRecordType

```
uint16_t otDnsRecordInfo::mRecordType
```

**Description:** The record type.

### mRecordLength

```
uint16_t otDnsRecordInfo::mRecordLength
```

**Description:** The record data length (in bytes).

### mTtl

```
uint32_t otDnsRecordInfo::mTtl
```

**Description:** Record TTL (in seconds).

### mDataBuffer

```
uint8_t* otDnsRecordInfo::mDataBuffer
```

**Description:** Buffer to output the data (Can be NULL if data not needed).

### mDataBufferSize

```
uint16_t otDnsRecordInfo::mDataBufferSize
```

**Description:** On input, size of `mDataBuffer`. On output number of bytes written.

### mSection

```
otDnsRecordSection otDnsRecordInfo::mSection
```

**Description:** Indicates the section of the record.