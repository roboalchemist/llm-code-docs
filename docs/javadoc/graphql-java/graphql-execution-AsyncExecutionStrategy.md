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

## Class AsyncExecutionStrategy

- java.lang.Object

- 

  - graphql.execution.ExecutionStrategy

  - 

    - graphql.execution.AbstractAsyncExecutionStrategy

    - 

      - graphql.execution.AsyncExecutionStrategy

- 

---

```
@PublicApi
public class AsyncExecutionStrategy
extends AbstractAsyncExecutionStrategy
```

The standard graphql execution strategy that runs fields asynchronously non-blocking.

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

`AsyncExecutionStrategy()`
The standard graphql execution strategy that runs fields asynchronously

`AsyncExecutionStrategy(DataFetcherExceptionHandler exceptionHandler)`
Creates a execution strategy that uses the provided exception handler

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`java.util.concurrent.CompletableFuture<ExecutionResult>`
`execute(ExecutionContext executionContext,
       ExecutionStrategyParameters parameters)`
This is the entry point to an execution strategy.

    - 

### Methods inherited from class graphql.execution.AbstractAsyncExecutionStrategy

`handleResults`

    - 

### Methods inherited from class graphql.execution.ExecutionStrategy

`assertNonNullFieldPrecondition, assertNonNullFieldPrecondition, completeField, completeValue, completeValueForEnum, completeValueForList, completeValueForList, completeValueForNull, completeValueForObject, completeValueForScalar, createExecutionStepInfo, fetchField, getFieldDef, getFieldDef, getNormalizedField, handleFetchingException, handleNonNullException, mkNameForPath, mkNameForPath, mkNameForPath, resolveField, resolveFieldWithInfo, resolveType, toIterable, toIterable, unboxPossibleDataFetcherResult`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AsyncExecutionStrategy

```
public AsyncExecutionStrategy()
```

The standard graphql execution strategy that runs fields asynchronously

    - 

#### AsyncExecutionStrategy

```
public AsyncExecutionStrategy(DataFetcherExceptionHandler exceptionHandler)
```

Creates a execution strategy that uses the provided exception handler

Parameters:
`exceptionHandler` - the exception handler to use

  - 

### Method Detail

    - 

#### execute

```
public java.util.concurrent.CompletableFuture<ExecutionResult> execute(ExecutionContext executionContext,
                                                                       ExecutionStrategyParameters parameters)
                                                                throws NonNullableFieldWasNullException
```

Description copied from class: `ExecutionStrategy`
This is the entry point to an execution strategy.  It will be passed the fields to execute and get values for.

Specified by:
`execute` in class `ExecutionStrategy`
Parameters:
`executionContext` - contains the top level execution parameters
`parameters` - contains the parameters holding the fields to be executed and source object
Returns:
a promise to an `ExecutionResult`
Throws:
`NonNullableFieldWasNullException` - in the future if a non null field resolves to a null value

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