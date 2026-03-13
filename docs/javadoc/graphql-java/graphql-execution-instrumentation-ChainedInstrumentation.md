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

graphql.execution.instrumentation

## Class ChainedInstrumentation

- java.lang.Object

- 

  - graphql.execution.instrumentation.ChainedInstrumentation

- 

All Implemented Interfaces:
Instrumentation

---

```
@PublicApi
public class ChainedInstrumentation
extends java.lang.Object
implements Instrumentation
```

This allows you to chain together a number of `Instrumentation` implementations
 and run them in sequence.  The list order of instrumentation objects is always guaranteed to be followed and
 the `InstrumentationState` objects they create will be passed back to the originating
 implementation.

See Also:
`Instrumentation`

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`ChainedInstrumentation(Instrumentation... instrumentations)` 

`ChainedInstrumentation(java.util.List<Instrumentation> instrumentations)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`InstrumentationContext<ExecutionResult>`
`beginExecuteOperation(InstrumentationExecuteOperationParameters parameters)`
This is called just before the execution of the query operation is started.

`InstrumentationContext<ExecutionResult>`
`beginExecution(InstrumentationExecutionParameters parameters)`
This is called right at the start of query execution and its the first step in the instrumentation chain.

`ExecutionStrategyInstrumentationContext`
`beginExecutionStrategy(InstrumentationExecutionStrategyParameters parameters)`
This is called each time an `ExecutionStrategy` is invoked, which may be multiple times
 per query as the engine recursively descends down over the query.

`InstrumentationContext<ExecutionResult>`
`beginField(InstrumentationFieldParameters parameters)`
This is called just before a field is resolved into a value.

`InstrumentationContext<ExecutionResult>`
`beginFieldComplete(InstrumentationFieldCompleteParameters parameters)`
This is called just before the complete field is started.

`InstrumentationContext<java.lang.Object>`
`beginFieldFetch(InstrumentationFieldFetchParameters parameters)`
This is called just before a field `DataFetcher` is invoked.

`InstrumentationContext<ExecutionResult>`
`beginFieldListComplete(InstrumentationFieldCompleteParameters parameters)`
This is called just before the complete field list is started.

`InstrumentationContext<Document>`
`beginParse(InstrumentationExecutionParameters parameters)`
This is called just before a query is parsed.

`InstrumentationContext<ExecutionResult>`
`beginSubscribedFieldEvent(InstrumentationFieldParameters parameters)`
This is called each time a subscription field produces a new reactive stream event value and it needs to be mapped over via the graphql field subselection.

`InstrumentationContext<java.util.List<ValidationError>>`
`beginValidation(InstrumentationValidationParameters parameters)`
This is called just before the parsed query document is validated.

`InstrumentationState`
`createState(InstrumentationCreateStateParameters parameters)`
This will be called just before execution to create an object that is given back to all instrumentation methods
 to allow them to have per execution request state

`java.util.List<Instrumentation>`
`getInstrumentations()` 

`DataFetcher<?>`
`instrumentDataFetcher(DataFetcher<?> dataFetcher,
                     InstrumentationFieldFetchParameters parameters)`
This is called to instrument a `DataFetcher` just before it is used to fetch a field, allowing you
 to adjust what information is passed back or record information about specific data fetches.

`DocumentAndVariables`
`instrumentDocumentAndVariables(DocumentAndVariables documentAndVariables,
                              InstrumentationExecutionParameters parameters)`
This is called to instrument a `Document` and variables before it is used allowing you to adjust the query AST if you so desire

`ExecutionContext`
`instrumentExecutionContext(ExecutionContext executionContext,
                          InstrumentationExecutionParameters parameters)`
This is called to instrument a `ExecutionContext` before it is used to execute a query,
 allowing you to adjust the base data used.

`ExecutionInput`
`instrumentExecutionInput(ExecutionInput executionInput,
                        InstrumentationExecutionParameters parameters)`
This is called to instrument a `ExecutionInput` before it is used to parse, validate
 and execute a query, allowing you to adjust what query input parameters are used

`java.util.concurrent.CompletableFuture<ExecutionResult>`
`instrumentExecutionResult(ExecutionResult executionResult,
                         InstrumentationExecutionParameters parameters)`
This is called to allow instrumentation to instrument the execution result in some way

`GraphQLSchema`
`instrumentSchema(GraphQLSchema schema,
                InstrumentationExecutionParameters parameters)`
This is called to instrument a `GraphQLSchema` before it is used to parse, validate
 and execute a query, allowing you to adjust what types are used.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface graphql.execution.instrumentation.Instrumentation

`createState`

- 

  - 

### Constructor Detail

    - 

#### ChainedInstrumentation

```
public ChainedInstrumentation(java.util.List<Instrumentation> instrumentations)
```

    - 

#### ChainedInstrumentation

```
public ChainedInstrumentation(Instrumentation... instrumentations)
```

  - 

### Method Detail

    - 

#### getInstrumentations

```
public java.util.List<Instrumentation> getInstrumentations()
```

Returns:
the list of instrumentations in play

    - 

#### createState

```
public InstrumentationState createState(InstrumentationCreateStateParameters parameters)
```

Description copied from interface: `Instrumentation`
This will be called just before execution to create an object that is given back to all instrumentation methods
 to allow them to have per execution request state

Specified by:
`createState` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a state object that is passed to each method

    - 

#### beginExecution

```
public InstrumentationContext<ExecutionResult> beginExecution(InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called right at the start of query execution and its the first step in the instrumentation chain.

Specified by:
`beginExecution` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginParse

```
public InstrumentationContext<Document> beginParse(InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before a query is parsed.

Specified by:
`beginParse` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginValidation

```
public InstrumentationContext<java.util.List<ValidationError>> beginValidation(InstrumentationValidationParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before the parsed query document is validated.

Specified by:
`beginValidation` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginExecuteOperation

```
public InstrumentationContext<ExecutionResult> beginExecuteOperation(InstrumentationExecuteOperationParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before the execution of the query operation is started.

Specified by:
`beginExecuteOperation` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginExecutionStrategy

```
public ExecutionStrategyInstrumentationContext beginExecutionStrategy(InstrumentationExecutionStrategyParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called each time an `ExecutionStrategy` is invoked, which may be multiple times
 per query as the engine recursively descends down over the query.

Specified by:
`beginExecutionStrategy` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginSubscribedFieldEvent

```
public InstrumentationContext<ExecutionResult> beginSubscribedFieldEvent(InstrumentationFieldParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called each time a subscription field produces a new reactive stream event value and it needs to be mapped over via the graphql field subselection.

Specified by:
`beginSubscribedFieldEvent` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginField

```
public InstrumentationContext<ExecutionResult> beginField(InstrumentationFieldParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before a field is resolved into a value.

Specified by:
`beginField` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginFieldFetch

```
public InstrumentationContext<java.lang.Object> beginFieldFetch(InstrumentationFieldFetchParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before a field `DataFetcher` is invoked.

Specified by:
`beginFieldFetch` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginFieldComplete

```
public InstrumentationContext<ExecutionResult> beginFieldComplete(InstrumentationFieldCompleteParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before the complete field is started.

Specified by:
`beginFieldComplete` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### beginFieldListComplete

```
public InstrumentationContext<ExecutionResult> beginFieldListComplete(InstrumentationFieldCompleteParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called just before the complete field list is started.

Specified by:
`beginFieldListComplete` in interface `Instrumentation`
Parameters:
`parameters` - the parameters to this step
Returns:
a non null `InstrumentationContext` object that will be called back when the step ends

    - 

#### instrumentExecutionInput

```
public ExecutionInput instrumentExecutionInput(ExecutionInput executionInput,
                                               InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to instrument a `ExecutionInput` before it is used to parse, validate
 and execute a query, allowing you to adjust what query input parameters are used

Specified by:
`instrumentExecutionInput` in interface `Instrumentation`
Parameters:
`executionInput` - the execution input to be used
`parameters` - the parameters describing the field to be fetched
Returns:
a non null instrumented ExecutionInput, the default is to return to the same object

    - 

#### instrumentDocumentAndVariables

```
public DocumentAndVariables instrumentDocumentAndVariables(DocumentAndVariables documentAndVariables,
                                                           InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to instrument a `Document` and variables before it is used allowing you to adjust the query AST if you so desire

Specified by:
`instrumentDocumentAndVariables` in interface `Instrumentation`
Parameters:
`documentAndVariables` - the document and variables to be used
`parameters` - the parameters describing the execution
Returns:
a non null instrumented DocumentAndVariables, the default is to return to the same objects

    - 

#### instrumentSchema

```
public GraphQLSchema instrumentSchema(GraphQLSchema schema,
                                      InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to instrument a `GraphQLSchema` before it is used to parse, validate
 and execute a query, allowing you to adjust what types are used.

Specified by:
`instrumentSchema` in interface `Instrumentation`
Parameters:
`schema` - the schema to be used
`parameters` - the parameters describing the field to be fetched
Returns:
a non null instrumented GraphQLSchema, the default is to return to the same object

    - 

#### instrumentExecutionContext

```
public ExecutionContext instrumentExecutionContext(ExecutionContext executionContext,
                                                   InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to instrument a `ExecutionContext` before it is used to execute a query,
 allowing you to adjust the base data used.

Specified by:
`instrumentExecutionContext` in interface `Instrumentation`
Parameters:
`executionContext` - the execution context to be used
`parameters` - the parameters describing the field to be fetched
Returns:
a non null instrumented ExecutionContext, the default is to return to the same object

    - 

#### instrumentDataFetcher

```
public DataFetcher<?> instrumentDataFetcher(DataFetcher<?> dataFetcher,
                                            InstrumentationFieldFetchParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to instrument a `DataFetcher` just before it is used to fetch a field, allowing you
 to adjust what information is passed back or record information about specific data fetches.  Note
 the same data fetcher instance maybe presented to you many times and that data fetcher
 implementations widely vary.

Specified by:
`instrumentDataFetcher` in interface `Instrumentation`
Parameters:
`dataFetcher` - the data fetcher about to be used
`parameters` - the parameters describing the field to be fetched
Returns:
a non null instrumented DataFetcher, the default is to return to the same object

    - 

#### instrumentExecutionResult

```
public java.util.concurrent.CompletableFuture<ExecutionResult> instrumentExecutionResult(ExecutionResult executionResult,
                                                                                         InstrumentationExecutionParameters parameters)
```

Description copied from interface: `Instrumentation`
This is called to allow instrumentation to instrument the execution result in some way

Specified by:
`instrumentExecutionResult` in interface `Instrumentation`
Parameters:
`executionResult` - `CompletableFuture` of the result to instrument
`parameters` - the parameters to this step
Returns:
a new execution result completable future

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