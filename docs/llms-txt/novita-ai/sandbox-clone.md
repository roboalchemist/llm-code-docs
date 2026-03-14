# Source: https://novita.ai/docs/guides/sandbox-clone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Clone

export const SandboxBetaVersionWarning = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Warning>The following features require <Link href="/guides/sandbox-sdk-and-cli#install-beta-sdk" target="self">installing the Beta SDK & CLI</Link>. Please note that beta features are subject to change and may be less stable than production releases. If you encounter any issues while using these features, please <Link href="https://meetings-na2.hubspot.com/junyu" target="_blank">contact us</Link>.</Warning>;
  }
};

At the current stage, AI Agents face a fundamental limitation when executing complex tasks: the "n of 1" problem — AI and developers are confined to a single working environment for serial reasoning. This pattern leads to several key issues:

1. **Experiment Conflicts and Environment Contamination**. When an AI Agent tries multiple solutions, experimental code changes may interfere with the developer's main workflow or contaminate the current runtime environment. Once an experiment goes wrong, recovery often requires a rollback, and valuable exploration paths cannot be preserved.

2. **Inability to Explore Multiple Solutions in Parallel**. Constrained to a single environment, the AI Agent can only test different approaches sequentially. This serial mode is not only inefficient, but more importantly, it limits the breadth of AI exploration — unable to simultaneously validate multiple parallel hypotheses or implementation approaches.

3. **Limited Scalability of Computing Power**. When facing tasks that require "Wide-Research" (e.g., comparing 100 solutions simultaneously, batch-generating multiple implementation versions), the single-environment architecture fundamentally restricts the ability to parallelize task processing.

The **"Sandbox Clone"** feature enables the transition from "Deep-Research" to "Wide-Research":

1. **Multi-Timeline Exploration Architecture**: Like a decision tree, the AI Agent can start from the same baseline state and create multiple independent sandbox copies, each exploring a different solution path without interfering with each other.
2. **True Parallel Computing Capability**: By splitting large tasks into batch subtasks, the AI Agent can scale its computing power by tens or even hundreds of times, simultaneously processing dozens or hundreds of exploration branches.
3. **Zero-Risk Experimentation Environment**: Cloned sandboxes are completely isolated, allowing the AI to freely experiment and test various possibilities without affecting the original environment or the developer's main workflow.
4. **Efficient Resource Utilization**: Although multiple sandbox instances may be launched simultaneously, by dynamically managing and promptly terminating branches (sandbox instances) that are no longer valuable, overall computing resource consumption can be kept within a reasonable range.

This capability enables AI Agents to break through current performance bottlenecks, transitioning from providing theoretical suggestions to delivering reliable solutions that have been verified in parallel and actually tested, truly achieving the ability to autonomously explore, iterate, and solve complex problems.

<SandboxBetaVersionWarning />

## Terminology

* **Origin Sandbox**: The original sandbox instance being cloned.
* **New Sandbox**: The new sandbox instance created through the clone operation.

## Feature Overview

The sandbox clone feature currently supports the following two scenarios:

* Clone a sandbox in Running state
* Clone a sandbox in Paused state

### Cloning a Running Sandbox

**During the clone process:**

* The origin sandbox will be briefly suspended during cloning;
* The sandbox instance is unavailable during suspension;
* The suspension duration is close to the time required for a single pause operation.

**After cloning is complete:**

**Origin Sandbox:**

* Status is restored to running;
* The existing pause record will be refreshed to a new pause record, based on the current sandbox state;
* A new snapshot template record is generated (to delete this snapshot template, you need to first terminate both the origin sandbox and the cloned sandboxes);

**New Sandbox:**

* Status is running;
* Ready to use immediately.

### Cloning a Paused Sandbox

**During the clone process:**

When the origin sandbox is in a paused state:

* The clone process will not trigger the origin sandbox to start;
* The origin sandbox remains in paused state.

**After cloning is complete:**

**Origin Sandbox:**

* The existing pause record is not cleared;
* A new snapshot template record is generated (to delete this snapshot template, you need to first terminate both the origin sandbox and the cloned sandboxes);

**New Sandbox:**

* Status is running;
* Ready to use immediately.

### New Sandbox Attribute Inheritance Rules

| Attribute   | Inherited |
| ----------- | --------- |
| auto resume | Yes       |
| auto pause  | No        |

## Parameter Description

* `count`: The number of sandbox instances to clone. The minimum value is 1, and the maximum must not exceed the platform's concurrent running sandbox instance limit (see: [Sandbox Quota Limit](/guides/sandbox-quota-limit));
* `strict`: Whether to strictly clone according to the number specified in the `count` parameter, default is false.
  * `true`: If the number of successfully cloned instances is less than `count`, a clone failure is returned; successfully created sandboxes will be automatically released.
  * `false`: Returns the actual number of successfully cloned sandbox instances.
* `timeout`(`timeoutMs`): The timeout for cloning sandbox instances.
  * If not specified:
    * When the origin sandbox is in running state, it inherits its timeout configuration;
    * When the origin sandbox is in paused state, the default value of 5 minutes is used.

## Return Value

After a successful clone operation, an object is returned containing the following properties:

| Property               | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `sandboxes`            | List of successfully cloned sandbox instances           |
| `count`                | Number of successfully cloned sandboxes                 |
| `snapshot_template_id` | Snapshot template ID generated during the clone process |

## Code Examples

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  from novita_sandbox.core import Sandbox

  # Create a sandbox
  sandbox = Sandbox.create(template="base")
  # clone
  clones = Sandbox.clone(sandbox.sandbox_id, 2)

  print("snapshot:", clones.snapshot_template_id)
  for sbx in clones:
      print("clone sandbox:", sbx.sandbox_id)
  ```

  ```js JavaScript & TypeScript icon="js" theme={"system"}
  import { Sandbox } from '@novita-sandbox/core'

  // Create a sandbox
  const sandbox = await Sandbox.create('base')

  // clone
  const sbxClones = await Sandbox.clone(sandbox.sandboxId, { count: 2 })

  console.log("snapshot:", sbxClones.snapshotTemplateId)
  for (const idx in sbxClones.sandboxes) {
      console.log("clone sandboxID[" + idx + "]:", sbxClones.sandboxes[idx].sandboxId)
  }
  ```
</CodeGroup>

Additionally, you can also use the Novita Sandbox CLI to clone a specified sandbox instance:

```bash Bash icon="terminal" theme={"system"}
# novita-sandbox-cli sandbox clone [sandboxID] -c [count] -s [strict] -t [timeout]
novita-sandbox-cli sandbox clone 0r0efkbfwzfp9p7qpc1c -c 2
```


Built with [Mintlify](https://mintlify.com).