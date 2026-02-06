# Concepts · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/migration_1.0/concepts

# Source: https://zenoh.io/docs/migration_1.0/concepts

# Concepts
The Zenoh team have been hard at work preparing an official version 1.0.0 of Zenoh!This major release comes with several API changes, quality of life improvements and developer conveniences.
We now have a more stable API and intend to keep backward compatibility in future Zenoh revisions.This guide is here to ease the transition to Zenoh 1.0.0 for our users!

## Value is gone, long live ZBytes
We have replacedValuewithZBytesandEncoding.ZBytesis the type core to data representation in Zenoh, all API’s have been reworked to acceptZBytesor something that can be converted into aZBytes.We have added a number of conversion implementations for language primitives as well as methods to seamlessly allow user defined structs to be serialized intoZBytes.Sample’s payloads are nowZBytes.Publisher,QueryableandSubscribernow expectZBytesfor all their interfaces. TheAttachmentAPI also now acceptsZBytes.
Each Language bindings will have their own specifics of Serializing and Deserializing, but for the most part it will involve implementing a serialize / deserialize function for your datatype or make use of auto-generated conversions for composite types.

## Encoding
Encodinghas been reworked, moving away from enumerables to now accepting strings.
While Zenoh does not impose anyEncodingrequirement on the user, providing anEncodingcan offer automatic wire-level optimization for known types.For the user definedEncoding, it can be thought of as optional metadata, carried over by Zenoh in such a way that the end user’s application may perform different operations based onEncoding.We have expanded our list of predefined encoding types from Zenoh 0.11.0 to include variants for numerous IANA standard encodings, including but not limited tovideo/x,application/x,text/x,image/xandaudio/xencoding families, as well as an encoding family specific to Zenoh defined by the prefixzenoh/x.Users can also define their own encoding scheme that does not need to be based on the predefined IANA variants. Upon declaring a specific encoding, the users encoding scheme will be prefixed withzenoh/bytesfor distinction.

## Attachment
We have made attachment more flexible across API’s, essentially accepting anything that can be converted to aZBytesas an optional extra toput,delete, onQuery’s and Queryreply’s.We also allow for composite types to be converted intoZBytes, meaning that using the Attachment API as a metadata transport is easier than ever.

## Query & Queryable
Thereplymethod of aQueryablehas gained two variants:reply_delandreply_errto respectively indicate that a deletion should be performed and that an error occurred.Additionally, the 3 variants behave similarly toputanddel, hence providing improved ergonomics.
We have added the ability to get the underlyingHandlerof a Queryable as well.

## Use accessors to get private members
Across language bindings we encapsulate members of structs, and they can’t be accessed directly now.The only way to access struct values is to use the getter function associated with them.

## Pull Subscribers have been removed
The concept of a pull subscriber no longer exists in Zenoh.
However, when creating aSubscriber, it may be the case that developers only care about the latest data and want to discard the oldest data.
TheRingChannelcan be used to get a similar behaviour.Rust ExampleThis contrasts with theFIFOChannel, the default channel type used internally in Subscribers, which drops new messages once its buffer is full.
You can take a look at examples of usage in any language’s examples/z_pull.x

## Timestamps
Previously we exposed a function to generate timestamps outside of a session.
Due to our efforts to improve the storage replication logic, users will now have to generate timestamps from a session, with the timestamp inheriting theZenohIDof the session.
This will affect user-created plugins and applications that need to generate timestamps in their Storage and sending of data.⚠️ Note: Timestamps are important for Storage Alignment (a.k.a. Replication). Data stored in Data bases must include a Timestamp to be properly aligned across Data Stores by Zenoh.
Thetimestampingconfiguration option must also be enabled for this.

## Plugins

### Storages
⚠️ Note: The storage-manager will fail to launch if thetimestampingconfiguration option is disabled.From Zenoh 1.0.0 user-applications can load plugins.A, somehow, implicit assumption that dictated the behaviour of storages is that the Zenoh node loading themhas to add a timestamp to any received publication that did not have one. This functionality is controlled by thetimestampingconfiguration option.Until Zenoh 1.0.0 this assumption held true as only a router could load storage and the default configuration for a router enablestimestamping. However, in Zenoh 1.0.0 nodes configured inclient&peermode can load storage andtheir default configuration disablestimestamping.

