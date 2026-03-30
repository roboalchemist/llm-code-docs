# Source: https://help.aikido.dev/aikido-autofix/refine-autofixes-with-aikido-ai.md

# Refine AutoFixes with Aikido AI

Aikido allows to automatically fix different types of findings. The **Refine with Aikido AI** chat panel lets you iteratively adjust AutoFixes using natural language, without leaving the diff view.

#### Use Cases

AutoFix gets you most of the way there. Refinement is useful when:

* The fix is correct but doesn't match your codebase's naming conventions or patterns
* You want to add explanatory comments
* You want to include unit tests
* You want to introduce specific logic, like error handling or logging calls
* The fix needs to account for context not available to the AI
* You want to tighten scope, for example limiting what gets sanitized or validated

#### How to Refine a Fix

**Step 1.** Open the diff modal via the `View Fix` action and click `Refine with Aikido AI` in the bottom left.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FMrrgU1MpqLqNPsGQo5nB%2Fimage.png?alt=media&#x26;token=3bffb876-53e9-4d7a-9000-f2c449e36614" alt=""><figcaption></figcaption></figure>

**Step 2.** Type your instruction in the text field.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FEsCvmAwcKr35zkMg4IIX%2Fimage.png?alt=media&#x26;token=dc0a9d0a-a948-435a-a8a4-9c4797a424d6" alt=""><figcaption></figcaption></figure>

**Step 3.** The diff view updates automatically when the refined fix is ready.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FlEh9RRZHBDxVa4UgYAEl%2Fimage.png?alt=media&#x26;token=b4387775-fa98-4192-9b98-8b76b9d700ff" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Each instruction you send is retained as context for subsequent refinements, so the AI builds on prior instructions rather than starting fresh.
{% endhint %}

#### Tips for Writing Instructions

Be specific about intent, not just the symptom:

* "Thrown an exception instead of returning an empty object"
* "Rename the sanitized variable from `safe_input` to `safeInput` "
* "Add a log when the regex matches"
