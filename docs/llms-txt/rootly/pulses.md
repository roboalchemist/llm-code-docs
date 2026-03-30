# Source: https://docs.rootly.com/configuration/pulses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Configure and manage pulses to track service changes like deployments, builds, and configuration updates that provide critical context during incident response.

## Overview[](#jBD-a)

Pulses represent service changes such as deploys, build completion, configuration updates, etc., providing contextual information that is critical during incident triage or hypercare.

They can be sent via specific integrations or our cli, and they do not create alerts, incidents or notifications.

## API[](#Gopxz)

You can create pulses through our API directly with curl for example:

```bash Linux theme={null}
curl --header "Content-Type: application/json" \
-H "Authorization: Bearer <your token>" \
--data '{"data": { "attributes": { "summary": "Something changed!" } } }' -X POST https://api.rootly.com/v1/pulses
```

## CLI[](#xZHxW)

You can create pulses through our CLI directly: [https://github.com/rootlyhq/cli](https://github.com/rootlyhq/cli "https://github.com/rootlyhq/cli")﻿

```bash Linux theme={null}
rootly pulse --api-key "ABC123" --environments "staging, production" --services "elasticsearch-staging, elasticsearch-prod" Hello World!
```

Or run a command

```bash Linux theme={null}
rootly pulse-run --api-key ABC123 --environments "production" --labels "version=2, attempt=1" --summary "Deploy Website" sh deploy.sh
```


Built with [Mintlify](https://mintlify.com).