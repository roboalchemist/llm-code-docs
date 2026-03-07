# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-linked-buffer.md

A linked buffer structure for use with TCP. 

A single [otLinkedBuffer](ot-linked-buffer) structure references an array of bytes in memory, via mData and mLength. The mNext field is used to form a chain of [otLinkedBuffer](ot-linked-buffer) structures. 

## Public Attributes

### mNext

```
struct otLinkedBuffer* otLinkedBuffer::mNext
```

**Description:** Pointer to the next linked buffer in the chain, or NULL if it is the end.

### mData

```
const uint8_t* otLinkedBuffer::mData
```

**Description:** Pointer to data referenced by this linked buffer.

### mLength

```
size_t otLinkedBuffer::mLength
```

**Description:** Length of this linked buffer (number of bytes).