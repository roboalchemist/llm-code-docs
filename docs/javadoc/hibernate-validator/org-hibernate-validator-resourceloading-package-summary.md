# Package org.hibernate.validator.resourceloading

---

package org.hibernate.validator.resourceloading

ResourceBundleLocator interface and its various implementations.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

- 

Classes

Class
Description
AggregateResourceBundleLocator

A `ResourceBundleLocator` implementation that provides access
to multiple source `ResourceBundle`s by merging them into one
aggregated bundle.

CachingResourceBundleLocator

A `ResourceBundleLocator` implementation that wraps around another
locator and caches values retrieved from that locator.

DelegatingResourceBundleLocator

Abstract base for all `ResourceBundleLocator` implementations, that
wish to delegate to some other locator.

PlatformResourceBundleLocator

A resource bundle locator, that loads resource bundles by invoking `ResourceBundle.loadBundle(String, Local, ClassLoader)`.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved