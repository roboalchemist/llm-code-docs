# Package org.apache.cxf.binding

---

package org.apache.cxf.binding

Interfaces for protocol bindings and their factories.

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
AbstractBindingFactory
 
Binding

A Binding provides interceptors and message creation logic for a
 specific protocol binding.

BindingConfiguration

A configuration for a binding.

BindingFactory

A factory interface for creating Bindings from BindingInfo metadata.

BindingFactoryManager

The manager interface represents a repository for accessing
 `BindingFactory`s.