# Zenoh Examples: zenoh

# Example: examples--build.rs

```rs
use std::{env, fs::File, io::Write, path::Path};

use which::which;

fn main() -> std::io::Result<()> {
    // If protoc is not installed, we cheat because building protoc from source
    // with protobuf-src is way too long
    if which("protoc").is_err() {
        const PROTO: &str = r#"#[derive(Clone, PartialEq, ::prost::Message)] pub struct Entity { #[prost(uint32, tag = "1")] pub id: u32, #[prost(string, tag = "2")] pub name: ::prost::alloc::string::String,}"#;
        let out_path = Path::new(&env::var("OUT_DIR").unwrap()).join("example.rs");
        File::create(out_path)?.write_all(PROTO.as_bytes())?;
        return Ok(());
    }
    prost_build::compile_protos(&["examples/example.proto"], &["examples/"])?;
    Ok(())
}
```

---

# examples--Cargo.toml

```toml
#
# Copyright (c) 2023 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
[package]
authors = { workspace = true }
categories = { workspace = true }
description = "Internal crate for zenoh."
edition = { workspace = true }
homepage = { workspace = true }
license = { workspace = true }
name = "zenoh-examples"
readme = "README.md"
repository = { workspace = true }
rust-version = { workspace = true }
version = { workspace = true }
# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
publish = false

[features]
default = ["zenoh-ext/default", "zenoh/default"]
shared-memory = ["zenoh/shared-memory"]
unstable = ["zenoh/unstable"]

[dependencies]
clap = { workspace = true, features = ["derive"] }
futures = { workspace = true }
prost = { workspace = true }
serde_json = { workspace = true }
tokio = { workspace = true, features = ["io-std", "rt-multi-thread", "time"] }
zenoh = { workspace = true, default-features = false }
zenoh-ext = { workspace = true, default-features = false, features = [
  "unstable",
] }

[dev-dependencies]
rand = { workspace = true, features = ["default"] }

[build-dependencies]
prost-build = "0.13"
which = "7.0.2"

[[example]]
name = "z_scout"
path = "examples/z_scout.rs"

[[example]]
name = "z_info"
path = "examples/z_info.rs"

[[example]]
name = "z_put"
path = "examples/z_put.rs"

[[example]]
name = "z_put_float"
path = "examples/z_put_float.rs"

[[example]]
name = "z_delete"
path = "examples/z_delete.rs"

[[example]]
name = "z_formats"
path = "examples/z_formats.rs"

[[example]]
name = "z_pub"
path = "examples/z_pub.rs"

[[example]]
name = "z_pub_shm"
path = "examples/z_pub_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_sub"
path = "examples/z_sub.rs"

[[example]]
name = "z_sub_shm"
path = "examples/z_sub_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_pull"
path = "examples/z_pull.rs"

[[example]]
name = "z_querier"
path = "examples/z_querier.rs"

[[example]]
name = "z_queryable"
path = "examples/z_queryable.rs"

[[example]]
name = "z_queryable_shm"
path = "examples/z_queryable_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_storage"
path = "examples/z_storage.rs"

[[example]]
name = "z_get"
path = "examples/z_get.rs"

[[example]]
name = "z_get_shm"
path = "examples/z_get_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_forward"
path = "examples/z_forward.rs"

[[example]]
name = "z_liveliness"
path = "examples/z_liveliness.rs"

[[example]]
name = "z_sub_liveliness"
path = "examples/z_sub_liveliness.rs"

[[example]]
name = "z_get_liveliness"
path = "examples/z_get_liveliness.rs"

[[example]]
name = "z_pub_thr"
path = "examples/z_pub_thr.rs"

[[example]]
name = "z_sub_thr"
path = "examples/z_sub_thr.rs"

[[example]]
name = "z_pub_shm_thr"
path = "examples/z_pub_shm_thr.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_ping"
path = "examples/z_ping.rs"

[[example]]
name = "z_ping_shm"
path = "examples/z_ping_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_pong"
path = "examples/z_pong.rs"

[[example]]
name = "z_alloc_shm"
path = "examples/z_alloc_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_bytes_shm"
path = "examples/z_bytes_shm.rs"
required-features = ["shared-memory", "unstable"]

[[example]]
name = "z_posix_shm_provider"
path = "examples/z_posix_shm_provider.rs"
required-features = ["shared-memory", "unstable"]
```

---

# Example: examples--examples--z_alloc_shm.rs

```rs
use std::mem::MaybeUninit;
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::sync::atomic::AtomicUsize;

use zenoh::{
    shm::{
        AllocAlignment, BlockOn, ConstBool, ConstUsize, Deallocate, Defragment, GarbageCollect,
        JustAlloc, MemoryLayout, PosixShmProviderBackend, ResideInShm, ShmProviderBuilder, Typed,
        TypedLayout, ZShmMut,
    },
    Config, Wait,
};

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");
    run().await.unwrap();
}

async fn run() -> zenoh::Result<()> {
    // Create an SHM provider
    let provider = {
        // Option 1: simple way to create default ShmProvider initialized with default-configured
        {
            // SHM backend (PosixShmProviderBackend)
            let _simple =
                ShmProviderBuilder::default_backend(MemoryLayout::try_from(42).unwrap()).wait()?;
        }

        // Option 2: comprehensive ShmProvider creation
        {
            // Create specific backed
            // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
            let comprehensive =
                PosixShmProviderBackend::builder((65536, AllocAlignment::ALIGN_8_BYTES)).wait()?;

            // ...and an SHM provider with specified backend
            ShmProviderBuilder::backend(comprehensive).wait()
        }
    };

    // Allocate SHM buffer

    // There are two ways of making shm buffer allocations: direct and through the layout...

    // Option 1: direct allocation
    // The direct allocation calculates all layouting checks on each allocation. It is good for making
    // uniquely-layouted allocations.
    {
        // Option 1: Simple allocation
        let _shm_buf = provider.alloc(512).wait()?;

        // Option 2: Allocation with custom alignment
        let _shm_buf = provider
            .alloc((512, AllocAlignment::ALIGN_2_BYTES))
            .wait()?;
    };

    // Option 2: allocation layout
    // Layout is reusable and is designed to handle series of similar allocations
    {
        // Option 1: Simple configuration:
        let simple_layout = provider.alloc_layout(512)?;
        let _shm_buf = simple_layout.alloc().wait()?;

        // Option 2: Comprehensive configuration:
        let comprehensive_layout = provider.alloc_layout((512, AllocAlignment::ALIGN_2_BYTES))?;
        let _shm_buf = comprehensive_layout.alloc().wait()?;
    };

    // Typed allocation
    {
        // Shared data
        #[repr(C)]
        pub struct SharedData {
            pub len: AtomicUsize,
            pub data: [u8; 1024],
        }

        // #SAFETY: this is safe because SharedData is safe to be shared
        unsafe impl ResideInShm for SharedData {}

        // typed layout

        // allocate typed SHM buffer; the allocated type is wrapped into `MaybeUninit`
        let typed_buf: Typed<MaybeUninit<SharedData>, ZShmMut> = provider
            .alloc(TypedLayout::<SharedData>::new())
            .wait()
            .unwrap();
        // the underlying buffer can be extracted
        let _buf: ZShmMut = Typed::into_inner(typed_buf);
    }

    // Allocation policies
    // Policy is a generics-based API to describe necessary allocation behaviour to be optimized at compile-time.
    // Policy can be sync and async.
    // The basic policies are:
    // -JustAlloc (sync)
    // -GarbageCollect (sync)
    // -Deallocate (sync)
    // --contains own set of dealloc policy generics:
    // ---DeallocateYoungest
    // ---DeallocateEldest
    // ---DeallocateOptimal
    // -BlockOn (sync and async)
    let mut sbuf = {
        // Option: The default allocation with default JustAlloc policy
        let default_alloc = provider.alloc(512).wait()?;

        // Option: Defragment and garbage collect if there is not enough shared memory for allocation
        let _gc_defragment_alloc = provider
            .alloc(512)
            .with_policy::<Defragment<GarbageCollect>>()
            .wait()?;

        // Option: Sync block if there is not enough shared memory for allocation
        let _sync_alloc = provider.alloc(512).with_policy::<BlockOn>().wait()?;

        // Option: Async block if there is not enough shared memory for allocation
        let _async_alloc = provider.alloc(512).with_policy::<BlockOn>().await?;

        // Option: The comprehensive allocation policy that tries to GC, defragment and then blocks
        // if provider is not able to allocate
        let _comprehensive_alloc = provider
            .alloc(512)
            .with_policy::<BlockOn<Defragment<GarbageCollect>>>()
            .await?;

        // Option: The comprehensive allocation policy that tries to GC, defragment and then deallocates up to
        // 10 buffers if provider is not able to allocate
        let _comprehensive_alloc = unsafe {
            provider.alloc(512).with_unsafe_policy::<Deallocate<
                ConstUsize<10>,
                Defragment<GarbageCollect<JustAlloc, JustAlloc, ConstBool<false>>>,
            >>()
        }
        .wait()?;

        default_alloc
    };

    // Fill recently-allocated buffer with data
    sbuf[0..8].fill(0);

    // Declare Session and Publisher (common code)
    let session = zenoh::open(Config::default()).await?;
    let publisher = session.declare_publisher("my/key/expr").await?;

    // Publish SHM buffer
    publisher.put(sbuf).await
}
```

