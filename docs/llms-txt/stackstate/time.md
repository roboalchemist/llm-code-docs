# Source: https://archivedocs.stackstate.com/5.1/develop/reference/scripting/script-apis/time.md

# Time - script API

Time API offers helper functions to manipulate with [time type](https://archivedocs.stackstate.com/5.1/develop/reference/scripting/time-in-scripts) in StackState scripts.

## Function: `Time.currentTimeSlice()`

Returns a time slice for the current timestamp

### Examples

```
Time.currentTimeSlice().then { slice -> 
    Topology.query('environments in ("Production")')
    .at(slice)
    .components()
    .thenCollect { component -> 
       Component
       .withId(component.id)
       .at(slice)
       .get()
    } 
}
```

## Function: `Time.format(instant: Instant, pattern: String)`

Format an instant to string using the given formatting pattern

### Args

* `instant` - [an instant type representation](https://archivedocs.stackstate.com/5.1/develop/reference/time-in-scripts#type-instant).
* `pattern` - [Java date formatting pattern](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/format/DateTimeFormatter.html#patterns)

### Examples

Format an instant to ISO 8601 time

```
Time.format(1577966400000, "yyyy-MM-dd'T'HH:mm:ss'Z'")
```

## Function: `Time.epochMs(instant: Instant)`

### Args

* `instant` - [an instant type representation](https://archivedocs.stackstate.com/5.1/develop/reference/time-in-scripts#type-instant).

### Examples

Convert a string timestamp to epoch

```
Time.epochMs("2011-12-03T10:15:30Z")
```
