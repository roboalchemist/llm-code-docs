# Source: https://docs.near.org/tutorials/examples/xcc.md

---
id: xcc
title: Cross Contract Call
description: "Learn how to perform a basic cross-contract call on NEAR to set and retrieve greetings."
---





This example performs the simplest cross-contract call possible: it calls our [Hello NEAR](https://github.com/near-examples/hello-near-examples) example to set and retrieve a greeting.
It is one of the simplest examples on making a cross-contract call, and the perfect gateway to the world of interoperative contracts.

:::info Advanced Cross-Contract Calls
Check the tutorial on how to perform cross-contract calls [in batches and in parallel](./advanced-xcc)
:::

---

## Clone the Example

You have two options to start the project:

1. You can use the app through `Github Codespaces`, which will open a web-based interactive environment.
2. Clone the repository locally and use it from your computer.

| Codespaces                                                                                                                                      | Clone locally                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/near-examples/cross-contract-calls?quickstart=1) | 🌐 `https://github.com/near-examples/cross-contract-calls` |

---

## Structure of the Example

The smart contract is available in two flavors: Rust and JavaScript

<Tabs groupId="code-tabs">

  <TabItem value="js" label="🌐 JavaScript">

```bash
┌── sandbox-ts # sandbox testing
│    ├── hello-near
│    │    └── hello-near.wasm
│    └── main.ava.ts
├── src # contract's code
│    └── contract.ts
├── package.json
├── README.md
└── tsconfig.json
```

  </TabItem>

  <TabItem value="rust" label="🦀 Rust">

```bash
┌── tests # sandbox testing
│    ├── hello-near
│    │    └── hello-near.wasm
│    └── tests.rs
├── src # contract's code
│    ├── external.rs
│    └── lib.rs
├── Cargo.toml # package manager
├── README.md
└── rust-toolchain.toml
```

  </TabItem>

</Tabs>

---

## Smart Contract

The contract exposes methods to query the greeting and change it. These methods do nothing but calling `get_greeting` and `set_greeting` in the `hello-near` example.

<hr class="subsection" />

### Querying for the Greeting

The contract performs a cross-contract call to `hello.near-example.testnet` to get the greeting message, and then handles the response in a **callback function**.

<Tabs>
  <TabItem value="js" label="🌐 JavaScript">
    ```
  @call({})
  query_greeting(): NearPromise {
    const promise = NearPromise.new(this.hello_account)
      .functionCall("get_greeting", NO_ARGS, NO_DEPOSIT, THIRTY_TGAS)
      .then(
        NearPromise.new(near.currentAccountId())
          .functionCall(
            "query_greeting_callback",
            NO_ARGS,
            NO_DEPOSIT,
            THIRTY_TGAS,
          ),
      );

    return promise.asReturn();
  }

```
  </TabItem>
  <TabItem value="rust" label="🦀 Rust (low level)">
    ```
impl Contract {
    // Public - query external greeting
    pub fn ll_query_greeting(&self) -> Promise {
        // Create a promise to call HelloNEAR.get_greeting()
        let hello_promise = Promise::new(self.hello_account.clone()).function_call(
            "get_greeting".to_owned(),
            NO_ARGS,
            NO_DEPOSIT,
            TEN_TGAS,
        );

        hello_promise.then(
            // Create a promise to callback query_greeting_callback
            Self::ext(env::current_account_id())
                .with_static_gas(TEN_TGAS)
                .ll_query_greeting_callback(),
        )
    }

```
  </TabItem>
  <TabItem value="rust-hl" label="🦀 Rust (high level)">
    ```
    pub fn hl_query_greeting(&self) -> Promise {
        // Create a promise to call HelloNEAR.get_greeting()
        let promise = hello_near::ext(self.hello_account.clone())
            .with_static_gas(FIVE_TGAS)
            .get_greeting();

        promise.then(
            // Create a promise to callback query_greeting_callback
            Self::ext(env::current_account_id())
                .with_static_gas(FIVE_TGAS)
                .hl_query_greeting_callback(),
        )
    }

```

    Which requires you to define the external contract interface:

    ```
#[ext_contract(hello_near)]
trait HelloNear {
    fn get_greeting(&self) -> String;
    fn set_greeting(&self, greeting: String);
}

```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Callback Function

The callback function processes the result of the cross-contract call. In this case, it simply returns the greeting message obtained from the `hello-near` contract.

Notice that the callback function is marked as **private**, meaning it can only be called by the contract itself.

