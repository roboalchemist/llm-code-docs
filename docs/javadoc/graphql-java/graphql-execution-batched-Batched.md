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

- Field | 

- Required | 

- Optional

- Detail: 

- Field | 

- Element

graphql.execution.batched

## Annotation Type Batched

- 

---

Deprecated. 
This has been deprecated in favour of using `AsyncExecutionStrategy` and `DataLoaderDispatcherInstrumentation`

```
@Target(value=METHOD)
 @Retention(value=RUNTIME)
 @Deprecated
public @interface Batched
```

 When placed on `DataFetcher.get(DataFetchingEnvironment)`, indicates that this DataFetcher is batched.
 This annotation must be used in conjunction with `BatchedExecutionStrategy`. Batching is valuable in many
 situations, such as when a `DataFetcher` must make a network or file system request.
 
 

 When a `DataFetcher` is batched, the `DataFetchingEnvironment.getSource()` method is
 guaranteed to return a `List`.  The `DataFetcher.get(DataFetchingEnvironment)`
 method MUST return a parallel `List` which is equivalent to running a `DataFetcher`
 over each input element individually.
 
 

 Using the `Batched` annotation is equivalent to implementing `BatchedDataFetcher` instead of `DataFetcher`.
 It is preferred to use the `Batched` annotation.
 
 For example, the following two `DataFetcher` objects are interchangeable if used with a
 `BatchedExecutionStrategy`.
 

```

 
 new DataFetcher() {
    @Override
    @Batched
   public Object get(DataFetchingEnvironment environment) {
      List<String> retVal = new ArrayList<>();
      for (String s: (List<String>) environment.getSource()) {}
       retVal.add(s + environment.getArgument("text"));
     
     return retVal;
   }
 }
 
 
```

 

```

 
 new DataFetcher() {
    @Override
   public Object get(DataFetchingEnvironment e) {
     return ((String)e.getSource()) + e.getArgument("text");
   }
 }
 
 
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

- Field | 

- Required | 

- Optional

- Detail: 

- Field | 

- Element