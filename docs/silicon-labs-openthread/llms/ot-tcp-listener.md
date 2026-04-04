# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcp-listener.md

Represents a TCP listener. 

A TCP listener is used to listen for and accept incoming TCP connections.

The application should not inspect the fields of this structure directly; it should only interact with it via the TCP API functions whose signatures are provided in this file. 

## Public Attributes

### mSize

```
uint8_t otTcpListener::mSize[OT_TCP_LISTENER_TCB_SIZE_BASE+OT_TCP_LISTENER_TCB_NUM_PTR *sizeof(void *)]
```

### mAlign

```
void* otTcpListener::mAlign
```

### mTcbListen

```
union otTcpListener::@22 otTcpListener::mTcbListen
```

### mNext

```
struct otTcpListener* otTcpListener::mNext
```

**Description:** A pointer to the next TCP listener (internal use only)

### mContext

```
void* otTcpListener::mContext
```

**Description:** A pointer to application-specific context.

### mAcceptReadyCallback

```
otTcpAcceptReady otTcpListener::mAcceptReadyCallback
```

**Description:** "Accept ready" callback function

### mAcceptDoneCallback

```
otTcpAcceptDone otTcpListener::mAcceptDoneCallback
```

**Description:** "Accept done" callback function