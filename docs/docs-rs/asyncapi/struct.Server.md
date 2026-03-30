asyncapi
# Struct Server 
Source 

```
pub struct Server {
    pub url: String,
    pub protocol: String,
    pub protocol_version: Option<String>,
    pub description: Option<String>,
    pub variables: IndexMap<String, ServerVariable>,
    pub security: Vec<SecurityRequirement>,
    pub bindings: Option<ReferenceOr<ServerBinding>>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`url: String`

**REQUIRED.** A URL to the target host. This URL supports Server
Variables and MAY be relative, to indicate that the host location is
relative to the location where the AsyncAPI document is being served.
Variable substitutions will be made when a variable is named in
`{`brackets`}`.
§`protocol: String`

**REQUIRED.** The protocol this URL supports for connection.
Supported protocol include, but are not limited to:
`amqp`, `amqps`, `http`, `https`, `ibmmq`, `jms`, `kafka`,
`kafka-secure`, `mqtt`, `secure-mqtt`, `stomp`, `stomps`, `ws`,
`wss`, `mercure`.
§`protocol_version: Option<String>`

The version of the protocol used for connection.
For instance: AMQP `0.9.1`, HTTP `2.0`, Kafka `1.0.0`, etc.
§`description: Option<String>`

An optional string describing the host designated by the URL.
CommonMark syntax MAY be used
for rich text representation.
§`variables: IndexMap<String, ServerVariable>`

A map between a variable name and its value. The value is used
for substitution in the server’s URL template.
§`security: Vec<SecurityRequirement>`

A declaration of which security mechanisms can be used with this
server. The list of values includes alternative security requirement
objects that can be used. Only one of the security requirement objects
need to be satisfied to authorize a connection or operation.
§`bindings: Option<ReferenceOr<ServerBinding>>`

A map where the keys describe the name of the protocol and the values
describe protocol-specific definitions for the server.
§`extensions: IndexMap<String, Value>`

This object MAY be extended with
Specification Extensions.

## Trait Implementations§