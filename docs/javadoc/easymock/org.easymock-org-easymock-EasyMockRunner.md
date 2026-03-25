Module org.easymock
Package org.easymock

## Class EasyMockRunner

- java.lang.Object

- 

  - org.junit.runner.Runner

  - 

    - org.junit.runners.ParentRunner<org.junit.runners.model.FrameworkMethod>

    - 

      - org.junit.runners.BlockJUnit4ClassRunner

      - 

        - org.easymock.EasyMockRunner

- 

All Implemented Interfaces:
`org.junit.runner.Describable`, `org.junit.runner.manipulation.Filterable`, `org.junit.runner.manipulation.Orderable`, `org.junit.runner.manipulation.Sortable`

---

```
public class EasyMockRunner
extends org.junit.runners.BlockJUnit4ClassRunner
```

JUnit runner used to process `Mock` and `TestSubject` annotations. Note
 that this runner only works with JUnit 4.5 or higher

Since:
3.2
Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`EasyMockRunner​(Class<?> klass)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`protected org.junit.runners.model.Statement`
`withBefores​(org.junit.runners.model.FrameworkMethod method,
           Object target,
           org.junit.runners.model.Statement statement)`

We are required to override a deprecated method because it's the only way the perform
 the mock injection before the `@Before` of our class being called.

    - 

### Methods inherited from class org.junit.runners.BlockJUnit4ClassRunner

`collectInitializationErrors, computeTestMethods, createTest, createTest, describeChild, getChildren, getTestRules, isIgnored, methodBlock, methodInvoker, possiblyExpectingExceptions, rules, runChild, testName, validateConstructor, validateFields, validateInstanceMethods, validateNoNonStaticInnerClass, validateOnlyOneConstructor, validateTestMethods, validateZeroArgConstructor, withAfters, withPotentialTimeout`

    - 

### Methods inherited from class org.junit.runners.ParentRunner

`childrenInvoker, classBlock, classRules, createTestClass, filter, getDescription, getName, getRunnerAnnotations, getTestClass, order, run, runLeaf, setScheduler, sort, validatePublicVoidNoArgMethods, withAfterClasses, withBeforeClasses, withInterruptIsolation`

    - 

### Methods inherited from class org.junit.runner.Runner

`testCount`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### EasyMockRunner

```
public EasyMockRunner​(Class<?> klass)
               throws org.junit.runners.model.InitializationError
```

Throws:
`org.junit.runners.model.InitializationError`

  - 

### Method Detail

    - 

#### withBefores

```
protected org.junit.runners.model.Statement withBefores​(org.junit.runners.model.FrameworkMethod method,
                                                        Object target,
                                                        org.junit.runners.model.Statement statement)
```

We are required to override a deprecated method because it's the only way the perform
 the mock injection before the `@Before` of our class being called. Using a statement
 wouldn't work.

Overrides:
`withBefores` in class `org.junit.runners.BlockJUnit4ClassRunner`
Parameters:
`method` - test method class
`target` - test class instance
`statement` - current statement
Returns:
a statement to return to the caller