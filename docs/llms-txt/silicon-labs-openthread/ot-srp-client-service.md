# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-srp-client-service.md

Represents an SRP client service. 

The values in this structure, including the string buffers for the names and the TXT record entries, MUST persist and stay constant after an instance of this structure is passed to OpenThread from `otSrpClientAddService()` or `otSrpClientRemoveService()`.

The `mState`, `mData`, `mNext` fields are used/managed by OT core only. Their value is ignored when an instance of `otSrpClientService` is passed in `otSrpClientAddService()` or `otSrpClientRemoveService()` or other functions. The caller does not need to set these fields.

The `mLease` and `mKeyLease` fields specify the desired lease and key lease intervals for this service. Zero value indicates that the interval is unspecified and then the default lease or key lease intervals from `otSrpClientGetLeaseInterval()` and `otSrpClientGetKeyLeaseInterval()` are used for this service. If the key lease interval (whether set explicitly or determined from the default) is shorter than the lease interval for a service, SRP client will re-use the lease interval value for key lease interval as well. For example, if in service `mLease` is explicitly set to 2 days and `mKeyLease` is set to zero and default key lease is set to 1 day, then when registering this service, the requested key lease for this service is also set to 2 days. 

## Public Attributes

### mName

```
const char* otSrpClientService::mName
```

**Description:** The service labels (e.g., "_mt._udp", not the full domain name).

### mInstanceName

```
const char* otSrpClientService::mInstanceName
```

**Description:** The service instance name label (not the full name).

### mSubTypeLabels

```
const char* const* otSrpClientService::mSubTypeLabels
```

**Description:** Array of sub-type labels (must end with `NULL` or can be `NULL`).

### mTxtEntries

```
const otDnsTxtEntry* otSrpClientService::mTxtEntries
```

**Description:** Array of TXT entries (`mNumTxtEntries` gives num of entries).

### mPort

```
uint16_t otSrpClientService::mPort
```

**Description:** The service port number.

### mPriority

```
uint16_t otSrpClientService::mPriority
```

**Description:** The service priority.

### mWeight

```
uint16_t otSrpClientService::mWeight
```

**Description:** The service weight.

### mNumTxtEntries

```
uint8_t otSrpClientService::mNumTxtEntries
```

**Description:** Number of entries in the `mTxtEntries` array.

### mState

```
otSrpClientItemState otSrpClientService::mState
```

**Description:** Service state (managed by OT core).

### mData

```
uint32_t otSrpClientService::mData
```

**Description:** Internal data (used by OT core).

### mNext

```
struct otSrpClientService* otSrpClientService::mNext
```

**Description:** Pointer to next entry in a linked-list (managed by OT core).

### mLease

```
uint32_t otSrpClientService::mLease
```

**Description:** Desired lease interval in sec - zero to use default.

### mKeyLease

```
uint32_t otSrpClientService::mKeyLease
```

**Description:** Desired key lease interval in sec - zero to use default.