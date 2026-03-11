# Zenoh Rust API

# https://docs.rs/zenoh-buffers/latest/zenoh_buffers/

Source: https://docs.rs/zenoh-buffers/latest/zenoh_buffers/

## [Crate zenoh\_buffers](#)



# Crate zenoh\_buffers

[Source](../src/zenoh_buffers/lib.rs.html#15-319)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

Provide different buffer implementations used for serialization and deserialization.

## Modules[§](#modules)

[buffer](buffer/index.html "mod zenoh_buffers::buffer")

[reader](reader/index.html "mod zenoh_buffers::reader")

[vec](vec/index.html "mod zenoh_buffers::vec")

[writer](writer/index.html "mod zenoh_buffers::writer")

## Macros[§](#macros)

[unsafe\_slice](macro.unsafe_slice.html "macro zenoh_buffers::unsafe_slice")

[unsafe\_slice\_mut](macro.unsafe_slice_mut.html "macro zenoh_buffers::unsafe_slice_mut")

## Structs[§](#structs)

[BBuf](struct.BBuf.html "struct zenoh_buffers::BBuf")

[ZBuf](struct.ZBuf.html "struct zenoh_buffers::ZBuf")

[ZBufPos](struct.ZBufPos.html "struct zenoh_buffers::ZBufPos")

[ZBufReader](struct.ZBufReader.html "struct zenoh_buffers::ZBufReader")

[ZBufSliceIterator](struct.ZBufSliceIterator.html "struct zenoh_buffers::ZBufSliceIterator")

[ZBufWriter](struct.ZBufWriter.html "struct zenoh_buffers::ZBufWriter")

[ZSlice](struct.ZSlice.html "struct zenoh_buffers::ZSlice")
:   A cloneable wrapper to a contiguous slice of bytes.

## Traits[§](#traits)

[ZSliceBuffer](trait.ZSliceBuffer.html "trait zenoh_buffers::ZSliceBuffer")

---

# https://docs.rs/zenoh-codec/latest/zenoh_codec/

Source: https://docs.rs/zenoh-codec/latest/zenoh_codec/

## [Crate zenoh\_codec](#)



# Crate zenoh\_codec

[Source](../src/zenoh_codec/lib.rs.html#15-155)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Modules[§](#modules)

[common](common/index.html "mod zenoh_codec::common")

[core](core/index.html "mod zenoh_codec::core")

[network](network/index.html "mod zenoh_codec::network")

[scouting](scouting/index.html "mod zenoh_codec::scouting")

[transport](transport/index.html "mod zenoh_codec::transport")

[zenoh](zenoh/index.html "mod zenoh_codec::zenoh")

## Macros[§](#macros)

[impl\_zextz64](macro.impl_zextz64.html "macro zenoh_codec::impl_zextz64")

## Structs[§](#structs)

[Zenoh080](struct.Zenoh080.html "struct zenoh_codec::Zenoh080")

[Zenoh080Bounded](struct.Zenoh080Bounded.html "struct zenoh_codec::Zenoh080Bounded")

[Zenoh080Condition](struct.Zenoh080Condition.html "struct zenoh_codec::Zenoh080Condition")

[Zenoh080Header](struct.Zenoh080Header.html "struct zenoh_codec::Zenoh080Header")

[Zenoh080Length](struct.Zenoh080Length.html "struct zenoh_codec::Zenoh080Length")

[Zenoh080Reliability](struct.Zenoh080Reliability.html "struct zenoh_codec::Zenoh080Reliability")

## Traits[§](#traits)

[LCodec](trait.LCodec.html "trait zenoh_codec::LCodec")

[RCodec](trait.RCodec.html "trait zenoh_codec::RCodec")

[WCodec](trait.WCodec.html "trait zenoh_codec::WCodec")

---

# https://docs.rs/zenoh-collections/latest/zenoh_collections/

Source: https://docs.rs/zenoh-collections/latest/zenoh_collections/

## [Crate zenoh\_collections](#)



# Crate zenoh\_collections

[Source](../src/zenoh_collections/lib.rs.html#15-44)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Re-exports[§](#reexports)

`pub use single_or_vec::SingleOrVec;`

`pub use single_or_box_hashset::SingleOrBoxHashSet;`

`pub use ring_buffer::*;`

`pub use stack_buffer::*;`

`pub use int_hash_map::*;`

## Modules[§](#modules)

[int\_hash\_map](int_hash_map/index.html "mod zenoh_collections::int_hash_map")

[ring\_buffer](ring_buffer/index.html "mod zenoh_collections::ring_buffer")

[single\_or\_box\_hashset](single_or_box_hashset/index.html "mod zenoh_collections::single_or_box_hashset")

[single\_or\_vec](single_or_vec/index.html "mod zenoh_collections::single_or_vec")

[stack\_buffer](stack_buffer/index.html "mod zenoh_collections::stack_buffer")

---

# https://docs.rs/zenoh-config/latest/zenoh_config/

Source: https://docs.rs/zenoh-config/latest/zenoh_config/

## [Crate zenoh\_config](#)

## [zenoh\_config](../zenoh_config/index.html)1.7.2

### [Crate Items](#reexports)

# Crate zenoh\_config Copy item path

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

Configuration to pass to `zenoh::open()` and `zenoh::scout()` functions and associated constants.

`zenoh::open()`
`zenoh::scout()`

## Re-exports[§](#reexports)

`pub use wrappers::ZenohId;`
`pub use mode_dependent::*;`
`pub use connection_retry::*;`

## Modules[§](#modules)

`whatami`
`zenoh`

## Macros[§](#macros)

## Structs[§](#structs)

`EndPoint`
`<locator>[#<config>]`
`Locator`
`<proto>/<address>[?<metadata>]`
`serde_json::Value`
`WhatAmI`

## Enums[§](#enums)

## Traits[§](#traits)

## Functions[§](#functions)

`'client'`
`peer`
`'peer'`

## Type Aliases[§](#types)

---

# https://docs.rs/zenoh-core/latest/zenoh_core/

Source: https://docs.rs/zenoh-core/latest/zenoh_core/

## [Crate zenoh\_core](#)



# Crate zenoh\_core

[Source](../src/zenoh_core/lib.rs.html#15-177)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Modules[§](#modules)

[macros](macros/index.html "mod zenoh_core::macros")

[zresult](zresult/index.html "mod zenoh_core::zresult")

## Macros[§](#macros)

[bail](macro.bail.html "macro zenoh_core::bail")

[lazy\_static](macro.lazy_static.html "macro zenoh_core::lazy_static")

[to\_u64](macro.to_u64.html "macro zenoh_core::to_u64")

[to\_zerror](macro.to_zerror.html "macro zenoh_core::to_zerror")

[zasync\_executor\_init](macro.zasync_executor_init.html "macro zenoh_core::zasync_executor_init")

[zasynclock](macro.zasynclock.html "macro zenoh_core::zasynclock")

[zasyncopt](macro.zasyncopt.html "macro zenoh_core::zasyncopt")

[zasyncread](macro.zasyncread.html "macro zenoh_core::zasyncread")

[zasyncrecv](macro.zasyncrecv.html "macro zenoh_core::zasyncrecv")

[zasyncsend](macro.zasyncsend.html "macro zenoh_core::zasyncsend")

[zasyncwrite](macro.zasyncwrite.html "macro zenoh_core::zasyncwrite")

[zcondfeat](macro.zcondfeat.html "macro zenoh_core::zcondfeat")

[zconfigurable](macro.zconfigurable.html "macro zenoh_core::zconfigurable")

[zerror](macro.zerror.html "macro zenoh_core::zerror")

[zlock](macro.zlock.html "macro zenoh_core::zlock")

[zparse](macro.zparse.html "macro zenoh_core::zparse")

[zparse\_default](macro.zparse_default.html "macro zenoh_core::zparse_default")

[zread](macro.zread.html "macro zenoh_core::zread")

[ztimeout](macro.ztimeout.html "macro zenoh_core::ztimeout")

[zwrite](macro.zwrite.html "macro zenoh_core::zwrite")

## Structs[§](#structs)

[ResolveClosure](struct.ResolveClosure.html "struct zenoh_core::ResolveClosure")

[ResolveFuture](struct.ResolveFuture.html "struct zenoh_core::ResolveFuture")

## Traits[§](#traits)

[Resolvable](trait.Resolvable.html "trait zenoh_core::Resolvable")
:   A resolvable execution, either sync or async

[Resolve](trait.Resolve.html "trait zenoh_core::Resolve")
:   Zenoh’s trait for resolving builder patterns.

[Wait](trait.Wait.html "trait zenoh_core::Wait")
:   Synchronous execution of a resolvable

## Functions[§](#functions)

[likely](fn.likely.html "fn zenoh_core::likely")

[unlikely](fn.unlikely.html "fn zenoh_core::unlikely")

## Type Aliases[§](#types)

[Error](type.Error.html "type zenoh_core::Error")

[Result](type.Result.html "type zenoh_core::Result")

---

# https://docs.rs/zenoh-ext/latest/zenoh_ext/

Source: https://docs.rs/zenoh-ext/latest/zenoh_ext/

## [Crate zenoh\_ext](#)

## [zenoh\_ext](../zenoh_ext/index.html)1.7.2

### [Sections](#)

### [Crate Items](#modules)

# Crate zenoh\_ext Copy item path

[Zenoh](https://zenoh.io) /zeno/ is a stack that unifies data in motion, data at
rest, and computations. It elegantly blends traditional pub/sub with geo-distributed
storage, queries, and computations, while retaining a level of time and space efficiency
that is well beyond any of the mainstream stacks.

This crate provides components extending the core Zenoh functionalities.

These components include

## [§](#serialization)Serialization

The base zenoh library allows to send/receive data as raw bytes payload. But in order to
simplify the library’s usability and, more importantly, to ensure interoperability
between zenoh-based applications, this crate provides serialization/deserialization
functionalities.

The key functions are [`z_serialize`](fn.z_serialize.html "fn zenoh_ext::z_serialize") and [`z_deserialize`](fn.z_deserialize.html "fn zenoh_ext::z_deserialize") that allows to
serialize/deserialize any data structure implementing the [`Serialize`](trait.Serialize.html "trait zenoh_ext::Serialize") and
[`Deserialize`](trait.Deserialize.html "trait zenoh_ext::Deserialize") traits respectively.

`z_serialize`
`z_deserialize`
`Serialize`
`Deserialize`

## [§](#advanced-pubsub)Advanced Pub/Sub

The [`AdvancedPublisher`](struct.AdvancedPublisher.html "struct zenoh_ext::AdvancedPublisher") and [`AdvancedSubscriber`](struct.AdvancedSubscriber.html "struct zenoh_ext::AdvancedSubscriber") provide advanced pub/sub
functionalities, including support for message history, recovery, and more.

`AdvancedPublisher`
`AdvancedSubscriber`

## Modules[§](#modules)

## Structs[§](#structs)

`Publisher`
`Subscriber`
`AdvancedSubscriber`
`AdvancedPublisher`
`fetch`
`FetchingSubscriber`
`history`
`PublicationCache`
`FetchingSubscriber`
`Resolvable`
`SampleMissListener::undeclare`
`SampleMissListener`
`ZDeserializer::deserialize_iter`

## Enums[§](#enums)

`FetchingSubscriber`

## Traits[§](#traits)

`zenoh::publication::PublisherBuilder`
`zenoh::subscriber::SubscriberBuilder`
`ExtractSample`
`zenoh::Session`
`zenoh::subscriber::SubscriberBuilder`
`subscriber.forward(receiver)`
`subscriber.stream().map(Ok).forward(publisher)`

## Functions[§](#functions)

## Type Aliases[§](#types)

---

# https://docs.rs/zenoh-keyexpr/latest/zenoh_keyexpr/

Source: https://docs.rs/zenoh-keyexpr/latest/zenoh_keyexpr/

## [Crate zenoh\_keyexpr](#)

## [zenoh\_keyexpr](../zenoh_keyexpr/index.html)1.7.2

### [Sections](#)

### [Crate Items](#modules)

# Crate zenoh\_keyexpr Copy item path

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

[Key expression](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md) are Zenoh’s address space.

In Zenoh, operations are performed on keys. To allow addressing multiple keys with a single operation, we use Key Expressions (KE).
KEs are a small language that express sets of keys through a glob-like language.

These semantics can be a bit difficult to implement, so this module provides the following facilities:

## [§](#storing-key-expressions)Storing Key Expressions

This module provides 2 flavours to store strings that have been validated to respect the KE syntax, and a third is provided by [`zenoh`](https://docs.rs/zenoh):

`zenoh`
`keyexpr`
`str`
`OwnedKeyExpr`
`Arc<str>`
`KeyExpr`
`Cow<str>`

All of these types [`Deref`](https://doc.rust-lang.org/nightly/core/ops/deref/trait.Deref.html "trait core::ops::deref::Deref") to [`keyexpr`](key_expr/struct.keyexpr.html "struct zenoh_keyexpr::key_expr::keyexpr"), which notably has methods to check whether a given [`keyexpr::intersects`](key_expr/struct.keyexpr.html#method.intersects "method zenoh_keyexpr::key_expr::keyexpr::intersects") with another,
or even if a [`keyexpr::includes`](key_expr/struct.keyexpr.html#method.includes "method zenoh_keyexpr::key_expr::keyexpr::includes") another.

`Deref`
`keyexpr`
`keyexpr::intersects`
`keyexpr::includes`

## [§](#tying-values-to-key-expressions)Tying values to Key Expressions

When storing values tied to Key Expressions, you might want something more specialized than a [`HashMap`](https://doc.rust-lang.org/nightly/std/collections/hash/map/struct.HashMap.html "struct std::collections::hash::map::HashMap") if you want to respect
the Key Expression semantics with high performance.

`HashMap`

Enter [KeTrees](keyexpr_tree/index.html "mod zenoh_keyexpr::keyexpr_tree"). These are data-structures specially built to store KE-value pairs in a manner that supports the set-semantics of KEs.

## [§](#building-and-parsing-key-expressions)Building and parsing Key Expressions

A common issue in REST API is the association of meaning to sections of the URL, and respecting that API in a convenient manner.
The same issue arises naturally when designing a KE space, and [`KeFormat`](key_expr/format/struct.KeFormat.html "struct zenoh_keyexpr::key_expr::format::KeFormat") was designed to help you with this,
both in constructing and in parsing KEs that fit the formats you’ve defined.

`KeFormat`

[`kedefine`](https://docs.rs/zenoh/latest/zenoh/key_expr/format/macro.kedefine.html) also allows you to define formats at compile time, allowing a more performant, but more importantly safer and more convenient use of said formats,
as the [`keformat`](https://docs.rs/zenoh/latest/zenoh/key_expr/format/macro.keformat.html) and [`kewrite`](https://docs.rs/zenoh/latest/zenoh/key_expr/format/macro.kewrite.html) macros will be able to tell you if you’re attempting to set fields of the format that do not exist.

`kedefine`
`keformat`
`kewrite`

## Re-exports[§](#reexports)

`pub use key_expr::*;`

## Modules[§](#modules)

`keyexpr`

---

# https://docs.rs/zenoh-link/latest/zenoh_link/

Source: https://docs.rs/zenoh-link/latest/zenoh_link/

## [Crate zenoh\_link](#)



# Crate zenoh\_link

[Source](../src/zenoh_link/lib.rs.html#15-425)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Modules[§](#modules)

[tcp](tcp/index.html "mod zenoh_link::tcp")

## Structs[§](#structs)

[EndPoint](struct.EndPoint.html "struct zenoh_link::EndPoint")
:   A string that respects the [`EndPoint`](struct.EndPoint.html "struct zenoh_link::EndPoint") canon form: `[#]`.

[Link](struct.Link.html "struct zenoh_link::Link")

[LinkConfigurator](struct.LinkConfigurator.html "struct zenoh_link::LinkConfigurator")

[LinkManagerBuilderMulticast](struct.LinkManagerBuilderMulticast.html "struct zenoh_link::LinkManagerBuilderMulticast")

[LinkManagerBuilderUnicast](struct.LinkManagerBuilderUnicast.html "struct zenoh_link::LinkManagerBuilderUnicast")

[LinkMulticast](struct.LinkMulticast.html "struct zenoh_link::LinkMulticast")

[LinkUnicast](struct.LinkUnicast.html "struct zenoh_link::LinkUnicast")

[ListenerUnicastIP](struct.ListenerUnicastIP.html "struct zenoh_link::ListenerUnicastIP")

[ListenersUnicastIP](struct.ListenersUnicastIP.html "struct zenoh_link::ListenersUnicastIP")

[Locator](struct.Locator.html "struct zenoh_link::Locator")
:   A string that respects the [`Locator`](struct.Locator.html "struct zenoh_link::Locator") canon form: `/[?]`.

[LocatorInspector](struct.LocatorInspector.html "struct zenoh_link::LocatorInspector")

## Enums[§](#enums)

[LinkAuthId](enum.LinkAuthId.html "enum zenoh_link::LinkAuthId")

[LinkKind](enum.LinkKind.html "enum zenoh_link::LinkKind")

## Constants[§](#constants)

[ALL\_SUPPORTED\_LINKS](constant.ALL_SUPPORTED_LINKS.html "constant zenoh_link::ALL_SUPPORTED_LINKS")

[BIND\_INTERFACE](constant.BIND_INTERFACE.html "constant zenoh_link::BIND_INTERFACE")

[BIND\_SOCKET](constant.BIND_SOCKET.html "constant zenoh_link::BIND_SOCKET")

[DSCP](constant.DSCP.html "constant zenoh_link::DSCP")

[TCP\_SO\_RCV\_BUF](constant.TCP_SO_RCV_BUF.html "constant zenoh_link::TCP_SO_RCV_BUF")

[TCP\_SO\_SND\_BUF](constant.TCP_SO_SND_BUF.html "constant zenoh_link::TCP_SO_SND_BUF")

## Traits[§](#traits)

[ConfigurationInspector](trait.ConfigurationInspector.html "trait zenoh_link::ConfigurationInspector")

[ConstructibleLinkManagerUnicast](trait.ConstructibleLinkManagerUnicast.html "trait zenoh_link::ConstructibleLinkManagerUnicast")

[LinkManagerMulticastTrait](trait.LinkManagerMulticastTrait.html "trait zenoh_link::LinkManagerMulticastTrait")

[LinkManagerUnicastTrait](trait.LinkManagerUnicastTrait.html "trait zenoh_link::LinkManagerUnicastTrait")

[LinkMulticastTrait](trait.LinkMulticastTrait.html "trait zenoh_link::LinkMulticastTrait")

[LinkUnicastTrait](trait.LinkUnicastTrait.html "trait zenoh_link::LinkUnicastTrait")

## Functions[§](#functions)

[get\_ip\_interface\_names](fn.get_ip_interface_names.html "fn zenoh_link::get_ip_interface_names")

[parse\_dscp](fn.parse_dscp.html "fn zenoh_link::parse_dscp")
:   Parse DSCP config.

[set\_dscp](fn.set_dscp.html "fn zenoh_link::set_dscp")
:   Set DSCP option to the socket if supported by the target.

## Type Aliases[§](#types)

[LinkManagerMulticast](type.LinkManagerMulticast.html "type zenoh_link::LinkManagerMulticast")

[LinkManagerUnicast](type.LinkManagerUnicast.html "type zenoh_link::LinkManagerUnicast")

[NewLinkChannelSender](type.NewLinkChannelSender.html "type zenoh_link::NewLinkChannelSender")

---

# https://docs.rs/zenoh-macros/latest/zenoh_macros/

Source: https://docs.rs/zenoh-macros/latest/zenoh_macros/

## [Crate zenoh\_macros](#)

## [zenoh\_macros](../zenoh_macros/index.html)1.7.2

### [Crate Items](#macros)

# Crate zenoh\_macros Copy item path

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Macros[§](#macros)

`keyexpr::new`
`Formatter`
`OwnedKeyExpr`
`Formatter`
`keformat`
`nonwild_keyexpr::new`

## Attribute Macros[§](#attributes)

`#[cfg(feature = "internal")]`
`#[doc(hidden)]`
`#[internal_trait]`
`impl Trait for Struct { ... }`
`#[cfg(feature = "unstable")]`
`#[cfg(feature = "unstable")]`

## Derive Macros[§](#derives)

`Param`
`T`
`trait DefaultParam { fn param() -> Param; }`
`Enum`
`Param`

---

# https://docs.rs/zenoh-plugin-trait/latest/zenoh_plugin_trait/

Source: https://docs.rs/zenoh-plugin-trait/latest/zenoh_plugin_trait/

## [Crate zenoh\_plugin\_trait](#)

## [zenoh\_plugin\_trait](../zenoh_plugin_trait/index.html)1.7.2

### [Sections](#)

### [Crate Items](#macros)

# Crate zenoh\_plugin\_trait Copy item path

## [§](#the-plugin-infrastructure-for-zenoh)The plugin infrastructure for Zenoh.

To build a plugin, implement [`Plugin`](trait.Plugin.html "trait zenoh_plugin_trait::Plugin").

`Plugin`

If building a plugin for [`zenohd`](https://crates.io/crates/zenoh), you should use the types exported in [`zenoh::plugins`](https://docs.rs/zenoh/latest/zenoh/plugins) to fill [`Plugin`](trait.Plugin.html "trait zenoh_plugin_trait::Plugin")’s associated types.
To check your plugin typing for `zenohd`, have your plugin implement [`zenoh::plugins::ZenohPlugin`](https://docs.rs/zenoh/latest/zenoh/plugins/struct.ZenohPlugin)

`zenohd`
`zenoh::plugins`
`Plugin`
`zenohd`
`zenoh::plugins::ZenohPlugin`

Plugin is a struct which implements the [`Plugin`](trait.Plugin.html "trait zenoh_plugin_trait::Plugin") trait. This trait has two associated types:

`Plugin`
`StartArgs`
`start`
`Instance`

The actual work of the plugin is performed by the instance, which is created by the [`start`](trait.Plugin.html#tymethod.start "associated function zenoh_plugin_trait::Plugin::start") function.

`start`

Plugins are loaded, started and stopped by [`PluginsManager`](struct.PluginsManager.html "struct zenoh_plugin_trait::PluginsManager"). Stopping plugin is just dropping it’s instance.

`PluginsManager`

Plugins can be static and dynamic.

Static plugin is just a type which implements [`Plugin`](trait.Plugin.html "trait zenoh_plugin_trait::Plugin") trait. It can be added to [`PluginsManager`](struct.PluginsManager.html "struct zenoh_plugin_trait::PluginsManager") by [`PluginsManager::declare_static_plugin`](struct.PluginsManager.html#method.declare_static_plugin "method zenoh_plugin_trait::PluginsManager::declare_static_plugin") method.

`Plugin`
`PluginsManager`
`PluginsManager::declare_static_plugin`

Dynamic plugin is a shared library which exports set of C-repr (unmangled) functions which allows to check plugin compatibility and create plugin instance. These functions are defined automatically by [`declare_plugin`](macro.declare_plugin.html "macro zenoh_plugin_trait::declare_plugin") macro.

`declare_plugin`

## Macros[§](#macros)

## Structs[§](#structs)

`Self::declare_dynamic_plugin_by_name`
`Self::declare_dynamic_plugin_by_paths`
`Self::declare_static_plugin`

## Enums[§](#enums)

## Constants[§](#constants)

## Traits[§](#traits)

## Type Aliases[§](#types)

---

# https://docs.rs/zenoh-protocol/latest/zenoh_protocol/

Source: https://docs.rs/zenoh-protocol/latest/zenoh_protocol/

## [Crate zenoh\_protocol](#)



# Crate zenoh\_protocol

[Source](../src/zenoh_protocol/lib.rs.html#15-31)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Modules[§](#modules)

[common](common/index.html "mod zenoh_protocol::common")

[core](core/index.html "mod zenoh_protocol::core")

[network](network/index.html "mod zenoh_protocol::network")

[scouting](scouting/index.html "mod zenoh_protocol::scouting")

[transport](transport/index.html "mod zenoh_protocol::transport")

[zenoh](zenoh/index.html "mod zenoh_protocol::zenoh")

## Macros[§](#macros)

[zextunit](macro.zextunit.html "macro zenoh_protocol::zextunit")

[zextz64](macro.zextz64.html "macro zenoh_protocol::zextz64")

[zextzbuf](macro.zextzbuf.html "macro zenoh_protocol::zextzbuf")

## Constants[§](#constants)

[VERSION](constant.VERSION.html "constant zenoh_protocol::VERSION")

---

# https://docs.rs/zenoh-result/latest/zenoh_result/

Source: https://docs.rs/zenoh-result/latest/zenoh_result/

## [Crate zenoh\_result](#)



# Crate zenoh\_result

[Source](../src/zenoh_result/lib.rs.html#15-346)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Macros[§](#macros)

[anyhow](macro.anyhow.html "macro zenoh_result::anyhow")
:   Construct an ad-hoc error from a string or existing non-`anyhow` error value.

[bail](macro.bail.html "macro zenoh_result::bail")

[to\_zerror](macro.to_zerror.html "macro zenoh_result::to_zerror")

[zerror](macro.zerror.html "macro zenoh_result::zerror")

## Structs[§](#structs)

[NegativeI8](struct.NegativeI8.html "struct zenoh_result::NegativeI8")

[ShmError](struct.ShmError.html "struct zenoh_result::ShmError")

[ZError](struct.ZError.html "struct zenoh_result::ZError")

## Traits[§](#traits)

[ErrNo](trait.ErrNo.html "trait zenoh_result::ErrNo")

[IError](trait.IError.html "trait zenoh_result::IError")
:   `Error` is a trait representing the basic expectations for error values, i.e., values of type `E` in [`Result`](https://doc.rust-lang.org/nightly/core/result/enum.Result.html "enum core::result::Result").

## Functions[§](#functions)

[cold](fn.cold.html "fn zenoh_result::cold")

[likely](fn.likely.html "fn zenoh_result::likely")

[unlikely](fn.unlikely.html "fn zenoh_result::unlikely")

## Type Aliases[§](#types)

[Error](type.Error.html "type zenoh_result::Error")

[ZResult](type.ZResult.html "type zenoh_result::ZResult")

---

# https://docs.rs/zenoh-shm/latest/zenoh_shm/

Source: https://docs.rs/zenoh-shm/latest/zenoh_shm/

## [Crate zenoh\_shm](#)



# Crate zenoh\_shm

[Source](../src/zenoh_shm/lib.rs.html#15-340)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Modules[§](#modules)

[api](api/index.html "mod zenoh_shm::api")

[header](header/index.html "mod zenoh_shm::header")

[init](init/index.html "mod zenoh_shm::init")

[metadata](metadata/index.html "mod zenoh_shm::metadata")

[posix\_shm](posix_shm/index.html "mod zenoh_shm::posix_shm")

[reader](reader/index.html "mod zenoh_shm::reader")

[version](version/index.html "mod zenoh_shm::version")

[watchdog](watchdog/index.html "mod zenoh_shm::watchdog")

## Macros[§](#macros)

[tested\_crate\_module](macro.tested_crate_module.html "macro zenoh_shm::tested_crate_module")

[tested\_module](macro.tested_module.html "macro zenoh_shm::tested_module")

## Structs[§](#structs)

[ShmBufInfo](struct.ShmBufInfo.html "struct zenoh_shm::ShmBufInfo")
:   Information about a [`ShmBufInner`](struct.ShmBufInner.html "struct zenoh_shm::ShmBufInner").

[ShmBufInner](struct.ShmBufInner.html "struct zenoh_shm::ShmBufInner")
:   A zenoh buffer in shared memory.

---

# https://docs.rs/zenoh-sync/latest/zenoh_sync/

Source: https://docs.rs/zenoh-sync/latest/zenoh_sync/

## [Crate zenoh\_sync](#)



# Crate zenoh\_sync

[Source](../src/zenoh_sync/lib.rs.html#15-72)

Expand description

⚠️ WARNING ⚠️

This module is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Re-exports[§](#reexports)

`pub use event::*;`

`pub use fifo_queue::*;`

`pub use lifo_queue::*;`

`pub use object_pool::*;`

`pub use mvar::*;`

`pub use condition::*;`

`pub use signal::*;`

`pub use cache::*;`

## Modules[§](#modules)

[cache](cache/index.html "mod zenoh_sync::cache")

[condition](condition/index.html "mod zenoh_sync::condition")

[event](event/index.html "mod zenoh_sync::event")

[fifo\_queue](fifo_queue/index.html "mod zenoh_sync::fifo_queue")

[lifo\_queue](lifo_queue/index.html "mod zenoh_sync::lifo_queue")

[mvar](mvar/index.html "mod zenoh_sync::mvar")

[object\_pool](object_pool/index.html "mod zenoh_sync::object_pool")

[signal](signal/index.html "mod zenoh_sync::signal")

## Structs[§](#structs)

[PinBoxFuture](struct.PinBoxFuture.html "struct zenoh_sync::PinBoxFuture")
:   An alias for `Pin + Send>>`.

## Functions[§](#functions)

[get\_mut\_unchecked](fn.get_mut_unchecked.html "fn zenoh_sync::get_mut_unchecked")

[pinbox](fn.pinbox.html "fn zenoh_sync::pinbox")

---

# https://docs.rs/zenoh-transport/latest/zenoh_transport/

Source: https://docs.rs/zenoh-transport/latest/zenoh_transport/

## [Crate zenoh\_transport](#)



# Crate zenoh\_transport

[Source](../src/zenoh_transport/lib.rs.html#15-141)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Re-exports[§](#reexports)

`pub use manager::*;`

## Modules[§](#modules)

[common](common/index.html "mod zenoh_transport::common")

[manager](manager/index.html "mod zenoh_transport::manager")

[multicast](multicast/index.html "mod zenoh_transport::multicast")

[unicast](unicast/index.html "mod zenoh_transport::unicast")

## Structs[§](#structs)

[DummyTransportEventHandler](struct.DummyTransportEventHandler.html "struct zenoh_transport::DummyTransportEventHandler")

[DummyTransportMulticastEventHandler](struct.DummyTransportMulticastEventHandler.html "struct zenoh_transport::DummyTransportMulticastEventHandler")

[DummyTransportPeerEventHandler](struct.DummyTransportPeerEventHandler.html "struct zenoh_transport::DummyTransportPeerEventHandler")

[TransportPeer](struct.TransportPeer.html "struct zenoh_transport::TransportPeer")

## Traits[§](#traits)

[TransportEventHandler](trait.TransportEventHandler.html "trait zenoh_transport::TransportEventHandler")

[TransportMulticastEventHandler](trait.TransportMulticastEventHandler.html "trait zenoh_transport::TransportMulticastEventHandler")

[TransportPeerEventHandler](trait.TransportPeerEventHandler.html "trait zenoh_transport::TransportPeerEventHandler")

---

# https://docs.rs/zenoh-util/latest/zenoh_util/

Source: https://docs.rs/zenoh-util/latest/zenoh_util/

## [Crate zenoh\_util](#)



# Crate zenoh\_util

[Source](../src/zenoh_util/lib.rs.html#15-72)

Expand description

⚠️ WARNING ⚠️

This crate is intended for Zenoh’s internal use.

[Click here for Zenoh’s documentation](https://docs.rs/zenoh/latest/zenoh)

## Re-exports[§](#reexports)

`pub use timer::*;`

`pub use lib_search_dirs::*;`

`pub use log::*;`

## Modules[§](#modules)

[ffi](ffi/index.html "mod zenoh_util::ffi")

[lib\_search\_dirs](lib_search_dirs/index.html "mod zenoh_util::lib_search_dirs")

[log](log/index.html "mod zenoh_util::log")

[net](net/index.html "mod zenoh_util::net")

[time\_range](time_range/index.html "mod zenoh_util::time_range")

[timer](timer/index.html "mod zenoh_util::timer")

## Macros[§](#macros)

[concat\_enabled\_features](macro.concat_enabled_features.html "macro zenoh_util::concat_enabled_features")

## Structs[§](#structs)

[LIB\_PREFIX](struct.LIB_PREFIX.html "struct zenoh_util::LIB_PREFIX")

[LIB\_SUFFIX](struct.LIB_SUFFIX.html "struct zenoh_util::LIB_SUFFIX")

[LibLoader](struct.LibLoader.html "struct zenoh_util::LibLoader")
:   LibLoader allows search for libraries and to load them.

## Constants[§](#constants)

[ZENOH\_HOME\_ENV\_VAR](constant.ZENOH_HOME_ENV_VAR.html "constant zenoh_util::ZENOH_HOME_ENV_VAR")
:   The “ZENOH\_HOME” environment variable name

## Functions[§](#functions)

[zenoh\_home](fn.zenoh_home.html "fn zenoh_util::zenoh_home")
:   Return the path to the ${ZENOH\_HOME} directory (~/.zenoh by default).

---

# https://docs.rs/zenoh/latest/zenoh/config/index.html

Source: https://docs.rs/zenoh/latest/zenoh/config/index.html

## [Module config](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module config](#)

### [Sections](#)

`open`
`scout`

### [Module Items](#structs)

## [In crate zenoh](../index.html)

# Module config Copy item path

## [§](#configuration-to-pass-to-open-and-scout-functions-and-associated-constants)Configuration to pass to [`open`](../fn.open.html "fn zenoh::open") and [`scout`](../fn.scout.html "fn zenoh::scout") functions and associated constants.

`open`
`scout`

The [`Config`](../struct.Config.html "struct zenoh::Config") object contains all parameters necessary to configure
a Zenoh session or the scouting process. Usually a configuration file is stored in the json or
yaml format and loaded using the [`Config::from_file`](../struct.Config.html#method.from_file "associated function zenoh::Config::from_file") method.
It’s also possible to read or
modify individual elements of the `Config` with the
[`Config::insert_json5`](../struct.Config.html#method.insert_json5 "method zenoh::Config::insert_json5")
and [`Config::get_json`](../struct.Config.html#method.get_json "method zenoh::Config::get_json") methods.

`Config`
`Config::from_file`
`Config`
`Config::insert_json5`
`Config::get_json`

An example configuration file is available in the [`Config`](../struct.Config.html "struct zenoh::Config") documentation section
and in the Zenoh repository as
[DEFAULT\_CONFIG.json5](https://github.com/eclipse-zenoh/zenoh/blob/release/1.0.0/DEFAULT_CONFIG.json5)

`Config`

## [§](#example)Example

`use zenoh::config::Config;
use serde_json::json;
let mut config = Config::from_file("path/to/config.json5").unwrap();
config.insert_json5("scouting/multicast/enabled", &json!(false).to_string()).unwrap();
let session = zenoh::open(config).await.unwrap();`

## Structs[§](#structs)

`EndPoint`
`<locator>[#<config>]`
`Locator`
`<proto>/<address>[?<metadata>]`
`unstable`
`Config`
`Session::config`
`Session`
`WhatAmI`

## Enums[§](#enums)

---

# https://docs.rs/zenoh/latest/zenoh/handlers/index.html

Source: https://docs.rs/zenoh/latest/zenoh/handlers/index.html

## [Module handlers](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module handlers](#)

### [Sections](#)

### [Module Items](#modules)

## [In crate zenoh](../index.html)

# Module handlers Copy item path

## [§](#callback-handler-trait)Callback handler trait.

Zenoh allows two ways to get sequential data from Zenoh primitives, like
[`Subscriber`](../pubsub/struct.Subscriber.html "struct zenoh::pubsub::Subscriber") or [`Query`](../query/struct.Query.html "struct zenoh::query::Query")

`Subscriber`
`Query`

**Callback functions**: the user provides a callback function that is called with each
incoming sample.

**Channels**: the user provides a channel that buffers incoming samples, and the user
retrieves samples from the channel when needed.

## [§](#-important-note)⚠️ Important Note

**Warning**: The callback function is called in the context of the Zenoh runtime.
Calling zenoh network operations from the callback (e.g., making queries)
may lead to deadlocks and other unexpected behaviors.

The Rust type system is not used to prevent calling zenoh network operations
from the callback for two reasons:

Below are the details of how channels work in Zenoh.

Under the hood, the sequential data from a primitive is always passed to a callback function.
However, to simplify using channels, Zenoh provides the
[`IntoHandler`](trait.IntoHandler.html "trait zenoh::handlers::IntoHandler") trait,
which returns a pair: a callback which pushes data to the channel and a “handler”
which allows retrieving data from the channel.

`IntoHandler`

The method [`with`](../pubsub/struct.SubscriberBuilder.html#method.with "method zenoh::pubsub::SubscriberBuilder::with") accepts any type that
implements the `IntoHandler` trait and extracts the callback and handler from it.
The Zenoh object calls the callback with each incoming sample.

`with`
`IntoHandler`

The handler is also stored in the Zenoh object. It’s completely opaque to the Zenoh object;
it’s just made available to the user via the [`handler`](../pubsub/struct.Subscriber.html#method.handler "method zenoh::pubsub::Subscriber::handler") method
or by dereferencing, allowing the user to call the handler’s methods directly on the
`Subscriber` or `Query` object.
This is syntactic sugar that allows the user not to care about the separate channel object.

`handler`
`Subscriber`
`Query`

The example of using channels is shown below.

`let subscriber = session.declare_subscriber("key/expression")
.with(zenoh::handlers::RingChannel::new(10))
.await.unwrap();
while let Ok(sample) = subscriber.recv_async().await {
println!("Received: {:?}", sample);
}`

Note that this code is equivalent to the following one, where the channel
and the callback are created explicitly.

`use zenoh::handlers::IntoHandler;
let (callback, mut ring_channel_handler)
= zenoh::handlers::RingChannel::new(10).into_handler();
let subscriber = session.declare_subscriber("key/expression")
.with((callback, ())) // or simply .callback(callback)
.await.unwrap();
while let Ok(sample) = ring_channel_handler.recv_async().await {
println!("Received: {:?}", sample);
}`

Obviously, the callback can also be defined manually, without using a channel, and passed
to the [`callback`](../pubsub/struct.SubscriberBuilder.html#method.callback "method zenoh::pubsub::SubscriberBuilder::callback") method.
In this case, the handler type is `()`, and no additional methods, like `recv_async`, are available on the
subscriber object.

`callback`
`()`
`recv_async`
`let subscriber = session.declare_subscriber("key/expression")
.callback(|sample| {
println!("Received: {:?}", sample);
}).await.unwrap();`

## Modules[§](#modules)

## Structs[§](#structs)

`FifoChannel`

## Traits[§](#traits)

`Callback`
`Handler`

---

# https://docs.rs/zenoh/latest/zenoh/key_expr/index.html

Source: https://docs.rs/zenoh/latest/zenoh/key_expr/index.html

## [Module key\_expr](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module key\_expr](#)

### [Sections](#)

### [Module Items](#modules)

## [In crate zenoh](../index.html)

# Module key\_expr Copy item path

## [§](#key-expressions)Key Expressions

[Key expressions](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md) are Zenoh’s address space.

In Zenoh, operations are performed on keys. To allow addressing multiple keys with a single operation, Zenoh uses Key Expressions (KEs).
KEs are a small language that expresses sets of keys through a glob-like syntax.

These semantics can be a bit difficult to implement, so this module provides the following facilities:

## [§](#storing-key-expressions)Storing Key Expressions

This module provides three ways to store strings that have been validated to respect the KE syntax:

`keyexpr`
`str`
`OwnedKeyExpr`
`std::sync::Arc<str>`
`KeyExpr`
`std::borrow::Cow<str>`

The key expression object can be created using the [`KeyExpr::new`](struct.KeyExpr.html#method.new "associated function zenoh::key_expr::KeyExpr::new") method,
which validates the syntax of the provided string.
The [`KeyExpr::from_str_unchecked`](struct.KeyExpr.html#method.from_str_unchecked "associated function zenoh::key_expr::KeyExpr::from_str_unchecked") method allows to
accelerate the creation of key expressions when the user can guarantee that the provided string
respects the KE syntax. There is also the
[`Session::declare_keyexpr`](../struct.Session.html#method.declare_keyexpr "method zenoh::Session::declare_keyexpr") method, which not only
declares the key expression, but also informs the Zenoh network of its existence, which can
accelerate routing.

`KeyExpr::new`
`KeyExpr::from_str_unchecked`
`Session::declare_keyexpr`

All of these types implement [`Deref`](https://doc.rust-lang.org/nightly/core/ops/deref/trait.Deref.html "trait core::ops::deref::Deref") to [`keyexpr`](struct.keyexpr.html "struct zenoh::key_expr::keyexpr"), which notably has methods to check whether a given key expression
[`intersects`](struct.keyexpr.html#method.intersects "method zenoh::key_expr::keyexpr::intersects") with another, or whether it [`includes`](struct.keyexpr.html#method.includes "method zenoh::key_expr::keyexpr::includes") another.

`Deref`
`keyexpr`
`intersects`
`includes`

## [§](#tying-values-to-key-expressions)Tying values to Key Expressions

When storing values tied to Key Expressions, you might want something more specialized than a [`HashMap`](https://doc.rust-lang.org/nightly/std/collections/hash/map/struct.HashMap.html "struct std::collections::hash::map::HashMap") to respect
Key Expression semantics with high performance.

`HashMap`

Enter [`KeTrees`](keyexpr_tree/index.html "mod zenoh::key_expr::keyexpr_tree"). These are data structures built to store KE–value pairs in a manner that supports the set semantics of KEs.

`KeTrees`

## [§](#building-and-parsing-key-expressions)Building and parsing Key Expressions

A common issue in REST APIs is assigning meaning to sections of the URL and respecting that API in a convenient manner.
The same issue arises naturally when designing a KE space, and [`KeFormat`](format/struct.KeFormat.html "struct zenoh::key_expr::format::KeFormat") was designed to help with this,
both in constructing and parsing KEs that fit the formats you’ve defined.

`KeFormat`

[`kedefine`](format/macro.kedefine.html "macro zenoh::key_expr::format::kedefine") also lets you define formats at compile time, enabling a more performant—and, more importantly, safer and more convenient—use of said formats,
as the [`keformat`](format/macro.keformat.html "macro zenoh::key_expr::format::keformat") and [`kewrite`](format/macro.kewrite.html "macro zenoh::key_expr::format::kewrite") macros will tell you if you’re attempting to set fields of the format that do not exist.

`kedefine`
`keformat`
`kewrite`

## [§](#example)Example

`let sensor = zenoh::key_expr::KeyExpr::new("robot/sensor").unwrap();
let sensor_temp = sensor.join("temp").unwrap();
let sensors = sensor.join("**").unwrap();
assert!(sensors.includes(&sensor_temp));`

## Modules[§](#modules)

`unstable`
`unstable`

## Structs[§](#structs)

`keyexpr`
`Session`
`Resolvable`
`Session::undeclare`
`KeyExpr`
`Arc<str>`
`Arc<str>`
`str`

## Enums[§](#enums)

`unstable`

## Traits[§](#traits)

`KeyExpr::autocanonize()`

---

# https://docs.rs/zenoh/latest/zenoh/query/index.html

Source: https://docs.rs/zenoh/latest/zenoh/query/index.html

## [Module query](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module query](#)

### [Sections](#)

### [Module Items](#structs)

## [In crate zenoh](../index.html)

# Module query Copy item path

## [§](#queryreply-primitives)Query/reply primitives

This module provides the query/reply API of Zenoh.

A [`Queryable`](struct.Queryable.html "struct zenoh::query::Queryable") is declared by the
[`Session::declare_queryable`](../struct.Session.html#method.declare_queryable "method zenoh::Session::declare_queryable") method
and serves queries [`Query`](struct.Query.html "struct zenoh::query::Query") using a callback
or a channel (see [handlers](../handlers/index.html "mod zenoh::handlers") module documentation for details).

`Queryable`
`Session::declare_queryable`
`Query`

The [`Query`](struct.Query.html "struct zenoh::query::Query") has the methods [`reply`](struct.Query.html#method.reply "method zenoh::query::Query::reply")
to reply with a data sample,
and [`reply_err`](struct.Query.html#method.reply_err "method zenoh::query::Query::reply_err") to send an error reply.

`Query`
`reply`
`reply_err`

The `reply` method sends a [`Sample`](../sample/struct.Sample.html "struct zenoh::sample::Sample") with a [`kind`](../sample/struct.Sample.html#method.kind "method zenoh::sample::Sample::kind")
field set to [`Put`](../sample/enum.SampleKind.html#variant.Put "variant zenoh::sample::SampleKind::Put").
If it’s necessary to reply with a [`Delete`](../sample/enum.SampleKind.html#variant.Delete "variant zenoh::sample::SampleKind::Delete") sample,
the [`reply_del`](struct.Query.html#method.reply_del "method zenoh::query::Query::reply_del") method should be used.

`reply`
`Sample`
`kind`
`Put`
`Delete`
`reply_del`

Data is requested from queryables via the [`Session::get`](../struct.Session.html#method.get "method zenoh::Session::get") function or by
a [`Querier`](struct.Querier.html "struct zenoh::query::Querier") object. Each request returns
zero or more [`Reply`](struct.Reply.html "struct zenoh::query::Reply") structures, each one from each queryable
that matches the request.
The reply contains either a [`Sample`](../sample/struct.Sample.html "struct zenoh::sample::Sample")
or a [`ReplyError`](struct.ReplyError.html "struct zenoh::query::ReplyError").

`Session::get`
`Querier`
`Reply`
`Sample`
`ReplyError`

## [§](#query-parameters)Query parameters

The query/reply API allows specifying additional parameters for the request.
These parameters are passed to the get operation using the [`Selector`](struct.Selector.html "struct zenoh::query::Selector")
syntax. The selector string has a syntax similar to a URL:
it’s a key expression followed by a question mark and the list of parameters in the format
“name=value” separated by ‘;’.
For example `key/expression?param1=value1;param2=value2`.

`Selector`
`key/expression?param1=value1;param2=value2`

## [§](#examples)Examples:

#### [§](#declaring-a-queryable)Declaring a queryable

The example below shows a queryable that replies with temperature data for a given day.

`let key_expr = "room/temperature/history";
let queryable = session.declare_queryable(key_expr).await.unwrap();
while let Ok(query) = queryable.recv_async().await {
if let Some(day)= query.selector().parameters().get("day") {
if let Some(value) = temperature_data.get(day) {
query.reply(key_expr, value).await.unwrap();
} else {
query.reply_err("no data for this day").await.unwrap();
}
} else {
query.reply_err("missing day parameter").await.unwrap();
}
}`

### [§](#requesting-data)Requesting data

The corresponding request for the above queryable requests the temperature for a given day.

`let replies = session.get("room/temperature/history?day=2023-03-15").await.unwrap();
while let Ok(reply) = replies.recv_async().await {
match reply.result() {
Ok(sample) => {
println!(">> Temperature is {}", sample.payload().try_to_string().unwrap());
}
Err(err) => {
println!(">> Error {}", err.payload().try_to_string().unwrap());
}
}`

## Structs[§](#structs)

`;`
`<newline>`
`=`
`Queryable`
`Querier`
`Session::declare_querier`
`get`
`Querier`
`handler`
`Reply`
`Resolvable`
`Queryable`
`get`
`Queryable`
`Queryable`
`Session::declare_queryable`
`Resolvable`
`Queryable`
`Queryable`
`Reply`
`Query::reply()`
`Query::reply_del()`
`ReplyBuilder`
`Delete`
`ReplyBuilder`
`Put`
`ReplyError`
`Query::reply_err()`
`Querier::get`
`Session::get`
`Reply`
`Key Expression`
`Parameters`
`unstable`

## Enums[§](#enums)

`Queryable`
`Session::get`
`Querier::get`
`unstable`
`unstable`
`unstable`

## Traits[§](#traits)

`unstable`

---

# https://docs.rs/zenoh/latest/zenoh/sample/index.html

Source: https://docs.rs/zenoh/latest/zenoh/sample/index.html

## [Module sample](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module sample](#)

### [Sections](#)

### [Module Items](#structs)

## [In crate zenoh](../index.html)

# Module sample Copy item path

## [§](#sample-primitives)Sample primitives

The [`Sample`](struct.Sample.html "struct zenoh::sample::Sample") structure is the data unit received
by [`Subscriber`](../pubsub/struct.Subscriber.html "struct zenoh::pubsub::Subscriber") or [`Querier`](../query/struct.Querier.html "struct zenoh::query::Querier")
or [`Session::get`](../struct.Session.html#method.get "method zenoh::Session::get"). It contains the payload and all metadata associated with the data.

`Sample`
`Subscriber`
`Querier`
`Session::get`

The module contains the definitions of the `Sample` itself, definitions of
types of its fields, and builders to create the sample.

`Sample`

In practice, users do not need to create samples manually, as they are created
by the Zenoh runtime when data is published or replied to a query. But sometimes
it’s useful to create samples, for example, for the simulation of data reception,
so the [`SampleBuilder`](struct.SampleBuilder.html "struct zenoh::sample::SampleBuilder") is provided.

`SampleBuilder`

The [`SampleFields`](struct.SampleFields.html "struct zenoh::sample::SampleFields") structure contains `Sample`
fields as public members, unlike the `Sample` itself where fields are private.
This allows deconstructing a sample to fields without cloning, which is more efficient
than using getter methods.

`SampleFields`
`Sample`
`Sample`

## Structs[§](#structs)

`Sample`
`Subscriber`
`Querier`
`Session::get`
`Sample`
`SampleBuilder`
`kind`
`SampleBuilder`
`Delete`
`SampleBuilder`
`Put`
`Sample`
`clone()`
`Sample`
`unstable`
`Sample`

## Enums[§](#enums)

`Sample`

## Type Aliases[§](#types)

`unstable`
`Sample`

---

# https://docs.rs/zenoh/latest/zenoh/session/index.html

Source: https://docs.rs/zenoh/latest/zenoh/session/index.html

## [Module session](#)

## [zenoh](../../zenoh/index.html)1.7.2

## [Module session](#)

### [Sections](#)

`Session`

### [Module Items](#structs)

## [In crate zenoh](../index.html)

# Module session Copy item path

## [§](#zenoh-session-and-associated-types)Zenoh [`Session`](../struct.Session.html "struct zenoh::Session") and associated types

`Session`

The [`Session`](../struct.Session.html "struct zenoh::Session") is the main component of Zenoh. It holds the zenoh runtime object,
which maintains the state of the connection of the node to the Zenoh network.

`Session`

The session allows declaring other zenoh entities like publishers, subscribers, queriers, queryables, etc.
and keeps them functioning. Closing the session will close all associated entities.

The session is cloneable so it’s easy to share it between tasks and threads. Each clone of the
session is an `Arc` to the internal session object, so cloning is cheap and fast.

`Arc`

A Zenoh session is instantiated using [`zenoh::open`](../fn.open.html "fn zenoh::open")
with parameters specified in the [`Config`](../struct.Config.html "struct zenoh::Config") object.

`zenoh::open`
`Config`

## Structs[§](#structs)

`Session::close`
`unstable`
`crate::open`
`Session`
`SessionInfo::peers_zid()`
`ZenohId`
`SessionInfo::routers_zid()`
`ZenohId`
`ZenohId`
`Session`
`get`
`Session`
`handler`
`Reply`
`Session::info()`
`Session`
`SessionInfo::zid()`
`ZenohId`
`Session`

## Traits[§](#traits)

## Functions[§](#functions)

`Session`

## Type Aliases[§](#types)

`unstable`
`Session`
`PublicationBuilder`
`Session::delete`
`PublicationBuilder`
`Session::put`

---

# https://docs.rs/zenoh/latest/zenoh/

Source: https://docs.rs/zenoh/latest/zenoh/

## [Crate zenoh](#)

## [zenoh](../zenoh/index.html)1.7.2

### [Sections](#)

### [Crate Items](#modules)

# Crate zenoh Copy item path

[Zenoh](https://zenoh.io) /zeno/ is a stack that unifies data in motion, data at
rest, and computations. It elegantly blends traditional pub/sub with geo-distributed
storage, queries, and computations, while retaining a level of time and space efficiency
that is well beyond any of the mainstream stacks.

## [§](#components-and-concepts)Components and concepts

The main Zenoh components and concepts are described below.

### [§](#session)Session

The root element of the Zenoh API is the [session](session/index.html "mod zenoh::session").
A session is created by the [`open`](fn.open.html "fn zenoh::open") function, which takes a [config](config/index.html "mod zenoh::config") as an argument.
The [`Session`](struct.Session.html "struct zenoh::Session") holds the runtime object,
which maintains the connection to the Zenoh network.

`open`
`Session`

The Zenoh protocol allows nodes to form a graph with an arbitrary topology, such as a mesh, a star, or a clique.
There is a `mode` parameter in the [config](config/index.html "mod zenoh::config") which specifies the role of the node in the topology: a peer, router or client.
See [`WhatAmI`](config/enum.WhatAmI.html "enum zenoh::config::WhatAmI") for details.

`mode`
`WhatAmI`

Zenoh supports two paradigms of communication: publish/subscribe and query/reply.
The entities that perform the communication (e.g., publishers, subscribers, queriers, and queryables) are declared by the session object.

### [§](#publishsubscribe)Publish/Subscribe

In the publish/subscribe paradigm, data is produced by [`Publisher`](pubsub/struct.Publisher.html "struct zenoh::pubsub::Publisher")
and consumed by [`Subscriber`](pubsub/struct.Subscriber.html "struct zenoh::pubsub::Subscriber"). See the [pubsub](pubsub/index.html "mod zenoh::pubsub") API for details.

`Publisher`
`Subscriber`

### [§](#queryreply)Query/Reply

In the query/reply paradigm, data is made available by [`Queryable`](query/struct.Queryable.html "struct zenoh::query::Queryable")
and requested by [`Querier`](query/struct.Querier.html "struct zenoh::query::Querier") or directly via [`Session::get`](struct.Session.html#method.get "method zenoh::Session::get") operations.
More details are available in the [query](query/index.html "mod zenoh::query") API.

`Queryable`
`Querier`
`Session::get`

### [§](#key-expressions)Key Expressions

Data is associated with keys in the form of a slash-separated path, e.g., `robot/sensor/temp`.
The requesting side uses [key expressions](key_expr/index.html "mod zenoh::key_expr") to address the data of interest. Key expressions can
contain wildcards, e.g., `robot/sensor/*` or `robot/**`.

`robot/sensor/temp`
`robot/sensor/*`
`robot/**`

### [§](#data-representation)Data representation

Data is received as [sample](sample/index.html "mod zenoh::sample")s, which contain the payload and all metadata associated with the data.
The raw byte payload object [`ZBytes`](bytes/index.html "mod zenoh::bytes"), which provides mechanisms for zero-copy creation and access,
is available in the [bytes](bytes/index.html "mod zenoh::bytes") module.
The [zenoh\_ext](https://docs.rs/zenoh-ext/latest/zenoh_ext) crate also provides serialization and deserialization
of basic types and structures for `ZBytes`.

`ZBytes`
`ZBytes`

### [§](#other-components)Other components

Other important functionality of Zenoh includes:

### [§](#builders)Builders

Zenoh extensively uses the builder pattern. For example, to create a publisher, you first create a
[`PublisherBuilder`](pubsub/struct.PublisherBuilder.html "struct zenoh::pubsub::PublisherBuilder")
using the [`declare_publisher`](struct.Session.html#method.declare_publisher "method zenoh::Session::declare_publisher") method. The builder is
resolved to the [`Publisher`](pubsub/struct.Publisher.html "struct zenoh::pubsub::Publisher") instance by awaiting it in an async context
or by calling the [`wait`](trait.Wait.html#tymethod.wait "method zenoh::Wait::wait") method in a synchronous context.

`PublisherBuilder`
`declare_publisher`
`Publisher`
`wait`

### [§](#channels-and-callbacks)Channels and callbacks

There are two ways to get sequential data from Zenoh primitives (e.g., a series of
[`Sample`](sample/struct.Sample.html "struct zenoh::sample::Sample")s from a [`Subscriber`](pubsub/struct.Subscriber.html "struct zenoh::pubsub::Subscriber")
or [`Reply`](query/struct.Reply.html "struct zenoh::query::Reply")s from a [`Query`](query/struct.Query.html "struct zenoh::query::Query")): by channel or by callback.

`Sample`
`Subscriber`
`Reply`
`Query`

In channel mode, methods like [`recv_async`](handlers/struct.FifoChannelHandler.html#method.recv_async "method zenoh::handlers::FifoChannelHandler::recv_async")
become available on the subscriber or query object (through Deref coercion to the corresponding channel
handler type). By default, the [`FifoChannel`](handlers/struct.FifoChannel.html "struct zenoh::handlers::FifoChannel") is used.

`recv_async`
`FifoChannel`

The builders provide methods [`with`](pubsub/struct.SubscriberBuilder.html#method.with "method zenoh::pubsub::SubscriberBuilder::with") to assign an arbitrary channel instead of
the default one, and [`callback`](pubsub/struct.SubscriberBuilder.html#method.callback "method zenoh::pubsub::SubscriberBuilder::callback") to assign a callback function.

`with`
`callback`

See more details in the [handlers](handlers/index.html "mod zenoh::handlers") module documentation.

## [§](#usage-examples)Usage examples

Below are basic examples of using Zenoh. More examples are available in the documentation for each module and in
[zenoh-examples](https://github.com/zenoh-io/zenoh/tree/main/examples).

### [§](#publishingsubscribing)Publishing/Subscribing

The example below shows how to publish and subscribe to data using Zenoh.

Publishing data:

`#[tokio::main]
async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("key/expression", "value").await.unwrap();
session.close().await.unwrap();
}`

Subscribing to data:

`use futures::prelude::*;
#[tokio::main]
async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session.declare_subscriber("key/expression").await.unwrap();
while let Ok(sample) = subscriber.recv_async().await {
println!("Received: {:?}", sample);
};
}`

### [§](#queryreply-1)Query/Reply

Declare a queryable:

`#[tokio::main]
async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let queryable = session.declare_queryable("key/expression").await.unwrap();
while let Ok(query) = queryable.recv_async().await {
let reply = query.reply("key/expression", "value").await.unwrap();
}
}`

Request data:

`use futures::prelude::*;
#[tokio::main]
async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let replies = session.get("key/expression").await.unwrap();
while let Ok(reply) = replies.recv_async().await {
println!(">> Received {:?}", reply.result());
}
}`

## [§](#features)Features

The following features are exposed by the crate:

`auth_pubkey`, `auth_usrpwd`

`auth_pubkey`
`auth_usrpwd`

Enable authentication support, credentials are configurable in the [`Config`](struct.Config.html "struct zenoh::Config")

`Config`

`internal`

`internal`

Enable some internal APIs, usually necessary to expose some internal functionalities to other language bindings. These APIs are not supposed
to be called by users as they are close to implementation and can be changed at any moment

`plugins`

`plugins`

Enable the APIs related to plugin support in `zenohd`. These APIs are `internal` and `unstable` for now

`zenohd`
`internal`
`unstable`

`runtime_plugins`

`runtime_plugins`

Enable the dynamic plugins loading. Includes `plugins`. May be removed in future and combined with `plugins`

`plugins`
`plugins`

`shared-memory`

`shared-memory`

Enable shared-memory transport support and specific shared-memory related APIs

`stats`

`stats`

Enable collection of statistical data. This data becomes available in “adminspace” (by key `@/<zenoh_id>/router/metrics`)

`@/<zenoh_id>/router/metrics`

`tracing-instrument`

`tracing-instrument`

Developer feature - enable tracing of asynchronous tasks for debugging

`transport-compression`

`transport-compression`

Enable data-compression on the fly. If this feature is enabled, compression can be turned on or off in [`Config`](struct.Config.html "struct zenoh::Config")

`Config`

`transport_multilink`

`transport_multilink`

Enable multiple link connection for unicast transports. Maximum number of connections is configurable in [`Config`](struct.Config.html "struct zenoh::Config")

`Config`

`transport_quic`, `transport_quic_datagram`, `transport_serial`, `transport_tcp`, `transport_tls`,
`transport_udp`, `transport_unixpipe`, `transport_unixsock-stream`, `transport_vsock`, `transport_ws`

`transport_quic`
`transport_quic_datagram`
`transport_serial`
`transport_tcp`
`transport_tls`
`transport_udp`
`transport_unixpipe`
`transport_unixsock-stream`
`transport_vsock`
`transport_ws`

Enable specific transports

`unstable`

`unstable`

Enable the unstable APIs which may change or disappear in future releases. The difference with `internal`
is that the `unstable` API may be stabilized, while `internal` is unstable by nature, because it reveals implementation details.

`internal`
`unstable`
`internal`

The features enabled by default are:

`auth_pubkey`, `auth_usrpwd`, `transport_compression`, `transport_multilink`,
`transport_quic`, `transport_quic_datagram`, `transport_tcp`, `transport_tls`, `transport_udp`,
`transport_unixsock-stream`, `transport_ws`.

`auth_pubkey`
`auth_usrpwd`
`transport_compression`
`transport_multilink`
`transport_quic`
`transport_quic_datagram`
`transport_tcp`
`transport_tls`
`transport_udp`
`transport_unixsock-stream`
`transport_ws`

## Modules[§](#modules)

`unstable`
`open`
`scout`
`Session`
`unstable`

## Structs[§](#structs)

`Session`

## Constants[§](#constants)

## Traits[§](#traits)

## Functions[§](#functions)

`Session`

## Type Aliases[§](#types)

---

