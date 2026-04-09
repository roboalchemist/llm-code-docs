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

## Class ChainedReporter

- java.lang.Object

- 

  - graphql.schema.diff.reporting.ChainedReporter

- 

All Implemented Interfaces:
DifferenceReporter

---

```
@PublicApi
public class ChainedReporter
extends java.lang.Object
implements DifferenceReporter
```

A reporter that chains together one or more difference reporters

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ChainedReporter(DifferenceReporter... reporters)` 

`ChainedReporter(java.util.List<DifferenceReporter> reporters)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

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

#### ChainedReporter

```
public ChainedReporter(DifferenceReporter... reporters)
```

    - 

#### ChainedReporter

```
public ChainedReporter(java.util.List<DifferenceReporter> reporters)
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