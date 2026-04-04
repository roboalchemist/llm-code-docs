# Source: https://docs.slatejs.org/api/locations.md

# Location Types

The `Location` interface is a union of the ways to refer to a specific location in a Slate document: paths, points or ranges. Methods will often accept a `Location` instead of requiring only a `Path`, `Point` or `Range`.

```typescript
type Location = Path | Point | Range
```

* [Location](https://docs.slatejs.org/api/locations/location)
* [Path](https://docs.slatejs.org/api/locations/path)
* [PathRef](https://docs.slatejs.org/api/locations/path-ref)
* [Point](https://docs.slatejs.org/api/locations/point)
* [PointEntry](https://docs.slatejs.org/api/locations/point-entry)
* [PointRef](https://docs.slatejs.org/api/locations/point-ref)
* [Range](https://docs.slatejs.org/api/locations/range)
* [RangeRef](https://docs.slatejs.org/api/locations/range-ref)
* [Span](https://docs.slatejs.org/api/locations/span)
