# Source: https://blog.nomic.foundation/solidity-vs-typescript-tests-how-to-choose-and-combine-in-hardhat-3/

Title: Solidity vs. TypeScript tests: How to choose and combine in Hardhat 3

URL Source: https://blog.nomic.foundation/solidity-vs-typescript-tests-how-to-choose-and-combine-in-hardhat-3/

Published Time: 2025-10-22T17:59:16.000Z

Markdown Content:
Testing is central to Ethereum smart contract development, as bugs and vulnerabilities can lead to catastrophic losses. Most projects tests contracts either in TypeScript or Solidity.

With **Hardhat 3**, you don’t have to choose between writing all your tests in Solidity or in TypeScript — both are first-class options, they can be combined, and each brings their unique strengths. The key is knowing where each approach fits best, and how they complement one another.

**Solidity Tests**
------------------

Writing tests directly in Solidity lets you run your contracts and tests directly on the Ethereum Virtual Machine (EVM). This approach has some clear advantages:

### **Testing in the same language**

Using the same language for contracts and tests prevents constant context switching between Solidity and Typescript. You can express your logic and tests using the same language, instead of thinking in two of them at the same time, and how things translate to each other.

### **Simpler unit tests**

Solidity tests are great for small, focused pieces of logic. Everything stays in Solidity, so you don’t need wrappers or RPC calls. Re-exporting internal or private functions for testing (e.g. via inheritance) is also straightforward when staying in the same language.

### **Faster test runs**

Solidity tests have less overhead by running directly on the EVM instead of simulating an entire blockchain. This leads to faster test runs.

### **Simpler mocking experience**

Solidity tests offer direct access to mocking contract interactions and parts of the execution environment, making some tests simpler to write.

### **Invariants and Fuzzing**

Solidity tests, being faster, are the only place where you can use built-in fuzzing and invariant testing. These are powerful tools to automatically explore unexpected states and catch edge cases.

### **Limitations of Solidity Tests**

*   They can become cumbersome for complex interactions.
*   Expressing higher-level scenarios is harder and often requires heavy mocking, which can diverge from real-world usage.
*   Cheatcodes make some things easier but also introduce “magical” helpers that don’t exist on-chain.

Solidity testing is strongest when you want **simple, fast, low-level,** tests that stay entirely inside the contract world.

**TypeScript Tests**
--------------------

TypeScript tests run your contracts in a complete simulation of a blockchain and your tests in Node.js. This brings the test environment much closer to how your contracts will be used in practice. The advantages of this approach are:

### **More expressive language**

Complex scenarios are often easier to express in a general-purpose language. Smaller tests may feel more verbose than Solidity, but for end-to-end coverage, TypeScript scales better.

### **Multi-step tests without excessive mocking**

By simulating an entire blockchain, you can tests things in multiple transactions, sent from different accounts, in different orders, or across multiple blocks. While some of this is possible in Solidity with mocking, it’s more natural and precise in TypeScript, with a blockchain-level simulation.

### **Easier interaction with offchain components**

TypeScript helps when your contracts depend on offchain systems like oracles, bots, bridges, or other services. You can simulate these interactions alongside your contracts.

### **Realistic blockchain-level tests**

TypeScript tests let you easily inspect data at the chain level — blocks, transactions, events, gas spent — and manipulate the chain (e.g. advancing time, mining blocks, forking), instead of mocking it. This is especially useful for integration tests.

### **Tests that mirror consumers**

You write tests the same way your frontend, scripts, or other contracts will interact with your system. This not only serves as validation and documentation for consumers—especially in end-to-end scenarios—but also helps you, the developer, confirm your assumptions. Writing tests from the consumer’s perspective forces you to see whether your contract’s API and usage actually match your intention.

### **Limitations of TypeScript Tests**

*   The additional stack (EVM + RPC + client library + test) adds complexity and boilerplate.
*   Tests tend to run slower compared to Solidity because of the extra overhead of simulating a more realistic environment.
*   Some tests can be harder to express compared to writing them directly in Solidity.

TypeScript tests are strongest when you want want to test **realistic or complex end-to-end scenarios**.

**Final thoughts**
------------------

With Hardhat 3, you can combine both approaches seamlessly:

*   **Solidity tests** for unit-level checks, invariants, and fuzzing.
*   **TypeScript tests** for end-to-end flows, blockchain-level tests, integrations, and consumer-facing examples.

By combining them, you get confidence both in the **internal correctness** of your contracts and in their **external behavior** in realistic scenarios.

Check out [Hardhat 3](https://hardhat.org/?ref=blog.nomic.foundation) and start testing your Solidity code in a more ergonomic and comprehensive way!
