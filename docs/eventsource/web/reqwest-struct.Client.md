eventsource::reqwest
# Struct Client 
Source 

```
pub struct Client {
    pub retry: Duration,
    /* private fields */
}
```

## Fields§
§`retry: Duration`

Reconnection time in milliseconds. Note that the reconnection time can be changed by the
event stream, so changing this may not make a difference.

## Implementations§