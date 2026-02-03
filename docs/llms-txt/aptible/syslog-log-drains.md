# Source: https://www.aptible.com/docs/core-concepts/observability/logs/log-drains/syslog-log-drains.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Syslog Log Drains

# Overview

Aptible can deliver your logs via Syslog to a destination of your choice. This option makes it easy to use third-party providers such as [Logentries](https://logentries.com/) or [Papertrail](https://papertrailapp.com/) with Aptible.

> ❗️ When sending logs to a third-party provider, make sure your logs don't include sensitive or regulated information, or that you have the proper agreement in place with your provider.

# TCP-TLS-Only

Syslog [Log Drains](/core-concepts/observability/logs/log-drains/overview) exclusively support TCP + TLS as the transport. This means you cannot deliver your logs over unencrypted and insecure channels, such as UDP or plaintext TCP.

# Logging Tokens

Syslog [Log Drains](/core-concepts/observability/logs/log-drains/overview) lets you inject a prefix in all your log lines. This is useful with providers such as Logentries, which require a logging token to associate the logs you send with your account.

# Get Started

<Card title="Setting up a logging to Papertrail" icon="books" iconType="duotone" href="https://www.aptible.com/docs/papertrail">
  Step-by-step instructions on setting up logging to Papertrail
</Card>
