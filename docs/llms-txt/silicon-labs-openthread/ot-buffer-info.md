# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-buffer-info.md

Represents the message buffer information for different queues used by OpenThread stack. 

## Public Attributes

### mTotalBuffers

```
uint16_t otBufferInfo::mTotalBuffers
```

**Description:** The total number of buffers in the messages pool (0xffff if unknown).

### mFreeBuffers

```
uint16_t otBufferInfo::mFreeBuffers
```

**Description:** The number of free buffers (0xffff if unknown).

### mMaxUsedBuffers

```
uint16_t otBufferInfo::mMaxUsedBuffers
```

**Description:** The maximum number of used buffers at the same time since OT stack initialization or last call to `otMessageResetBufferInfo()`.

### m6loSendQueue

```
otMessageQueueInfo otBufferInfo::m6loSendQueue
```

**Description:** Info about 6LoWPAN send queue.

### m6loReassemblyQueue

```
otMessageQueueInfo otBufferInfo::m6loReassemblyQueue
```

**Description:** Info about 6LoWPAN reassembly queue.

### mIp6Queue

```
otMessageQueueInfo otBufferInfo::mIp6Queue
```

**Description:** Info about IPv6 send queue.

### mMplQueue

```
otMessageQueueInfo otBufferInfo::mMplQueue
```

**Description:** Info about MPL send queue.

### mMleQueue

```
otMessageQueueInfo otBufferInfo::mMleQueue
```

**Description:** Info about MLE delayed message queue.

### mCoapQueue

```
otMessageQueueInfo otBufferInfo::mCoapQueue
```

**Description:** Info about CoAP/TMF send queue.

### mCoapSecureQueue

```
otMessageQueueInfo otBufferInfo::mCoapSecureQueue
```

**Description:** Info about CoAP secure send queue.

### mApplicationCoapQueue

```
otMessageQueueInfo otBufferInfo::mApplicationCoapQueue
```

**Description:** Info about application CoAP send queue.