---

# Example: examples--examples--z_bytes_shm.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use zenoh::{
    bytes::ZBytes,
    shm::{zshmmut, ShmProviderBuilder, ZShm, ZShmMut},
    Wait,
};

fn main() {
    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(4096).wait().unwrap();

    // Allocate an SHM buffer
    // NOTE: For allocation API please check z_alloc_shm.rs example
    let mut owned_shm_buf_mut = provider.alloc(1024).wait().unwrap();

    // mutable and immutable API
    let _data: &[u8] = &owned_shm_buf_mut;
    let _data_mut: &mut [u8] = &mut owned_shm_buf_mut;

    // convert into immutable owned buffer (ZShmMut -> ZShm)
    let owned_shm_buf: ZShm = owned_shm_buf_mut.into();

    // immutable API
    let _data: &[u8] = &owned_shm_buf;

    // convert again into mutable owned buffer (ZShm -> ZShmMut)
    let mut owned_shm_buf_mut: ZShmMut = owned_shm_buf.try_into().unwrap();

    // mutable and immutable API
    let _data: &[u8] = &owned_shm_buf_mut;
    let _data_mut: &mut [u8] = &mut owned_shm_buf_mut;

    // build a ZBytes from an SHM buffer (ZShmMut -> ZBytes)
    let mut payload: ZBytes = owned_shm_buf_mut.into();

    // branch to illustrate immutable access to SHM data
    {
        // deserialize ZBytes as an immutably borrowed zshm (ZBytes -> &zshm)
        let borrowed_shm_buf = payload.as_shm().unwrap();

        // immutable API
        let _data: &[u8] = borrowed_shm_buf;

        // construct owned buffer from borrowed type (&zshm -> ZShm)
        let owned = borrowed_shm_buf.to_owned();

        // immutable API
        let _data: &[u8] = &owned;

        // try to construct mutable ZShmMut (ZShm -> ZShmMut)
        let owned_mut: Result<ZShmMut, _> = owned.try_into();
        // the attempt fails because ZShm has two existing references ('owned' and inside 'payload')
        assert!(owned_mut.is_err())
    }

    // branch to illustrate mutable access to SHM data
    {
        // deserialize ZBytes as mutably borrowed zshm (ZBytes -> &mut zshm)
        let borrowed_shm_buf = payload.as_shm_mut().unwrap();

        // immutable API
        let _data: &[u8] = borrowed_shm_buf;

        // convert zshm to zshmmut (&mut zshm -> &mut zshmmut)
        let borrowed_shm_buf_mut: &mut zshmmut = borrowed_shm_buf.try_into().unwrap();

        // mutable and immutable API
        let _data: &[u8] = borrowed_shm_buf_mut;
        let _data_mut: &mut [u8] = borrowed_shm_buf_mut;
    }
}
```

---

# Example: examples--examples--z_bytes.rs

```rs
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::collections::HashMap;

use zenoh::bytes::ZBytes;

fn main() {
    // Raw bytes
    let input = b"raw bytes".as_slice();
    // raw bytes are copied into ZBytes, or moved in case of Vec<u8>
    let payload_copy = ZBytes::from(input);
    let payload_move = ZBytes::from(input.to_vec());
    assert_eq!(payload_copy, payload_move);
    // retrieving raw bytes from ZBytes is infallible
    let output = payload_move.to_bytes();
    assert_eq!(input, &*output);
    // Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    // let encoding = Encoding::ZENOH_BYTES;

    // Raw utf8 bytes, i.e. string
    let input = "raw bytes";
    // string is copied into ZBytes, or moved in case of String
    let payload_copy = ZBytes::from(input);
    let payload_move = ZBytes::from(input.to_string());
    assert_eq!(payload_copy, payload_move);
    // retrieving utf8 string from ZBytes can fail if the bytes are not utf8
    let output = payload_move.try_to_string().unwrap();
    assert_eq!(input, output);
    // Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    // let encoding = Encoding::ZENOH_STRING;

    // JSON
    let input = serde_json::json!({
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    });
    let payload = ZBytes::from(serde_json::to_vec(&input).unwrap());
    let output: serde_json::Value = serde_json::from_slice(&payload.to_bytes()).unwrap();
    assert_eq!(input, output);
    // Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    // let encoding = Encoding::APPLICATION_JSON;

    // Protobuf (see example.proto)
    mod example {
        include!(concat!(env!("OUT_DIR"), "/example.rs"));
    }
    use prost::Message;
    let input = example::Entity {
        id: 1234,
        name: String::from("John Doe"),
    };
    let payload = ZBytes::from(input.encode_to_vec());
    let output = example::Entity::decode(&*payload.to_bytes()).unwrap();
    assert_eq!(input, output);
    // Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    // let encoding = Encoding::APPLICATION_PROTOBUF;

    // zenoh-ext serialization
    {
        use zenoh_ext::{z_deserialize, z_serialize};

        // Numeric types: u8, u16, u32, u128, i8, i16, i32, i128, f32, f64
        let input = 1234_u32;
        let payload = z_serialize(&input);
        let output: u32 = z_deserialize(&payload).unwrap();
        assert_eq!(input, output);

        // Vec
        let input = vec![0.0f32, 1.5, 42.0];
        let payload = z_serialize(&input);
        let output: Vec<f32> = z_deserialize(&payload).unwrap();
        assert_eq!(input, output);

        // HashMap
        let mut input: HashMap<u32, String> = HashMap::new();
        input.insert(0, String::from("abc"));
        input.insert(1, String::from("def"));
        let payload = z_serialize(&input);
        let output: HashMap<u32, String> = z_deserialize(&payload).unwrap();
        assert_eq!(input, output);

        // Tuple
        let input = (0.42f64, "string".to_string());
        let payload = z_serialize(&input);
        let output: (f64, String) = z_deserialize(&payload).unwrap();
        assert_eq!(input, output);

        // Array (handled as variable-length sequence, not as tuple)
        let input = [0.0f32, 1.5, 42.0];
        let payload = z_serialize(&input);
        let output: [f32; 3] = z_deserialize(&payload).unwrap();
        assert_eq!(input, output);
        // can also be deserialized as a vec
        let output: Vec<f32> = z_deserialize(&payload).unwrap();
        assert_eq!(input.as_slice(), output);

        // Look at Serialize/Deserialize documentation for the exhaustive
        // list of provided implementations
    }

    // Writer/reader
    use std::io::{Read, Write};
    let input1 = &[0u8, 1];
    let input2 = ZBytes::from([2, 3]);
    let mut writer = ZBytes::writer();
    writer.write_all(&[0u8, 1]).unwrap();
    writer.append(input2.clone());
    let zbytes = writer.finish();
    assert_eq!(*zbytes.to_bytes(), [0u8, 1, 2, 3]);
    let mut reader = zbytes.reader();
    let mut buf = [0; 2];
    reader.read_exact(&mut buf).unwrap();
    assert_eq!(buf, *input1);
    reader.read_exact(&mut buf).unwrap();
    assert_eq!(buf, *input2.to_bytes());
}
```

---

# Example: examples--examples--z_delete.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Deleting resources matching '{key_expr}'...");
    session.delete(&key_expr).await.unwrap();

    session.close().await.unwrap();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-put")]
    /// The key expression to write to.
    key: KeyExpr<'static>,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>) {
    let args = Args::parse();
    (args.common.into(), args.key)
}
```

---

# Example: examples--examples--z_formats.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

use zenoh::key_expr::{
    format::{kedefine, keformat},
    keyexpr,
};
kedefine!(
    pub file_format: "user_id/${user_id:*}/file/${file:*/**}",
    pub(crate) settings_format: "user_id/${user_id:*}/settings/${setting:**}"
);

fn main() {
    // Formatting
    let mut formatter = file_format::formatter();
    let file = "hi/there";
    let ke = keformat!(formatter, user_id = 42, file).unwrap();
    println!("{formatter:?} => {ke}");
    // Parsing
    let settings_ke = keyexpr::new("user_id/30/settings/dark_mode").unwrap();
    let parsed = settings_format::parse(settings_ke).unwrap();
    assert_eq!(parsed.user_id(), keyexpr::new("30").unwrap());
    assert_eq!(parsed.setting(), keyexpr::new("dark_mode").ok());
}
```

---

# Example: examples--examples--z_forward.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;
use zenoh_ext::SubscriberForward;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, forward) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Subscriber on '{key_expr}'...");
    let mut subscriber = session.declare_subscriber(&key_expr).await.unwrap();
    println!("Declaring Publisher on '{forward}'...");
    let publisher = session.declare_publisher(&forward).await.unwrap();
    println!("Forwarding data from '{key_expr}' to '{forward}'...");
    subscriber.forward(publisher).await.unwrap();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The key expression to subscribe to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "demo/forward")]
    /// The key expression to forward to.
    forward: KeyExpr<'static>,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, KeyExpr<'static>) {
    let args = Args::parse();
    (args.common.into(), args.key, args.forward)
}
```

