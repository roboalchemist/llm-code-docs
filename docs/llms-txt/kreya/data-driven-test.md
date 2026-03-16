# Source: https://kreya.app/docs/scripting-and-tests/samples/data-driven-test.md

# Data driven testing [Pro / Enterprise](/pricing.md)

Run one (or many) Kreya operations against a list of different inputs and assert the responses. This pattern is useful for:

* Verifying lots of simple variations (happy path + edge cases) fast
* Keeping test data outside of scripts so it is easy to review and extend
* Re‑using the same assertion logic while only swapping inputs/expected outputs

## Test data file[​](#test-data-file "Direct link to Test data file")

In this sample we use a simple `Greet` operation that takes a name and returns a greeting message. We want to verify that the greeting is correct for various names (normal, empty, special characters, etc.). To describe the test cases we use a JSON file containing an array with arbitrary fields for `input` and `expectedOutput`, plus a human‑readable `name` used as the test name.

greet-test-data.json

```
[
  {
    "name": "Regular",
    "input": { "name": "Peter" },
    "expectedOutput": { "greeting": "Hello Peter" }
  },
  {
    "name": "Empty Name",
    "input": { "name": "" },
    "expectedOutput": { "greeting": "Hello " }
  },
  {
    "name": "Single Character",
    "input": { "name": "A" },
    "expectedOutput": { "greeting": "Hello A" }
  },
  {
    "name": "Whitespace Name",
    "input": { "name": "   " },
    "expectedOutput": { "greeting": "Hello    " }
  },
  {
    "name": "Name With Spaces",
    "input": { "name": "John Doe" },
    "expectedOutput": { "greeting": "Hello John Doe" }
  },
  {
    "name": "Name With Special Characters",
    "input": { "name": "@lice#123" },
    "expectedOutput": { "greeting": "Hello @lice#123" }
  },
  {
    "name": "Unicode Characters",
    "input": { "name": "Élise" },
    "expectedOutput": { "greeting": "Hello Élise" }
  },
  {
    "name": "Long Name",
    "input": { "name": "ThisIsAVeryLongNameToTestTheAPIHandling" },
    "expectedOutput": { "greeting": "Hello ThisIsAVeryLongNameToTestTheAPIHandling" }
  }
]
```

## Operation and assertion[​](#operation-and-assertion "Direct link to Operation and assertion")

Create a Kreya operation named `Greet` and calls the gRPC method we want to test. Set the `name` field in the request from a user variable (`{{ vars.name }}`).

request.json

```
{
  "name": "{{ vars.testCase.input.name }}"
}
```

Add a script to assert the response. This script runs for every invocation of the operation.

Operation script

```
import { expect } from 'chai';

kreya.grpc.onResponse(msg => {
  const testCase = kreya.variables.get('testCase');
  kreya.test(testCase.name, () => expect(msg.content.message).to.eql(testCase.expectedOutput.greeting));
});
```

This script:

1. Listens for the response (`kreya.grpc.onResponse`, use the protocol-specific equivalent hook for other protocols).
2. Defines a test with the dynamic test name stored in user variables.
3. Compares the actual response field with the expected value (also stored in user variables).

## Orchestrator script[​](#orchestrator-script "Direct link to Orchestrator script")

Add a Kreya script named `GreetTest` that orchestrates the data-driven test. Reads the JSON file, iterates test cases, sets the user variable, and invokes the operation once per test case.

GreetTest

```
import { readFile } from 'fs/promises';

const content = await readFile('./greet-test-data.json', 'utf-8');
const testCases = JSON.parse(content);

for (const testCase of testCases) {
  // Set variable consumed by the operation script
  kreya.variables.set('testCase', testCase);

  // Invoke the operation (relative path to the saved operation in the project tree)
  await kreya.invokeOperation('./Greet');
}
```

Notes:

* `./Greet` must match the operation’s relative path (e.g. if nested deeper, adjust the path).
* Any variables you set here are accessible in the operation script via `kreya.variables.get(...)`.

## Running the test suite[​](#running-the-test-suite "Direct link to Running the test suite")

1. Open the `GreetTest` script in Kreya.
2. Run it. Each JSON entry becomes an individual test in the results panel.
3. Add / change rows in `greet-test-data.json` to extend coverage. Re-run the script, no code changes needed.

If a response differs, the failing test clearly shows the test name you set (`name` in the JSON). That makes it easy to track which row needs an update.

## How it works (flow)[​](#how-it-works-flow "Direct link to How it works (flow)")

1. Orchestrator script loads structured test data.
2. For each row it sets the test case as a user variable.
3. It invokes the operation.
4. The operation-level script waits for the response and creates a test.
5. Kreya aggregates all created tests and reports success/failure.

## Related[​](#related "Direct link to Related")

* Scripting overview: [Scripting and tests](/docs/scripting-and-tests.md)
* Invoker scripts API: [Scripts API reference](/docs/scripting-and-tests/invoker-scripts/api-reference.md)
* Example project: [Kreya example project on GitHub](https://github.com/riok/Kreya) (see `example-project/Kreya features/UseCases/DataDrivenTesting`)
