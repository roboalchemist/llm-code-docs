# Crate httptest 
Source 
## Re-exports§
`pub use bytes;``pub use http;`
## Modules§
matchersMatcher implementations.respondersResponder implementations.
## Macros§
all_oftrue if all the provided matchers return true.any_oftrue if any of the provided matchers return true.cyclea Responder that cycles through a list of responses.
## Structs§
ExpectationAn expectation to be asserted by the server.ExpectationBuilderDefine expectations using a builder pattern.ServerThe ServerServerBuilderCustom Server Builder.ServerHandleA handle to a server. Expectations are inserted when the handle is dropped.ServerPoolA pool of shared servers.
## Traits§
IntoTimesHow many times is an expectation expected to occur.
Implemented for usize and any range of usize values.