---

# Example: examples--examples--z_get_liveliness.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, timeout) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Sending Liveliness Query '{key_expr}'...");
    let replies = session
        .liveliness()
        .get(&key_expr)
        .timeout(timeout)
        .await
        .unwrap();
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => println!(">> Alive token ('{}')", sample.key_expr().as_str(),),
            Err(err) => {
                let payload = err
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(">> Received (ERROR: '{payload}')");
            }
        }
    }
}

#[derive(Parser, Clone, Debug)]
struct Args {
    #[arg(short, long, default_value = "group1/**")]
    /// The key expression matching liveliness tokens to query.
    key_expr: KeyExpr<'static>,
    #[arg(short = 'o', long, default_value = "10000")]
    /// The query timeout in milliseconds.
    timeout: u64,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, Duration) {
    let args = Args::parse();
    let timeout = Duration::from_millis(args.timeout);
    (args.common.into(), args.key_expr, timeout)
}
```

---

# Example: examples--examples--z_get_shm.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{
    query::{QueryTarget, Selector},
    shm::{BlockOn, GarbageCollect, ShmProviderBuilder},
    Config, Wait,
};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, selector, mut payload, target, timeout) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Creating POSIX SHM provider...");
    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(1024 * 1024)
        .wait()
        .unwrap();

    // Allocate an SHM buffer
    // NOTE: For allocation API please check z_alloc_shm.rs example
    // NOTE: For buf's API please check z_bytes_shm.rs example
    println!("Allocating Shared Memory Buffer...");
    let mut sbuf = provider
        .alloc(1024)
        .with_policy::<BlockOn<GarbageCollect>>()
        .await
        .unwrap();

    let content = payload
        .take()
        .unwrap_or_else(|| "Get from Rust SHM!".to_string());
    sbuf[0..content.len()].copy_from_slice(content.as_bytes());

    println!("Sending Query '{selector}'...");
    let replies = session
        .get(&selector)
        .payload(sbuf)
        .target(target)
        .timeout(timeout)
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                print!(">> Received ('{}': ", sample.key_expr().as_str());
                match sample.payload().as_shm() {
                    Some(payload) => println!("'{}')", String::from_utf8_lossy(payload)),
                    None => println!("'Not a ShmBufInner')"),
                }
            }
            Err(err) => {
                let payload = err
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(">> Received (ERROR: '{payload}')");
            }
        }
    }
}

#[derive(clap::ValueEnum, Clone, Copy, Debug)]
#[value(rename_all = "SCREAMING_SNAKE_CASE")]
enum Qt {
    BestMatching,
    All,
    AllComplete,
}

#[derive(Parser, Clone, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The selection of resources to query
    selector: Selector<'static>,
    /// The payload to publish.
    payload: Option<String>,
    #[arg(short, long, default_value = "BEST_MATCHING")]
    /// The target queryables of the query.
    target: Qt,
    #[arg(short = 'o', long, default_value = "10000")]
    /// The query timeout in milliseconds.
    timeout: u64,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (
    Config,
    Selector<'static>,
    Option<String>,
    QueryTarget,
    Duration,
) {
    let args = Args::parse();
    (
        args.common.into(),
        args.selector,
        args.payload,
        match args.target {
            Qt::BestMatching => QueryTarget::BestMatching,
            Qt::All => QueryTarget::All,
            Qt::AllComplete => QueryTarget::AllComplete,
        },
        Duration::from_millis(args.timeout),
    )
}
```

---

# Example: examples--examples--z_get.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{
    query::{QueryTarget, Selector},
    Config,
};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, selector, payload, target, timeout) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Sending Query '{selector}'...");
    let mut builder = session
        .get(&selector)
        // // By default get receives replies from a FIFO.
        // // Uncomment this line to use a ring channel instead.
        // // More information on the ring channel are available in the z_pull example.
        // .with(zenoh::handlers::RingChannel::default())
        // Refer to z_bytes.rs to see how to serialize different types of message
        .target(target)
        .timeout(timeout);
    if let Some(payload) = payload {
        builder = builder.payload(payload);
    }
    let replies = builder.await.unwrap();
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                // Refer to z_bytes.rs to see how to deserialize different types of message
                let payload = sample
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(
                    ">> Received ('{}': '{}')",
                    sample.key_expr().as_str(),
                    payload,
                );
            }
            Err(err) => {
                let payload = err
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(">> Received (ERROR: '{payload}')");
            }
        }
    }
}

#[derive(clap::ValueEnum, Clone, Copy, Debug)]
#[value(rename_all = "SCREAMING_SNAKE_CASE")]
enum Qt {
    BestMatching,
    All,
    AllComplete,
}

#[derive(Parser, Clone, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The selection of resources to query
    selector: Selector<'static>,
    #[arg(short, long)]
    /// An optional payload to put in the query.
    payload: Option<String>,
    #[arg(short, long, default_value = "BEST_MATCHING")]
    /// The target queryables of the query.
    target: Qt,
    #[arg(short = 'o', long, default_value = "10000")]
    /// The query timeout in milliseconds.
    timeout: u64,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (
    Config,
    Selector<'static>,
    Option<String>,
    QueryTarget,
    Duration,
) {
    let args = Args::parse();
    (
        args.common.into(),
        args.selector,
        args.payload,
        match args.target {
            Qt::BestMatching => QueryTarget::BestMatching,
            Qt::All => QueryTarget::All,
            Qt::AllComplete => QueryTarget::AllComplete,
        },
        Duration::from_millis(args.timeout),
    )
}
```

---

# Example: examples--examples--z_info.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
#[cfg(feature = "unstable")]
use zenoh::sample::SampleKind;
use zenoh::session::ZenohId;
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let config = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    let info = session.info();
    println!("zid: {}", info.zid().await);
    println!(
        "routers zid: {:?}",
        info.routers_zid().await.collect::<Vec<ZenohId>>()
    );
    println!(
        "peers zid: {:?}",
        info.peers_zid().await.collect::<Vec<ZenohId>>()
    );

    // Display current transports
    #[cfg(feature = "unstable")]
    {
        println!("\ntransports:");
        let transports = info.transports().await;
        for transport in transports {
            println!("{:?}", transport);
        }

        // Display current links
        println!("\nlinks:");
        let links = info.links().await;
        for link in links {
            println!("{:?}", link);
        }

        println!("\nConnectivity events (Press CTRL-C to quit):");

        // Set up transport events listener (using default handler)
        let transport_events = info
            .transport_events_listener()
            .history(false) // Don't repeat transports we already printed
            .await
            .expect("Failed to declare transport events listener");

        // Set up link events listener (using default handler)
        let link_events = info
            .link_events_listener()
            .history(false) // Don't repeat links we already printed
            .await
            .expect("Failed to declare link events listener");

        // Listen for events until CTRL-C
        loop {
            tokio::select! {
                Ok(event) = transport_events.recv_async() => {
                    match event.kind() {
                        SampleKind::Put => {
                            println!("[Transport Event] Opened: {:?}", event.transport());
                        }
                        SampleKind::Delete => {
                            println!("[Transport Event] Closed: {:?}", event.transport());
                        }
                    }
                }
                Ok(event) = link_events.recv_async() => {
                    match event.kind() {
                        SampleKind::Put => {
                            println!("[Link Event] Added: {:?}", event.link());
                        }
                        SampleKind::Delete => {
                            println!("[Link Event] Removed: {:?}", event.link());
                        }
                    }
                }
            }
        }
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> zenoh::Config {
    let args = Args::parse();
    args.common.into()
}
```

---

