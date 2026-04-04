# Source: https://kreya.app/docs/scripting-and-tests/tests/scripting-tests.md

# Scripting tests [Pro / Enterprise](/pricing.md)

For more advanced or custom assertions, you can use the [`kreya.test`](/docs/scripting-and-tests/general/kreya-base-script-api.md#test) scripting function. This function is available in both Kreya [operation scripts](/docs/scripting-and-tests/operation-scripts.md) and Kreya [scripts](/docs/scripting-and-tests/invoker-scripts.md). These tests also run as part of a collection.

The `kreya.test` function accept a name and a boolean indicating whether the test was successful or a callback which can be used to run more complex assertions. Any callback returning false or throwing an error is considered a test failure. The popular [Chai](https://www.chaijs.com/) assertion library comes bundled with Kreya and allows complex assertions in the test callbacks.

Here are some examples:

* Boolean assertions
* Chai assertions

```
// as simple boolean results
kreya.test('test that will fail', 2 >= 3);
kreya.test('test that will succeed', 6 === 6);

// or as callbacks
kreya.test('test that will fail', () => 2 >= 3);
kreya.test('test that will succeed', () => 6 === 6);
```

```
import { expect } from 'chai'; // Chai is pre-installed in Kreya

kreya.test('test that will fail', () => expect(2).to.eql(3));
kreya.test('test that will succeed', () => expect(6).to.eql(6));
```

You can combine snapshot and scripting assertions in the same script:

```
import { expect } from 'chai';

kreya.snapshot.verifyObjectAsJson('response', responseData);

kreya.rest.onCallCompleted(ctx => {
  kreya.test('status code is 200', () => {
    expect(ctx.status.code).to.eql(200);
  });
});
```

While these examples are simple, you can create more realistic tests by referencing the [gRPC](/docs/scripting-and-tests/operation-scripts/grpc-script-api-reference.md) or [REST](/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md) examples.

![Viewing scripted Kreya test results](/assets/ideal-img/viewing-scripting-tests.c4d8e3c.400.png)
