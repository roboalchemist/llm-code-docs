# API Gaps: Reconciliation Report

**Coverage**: 147/272 symbols = 54.0%

**Missing**: 125 symbols not found in `output/api/rust.md`

## Summary by Kind

- `fn`: 74 missing
- `struct`: 36 missing
- `trait`: 11 missing
- `type`: 4 missing

## Missing Symbols

Sorted by kind (structs/enums first as most important), then name.

| Kind | Name | Module | Description |
|------|------|--------|-------------|
| `fn` | `accepts_replies` | `queryable` | ``` # #[tokio::main] # async fn main() { |
| `fn` | `aggregated_publishers` | `session` | pub fn aggregated_publishers(mut self, exprs: Vec<OwnedKeyExpr>) -> Self { |
| `fn` | `aggregated_subscribers` | `session` | pub fn aggregated_subscribers(mut self, exprs: Vec<OwnedKeyExpr>) -> Self { |
| `fn` | `append` | `bytes` | let three = ZBytes::from(vec![6, 7]);  let mut writer = ZBytes::writer(); |
| `fn` | `as_keyexpr` | `key_expr` | # Safety Key Expressions must follow some rules to be accepted by a Zenoh network. Messages addressed with invalid key e |
| `fn` | `as_shm` | `bytes` | assert_eq!(buf1.as_slice(), iter.next().unwrap()); assert_eq!(buf2.as_slice(), iter.next().unwrap()); ``` |
| `fn` | `as_shm_mut` | `bytes` | pub fn as_shm_mut(&mut self) -> Option<&mut zshm> { |
| `fn` | `attachment_mut` | `queryable` | let queryable = session .declare_queryable("key/expression") .callback(move \|mut query\| { |
| `fn` | `auth_identifier` | `info` | Returns whether the link is streamed. Gets the network interfaces associated with the link. Gets the authentication iden |
| `fn` | `autocanonize` | `key_expr` | Canonizes the passed value before returning it as a `KeyExpr`.  Will return Err if the passed value isn't a valid key ex |
| `fn` | `borrowed` | `selector` | Build a new selector holding references to keyexpr and parameters Useful for printing pairs of keyexpr and parameters in |
| `fn` | `borrowing_clone` | `key_expr` | Constructs a new [`KeyExpr`] aliasing `self`.  Note that [`KeyExpr`] (as well as [`OwnedKeyExpr`]) use reference counter |
| `fn` | `capacity` | `fifo` | Returns true if the channel is full. Note: Zero-capacity channels are always full. Returns the number of messages in the |
| `fn` | `drain` | `fifo` | all senders have been dropped or the channel is empty. Take all msgs currently sitting in the channel and produce an ite |
| `fn` | `dst` | `info` | Gets the ZenohId of the transport this link belongs to. Gets the source locator (local endpoint). Gets the destination l |
| `fn` | `dummy` | `key_expr` | Constructs a key expression object to be used as a dummy value for empty objects. This method is not supposed to be call |
| `fn` | `empty` | `info` | Constructs an uninitialized empty Transport. |
| `fn` | `finish` | `bytes` | let zbytes = writer.finish();  assert_eq!(zbytes.to_bytes(), vec![0u8, 1, 2, 3, 4, 5, 6, 7]); |
| `fn` | `from_env` | `config` | Default environment variable containing the file path used in [`Config::from_env`]. Load configuration from the file pat |
| `fn` | `from_json5` | `config` | Load configuration from the file at `path`. Load configuration from the JSON5 string `input`. |
| `fn` | `from_reader` | `bytes` |  See [`ZBytesWriter`] on how to chain the deserialization of different types from a single [`ZBytes`]. Build a [`ZBytes` |
| `fn` | `get_json` | `config` | Returns a JSON string containing the configuration at `key`. |
| `fn` | `get_shm_provider` | `session` | let shm_provider = session.get_shm_provider(); assert!(shm_provider.into_option().is_none()); std::thread::sleep(std::ti |
| `fn` | `group` | `info` | Gets the source locator (local endpoint). Gets the destination locator (remote endpoint). Gets the optional group locato |
| `fn` | `in_background` | `close` |  # Arguments  |
| `fn` | `init` | `session` | Initialize a Session with an existing Runtime. This operation is used by the plugins to share the same Runtime as the ro |
| `fn` | `insert_json5` | `config` | Inserts configuration value `value` at `key`. |
| `fn` | `interfaces` | `info` | Gets the maximum transmission unit in bytes (MTU) of the link. Returns whether the link is streamed. Gets the network in |
| `fn` | `into_owned` | `key_expr` | Messages addressed with invalid key expressions will be dropped. Returns the borrowed version of `self` Ensures `self` o |
| `fn` | `into_recv_async` | `fifo` | Convert this receiver into a future that asynchronously receives a single message from the channel, returning an error i |
| `fn` | `into_stream` | `fifo` | from the channel. The receiver will continue to be usable after the stream has been dropped. Convert this receiver into  |
| `fn` | `is_cancelled` | `cancellation` | In case of failure, some operations might not be cancelled. Once cancelled, all newly added get queries will cancel auto |
| `fn` | `is_closed` | `session` | Check if the session has been closed.  # Examples |
| `fn` | `is_disconnected` | `fifo` | Take all msgs currently sitting in the channel and produce an iterator over them. Unlike `try_iter`, the iterator will n |
| `fn` | `is_dummy` | `key_expr` | Checks if the key expression is the dummy one. This method is not supposed to be called in user code, but may be used in |
| `fn` | `is_empty` | `bytes` | let mut buf = [0; 14]; reader.read_exact(&mut buf).unwrap(); assert_eq!(&buf, b"some raw bytes"); |
| `fn` | `is_full` | `fifo` | Returns true if the channel is empty. Note: Zero-capacity channels are always empty. Returns true if the channel is full |
| `fn` | `is_multicast` | `info` | Returns whether this transport supports QoS. Returns whether this transport supports shared memory. Returns whether this |
| `fn` | `is_qos` | `info` | Gets the ZenohId of the remote zenoh node. Gets the type of the remote zenoh node (Router, Peer, or Client). Returns whe |
| `fn` | `is_shm` | `info` | Gets the type of the remote zenoh node (Router, Peer, or Client). Returns whether this transport supports QoS. Returns w |
| `fn` | `is_streamed` | `info` | Gets the optional group locator (destination if link is for multicast). Gets the maximum transmission unit in bytes (MTU |
| `fn` | `iter` | `fifo` | Create a blocking iterator over the values received on the channel that finishes iteration when all senders have been dr |
| `fn` | `len` | `bytes` | Create an empty ZBytes. Returns whether the [`ZBytes`] is empty or not. Returns the total number of bytes in the [`ZByte |
| `fn` | `link_mut` | `info` | Returns the kind of event (Put for added, Delete for removed) Returns a reference to the link Returns a mutable referenc |
| `fn` | `locators` | `info` |  # Examples ``` |
| `fn` | `locked` | `callback` | A function that can transform an [`FnMut`]`(T)` into an [`Fn`]`(T)` with the help of a [`Mutex`](std::sync::Mutex). |
| `fn` | `mtu` | `info` | Gets the destination locator (remote endpoint). Gets the optional group locator (destination if link is for multicast).  |
| `fn` | `owned` | `selector` | Get the [`Parameters`] of this selector. Deconstruct the selector into ([`KeyExpr`], [`Parameters`]) Builds a new select |
| `fn` | `payload_mut` | `query` | Gets the payload of this ReplyError. Gets the mutable payload of this ReplyError. Gets the encoding of this ReplyError. |
| `fn` | `priorities` | `info` | Gets the optional priority range (min, max) associated with the link. The numeric priority values corresponds [`Priority |
| `fn` | `reader` | `bytes` | Get a [`ZBytesReader`] implementing the [`std::io::Read`] trait.  See [`ZBytesWriter`] on how to chain the deserializati |
| `fn` | `receiver_count` | `fifo` | If the channel is bounded, returns its capacity. Get the number of senders that currently exist. Get the number of recei |
| `fn` | `recv_deadline` | `fifo` | error if all senders have been dropped. Wait for an incoming value from the channel associated with this receiver, retur |
| `fn` | `recv_timeout` | `fifo` | Wait for an incoming value from the channel associated with this receiver, returning an error if all senders have been d |
| `fn` | `remaining` | `bytes` | assert_eq!(&buf, b"some raw bytes"); reader.seek(SeekFrom::Start(5)).unwrap(); let mut buf2 = [0; 4]; |
| `fn` | `reply_sample` | `queryable` | let session = zenoh::open(zenoh::Config::default()).await.unwrap(); let queryable = session .declare_queryable("key/expr |
| `fn` | `result_mut` | `query` | Gets a borrowed result of this `Reply`. Use [`Reply::into_result`] to take ownership of the result. Gets a mutable borro |
| `fn` | `same_channel` | `fifo` | Get the number of senders that currently exist. Get the number of receivers that currently exist, including this one. Re |
| `fn` | `schema` | `encoding` | pub fn schema(&self) -> Option<&ZSlice> { |
| `fn` | `sender_count` | `fifo` | Returns the number of messages in the channel. If the channel is bounded, returns its capacity. Get the number of sender |
| `fn` | `slices` | `bytes` |  let mut writer = ZBytes::writer(); writer.append(ZBytes::from(buf1.clone())); |
| `fn` | `source_id` | `sample` | Build a new [`SourceInfo`]. The [`EntityGlobalId`] of the zenoh entity that published the [`Sample`] in question. The se |
| `fn` | `source_sn` | `sample` | The [`EntityGlobalId`] of the zenoh entity that published the [`Sample`] in question. The sequence number of the [`Sampl |
| `fn` | `split` | `selector` | Get the [`KeyExpr`] of this selector. Get the [`Parameters`] of this selector. Deconstruct the selector into ([`KeyExpr` |
| `fn` | `src` | `info` | Gets the ZenohId of the transport this link belongs to. Gets the source locator (local endpoint). Gets the destination l |
| `fn` | `stop` | `scouting` | Stop scouting.  # Examples |
| `fn` | `stream` | `fifo` | Create an asynchronous stream that uses this receiver to asynchronously receive messages from the channel. The receiver  |
| `fn` | `to_bytes` | `bytes` | Access raw bytes contained in the [`ZBytes`].  In the case `ZBytes` contains non-contiguous regions of memory, an alloca |
| `fn` | `transport_mut` | `info` | Returns the kind of event (Put for opened, Delete for closed) Returns a reference to the transport Returns a mutable ref |
| `fn` | `try_iter` | `fifo` | Create a blocking iterator over the values received on the channel that finishes iteration when all senders have been dr |
| `fn` | `try_to_string` | `bytes` |  In the case `ZBytes` contains non-contiguous regions of memory, an allocation and a copy will be done; that's why the m |
| `fn` | `whatami` | `info` | Gets the ZenohId of the remote zenoh node. Gets the type of the remote zenoh node (Router, Peer, or Client). Returns whe |
| `fn` | `with_schema` | `encoding` | The default [`Encoding`] is [`ZENOH_BYTES`](Encoding::ZENOH_BYTES). Set a schema for this encoding. Zenoh does not defin |
| `fn` | `writer` | `bytes` | Get a [`ZBytesWriter`] implementing [`std::io::Write`] trait.  See [`ZBytesWriter`] on how to chain the serialization of |
| `struct` | `BackgroundCloseBuilder` | `close` | A builder for close operations running in the background |
| `struct` | `Callback` | `callback` | Callback type used by zenoh entities.  This type stores the callback function passed to zenoh entities. |
| `struct` | `CallbackDrop` | `callback` | - `drop`: a callback invoked when this handler is dropped.  It is guaranteed that: |
| `struct` | `CancelResult` | `cancellation` | pub struct CancelResult(CancellationToken); |
| `struct` | `Drain` | `fifo` | A non-blocking iterator over the msgs received from a channel. A fixed-size iterator over the msgs drained from a channe |
| `struct` | `FifoChannel` | `fifo` |  Note that pushing on a [`FifoChannel`] that is full will block until a slot is available. E.g., a slow subscriber could |
| `struct` | `FifoChannelHandler` | `fifo` | Initialize the [`FifoChannel`] with the capacity size. [`FifoChannel`] handler. This is the receiver side of the channel |
| `struct` | `InitBuilder` | `session` | A builder returned by [`init`] and used to initialize a Session with an existing Runtime. |
| `struct` | `IntoIter` | `fifo` | An owned iterator over the msgs received from a channel. |
| `struct` | `KeyExprUndeclaration` | `key_expr` |  # Examples ``` |
| `struct` | `LinkEventsListenerUndeclaration` | `info_links` | A [`Resolvable`] returned by [`LinkEventsListener::undeclare`] |
| `struct` | `LookupGuard` | `config` | pub struct LookupGuard<'a, T> { |
| `struct` | `MatchingListenerUndeclaration` | `matching` | A [`Resolvable`] returned by [`MatchingListener::undeclare`] |
| `struct` | `NolocalJoinHandle` | `close` | pub struct NolocalJoinHandle<TOutput: Send + 'static> { |
| `struct` | `Notifier` | `config` | The wrapper for a [`Config`] that allows to subscribe to changes. This type is returned by [`Session::config`](crate::Se |
| `struct` | `PublicationBuilderDelete` | `publisher` | The type-modifier for a [`PublicationBuilder`] for a `Delete` operation.  Makes the publication builder make a sample of |
| `struct` | `PublicationBuilderPut` | `publisher` | The type-modifier for a [`PublicationBuilder`] for a `Put` operation.  Makes the publication builder make a sample of a  |
| `struct` | `QuerierUndeclaration` | `querier` |  # Examples ``` |
| `struct` | `RecvFut` | `fifo` | A future which allows asynchronously receiving a message.  Can be created via [`FifoChannelHandler::recv_async`] or [`Fi |
| `struct` | `RecvStream` | `fifo` | Convert this receiver into a stream that allows asynchronously receiving messages from the channel. A stream which allow |
| `struct` | `ReplySample` | `queryable` | pub struct ReplySample<'a> { |
| `struct` | `Response` | `plugins` | A Response for the administration space. |
| `struct` | `RingChannel` | `ring` | A synchronous ring channel with a limited size that allows users to keep the last N data items.  [`RingChannel`] impleme |
| `struct` | `RingChannelHandler` | `ring` | Initialize the RingBuffer with the given capacity. Receive from the ring channel.  |
| `struct` | `SampleBuilder` | `sample` | Attach user-provided data in key-value format Set the [`Encoding`] The type modifier for a [`SampleBuilder`] to create a |
| `struct` | `SampleBuilderAny` | `sample` | The type modifier for a [`SampleBuilder`] for the building stage when the sample [`kind`](crate::sample::Sample::kind) i |
| `struct` | `SampleBuilderDelete` | `sample` | Set the [`Encoding`] The type modifier for a [`SampleBuilder`] to create a [`Put`](crate::sample::SampleKind::Put) sampl |
| `struct` | `SampleBuilderPut` | `sample` | Attach user-provided data in key-value format Set the [`Encoding`] The type modifier for a [`SampleBuilder`] to create a |
| `struct` | `SampleFields` | `sample` | .into(); let fields: SampleFields = sample.into(); let SampleFields { |
| `struct` | `ScoutBuilder` | `scouting` | use zenoh::config::WhatAmI;  let receiver = zenoh::scout(WhatAmI::Peer \| WhatAmI::Router, zenoh::Config::default()) |
| `struct` | `SessionClosedError` | `session` | Error indicating the operation cannot proceed because the session is closed.  It may be returned by operations like [`Se |
| `struct` | `TransportEventsListenerUndeclaration` | `info_transport` | A [`Resolvable`] returned by [`TransportEventsListener::undeclare`] |
| `struct` | `TryIter` | `fifo` | An iterator over the msgs received from a channel. A non-blocking iterator over the msgs received from a channel. A fixe |
| `struct` | `ZBytesReader` | `bytes` | let payload = writer.finish(); let mut reader = payload.reader(); let mut buf = [0; 14]; |
| `struct` | `ZBytesSliceIterator` | `bytes` | let buf: Vec<u8> = buf1.into_iter().chain(buf2.into_iter()).collect(); // Concatenate raw bytes in a single vector let o |
| `struct` | `ZBytesWriter` | `bytes` | ``` It is also possible to append existing [`ZBytes`] instances by taking ownership of them using the [`append`](Self::a |
| `trait` | `CallbackParameter` | `callback` | A function that can transform an [`FnMut`]`(T)` into an [`Fn`]`(T)` with the help of a [`Mutex`](std::sync::Mutex). |
| `trait` | `CancellationTokenBuilderTrait` | `cancellation` | pub trait CancellationTokenBuilderTrait { |
| `trait` | `EncodingBuilderTrait` | `sample` | Attach source information Attach user-provided data in key-value format Set the [`Encoding`] |
| `trait` | `QoSBuilderTrait` | `sample` | Change the `congestion_control` to apply when routing the data. Change the p |
| `trait` | `RunningPluginTrait` | `plugins` | A Response for the administration space. Function that will be called when the configuration relevant to the plugin is a |
| `trait` | `SampleBuilderTrait` | `sample` | When express is set to `true`, then the message will not be batched. This usually has a positive impact on latency but n |
| `trait` | `TimestampBuilderTrait` | `sample` | Change the priority of the written data. Change the `express` policy to apply when routing the data. When express is set |
| `trait` | `Undeclarable` | `session` | A trait implemented by types that can be undeclared. |
| `trait` | `UndeclarableSealed` | `session` | A trait implemented by types that can be undeclared. |
| `trait` | `ZenohParameters` | `selector` | The trait allows setting/reading parameters processed by the Zenoh library itself. These parameter names are not part of |
| `trait` | `ZenohPlugin` | `plugins` | A zenoh plugin, when started, must return this type. Zenoh plugins should implement this trait to ensure type-safety, ev |
| `type` | `Notification` | `config` | The wrapper for a [`Config`] that allows to subscribe to chang |
| `type` | `PluginsManager` | `plugins` |  The zenoh plugins manager. It handles the full lifetime of plugins, from loading to destruction. |
| `type` | `RunningPlugin` | `plugins` | A Response for the administration space. Function that will be called when the configuration relevant to the plugin is a |
| `type` | `SourceSn` | `sample` | The sequence number of the [`Sample`] from the source. The locality of samples/queries to be received by subscribers/que |

## Found Symbols (sample)

First 20 of 147 symbols confirmed present in api/rust.md:

- `timeout`
- `wait_callbacks`
- `CloseBuilder`
- `ZenohIdBuilder`
- `RoutersZenohIdBuilder`
- `PeersZenohIdBuilder`
- `transport`
- `undeclare`
- `handler`
- `handler_mut`
- `set_background`
- `history`
- `with`
- `callback`
- `callback_mut`
- `background`
- `LinksBuilder`
- `LinkEventsListener`
- `LinkEventsListenerBuilder`
- `TransportsBuilder`


## Generated Gap-Fill Documentation

### `BackgroundCloseBuilder`
The `BackgroundCloseBuilder` is a builder for executing close operations asynchronously in the background. It's hidden under certain feature flags and primarily designed for internal zenoh use, allowing a future operation for background processing to be set up without blocking current execution.

### `Callback`
`Callback` is a type that encapsulates callback functions used by zenoh entities. It stores the functions to be called back on specific events or conditions, and it may have additional features under certain configurations.

### `CallbackDrop`
`CallbackDrop` is a struct that pairs a callback with a drop function, which ensures that the callback and drop function do not execute concurrently. It guarantees that resources are cleaned up correctly when the callback is no longer in use.

### `CallbackParameter`
`CallbackParameter` is a trait representing a parameter type for callback functions. It defines how messages are converted to this parameter type, enabling flexible and type-safe callback handling within zenoh.

### `CancelResult`
`CancelResult` is a struct representing the result of a cancellation operation, integrating with asynchronous futures. It encapsulates a `CancellationToken`, allowing the calling code to convert it into a future for waiting until the cancellation completes.

### `CancellationTokenBuilderTrait`
The `CancellationTokenBuilderTrait` is a trait for building components that involve a cancellation token. It provides a method to set the token, ensuring that components can handle cancellation events and manage their lifecycles appropriately.

### `Drain`
`Drain` is a struct representing a fixed-size iterator over messages drained from a channel. It's used when you need to process all available messages in a channel without blocking, providing efficient batch handling capabilities.

### `EncodingBuilderTrait`
`EncodingBuilderTrait` is used to set the encoding for a sample being built, allowing users to specify the desired encoding format for data transmission. It ensures that samples are encoded consistently and according to requirements during creation.

### `FifoChannel`
`FifoChannel` is a struct that represents a first-in, first-out channel with a fixed capacity. It's used for queuing data with predictable ordering, dropping the oldest data when the capacity is exceeded by newly arriving data.

### `FifoChannelHandler`
The `FifoChannelHandler` manages the receiver side of a FIFO channel, implementing data-receiving methods. It provides an interface for clients to interact with the FIFO queue to retrieve messages as they become available.

### `InitBuilder`
`InitBuilder` is a struct used internally in zenoh for setting up session initialization parameters. It aggregates configurations for subscribers and publishers, ensuring that the session is established with the correct settings.

### `IntoIter`
`IntoIter` is a struct representing an owned iterator over messages received from a channel, providing a means to consume all queued messages in ownership and transfer them out of the communication channel.

### `KeyExprUndeclaration`
`KeyExprUndeclaration` is a struct representing the undeclaration of a key expression in a session, allowing asynchronous resolution. It's used to retract previously declared key expressions, supporting dynamic configuration changes.

### `LinkEventsListenerUndeclaration`
`LinkEventsListenerUndeclaration` is a `Resolvable` struct returned when undeclaring a `LinkEventsListener`. It supports waiting for the undeclaration to complete, ensuring that all link event callbacks are properly disposed of.

### `LookupGuard`
`LookupGuard` is a struct that binds to a configuration lock, preventing modifications while a section of configuration is being accessed. It's used to access configuration data safely and consistently in a concurrent environment.

### `MatchingListenerUndeclaration`
`MatchingListenerUndeclaration` is a struct representing the process of removing a matching listener from the system. It ensures any ongoing matching listener operations are finalized and removed properly without race conditions.

### `NolocalJoinHandle`
`NolocalJoinHandle` handles asynchronous tasks that are executed in the background without blocking the main task. It's used when you need to run non-local operations and track their results without affecting the control flow.

### `Notifier`
`Notifier` facilitates real-time updates in zenoh configuration, allowing the `Session` to react immediately to configuration changes. It serves as a bridge between configuration changes and session updates, enhancing dynamic configurability.

### `PublicationBuilderDelete`
`PublicationBuilderDelete` is a struct for creating publications that delete samples from the system. It's an intermediary in the publication flow, enabling users to prepare and execute delete operations in a structured manner.

### `PublicationBuilderPut`
`PublicationBuilderPut` facilitates the creation and modification of publications to add or update samples. It stores the payload and encoding, allowing users to construct publications incrementally before sending.

### `QoSBuilderTrait`
The `QoSBuilderTrait` provides methods to modify quality of service parameters such as congestion control, priority, etc. It's essential for customizing the data delivery guarantees to meet application-specific needs.

### `QuerierUndeclaration`
`QuerierUndeclaration` represents an undeclaration operation for queriers, ensuring all related query operations are resolved or canceled appropriately. It provides a way to manage resources and terminate queries gracefully.

### `RecvFut`
`RecvFut` is a future representing the asynchronous reception of messages from a channel. It is primarily used for waiting on messages to arrive, integrating with Rust's async framework to support non-blocking data flow handling.

### `RecvStream`
`RecvStream` is a struct for streaming messages asynchronously from a FIFO channel. It's used when you want to consume messages lazily as they arrive, supporting backpressure and non-blocking streaming operations.

### `ReplySample`
`ReplySample` is part of the queryable module handling query responses with encapsulated sample and query references. It facilitates managing responses and ensures they comply with zenoh's asynchronous resolution model.

### `Response`
The `Response` struct encapsulates a response in the administration space, carrying key-value pairs encoded in JSON. It's designed to standardize responses and is typically used in plugin communications or system status reports.

### `RingChannel`
A `RingChannel` is a channel type utilizing a ring buffer with a drop strategy for overflowing elements. This makes it suitable for scenarios where retaining only the most recent dataset is crucial, and older data can be discarded.

### `RingChannelHandler`
`RingChannelHandler` receives data from a `RingChannel`, blocking when empty. It's used when a blocking, loss-tolerant channel is appropriate, where newer data may overwrite the oldest to preserve a set capacity.

### `RunningPluginTrait`
`RunningPluginTrait` provides control and configuration change interfaces for running plugins. It's crucial for plugin lifecycle management, allowing plugins to be responsive to configuration updates and control operations.

### `SampleBuilder`
`SampleBuilder` constructs `Sample` instances, facilitating the assembly and modification of sample data before transmission. It provides an API for step-by-step sample construction, aiding in dynamic data configuration.

### `SampleBuilderAny`
`SampleBuilderAny` is used as an initial state in the sample creation process, allowing flexibility in specifying sample kinds later. It simplifies transitioning between sample types until a final structure is committed.

### `SampleBuilderDelete`
`SampleBuilderDelete` provides a builder for samples of kind `Delete`, focusing on sample removal instructions to ensure a consistent and flexible sample creation process for deletion operations within zenoh.

### `SampleBuilderPut`
`SampleBuilderPut` is used for building samples destined for addition or update operations in zenoh. It structures the sample data with kind `Put`, incorporating payload and encoding configuration in a systematic manner.

### `SampleBuilderTrait`
The `SampleBuilderTrait` enables additional sample configuration options such as attaching source information and user-defined data. It expands the `SampleBuilder` functionality, promoting customizable sample creation.

### `SampleFields`
`SampleFields` is a struct that holds detailed information about a sample, such as the key expression, payload, and metadata like encoding and priority. It is crucial for maintaining complete sample specifications in operations.

### `ScoutBuilder`
`ScoutBuilder` configures and initializes scout operations, including the allocation of handlers and configurations necessary for discovery tasks. It underpins zenoh's discovery capabilities by setting up matching criteria.

### `SessionClosedError`
`SessionClosedError` is an error type thrown when operations are attempted on a closed session. It signals the need for user intervention to re-establish or handle terminated session contexts in application logic.

### `TimestampBuilderTrait`
`TimestampBuilderTrait` is used to attach or clear timestamps on samples, affecting timing precision and data recording intervals. It's crucial for use cases where precise timing information impacts data processing or storage.

### `TransportEventsListenerUndeclaration`
`TransportEventsListenerUndeclaration` provides functionality to undeclare transport event listeners, halting their operations and ensuring no pending callbacks execute. It's used to manage listener lifecycles effectively.

### `TryIter`
`TryIter` is a non-blocking iterator for consuming messages in a channel, useful when asynchronous processing needs to check for available messages without waiting. It supports efficient handling of incoming data with minimal latency.