# Example: examples--examples--z_liveliness.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring LivelinessToken on '{}'...", &key_expr);
    let token = session.liveliness().declare_token(&key_expr).await.unwrap();

    println!("Press CTRL-C to undeclare LivelinessToken and quit...");
    std::thread::park();

    // LivelinessTokens are automatically closed when dropped
    // Use the code below to manually undeclare it if needed
    token.undeclare().await.unwrap();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "group1/zenoh-rs")]
    /// The key expression of the liveliness token.
    key: KeyExpr<'static>,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>) {
    let args = Args::parse();
    (args.common.into(), args.key)
}
```

---

# Example: examples--examples--z_ping_shm.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::{Duration, Instant};

use clap::Parser;
use zenoh::{
    bytes::ZBytes, key_expr::keyexpr, qos::CongestionControl, shm::ShmProviderBuilder, Config, Wait,
};
use zenoh_examples::CommonArgs;

fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, warmup, size, n) = parse_args();

    let session = zenoh::open(config).wait().unwrap();

    // The key expression to publish data on
    let key_expr_ping = keyexpr::new("test/ping").unwrap();

    // The key expression to wait the response back
    let key_expr_pong = keyexpr::new("test/pong").unwrap();

    let sub = session.declare_subscriber(key_expr_pong).wait().unwrap();
    let publisher = session
        .declare_publisher(key_expr_ping)
        .congestion_control(CongestionControl::Block)
        .wait()
        .unwrap();

    let mut samples = Vec::with_capacity(n);

    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(size).wait().unwrap();

    // Allocate an SHM buffer
    // NOTE: For allocation API please check z_alloc_shm.rs example
    // NOTE: For buf's API please check z_bytes_shm.rs example
    let buf = provider.alloc(size).wait().unwrap();

    // convert ZShmMut into ZBytes as ZShmMut does not support Clone
    let buf: ZBytes = buf.into();

    // -- warmup --
    println!("Warming up for {warmup:?}...");
    let now = Instant::now();
    while now.elapsed() < warmup {
        publisher.put(buf.clone()).wait().unwrap();
        let _ = sub.recv().unwrap();
    }

    for _ in 0..n {
        let buf = buf.clone();
        let write_time = Instant::now();
        publisher.put(buf).wait().unwrap();

        let _ = sub.recv();
        let ts = write_time.elapsed().as_micros();
        samples.push(ts);
    }

    for (i, rtt) in samples.iter().enumerate().take(n) {
        println!(
            "{} bytes: seq={} rtt={:?}µs lat={:?}µs",
            size,
            i,
            rtt,
            rtt / 2
        );
    }
}

#[derive(Parser)]
struct Args {
    #[arg(short, long, default_value = "1")]
    /// The number of seconds to warm up (float)
    warmup: f64,
    #[arg(short = 'n', long, default_value = "100")]
    /// The number of round-trips to measure
    samples: usize,
    /// Sets the size of the payload to publish
    payload_size: usize,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, Duration, usize, usize) {
    let args = Args::parse();
    (
        args.common.into(),
        Duration::from_secs_f64(args.warmup),
        args.payload_size,
        args.samples,
    )
}
```

---

# Example: examples--examples--z_ping.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::{Duration, Instant};

use clap::Parser;
use zenoh::{bytes::ZBytes, key_expr::keyexpr, qos::CongestionControl, Config, Wait};
use zenoh_examples::CommonArgs;

fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, warmup, size, n, express) = parse_args();
    let session = zenoh::open(config).wait().unwrap();

    // The key expression to publish data on
    let key_expr_ping = keyexpr::new("test/ping").unwrap();

    // The key expression to wait the response back
    let key_expr_pong = keyexpr::new("test/pong").unwrap();

    let sub = session.declare_subscriber(key_expr_pong).wait().unwrap();
    let publisher = session
        .declare_publisher(key_expr_ping)
        .congestion_control(CongestionControl::Block)
        .express(express)
        .wait()
        .unwrap();

    let data: ZBytes = (0usize..size)
        .map(|i| (i % 10) as u8)
        .collect::<Vec<u8>>()
        .into();

    let mut samples = Vec::with_capacity(n);

    // -- warmup --
    println!("Warming up for {warmup:?}...");
    let now = Instant::now();
    while now.elapsed() < warmup {
        let data = data.clone();
        publisher.put(data).wait().unwrap();

        let _ = sub.recv();
    }

    for _ in 0..n {
        let data = data.clone();
        let write_time = Instant::now();
        publisher.put(data).wait().unwrap();

        let _ = sub.recv();
        let ts = write_time.elapsed().as_micros();
        samples.push(ts);
    }

    for (i, rtt) in samples.iter().enumerate().take(n) {
        println!(
            "{} bytes: seq={} rtt={:?}µs lat={:?}µs",
            size,
            i,
            rtt,
            rtt / 2
        );
    }
}

#[derive(Parser)]
struct Args {
    /// express for sending data
    #[arg(long, default_value = "false")]
    no_express: bool,
    #[arg(short, long, default_value = "1")]
    /// The number of seconds to warm up (float)
    warmup: f64,
    #[arg(short = 'n', long, default_value = "100")]
    /// The number of round-trips to measure
    samples: usize,
    /// Sets the size of the payload to publish
    payload_size: usize,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, Duration, usize, usize, bool) {
    let args = Args::parse();
    (
        args.common.into(),
        Duration::from_secs_f64(args.warmup),
        args.payload_size,
        args.samples,
        !args.no_express,
    )
}
```

---

# Example: examples--examples--z_pong.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::keyexpr, qos::CongestionControl, Config, Wait};
use zenoh_examples::CommonArgs;

fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, express) = parse_args();

    let session = zenoh::open(config).wait().unwrap();

    // The key expression to read the data from
    let key_expr_ping = keyexpr::new("test/ping").unwrap();

    // The key expression to echo the data back
    let key_expr_pong = keyexpr::new("test/pong").unwrap();

    let publisher = session
        .declare_publisher(key_expr_pong)
        .congestion_control(CongestionControl::Block)
        .express(express)
        .wait()
        .unwrap();

    session
        .declare_subscriber(key_expr_ping)
        .callback(move |sample| publisher.put(sample.payload().clone()).wait().unwrap())
        .background()
        .wait()
        .unwrap();
    std::thread::park();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    /// express for sending data
    #[arg(long, default_value = "false")]
    no_express: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, bool) {
    let args = Args::parse();
    (args.common.into(), !args.no_express)
}
```

---

# Example: examples--examples--z_posix_shm_provider.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use zenoh::{
    shm::{AllocAlignment, MemoryLayout, PosixShmProviderBackend, ShmProviderBuilder},
    Wait,
};

fn main() {
    // Construct an SHM backend
    let backend = {
        // NOTE: code in this block is a specific PosixShmProviderBackend API.

        // Total amount of shared memory to allocate
        let size = 4096;

        // An alignment for POSIX SHM provider
        // Due to internal optimization, all allocations will be aligned corresponding to this alignment,
        // so the provider will be able to satisfy allocation layouts with alignment <= provider_alignment
        let provider_alignment = AllocAlignment::default();

        // A layout for POSIX Provider's memory
        let provider_layout = MemoryLayout::new(size, provider_alignment).unwrap();

        // Build a provider backend
        PosixShmProviderBackend::builder(&provider_layout)
            .wait()
            .unwrap()
    };

    // Construct an SHM provider for particular backend
    let _shm_provider = ShmProviderBuilder::backend(backend).wait();
}
```

---

# Example: examples--examples--z_pub_shm_thr.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{bytes::ZBytes, qos::CongestionControl, shm::ShmProviderBuilder, Config, Wait};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");
    let (config, sm_size, size) = parse_args();

    let z = zenoh::open(config).await.unwrap();

    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(sm_size).wait().unwrap();

    // Allocate an SHM buffer
    // NOTE: For allocation API please check z_alloc_shm.rs example
    // NOTE: For buf's API please check z_bytes_shm.rs example
    let mut buf = provider.alloc(size).wait().unwrap();

    for b in buf.as_mut() {
        *b = rand::random::<u8>();
    }

    let publisher = z
        .declare_publisher("test/thr")
        // Make sure to not drop messages because of congestion control
        .congestion_control(CongestionControl::Block)
        .await
        .unwrap();

    // convert ZShmMut into ZBytes as ZShmMut does not support Clone
    let buf: ZBytes = buf.into();

    println!("Press CTRL-C to quit...");
    loop {
        publisher.put(buf.clone()).await.unwrap();
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "32")]
    /// shared memory size in MBytes.
    shared_memory: usize,
    /// Sets the size of the payload to publish.
    payload_size: usize,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, usize, usize) {
    let args = Args::parse();
    let sm_size = args.shared_memory * 1024 * 1024;
    let size = args.payload_size;
    (args.common.into(), sm_size, size)
}
```

---

