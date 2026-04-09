# Package org.apache.cxf.databinding

---

package org.apache.cxf.databinding

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

org.apache.cxf.databinding.source
 
org.apache.cxf.databinding.stax
 

- 

Class
Description
AbstractDataBinding

Supply default implementations, as appropriate, for DataBinding.

AbstractInterceptorProvidingDataBinding
 
AbstractWrapperHelper

This wrapper helper will use reflection to handle the wrapped message

DataBinding
 
DataReader<T>

The 'read' side of the data binding abstraction of CXF.

DataWriter<T>

The 'write' side of the data binding abstraction of CXF.

WrapperCapableDatabinding

To create the WrapperHelper instance for the wrapper capable data binding

WrapperHelper

This wrapper helper will help to create a wrapper object with part elements or
  get a list of part elements from a wrapper object.