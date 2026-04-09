carton::types
# Type Alias CartonInfo 
Source 

```
pub type CartonInfo<T> = CartonInfo<T>;
```

## Aliased Type§

```
pub struct CartonInfo<T> {}
```

## Fields§
§`model_name: Option<String>`

The name of the model
§`short_description: Option<String>`

A short description (should be 100 characters or less)
§`model_description: Option<String>`

The model description
§`license: Option<String>`

The license for this model. This should be an SPDX expression, but may not be
for non-SPDX license types.
§`repository: Option<String>`

A URL for a repository for this model
§`homepage: Option<String>`

A URL for a website that is the homepage for this model
§`required_platforms: Option<Vec<Triple>>`

A list of platforms this model supports
If empty or unspecified, all platforms are okay
§`inputs: Option<Vec<TensorSpec>>`

A list of inputs for the model
Can be empty
§`outputs: Option<Vec<TensorSpec>>`

A list of outputs for the model
Can be empty
§`self_tests: Option<Vec<SelfTest<T>>>`

Test data
Can be empty
§`examples: Option<Vec<Example<T>>>`

Examples
Can be empty
§`runner: RunnerInfo`

Information about the runner to use
§`misc_files: Option<HashMap<String, Arc<dyn MiscFileLoader + Sync + Send>>>`

Misc files that can be referenced by the description. The key is a normalized relative path
(i.e one that does not reference parent directories, etc)