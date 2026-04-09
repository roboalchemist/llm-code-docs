# Package io.vavr.concurrent

---

package io.vavr.concurrent

This package contains basic building blocks for creating fast, asynchronous, non-blocking parallel code.
 

 A Future represents an asynchronous task. It is a placeholder for a
 value that becomes available at some point. With the help of `Future` we efficiently perform many non-blocking
 operations in parallel. The value of a Future is supplied concurrently and can subsequently be used. Multiple
 concurrent tasks represented by Futures can be composed to a single Future.

- 

Related Packages

Package
Description
io.vavr

Beside `API` the io.vavr package contains core types like (Checked)Functions and Tuples.

io.vavr.collection

Purely functional collections based on Traversable.

io.vavr.control

Control structures like the disjoint union type Either, the optional value type
 Option and Try for exception handling.

- 

Interfaces

Class
Description
Future<T>

Represents the result of an asynchronous computation that becomes available at some point in the future.

Promise<T>

A `Promise` is a write-once container for a read-only `Future`, allowing the underlying `Future`
 to be completed with a value or an exception.