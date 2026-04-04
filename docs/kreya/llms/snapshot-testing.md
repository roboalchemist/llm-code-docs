# Source: https://kreya.app/docs/scripting-and-tests/tests/snapshot-testing.md

# Snapshot tests [Pro / Enterprise](/pricing.md)

Snapshot tests are the easiest and most convenient way to ensure your APIs behave consistently over time. Inspired by [Jest snapshot tests](https://jestjs.io/docs/snapshot-testing), Kreya's snapshot tests let you automatically capture and compare API responses, no coding required. Simply enable snapshot testing in the Kreya settings, and responses will be automatically snapshotted and compared on each run. This makes it simple to detect unexpected changes and review them before accepting.

![Screenshot of the snapshot test mismatch](/assets/ideal-img/snapshots-mismatched.f3ae576.400.png)

If you need more control or want to snapshot custom values, you can use the advanced [`kreya.snapshot`](/docs/scripting-and-tests/general/kreya-base-script-api.md#snapshotscriptapi) API in your scripts:

```
kreya.grpc.onResponse(async msg => await kreya.snapshot.verifyObjectAsJson('response', { length: msg.value.length }));
```

On the first run, this stores a snapshot named "response". On later runs, Kreya compares the current value to the stored snapshot and fails the test if they differ.

For most users, enabling snapshot tests in the settings is all you need. For more details on snapshot scripting, see the [Kreya snapshot documentation](/docs/scripting-and-tests/general/kreya-base-script-api.md#snapshot).

## Enable snapshot testing[​](#enable-snapshot-testing "Direct link to Enable snapshot testing")

To enable snapshot testing, go to the settings tab of an operation and enable the assertions in the `Snapshot testing` section:

![Screenshot of the snapshot testing configuration](/assets/ideal-img/snapshots-config.e2649a9.400.png)

You can also enable snapshot testing for an entire project or a specific directory, see [default settings](/docs/default-settings.md) for more details.

## Deterministic tests[​](#deterministic-tests "Direct link to Deterministic tests")

For best results, your tests must be deterministic, meaning they produce the same output every time they run. Non-deterministic snapshots (e.g., those containing random or time-dependent data) do not work at all, since they change each time and will always fail. Avoid including such data in your API responses, or use scripting to normalize these values before snapshotting. Deterministic tests make it possible to spot real changes and avoid unnecessary snapshot updates.

## Scrubbers[​](#scrubbers "Direct link to Scrubbers")

Kreya automatically scrubs certain values from your snapshots to keep them stable and secure. Common dynamic values such as timestamps, the local machine name, the current username, and UUIDs are replaced with placeholders. This helps ensure that your snapshots remain consistent across different environments and test runs.

Each built-in scrubber can be enabled or disabled in the settings (see also [default / directory settings](/docs/default-settings.md)). You can also define custom regular-expression replacements to remove or normalize additional values.

Scrubbers (built-in and custom) are applied to operation-related snapshots only; they are not applied to invoker scripts. If your invoker scripts generate dynamic values, normalize them in your script before calling [`kreya.snapshot`](/docs/scripting-and-tests/general/kreya-base-script-api.md#snapshotscriptapi).

If you need to scrub additional or custom values beyond the built-ins, configure custom regex replacements in settings, or use the script snapshot API to preprocess and normalize your data before snapshotting. For example, you can remove or replace sensitive or variable fields in your script before calling [`kreya.snapshot`](/docs/scripting-and-tests/general/kreya-base-script-api.md#snapshotscriptapi).

## Treat snapshots as code[​](#treat-snapshots-as-code "Direct link to Treat snapshots as code")

Snapshots are an important part of your test suite. Treat them like code: review changes carefully, check them into version control, and keep them up to date as your APIs evolve. Reviewing snapshot diffs helps you catch unintended changes and maintain confidence in your API's behavior.

### Disable formatters[​](#disable-formatters "Direct link to Disable formatters")

Tools that rewrite files (for example Prettier) can modify Kreya-generated snapshots and cause false snapshot comparison failures. Ensure these tools ignore snapshot files.

If you use Prettier, add the following to '.prettierignore' to prevent formatting snapshots:

```
# Ignore Kreya snapshot files
*.snapshot.*
```
