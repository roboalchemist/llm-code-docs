# Source: https://docs.augmentcode.com/setup-augment/user-secrets.md

# Secrets Manager

> Securely store and manage secrets for your development environment, including API keys, tokens, and credentials.

export const Availability = ({tags}) => {
  const tagTypes = {
    invite: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    beta: {
      styles: "border border-zinc-500/20 bg-zinc-50/50 dark:border-zinc-500/30 dark:bg-zinc-500/10 text-zinc-900 dark:text-zinc-200"
    },
    vscode: {
      styles: "border border-sky-500/20 bg-sky-50/50 dark:border-sky-500/30 dark:bg-sky-500/10 text-sky-900 dark:text-sky-200"
    },
    jetbrains: {
      styles: "border border-amber-500/20 bg-amber-50/50 dark:border-amber-500/30 dark:bg-amber-500/10 text-amber-900 dark:text-amber-200"
    },
    vim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    neovim: {
      styles: "bg-gray-700 text-white dark:border-gray-50/10"
    },
    default: {
      styles: "bg-gray-200"
    }
  };
  return <div className="flex items-center space-x-2 border-b pb-4 border-gray-200 dark:border-white/10">
      <span className="text-sm font-medium">Availability</span>
      {tags.map(tag => {
    const tagType = tagTypes[tag] || tagTypes.default;
    return <div key={tag} className={`px-2 py-0.5 rounded-md text-xs font-medium ${tagType.styles}`}>
            {tag}
          </div>;
  })}
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
