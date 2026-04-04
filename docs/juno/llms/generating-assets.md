# Source: https://juno.build/docs/examples/functions/rust/generating-assets.md

# Generating Assets with Rust Serverless Functions

This example demonstrates how to use **Rust serverless functions** to dynamically generate and store assets in **Juno Storage** from a **Satellite**. In this example, the generated assets are JSON files.

Each time a note is added through the frontend, the Satellite saves the note as an individual JSON file and updates a list of all notes as another JSON file. This pattern is useful for exposing structured, queryable data as static assets â consumable by your frontend or external services.

You can browse the source code here: [github.com/junobuild/examples/tree/main/functions/rust/json](https://github.com/junobuild/examples/tree/main/functions/rust/json)

---

## Folder Structure

```
rust/json/âââ src/â   âââ satellite/           # Rust Satellite serverless functionâ   â   âââ src/â   â   â   âââ lib.rs       # Main Rust logic for Satelliteâ   â   â   âââ generators.rs# Helper logic for JSON generation/storageâ   â   âââ satellite.did    # Candid interface definitionâ   â   âââ Cargo.toml       # Rust package configâ   âââ declarations/        # TypeScript declarations for Satelliteâ   âââ lib/                 # Svelte frontend components, stores, typesâ   âââ routes/              # SvelteKit route filesâ   âââ app.html             # Svelte app entryâ   âââ app.css              # Stylesâââ juno.config.ts           # Juno Satellite configurationâââ package.json             # Frontend dependenciesâââ ...
```

---

## Key Features

*   **Serverless JSON Generation**: Demonstrates how to generate and store JSON files in Storage from Rust serverless functions.
*   **Automatic List Updates**: Each note addition updates both the individual note JSON and a list of all notes as JSON.
*   **Integration with Juno Storage**: Uses Juno's Storage API to expose JSON assets on the web.
*   **Minimal SvelteKit UI**: A simple SvelteKit frontend is included to test and demonstrate the logic.

---

## Main Backend Components

*   **src/satellite/src/lib.rs**: The entry point for the Satellite serverless function. Triggers JSON generation and list update on document set.
*   **src/satellite/src/generators.rs**: Helper logic for encoding notes and lists as JSON and storing them as assets.
*   **src/satellite/Cargo.toml**: Rust package configuration for the Satellite function.

---

## Example: Generating and Storing JSON

Hereâs the actual Rust logic from `lib.rs` and `generators.rs`:

```
// src/satellite/src/lib.rsmod generators;use crate::generators::{generate_list_of_notes, generate_note};use junobuild_macros::on_set_doc;use junobuild_satellite::{include_satellite, OnSetDocContext};/// Hook triggered whenever a document is set (e.g., added or updated)./// This example:/// - Stores the updated document as an individual JSON file in Storage/// - Updates a list of all note filenames as a separate JSON file#[on_set_doc]async fn on_set_doc(context: OnSetDocContext) -> Result<(), String> {    ic_cdk::print("Let's go!");    // Save the current note as a JSON asset    generate_note(&context.data.key, &context.data.data.after)?;    // Regenerate the list of notes as a JSON array    generate_list_of_notes()?;    Ok(())}// Boilerplate macro to include the all Satellite runtimeinclude_satellite!();
```

```
// src/satellite/src/generators.rsuse junobuild_satellite::{list_assets_store, set_asset_handler, Doc};use junobuild_shared::types::core::Key;use junobuild_shared::types::list::ListParams;use junobuild_storage::http::types::HeaderField;use junobuild_storage::types::store::AssetKey;use junobuild_utils::{decode_doc_data, encode_doc_data_to_string};use serde::{Deserialize, Serialize};/// Represents the expected shape of a note stored in the Datastore#[derive(Serialize, Deserialize)]struct Note {    text: String,    url: Option<String>,}/// Encodes a note document as JSON and stores it as a `.json` file in Storagepub fn generate_note(key: &Key, doc: &Doc) -> Result<(), String> {    let note: Note = decode_doc_data(&doc.data)?;    let json = encode_doc_data_to_string(&note)?;    let name = format!("{}.json", key);    insert_asset(&name, &json)}const STORAGE_COLLECTION: &str = "json";/// Lists all assets in the `json` collection and stores their filenames/// in a `notes.json` file â a JSON array of all note filenamespub fn generate_list_of_notes() -> Result<(), String> {    let params: ListParams = ListParams {        matcher: None,        paginate: None,        order: None,        owner: None,    };    let result = list_assets_store(ic_cdk::id(), STORAGE_COLLECTION, &params)?;    // Extract the full paths of all assets in the collection    let list_of_keys: Vec<String> = result        .items        .iter()        .map(|(_, asset)| asset.key.full_path.clone())        .collect();    let json = encode_doc_data_to_string(&list_of_keys)?;    let name = "notes.json".to_string();    insert_asset(&name, &json)?;    Ok(())}/// Stores a given string as an asset in the `json` collectionfn insert_asset(name: &String, json: &String) -> Result<(), String> {    ic_cdk::print(format!("Json: {} {}", name, json));    let full_path = format!("/{}/{}", STORAGE_COLLECTION, name);    let key: AssetKey = AssetKey {        name: name.clone(),        full_path: full_path.clone(),        token: None,        collection: STORAGE_COLLECTION.to_string(),        owner: ic_cdk::id(),        description: None,    };    // Set appropriate headers for serving JSON    let headers = vec![HeaderField(        "content-type".to_string(),        "application/json".to_string(),    )];    // Upload asset to Juno Storage    set_asset_handler(&key, &json.as_bytes().to_vec(), &headers)?;    ic_cdk::print(format!(        "Asset saved in Storage: http://{}.localhost:5987{}",        ic_cdk::id(),        full_path    ));    Ok(())}
```

**Explanation:**

*   When a note is added or updated, the `on_set_doc` hook is triggered.
*   The note is encoded as JSON and stored as an asset in the `json` collection.
*   A list of all note asset paths is also generated and stored as `notes.json`.
*   These JSON assets are accessible via the Storage API and can be fetched by the frontend or other clients.

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
*   `json` in Storage: [http://localhost:5866/storage](http://localhost:5866/storage)

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
*   Use this project as a starting point for generate dynamic assets using Juno and Rust.

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