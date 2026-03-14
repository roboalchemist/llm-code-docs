Package org.jbake.render

# Class FeedRenderer

java.lang.Object
org.jbake.render.FeedRenderer

All Implemented Interfaces:
`RenderingTool`

---

public class FeedRenderer
extends Object
implements RenderingTool

- 

## Constructor Summary

Constructors

Constructor
Description
`FeedRenderer()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`render(Renderer renderer,
 ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config)`
 
`int`
`render(Renderer renderer,
 ContentStore db,
 JBakeConfiguration config)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### FeedRenderer

public FeedRenderer()

- 

## Method Details

  - 

### render

public int render(Renderer renderer,
 ContentStore db,
 JBakeConfiguration config)
           throws RenderingException

Specified by:
`render` in interface `RenderingTool`
Throws:
`RenderingException`

  - 

### render

public int render(Renderer renderer,
 ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config)
           throws RenderingException

Specified by:
`render` in interface `RenderingTool`
Throws:
`RenderingException`