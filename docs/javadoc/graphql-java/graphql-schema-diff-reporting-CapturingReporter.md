JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.schema.diff.reporting

## Class CapturingReporter

- java.lang.Object

- 

  - graphql.schema.diff.reporting.CapturingReporter

- 

All Implemented Interfaces:
DifferenceReporter

---

```
@PublicApi
public class CapturingReporter
extends java.lang.Object
implements DifferenceReporter
```

A reporter that captures all the difference events as they occur

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`CapturingReporter()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`int`
`getBreakageCount()` 

`java.util.List<DiffEvent>`
`getBreakages()` 

`int`
`getDangerCount()` 

`java.util.List<DiffEvent>`
`getDangers()` 

`java.util.List<DiffEvent>`
`getEvents()` 

`int`
`getInfoCount()` 

`java.util.List<DiffEvent>`
`getInfos()` 

`void`
`onEnd()`
Called when the difference operation if finished

`void`
`report(DiffEvent differenceEvent)`
Called to report a difference

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### CapturingReporter

```
public CapturingReporter()
```

  - 

### Method Detail

    - 

#### report

```
public void report(DiffEvent differenceEvent)
```

Description copied from interface: `DifferenceReporter`
Called to report a difference

Specified by:
`report` in interface `DifferenceReporter`
Parameters:
`differenceEvent` - the event describing the difference

    - 

#### onEnd

```
public void onEnd()
```

Description copied from interface: `DifferenceReporter`
Called when the difference operation if finished

Specified by:
`onEnd` in interface `DifferenceReporter`

    - 

#### getEvents

```
public java.util.List<DiffEvent> getEvents()
```

    - 

#### getInfos

```
public java.util.List<DiffEvent> getInfos()
```

    - 

#### getBreakages

```
public java.util.List<DiffEvent> getBreakages()
```

    - 

#### getDangers

```
public java.util.List<DiffEvent> getDangers()
```

    - 

#### getInfoCount

```
public int getInfoCount()
```

    - 

#### getBreakageCount

```
public int getBreakageCount()
```

    - 

#### getDangerCount

```
public int getDangerCount()
```

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method