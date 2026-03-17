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

boofcv.alg.feature.detect.template

## Class BaseTemplateIntensity<T extends ImageBase>

- java.lang.Object

- 

  - boofcv.alg.feature.detect.template.BaseTemplateIntensity<T>

- 

All Implemented Interfaces:
TemplateMatchingIntensity<T>

Direct Known Subclasses:
TemplateDiffSquared, TemplateNCC

---

```
public abstract class BaseTemplateIntensity<T extends ImageBase>
extends java.lang.Object
implements TemplateMatchingIntensity<T>
```

Base class which implements common elements
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected T`
`**image**` 

`protected T`
`**template**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BaseTemplateIntensity**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`protected abstract float`
`**evaluate**(int tl_x,
        int tl_y)`
Evaluate the template at the specified location.

`ImageFloat32`
`**getIntensity**()`
Contains results of template matching.

`int`
`**getOffsetX**()`
Offset from template's top left corner x-coordinate

`int`
`**getOffsetY**()`
Offset from template's top left corner y-coordinate

`void`
`**process**(T image,
       T template)`
Matches the template to the image and computes an intensity image.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface boofcv.alg.feature.detect.template.TemplateMatchingIntensity

`isBorderProcessed`

- 

  - 

### Field Detail

    - 

#### image

```
protected T extends ImageBase image
```

    - 

#### template

```
protected T extends ImageBase template
```

  - 

### Constructor Detail

    - 

#### BaseTemplateIntensity

```
public BaseTemplateIntensity()
```

  - 

### Method Detail

    - 

#### process

```
public void process(T image,
           T template)
```

**Description copied from interface: `TemplateMatchingIntensity`**
Matches the template to the image and computes an intensity image.

**Specified by:**
`process` in interface `TemplateMatchingIntensity<T extends ImageBase>`
Parameters:`image` - Input image. Not modified.`template` - Template image.  Must be equal to or smaller than the input image. Not modified.

    - 

#### evaluate

```
protected abstract float evaluate(int tl_x,
             int tl_y)
```

Evaluate the template at the specified location.
Parameters:`tl_x` - Template's top left corner x-coordinate`tl_y` - Template's top left corner y-coordinate
Returns:match value with better matches having a more positive value

    - 

#### getIntensity

```
public ImageFloat32 getIntensity()
```

**Description copied from interface: `TemplateMatchingIntensity`**
Contains results of template matching.  Higher intensity values correspond to a better match.
 Local matches can be found using `NonMaxSuppression`.
 See comment about processing the image border.

**Specified by:**
`getIntensity` in interface `TemplateMatchingIntensity<T extends ImageBase>`
Returns:Feature intensity

    - 

#### getOffsetX

```
public int getOffsetX()
```

**Description copied from interface: `TemplateMatchingIntensity`**
Offset from template's top left corner x-coordinate

**Specified by:**
`getOffsetX` in interface `TemplateMatchingIntensity<T extends ImageBase>`
Returns:Offset in pixels

    - 

#### getOffsetY

```
public int getOffsetY()
```

**Description copied from interface: `TemplateMatchingIntensity`**
Offset from template's top left corner y-coordinate

**Specified by:**
`getOffsetY` in interface `TemplateMatchingIntensity<T extends ImageBase>`
Returns:Offset in pixels

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