rnp
# Struct RnpPingRunnerConfig
Source 

```
pub struct RnpPingRunnerConfig {
    pub worker_config: PingWorkerConfig,
    pub worker_scheduler_config: PingWorkerSchedulerConfig,
    pub result_processor_config: PingResultProcessorConfig,
    pub external_ping_client_factory: Option<PingClientFactory>,
    pub extra_ping_result_processors: Vec<Box<dyn PingResultProcessor + Send + Sync>>,
}
```

## Fields§
§`worker_config: PingWorkerConfig`§`worker_scheduler_config: PingWorkerSchedulerConfig`§`result_processor_config: PingResultProcessorConfig`§`external_ping_client_factory: Option<PingClientFactory>`§`extra_ping_result_processors: Vec<Box<dyn PingResultProcessor + Send + Sync>>`
## Trait Implementations§