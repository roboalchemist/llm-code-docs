# Source: https://docs.tabnine.com/main/getting-started/code-completion/code-acceptance-logs.md

# Code Acceptance Logs

**Code Acceptance Logging** tracks all explicit acceptances of code recommendations by the use or code recommended by Tabnine. These logs can be leveraged for compliance needs.

{% hint style="info" %}
To activate this service and access all Acceptance Logs, please contact <support@tabnine.com>.
{% endhint %}

{% hint style="info" %}
This is only available for self-hosted instances.
{% endhint %}

Accepted code may come from any of these code generation sources:

1. [Code Completions](https://docs.tabnine.com/main/getting-started/code-completion)
2. [Tabnine Chat](https://docs.tabnine.com/main/getting-started/tabnine-chat) (via Apply, insert, copy, or manual highlight-and-copy \[copy-raw])
3. [Inline Actions](https://docs.tabnine.com/main/getting-started/inline-actions)
4. [Test Agent](https://github.com/codota/docs/blob/main/main/getting-started/getting-the-most-from-tabnines-code-completion/broken-reference/README.md)
5. [Edit Agent](https://docs.tabnine.com/main/getting-started/code-completion/broken-reference) (when available)

All logs will include standard information such as:

1. The full code snippet that was accepted
2. Timestamp
3. Session ID
4. Code generation source
5. Model name
6. User ID
7. Team ID
