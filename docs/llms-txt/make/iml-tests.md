# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/iml-tests.md

# Write IML tests

You can write tests for your custom IML functions. Use the `it` function and `asserts`.

{% tabs %}
{% tab title="Example function" %}

```javascript
function formatUsername(user) {
    if (!user || !user.firstName || !user.lastName) {
        return null;
    }
    return `${user.firstName} ${user.lastName}`;
}
```

{% endtab %}

{% tab title="Test for the function, two blocks" %}

```javascript
it("should format full name correctly", () => {
    const user = { firstName: "Jane", lastName: "Doe" };
    const result = formatUsername(user);
    assert.strictEqual(result, "Jane Doe");
});

it("should return null if last name missing", () => {
    const user = { firstName: "Jane" };
    const result = formatUsername(user);
    assert.strictEqual(result, null);
});
```

{% hint style="info" %}
The `it` function accepts exactly two parameters, the name of the test and the code to run. In this code, we can verify expected outputs using `assert.ok()` function.
{% endhint %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
When using IML functions that work with date and time, remember to set the correct `timezone` in extension settings. The accepted format is the [international time zone format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

*For example "Europe/Prague"*
{% endhint %}

### Common asserts functions

<table><thead><tr><th width="388.4444580078125" valign="top">Function</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>assert.ok(value)</code></td><td valign="top">Passes if value is truthy.</td></tr><tr><td valign="top"><code>assert.strictEqual(actual, expected)</code></td><td valign="top">Passes if actual === expected.</td></tr><tr><td valign="top"><code>assert.deepStrictEqual(actual, expected)</code></td><td valign="top">Passes if objects or arrays are deeply equal.</td></tr><tr><td valign="top"><code>assert.notStrictEqual(actual, expected)</code></td><td valign="top">Passes if values are not strictly equal.</td></tr><tr><td valign="top"><code>assert.throws(fn, [error])</code></td><td valign="top">Passes if the function throws an error.</td></tr><tr><td valign="top"><code>assert.doesNotThrow(fn)</code></td><td valign="top">Passes if the function does not throw an error.</td></tr><tr><td valign="top"><code>assert.match(string, regex)</code></td><td valign="top">Passes if the string matches the regex.</td></tr><tr><td valign="top"><code>assert.doesNotMatch(string, regex)</code></td><td valign="top">Passes if the string does not match the regex.</td></tr></tbody></table>

## Run a test

To run a test on a specific function, right-click the function name in the tree and select **Run IML test.**

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4ab0d2b74cadf0cf1c107d83ce0a7082c74e71b5%2FScreen%20Shot%202022-08-22%20at%2014.18.24.png?alt=media" alt="Run IML test option" width="563"></div>

The test starts and the output is in the **IML tests** output channel.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-093fe4924efda0ab89cef9b73d10c96e57f3f49a%2Ftests_result.png?alt=media" alt="" width="563"></div>
