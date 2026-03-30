# Source: https://novita.ai/docs/guides/sandbox-commit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox Snapshot Template

export const SandboxBetaVersionWarning = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    return <Warning>The following features require <Link href="/guides/sandbox-sdk-and-cli#install-beta-sdk" target="self">installing the Beta SDK & CLI</Link>. Please note that beta features are subject to change and may be less stable than production releases. If you encounter any issues while using these features, please <Link href="https://meetings-na2.hubspot.com/junyu" target="_blank">contact us</Link>.</Warning>;
  }
};

<SandboxBetaVersionWarning />

## Terminology

* **Commit**: A commit operation saves the current state of a sandbox as a template, resulting in a new template of type snapshot template.
* **Origin Sandbox**: The sandbox instance being committed.
* **Snapshot Template**: The template generated after a commit operation.

## Feature Description

### Committing a Running Sandbox

**During the commit process:**

* The origin sandbox will be briefly suspended during committing;
* The sandbox instance is unavailable during suspension;
* The suspension duration is close to the time required for a single pause operation.

**After committing is complete:**

**Origin Sandbox:**

* The existing pause record will be refreshed to a new pause record, based on the current sandbox state;
* The origin sandbox continues to run;
* A new template record is generated.

### Committing a Paused Sandbox

**During the commit process:**

* The commit process will not trigger the origin sandbox to start;
* The origin sandbox remains in paused state.

**After committing is complete:**

**Origin Sandbox:**

* The existing pause record is not cleared;
* A new template record is generated.

## Parameter Description

| Parameter    | Type     | Required | Description                              |
| ------------ | -------- | -------- | ---------------------------------------- |
| `sandbox_id` | `string` | Yes      | The ID of the sandbox instance to commit |
| `alias`      | `string` | No       | Set an alias for the generated template  |

## Return Value

After a successful commit operation, a `Template` object is returned.

## Code Examples

<CodeGroup>
  ```python Python icon="python" theme={"system"}
  from novita_sandbox.core import Sandbox

  # Commit an existing sandbox by ID to create a template snapshot
  # sandbox_id: str - Required. The ID of the sandbox to commit
  # alias: Optional[str] - Optional alias name for the created template
  # Note: Default timeout is 10 minutes for commit operation
  template = Sandbox.commit(
      sandbox_id="existing-sandbox-id",
      alias="my-template-alias"
  )
  print(f"Template ID: {template.template_id}")
  print(f"Build ID: {template.build_id}")
  ```

  ```js TypeScript icon="js" theme={"system"}
  import { Sandbox } from '@novita-sandbox/core'

  // Commit an existing sandbox by ID to create a template snapshot
  // sandboxId: string - Required. The ID of the sandbox to commit
  // opts?: { alias?: string } - Optional commit options
  const template = await Sandbox.commit('existing-sandbox-id', {
    alias: 'my-template-alias'
  })
  console.log(`Template ID: ${template.templateId}`)
  console.log(`Build ID: ${template.buildId}`)
  ```
</CodeGroup>

Additionally, you can also use the Novita Sandbox CLI to commit a specified sandbox instance:

```bash Bash icon="terminal" theme={"system"}
# Basic commit - creates a template snapshot from a sandbox
novita-sandbox-cli sandbox commit <sandboxID>

# Commit with alias - assign a friendly name to the template
novita-sandbox-cli sandbox commit <sandboxID> --alias my-template-alias

```


Built with [Mintlify](https://mintlify.com).