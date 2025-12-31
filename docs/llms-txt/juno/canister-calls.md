# Source: https://juno.build/docs/examples/functions/typescript/canister-calls.md

# Source: https://juno.build/docs/examples/functions/rust/canister-calls.md

# Making Canister Calls in Rust Serverless Functions

This example demonstrates how to use **Rust serverless functions** to perform canister calls (such as `transfer_from` on the ICP ledger) in response to Datastore events in your Juno **Satellite**.

When a document is added to the `request` collection, a serverless function is triggered to:

*   Check if the user has enough ICP in their wallet
*   Transfer ICP from the user's wallet to the Satellite using the ICRC ledger's `transfer_from` method
*   Mark the request as `processed` if the transfer succeeds

This pattern is useful for building workflows that require asset transfers or other canister calls in response to user actions.

You can browse the source code here: [github.com/junobuild/examples/tree/main/functions/rust/calls](https://github.com/junobuild/examples/tree/main/functions/rust/calls)

---

## Folder Structure

```
rust/calls/âââ src/â   âââ satellite/           # Rust Satellite serverless functionâ   â   âââ src/â   â   â   âââ lib.rs       # Main Rust logic for Satelliteâ   â   â   âââ services.rs  # Helper logic for balance, transfer, statusâ   â   â   âââ types.rs     # Data model for requestsâ   â   â   âââ ledger_icrc.rs # Ledger helper functionsâ   â   â   âââ ...â   â   âââ satellite.did    # Candid interface definitionâ   â   âââ Cargo.toml       # Rust package configâ   âââ declarations/        # TypeScript declarations for Satelliteâ   âââ components/          # React frontend componentsâ   âââ services/            # Frontend service logicâ   âââ types/               # Frontend type definitionsâ   âââ main.tsx             # Frontend entryâ   âââ ...âââ juno.config.ts           # Juno Satellite configurationâââ package.json             # Frontend dependenciesâââ
```

---

## Key Features

*   **Serverless Canister Calls**: Demonstrates how to perform ICRC ledger calls (e.g., `transfer_from`) from Rust serverless functions.
*   **Atomic Request Processing**: Ensures that request status is only updated if the transfer succeeds.
*   **Wallet Balance Checks**: Fails early if the user does not have enough ICP.
*   **Minimal React UI**: A simple React frontend is included to test and demonstrate the logic.

---

## Main Backend Components

*   **src/satellite/src/lib.rs**: The entry point for the Satellite serverless function. Triggers the canister call and updates request status on document set.
*   **src/satellite/src/services.rs**: Helper logic for checking wallet balance, performing the transfer, and updating request status.
*   **src/satellite/src/types.rs**: Data model for requests and status.
*   **src/satellite/Cargo.toml**: Rust package configuration for the Satellite function.

---

## Example: Canister Call on Document Set

Hereâs the actual Rust logic from `lib.rs` and `services.rs`:

```
// src/satellite/src/lib.rsmod env;mod ledger_icrc;mod services;mod types;mod utils;use crate::services::{assert_wallet_balance, set_request_processed, transfer_icp_from_wallet};use crate::types::RequestData;use crate::utils::icp_ledger_id;use ic_cdk::id;use icrc_ledger_types::icrc1::account::Account;use junobuild_macros::on_set_doc;use junobuild_satellite::{include_satellite, OnSetDocContext};use junobuild_utils::decode_doc_data;// Triggered when a new document is set in the "request" collection#[on_set_doc(collections = ["request"])]async fn on_set_doc(context: OnSetDocContext) -> Result<(), String> {    // Init data    let data: RequestData = decode_doc_data(&context.data.data.after.data)?;    let request_amount = data.amount.value;    let fee = data.fee.as_ref().map(|fee| fee.value);    let ledger_id = icp_ledger_id()?;    let from_account: Account = Account::from(context.caller);    // Check current account balance    assert_wallet_balance(&ledger_id, &from_account, &request_amount, &fee).await?;    // Update request status to processed (atomic with transfer)    set_request_processed(context.data.key, &data, &context.data.data.after.version)?;    // Transfer from wallet to satellite    let to_account: Account = Account::from(id());    transfer_icp_from_wallet(        &ledger_id,        &from_account,        &to_account,        &request_amount,        &fee,    )    .await?;    Ok(())}include_satellite!();
```

```
// src/satellite/src/services.rs/// Asserts that the given account has enough balance to cover the amount and fee.pub async fn assert_wallet_balance(    ledger_id: &Principal,    from_account: &Account,    amount: &u64,    fee: &Option<u64>,) -> Result<(), String> {    let balance = icrc_balance_of(&ledger_id, &from_account).await?;    let total = amount.saturating_add(fee.unwrap_or(10_000u64));    if balance < total {        return Err(format!("Balance {} is smaller than {}", balance, total));    }    Ok(())}/// Transfers ICP from one account to another using `icrc2_transfer_from`.pub async fn transfer_icp_from_wallet(    ledger_id: &Principal,    from_account: &Account,    to_account: &Account,    amount: &u64,    fee: &Option<u64>,) -> Result<(), String> {    let result = icrc_transfer_from(        &ledger_id,        &from_account,        &to_account,        &Nat::from(amount.clone()),        &fee.map(|fee| Nat::from(fee)),    )    .await    .map_err(|e| format!("Failed to call ICRC ledger icrc_transfer_from: {:?}", e))    .and_then(|result| {        result.map_err(|e| format!("Failed to execute the transfer from: {:?}", e))    })?;    print(format!("Result of the transfer from is {:?}", result));    Ok(())}/// Updates the request document status to `Processed`.pub fn set_request_processed(    key: String,    original_data: &RequestData,    original_version: &Option<u64>,) -> Result<(), String> {    let update_data: RequestData = RequestData {        status: RequestStatus::Processed,        ..original_data.clone()    };    let data = encode_doc_data(&update_data)?;    let doc: SetDoc = SetDoc {        data,        description: None,        version: original_version.clone(),    };    let _ = set_doc_store(id(), "request".to_string(), key, doc)?;    Ok(())}
```

**Explanation:**

*   When a request is submitted, the `on_set_doc` hook is triggered for the `request` collection.
*   The function checks the user's wallet balance, updates the request status, and performs the ICP transfer atomically.
*   If any step fails, the entire operation is reverted.
*   The frontend can monitor request status and balances via the exposed APIs.

---

## How to Run

1.  **Clone the repo**:

```
git clone https://github.com/junobuild/examplescd rust/calls
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

*   `request` in Datastore: [http://localhost:5866/datastore](http://localhost:5866/datastore)

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

*   This example focuses on the Rust serverless function and canister call integration. The frontend is intentionally minimal and included only for demonstration.
*   Use this project as a starting point for workflows that require on-chain asset transfers or canister calls in response to user actions.

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

*   [icrc-ledger-types](https://docs.rs/icrc-ledger-types): Types for interacting with the ICRC ledger standard.
    
*   [ic-cdk](https://docs.rs/ic-cdk): Internet Computer canister development kit for Rust.