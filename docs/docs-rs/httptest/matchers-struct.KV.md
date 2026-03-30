httptest::matchers
# Struct KV 
Source 

```
pub struct KV<K, V>where
    Self: Sized,
    K: ToOwned + ?Sized,
    V: ToOwned + ?Sized,{
    pub k: K::Owned,
    pub v: V::Owned,
}
```

## Fields§
§`k: K::Owned`

The key
§`v: V::Owned`

The value

## Implementations§