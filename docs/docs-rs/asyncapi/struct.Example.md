asyncapi
# Struct Example 
Source 

```
pub struct Example {
    pub name: Option<String>,
    pub summary: Option<String>,
    pub description: Option<String>,
    pub payload: Option<Value>,
    pub headers: Option<Value>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`name: Option<String>`

A machine-friendly name.
§`summary: Option<String>`

A short summary of what the example is about.
§`description: Option<String>`

Long description for the example.
CommonMark syntax MAY be used for rich text representation.
§`payload: Option<Value>`

Payload as described in the `websocket-gemini` example.
§`headers: Option<Value>`

field name proposed in the issue #606
§`extensions: IndexMap<String, Value>`

Inline extensions to this object.

## Trait Implementations§