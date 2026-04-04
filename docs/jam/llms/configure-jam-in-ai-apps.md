# Source: https://jam.dev/docs/guides/tutorials/configure-jam-in-ai-apps.md

# Configure Jam in AI Apps

With Jam you can create a perfect bug report in just one click, automatically capturing detailed logs from your AI app so engineers can pinpoint and resolve issues fast.&#x20;

### Here's how to use Jam for AI apps

#### Jam.Metadata

Use [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") to log parameters such as temperature, max token length, context window size, or any custom settings you need.

**How it helps:**&#x20;

* **Version & configuration consistency:** identify changes that cause unexpected AI behavior, such as modifying temperature settings unintentionally or deploying a beta system prompt. You can easily get version numbers, system prompts, and configuration settings with every bug report.&#x20;

<figure><img src="https://1301043760-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2uHTnjhJbqxe3DyUE8c0%2Fuploads%2Fuz2jyu2g4J23YMxph5By%2Fimage.png?alt=media&#x26;token=1dcc65c1-c5e9-45fc-a513-6f56aab67ade" alt=""><figcaption></figcaption></figure>

#### Instant replay

Use [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") to catch nondeterministic bugs, in cases when a model provides incorrect responses, or hallucinations.&#x20;

**How it helps:**&#x20;

* **Context drift:** AI apps sometimes lose track of earlier context, leading to inconsistent or irrelevant outputs. Use instant replay to capture this behavior so engineers can pinpoint when and where the conversation deviates.
* **Error and exception details:** AI app bots can sometimes fail to return a response and instead output a generic error message. With instant replay you can automatically capture a bug that just happened, without having to reproduce it again, and engineers get all technical details they need to debug.&#x20;

*Bonus: with* [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") *you get automatic repro steps, and engineers always get a useful ticket.*&#x20;

<figure><img src="https://1301043760-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2uHTnjhJbqxe3DyUE8c0%2Fuploads%2FFn43eP5zkUQi1CG1DcEj%2FIR-for-AI.gif?alt=media&#x26;token=29fea20a-cf62-455f-b87c-edfe6928cfe5" alt="" width="563"><figcaption></figcaption></figure>

#### DevTools

Engineers get full stack trace and console logs with [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") so they can quickly identify the cause for specific issues in your AI app.&#x20;

**How it helps:**&#x20;

* **Output variability & latency:** when an AI app returns inconsistent responses, the captured console and network logs can reveal if unexpected API responses or token limits are affecting performance.

<figure><img src="https://1301043760-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2uHTnjhJbqxe3DyUE8c0%2Fuploads%2F8nH4PIuKI9aZv1a33WLP%2Fimage.png?alt=media&#x26;token=7d5c7768-f8b5-44b9-9fff-326703cb5330" alt="" width="563"><figcaption></figcaption></figure>

#### Backend logs

Use Jam's [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") integration to automatically capture server-side errors, so engineers can quickly diagnose issues such as rate limiting or misconfigured API endpoints.&#x20;

**How it helps:**&#x20;

* **Backend diagnostics:** when your AI app’s backend encounters issues (like HTTP 503 errors or timeouts during LLM API calls), these errors are logged and attached to the bug report.&#x20;

<figure><img src="https://1301043760-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2uHTnjhJbqxe3DyUE8c0%2Fuploads%2F3Xx3rpmQva74H62g3AIc%2Fimage%20(3).png?alt=media&#x26;token=b0597fc4-93fa-42f3-918e-06d017605854" alt="" width="563"><figcaption></figcaption></figure>

#### Screen recording&#x20;

Use [Broken link](https://jam.dev/docs/guides/tutorials/broken-reference "mention") to capture the intermediate step the AI takes while reasoning.&#x20;

**How it helps:**&#x20;

* **Chain-of-thought debugging:** in cases when answers are incorrect or incomplete, by capturing the reasoning state engineers can review the steps taken by the model.

If we can help you configure Jam for your AI app, [DM us on X](https://x.com/jamdotdev) or [reach out to our team](https://jam.dev/contact-sales).&#x20;
