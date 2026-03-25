# Package org.apache.cxf.bus.extension

---

package org.apache.cxf.bus.extension

- 

Related Packages

Package
Description
org.apache.cxf.bus
 
org.apache.cxf.bus.managers
 
org.apache.cxf.bus.resource
 
org.apache.cxf.bus.spring
 

- 

Class
Description
Extension
 
ExtensionException
 
ExtensionManager
 
ExtensionManagerBus

This bus uses CXF's built in extension manager to load components
 (as opposed to using the Spring bus implementation).

ExtensionManagerBus.ExtensionFinder
 
ExtensionManagerImpl
 
ExtensionRegistry

Static registry of extensions that are loaded in addition to the
 extensions the Bus will automatically detect.

TextExtensionFragmentParser