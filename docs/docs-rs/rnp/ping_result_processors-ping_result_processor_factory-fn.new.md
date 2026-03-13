rnp::ping_result_processors::ping_result_processor_factory
# Function new
Source 

```
pub fn new(
    config: &PingResultProcessorConfig,
    extra_ping_result_processors: Vec<Box<dyn PingResultProcessor + Send + Sync>>,
    ping_stop_event: Arc<ManualResetEvent>,
) -> Vec<Box<dyn PingResultProcessor + Send + Sync>>
```