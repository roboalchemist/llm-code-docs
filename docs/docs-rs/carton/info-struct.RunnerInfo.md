carton::info
# Struct RunnerInfo 
Source 

```
pub struct RunnerInfo {
    pub runner_name: String,
    pub required_framework_version: VersionReq,
    pub runner_compat_version: Option<u64>,
    pub opts: Option<HashMap<String, RunnerOpt>>,
}
```

## Fields§
§`runner_name: String`

The name of the runner to use
§`required_framework_version: VersionReq`

The required framework version range to run the model with
This is a semver version range. See https://docs.rs/semver/1.0.16/semver/struct.VersionReq.html
for format details.
For example `=1.2.4`, means exactly version `1.2.4`
In most cases, this should be exactly one version
§`runner_compat_version: Option<u64>`

Don’t set this unless you know what you’re doing
§`opts: Option<HashMap<String, RunnerOpt>>`

Options to pass to the runner. These are runner-specific (e.g.
PyTorch, TensorFlow, etc).

Sometimes used to configure thread-pool sizes, etc.
See the documentation for more info

## Trait Implementations§