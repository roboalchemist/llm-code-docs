# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcp-listener-initialize-args.md

Contains arguments to the [otTcpListenerInitialize()](api-tcp#ot-tcp-listener-initialize) function. 

## Public Attributes

### mContext

```
void* otTcpListenerInitializeArgs::mContext
```

**Description:** Pointer to application-specific context.

### mAcceptReadyCallback

```
otTcpAcceptReady otTcpListenerInitializeArgs::mAcceptReadyCallback
```

**Description:** "Accept ready" callback function

### mAcceptDoneCallback

```
otTcpAcceptDone otTcpListenerInitializeArgs::mAcceptDoneCallback
```

**Description:** "Accept done" callback function