<Tabs>
  <TabItem value="js" label="🌐 JavaScript">
    ```
  @call({ privateFunction: true })
  query_greeting_callback(): String {
    let { result, success } = promiseResult();

    if (success) {
      return result.substring(1, result.length - 1);
    } else {
      near.log("Promise failed...");
      return "";
    }
  }

```
  </TabItem>
  <TabItem value="rust" label="🦀 Rust">
    ```
    #[private] // Public - but only callable by env::current_account_id()
    pub fn ll_query_greeting_callback(
        &self,
        #[callback_result] call_result: Result<String, PromiseError>,
    ) -> String {
        // Check if the promise succeeded by calling the method outlined in external.rs
        if call_result.is_err() {
            log!("There was an error contacting Hello NEAR");
            return "".to_string();
        }

        // Return the greeting
        let greeting: String = call_result.unwrap();
        greeting
    }

```
  </TabItem>
</Tabs>

---

## Testing the Contract

The contract readily includes a set of unit and sandbox testing to validate its functionality. To execute the tests, run the following commands:

<Tabs groupId="code-tabs">
  <TabItem value="js" label="🌐 JavaScript">

  ```bash
  cd contract-simple-ts
  yarn
  yarn test
  ```

  </TabItem>
  <TabItem value="rust" label="🦀 Rust">

  ```bash
  cd contract-simple-rs
  cargo test
  ```
  </TabItem>

</Tabs>

:::tip
The `integration tests` use a sandbox to create NEAR users and simulate interactions with the contract.
:::

In this project in particular, the integration tests first deploy the `hello-near` contract. Then,
they test that the cross-contract call correctly sets and retrieves the message. You will find the integration tests
in `sandbox-ts/` for the JavaScript version and in `tests/` for the Rust version.

<CodeTabs>
  <Language value="js" language="js">
    ```
test.beforeEach(async (t) => {
  // Create sandbox, accounts, deploy contracts, etc.
  const worker = t.context.worker = await Worker.init();
  
  // Get root account
  const root = worker.rootAccount;

  // Create test accounts
  const alice = await root.createSubAccount("alice");
  const xcc = await root.createSubAccount("xcc");
  const helloNear = await root.createSubAccount("hello-near");

  // Deploy the hello near contract
  await helloNear.deploy("./sandbox-ts/hello-near/hello-near.wasm");

  // Deploy the xcc contract
  await xcc.deploy(process.argv[2]);
  await xcc.call(xcc, "init", { hello_account: helloNear.accountId });

  // Save state for test runs, it is unique for each test
  t.context.accounts = { root, alice, xcc, helloNear };
});

test.afterEach.always(async (t) => {
  // Stop Sandbox server
  await t.context.worker.tearDown().catch((error) => {
    console.log('Failed to stop the Sandbox:', error);
  });
});

test("returns the default greeting", async (t) => {
  const { xcc, alice } = t.context.accounts;
  const greeting = await alice.call(xcc, "query_greeting", {}, { gas: "200000000000000" });
  t.is(greeting, 'Hello');
});

test("change the greeting", async (t) => {
  const { xcc, alice } = t.context.accounts;

  const howdyChangingResult = await alice.call(xcc, "change_greeting", { new_greeting: "Howdy" }, { gas: "200000000000000" });
  t.is(howdyChangingResult, true);

  const howdyResult = await alice.call(xcc, "query_greeting", {}, { gas: "200000000000000" });
  t.is(howdyResult, 'Howdy');
});
```
  </Language>
  <Language value="rust" language="rust">
    ```
#[tokio::test]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let worker = near_workspaces::sandbox().await?;

    // Build and deploy hello contract
    let hello_contract_wasm = near_workspaces::compile_project("./tests/hello-near").await?;
    let hello_contract: Contract = worker.dev_deploy(&hello_contract_wasm).await?;

    // Deploy contract for testing
    let contract_wasm = near_workspaces::compile_project("./").await?;
    let contract = worker.dev_deploy(&contract_wasm).await?;

    // Create accounts
    let account = worker.dev_create_account().await?;
    let alice = account
        .create_subaccount("alice")
        .initial_balance(NearToken::from_near(30))
        .transact()
        .await?
        .into_result()?;

    // Init contract
    let _ = contract
        .call("init")
        .args_json(json!({ "hello_account": hello_contract.id() }))
        .transact()
        .await?
        .into_result()?;

    // Begin tests
    test_hl_default_greeting(&alice, &contract).await?;
    test_hl_change_greeting(&alice, &contract).await?;
    test_ll_change_greeting(&alice, &contract).await?;
    Ok(())
}

async fn test_hl_default_greeting(
    user: &Account,
    contract: &Contract,
) -> Result<(), Box<dyn std::error::Error>> {
    let greeting: String = user
        .call(contract.id(), "hl_query_greeting")
        .args_json(json!({}))
        .max_gas()
        .transact()
        .await?
        .json()?;

    assert_eq!(greeting, "Hello".to_string());
    Ok(())
}

async fn test_hl_change_greeting(
    user: &Account,
    contract: &Contract,
) -> Result<(), Box<dyn std::error::Error>> {
    let result: bool = user
        .call(contract.id(), "hl_change_greeting")
        .args_json(json!({ "new_greeting": "Howdy" }))
        .max_gas()
        .transact()
        .await?
        .json()?;

    assert!(result);

    let greeting: String = user
        .call(contract.id(), "hl_query_greeting")
        .args_json(json!({}))
        .max_gas()
        .transact()
        .await?
        .json()?;

    assert_eq!(greeting, "Howdy".to_string());
```
  </Language>
