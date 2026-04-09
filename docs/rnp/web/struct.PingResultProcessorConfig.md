rnp
# Struct PingResultProcessorConfig
Source 

```
pub struct PingResultProcessorConfig {
    pub common_config: PingResultProcessorCommonConfig,
    pub exit_on_fail: bool,
    pub exit_failure_reason: Option<Arc<Mutex<Option<PingResultDto>>>>,
    pub csv_log_path: Option<PathBuf>,
    pub json_log_path: Option<PathBuf>,
    pub text_log_path: Option<PathBuf>,
    pub show_result_scatter: bool,
    pub show_latency_scatter: bool,
    pub latency_buckets: Option<Vec<f64>>,
}
```

## Fields§
§`common_config: PingResultProcessorCommonConfig`§`exit_on_fail: bool`§`exit_failure_reason: Option<Arc<Mutex<Option<PingResultDto>>>>`§`csv_log_path: Option<PathBuf>`§`json_log_path: Option<PathBuf>`§`text_log_path: Option<PathBuf>`§`show_result_scatter: bool`§`show_latency_scatter: bool`§`latency_buckets: Option<Vec<f64>>`
## Trait Implementations§