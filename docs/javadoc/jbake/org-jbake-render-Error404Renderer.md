Package org.jbake.render

# Class Error404Renderer

java.lang.Object
org.jbake.render.Error404Renderer

All Implemented Interfaces:
`RenderingTool`

---

public class Error404Renderer
extends Object
implements RenderingTool

- 

## Constructor Summary

Constructors

Constructor
Description
`Error404Renderer()`
 

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

### Error404Renderer

public Error404Renderer()

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