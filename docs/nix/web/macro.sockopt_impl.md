nix

# Macro sockopt_impl

Source

```
macro_rules! sockopt_impl {
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, bool) => { ... };
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, u8) => { ... };
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, usize) => { ... };
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, OwnedFd) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, bool) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, u8) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, usize) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, OwnedFd) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, bool) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, u8) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, usize) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, OwnedFd) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path,
     OsString<$array:ty>) => { ... };
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, $ty:ty) => { ... };
    ($(#[$attr:meta])* $name:ident, GetOnly, $level:expr, $flag:path, $ty:ty,
     $getter:ty) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, $ty:ty) => { ... };
    ($(#[$attr:meta])* $name:ident, SetOnly, $level:expr, $flag:path, $ty:ty,
     $setter:ty) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, $ty:ty,
     $getter:ty, $setter:ty) => { ... };
    ($(#[$attr:meta])* $name:ident, Both, $level:expr, $flag:path, $ty:ty) => { ... };
}
```

Available on **Unix** only.
