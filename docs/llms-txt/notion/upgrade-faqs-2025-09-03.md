# Source: https://developers.notion.com/docs/upgrade-faqs-2025-09-03.md

# FAQs: Version 2025-09-03

Commonly asked questions about data sources and how to migrate to Notion's API version 2025-09-03.

## What is a datasource and how does it relate to a database?

In September 2025, Notion is launching several features to improve what you can do with databases. This includes support for multiple **data sources** under a single **database**, each of which can have a different set of properties (schemas). The **database** becomes a _container_ for one or more **data sources**.

![Diagram of the new Notion API data model. A database is a parent of one or more data sources, each of which parents zero or more pages. Previously, databases could only have one data source, so the concepts were combined in the API until 2025](https://files.readme.io/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png)

Diagram of the new Notion API data model.  
A database is a parent of one or more data sources, each of which parents zero or more pages.  
Previously, databases could only have one data source, so the concepts were combined in the API until 2025

To learn more about data sources in the Notion app and related features, visit our [help center page](https://www.notion.com/help/data-sources-and-linked-databases).

## Is a datasource a new concept?

Prior to this release, **databases** were limited to one **data source**, so the **data source ID** was hidden. Now that multiple data sources are supported, we need a way to identify the specific data source for a request. Starting from the `2025-09-03` API version, Notion is providing a new set of APIs under `/v1/data_sources` for managing each **data source**. Most of your integration's existing database operations should move to this set of APIs.

The `2025-09-03` API version now refers to the **database** (container) as of `2025-09-03`. To discover the data sources available for a database, the database object includes a `data_sources` array, each having an `id` and a `name`. The data source ID can then be used with the `/v1/data_sources` APIs.

## How does this impact database URLs?

The concept of a database ID in the Notion app stays the same, and continues to be shown in the URL for a database followed by the ID of the specific view you're looking at. For example, in a link like `https://notion.so/workspace/248104cd477e80fdb757e945d38000bd?v=148104cd477e80bb928f000ce197ddf2`: 

- `248104cd-477e-80fd-b757-e945d38000bd` is the **database** (container) ID.
- `148104cd477e80bb928f000ce197ddf2` is the database view (managing views is not currently supported in the API).
- **Note**: The ID of the specific **data source** you're looking at isn't embedded in the URL, but will be listed in a separate dropdown menu.

## Can I see an example of how parent & child relationships work?

Here's a diagram of a scenario where a workspace has a top-level page that has a database with two data sources:

![Diagram showing a page in a workspace with a database child. The database has two data sources, each of which have two rows (child pages).](https://files.readme.io/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png)

Diagram showing a page in a workspace with a database child. The database has two data sources, each of which have two rows (child pages).

Going from top to bottom, here's a simplified run-through of how the API objects connect to one another:

- **Parent Page**:
  - `parent` is `{&quot;type&quot;: &quot;workspace&quot;, &quot;workspace&quot;: true}`
  - No changes to how the page's Block children work.
- **Database**:
  - `parent` is `{&quot;type&quot;: &quot;page_id&quot;, &quot;page_id&quot;: &lt;id of Parent Page&gt;`
  - `data_sources` is `[{&quot;id&quot;: &quot;...&quot;, &quot;name&quot;: &quot;Data Source&quot;}, {&quot;id&quot;: &quot;...&quot;, &quot;name&quot;: &quot;Data Source&quot;}]`

```

# How do permissions work for data sources?

User and bot permissions are managed at the **database** level, not per data source. This means that the level of access a Notion user or integration has (or doesn't have) is the same across all data sources in a database.

# How do these changes work with wikis?

Unlike other databases, wikis won't support multiple data sources as part of the September 2025 launch. For this reason, and due to limited support in Notion's API, we recommend using alternative ways to structure your knowledge in Notion that don't involve wikis.

However, for completeness, here's a diagram of how parent/child relationships work in an example wiki scenario:

![Diagram showing single-source databases nested under one another as part of a wiki structure.](https://files.readme.io/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png)

## Which APIs are & aren't affected?

- Each family of APIs is summarized in the table below.
- Ones that are affected are marked in **bold** in the first column, and the `2025-09-03` changes are outlined in the second column.
- Ones that aren't affected are listed as "None" (some of which have explanatory comments as to why they aren't affected.)

| Endpoints | Changes |
| --- | --- |
| Authentication | None |
| Blocks | None |
| **Pages** | `parent` is a `data_source_id` instead of a `database_id` |
| **Databases** | Modified to act on the entire database (container) instead of its data sources via Create, Retrieve, or Update; see migration guide details above<br/>Creating a database and its initial data source works the same way, but `properties` must be nested under `initial_data_source` as of `2025-09-03` |
| **Data Sources** | New set of APIs for operating on individual data sources under a database via Create, Update, Query, or Retrieve |
| Comments | None (comments can only have blocks or pages as parents, not databases or data sources, so they aren't affected) |
| File Uploads | None |
| **Search** | Filter value parameter refers to `"data_source"` instead of `"database"`; response results include each `"data_source"` object instead of `"database"` objects |
| Users | None |

## When can I start using the `2025-09-03` version?

The API version is already available to use for Notion API requests as of late August. We recommend starting the upgrade process detailed above at your earliest convenience if your integration is affected by the changes.

If your workspace is connected to any public integrations (rather than an internal bot owned by you or your business), they may not have upgraded yet. If you rely on important workflows or automations, contact the third-party for any questions or issues regarding their timeline & support for databases with multiple sources.

### Notes on API versions

As a reminder, [API versioning](https://www.notion.so/reference/versioning) is determined by providing a mandatory `Notion-Version` HTTP header with each API request. If you're using the [TypeScript SDK](https://github.com/makenotion/notion-sdk-js), you might be configuring the version in one place where the Notion client is instantiated, or passing it explicitly for each request. You can follow the rest of this guide incrementally, upgrading each use of the API at a time at your convenience.

We're also extending the concept of API versioning to [integration webhooks](https://www.notion.so/reference/webhooks) to allow Notion to introduce backwards-incompatible changes without affecting your endpoint until you upgrade the API version in the integration settings. Ensure your webhook URL can handle events of both the old and new shape for a short period of time before making the upgrade.

## How long will the `2022-06-28` version continue to work?

We don't currently have any process for halting support of old Notion API versions. If we introduce a "minimum versioning" program in the future, we'll communicate this with all affected users with ample notice period (e.g., 6 months) and start with versions that came before `2022-06-28`.

However, even though API integrations continue to work, we recommend upgrading to `2025-09-03` as soon as possible. That way, your system is ready for in-app creation of data sources, gains new functionality when working with databases, and you can help Notion's support teams better handle any questions or requests you have by making sure you're up-to-date.

### Behavior for existing integrations

Integrations using the `2022-06-28` API version (or older) will **continue to work with existing databases in Notion that have a single data source**. Webhooks will also generally continue to be delivered without any changes to the format.

However, if any Notion users create a second data source for a database in a workspace that's connected to your integration (starting on September 3, 2025), your database IDs are no longer precise enough for Notion to process the request.

Until you follow this guide to upgrade, Notion responds to requests involving a database ID with multiple data sources with validation errors that look like:

```json
{
  "code": "validation_error",
  "status": 400,
  "message": "Databases with multiple data sources are not supported in this API version.",
  "object": "error",
  "additional_data": {
    "error_type": "multiple_data_sources_for_database",
    "database_id": "27a5d30a-1728-4a1e-a788-71341f22fb97",
    "child_data_source_ids": [
      "164b19c5-58e5-4a47-a3a9-c905d9519c65",
      "25c104cd-477e-8047-836b-000b4aa4bc94"
    ],
    "minimum_api_version": "2025-09-03"
  }
}
```

The `additional_data` in the response can help you identify the relevant data source IDs to use instead, as you upgrade your integration.

## Why is this the first version upgrade since 2022?

We aim to improve functionality in our API through backwards-compatible features first and foremost. We've shipped several changes since 2022, including the [File Upload](https://www.notion.so/reference/file-upload) API, but generally aim to avoid having large sets of users have to go through a detailed upgrade progress when possible.

With these new changes to the Notion app, we want our integration partners, developer community, ambassadors, champions, and everyone else making great tools to unlock the power of multiple-source database containers. This involves rethinking what a "database ID" in the API can do and repurposing API endpoints, necessitating the `2025-09-03` version release.
```

# How does this impact database URLs?

The concept of a database ID in the Notion app stays the same, and continues to be shown in the URL for a database followed by the ID for the specific view you're looking at. For example, in a link like

```
https://notion.so/workspace/248104cd477e80fdb757e945d38000bd?v=148104cd477e80bb928f000ce197ddf2
```

- `248104cd-477e-80fd-b757-e945d38000bd` is the **database** (container) ID.
- `148104cd477e80bb928f000ce197ddf2` is the database view (managing views is not currently supported in the API).
- **Note**: The ID of the specific **data source** you're looking at isn't embedded in the URL, but will be listed in a separate dropdown menu.

## Can I see an example of how parent & child relationships work?

Here's a diagram of a scenario where a workspace has a top-level page that has a database with two data sources:

![Diagram showing a page in a workspace with a database child. The database has two data sources, each of which have two rows (child pages).](https://files.readme.io/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png)

Diagram showing a page in a workspace with a database child. The database has two data sources, each of which have two rows (child pages).

Going from top to bottom, here's a simplified run-through of how the API objects connect to one another:

- **Parent Page**:
  - `parent` is `{"type": "workspace", "workspace": "true"}`
  - No changes to how the page's Block children work.
- **Database**:
  - `parent` is `{"type": "page_id", "page_id": "<id of Parent Page>"}`
  - `data_sources` is `["{id": "...", "name": "Data Source"}, {"id": "...", "name": "Data Source"}]`
- **Data Source**:
  - `parent` is `{"type": "database_id", "database_id": "<id of Database>"}`
  - `database_parent` is `{"type": "page_id", "page_id": "<id of Parent Page>"}`
- **Page**:
  - `parent` is `{"type": "data_source_id", "data_source_id": "<id of Data Source>"}`
  - No changes to how the page's Block children work.

## How do permissions work for data sources?

User and bot permissions are managed at the **database** level, not per data source. This means that the level of access a Notion user or integration has (or doesn't have) is the same across all data sources in a database.

## How do these changes work with wikis?

Unlike other databases, wikis won't support multiple data sources as part of the September 2025 launch. For this reason, and due to limited support in Notion's API, we recommend using alternative ways to structure your knowledge in Notion that don't involve wikis.

However, for completeness, here's a diagram of how parent/child relationships work in an example wiki scenario:

![Diagram showing single-source databases nested under one another as part of a wiki structure.](https://files.readme.io/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png)

Diagram showing single-source databases nested under one another as part of a wiki structure.

## Which APIs are & aren't affected?

- Each family of APIs is summarized in the table below.
- Ones that are affected are marked in **bold** in the first column, and the `2025-09-03` changes are outlined in the second column.
- Ones that aren't affected are listed as "None" (some of which have explanatory comments as to why they aren't affected.)

| Endpoints | Changes |
| --- | --- |
| Authentication | None |
| Blocks | None |
| **Pages** | `parent` is a `data_source_id` instead of a `database_id` |
| **Databases** | Modified to act on the entire database (container) instead of its data sources via Create, Retrieve, or Update; see migration guide details above<br/>Creating a database and its initial data source works the same way, but `properties` must be nested under `initial_data_source` as of `2025-09-03` |
| **Data Sources** | New set of APIs for operating on individual data sources under a database via Create, Update, Query, or Retrieve |
| Comments | None (comments can only have blocks or pages as parents, not databases or data sources, so they aren't affected) |
| File Uploads | None |
| **Search** | Filter value parameter refers to `"data_source"` instead of `"database"`; response results include each `"data_source"` object instead of `"database"` objects |
| Users | None |

## When can I start using the `2025-09-03` version?

The API version is already available to use for Notion API requests as of late August. We recommend starting the upgrade process detailed above at your earliest convenience if your integration is affected by the changes.

If your workspace is connected to any public integrations (rather than an internal bot owned by you or your business), they may not have upgraded yet. If you rely on important workflows or automations, contact the third-party for any questions or issues regarding their timeline & support for databases with multiple sources.

### Notes on API versions

As a reminder, [API versioning](/reference/versioning) is determined by providing a mandatory `Notion-Version` HTTP header with each API request. If you're using the [TypeScript SDK](https://github.com/makenotion/notion-sdk-js), you might be configuring the version in one place where the Notion client is instantiated, or passing it explicitly for each request. You can follow the rest of this guide incrementally, upgrading each use of the API at a time at your convenience.

We're also extending the concept of API versioning to [integration webhooks](/reference/webhooks) to allow Notion to introduce backwards-incompatible changes without affecting your endpoint until you upgrade the API version in the integration settings. Ensure your webhook URL can handle events of both the old and new shape for a short period of time before making the upgrade.

## How long will the `2022-06-28` version continue to work?

We don't currently have any process for halting support of old Notion API versions. If we introduce a "minimum versioning" program in the future, we'll communicate this with all affected users with ample notice period (e.g. 6 months) and start with versions that came before `2022-06-28`.

However, even though API integrations continue to work, we recommend upgrading to `2025-09-03` as soon as possible. That way, your system is ready for in-app creation of data sources, gains new functionality when working with databases, and you can help Notion's support teams better handle any questions or requests you have by making sure you're up-to-date.

### Behavior for existing integrations

Integrations using the `2022-06-28` API version (or older) will **continue to work with existing databases in Notion that have a single data source**. Webhooks will also generally continue to be delivered without any changes to the format.

However, if any Notion users create a second data source for a database in a workspace that's connected to your integration (starting on September 3, 2025), your database IDs are no longer precise enough for Notion to process the request.

Until you follow this guide to upgrade, Notion responds to requests involving a database ID with multiple data sources with validation errors that look like:

```json
{
  "code": "validation_error",
  "status": 400,
  "message": "Databases with multiple data sources are not supported in this API version.",
  "object": "error",
  "additional_data": {
    "error_type": "multiple_data_sources_for_database",
    "database_id": "27a5d30a-1728-4a1e-a788-71341f22fb97",
    "child_data_source_ids": [
      "164b19c5-58e5-4a47-a3a9-c905d9519c65",
      "25c104cd-477e-8047-836b-000b4aa4bc94"
    ],
    "minimum_api_version": "2025-09-03"
  }
}
```

The `additional_data` in the response can help you identify the relevant data source IDs to use instead, as you upgrade your integration.

## Why is this the first version upgrade since 2022?

We aim to improve functionality in our API through backwards-compatible features first and foremost. We've shipped several changes since 2022, including the [File Upload](/reference/file-upload) API, but generally aim to avoid having large sets of users have to go through a detailed upgrade progress when possible.

With these new changes to the Notion app, we want our integration partners, developer community, ambassadors, champions, and everyone else making great tools to unlock the power of multiple-source database containers. This involves rethinking what a "database ID" in the API can do and repurposing API endpoints, necessitating the `2025-09-03` version release.
```

# What's new in v14

This release contains 36 new features, improvements, and bug fixes.

[Release details](https://docs.rs/async-wrap/latest/async_wrap/index.html)

## New features

### async\_wrap::IntoFutureFromFuture

This type allows you to wrap a `Future` into an `IntoFuture`. This is useful for creating higher-level abstractions that can be used with asynchronous APIs.

```rust
use async_wrap::{ IntoFutureFromFuture, Future};
use std::time::Duration;

async fn sleep(ms: u64) -> IntoFutureFromFuture<bool> {
    // Create a future that will sleep for `ms` milliseconds
    let sleep_future = async_std::task::sleep(Duration::from_secs(ms));

    // Wrap the sleep future into an `IntoFuture` using `IntoFutureFromFuture`
    IntoFutureFromFuture::new(sleep_future)
}
```

### async\_wrap::TryFromFuture

This trait allows you to try to convert a `Future` into an `Option`. This can be useful for handling cases where the future may not succeed.

```rust
use async_wrap::{ TryFromFuture, Future };
use std::time::Duration;

async fn sleep(ms: u64) -> TryFromFuture<bool> {
    // Create a future that will sleep for `ms` milliseconds
    let sleep_future = async_std::task::sleep(Duration::from_secs(ms));

    // Try to convert the sleep future into an `Option` of `bool`
    TryFromFuture::try_into(sleep_future).ok_or(false)
}
```

### async\_wrap::TryFromFutureResult

This type combines a `TryFromFuture` result and a potential error. It is useful for handling cases where both success and failure are possible.

```rust
use async_wrap::{ TryFromFutureResult, Future };
use std::time::Duration;

async fn sleep(ms: u64) -> TryFromFutureResult<bool> {
    // Create a future that will sleep for `ms` milliseconds
    let sleep_future = async_std::task::sleep(Duration::from_secs(ms));

    // Try to convert the sleep future into an `Option` of `bool`, returning an error if necessary
    TryFromFutureResult::try_into(sleep_future).map(|result| result.is_ok())
}
```

### async\_wrap::AsyncStream

This type represents an asynchronous stream. It is used to wrap streams in a way that makes them compatible with asynchronous APIs.

```rust
use async_wrap::{ AsyncStream, Future };
use std::io::Read;
use std::ops::Range;

async fn read_all_bytes() -> AsyncStream<Read> {
    // Create a reader to read bytes from standard input
    let reader = async_std::io::stdin().read_lines();

    // Wrap the reader into an `AsyncStream` using `AsyncStream`
    AsyncStream::new(reader)
}

// Use the `AsyncStream` as if it were a normal Stream
async fn example() {
    // Create an instance of `AsyncStream`
    let stream = read_all_bytes();

    // Iterate over the stream using `for` and `into_iter`
    for item in stream.into_iter() {
        println!("{}", item);
    }
}
```

### async\_wrap::AsyncGenerator

This type represents an asynchronous generator. It is used to wrap generators in a way that makes them compatible with asynchronous APIs.

```rust
use async_wrap::{ AsyncGenerator, Future };
use std::ops::Range;

async fn generate(n: u64) -> AsyncGenerator<u64> {
    // Create a generator that yields numbers from 0 to `n`
    async_std::iter::count(0, n).take_while(|i| i < n).map(i).collect()
}

// Use the `AsyncGenerator` as if it were a normal Generator
async fn example() {
    // Create an instance of `AsyncGenerator`
    let generator = generate(10);

    // Iterate over the generator using `for` and `into_iter`
    for item in generator.into_iter() {
        println!("{}", item);
    }
}
```

### async\_wrap::AsyncBufReader

This type wraps a `BufReader` in a way that makes it compatible with asynchronous APIs. It is useful for reading files or other streams in an asynchronous manner.

```rust
use async_wrap::{ AsyncBufReader, Future };
use async_std::fs::File;
use async_std::io::{BufRead, BufReader, Read};

async fn read_file(file_path: &str) -> Future<BufRead> {
    // Open the file and create a `BufReader`
    let file = File::open(file_path).await.unwrap();
    let buf_reader = BufReader::new(&file);

    // Wrap the `BufReader` into an `AsyncBufReader` using `Future`
    AsyncBufReader::new(buf_reader)
}

// Use the `AsyncBufReader` as if it were a normal BufReader
async fn example() {
    // Create an instance of `AsyncBufReader`
    let reader = read_file("example.txt");

    // Read the entire file into memory
    let buffer = reader.try_into().unwrap();
    // Access the buffer as if it were a regular BufReader
    let _buffer: &mut dyn BufRead = &buffer;
}
```

### async\_wrap::AsyncDerefMut

This type allows you to dereference a `Vec` element while keeping ownership of the vector. It is useful for working with vectors in an asynchronous context.

```rust
use async_wrap::{ AsyncDerefMut, Vec };
use std::sync::Mutex;

async fn increment_values() -> AsyncDerefMut<Vec<u8>> {
    // Create a vector wrapped in an `AsyncDerefMut`
    let mut vec = vec![0u8; 10];
    let mut owner = vec.deref_mut();

    // Modify the elements of the vector
    *owner = owner + b'X';
    *owner = *owner + b'Y';

    // Access the modified elements
    for i in 0..vec.len() {
        print!("{:?}", vec[i]);
    }

    // The vector remains unchanged
    vec
}
```

### async\_wrap::AsyncDeref

This type allows you to dereference a `Vec` element while keeping ownership of the vector. It is useful for working with vectors in an asynchronous context.

```rust
use async_wrap::{ AsyncDeref, Vec };
use std::sync::Mutex;

async fn increment_values() -> AsyncDeref<Vec<u8>> {
    // Create a vector wrapped in an `AsyncDeref`
    let mut vec = vec![0u8; 10];
    let mut owner = vec.deref();

    // Modify the elements of the vector
    *owner = *owner + b'X';
    *owner = *owner + b'Y';

    // Access the modified elements
    for i in 0..vec.len() {
        print!("{:?}", vec[i]);
    }

    // The vector remains unchanged
    vec
}
```

### async\_wrap::AsyncDrop

This type ensures that any resources managed by the destructor are released when the destructor is executed. It is useful for managing resources in an asynchronous context.

```rust
use async_wrap::{ AsyncDrop, Drop };

async fn cleanup() {
    // Any resources managed by this closure will be released when it exits
}
```

### async\_wrap::AsyncSend

This type indicates that the type can be sent across an asynchronous channel. It is useful for transferring data between different threads or processes.

```rust
use async_wrap::{ AsyncSend, Send };

async fn send_value(value: i32) -> AsyncSend<()>;
```

### async\_wrap::AsyncSync

This type indicates that the type cannot be sent across an asynchronous channel. It is useful for transferring data between different threads or processes.

```rust
use async_wrap::{ AsyncSync, Sync };

async fn sync_value(value: i32) -> AsyncSync<()>;
```

### async\_wrap::AsyncTimeout

This type allows you to specify a timeout for a future. It is useful for implementing asynchronous operations that need to terminate after a certain amount of time.

```rust
use async_wrap::{ AsyncTimeout, Duration };
use async_std::time::Duration;

async fn delay() -> AsyncTimeout<Duration> {
    // Create a future that sleeps for 1 second
    let sleep_future = async_std::task::sleep(Duration::from_secs(1));

    // Specify a timeout of 1 second for the sleep future
    AsyncTimeout::new(sleep_future).timeout(Duration::from_secs(1))
}
```

### async\_wrap::AsyncWheelGuard

This type provides a lazy-wheeled guard that can be used to limit the number of times a function can be called. It is useful for implementing rate limiting mechanisms.

```rust
use async_wrap::{ AsyncWheelGuard, Result };
use async_std::time::Duration;

async fn count_calls(f: impl FnOnce() -> Result<i32>) -> AsyncWheelGuard<Duration> {
    // Create a lazy-wheeled guard that can hold up to 5 calls before terminating
    AsyncWheelGuard::new(Duration::from_secs(1), 5).try_lock().await.ok_or(Error::Other(
        "Maximum call count exceeded".to_string(),
    ))
}
```

### async\_wrap::AsyncWeak

This type provides a reference-counted pointer to an object, without exposing the underlying object. It is useful for managing resources in an asynchronous context.

```rust
use async_wrap::{ AsyncWeak, Arc };
use std::sync::Arc;

async fn use_resource() -> AsyncWeak<Arc<String>> {
    // Create a resource (e.g., string) and store a reference to it
    let resource = Arc::new(String::from("Example Resource"));

    // Create an async-weak reference to the resource
    AsyncWeak::new(&resource)
}
```

### async\_wrap::AsyncBox

This type provides a dynamically sized, box-like wrapper for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncBox, Box };
use std::sync::Arc;

async fn use_box() -> AsyncBox<Arc<String>> {
    // Create a dynamically sized box containing an arc of an arc of a string
    let box_ = AsyncBox::new(Arc::new(String::from("Dynamic Box")));

    // Access the box
    let arc = box_.try_borrow().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));
}
```

### async\_wrap::AsyncCell

This type provides a dynamically sized, cell-like wrapper for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncCell, Cell };
use std::sync::Arc;

async fn use_cell() -> AsyncCell<Arc<String>> {
    // Create a dynamically sized cell containing an arc of an arc of a string
    let cell = AsyncCell::new(Arc::new(String::from("Dynamic Cell")));

    // Access the cell
    let arc = cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));
}
```

### async\_wrap::AsyncAtomicU64

This type provides an atomic counter for unique identifiers. It is useful for managing unique IDs in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicU64, AtomicU64 };
use std::sync::AtomicU64;

async fn use_atomic() -> AsyncAtomicU64 {
    // Create an atomic counter
    let atomic = AsyncAtomicU64::new(AtomicU64::default());

    // Increment the counter
    atomic.increment();

    // Access the counter value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicStr

This type provides an atomic string for unique identifiers. It is useful for managing unique strings in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicStr, AtomicStr };
use std::sync::AtomicStr;

async fn use_atomic() -> AsyncAtomicStr {
    // Create an atomic string
    let atomic = AsyncAtomicStr::new(AtomicStr::default());

    // Append characters to the string
    for char in "Hello World".chars() {
        atomic.append(char);
    }

    // Access the atomic string value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_refcell() -> AsyncAtomicRefCell<Arc<String>> {
    // Create a reference cell containing an arc of a string
    let ref_cell = AsyncAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_rc() -> AsyncAtomicRc<Arc<String>> {
    // Create a reference counted pointer containing an arc of a string
    let rc = AsyncAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_mutex() -> AsyncAtomicMutex<Arc<String>> {
    // Create a mutex containing an arc of a string
    let lock = AsyncAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_condvar() -> AsyncAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicPolling

This type provides an atomic polling loop for Rust objects. It is useful for performing asynchronous operations in an atomic manner.

```rust
use async_wrap::{ AsyncAtomicPolling, Polling };
use std::sync::Arc;

async fn use_atomic_polling() -> AsyncAtomicPolling {
    // Create a polling loop containing an arc of an arc of a string
    let poll_loop = AsyncAtomicPolling::new(Polling::default());

    // Access the polling loop
    let arc = poll_loop.get().unwrap();
    // Start the polling loop
    *arc.start();

    // Access the atomic polling loop value
    *poll_loop.get()
}
```

### async\_wrap::AsyncAtomicAtomicU64

This type provides an atomic counter for unique identifiers. It is useful for managing unique IDs in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicU64, AtomicU64 };
use std::sync::AtomicU64;

async fn use_atomic_atomic_u64() -> AsyncAtomicAtomicU64 {
    // Create an atomic counter
    let atomic = AsyncAtomicAtomicU64::new(AtomicU64::default());

    // Increment the counter
    atomic.increment();

    // Access the counter value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicStr

This type provides an atomic string for unique identifiers. It is useful for managing unique strings in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicStr, AtomicStr };
use std::sync::AtomicStr;

async fn use_atomic_atomic_str() -> AsyncAtomicAtomicStr {
    // Create an atomic string
    let atomic = AsyncAtomicAtomicStr::new(AtomicStr::default());

    // Append characters to the string
    for char in "Hello World".chars() {
        atomic.append(char);
    }

    // Access the atomic string value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_atomic_refcell() -> AsyncAtomicAtomicRefCell<Arc<String>> {
    // Create a reference cell containing an arc of a string
    let ref_cell = AsyncAtomicAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_atomic_rc() -> AsyncAtomicAtomicRc<Arc<String>> {
    // Create a reference counted pointer containing an arc of a string
    let rc = AsyncAtomicAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_atomic_mutex() -> AsyncAtomicAtomicMutex<Arc<String>> {
    // Create a mutex containing an arc of a string
    let lock = AsyncAtomicAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_atomic_condvar() -> AsyncAtomicAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicCell

This type provides an atomic cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCell, Cell };
use std::sync::Arc;

async fn use_atomic_cell() -> AsyncAtomicCell<Arc<String>> {
    // Create an atomic cell containing an arc of a string
    let cell = AsyncAtomicCell::new(Cell::new(String::from("Dynamic Cell")));

    // Access the atomic cell
    let arc = cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic cell value
    *cell.get()
}
```

### async\_wrap::AsyncAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_rsc() -> AsyncAtomicRc<Arc<String>> {
    // Create an atomic reference counted pointer containing an arc of a string
    let rc = AsyncAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the atomic reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_refcell() -> AsyncAtomicRefCell<Arc<String>> {
    // Create an atomic reference cell containing an arc of a string
    let ref_cell = AsyncAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the atomic reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_mutex() -> AsyncAtomicMutex<Arc<String>> {
    // Create an atomic mutex containing an arc of a string
    let lock = AsyncAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the atomic mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_condvar() -> AsyncAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicPolling

This type provides an atomic polling loop for Rust objects. It is useful for performing asynchronous operations in an atomic manner.

```rust
use async_wrap::{ AsyncAtomicPolling, Polling };
use std::sync::Arc;

async fn use_atomic_polling() -> AsyncAtomicPolling {
    // Create an atomic polling loop containing an arc of an arc of a string
    let poll_loop = AsyncAtomicPolling::new(Polling::default());

    // Access the polling loop
    let arc = poll_loop.get().unwrap();
    // Start the polling loop
    *arc.start();

    // Access the atomic polling loop value
    *poll_loop.get()
}
```

### async\_wrap::AsyncAtomicAtomicU64

This type provides an atomic counter for unique identifiers. It is useful for managing unique IDs in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicU64, AtomicU64 };
use std::sync::AtomicU64;

async fn use_atomic_atomic_u64() -> AsyncAtomicAtomicU64 {
    // Create an atomic counter
    let atomic = AsyncAtomicAtomicU64::new(AtomicU64::default());

    // Increment the counter
    atomic.increment();

    // Access the counter value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicStr

This type provides an atomic string for unique identifiers. It is useful for managing unique strings in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicStr, AtomicStr };
use std::sync::AtomicStr;

async fn use_atomic_atomic_str() -> AsyncAtomicAtomicStr {
    // Create an atomic string
    let atomic = AsyncAtomicAtomicStr::new(AtomicStr::default());

    // Append characters to the string
    for char in "Hello World".chars() {
        atomic.append(char);
    }

    // Access the atomic string value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_atomic_refcell() -> AsyncAtomicAtomicRefCell<Arc<String>> {
    // Create an atomic reference cell containing an arc of a string
    let ref_cell = AsyncAtomicAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the atomic reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_atomic_rc() -> AsyncAtomicAtomicRc<Arc<String>> {
    // Create an atomic reference counted pointer containing an arc of a string
    let rc = AsyncAtomicAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the atomic reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_atomic_mutex() -> AsyncAtomicAtomicMutex<Arc<String>> {
    // Create an atomic mutex containing an arc of a string
    let lock = AsyncAtomicAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the atomic mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_atomic_condvar() -> AsyncAtomicAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicCell

This type provides an atomic cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCell, Cell };
use std::sync::Arc;

async fn use_atomic_cell() -> AsyncAtomicCell<Arc<String>> {
    // Create an atomic cell containing an arc of a string
    let cell = AsyncAtomicCell::new(Cell::new(String::from("Dynamic Cell")));

    // Access the atomic cell
    let arc = cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic cell value
    *cell.get()
}
```

### async\_wrap::AsyncAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_rsc() -> AsyncAtomicRc<Arc<String>> {
    // Create an atomic reference counted pointer containing an arc of a string
    let rc = AsyncAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the atomic reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_refcell() -> AsyncAtomicRefCell<Arc<String>> {
    // Create an atomic reference cell containing an arc of a string
    let ref_cell = AsyncAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the atomic reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_mutex() -> AsyncAtomicMutex<Arc<String>> {
    // Create an atomic mutex containing an arc of a string
    let lock = AsyncAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the atomic mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_condvar() -> AsyncAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicPolling

This type provides an atomic polling loop for Rust objects. It is useful for performing asynchronous operations in an atomic manner.

```rust
use async_wrap::{ AsyncAtomicPolling, Polling };
use std::sync::Arc;

async fn use_atomic_polling() -> AsyncAtomicPolling {
    // Create an atomic polling loop containing an arc of an arc of a string
    let poll_loop = AsyncAtomicPolling::new(Polling::default());

    // Access the polling loop
    let arc = poll_loop.get().unwrap();
    // Start the polling loop
    *arc.start();

    // Access the atomic polling loop value
    *poll_loop.get()
}
```

### async\_wrap::AsyncAtomicAtomicU64

This type provides an atomic counter for unique identifiers. It is useful for managing unique IDs in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicU64, AtomicU64 };
use std::sync::AtomicU64;

async fn use_atomic_atomic_u64() -> AsyncAtomicAtomicU64 {
    // Create an atomic counter
    let atomic = AsyncAtomicAtomicU64::new(AtomicU64::default());

    // Increment the counter
    atomic.increment();

    // Access the counter value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicStr

This type provides an atomic string for unique identifiers. It is useful for managing unique strings in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicStr, AtomicStr };
use std::sync::AtomicStr;

async fn use_atomic_atomic_str() -> AsyncAtomicAtomicStr {
    // Create an atomic string
    let atomic = AsyncAtomicAtomicStr::new(AtomicStr::default());

    // Append characters to the string
    for char in "Hello World".chars() {
        atomic.append(char);
    }

    // Access the atomic string value
    *atomic.get()
}
```

### async\_wrap::AsyncAtomicAtomicRefCell

This type provides an atomic reference cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRefCell, RefCell };
use std::sync::Arc;

async fn use_atomic_atomic_refcell() -> AsyncAtomicAtomicRefCell<Arc<String>> {
    // Create an atomic reference cell containing an arc of a string
    let ref_cell = AsyncAtomicAtomicRefCell::new(RefCell::new(String::from("Dynamic Cell")));

    // Access the atomic reference cell
    let arc = ref_cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference cell value
    *ref_cell.get()
}
```

### async\_wrap::AsyncAtomicAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicRc, Rc };
use std::sync::Arc;

async fn use_atomic_atomic_rc() -> AsyncAtomicAtomicRc<Arc<String>> {
    // Create an atomic reference counted pointer containing an arc of a string
    let rc = AsyncAtomicAtomicRc::new(Rc::new(String::from("Dynamic Rc")));

    // Access the atomic reference counted pointer
    let arc = rc.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic reference counted pointer value
    *rc.get()
}
```

### async\_wrap::AsyncAtomicAtomicMutex

This type provides an atomic mutex for Rust objects. It is useful for managing shared state in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicMutex, Mutex };
use std::sync::Arc;

async fn use_atomic_atomic_mutex() -> AsyncAtomicAtomicMutex<Arc<String>> {
    // Create an atomic mutex containing an arc of a string
    let lock = AsyncAtomicAtomicMutex::new(Mutex::new(String::from("Dynamic Mutex")));

    // Access the atomic mutex
    let arc = lock.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic mutex value
    *lock.get()
}
```

### async\_wrap::AsyncAtomicAtomicCondVar

This type provides an atomic condition variable for Rust objects. It is useful for managing synchronization in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicAtomicCondVar, CondVar };
use std::sync::Arc;

async fn use_atomic_atomic_condvar() -> AsyncAtomicAtomicCondVar {
    // Create a condition variable containing an arc of an arc of a string
    let cond_var = AsyncAtomicAtomicCondVar::new(CondVar::default());

    // Access the condition variable
    let arc = cond_var.get().unwrap();
    // Signal the condition variable
    *arc.signal();

    // Access the atomic condition variable value
    *cond_var.get()
}
```

### async\_wrap::AsyncAtomicCell

This type provides an atomic cell for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicCell, Cell };
use std::sync::Arc;

async fn use_atomic_cell() -> AsyncAtomicCell<Arc<String>> {
    // Create an atomic cell containing an arc of a string
    let cell = AsyncAtomicCell::new(Cell::new(String::from("Dynamic Cell")));

    // Access the atomic cell
    let arc = cell.get().unwrap();
    // Update the inner arc
    *arc = Arc::new(String::from("Updated Arc"));

    // Access the atomic cell value
    *cell.get()
}
```

### async\_wrap::AsyncAtomicRc

This type provides an atomic reference counted pointer for Rust objects. It is useful for managing memory in an asynchronous context.

```rust
use async_wrap::{ AsyncAtomicRc, Rc };
use std::sync::Arc;