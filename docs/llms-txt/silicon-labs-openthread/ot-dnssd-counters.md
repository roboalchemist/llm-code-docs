# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dnssd-counters.md

Contains the counters of DNS-SD server. 

## Public Attributes

### mSuccessResponse

```
uint32_t otDnssdCounters::mSuccessResponse
```

**Description:** The number of successful responses.

### mServerFailureResponse

```
uint32_t otDnssdCounters::mServerFailureResponse
```

**Description:** The number of server failure responses.

### mFormatErrorResponse

```
uint32_t otDnssdCounters::mFormatErrorResponse
```

**Description:** The number of format error responses.

### mNameErrorResponse

```
uint32_t otDnssdCounters::mNameErrorResponse
```

**Description:** The number of name error responses.

### mNotImplementedResponse

```
uint32_t otDnssdCounters::mNotImplementedResponse
```

**Description:** The number of 'not implemented' responses.

### mOtherResponse

```
uint32_t otDnssdCounters::mOtherResponse
```

**Description:** The number of other responses.

### mResolvedBySrp

```
uint32_t otDnssdCounters::mResolvedBySrp
```

**Description:** The number of queries resolved by the local SRP server.

### mUpstreamDnsCounters

```
otUpstreamDnsCounters otDnssdCounters::mUpstreamDnsCounters
```

**Description:** The number of queries, responses, failures handled by upstream DNS server.