### Plugin Loading
We added the ability for user-applications to load compiled plugins written in Rust, regardless of which language bindings you are using!
Usage of this feature isPlugin Loading
⚠️ Note : When loading a plugin, the Plugin must have been built with the same version of the Rust compiler as the bindings loading it, and theCargo.lockof the plugin must be synced with the same commit of Zenoh.This means that if the language bindings are usingrustcversion1.75, the plugin must:
- Be built with the same toolchain version1.75
- Be built with the same Zenoh Commit
- The pluginCargo.lockhave had its packages synced with the ZenohCargo.lock
The reason behind this strict set of requirements is due to Rust making no guarantees regarding data layout in memory.This means between compiler versions, the representation may change based on optimizations.More on this topic at here :Rust:Type-Layout

## Config Changes

### Plugin Loading
Loading plugins is achieved by enabling theplugins_loadingsection in config file, with the membersenabledset to true, and specifying thesearch_dirsfor the plugins.
Directories are specified as an object with fieldskindandvalue.
- Ifkindiscurrent_exe_parent, then the parent of the current executable’s directory is searched andvalueshould benull.
In Bash notation,{ "kind": "current_exe_parent" }equals$(dirname $(which zenohd))while"."equals$PWD.
- Ifkindis"path", thenvalueis interpreted as a filesystem path, i.e.{ "kind": "path" , "value": "path/to/plugin/dir"}.Simply supplying a string instead of an object is equivalent to this.Ifenabled: trueandsearch_dirsis not specified thensearch_dirsfalls back to the default value of:".:~/.zenoh/lib:/opt/homebrew/lib:/usr/local/lib:/usr/lib”
```
 plugins_loading: {
    // Enable plugins loading.
    enabled: false,
    /// Directories where plugins configured by name should be looked for. Plugins configured by __path__ are not subject to lookup.
    /// If `enabled: true` and `search_dirs` is not specified then `search_dirs` falls back to the default value: ".:~/.zenoh/lib:/opt/homebrew/lib:/usr/local/lib:/usr/lib"
    search_dirs: [{ "kind": "current_exe_parent" }, ".", "~/.zenoh/lib", "/opt/homebrew/lib", "/usr/local/lib", "/usr/lib"],
}
// ... Rest of Config 
```

### Mode Dependent endpoints
Configuration now supports a different list of endpoints depending on the mode zenohd is launched with.
The old behaviour of a single List of endpoints is still supported, applying torouter,peerandclient, however users can now set endpoints per mode:
```
  connect: {
    /// The list of endpoints to connect to.
    /// Accepts a single list (e.g. endpoints: ["tcp/10.10.10.10:7447", "tcp/11.11.11.11:7447"])
    /// or different lists for router, peer and client 
    endpoints: { router: ["tcp/10.10.10.10:7447"], peer: ["tcp/11.11.11.11:7447"], client: ["tcp/somewhere1::7447", "udp/somewhere2:7447"]  }
},
```

⚠️ Note: inclientmode,zenohdwill try connect to each endpoint in order until one is successful, then stop subsequent endpoint connection attempts.client’s only connect to a single endpoint.

### Scouting
We have implemented a small change in the configuration syntax concerning thescoutingsection.Bothgossipandmulticast’sautoconnectsection’s have changed to accept lists of either"peer","client"or"router"
```
// Zenoh 0.11.0
scouting: {
  multicast: {
    autoconnect: { router: "", peer: "router|peer" },
  },
  gossip: {
    autoconnect: { router: "", peer: "router|peer" },
  },
},

// Zenoh 1.0.0
scouting: {
    multicast: {
      autoconnect: { router: [], peer: ["router", "peer"] },
    },
    gossip: {
      autoconnect: { router: [], peer: ["router", "peer"] },
    },
}
```

Next step is to dive into the migration examples for your favourite language!
