# Source: https://docs.inkeep.com/deployment/add-other-services/datadog-apm

# Datadog (/deployment/add-other-services/datadog-apm)

Add Datadog APM to your Inkeep Agent Framework services



## Overview

Learn how to add Datadog APM to your Inkeep Agent Framework services.

## Step 1: Install Datadog APM

From the root of your workspace, run the following command:

```bash
pnpm install dd-trace
```

## Step 2: Set up tracer.ts

In `apps/agents-api` create a new file called `tracer.ts` and add the following code:

```typescript
import tracer from "dd-trace";
tracer.init(); // initialized in a different file to avoid hoisting.
export default tracer;
```

In `apps/run-api/src/index.ts` and `apps/manage-api/src/index.ts` add the following code to the top of the file before all other imports:

```typescript
import "./tracer";
```

## Additional Resources

For more information on how to configure APM, you can consult the official Datadog Node.js [documentation](https://app.datadoghq.com/apm/service-setup?architecture=host-based\&framework=typescript\&language=node\&product=apm).
