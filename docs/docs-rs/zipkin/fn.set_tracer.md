zipkin
# Function set_tracer 
Source 

```
pub fn set_tracer<S, R>(
    sampler: S,
    reporter: R,
    local_endpoint: Endpoint,
) -> Result<(), SetTracerError>where
    S: Sample + 'static + Sync + Send,
    R: Report + 'static + Sync + Send,
```