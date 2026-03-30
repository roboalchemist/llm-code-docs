# Package org.apache.cxf.resource

---

package org.apache.cxf.resource

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
ClassLoaderResolver
 
ClasspathResolver

Resolve resources from the system class path.

DefaultResourceManager
 
ExtendedURIResolver
 
ObjectTypeResolver
 
PropertiesResolver
 
ResourceManager

Locates resources that are used at runtime.

ResourceResolver

Resolves resource.

SinglePropertyResolver
 
URIResolver

Resolves a File, classpath resource, or URL according to the follow rules:
 
 Check to see if a file exists, relative to the base URI.
 If the file doesn't exist, check the classpath
 If the classpath doesn't exist, try to create URL from the URI.