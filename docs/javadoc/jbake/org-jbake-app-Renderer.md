Package org.jbake.app

# Class Renderer

java.lang.Object
org.jbake.app.Renderer

---

public class Renderer
extends Object
Render output to a file.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`class `
`Renderer.ModelRenderingConfig`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`Renderer(ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config)`

Deprecated.
Use `Renderer(ContentStore, JBakeConfiguration)` instead.

`Renderer(ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config,
 DelegatingTemplateEngine renderingEngine)`

Deprecated.
Use `Renderer(ContentStore, JBakeConfiguration, DelegatingTemplateEngine)` instead.

`Renderer(ContentStore db,
 JBakeConfiguration config)`

Creates a new instance of Renderer with supplied references to folders.

`Renderer(ContentStore db,
 JBakeConfiguration config,
 DelegatingTemplateEngine renderingEngine)`

Creates a new instance of Renderer with supplied references to folders and the instance of DelegatingTemplateEngine to use.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`render(DocumentModel content)`

Render the supplied content to a file.

`void`
`renderArchive(String archiveFile)`

Render an archive file using the supplied content.

`void`
`renderError404(String errorFile)`

Render an 404 file using the predefined template.

`void`
`renderFeed(String feedFile)`

Render an XML feed file using the supplied content.

`void`
`renderIndex(String indexFile)`

Render an index file using the supplied content.

`void`
`renderIndexPaging(String indexFile)`
 
`void`
`renderSitemap(String sitemapFile)`

Render an XML sitemap file using the supplied content.

`int`
`renderTags(String tagPath)`

Render tag files using the supplied content.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### Renderer

@Deprecated
public Renderer(ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config)
Deprecated.
Use `Renderer(ContentStore, JBakeConfiguration)` instead.
 Creates a new instance of Renderer with supplied references to folders.

Parameters:
`db` - The database holding the content
`destination` - The destination folder
`templatesPath` - The templates folder
`config` - Project configuration

  - 

### Renderer

@Deprecated
public Renderer(ContentStore db,
 File destination,
 File templatesPath,
 org.apache.commons.configuration2.CompositeConfiguration config,
 DelegatingTemplateEngine renderingEngine)
Deprecated.
Use `Renderer(ContentStore, JBakeConfiguration, DelegatingTemplateEngine)` instead.
 Creates a new instance of Renderer with supplied references to folders and the instance of DelegatingTemplateEngine to use.

Parameters:
`db` - The database holding the content
`destination` - The destination folder
`templatesPath` - The templates folder
`config` - Project configuration
`renderingEngine` - The instance of DelegatingTemplateEngine to use

  - 

### Renderer

public Renderer(ContentStore db,
 JBakeConfiguration config)
Creates a new instance of Renderer with supplied references to folders.

Parameters:
`db` - The database holding the content
`config` - Project configuration

  - 

### Renderer

public Renderer(ContentStore db,
 JBakeConfiguration config,
 DelegatingTemplateEngine renderingEngine)
Creates a new instance of Renderer with supplied references to folders and the instance of DelegatingTemplateEngine to use.

Parameters:
`db` - The database holding the content
`config` - The application specific configuration
`renderingEngine` - The instance of DelegatingTemplateEngine to use

- 

## Method Details

  - 

### render

public void render(DocumentModel content)
            throws Exception
Render the supplied content to a file.

Parameters:
`content` - The content to renderDocument
Throws:
`Exception` - if IOException or SecurityException are raised

  - 

### renderIndex

public void renderIndex(String indexFile)
                 throws Exception
Render an index file using the supplied content.

Parameters:
`indexFile` - The name of the output file
Throws:
`Exception` - if IOException or SecurityException are raised

  - 

### renderIndexPaging

public void renderIndexPaging(String indexFile)
                       throws Exception

Throws:
`Exception`

  - 

### renderSitemap

public void renderSitemap(String sitemapFile)
                   throws Exception
Render an XML sitemap file using the supplied content.

Parameters:
`sitemapFile` - configuration for site map
Throws:
`Exception` - if can't create correct default rendering config
See Also:

    - About Sitemaps

    - Sitemap protocol

  - 

### renderFeed

public void renderFeed(String feedFile)
                throws Exception
Render an XML feed file using the supplied content.

Parameters:
`feedFile` - The name of the output file
Throws:
`Exception` - if default rendering configuration is not loaded correctly

  - 

### renderArchive

public void renderArchive(String archiveFile)
                   throws Exception
Render an archive file using the supplied content.

Parameters:
`archiveFile` - The name of the output file
Throws:
`Exception` - if default rendering configuration is not loaded correctly

  - 

### renderError404

public void renderError404(String errorFile)
                    throws Exception
Render an 404 file using the predefined template.

Parameters:
`errorFile` - The name of the output file
Throws:
`Exception` - if default rendering configuration is not loaded correctly

  - 

### renderTags

public int renderTags(String tagPath)
               throws Exception
Render tag files using the supplied content.

Parameters:
`tagPath` - The output path
Returns:
Number of rendered tags
Throws:
`Exception` - if cannot render tags correctly