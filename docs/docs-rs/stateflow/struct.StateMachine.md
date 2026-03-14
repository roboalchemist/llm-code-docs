stateflow

# Struct StateMachine

Source

```
pub struct StateMachine<'a, C> {
    pub memory: Arc<RwLock<Map<String, Value>>>,
    pub context: Arc<RwLock<C>>,
    /* private fields */
}
```

## Fields§

§`memory: Arc<RwLock<Map<String, Value>>>`

The memory used by the state machine to store data.
§`context: Arc<RwLock<C>>`

The context used by the state machine to store state.

## Implementations§
