Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusFuture<T>

java.lang.Object
java.util.concurrent.CompletableFuture<T>
org.glassfish.tyrus.core.TyrusFuture<T>

All Implemented Interfaces:
`CompletionStage<T>`, `Future<T>`

---

public class TyrusFuture<T>
extends CompletableFuture<T>
Tyrus `Future` implementation.

-

## Nested Class Summary

## Nested classes/interfaces inherited from class java.util.concurrent.CompletableFuture

`CompletableFuture.AsynchronousCompletionTask`

## Nested classes/interfaces inherited from interface java.util.concurrent.Future

`Future.State`

-

## Constructor Summary

Constructors

Constructor
Description
`TyrusFuture()`

-

## Method Summary

Modifier and Type
Method
Description
`void`
`setFailure(Throwable throwable)`

Sets the failure result of message writing process.

`void`
`setResult(T result)`

Sets the result of the message writing process.

### Methods inherited from class java.util.concurrent.CompletableFuture

`acceptEither, acceptEitherAsync, acceptEitherAsync, allOf, anyOf, applyToEither, applyToEitherAsync, applyToEitherAsync, cancel, complete, completeAsync, completeAsync, completedFuture, completedStage, completeExceptionally, completeOnTimeout, copy, defaultExecutor, delayedExecutor, delayedExecutor, exceptionally, exceptionallyAsync, exceptionallyAsync, exceptionallyCompose, exceptionallyComposeAsync, exceptionallyComposeAsync, exceptionNow, failedFuture, failedStage, get, get, getNow, getNumberOfDependents, handle, handleAsync, handleAsync, isCancelled, isCompletedExceptionally, isDone, join, minimalCompletionStage, newIncompleteFuture, obtrudeException, obtrudeValue, orTimeout, resultNow, runAfterBoth, runAfterBothAsync, runAfterBothAsync, runAfterEither, runAfterEitherAsync, runAfterEitherAsync, runAsync, runAsync, state, supplyAsync, supplyAsync, thenAccept, thenAcceptAsync, thenAcceptAsync, thenAcceptBoth, thenAcceptBothAsync, thenAcceptBothAsync, thenApply, thenApplyAsync, thenApplyAsync, thenCombine, thenCombineAsync, thenCombineAsync, thenCompose, thenComposeAsync, thenComposeAsync, thenRun, thenRunAsync, thenRunAsync, toCompletableFuture, toString, whenComplete, whenCompleteAsync, whenCompleteAsync`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### TyrusFuture

public TyrusFuture()

-

## Method Details

-

### setResult

public void setResult(T result)
Sets the result of the message writing process.

Parameters:
`result` - result

-

### setFailure

public void setFailure(Throwable throwable)
Sets the failure result of message writing process.

Parameters:
`throwable` - throwable.
