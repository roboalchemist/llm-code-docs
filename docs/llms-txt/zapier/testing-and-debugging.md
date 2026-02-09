# Source: https://docs.zapier.com/platform/build-cli/testing-and-debugging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing and debugging

> Test your integration using `invoke` command and unit tests. Debug locally using a step-by-step debugger.

There are several ways to test your Zapier integration:

* You can use the `zapier-platform invoke` command to invoke a trigger, search, create, or an authentication method locally or remotely.
* You can write unit tests for your Zapier integration that run locally, outside of the Zapier editor.
* You can run these tests in a CI tool like [Travis](https://travis-ci.com/).

### Using `zapier-platform invoke` Command

*Added in v15.17.0.*

The `zapier-platform invoke <ACTION_TYPE> <ACTION_KEY>` CLI command emulates how the Zapier production environment would invoke your integration. Since it runs code locally, it's a fast way to debug and test interactively without needing to deploy the code to Zapier.

Its general execution flow involves calling `operation.inputFields` of an action, resolving the input data to the expected types, and then calling the `operation.perform` method.

[`zapier-platform invoke --help`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#invoke) has detailed documentation, but here's a quick rundown:

```bash  theme={null}
# Initialize auth data in .env file locally
zapier-platform invoke auth start

# Refresh auth data (for OAuth2 or Session auth)
zapier-platform invoke auth refresh

# Test your auth data in .env
zapier-platform invoke auth test
zapier-platform invoke auth label

# Invoke a polling trigger
zapier-platform invoke trigger new_recipe

# Invoke a create action
zapier-platform invoke create add_recipe --inputData '{"name": "Pancakes"}'
zapier-platform invoke create add_recipe --inputData @file.json
```

Starting in v18.1.0, you can use `zapier-platform invoke --remote` (or `-r`) to invoke your integration code remotely in Zapier's production environment.

```bash  theme={null}
# Invoke your integration code remotely (will ask you which action to run)
zapier-platform invoke -r

# Test auth data remotely (will ask you to select a connected account)
zapier-platform invoke -r auth test

# Invoke a polling trigger remotely
zapier-platform invoke -r trigger new_recipe
```

### Writing Unit Tests

From v10 of `zapier-platform-cli`, we recommend using the [Jest](https://jestjs.io/) testing framework. After running `zapier-platform init` you should find an example test to start from in the `test` directory.

<Info>
  Before v10, `zapier-platform init` project templates used [Mocha](https://mochajs.org/) for the test framework. Now we recommend Jest.
</Info>

```js  theme={null}
/* globals describe, expect, test */

const zapier = require("zapier-platform-core");

// createAppTester() makes it easier to test your integration. It takes your raw app
// definition, and returns a function that will test you integration.
const App = require("../index");
const appTester = zapier.createAppTester(App);

// Inject the vars from the .env file to process.env. Do this if you have a .env
// file.
zapier.tools.env.inject();

describe("triggers", () => {
  test("new recipe", async () => {
    const bundle = {
      inputData: {
        style: "mediterranean",
      },
    };

    const results = await appTester(
      App.triggers.recipe.operation.perform,
      bundle,
    );
    expect(results.length).toBeGreaterThan(1);

    const firstRecipe = results[0];
    expect(firstRecipe.id).toBe(1);
    expect(firstRecipe.name).toBe("Baked Falafel");
  });
});
```

### Using the `z` Object in Tests

Introduced in `core@11.1.0`, `appTester` can now run arbitrary functions:

```js  theme={null}
/* globals describe, expect, test */

const zapier = require("zapier-platform-core");

const App = require("../index");
const appTester = zapier.createAppTester(App);

describe("triggers", () => {
  test("new recipe", async () => {
    const adHocResult = await appTester(
      // your in-line function takes the same [z, bundle] arguments as normal
      async (z, bundle) => {
        // requests are made using your integration's actual middleware
        // make sure to pass the normal `bundle` arg to `appTester` if your requests need auth
        const response = await z.request(
          "https://example.com/some/setup/method",
          {
            params: {
              numItems: bundle.inputData.someValue,
            },
          },
        );

        return {
          // you can use all the functions on the `z` object
          someHash: z.hash("md5", "mySecret"),
          data: response.data,
        };
      },
      {
        // you must provide auth data for authenticated requests
        // (just like running a normal trigger)
        authData: { token: "some-api-key" },
        // put arbitrary function params in `inputData`
        inputData: {
          someValue: 3,
        },
      },
    );

    expect(adHocResult.someHash).toEqual("a5beb6624e092adf7be31176c3079e64");
    expect(adHocResult.data).toEqual({ whatever: true });

    // ... rest of test
  });
});
```

### Mocking Requests

It's useful to test your code without actually hitting any external services. [Nock](https://github.com/node-nock/nock) is a Node.js utility that intercepts requests before they ever leave your computer. You can specify a response code, body, headers, and more. It works out of the box with `z.request` by setting up your `nock` before calling `appTester`.

```js  theme={null}
/* globals describe, expect, test */

const zapier = require("zapier-platform-core");

const App = require("../index");
const appTester = zapier.createAppTester(App);

const nock = require("nock");

describe("triggers", () => {
  test("new recipe", async () => {
    const bundle = {
      inputData: {
        style: "mediterranean",
      },
    };

    // mocks the next request that matches this url and querystring
    nock("https://example.com/api")
      .get("/recipes")
      .query(bundle.inputData)
      .reply(200, [
        { name: "name 1", directions: "directions 1", id: 1 },
        { name: "name 2", directions: "directions 2", id: 2 },
      ]);

    const results = await appTester(
      App.triggers.recipe.operation.perform,
      bundle,
    );

    expect(results.length).toBeGreaterThan(1);

    const firstRecipe = results[0];
    expect(firstRecipe.id).toBe(1);
    expect(firstRecipe.name).toBe("name 1");
  });
});
```

Here's more info about nock and its usage in the [README](https://github.com/node-nock/nock/blob/master/README.md).

### Running Unit Tests

To run all your tests do:

```bash  theme={null}
zapier-platform test
```

<Info>
  You can also go directly with `npm test` or `node_modules/.bin/jest`.
</Info>

### Testing & Environment Variables

The best way to store sensitive values (like API keys, OAuth secrets, or passwords) is in an `.env` (or `.environment`, see below note) file ([learn more](https://github.com/motdotla/dotenv#faq)). Then, you can include the following before your tests run:

```js  theme={null}
const zapier = require("zapier-platform-core");
zapier.tools.env.inject(); // inject() can take a filename; defaults to ".env"

// now process.env has all the values in your .env file
```

<Info>
  `.env` is the new recommended name for the environment file since v5.1.0. The
  old name `.environment` is deprecated but will continue to work for backward
  compatibility.
</Info>

<Info>Remember: **NEVER** add your secrets file to version control!</Info>

Additionally, you can provide them dynamically at runtime:

```bash  theme={null}
CLIENT_ID=1234 CLIENT_SECRET=abcd zapier-platform test
```

Or, `export` them explicitly and place them into the environment:

```bash  theme={null}
export CLIENT_ID=1234
export CLIENT_SECRET=abcd
zapier-platform test
```

### Testing in Your CI

Whether you use Travis, Circle, Jenkins, or another service, we aim to make it painless to test in an automated environment.

Behind the scenes `zapier-platform test` does a standard `npm test`, which could be [Jest](https://jestjs.io/) or [Mocha](https://mochajs.org/), based on your project setup.

This makes it straightforward to integrate into your testing interface. For example, if you want to test with [Travis CI](https://travis-ci.com/), the `.travis.yml` would look something like this:

```yaml  theme={null}
language: node_js
node_js:
  - "v22"
before_script: npm install -g zapier-platform-cli
script: CLIENT_ID=1234 CLIENT_SECRET=abcd zapier-platform test
```

You can substitute `zapier-platform test` with `npm test`, or a direct call to `node_modules/.bin/jest`. We recommend putting environment variables directly into the configuration screens Jenkins, Travis, or other services provide.

Alternatively to reading the deploy key from root (the default location), you may set the `ZAPIER_DEPLOY_KEY` environment variable to run privileged commands without the human input needed for `zapier-platform login`. We suggest encrypting your deploy key in the manner your CI provides (such as [these instructions](https://docs.travis-ci.com/user/environment-variables/#Defining-encrypted-variables-in-.travis.yml), for Travis).

### Debugging Tests

Sometimes tests aren't enough, and you may want to step through your code and set breakpoints. The testing suite is a regular Node.js process, so debugging it doesn't take anything special. Because we recommend `jest` for testing, these instructions will outline steps for debugging w/ jest, but other test runners will work similarly. You can also refer to [Jest's own docs on the subject](https://jestjs.io/docs/en/troubleshooting#tests-are-failing-and-you-dont-know-why).

To start, add the following line to the `scripts` section of your `package.json`:

```
"test:debug": "node --inspect-brk node_modules/.bin/jest --runInBand"
```

This will tell `node` to inspect the `jest` processes, which is exactly what we need.

Next, add a `debugger;` statement somewhere in your code, probably in a `perform` method:

```js  theme={null}
// triggers on a new pizza with a certain tag
const perform = async (z, bundle) => {
  const response = await z.request({
    url: "https://jsonplaceholder.typicode.com/posts",
    params: {
      tag: bundle.inputData.tagName,
    },
  });
  debugger;
  // this should return an array of objects
  return response.data;
};
```

This creates a *breakpoint* while `inspect`ing, or a starting point for our manual inspection.

Next, you'll need an inspection client. The most available one is probably the Google Chrome browser, but there are [lots of options](https://nodejs.org/en/docs/guides/debugging-getting-started/#inspector-clients). We'll use Chrome for this example. In your terminal (and in your integration's root directory), run `yarn test:debug` (or `npm run test:debug`). You should see the following:

```
% yarn test:debug
yarn run v1.22.10
$ node --inspect-brk node_modules/.bin/jest --runInBand
Debugger listening on ws://127.0.0.1:9229/5edaab3c-a1d3-45e4-b374-0536095c559b
For help, see: https://nodejs.org/en/docs/inspector
```

Now in Chrome, go to chrome://inspect. Make sure `Discover Network Targets` is checked and you should see a path to your `jest` file on your local machine:

![](https://cdn.zappy.app/e2836d2950e1f8a03e3621a22452c3cd.png)

Click `inspect`. A new window will open. Next, click the little blue arrow in the top right to actually run the code:

![](https://cdn.zappy.app/a64e7963a7090e9730d9c8e7b3595a6a.png)

After a few seconds, you'll see your code, the `debugger` statement, and info about the current environment on the right panel. You should see familiar data in the `Locals` section, such as the `response` variable, and the `z` object.

![](https://cdn.zappy.app/4bfdfe079a344ab7aced64ad7728bc6a.png)

Debugging combined with thorough unit tests will hopefully equip you in keeping your Zapier integration in smooth working order.
