Package org.jbake.render

# Class DocumentsRenderer

java.lang.Object
org.jbake.render.DocumentsRenderer

All Implemented Interfaces:
`RenderingTool`

---

public class DocumentsRenderer
extends Object
implements RenderingTool

- 

## Constructor Summary

Constructors

Constructor
Description
`DocumentsRenderer()`
 

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

### DocumentsRenderer

public DocumentsRenderer()

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