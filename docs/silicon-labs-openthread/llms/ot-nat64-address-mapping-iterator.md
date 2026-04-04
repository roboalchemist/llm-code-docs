# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-nat64-address-mapping-iterator.md

Used to iterate through NAT64 address mappings. 

The fields in this type are opaque (intended for use by OpenThread core only) and therefore should not be accessed or used by caller.

Before using an iterator, it MUST be initialized using `otNat64InitAddressMappingIterator()`.

The member fields in this struct are for internal OpenThread stack use and should not be accessed directly. 

## Public Attributes

### mPtr

```
const void* otNat64AddressMappingIterator::mPtr
```

### mData32

```
uint32_t otNat64AddressMappingIterator::mData32
```