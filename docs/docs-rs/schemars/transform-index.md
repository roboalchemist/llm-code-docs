schemars

# Module transform

Source

## Structs§

AddNullableAdds a `"nullable": true` property to schemas that allow `null` types.RecursiveTransformA helper struct that can wrap a non-recursive `Transform` (i.e. one that does not apply to
subschemas) into a recursive one.RemoveRefSiblingsRestructures JSON Schema objects so that the `$ref` property will never appear alongside any
other properties.ReplaceBoolSchemasReplaces boolean JSON Schemas with equivalent object schemas.ReplaceConstValueReplaces the `const` schema property with a single-valued `enum` property.ReplacePrefixItemsRename the `prefixItems` schema property to `items`.ReplaceUnevaluatedPropertiesReplaces the `unevaluatedProperties` schema property with the `additionalProperties` property,
adding properties from a schema’s subschemas to its `properties` where necessary.RestrictFormatsRemoves any `format` values that are not defined by the JSON Schema standard or explicitly
allowed by a custom list.SetSingleExampleRemoves the `examples` schema property and (if present) set its first value as the `example`
property.

## Traits§

TransformTrait used to modify a constructed schema and optionally its subschemas.

## Functions§

transform_subschemasApplies the given `Transform` to all direct subschemas of the `Schema`.
