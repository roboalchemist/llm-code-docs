# Package org.apache.cxf.common.spi

---

package org.apache.cxf.common.spi

- 

Related Packages

Package
Description
org.apache.cxf.common
 

- 

Class
Description
ClassGeneratorClassLoader

Class loader used to store and retrieve class generated during runtime to avoid class generation each time.

ClassGeneratorClassLoader.TypeHelperClassLoader
 
ClassLoaderProxyService
 
ClassLoaderService
 
GeneratedClassClassLoader

Class loader used to find class generated during build time to avoid class generation during runtime.

GeneratedClassClassLoader.TypeHelperClassLoader
 
GeneratedClassClassLoaderCapture

Implement this interface to store class generated in order during build phase
  inject it back before runtime to avoid class generation.

GeneratedNamespaceClassLoader

If class has been generated during build time
  (use @see org.apache.cxf.common.spi.GeneratedClassClassLoaderCapture capture to save bytes)
  you can set class loader to avoid class generation during runtime:
  bus.setExtension(new GeneratedNamespaceClassLoader(bus), NamespaceClassCreator.class);

NamespaceClassCreator

SPI interface to implement the proxy defining logic.

NamespaceClassGenerator