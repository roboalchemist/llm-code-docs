druid

# Module lens

Source

## Structs§

ConstantA lens that always gives the same value and discards changes.Deref`Lens` for invoking `Deref` and `DerefMut` on a type.FieldLens accessing a member of some type using accessor functionsIdentityThe identity lens: the lens which does nothing, i.e. exposes exactly
the original value.InArcA `Lens` that exposes data within an `Arc` with copy-on-write semanticsIndex`Lens` for indexing containersMap`Lens` built from a getter and a setterRef`Lens` for invoking `AsRef` and `AsMut` on a type.Then`Lens` composed of two lenses joined togetherUnitA `Lens` that always yields ().

## Traits§

LensA lens is a datatype that gives access to a part of a larger
data structure.LensExtHelpers for manipulating `Lens`es