# Example: examples--examples--z_pub_shm.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{
    key_expr::KeyExpr,
    shm::{BlockOn, GarbageCollect, ShmProviderBuilder},
    Config, Wait,
};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, path, payload) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Creating POSIX SHM provider...");
    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(1024 * 1024)
        .wait()
        .unwrap();

    println!("Declaring Publisher on '{path}'...");
    let publisher = session.declare_publisher(&path).await.unwrap();

    println!("Press CTRL-C to quit...");
    for idx in 0..u32::MAX {
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;

        // We reserve a small space at the beginning of the buffer to include the iteration index
        // of the write. This is simply to have the same format as zn_pub.
        let prefix = format!("[{idx:4}] ");
        let prefix_len = prefix.len();
        let slice_len = prefix_len + payload.len();

        // Allocate SHM buffer
        let mut sbuf = provider
            .alloc(slice_len)
            .with_policy::<BlockOn<GarbageCollect>>()
            .await
            .unwrap();

        sbuf[0..prefix_len].copy_from_slice(prefix.as_bytes());
        sbuf[prefix_len..slice_len].copy_from_slice(payload.as_bytes());

        // Write the data
        println!(
            "Put SHM Data ('{}': '{}')",
            path,
            String::from_utf8_lossy(&sbuf[0..slice_len])
        );
        publisher.put(sbuf).await?;
    }

    Ok(())
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-pub")]
    /// The key expression to publish onto.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "Pub from Rust SHM!")]
    /// The payload of to publish.
    payload: String,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, String) {
    let args = Args::parse();
    (args.common.into(), args.key, args.payload)
}
```

---

# Example: examples--examples--z_pub_thr.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//

use std::convert::TryInto;

use clap::Parser;
use zenoh::{
    bytes::ZBytes,
    qos::{CongestionControl, Priority},
    Wait,
};
use zenoh_examples::CommonArgs;

fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");
    let args = Args::parse();

    let mut prio = Priority::DEFAULT;
    if let Some(p) = args.priority {
        prio = p.try_into().unwrap();
    }

    let payload_size = args.payload_size;

    let data: ZBytes = (0..payload_size)
        .map(|i| (i % 10) as u8)
        .collect::<Vec<u8>>()
        .into();

    let session = zenoh::open(args.common).wait().unwrap();

    let publisher = session
        .declare_publisher("test/thr")
        .congestion_control(CongestionControl::Block)
        .priority(prio)
        .express(args.express)
        .wait()
        .unwrap();

    println!("Press CTRL-C to quit...");
    let mut count: usize = 0;
    let mut start = std::time::Instant::now();
    loop {
        publisher.put(data.clone()).wait().unwrap();

        if args.print {
            if count < args.number {
                count += 1;
            } else {
                let thpt = count as f64 / start.elapsed().as_secs_f64();
                println!("{thpt} msg/s");
                count = 0;
                start = std::time::Instant::now();
            }
        }
    }
}

#[derive(Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    /// express for sending data
    #[arg(long, default_value = "false")]
    express: bool,
    /// Priority for sending data
    #[arg(short, long)]
    priority: Option<u8>,
    /// Print the statistics
    #[arg(short = 't', long)]
    print: bool,
    /// Number of messages in each throughput measurements
    #[arg(short, long, default_value = "100000")]
    number: usize,
    /// Sets the size of the payload to publish
    payload_size: usize,
    #[command(flatten)]
    common: CommonArgs,
}
```

---

# Example: examples--examples--z_pub.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{bytes::Encoding, key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, payload, attachment, add_matching_listener) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Publisher on '{key_expr}'...");
    let publisher = session.declare_publisher(&key_expr).await.unwrap();

    if add_matching_listener {
        publisher
            .matching_listener()
            .callback(|matching_status| {
                if matching_status.matching() {
                    println!("Publisher has matching subscribers.");
                } else {
                    println!("Publisher has NO MORE matching subscribers.");
                }
            })
            .background()
            .await
            .unwrap();
    }

    println!("Press CTRL-C to quit...");
    for idx in 0..u32::MAX {
        tokio::time::sleep(Duration::from_secs(1)).await;
        let buf = format!("[{idx:4}] {payload}");
        println!("Putting Data ('{}': '{}')...", &key_expr, buf);
        // Refer to z_bytes.rs to see how to serialize different types of message
        publisher
            .put(buf)
            .encoding(Encoding::TEXT_PLAIN) // Optionally set the encoding metadata 
            .attachment(attachment.clone()) // Optionally add an attachment
            .await
            .unwrap();
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-pub")]
    /// The key expression to write to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "Pub from Rust!")]
    /// The payload to write.
    payload: String,
    #[arg(short, long)]
    /// The attachments to add to each put.
    attach: Option<String>,
    /// Enable matching listener.
    #[arg(long)]
    add_matching_listener: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, String, Option<String>, bool) {
    let args = Args::parse();
    (
        args.common.into(),
        args.key,
        args.payload,
        args.attach,
        args.add_matching_listener,
    )
}
```

---

# Example: examples--examples--z_pull.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{handlers::RingChannel, key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, size, interval) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Subscriber on '{key_expr}'...");
    let subscriber = session
        .declare_subscriber(&key_expr)
        .with(RingChannel::new(size))
        .await
        .unwrap();

    println!("Press CTRL-C to quit...");

    // Blocking recv. If the ring is empty, wait for the first sample to arrive.
    loop {
        // Use .recv() for the synchronous version.
        match subscriber.recv_async().await {
            Ok(sample) => {
                let payload = sample
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(
                    ">> [Subscriber] Pulled {} ('{}': '{}')... performing a computation of {:#?}",
                    sample.kind(),
                    sample.key_expr().as_str(),
                    payload,
                    interval
                );
                tokio::time::sleep(interval).await;
            }
            Err(e) => {
                println!(">> [Subscriber] Pull error: {e}");
                return;
            }
        }
    }

    // Non-blocking recv. This can be usually used to implement a polling mechanism.
    // loop {
    //     match subscriber.try_recv() {
    //         Ok(Some(sample)) => {
    //             let payload = sample
    //                 .payload()
    //                 .try_to_string()
    //                 .unwrap_or_else(|e| e.to_string().into());
    //             println!(
    //                 ">> [Subscriber] Pulled {} ('{}': '{}')",
    //                 sample.kind(),
    //                 sample.key_expr().as_str(),
    //                 payload,
    //             );
    //         }
    //         Ok(None) => {
    //             println!(
    //                 ">> [Subscriber] Pulled nothing... sleep for {:#?}",
    //                 interval
    //             );
    //             tokio::time::sleep(interval).await;
    //         }
    //         Err(e) => {
    //             println!(">> [Subscriber] Pull error: {e}");
    //             return;
    //         }
    //     }
    // }
}

#[derive(clap::Parser, Clone, PartialEq, Debug)]
struct SubArgs {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The Key Expression to subscribe to.
    key: KeyExpr<'static>,
    /// The size of the ringbuffer.
    #[arg(short, long, default_value = "3")]
    size: usize,
    /// The interval for pulling the ringbuffer.
    #[arg(short, long, default_value = "5.0")]
    interval: f32,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, usize, Duration) {
    let args = SubArgs::parse();
    let interval = Duration::from_secs_f32(args.interval);
    (args.common.into(), args.key, args.size, interval)
}
```

---

# Example: examples--examples--z_put_float.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;
use zenoh_ext::z_serialize;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, payload) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Putting Float ('{key_expr}': '{payload}')...");
    // you must have imported `zenoh_ext::ZBytesExt` to use `ZBytes::serialize`
    session.put(&key_expr, z_serialize(&payload)).await.unwrap();

    session.close().await.unwrap();
}

#[derive(clap::Parser, Clone, PartialEq, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-put")]
    /// The key expression to write to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value_t = std::f64::consts::PI)]
    /// The payload to write.
    payload: f64,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, f64) {
    let args = Args::parse();
    (args.common.into(), args.key, args.payload)
}
```

---

# Example: examples--examples--z_put.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, payload) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Putting Data ('{key_expr}': '{payload}')...");
    // Refer to z_bytes.rs to see how to serialize different types of message
    session.put(&key_expr, payload).await.unwrap();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-put")]
    /// The key expression to write to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "Put from Rust!")]
    /// The payload to write.
    payload: String,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, String) {
    let args = Args::parse();
    (args.common.into(), args.key, args.payload)
}
```

---

# Example: examples--examples--z_querier.rs

```rs
//
// Copyright (c) 2024 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Duration;

use clap::Parser;
use zenoh::{
    query::{QueryTarget, Selector},
    Config,
};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");
    let (config, selector, payload, target, timeout, add_matching_listener) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Querier on '{}'...", selector.key_expr());
    let querier = session
        .declare_querier(selector.key_expr())
        .target(target)
        .timeout(timeout)
        .await
        .unwrap();

    if add_matching_listener {
        querier
            .matching_listener()
            .callback(|matching_status| {
                if matching_status.matching() {
                    println!("Querier has matching queryables.");
                } else {
                    println!("Querier has NO MORE matching queryables.");
                }
            })
            .background()
            .await
            .unwrap();
    }

    let params = selector.parameters().as_str();

    println!("Press CTRL-C to quit...");
    for idx in 0..u32::MAX {
        tokio::time::sleep(Duration::from_secs(1)).await;
        let buf = format!("[{idx:4}] {}", payload.clone().unwrap_or_default());
        println!("Querying '{}' with payload: '{}'...", &selector, buf);
        let replies = querier
            .get()
            // // By default get receives replies from a FIFO.
            // // Uncomment this line to use a ring channel instead.
            // // More information on the ring channel are available in the z_pull example.
            // .with(zenoh::handlers::RingChannel::default())
            // Refer to z_bytes.rs to see how to serialize different types of message
            .payload(buf)
            .parameters(params)
            .await
            .unwrap();
        while let Ok(reply) = replies.recv_async().await {
            match reply.result() {
                Ok(sample) => {
                    // Refer to z_bytes.rs to see how to deserialize different types of message
                    let payload = sample
                        .payload()
                        .try_to_string()
                        .unwrap_or_else(|e| e.to_string().into());
                    println!(
                        ">> Received ('{}': '{}')",
                        sample.key_expr().as_str(),
                        payload,
                    );
                }
                Err(err) => {
                    let payload = err
                        .payload()
                        .try_to_string()
                        .unwrap_or_else(|e| e.to_string().into());
                    println!(">> Received (ERROR: '{payload}')");
                }
            }
        }
    }
}

#[derive(clap::ValueEnum, Clone, Copy, Debug)]
#[value(rename_all = "SCREAMING_SNAKE_CASE")]
enum Qt {
    BestMatching,
    All,
    AllComplete,
}

#[derive(Parser, Clone, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The selection of resources to query
    selector: Selector<'static>,
    #[arg(short, long)]
    /// An optional payload to put in the query.
    payload: Option<String>,
    #[arg(short, long, default_value = "BEST_MATCHING")]
    /// The target queryables of the query.
    target: Qt,
    #[arg(short = 'o', long, default_value = "10000")]
    /// The query timeout in milliseconds.
    timeout: u64,
    /// Enable matching listener.
    #[arg(long)]
    add_matching_listener: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (
    Config,
    Selector<'static>,
    Option<String>,
    QueryTarget,
    Duration,
    bool,
) {
    let args = Args::parse();
    (
        args.common.into(),
        args.selector,
        args.payload,
        match args.target {
            Qt::BestMatching => QueryTarget::BestMatching,
            Qt::All => QueryTarget::All,
            Qt::AllComplete => QueryTarget::AllComplete,
        },
        Duration::from_millis(args.timeout),
        args.add_matching_listener,
    )
}
```

