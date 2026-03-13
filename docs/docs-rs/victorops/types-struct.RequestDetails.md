victorops::types
# Struct RequestDetails 
Source 

```
pub struct RequestDetails {
    pub status_code: u16,
    pub response_body: String,
    pub request_body: String,
}
```

## Fields§
§`status_code: u16`

The HTTP status code of the response.
§`response_body: String`

The response body as a string.
§`request_body: String`

The request body that was sent.

## Trait Implementations§