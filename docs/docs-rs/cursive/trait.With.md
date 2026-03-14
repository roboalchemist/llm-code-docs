cursive
# Trait With 
Source 

```
pub trait With: Sized {
    // Provided methods
    fn wrap_with<U, F>(self, f: F) -> U
       where F: FnOnce(Self) -> U { ... }
    fn with<F>(self, f: F) -> Self
       where F: FnOnce(&mut Self) { ... }
    fn try_with<E, F>(self, f: F) -> Result<Self, E>
       where F: FnOnce(&mut Self) -> Result<(), E> { ... }
    fn with_if<F>(self, condition: bool, f: F) -> Self
       where F: FnOnce(&mut Self) { ... }
}
```

## Provided Methods§