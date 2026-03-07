# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dns-query-config.md

Represents a DNS query configuration. 

Any of the fields in this structure can be set to zero to indicate that it is not specified. How the unspecified fields are treated is determined by the function which uses the instance of `otDnsQueryConfig`. 

## Public Attributes

### mServerSockAddr

```
otSockAddr otDnsQueryConfig::mServerSockAddr
```

**Description:** Server address (IPv6 addr/port). All zero or zero port for unspecified.

### mResponseTimeout

```
uint32_t otDnsQueryConfig::mResponseTimeout
```

**Description:** Wait time (in msec) to rx response. Zero indicates unspecified value.

### mMaxTxAttempts

```
uint8_t otDnsQueryConfig::mMaxTxAttempts
```

**Description:** Maximum tx attempts before reporting failure. Zero for unspecified value.

### mRecursionFlag

```
otDnsRecursionFlag otDnsQueryConfig::mRecursionFlag
```

**Description:** Indicates whether the server can resolve the query recursively or not.

### mNat64Mode

```
otDnsNat64Mode otDnsQueryConfig::mNat64Mode
```

**Description:** Allow/Disallow NAT64 address translation during address resolution.

### mServiceMode

```
otDnsServiceMode otDnsQueryConfig::mServiceMode
```

**Description:** Determines which records to query during service resolution.

### mTransportProto

```
otDnsTransportProto otDnsQueryConfig::mTransportProto
```

**Description:** Select default transport protocol.