---

# Example: examples--examples--z_queryable_shm.rs

```rs
use std::borrow::Cow;

//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{
    bytes::ZBytes,
    key_expr::KeyExpr,
    shm::{BlockOn, GarbageCollect, ShmProviderBuilder},
    Config, Wait,
};
use zenoh_examples::CommonArgs;

const N: usize = 10;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, payload, complete) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Creating POSIX SHM provider...");
    // Create SHM provider with default backend
    // NOTE: For extended PosixShmProviderBackend API please check z_posix_shm_provider.rs
    let provider = ShmProviderBuilder::default_backend(N * 1024)
        .wait()
        .unwrap();

    println!("Declaring Queryable on '{key_expr}'...");
    let queryable = session
        .declare_queryable(&key_expr)
        .complete(complete)
        .await
        .unwrap();

    println!("Press CTRL-C to quit...");
    while let Ok(query) = queryable.recv_async().await {
        // Print overall query payload information
        match query.payload() {
            Some(payload) => {
                let (payload_type, payload) = handle_bytes(payload);
                print!(
                    ">> [Queryable] Received Query ('{}': '{}') [{}]",
                    query.selector(),
                    payload,
                    payload_type,
                );
            }
            None => {
                print!(">> Received Query '{}'", query.selector());
            }
        };

        // Print attachment information
        if let Some(att) = query.attachment() {
            let (attachment_type, attachment) = handle_bytes(att);
            print!(" ({attachment_type}: {attachment})");
        }

        println!();

        // Allocate an SHM buffer
        // NOTE: For allocation API please check z_alloc_shm.rs example
        // NOTE: For buf's API please check z_bytes_shm.rs example
        println!("Allocating Shared Memory Buffer...");
        let mut sbuf = provider
            .alloc(1024)
            .with_policy::<BlockOn<GarbageCollect>>()
            .await
            .unwrap();

        sbuf[0..payload.len()].copy_from_slice(payload.as_bytes());

        println!(
            ">> [Queryable] Responding ('{}': '{}')",
            key_expr.as_str(),
            payload,
        );
        query
            .reply(key_expr.clone(), sbuf)
            .await
            .unwrap_or_else(|e| println!(">> [Queryable ] Error sending reply: {e}"));
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-queryable")]
    /// The key expression matching queries to reply to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "Queryable from Rust SHM!")]
    /// The payload to reply to queries.
    payload: String,
    #[arg(long)]
    /// Declare the queryable as complete w.r.t. the key expression.
    complete: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, String, bool) {
    let args = Args::parse();
    (args.common.into(), args.key, args.payload, args.complete)
}

fn handle_bytes(bytes: &ZBytes) -> (&str, Cow<'_, str>) {
    // Determine buffer type for indication purpose
    let bytes_type = {
        // if Zenoh is built without SHM support, the only buffer type it can receive is RAW
        #[cfg(not(feature = "shared-memory"))]
        {
            "RAW"
        }

        // if Zenoh is built with SHM support but without SHM API (that is unstable), it can
        // receive buffers of any type, but there is no way to detect the buffer type
        #[cfg(all(feature = "shared-memory", not(feature = "unstable")))]
        {
            "UNKNOWN"
        }

        // if Zenoh is built with SHM support and with SHM API  we can detect the exact buffer type
        #[cfg(all(feature = "shared-memory", feature = "unstable"))]
        match bytes.as_shm() {
            Some(_) => "SHM",
            None => "RAW",
        }
    };

    // In order to indicate the real underlying buffer type the code above is written ^^^
    // Sample is SHM-agnostic: Sample handling code works both with SHM and RAW data transparently.
    // In other words, the common application compiled with "shared-memory" feature will be able to
    // handle incoming SHM data without any changes in the application code.
    //
    // Refer to z_bytes.rs to see how to deserialize different types of message
    let bytes_string = bytes
        .try_to_string()
        .unwrap_or_else(|e| e.to_string().into());

    (bytes_type, bytes_string)
}
```

---

# Example: examples--examples--z_queryable.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, payload, complete) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Queryable on '{key_expr}'...");
    let queryable = session
        .declare_queryable(&key_expr)
        // // By default queryable receives queries from a FIFO.
        // // Uncomment this line to use a ring channel instead.
        // // More information on the ring channel are available in the z_pull example.
        // .with(zenoh::handlers::RingChannel::default())
        .complete(complete)
        .await
        .unwrap();

    println!("Press CTRL-C to quit...");
    while let Ok(query) = queryable.recv_async().await {
        match query.payload() {
            None => println!(">> [Queryable ] Received Query '{}'", query.selector()),
            Some(query_payload) => {
                // Refer to z_bytes.rs to see how to deserialize different types of message
                let deserialized_payload = query_payload
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!(
                    ">> [Queryable ] Received Query '{}' with payload '{}'",
                    query.selector(),
                    deserialized_payload
                )
            }
        }
        println!(
            ">> [Queryable ] Responding ('{}': '{}')",
            key_expr.as_str(),
            payload,
        );
        // Refer to z_bytes.rs to see how to serialize different types of message
        query
            .reply(key_expr.clone(), payload.clone())
            .await
            .unwrap_or_else(|e| println!(">> [Queryable ] Error sending reply: {e}"));
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/zenoh-rs-queryable")]
    /// The key expression matching queries to reply to.
    key: KeyExpr<'static>,
    #[arg(short, long, default_value = "Queryable from Rust!")]
    /// The payload to reply to queries.
    payload: String,
    #[arg(long)]
    /// Declare the queryable as complete w.r.t. the key expression.
    complete: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, String, bool) {
    let args = Args::parse();
    (args.common.into(), args.key, args.payload, args.complete)
}
```

---

# Example: examples--examples--z_scout.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use zenoh::{config::WhatAmI, scout, Config};

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    println!("Scouting...");
    let receiver = scout(WhatAmI::Peer | WhatAmI::Router, Config::default())
        .await
        .unwrap();

    let _ = tokio::time::timeout(std::time::Duration::from_secs(1), async {
        while let Ok(hello) = receiver.recv_async().await {
            println!("{hello}");
        }
    })
    .await;

    // stop scouting
    receiver.stop();
}
```

---

# Example: examples--examples--z_storage.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
#![recursion_limit = "256"]

use std::collections::HashMap;

