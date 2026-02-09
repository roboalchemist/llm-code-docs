# Source: https://docs.zapier.com/platform/build-cli/faqs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Frequently Asked Questions

### Why doesn't Zapier support newer versions of Node.js?

We run your code on AWS Lambda, which only supports a few [versions](https://docs.aws.amazon.com/lambda/latest/dg/programming-model.html) of Node. Sometimes that doesn't include the latest version. Additionally, with thousands of integrations running on the Zapier platform, we have to be sure upgrading to the latest Node version will not have a negative impact.

### How do I manually set the Node.js version to run my integration with?

Update your `zapier-platform-core` dependency in `package.json`. Each major version ties to a specific version of Node.js. You can find the mapping [here](https://github.com/zapier/zapier-platform/blob/main/packages/cli/src/version-store.js). We only support the version(s) supported by [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/programming-model.html).

**IMPORTANT CAVEAT:** AWS periodically deprecates Node versions as they reach EOL. They announce this [on their blog](https://aws.amazon.com/blogs/developer/node-js-6-is-approaching-end-of-life-upgrade-your-aws-lambda-functions-to-the-node-js-10-lts/). Similar info and dates are available on [github](https://github.com/nodejs/Release). Well before this date, we'll have a version of `core` that targets the newer Node version.

If you don't upgrade before the cutoff date, there's a chance that AWS will throw an error when attempting to run your integration's code. If that's the case, we'll instead run it under the oldest Node version still supported. All that is to say, **we may run your code on a newer version of Node.js than you intend** if you don't update your integration's dependencies periodically.

### Does Zapier support XML (SOAP) APIs?

Not natively, but it can! Users have reported that the following `npm` modules are compatible with the CLI Platform:

* [pixl-xml](https://github.com/jhuckaby/pixl-xml)
* [xml2js](https://github.com/Leonidas-from-XIV/node-xml2js)
* [fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser)

Since core v10, it's possible for [shorthand requests](/platform/build-cli/overview#shorthand-http-requests) to parse XML. Use an `afterResponse` [middleware](/platform/build-cli/overview#using-http-middleware) that sets `response.data` to the parsed XML:

```js  theme={null}
const xml = require("pixl-xml");

const App = {
  // ...
  afterResponse: [
    (response, z, bundle) => {
      // Only works on core v10+!
      response.throwForStatus();
      response.data = xml.parse(response.content);
      return response;
    },
  ],
  // ...
};
```

<a id="paging" />

### What's the deal with pagination? When is it used and how does it work?

Moved to [paging](/platform/build-cli/overview#paging).

<a id="dedup" />

### How does deduplication work?

Each time a polling Zap runs, Zapier extracts a unique "primary key" for each item in the response. Zapier needs to decide which of the items should trigger the Zap. To do this, we compare the primary keys to all those we've seen before, trigger on new objects, and update the list of seen primary keys. When a Zap is turned on, we initialize the list of seen primary keys with a single poll. When it's turned off, we clear that list. For this reason, it's important that calls to a polling endpoint always return the newest items.

For example, the initial poll returns objects 4, 5, and 6 (where a higher primary key is newer). If a later poll increases the limit and returns objects 1-6, then 1, 2, and 3 will be (incorrectly) treated like new objects.

By default, the primary key is the item's `id` field. Since v15.6.0, you can customize the primary key by setting `primary` to true in `outputFields`.

There's a more in-depth explanation [here](/platform/build/deduplication).

### Why are my triggers complaining if I don't provide an explicit `id` field?

For deduplication to work, we need to be able to identify and use a unique field. In older, legacy Zapier Web Builder integrations, we guessed if `id` wasn't present. In order to ensure we don't guess wrong, we now require that the developers send us an `id` field. If your objects have a differently-named unique field, feel free to adapt this snippet and ensure this test passes:

```js  theme={null}
// ...
let items = response.data.items; // or response.json.items if you're using core v9 or older
return items.map((item) => {
  item.id = item.contactId;
  return item;
});
```

Since v15.6.0, instead of using the default `id` field, you can also define one or more `outputFields` as `primary`. For example:

```js  theme={null}
{
  triggers: {
    recipe: {
      operation: {
        outputField: [
          { key: "userId", primary: true },
          { key: "slug", primary: true },
          { key: "name" },
        ];
      }
    }
  }
}
```

will tell Zapier to use `(userId, slug)` as the unique primary key to deduplicate items when running a polling trigger.

**Limitation:** The `primary` option currently doesn't support mixing top-level fields with nested fields that use double underscores in their keys. For example, if you set `primary: true` on both `id` and `user__id`, the `primary` setting on the `user__id` field will be ignored; only `id` will be used for deduplication. However, if all the `primary` fields are all nested, such as `user__id` + `user__name`, it will work as expected.

### Node X No Longer Supported

If you're seeing errors like the following:

```
InvalidParameterValueException An error occurred (InvalidParameterValueException) when calling the CreateFunction operation: The runtime parameter of nodejs6.10 is no longer supported for creating or updating AWS Lambda functions. We recommend you use the new runtime (nodejsX.Y) while creating or updating functions.
```

... then you need to update your `zapier-platform-core` dependency to a non-deprecated version that uses a newer version of Node.js. Complete the following instructions as soon as possible:

1. Edit `package.json` to depend on a later major version of `zapier-platform-core`. There's a list of all breaking changes (marked with a :exclamation:) in the corresponding changelog in [Platform News](/platform/news).
2. Increment the `version` property in `package.json`
3. Ensure you're using version `v18` (or greater) of node locally (`node -v`). Use [nvm](https://github.com/nvm-sh/nvm) to use a different one if need be.
4. Run `rm -rf node_modules && npm i` to get a fresh copy of everything
5. Run `zapier-platform test` (or deprecated `zapier test`) to ensure your tests still pass
6. Run `zapier-platform push` (or deprecated `zapier push`)
7. Run `zapier-platform promote YOUR_NEW_VERSION` (or deprecated `zapier promote YOUR_NEW_VERSION`) (from step 2)
8. Migrate your users from the previous version (`zapier migrate OLD_VERSION YOUR_NEW_VERSION`)

<a id="analytics" />

### What Analytics are Collected?

Starting with v8.4.0, Zapier collects information about each invocation of the CLI tool.

This data is collected purely to improve the CLI experience and will **never** be used for advertising or any non-product purpose. There are 3 collection modes that are set on a per-computer basis.

**Anonymous**

When you run a command with analytics in `anonymous` mode, the following data is sent to Zapier:

* which command you ran
* if that command is a known command
* how many arguments you supplied (but not the contents of the arguments)
* which flags you used (but not their contents)
* the version of CLI that you're using
* the integration app the CLI commands are run in

**Enabled** (the default)

When analytics are fully `enabled`, the above is sent, plus:

* your operating system (the result of calling [`process.platform`](https://nodejs.org/api/process.html#process_process_platform))
* your Zapier user id

**Disabled**

Lastly, analytics can be `disabled` entirely, either by running `zapier analytics --mode disabled` or setting the `DISABLE_ZAPIER_ANALYTICS` environment variable to `1`.

We take great care not to collect any information about your filesystem or anything otherwise secret. You can see exactly what's being collecting at runtime by prefixing any command with `DEBUG=zapier:analytics`.

### What's the Difference Between an "App" and an "Integration"?

We're in the process of doing some renaming across our Zapier marketing terms. Eventually we'll use "integration" everywhere. Until then, know that these terms are interchangeable and describe the code that you write that connects your API to Zapier.

### What does performGet do?

The `performGet` method is an optional feature in Zapier that allows you to retrieve detailed information about an object. For instance, if your `create` action's `perform` method only returns the new object's `ID`, you can use `performGet` to fetch the object's full properties using that `ID`.
`performGet` is only available for `Create` or `Search` actions and is most useful when the initial `perform` result is limited, and additional information is needed.
The results from `perform` are automatically passed to `performGet` via `bundle.inputData` each time the `create` or `search` runs, allowing you to retrieve more comprehensive details.
It's important to note that `performGet` is only invoked when the result returned by `perform` is not empty.