</CodeTabs>


<hr class="subsection" />

### Deploying the Contract to the NEAR network

In order to deploy the contract you will need to create a NEAR account.

<Tabs groupId="cli-tabs">
  <TabItem value="short" label="Short">

  ```bash
  # Create a new account pre-funded by a faucet
  near create-account <accountId> --useFaucet
  ```
  </TabItem>

  <TabItem value="full" label="Full">

  ```bash
  # Create a new account pre-funded by a faucet
  near account create-account sponsor-by-faucet-service <my-new-dev-account>.testnet autogenerate-new-keypair save-to-keychain network-config testnet create
  ```
  </TabItem>
</Tabs>

Go into the directory containing the smart contract (`cd contract-advanced-ts` or `cd contract-advanced-rs`), build and deploy it:

<Tabs groupId="code-tabs">

  <TabItem value="js" label="🌐 JavaScript">

    ```bash
    npm run build
    near deploy <accountId> ./build/cross_contract.wasm --initFunction new --initArgs '{"hello_account":"hello.near-example.testnet"}'
    ```

  </TabItem>
  <TabItem value="rust" label="🦀 Rust">
  
  ```bash
  cargo near deploy build-non-reproducible-wasm <accountId> with-init-call new json-args '{"hello_account":"hello.near-example.testnet"}' prepaid-gas '100.0 Tgas' attached-deposit '0 NEAR' network-config testnet sign-with-keychain send

  ```

  </TabItem>

</Tabs>

<hr class="subsection" />

### CLI: Interacting with the Contract

To interact with the contract through the console, you can use the following commands:

<Tabs groupId="cli-tabs">
  <TabItem value="short" label="Short">

  ```bash
  # Get message from the hello-near contract
  # Replace <accountId> with your account ID
  near call <accountId> query_greeting --useAccount <accountId>

  # Set a new message for the hello-near contract
  # Replace <accountId> with your account ID
  near call <accountId> change_greeting '{"new_greeting":"XCC Hi"}' --useAccount <accountId>
  ```
  </TabItem>

  <TabItem value="full" label="Full">

  ```bash
  # Get message from the hello-near contract
  # Replace <accountId> with your account ID
  near contract call-function as-transaction <accountId> query_greeting json-args '{}' prepaid-gas '100.0 Tgas' attached-deposit '0 NEAR' sign-as <accountId> network-config testnet sign-with-keychain send

  # Set a new message for the hello-near contract
  # Replace <accountId> with your account ID
  near contract call-function as-transaction <accountId> change_greeting json-args '{"new_greeting":"XCC Hi"}' prepaid-gas '100.0 Tgas' attached-deposit '0 NEAR' sign-as <accountId> network-config testnet sign-with-keychain send
  ```
  </TabItem>
</Tabs>

---

## Moving Forward

A nice way to learn is by trying to expand a contract. Modify the cross contract example to use the [guest-book](https://github.com/near-examples/guest-book-examples)
contract!. In this way, you can try to make a cross-contract call that attaches money. Remember to correctly [handle the callback](/smart-contracts/anatomy/crosscontract#callback-function),
and to return the money to the user in case of error.

### Advanced Cross Contract Calls

Your contract can perform multiple cross-contract calls in simultaneous, creating promises that execute in parallel, or as a batch transaction. Check the [advanced cross contract calls
tutorial](./advanced-xcc) to learn more.

<MovingForwardSupportSection />

:::note Versioning for this article

At the time of this writing, this example works with the following versions:

- near-cli: `4.0.13`
- node: `18.19.1`
- rustc: `1.77.0`

:::