use clap::Parser;
use futures::select;
use zenoh::{
    key_expr::{keyexpr, KeyExpr},
    sample::{Sample, SampleKind},
    Config,
};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, complete) = parse_args();

    let mut stored: HashMap<String, Sample> = HashMap::new();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Subscriber on '{key_expr}'...");
    let subscriber = session.declare_subscriber(&key_expr).await.unwrap();

    println!("Declaring Queryable on '{key_expr}'...");
    let queryable = session
        .declare_queryable(&key_expr)
        .complete(complete)
        .await
        .unwrap();

    println!("Press CTRL-C to quit...");
    loop {
        select!(
            sample = subscriber.recv_async() => {
                let sample = sample.unwrap();
                let payload = sample.payload().try_to_string().unwrap_or_else(|e| e.to_string().into());
                println!(">> [Subscriber] Received {} ('{}': '{}')", sample.kind(), sample.key_expr().as_str(),payload);
                match sample.kind() {
                    SampleKind::Delete => stored.remove(&sample.key_expr().to_string()),
                    SampleKind::Put => stored.insert(sample.key_expr().to_string(), sample),
                };
            },

            query = queryable.recv_async() => {
                let query = query.unwrap();
                println!(">> [Queryable ] Received Query '{}'", query.selector());
                for (stored_name, sample) in stored.iter() {
                    if query.key_expr().intersects(unsafe {keyexpr::from_str_unchecked(stored_name)}) {
                        query.reply(sample.key_expr().clone(), sample.payload().clone()).await.unwrap();
                    }
                }
            }
        );
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The selection of resources to store.
    key: KeyExpr<'static>,
    #[arg(long)]
    /// Declare the storage as complete w.r.t. the key expression.
    complete: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, bool) {
    let args = Args::parse();
    (args.common.into(), args.key, args.complete)
}
```

---

# Example: examples--examples--z_sub_liveliness.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, sample::SampleKind, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr, history) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Liveliness Subscriber on '{}'...", &key_expr);

    let subscriber = session
        .liveliness()
        .declare_subscriber(&key_expr)
        .history(history)
        .await
        .unwrap();

    println!("Press CTRL-C to quit...");
    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => println!(
                ">> [LivelinessSubscriber] New alive token ('{}')",
                sample.key_expr().as_str()
            ),
            SampleKind::Delete => println!(
                ">> [LivelinessSubscriber] Dropped token ('{}')",
                sample.key_expr().as_str()
            ),
        }
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "group1/**")]
    /// The key expression to subscribe to.
    key: KeyExpr<'static>,
    #[arg(long)]
    /// Get historical liveliness tokens.
    history: bool,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>, bool) {
    let args = Args::parse();
    (args.common.into(), args.key, args.history)
}
```

---

# Example: examples--examples--z_sub_shm.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::borrow::Cow;

