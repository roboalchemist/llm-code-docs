# Source: https://developers.make.com/custom-apps-documentation/app-components/base/sanitization.md

# Sanitization

Sanitization protects sensitive data (passwords, secret keys, etc.) from leakage.

You should always [sanitize the log](https://developers.make.com/custom-apps-documentation/component-blocks/api/making-requests#log) so no personal tokens and/or keys are leaked.

If you don't use sanitization, the request and response logs will not be available in the [console](https://developers.make.com/custom-apps-documentation/debug-your-app/make-devtool).

{% tabs %}
{% tab title="With correct sanitization" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-5ae4e0155c333a37838bd114a871f689e31b3408%2Fcorrect_sanitization.png?alt=media" alt="Example of a log from the console with a sanitized access token" width="418"></div>

```json
...
"log": {
        "sanitize": ["request.headers.accesstoken"]
    }
...
```

{% hint style="info" %}
`Accesstoken` is correctly mapped, so it's not exposed.
{% endhint %}
{% endtab %}

{% tab title="Without sanitization" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-afc794842de2c1ef2a3706b910db1ac50321ba6f%2Fsanitization_without.png?alt=media" alt="Output from the Scenario Debugger" width="277"></div>

{% hint style="info" %}
Without sanitization, there isn't a log in the list of executions in Live Stream.

Additionally there will be no shown log in the Scenario Debugger, as shown in the screenshot above.

Neither the developer nor user can see the original request and respond to debug possible issues.
{% endhint %}
{% endtab %}

{% tab title="With incorrect sanitization" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-619c789dac4822a4f046bcb0c08036af0867c44a%2Fincorrect_sanitization.png?alt=media" alt="Example of a log from the console with an exposed access token" width="418"></div>

```json
...
"log": {
        "sanitize": ["request.headers.token"]
    }
...
```

{% hint style="info" %}
Notice, the `accesstoken` was mistaken for `token`. Therefore the `accesstoken` was exposed in the log.
{% endhint %}
{% endtab %}
{% endtabs %}
