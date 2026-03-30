# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dnssd-service-instance-info.md

Represents information of a discovered service instance for a DNS-SD query. 

## Public Attributes

### mFullName

```
const char* otDnssdServiceInstanceInfo::mFullName
```

**Description:** Full instance name (e.g. "OpenThread._ipps._tcp.default.service.arpa.").

### mHostName

```
const char* otDnssdServiceInstanceInfo::mHostName
```

**Description:** Host name (e.g. "ot-host.default.service.arpa.").

### mAddressNum

```
uint8_t otDnssdServiceInstanceInfo::mAddressNum
```

**Description:** Number of host IPv6 addresses.

### mAddresses

```
const otIp6Address* otDnssdServiceInstanceInfo::mAddresses
```

**Description:** Host IPv6 addresses.

### mPort

```
uint16_t otDnssdServiceInstanceInfo::mPort
```

**Description:** Service port.

### mPriority

```
uint16_t otDnssdServiceInstanceInfo::mPriority
```

**Description:** Service priority.

### mWeight

```
uint16_t otDnssdServiceInstanceInfo::mWeight
```

**Description:** Service weight.

### mTxtLength

```
uint16_t otDnssdServiceInstanceInfo::mTxtLength
```

**Description:** Service TXT RDATA length.

### mTxtData

```
const uint8_t* otDnssdServiceInstanceInfo::mTxtData
```

**Description:** Service TXT RDATA.

### mTtl

```
uint32_t otDnssdServiceInstanceInfo::mTtl
```

**Description:** Service TTL (in seconds).