carton::types
# Struct LoadOpts 
Source 

```
pub struct LoadOpts {
    pub override_runner_name: Option<String>,
    pub override_required_framework_version: Option<String>,
    pub override_runner_opts: Option<HashMap<String, RunnerOpt>>,
    pub visible_device: Device,
}
```

## Fields§
§`override_runner_name: Option<String>`

Override the runner to use
If not overridden, this is fetched from the carton metadata
§`override_required_framework_version: Option<String>`

Override the framework_version to use
If not overridden, this is fetched from the carton metadata
§`override_runner_opts: Option<HashMap<String, RunnerOpt>>`

Options to pass to the runner. These are runner-specific (e.g.
PyTorch, TensorFlow, etc).

Overrides are merged with the options set in the carton metadata
Sometimes used to configure thread-pool sizes, etc.
See the documentation for more info
§`visible_device: Device`

The device that is visible to this model.
Note: a visible device does not necessarily mean that the model
will use that device; it is up to the model to actually use it
(e.g. by moving itself to GPU if it sees one available)

## Trait Implementations§