# Source: https://docs.augmentcode.com/setup-augment/user-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Secrets Manager

> Securely store and manage secrets for your development environment, including API keys, tokens, and credentials.

export const Availability = ({tags = []}) => {
  const tagColor = {
    invite: "purple",
    beta: "gray",
    "private-preview": "purple",
    vscode: "blue",
    jetbrains: "orange",
    vim: "gray",
    neovim: "gray",
    cli: "green"
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => <Badge key={tag} size="sm" color={tagColor[tag] || "gray"}>
          {tag}
        </Badge>)}
    </div>;
};

<Availability tags={["vscode"]} />

The Secrets Manager allows you to securely store and manage user-defined secrets that can be used in your development environment. It supports two types of secrets: **Environment Variables** and **Mounted Files**.

## Overview

The Secrets Manager provides a secure way to store sensitive information like API keys, database credentials, and configuration secrets. All secrets are encrypted and stored securely, with automatic redaction in logs to prevent accidental exposure.

## Accessing the Secrets Manager

Open the Settings Panel (gear icon in the Augment panel) and navigate to the **Secrets** section to manage your secrets.

## Secret Types

### Environment Variables

Environment variables are injected into your development environment and accessible via standard environment variable access patterns.

**Use cases:**

* API keys (GitHub tokens, OpenAI keys)
* Database connection strings
* Service endpoints
* Configuration flags

**How they work:**

* Secrets are made available as environment variables in your workspace
* Generated profile script at `/etc/profile.d/15-augment-secrets.sh`
* Automatically loaded in shell sessions

### Mounted Files

Mounted files are stored as actual files in your workspace filesystem at specified paths.

**Use cases:**

* SSH private keys
* Certificate files
* Configuration files
* Large secret content

**How they work:**

* Files are mounted to `/run/augment_secrets/` by default
* You specify the mount path when creating the secret
* Files are accessible via standard filesystem operations

## Security Features

* Secret values are never displayed by default
* All secret values are redacted in logs
* Each user can only access their own secrets

## Limits and Quotas

| Limit                | Default Value  |
| -------------------- | -------------- |
| Max secrets per user | 100            |
| Max secret size      | 4KB            |
| Max name length      | 255 characters |
| Max tags per secret  | 50             |

## Security Best Practices

1. **Use descriptive names**: Make secret purposes clear without exposing sensitive info
2. **Regular cleanup**: Remove unused secrets to minimize exposure
3. **Avoid logging values**: The system automatically redacts secrets in logs
4. **Use appropriate type**: Choose environment variables for simple values, mounted files for complex content
