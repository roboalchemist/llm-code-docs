argon2
# Trait PasswordHasher 
Source 

```
pub trait PasswordHasher {
    type Params: Clone + Debug + Default + for<'a> TryFrom<&'a PasswordHash<'a>, Error = Error> + TryInto<ParamsString, Error = Error>;

    // Required method
    fn hash_password_customized<'a>(
        &self,
        password: &[u8],
        algorithm: Option<Ident<'a>>,
        version: Option<u32>,
        params: Self::Params,
        salt: impl Into<Salt<'a>>,
    ) -> Result<PasswordHash<'a>, Error>;

    // Provided method
    fn hash_password<'a>(
        &self,
        password: &[u8],
        salt: impl Into<Salt<'a>>,
    ) -> Result<PasswordHash<'a>, Error> { ... }
}
```
Available on **crate feature `password-hash`** only.
## Required Associated Types§