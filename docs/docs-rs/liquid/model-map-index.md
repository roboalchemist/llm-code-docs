liquid::model
# Module map
Source 
## Structs§
IntoIterAn owning iterator over a liquid_core::model::Object’s entries.IterAn iterator over a liquid_core::model::Object’s entries.IterMutA mutable iterator over a liquid_core::model::Object’s entries.KeysAn iterator over a liquid_core::model::Object’s keys.ObjectType representing a Liquid object, payload of the `Value::Object` variantOccupiedEntryAn occupied Entry. It is part of the `Entry` enum.VacantEntryA vacant Entry. It is part of the `Entry` enum.ValuesAn iterator over a liquid_core::model::Object’s values.ValuesMutA mutable iterator over a liquid_core::model::Object’s values.
## Enums§
EntryA view into a single entry in a map, which may either be vacant or occupied.
This enum is constructed from the `entry` method on `Object`.