use clap::Parser;
#[cfg(all(feature = "shared-memory", feature = "unstable"))]
use zenoh::shm::zshmmut;
use zenoh::{bytes::ZBytes, config::Config, key_expr::KeyExpr};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Subscriber on '{}'...", &key_expr);
    let subscriber = session.declare_subscriber(&key_expr).await.unwrap();

    println!("Press CTRL-C to quit...");
    while let Ok(mut sample) = subscriber.recv_async().await {
        let kind = sample.kind();
        let key_str = sample.key_expr().as_str().to_owned();

        // Print overall payload information
        let (payload_type, payload) = handle_bytes(sample.payload_mut());
        print!(">> [Subscriber] Received {kind} ('{key_str}': '{payload}') [{payload_type}] ",);

        // Print attachment information
        if let Some(att) = sample.attachment_mut() {
            let (attachment_type, attachment) = handle_bytes(att);
            print!(" ({attachment_type}: {attachment})");
        }

        println!();
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct SubArgs {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The Key Expression to subscribe to.
    key: KeyExpr<'static>,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>) {
    let args = SubArgs::parse();
    (args.common.into(), args.key)
}

fn handle_bytes(bytes: &mut ZBytes) -> (&str, Cow<'_, str>) {
    // Determine buffer type for indication purpose
    let bytes_type = {
        // if Zenoh is built without SHM support, the only buffer type it can receive is RAW
        #[cfg(not(feature = "shared-memory"))]
        {
            "RAW"
        }

        // if Zenoh is built with SHM support but without SHM API (that is unstable), it can
        // receive buffers of any type, but there is no way to detect the buffer type
        #[cfg(all(feature = "shared-memory", not(feature = "unstable")))]
        {
            "UNKNOWN"
        }

        // if Zenoh is built with SHM support and with SHM API we can detect the exact buffer type
        #[cfg(all(feature = "shared-memory", feature = "unstable"))]
        match bytes.as_shm_mut() {
            // try to mutate SHM buffer to get it's mutability property
            Some(shm) => match <&mut zshmmut>::try_from(shm) {
                Ok(_shm_mut) => "SHM (MUT)",
                Err(_) => "SHM (IMMUT)",
            },
            None => "RAW",
        }
    };

    // In order to indicate the real underlying buffer type the code above is written ^^^
    // Sample is SHM-agnostic: Sample handling code works both with SHM and RAW data transparently.
    // In other words, the common application compiled with "shared-memory" feature will be able to
    // handle incoming SHM data without any changes in the application code.
    //
    // Refer to z_bytes.rs to see how to deserialize different types of message
    let bytes_string = bytes
        .try_to_string()
        .unwrap_or_else(|e| e.to_string().into());

    (bytes_type, bytes_string)
}
```

---

# Example: examples--examples--z_sub_thr.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use std::time::Instant;

use clap::Parser;
use zenoh::{Config, Wait};
use zenoh_examples::CommonArgs;

struct Stats {
    round_count: usize,
    round_size: usize,
    finished_rounds: usize,
    round_start: Instant,
    global_start: Option<Instant>,
}
impl Stats {
    fn new(round_size: usize) -> Self {
        Stats {
            round_count: 0,
            round_size,
            finished_rounds: 0,
            round_start: Instant::now(),
            global_start: None,
        }
    }
    fn increment(&mut self) {
        if self.round_count == 0 {
            self.round_start = Instant::now();
            if self.global_start.is_none() {
                self.global_start = Some(self.round_start)
            }
            self.round_count += 1;
        } else if self.round_count < self.round_size {
            self.round_count += 1;
        } else {
            self.print_round();
            self.finished_rounds += 1;
            self.round_count = 0;
        }
    }
    fn print_round(&self) {
        let elapsed = self.round_start.elapsed().as_secs_f64();
        let throughput = (self.round_size as f64) / elapsed;
        println!("{throughput} msg/s");
    }
}
impl Drop for Stats {
    fn drop(&mut self) {
        let Some(global_start) = self.global_start else {
            return;
        };
        let elapsed = global_start.elapsed().as_secs_f64();
        let total = self.round_size * self.finished_rounds + self.round_count;
        let throughput = total as f64 / elapsed;
        println!("Received {total} messages over {elapsed:.2}s: {throughput}msg/s");
    }
}

fn main() {
    // initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, m, n) = parse_args();

    let session = zenoh::open(config).wait().unwrap();

    let key_expr = "test/thr";

    let mut stats = Stats::new(n);
    session
        .declare_subscriber(key_expr)
        .callback_mut(move |_sample| {
            stats.increment();
            if stats.finished_rounds >= m {
                std::process::exit(0)
            }
        })
        .background()
        .wait()
        .unwrap();

    println!("Press CTRL-C to quit...");
    std::thread::park();
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct Args {
    #[arg(short, long, default_value = "10")]
    /// Number of throughput measurements.
    samples: usize,
    #[arg(short, long, default_value = "100000")]
    /// Number of messages in each throughput measurements.
    number: usize,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, usize, usize) {
    let args = Args::parse();
    (args.common.into(), args.samples, args.number)
}
```

---

# Example: examples--examples--z_sub.rs

```rs
//
// Copyright (c) 2023 ZettaScale Technology
//
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
// which is available at https://www.apache.org/licenses/LICENSE-2.0.
//
// SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
//
// Contributors:
//   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
//
use clap::Parser;
use zenoh::{key_expr::KeyExpr, Config};
use zenoh_examples::CommonArgs;

#[tokio::main]
async fn main() {
    // Initiate logging
    zenoh::init_log_from_env_or("error");

    let (config, key_expr) = parse_args();

    println!("Opening session...");
    let session = zenoh::open(config).await.unwrap();

    println!("Declaring Subscriber on '{}'...", &key_expr);
    let subscriber = session.declare_subscriber(&key_expr).await.unwrap();

    println!("Press CTRL-C to quit...");
    while let Ok(sample) = subscriber.recv_async().await {
        // Refer to z_bytes.rs to see how to deserialize different types of message
        let payload = sample
            .payload()
            .try_to_string()
            .unwrap_or_else(|e| e.to_string().into());

        print!(
            ">> [Subscriber] Received {} ('{}': '{}')",
            sample.kind(),
            sample.key_expr().as_str(),
            payload
        );
        if let Some(att) = sample.attachment() {
            let att = att.try_to_string().unwrap_or_else(|e| e.to_string().into());
            print!(" ({att})");
        }
        println!();
    }
}

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
struct SubArgs {
    #[arg(short, long, default_value = "demo/example/**")]
    /// The Key Expression to subscribe to.
    key: KeyExpr<'static>,
    #[command(flatten)]
    common: CommonArgs,
}

fn parse_args() -> (Config, KeyExpr<'static>) {
    let args = SubArgs::parse();
    (args.common.into(), args.key)
}
```

---

# Zenoh Rust examples

## Start instructions

   When Zenoh is built in release mode:

   ```bash
   ./target/release/example/<example_name>
   ```

   Each example accepts the `-h` or `--help` option that provides a description of its arguments and their default values.

   If you run the tests against the Zenoh router running in a Docker container, you need to add the
   `-e tcp/localhost:7447` option to your examples. That's because Docker doesn't support UDP multicast
   transport, and therefore the Zenoh scouting and discovery mechanism cannot work with it.

## Examples description

### z_scout

   Scouts for Zenoh peers and routers available on the network.

   Typical usage:

   ```bash
   z_scout
   ```

### z_info

   Gets information about the Zenoh session.

   Typical usage:

   ```bash
   z_info
   ```

### z_put

   Puts a path/value into Zenoh.
   The path/value will be received by all matching subscribers, for instance the [z_sub](#z_sub)
   and [z_storage](#z_storage) examples.

   Typical usage:

   ```bash
   z_put
   ```

   or

   ```bash
   z_put -k demo/example/test -v 'Hello World'
   ```

### z_pub

   Declares a key expression and a publisher. Then writes values periodically on the declared key expression.
   The published value will be received by all matching subscribers, for instance the [z_sub](#z_sub) and [z_storage](#z_storage) examples.

   Typical usage:

   ```bash
   z_pub
   ```

   or

   ```bash
   z_pub -k demo/example/test -v 'Hello World'
   ```

### z_sub

   Declares a key expression and a subscriber.
   The subscriber will be notified of each `put` or `delete` made on any key expression matching the subscriber key expression, and will print this notification.

   Typical usage:

   ```bash
   z_sub
   ```

   or

   ```bash
   z_sub -k 'demo/**'
   ```

### z_pull

   Declares a key expression and a pull subscriber.  
   On each pull, the pull subscriber will be notified of the last N `put` or `delete` made on each key expression matching the subscriber key expression, and will print this notification.

   Typical usage:

   ```bash
   z_pull
   ```

   or

   ```bash
   z_pull -k demo/** --size 3
   ```

### z_get

   Sends a query message for a selector.
   The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
   will receive this query and reply with paths/values that will be received by the receiver stream.

   Typical usage:

   ```bash
   z_get
   ```

   or

   ```bash
   z_get -s 'demo/**'
   ```

### z_querier

   Continuously sends query messages for a selector.
   The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
   will receive these queries and reply with paths/values that will be received by the querier.

   Typical usage:

   ```bash
   z_querier
   ```

   or

   ```bash
   z_querier -s 'demo/**'
   ```

### z_queryable

   Declares a queryable function with a path.
   This queryable function will be triggered by each call to get
   with a selector that matches the path, and will return a value to the querier.

   Typical usage:

   ```bash
   z_queryable
   ```

   or

   ```bash
   z_queryable -k demo/example/queryable -v 'This is the result'
   ```

### z_storage

   Trivial implementation of a storage in memory.
   This example declares a subscriber and a queryable on the same selector.
   The subscriber callback will store the received paths/values in a hashmap.
   The queryable callback will answer to queries with the paths/values stored in the hashmap
   and that match the queried selector.

   Typical usage:

   ```bash
   z_storage
   ```

   or

   ```bash
   z_storage -k 'demo/**'
   ```

### z_pub_shm & z_sub

   A pub/sub example involving the shared-memory feature.
   Note that on subscriber side, the same `z_sub` example than for non-shared-memory example is used.

   Typical Subscriber usage:

   ```bash
   z_sub
   ```

   Typical Publisher usage:

   ```bash
   z_pub_shm
   ```

### z_pub_thr & z_sub_thr

   Pub/Sub throughput test.
   This example allows performing throughput measurements between a publisher performing
   put operations and a subscriber receiving notifications of those puts.

   Typical Subscriber usage:

   ```bash
   z_sub_thr
   ```

   Typical Publisher usage:

   ```bash
   z_pub_thr 1024
   ```

### z_ping & z_pong

   Pub/Sub roundtrip time test.
   This example allows performing roundtrip time measurements. The z_ping example
   performs a put operation on a first key expression, waits for a reply from the pong
   example on a second key expression and measures the time between the two.
   The pong application waits for samples on the first key expression and replies by
   writing back the received data on the second key expression.

  :warning: z_pong needs to start first to avoid missing the kickoff from z_ping.

   Typical Pong usage:

   ```bash
   z_pong
   ```

   Typical Ping usage:

   ```bash
   z_ping 1024
   ```

### z_pub_shm_thr & z_sub_thr

   Pub/Sub throughput test involving the shared-memory feature.
   This example allows performing throughput measurements between a publisher performing
   put operations with the shared-memory feature and a subscriber receiving notifications
   of those puts.
   Note that on subscriber side, the same `z_sub_thr` example than for non-shared-memory example is used.

   Typical Subscriber usage:

   ```bash
   z_sub_thr
   ```

   Typical Publisher usage:

   ```bash
   z_pub_shm_thr
   ```

### z_liveliness

   Declares a liveliness token on a given key expression (`group1/zenoh-rs` by default).
   This token will be seen alive by the `z_get_liveliness` and `z_sub_liveliness` until
   user explicitly drops the token by pressing `'d'` or implicitly dropped by terminating
   or killing the `z_liveliness` example.

   Typical usage:

   ```bash
   z_liveliness
   ```

   or

   ```bash
   z_liveliness -k 'group1/member1'
   ```

### z_get_liveliness

   Queries all the currently alive liveliness tokens that match a given key expression
   (`group1/**` by default). Those tokens could be declared by the `z_liveliness` example.

   Typical usage:

   ```bash
   z_get_liveliness
   ```

   or

   ```bash
   z_get_liveliness -k 'group1/**'
   ```

### z_sub_liveliness

   Subscribe to all liveliness changes (liveliness tokens getting alive or
   liveliness tokens being dropped) that match a given key expression
   (`group1/**` by default). Those tokens could be declared by the `z_liveliness`
   example.
   Note: the `z_sub_liveliness` example will not receive information about
   matching liveliness tokens that were alive before it's start.

   Typical usage:

   ```bash
   z_sub_liveliness
   ```

   or

   ```bash
   z_sub_liveliness -k 'group1/**'
   ```

### z_bytes

   Show how to serialize different message types into ZBytes, and then deserialize from ZBytes to the original message types.

### z_bytes_shm

   Show how to work with SHM buffers: mut and const access, buffer ownership concepts

### z_alloc_shm

   Show how to allocate SHM buffers

---

# Example: examples--src--lib.rs

```rs
//! Examples on using Zenoh.
//! See the code in ../examples/
//! Check ../README.md for usage.
//!

use serde_json::json;
use zenoh::{config::WhatAmI, Config};

#[derive(clap::Parser, Clone, PartialEq, Eq, Hash, Debug)]
pub struct CommonArgs {
    #[arg(short, long)]
    /// A configuration file.
    config: Option<String>,
    #[arg(long)]
    /// Allows arbitrary configuration changes as column-separated KEY:VALUE pairs, where:
    ///   - KEY must be a valid config path.
    ///   - VALUE must be a valid JSON5 string that can be deserialized to the expected type for the KEY field.
    ///
    /// Example: `--cfg='transport/unicast/max_links:2'`
    #[arg(long)]
    cfg: Vec<String>,
    #[arg(short, long)]
    /// The Zenoh session mode [default: peer].
    mode: Option<WhatAmI>,
    #[arg(short = 'e', long)]
    /// Endpoints to connect to.
    connect: Vec<String>,
    #[arg(short, long)]
    /// Endpoints to listen on.
    listen: Vec<String>,
    #[arg(long)]
    /// Disable the multicast-based scouting mechanism.
    no_multicast_scouting: bool,
    #[arg(long)]
    /// Enable shared-memory feature.
    enable_shm: bool,
}

impl From<CommonArgs> for Config {
    fn from(value: CommonArgs) -> Self {
        (&value).into()
    }
}

impl From<&CommonArgs> for Config {
    fn from(args: &CommonArgs) -> Self {
        let mut config = match &args.config {
            Some(path) => Config::from_file(path).unwrap(),
            None => Config::default(),
        };
        if let Some(mode) = args.mode {
            config
                .insert_json5("mode", &json!(mode.to_str()).to_string())
                .unwrap();
        }

        if !args.connect.is_empty() {
            config
                .insert_json5("connect/endpoints", &json!(args.connect).to_string())
                .unwrap();
        }
        if !args.listen.is_empty() {
            config
                .insert_json5("listen/endpoints", &json!(args.listen).to_string())
                .unwrap();
        }
        if args.no_multicast_scouting {
            config
                .insert_json5("scouting/multicast/enabled", &json!(false).to_string())
                .unwrap();
        }
        if args.enable_shm {
            #[cfg(feature = "shared-memory")]
            config
                .insert_json5("transport/shared_memory/enabled", &json!(true).to_string())
                .unwrap();
            #[cfg(not(feature = "shared-memory"))]
            {
                eprintln!("`--enable-shm` argument: SHM cannot be enabled, because Zenoh is compiled without shared-memory feature!");
                std::process::exit(-1);
            }
        }
        for json in &args.cfg {
            if let Some((key, value)) = json.split_once(':') {
                if let Err(err) = config.insert_json5(key, value) {
                    eprintln!("`--cfg` argument: could not parse `{json}`: {err}");
                    std::process::exit(-1);
                }
            } else {
                eprintln!("`--cfg` argument: expected KEY:VALUE pair, got {json}");
                std::process::exit(-1);
            }
        }
        config
    }
}
```

---

