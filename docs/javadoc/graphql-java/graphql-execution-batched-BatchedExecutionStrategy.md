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

graphql.execution.batched

## Class BatchedExecutionStrategy

- java.lang.Object

- 

  - graphql.execution.ExecutionStrategy

  - 

    - graphql.execution.batched.BatchedExecutionStrategy

- 

---

Deprecated. 
This has been deprecated in favour of using `AsyncExecutionStrategy` and `DataLoaderDispatcherInstrumentation`

```
@PublicApi
 @Deprecated
public class BatchedExecutionStrategy
extends ExecutionStrategy
```

 BatchedExecutionStrategy has been deprecated in favour of `AsyncExecutionStrategy`
 and `DataLoaderDispatcherInstrumentation`.
 

 BatchedExecutionStrategy does not properly implement the graphql runtime specification.  Specifically it
 does not correctly handle non null fields and how they are to cascade up their parent fields.  It has proven
 an intractable problem to make this code handle these cases.
 

 See http://facebook.github.io/graphql/October2016/#sec-Errors-and-Non-Nullability
 

 We will remove it once we are sure the alternative is as least good as the BatchedExecutionStrategy.

 
 

 Execution Strategy that minimizes calls to the data fetcher when used in conjunction with `DataFetcher`s that have
 `DataFetcher.get(DataFetchingEnvironment)` methods annotated with `Batched`. See the javadoc comment on
 `Batched` for a more detailed description of batched data fetchers.
 

 The strategy runs a BFS over terms of the query and passes a list of all the relevant sources to the batched data fetcher.
 
 Normal DataFetchers can be used, however they will not see benefits of batching as they expect a single source object
 at a time.

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

`BatchedExecutionStrategy()`
Deprecated. 
 

`BatchedExecutionStrategy(DataFetcherExceptionHandler dataFetcherExceptionHandler)`
Deprecated. 
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description

`java.util.concurrent.CompletableFuture<ExecutionResult>`
`execute(ExecutionContext executionContext,
       ExecutionStrategyParameters parameters)`
Deprecated. 
This is the entry point to an execution strategy.

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

#### BatchedExecutionStrategy

```
public BatchedExecutionStrategy()
```

Deprecated. 

    - 

#### BatchedExecutionStrategy

```
public BatchedExecutionStrategy(DataFetcherExceptionHandler dataFetcherExceptionHandler)
```

Deprecated. 

  - 

### Method Detail

    - 

#### execute

```
public java.util.concurrent.CompletableFuture<ExecutionResult> execute(ExecutionContext executionContext,
                                                                       ExecutionStrategyParameters parameters)
```

Deprecated. 
Description copied from class: `ExecutionStrategy`
This is the entry point to an execution strategy.  It will be passed the fields to execute and get values for.

Specified by:
`execute` in class `ExecutionStrategy`
Parameters:
`executionContext` - contains the top level execution parameters
`parameters` - contains the parameters holding the fields to be executed and source object
Returns:
a promise to an `ExecutionResult`

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