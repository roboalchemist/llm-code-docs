# Crate asyncapi 
Source 
## Re-exports§
`pub use channel_binding::ChannelBinding;``pub use message_binding::MessageBinding;``pub use operation_binding::OperationBinding;``pub use schema::Schema;``pub use server_binding::ServerBinding;`
## Modules§
channel_bindingmessage_bindingoperation_bindingschemaserver_binding
## Structs§
AsyncAPIThis is the root document object for the API specification.
It combines resource listing and API declaration together into one document.ChannelDescribes the operations available on a single channel.ComponentsHolds a set of reusable objects for different aspects of the AsyncAPI specification.
All objects defined within the components object will have no effect on the API
unless they are explicitly referenced from properties outside the components object.ContactContact information for the exposed API.CorrelationIdAn object that specifies an identifier at design time that can used for
message tracing and correlation.ExampleThe asyncapi spec doesn’t describe a structured example object.ExternalDocumentationAllows referencing an external resource for extended documentation.InfoThe object provides metadata about the API. The metadata can be used by the clients if needed.LicenseLicense information for the exposed API.MessageDescribes a message received on a given channel and operation.MessageTraitDescribes a trait that MAY be applied to a
Message Object.
This object MAY contain any property from the
Message Object,
except `payload` and `traits`.OperationDescribes a publish or a subscribe operation. This provides a place to document how
and why messages are sent and received.OperationTraitDescribes a trait that MAY be applied to an
Operation Object.
This object MAY contain any property from the
Operation Object,
except `message` and `traits`.ParameterDescribes a parameter included in a channel name.SecurityRequirementLists the required security schemes to execute this operation. The name
used for each property MUST correspond to a security scheme declared in the
Security Schemes under the Components Object.ServerAn object representing a message broker, a server or any other kind of
computer program capable of sending and/or receiving data. This object is
used to capture details such as URIs, protocols and security configuration.
Variable substitution can be used so that some details, for example
usernames and passwords, can be injected by code generation tools.ServerVariableAn object representing a Server Variable for server URL
template substitution.TagAllows adding meta data to a single tag.
## Enums§
ReferenceOrSecuritySchemeDefines a security scheme that can be used by the operations. Supported schemes are:VariantOrUnknownVariantOrUnknownOrEmpty