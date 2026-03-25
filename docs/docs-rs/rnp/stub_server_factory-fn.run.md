rnp::stub_server_factory
# Function run
Source 

```
pub fn run(
    config: &RnpStubServerConfig,
    stop_event: Arc<ManualResetEvent>,
    server_started_event: Arc<ManualResetEvent>,
) -> JoinHandle<Result<(), Box<dyn Error + Send + Sync>>>
```