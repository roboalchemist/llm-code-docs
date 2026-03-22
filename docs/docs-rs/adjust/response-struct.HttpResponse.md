adjust::response
# Struct HttpResponse 
Source 

```
pub struct HttpResponse<T = HttpResponseCode, E = HttpError>where
    T: Serialize,
    E: Serialize + IntoResponse,{ /* private fields */ }
```

## Implementations§