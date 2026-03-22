# Class ReactiveWebMergedContextConfiguration

java.lang.Object
org.springframework.test.context.MergedContextConfiguration
org.springframework.boot.test.context.ReactiveWebMergedContextConfiguration

All Implemented Interfaces:
`Serializable`

---

public class ReactiveWebMergedContextConfiguration
extends org.springframework.test.context.MergedContextConfiguration
Encapsulates the *merged* context configuration declared on a test class and all
of its superclasses for a reactive web application.

Since:
2.0.0
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ReactiveWebMergedContextConfiguration(org.springframework.test.context.MergedContextConfiguration mergedConfig)`
 

- 

## Method Summary

### Methods inherited from class org.springframework.test.context.MergedContextConfiguration

`equals, getActiveProfiles, getClasses, getContextCustomizers, getContextInitializerClasses, getContextLoader, getLocations, getParent, getParentApplicationContext, getPropertySourceDescriptors, getPropertySourceLocations, getPropertySourceProperties, getTestClass, hasClasses, hashCode, hasLocations, hasResources, nullSafeClassName, processStrings, toString`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### ReactiveWebMergedContextConfiguration

public ReactiveWebMergedContextConfiguration(org.springframework.test.context.MergedContextConfiguration mergedConfig)