# Source: https://juno.build/docs/examples/functions/typescript/assertion.md

# Source: https://juno.build/docs/examples/functions/rust/assertion.md

# Rust Assertion Example

This example demonstrates how to write a **custom assertion** in **Rust** for a Juno **serverless function**. It shows how to intercept and validate data operationsâsuch as rejecting specific contentâbefore it's written to the datastore.

The project includes a minimal frontend to help trigger and test the logic, but the primary focus is the backend assertion.

You can browse the source code here: [github.com/junobuild/examples/tree/main/functions/rust/assertions](https://github.com/junobuild/examples/tree/main/functions/rust/assertions)

---

## Folder Structure

```
rust/assertions/âââ src/â   âââ satellite/           # Rust Satellite serverless functionâ   â   âââ src/â   â   â   âââ lib.rs       # Main Rust logic for Satelliteâ   â   âââ satellite.did    # Candid interface definitionâ   â   âââ Cargo.toml       # Rust package configâââ src/components/          # Minimal frontend React componentsâââ juno.config.ts           # Juno Satellite configurationâââ package.json             # Frontend dependenciesâââ ...
```

---

## Key Features

*   **Custom Assertions in Rust**: Demonstrates how to reject or validate data before it's saved, using Rust serverless functions.
*   **Serverless Integration**: Runs as a Satellite function and integrates with Juno's datastore and authentication system.
*   **Minimal UI for Testing**: A simple frontend is included to test and demonstrate the assertion logic in action.

---

## Main Backend Components

*   **src/satellite/src/lib.rs**: The core Rust logic for the Satellite serverless function. Implements the custom assertions (e.g., only allow certain valid inputs, etc.).
*   **src/satellite/Cargo.toml**: Rust package configuration for the Satellite function.

---

## Example: Custom Assertion in Rust

Hereâs the actual Rust logic from `lib.rs`:

```
// This example defines a custom assertion in a Juno Satellite using Rust.// It checks if a document being saved to the "notes" collection contains the word "hello".// If it does, the assertion rejects the operation and logs a message.use ic_cdk::print;use junobuild_macros::assert_set_doc;use junobuild_satellite::{include_satellite, AssertSetDocContext};use junobuild_utils::decode_doc_data;use serde::{Deserialize, Serialize};#[derive(Serialize, Deserialize)]struct Note {    text: String,    url: Option<String>,}#[assert_set_doc(collections = ["notes"])]fn assert_set_doc(context: AssertSetDocContext) -> Result<(), String> {    let note = decode_doc_data::<Note>(&context.data.data.proposed.data)?;    if note.text.to_lowercase().contains("hello") {        print(format!("â Rejected note containing 'hello': {}", note.text));        return Err("The note should not contain the keyword 'hello'.".to_string());    }    print(format!("â Note accepted: {}", note.text));    Ok(())}include_satellite!();
```

**Explanation:**

*   Defines a `Note` struct with `text` and optional `url` fields. Similar as the fields used in the frontend.
*   Uses the `#[assert_set_doc]` macro to create a custom assertion for the `notes` collection.
*   When a note is created or updated, the assertion checks if the note's text contains the word "hello" (case-insensitive).
*   If it does, the note is rejected and an error message is returned; otherwise, the note is accepted.
*   Prints a message to the log for both accepted and rejected notes.
*   `include_satellite!();` brings in the necessary boilerplate for the Juno Satellite runtime.

---

## How to Run

1.  **Clone the repo**:

```
git clone https://github.com/junobuild/examplescd rust/assertions
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

*   `notes` in Datastore: [http://localhost:5866/datastore](http://localhost:5866/datastore)
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

*   This example focuses on the Rust serverless function; the frontend is intentionally minimal and only included for demonstration purposes.
*   Use this project as a starting point for writing custom assertions and backend logic in Rust with Juno.

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