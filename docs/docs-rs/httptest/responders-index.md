httptest
# Module responders 
Source 
## Macros§
cyclea Responder that cycles through a list of responses.
## Structs§
CycleThe `Cycle` responder returned by cycle()DelayResponder that delays the embedded responseResponseBuilderConvenient ResponseBuilder that implements Responder.
## Traits§
ResponderRespond with an HTTP response.
## Functions§
cycleCycle through the provided list of responders.delay_and_thenrespond with the given responder after a delayjson_encodedrespond with a body that is the json encoding of data.status_coderespond with the provided status code and an empty body.url_encodedrespond with a body that is the url encoding of data.