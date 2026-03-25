typebox
# Module value 
Source 
## Re-exports§
`pub use cast::cast;``pub use check::check;``pub use check::check_with_errors;``pub use clean::clean;``pub use clone::clone;``pub use create::create;``pub use delta::delta;``pub use delta::diff_summary;``pub use delta::Delta;``pub use delta::Edit;``pub use equal::equal;``pub use hash::hash_fnv1a;``pub use mutate::mutate;``pub use patch::patch;``pub use pointer::delete_pointer;``pub use pointer::get_pointer;``pub use pointer::get_pointer_mut;``pub use pointer::has_pointer;``pub use pointer::set_pointer;`
## Modules§
castValue coercion to match schemas.checkValue validation against schemas.cleanRemove extraneous properties from values.cloneDeep clone values.createDefault value generation from schemas.deltaDiff computation between values.equalStructural equality comparison.hashFNV-1A 64-bit hash implementation for `Value`.mutateIn-place deep mutation for `Value`.patchApply delta edits to values.pointerJSON Pointer (RFC6901) operations for `Value`.
## Structs§
ObjectBuilderBuilder for constructing object values.
## Enums§
ValueA dynamically-typed value with schema-aware operations.