# Storing call traces

MonkeyType operates in two phases: call tracing and stub generation. You first run some code under MonkeyType tracing and store the traced calls. You can do this repeatedly, maybe even sampled in production continually so you always have up-to-date traces available. Then whenever you need, you run `monkeytype stub` or `monkeytype apply` to generate annotations based on types from the recorded traces.

In order to do this, MonkeyType needs a backing store for the recorded call traces. By default it will use `SQLiteStore`, which stores traces in a local SQLite database file. But you can write your own `CallTraceStore` subclass to store traces in whatever data store works best for you, and return an instance of your custom store from the `trace_store` method of your `Config` class.

## CallTraceStore interface

The `CallTraceStore` base class defines the interface that all call-trace stores must implement. The `SQLiteStore` subclass provides a useful example implementation of the `CallTraceStore` interface.

### CallTraceStore

#### `make_store(connection_string: str) -> CallTraceStore`

Create and return an instance of the store, given a connection string.

The format and interpretation of the connection string is entirely up to the store class. Typically it might be e.g. a URI like `mysql://john:pass@localhost:3306/my_db`.

#### `add(traces: Iterable[CallTrace]) -> None`

Store one or more `CallTrace` instances.

Implementations of this method will probably find the `serialize_traces` function useful.

#### `filter(module: str, qualname_prefix: Optional[str] = None, limit: int = 2000) -> List[CallTraceThunk]`

Query call traces from the call trace store. The `module` argument should be provided as a dotted Python import path (e.g. `some.module`).

The store should return the most recent `limit` traces available for the given `module` and `qualname`.

The returned `CallTraceThunk` instances can be any object that implements a `to_trace` zero-argument method returning a `CallTrace` instance. This allows callers of `filter` to handle deserialization errors as desired per-trace.

Most stores will choose to return instances of `CallTraceRow`, which implements a `to_trace` that deserializes traces from the same JSON format that its `from_trace` classmethod serializes to.

#### `list_modules() -> List[str]`

Query all traces in the trace store and return a list of module names for which traces exist in the store.

## SQLiteStore

MonkeyType bundles one sample store implementation, which `DefaultConfig` uses as the default store. It stores call traces in a SQLite database in a local file.

### SQLiteStore

#### `make_store(connection_string: str) -> SQLiteStore`

The `connection_string` argument will be passed straight through to the Python standard library `sqlite` module.

#### `add(traces: Iterable[CallTrace]) -> None`

Store one or more `CallTrace` instances in the SQLite database, encoded via `CallTraceRow`.

#### `filter(module: str, qualname_prefix: Optional[str] = None, limit: int = 2000) -> List[CallTraceRow]`

Query up to `limit` call traces from the SQLite database for a given `module` and optional `qualname_prefix`, returning each as a `CallTraceRow` instance.

## serialize_traces

### Function

Serialize an iterable of `CallTrace` to an iterable of `CallTraceRow` (via `CallTraceRow.from_trace`). If any trace fails to serialize, the exception is logged and serialization continues.

```python
serialize_traces(traces: Iterable[CallTrace]) -> Iterable[CallTraceRow]
```

## CallTraceRow

The `CallTraceRow` class implements serialization/deserialization of `CallTrace` instances to/from JSON. See the implementation of `SQLiteStore` for example usage.

It is not required for a custom store to use `CallTraceRow`; a store may choose to implement its own alternative (de)serialization.

### CallTraceRow

#### `from_trace(trace: CallTrace) -> CallTraceRow`

Serialize a `CallTraceRow` from the given `CallTrace`.

#### `to_trace() -> CallTrace`

Deserialize and return the `CallTrace` represented by this `CallTraceRow`.

#### `module: str`

The module in which the traced function is defined, e.g. `some.module`.

#### `qualname: str`

The `__qualname__` of the traced function or method, e.g. `some_func` for a top-level function or `SomeClass.some_method` for a method.

#### `arg_types: str`

A JSON-serialized representation of the concrete argument types for a single traced call. See the implementation for details of the format.

#### `return_type: Optional[str]`

A JSON-serialized representation of the actual return type of this traced call, or `None` if this call did not return (i.e. yielded instead).

#### `yield_type: Optional[str]`

A JSON-serialized representation of the actual yield type for this traced call, or `None` if this call did not yield (i.e. returned instead).

## CallTraceThunk

The minimal required interface of the objects returned from `CallTraceStore.filter`. Most stores will use `CallTraceRow` to satisfy this interface.

### CallTraceThunk

#### `to_trace() -> CallTrace`

Produce a `CallTrace` instance based on the serialized trace data stored in this thunk.

## Source

This documentation is extracted from the [Instagram/MonkeyType GitHub repository](https://github.com/Instagram/MonkeyType).
