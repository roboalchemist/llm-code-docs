zeromq
# Trait TryIntoEndpoint 
Source 

```
pub trait TryIntoEndpoint: Send + Sealed {
    // Required method
    fn try_into(self) -> Result<Endpoint, EndpointError>;
}
```

## Required Methods§