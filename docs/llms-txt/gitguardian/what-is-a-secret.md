# Source: https://docs.gitguardian.com/secrets-detection/core-concepts/what-is-a-secret.md

# What is a secret?

> Defines what a secret is in the context of software development and explains how secrets authenticate application components.

In everyday language, a secret can be any sensitive data that we want to keep private. When discussing secrets in the context of software development, secrets generally refer to digital authentication credentials that grant access to systems or data. These are most commonly API keys, usernames and passwords, or security certificates.

Secrets exist in the context of applications that are no longer standalone monoliths. Applications nowadays rely on thousands of independent building blocks: cloud infrastructure, databases, third-party APIs and services such as Stripe, Slack, HubSpotâ¦

Secrets tie together the different building blocks of a single application by authenticating each component against one another.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3fpN-1kPcDE?controls=0&modestbranding=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

## What do secrets look like?

Secrets are typically high entropy strings which means that they are strings or text that are very random in value. Some API keys can be pre or post fix which means they share the same characters at the start or at the end of the string but most secrets arenât and are just a highly randomized value that contains different types of character.

### Examples

Below is an example of a **specific secret**, a GitHub personal access token:

```yaml
- text: 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
  apikey: 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
```

As you can notice the secret is prefixed with the `ghp` string. Below is another example of a secret, this time a **generic** one in the form of a Base64 basic auth string:

```yaml
- text: |
    "Authorization": "Basic aW50ZXJuc2hpcDpjZGk="
  username: aW50ZXJuc2hpcD # decodes to `internship`
  password: pjZGk # decodes to `cdi`
```
