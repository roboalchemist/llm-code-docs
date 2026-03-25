JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.execution

## Class AbstractAsyncExecutionStrategy

- java.lang.Object

- 

  - graphql.execution.ExecutionStrategy

  - 

    - graphql.execution.AbstractAsyncExecutionStrategy

- 

Direct Known Subclasses:
AsyncExecutionStrategy, AsyncSerialExecutionStrategy

---

```
@PublicSpi
public abstract class AbstractAsyncExecutionStrategy
extends ExecutionStrategy
```

- 

  - 

### Field Summary

    - 

### Fields inherited from class graphql.execution.ExecutionStrategy

`dataFetcherExceptionHandler, executionStepInfoFactory, fieldCollector, valuesResolver`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractAsyncExecutionStrategy()` 

`AbstractAsyncExecutionStrategy(DataFetcherExceptionHandler dataFetcherExceptionHandler)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected java.util.function.BiConsumer<java.util.List<ExecutionResult>,java.lang.Throwable>`
`handleResults(ExecutionContext executionContext,
             java.util.List<java.lang.String> fieldNames,
             java.util.concurrent.CompletableFuture<ExecutionResult> overallResult)` 

    - 

### Methods inherited from class graphql.execution.ExecutionStrategy

`assertNonNullFieldPrecondition, assertNonNullFieldPrecondition, completeField, completeValue, completeValueForEnum, completeValueForList, completeValueForList, completeValueForNull, completeValueForObject, completeValueForScalar, createExecutionStepInfo, execute, fetchField, getFieldDef, getFieldDef, getNormalizedField, handleFetchingException, handleNonNullException, mkNameForPath, mkNameForPath, mkNameForPath, resolveField, resolveFieldWithInfo, resolveType, toIterable, toIterable, unboxPossibleDataFetcherResult`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AbstractAsyncExecutionStrategy

```
public AbstractAsyncExecutionStrategy()
```

    - 

#### AbstractAsyncExecutionStrategy

```
public AbstractAsyncExecutionStrategy(DataFetcherExceptionHandler dataFetcherExceptionHandler)
```

  - 

### Method Detail

    - 

#### handleResults

```
protected java.util.function.BiConsumer<java.util.List<ExecutionResult>,java.lang.Throwable> handleResults(ExecutionContext executionContext,
                                                                                                           java.util.List<java.lang.String> fieldNames,
                                                                                                           java.util.concurrent.CompletableFuture<ExecutionResult> overallResult)
```

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method