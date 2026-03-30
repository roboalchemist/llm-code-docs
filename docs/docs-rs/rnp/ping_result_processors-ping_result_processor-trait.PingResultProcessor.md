rnp::ping_result_processors::ping_result_processor
# Trait PingResultProcessor
Source 

```
pub trait PingResultProcessor {
    // Required methods
    fn name(&self) -> &'static str;
    fn config(&self) -> &PingResultProcessorCommonConfig;
    fn process_ping_result(&mut self, ping_result: &PingResult);

    // Provided methods
    fn has_quiet_level(&self, quiet_level: i32) -> bool { ... }
    fn initialize(&mut self) { ... }
    fn rundown(&mut self) { ... }
}
```

## Required Methods§
Source
#### fn name(&self) -> &'static str