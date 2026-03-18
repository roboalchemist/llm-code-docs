adjust::response
# Type Alias HttpResult 
Source 

```
pub type HttpResult<T = HttpResponseCode> = RawHttpResult<Json<HttpResponse<T, HttpError>>>;
```

## Aliased Type§

```
pub enum HttpResult<T = HttpResponseCode> {
    Ok(Json<HttpResponse<T>>),
    Err(HttpError),
}
```

## Variants§
§1.0.0
### Ok(Json<HttpResponse<T>>)