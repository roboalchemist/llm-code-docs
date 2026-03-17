asyncapi
# Struct AsyncAPI 
Source 

```
pub struct AsyncAPI {
    pub asyncapi: String,
    pub id: Option<String>,
    pub info: Info,
    pub servers: IndexMap<String, ReferenceOr<Server>>,
    pub default_content_type: Option<String>,
    pub channels: IndexMap<String, Channel>,
    pub components: Option<Components>,
    pub tags: Vec<Tag>,
    pub external_docs: Option<ExternalDocumentation>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`asyncapi: String`

**Required.** Specifies the AsyncAPI Specification version being used.
It can be used by tooling Specifications and clients to interpret the
version. The structure shall be `major`.`minor`.`patch`, where `patch`
versions must be compatible with the existing `major`.`minor` tooling.
Typically patch versions will be introduced to address errors in the
documentation, and tooling should typically be compatible with the
corresponding `major`.`minor` (1.0.*). Patch versions will correspond
to patches of this document.

The version string signifies the version of the AsyncAPI Specification
that the document complies to. The format for this string must be
`major`.`minor`.`patch`. The `patch` may be suffixed by a hyphen and
extra alphanumeric characters.

A `major`.`minor` shall be used to designate the AsyncAPI
Specification version, and will be considered compatible with the
AsyncAPI Specification specified by that `major`.`minor` version. The
patch version will not be considered by tooling, making no distinction
between `1.0.0` and `1.0.1`.

In subsequent versions of the AsyncAPI Specification, care will be
given such that increments of the `minor` version should not interfere
with operations of tooling developed to a lower minor version. Thus a
hypothetical `1.1.0` specification should be usable with tooling
designed for `1.0.0`.
§`id: Option<String>`

Identifier of the
application
the AsyncAPI document is defining.

This field represents a unique universal identifier of the
application
the AsyncAPI document is defining. It must conform to the URI format,
according to RFC3986.

It is RECOMMENDED to use a URN
to globally and uniquely identify the application during long periods
of time, even after it becomes unavailable or ceases to exist.

### §Examples

```
{
    "id": "urn:com:smartylighting:streetlights:server"
}
```

```
id: 'urn:com:smartylighting:streetlights:server'
```

```
{
    "id": "https://github.com/smartylighting/streetlights-server"
}
```

```
id: 'https://github.com/smartylighting/streetlights-server'
```
§`info: Info`

**Required.** Provides metadata about the API.
The metadata can be used by the clients if needed.
§`servers: IndexMap<String, ReferenceOr<Server>>`

Provides connection details of servers.

The Servers Object is a map of
Server Objects.

### §Examples

```
{
    "production": {
        "url": "development.gigantic-server.com",
        "description": "Development server",
        "protocol": "kafka",
        "protocolVersion": "1.0.0"
    }
}
```

```
production:
    url: development.gigantic-server.com
    description: Development server
    protocol: kafka
    protocolVersion: '1.0.0'
```
§`default_content_type: Option<String>`

Default content type to use when encoding/decoding a message’s payload.
A string representing the default content type to use when encoding/decoding a
message’s payload. The value MUST be a specific media type (e.g. `application/json`).
This value MUST be used by schema parsers when the
contentType
property is omitted.

In case a message can’t be encoded/decoded using this value, schema
parsers MUST use their default content type.

### §Examples

```
{
  "defaultContentType": "application/json"
}
```

```
defaultContentType: application/json
```
§`channels: IndexMap<String, Channel>`

**Required** The available channels and messages for the API.

Holds the relative paths to the individual channel and their operations.
Channel paths are relative to servers.

Channels are also known as “topics”, “routing keys”, “event types” or “paths”.

Each item is a relative path to an individual channel. The field name MUST be in
the form of a RFC 6570 URI template.
Query parameters and fragments SHALL NOT be used, instead use
bindings to define them.

### §Examples

```
{
    "user/signedup": {
        "subscribe": {
        "$ref": "#/components/messages/userSignedUp"
        }
    }
}
```

```
user/signedup:
  subscribe:
    $ref: "#/components/messages/userSignedUp"
```
§`components: Option<Components>`

An element to hold various schemas for the specification.
§`tags: Vec<Tag>`

A list of tags used by the specification with additional metadata.
Each tag name in the list MUST be unique.
§`external_docs: Option<ExternalDocumentation>`

Additional external documentation.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§