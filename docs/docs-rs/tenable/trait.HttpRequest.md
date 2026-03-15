tenable
# Trait HttpRequest 
Source 

```
pub trait HttpRequest<RE: Debug>: Clone {
    type Output;

    // Required methods
    fn to_request(&self) -> Result<Request<Vec<u8>>, Error<RE>>;
    fn from_response(&self, res: Response) -> Result<Self::Output, Error<RE>>;
}
```

## Required Associated Types§