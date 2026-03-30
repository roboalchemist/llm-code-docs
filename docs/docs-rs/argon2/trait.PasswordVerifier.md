argon2
# Trait PasswordVerifier 
Source 

```
pub trait PasswordVerifier {
    // Required method
    fn verify_password(
        &self,
        password: &[u8],
        hash: &PasswordHash<'_>,
    ) -> Result<(), Error>;
}
```
Available on **crate feature `password-hash`** only.
## Required Methods§