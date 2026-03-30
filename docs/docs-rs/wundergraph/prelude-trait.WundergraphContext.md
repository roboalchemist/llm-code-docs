wundergraph::prelude
# Trait WundergraphContext 
Source 

```
pub trait WundergraphContext {
    type Connection: Connection + 'static;

    // Required method
    fn get_connection(&self) -> &Self::Connection;
}
```

## Required Associated Types§