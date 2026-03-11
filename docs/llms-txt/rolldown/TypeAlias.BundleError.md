# Source: https://rolldown.rs/reference/TypeAlias.BundleError.md

---
url: /reference/TypeAlias.BundleError.md
---
# Type Alias: BundleError

* **Type**: `Error` & { `errors?`: [`RolldownError`](Interface.RolldownError.md)\[]; }

The error type that is thrown by Rolldown for the whole build.

## Type Declaration

### errors?

* **Type**: [`RolldownError`](Interface.RolldownError.md)\[]
* **Optional**

The individual errors that happened during the build.

This property is a getter to avoid unnecessary expansion of error details when the error is logged.
