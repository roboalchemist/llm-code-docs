# Package org.apache.cxf.service.invoker

---

package org.apache.cxf.service.invoker

- 

Related Packages

Package
Description
org.apache.cxf.service

This package and its sub packages contain classes relating to services and the CXF
service model

org.apache.cxf.service.invoker.spring
 
org.apache.cxf.service.factory
 
org.apache.cxf.service.model
 

- 

Class
Description
AbstractInvoker

Abstract implementation of Invoker.

BeanInvoker

Invoker for externally created service objects.

Factory

Represents an object factory.

FactoryInvoker

This invoker implementation calls a Factory to create the service object.

Invoker

Invokers control how a particular service is invoked.

MethodDispatcher

Provides functionality to map BindingOperations to Methods and
 vis a versa.

PerRequestFactory

Creates a new instance of the service object for each call to create().

PooledFactory

Factory the maintains a pool of instances that are used.

SessionFactory

Creates a new instance for each session.

SingletonFactory

Always returns a single instance of the bean.