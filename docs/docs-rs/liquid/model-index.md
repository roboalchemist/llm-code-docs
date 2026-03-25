liquid
# Module model
Source 
## Modules§
mapType representing a Liquid object, payload of the `Value::Object` variant
## Macros§
arrayA value::Array literal.objectA value::Object literal.scalarA value::Scalar literal.valueA value::Value literal.
## Structs§
DateLiquid’s native date only type.DateTimeLiquid’s native date + time type.KStringRefA reference to a UTF-8 encoded, immutable string.ObjectType representing a Liquid object, payload of the `Value::Object` variantObjectRenderHelper for `ObjectView::render`ObjectSourceHelper for `ObjectView::source`PathPath to a value in an `Object`.PathIterIterate over indexes in a `Value`’s `Path`.ScalarCowA Liquid scalar valueValueViewCmp`Value` comparison semantics for types implementing `ValueView`.
## Enums§
DisplayCowAbstract the lifetime of a `Display`.StateQueryable state for a `Value`.ValueAn enum to represent different value typesValueCowAbstract the lifetime of a `Value`.
## Traits§
ArrayViewAccessor for arrays.ObjectIndexOwned object indexObjectViewAccessor for objects.ValueViewAccessor for Values._ObjectViewAccessor for objects._ValueViewAccessor for Values.
## Functions§
findFind a `ValueView` nested in an `ObjectView`from_valueConvert a value into `T`.to_objectConvert a `T` into `liquid_core::model::Object`.to_scalarConvert a `T` into `liquid_core::model::Scalar`.to_valueConvert a `T` into `liquid_core::model::Value`.try_findFind a `ValueView` nested in an `ObjectView`
## Type Aliases§
ArrayType representing a Liquid array, payload of the `Value::Array` variantKStringA UTF-8 encoded, immutable string.KStringCowA reference to a UTF-8 encoded, immutable string.ScalarA Liquid scalar value
## Derive Macros§
ObjectViewValueView