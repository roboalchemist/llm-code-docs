# Source: https://valibot.dev/api/MapPathItem.md

# MapPathItem

Map path item interface.

## Definition

- `MapPathItem`
  - `type` <Property {...properties.type} />
  - `origin` <Property {...properties.origin} />
  - `input` <Property {...properties.input} />
  - `key` <Property type='unknown' />
  - `value` <Property type='unknown' />

The `input` of a path item may differ from the `input` of its issue. This is because path items are subsequently added by parent schemas and are related to their input. Transformations of child schemas are not taken into account.
