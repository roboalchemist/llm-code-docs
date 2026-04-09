asyncapi
# Struct Channel 
Source 

```
pub struct Channel {
    pub reference: Option<String>,
    pub description: Option<String>,
    pub servers: Vec<String>,
    pub subscribe: Option<Operation>,
    pub publish: Option<Operation>,
    pub parameters: IndexMap<String, ReferenceOr<Parameter>>,
    pub bindings: Option<ReferenceOr<ChannelBinding>>,
    pub extensions: IndexMap<String, Value>,
}
```

## Fields§
§`reference: Option<String>`👎Deprecated: The $ref field in Channel Item Object is now deprecated
from AsyncAPI 2.3.0. The current plan is that the $ref field will be
removed from Channel Item Object in AsyncAPI 3.0, and replaced with
Reference Object.

Allows for an external definition of this channel item. The referenced structure
MUST be in the format of a
Channel Item Object.
If there are conflicts between the referenced definition and this Channel Item’s
definition, the behavior is *undefined*.
§`description: Option<String>`

An optional description of this channel item.
CommonMark syntax can be used for rich
text representation.
§`servers: Vec<String>`

The servers on which this channel is available, specified as an optional unordered
list of names (string keys) of Server Objects defined in the
Servers Object (a map). If `servers` is absent or empty then this
channel must be available on all servers defined in the Servers Object.
§`subscribe: Option<Operation>`

A definition of the SUBSCRIBE operation, which defines the messages produced
by the application and sent to the channel.
§`publish: Option<Operation>`

A definition of the PUBLISH operation, which defines the messages consumed
by the application from the channel.
§`parameters: IndexMap<String, ReferenceOr<Parameter>>`

A map of the parameters included in the channel name. It SHOULD be present only
when using channels with expressions (as defined by
RFC 6570 section 2.2).

Describes a map of parameters included in a channel name.

This map MUST contain all the parameters used in the parent channel name.

### §Examples

```
{
    "user/{userId}/signup": {
        "parameters": {
            "userId": {
                "description": "Id of the user.",
                "schema": {
                   "type": "string"
                }
            }
        },
        "subscribe": {
            "$ref": "#/components/messages/userSignedUp"
        }
    }
}
```

```
user/{userId}/signup:
  parameters:
    userId:
      description: Id of the user.
      schema:
        type: string
  subscribe:
    $ref: "#/components/messages/userSignedUp"
```
§`bindings: Option<ReferenceOr<ChannelBinding>>`

A map where the keys describe the name of the protocol and the values
describe protocol-specific definitions for the channel.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§