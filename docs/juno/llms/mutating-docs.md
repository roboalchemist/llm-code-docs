# Source: https://juno.build/docs/examples/functions/typescript/mutating-docs.md

# Source: https://juno.build/docs/examples/functions/rust/mutating-docs.md

# Mutating Documents with Rust Hooks

This example demonstrates how to use **hooks in Rust** to modify documents automatically when they're created or updated in your Juno **Satellite**.

Hooks let you react to events like document creation, deletion, or asset uploads â and run custom backend logic in response.

You can browse the source code here: [github.com/junobuild/examples/tree/main/functions/rust/hooks](https://github.com/junobuild/examples/tree/main/functions/rust/hooks)

---

## Folder Structure

```
rust/hooks/âââ src/â   âââ satellite/           # Rust Satellite serverless functionâ   â   âââ src/â   â   â   âââ lib.rs       # Main Rust logic for Satelliteâ   â   âââ satellite.did    # Candid interface definitionâ   â   âââ Cargo.toml       # Rust package configâ   âââ declarations/        # TypeScript declarations for Satelliteâ   âââ admin.ts             # Frontend admin logicâ   âââ doc.ts               # Frontend doc logicâ   âââ main.ts              # Frontend entry pointâ   âââ storage.ts           # Frontend storage logicâ   âââ style.css            # Frontend stylesâââ juno.config.ts           # Juno Satellite configurationâââ package.json             # Frontend dependenciesâââ ...
```

---

## Key Features

*   **Serverless Hooks in Rust**: Demonstrates how to react to data and asset operations using hooks in Rust serverless functions.
*   **Multiple Hook Types**: Includes hooks for document set, set-many, delete, and asset upload operations.
*   **Serverless Integration**: Runs as a Satellite function and integrates with Juno's datastore and authentication system.
*   **Minimal UI for Testing**: A simple frontend is included to test and demonstrate the hook logic in action.

---

## Main Backend Components

*   **src/satellite/src/lib.rs**: The core Rust logic for the Satellite serverless function. Implements hooks for various operations (set, set-many, delete, upload).
*   **src/satellite/Cargo.toml**: Rust package configuration for the Satellite function.

---

## Example: Mutating Documents

Hereâs the actual Rust logic from `lib.rs`:

```
use ic_cdk::print;use junobuild_macros::{on_delete_doc, on_set_doc, on_set_many_docs, on_upload_asset};use junobuild_satellite::{    include_satellite, set_doc_store, OnDeleteDocContext, OnSetDocContext, OnSetManyDocsContext,    OnUploadAssetContext, SetDoc,};use junobuild_utils::{decode_doc_data, encode_doc_data};use junobuild_utils::{DocDataBigInt, DocDataPrincipal};use serde::{Deserialize, Serialize};/// Example struct used to demonstrate decode/edit/store flow.#[derive(Serialize, Deserialize)]struct Person {    yolo: bool,    hello: String,    principal: DocDataPrincipal,    value: DocDataBigInt,}// Hook that runs when a document is set in the "demo" collection#[on_set_doc(collections = ["demo"])]async fn on_set_doc(context: OnSetDocContext) -> Result<(), String> {    // Decode the document into our Person struct    let mut data: Person = decode_doc_data(&context.data.data.after.data)?;    // Log some values for debugging    print(format!("[on_set_doc] Caller: {}", context.caller.to_text()));    print(format!("[on_set_doc] Collection: {}", context.data.collection));    print(format!("[on_set_doc] Data: {} {}", data.principal.value, data.value.value));    // Modify the document before storing it again    data.hello = format!("{} checked", data.hello);    data.yolo = false;    // Encode and re-store the updated document    let encode_data = encode_doc_data(&data)?;    let doc: SetDoc = SetDoc {        data: encode_data,        description: context.data.data.after.description,        version: context.data.data.after.version,    };    set_doc_store(        context.caller,        context.data.collection,        context.data.key,        doc,    )?;    Ok(())}include_satellite!();
```

**Explanation:**

*   Defines a `Person` struct with fields for demo purposes.
*   Uses the `#[on_set_doc]` macro to run logic whenever a document is set in the `demo` collection. Updates the document and saves it back.
*   `include_satellite!();` brings in the necessary boilerplate for the Juno Satellite runtime.

---

## How to Run

1.  **Clone the repo**:

```
git clone https://github.com/junobuild/examplescd rust/hooks
```

2. **Install dependencies**:

```
npm install
```

3. **Start Juno local emulator**:

**Important:**

Requires the Juno CLI to be available `npm i -g @junobuild/cli`

```
juno emulator start
```

4. **Create a Satellite** for local dev:

*   Visit [http://localhost:5866](http://localhost:5866) and follow the instructions.
*   Update `juno.config.ts` with your Satellite ID.

5.  **Create required collections**:

*   `demo` in Datastore: [http://localhost:5866/datastore](http://localhost:5866/datastore)
*   `images` in Storage: [http://localhost:5866/storage](http://localhost:5866/storage)

6.  **Start the frontend dev server** (in a separate terminal):

```
npm run dev
```

7.  **Build the serverless functions** (in a separate terminal):

```
juno functions build
```

The emulator will automatically upgrade your Satellite and live reload the changes.

---

## Juno-Specific Configuration

*   **juno.config.ts**: Defines Satellite IDs for development/production, build source, and predeploy steps. See the [Configuration reference](/docs/reference/configuration.md) for details.
*   **vite.config.ts**: Registers the `juno` plugin to inject environment variables automatically. See the [Vite Plugin reference](/docs/reference/plugins.md#vite-plugin) for more information.

---

## Production Deployment

*   Create a Satellite on the [Juno Console](https://console.juno.build) for mainnet.
*   Update `juno.config.ts` with the production Satellite ID.
*   Build and deploy the frontend:

```
npm run buildjuno hosting deploy
```

*   Build and upgrade the serverless functions:

```
juno functions buildjuno functions upgrade
```

---

## Notes

*   This example focuses on the Rust serverless function. The frontend is intentionally minimal and included only for demonstration.
*   Use this project as a starting point for writing custom backend logic in Rust using Juno hooks.

---

## Real-World Example

Want to see how assertions and serverless logic are used in a live project?

Check out [proposals.network](https://proposals.network), an open-source app built with Juno:

*   GitHub: [github.com/peterpeterparker/proposals.network](https://github.com/peterpeterparker/proposals.network)
*   Example logic: [src/satellite/src/lib.rs](https://github.com/peterpeterparker/proposals.network/blob/main/src/satellite/src/lib.rs)

This app uses:

*   `#[on_delete_doc]` and `#[assert_delete_doc]` to validate and clean up related documents and assets
*   Shared helper modules like `assert`, `delete`, and `types` to keep logic organized
*   A real-world pattern of chaining asset/document deletions with assertions

Itâs a great reference for more advanced setups and multi-collection coordination.

---

## References

*   [Serverless Functions Guide](/docs/guides/rust.md)
*   [Functions Development](/docs/build/functions.md)
*   [Rust SDK Reference](/docs/reference/functions/rust/sdk.md)
*   [Rust Utils Reference](/docs/reference/functions/rust/utils.md)
*   [Run Local Development](/docs/guides/local-development.md)
*   [CLI Reference](/docs/reference/cli.md)
*   [Configuration Reference](/docs/reference/configuration.md)
*   [Datastore Collections](/docs/build/datastore/collections.md)

---

## Crate Docs

These crates are used to build and extend serverless functions in Rust with Juno:

*   [junobuild-satellite](https://docs.rs/junobuild-satellite): Core features and runtime for building a Satellite in Rust, including hooks, assertions, and datastore integration.
*   [junobuild-macros](https://docs.rs/junobuild-macros): Procedural macros for declaratively attaching hooks and assertions.
*   [junobuild-utils](https://docs.rs/junobuild-utils): Utility helpers for working with documents, including data encoding, decoding, and assertion context handling.
*   [junobuild-shared](https://docs.rs/junobuild-shared): Shared types and helpers for Juno projects. Used by all containers including the Console.
*   [junobuild-storage](https://docs.rs/junobuild-storage): Storage helpers for working with assets and HTTP headers in Juno.