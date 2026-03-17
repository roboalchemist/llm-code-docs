JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

boofcv.gui

## Interface BasicInterfaceListener

- 

---

```
public interface BasicInterfaceListener
```

Simple interface for a GUI to tell the main processing that it needs to render the display
 or reprocess that data.  Settings are accessed else where and more fine control over what
 has changed is not provided.
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**eventReprocess**()`
Data needs to be reprocessed using the new settings

`void`
`**eventUpdateGui**()`
The data does not need to be reprocessed but the user has requested that different
 information be displayed.

- 

  - 

### Method Detail

    - 

#### eventUpdateGui

```
void eventUpdateGui()
```

The data does not need to be reprocessed but the user has requested that different
 information be displayed.

    - 

#### eventReprocess

```
void eventReprocess()
```

Data needs to be reprocessed using the new settings

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**