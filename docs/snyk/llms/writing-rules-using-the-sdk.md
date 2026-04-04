# Source: https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk.md

# Writing rules using the SDK

To get you started with the SDK, you will learn how to:

1. [Parse a fixture file](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk/parsing-an-input-file), to help you understand how to write a rule.
2. [​Write a rule with the SDK](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk/writing-a-rule) using Rego.
3. [Add unit tests for the rules you have written](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk/testing-a-rule) to verify your rules.
4. [Build a bundle containing your custom rules](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk/bundling-rules) so that you can [use it with the Snyk CLI](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/use-iac-custom-rules-with-cli).
5. [Push the bundle containing your custom rules to a container registry](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/writing-rules-using-the-sdk/pushing-a-bundle) so that you can [enforce its usage with the Snyk CLI](https://docs.snyk.io/scan-with-snyk/snyk-iac/current-iac-custom-rules/use-iac-custom-rules-with-cli).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1e2ae32cc40396e5abfffc0fde383bfeadce427f%2Fimage%20(30).png?alt=media" alt="Development to distribution workflow"><figcaption><p>Development to distribution workflow</p></figcaption></figure>
