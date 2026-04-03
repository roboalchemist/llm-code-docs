# Source: https://docs.jfrog.com/artifactory/docs/use-pnpm-with-jfrog-cli.md

# Use Pnpm with Jfrog CLI

<br />

This procedure is for teams that use **pnpm** for JavaScript or TypeScript builds and use **JFrog Artifactory** as an npm registry. **JFrog CLI** (`jf`) exposes **`jf pnpm`** so you can run **pnpm install** and **pnpm publish** with optional **build-info** collection and later publish that build info to Artifactory.

**Why use it:** You keep using **pnpm** as usual while the CLI can record dependency and artifact metadata for **build-info**, which supports traceability, promotion, and integration with other JFrog features.

**Wider context:** This is part of [JFrog CLI](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli) Artifactory workflows. You still configure **registry URLs and npm auth** for pnpm (for example **`.npmrc`**).

***

## What Do You Need Before You Start?

| Prerequisite                   | Requirement                                                                                                                                                                                                                                             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pnpm                           | **10.x** only (from **10.0.0** through **10.x**, not **11.x**). On your machine, run **`pnpm --version`** and ensure **`pnpm`** is on your **`PATH`**.                                                                                                  |
| Node.js                        | **20** or newer. Run **`node --version`**.                                                                                                                                                                                                              |
| Artifactory                    | At least one **npm**-type repository (virtual, remote, and/or local) appropriate for resolve and publish.                                                                                                                                               |
| **`.npmrc` (registry + auth)** | **Required** for pnpm operations against Artifactory to work end to end. Configure registry URL and credentials in **`.npmrc`** (or the equivalent via **`pnpm config`**). The JFrog CLI does not replace this file for integrated **`jf pnpm`** flows. |

**Quick verification**

```bash
jf --version
jf pnpm --help
pnpm --version
node --version
```

**How components interact**

| Component       | Role                                                                                                                          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **`.npmrc`**    | Sets **registry** and **authentication** for pnpm. Required for installs and publishes.                                       |
| **`jf config`** | Stores **Artifactory URL and credentials** for the CLI (**`--server-id`**, build-info API calls).                             |
| **`jf pnpm`**   | Integrates **`install`** / **`i`** and **`publish`** / **`p`**; all other subcommands are forwarded to the **`pnpm`** binary. |

Do not rely on CLI screenshots; use the command examples below as your source of truth.

***

## Important limitations and behaviors

The following behaviors apply to the **pnpm** integration in **JFrog CLI** (product expectations and pnpm semantics):

| Topic                              | Behavior                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`.npmrc`**                       | **Required.** Registry and authentication for **pnpm** must be configured (typically **`.npmrc`** or **`pnpm config`**). Without it, integrated **`jf pnpm`** installs and publishes do not go through reliably against **Artifactory**.                                                                       |
| **Git-based dependencies**         | **Not supported** in the sense that matters for **Artifactory**: resolution from **git** does not provide a tarball stored in **Artifactory**, so the integration cannot treat those dependencies like registry-hosted packages.                                                                               |
| **`pnpm add`**                     | **Pass-through only.** **`jf pnpm add`** runs **pnpm** directly; the CLI does **not** manipulate or collect **build-info** for **`add`**.                                                                                                                                                                      |
| **Optional dependencies**          | The integration currently **does not record** **`optionalDependencies`** in build-info. **Avoid** leaning on **`optionalDependencies`** where correctness of the dependency graph matters—they can introduce **false-positive** scenarios for build-info and resolution reporting.                             |
| **`workspaces` in `package.json`** | Defining workspaces with the **npm**-style **`workspaces`** field in **`package.json`** can **fail from pnpm itself**. **pnpm** expects workspace roots via **`pnpm-workspace.yaml`** (and related layout). This is a **pnpm** limitation, not specific to **JFrog CLI**.                                      |
| **`pnpm patch`**                   | Patches used only for **local debugging**, **without** publishing a **new package version**, are **not reflected** in what the integration considers published. Use **`pnpm patch`** for local sessions; bump and **publish** a new version when the change must be visible to **Artifactory** and build-info. |

***

## How Do You Integrate pnpm With Artifactory?

Use the following sections in order, or skip steps that do not apply to your workflow.

* [Important limitations and behaviors](#important-limitations-and-behaviors)
* [Step 1: Register Artifactory in the CLI](#step-1-register-artifactory-in-the-cli)
* [Step 2: Point pnpm at Artifactory](#step-2-point-pnpm-at-artifactory)
* [Step 3: Install dependencies with JFrog CLI](#step-3-install-dependencies-with-jfrog-cli)
* [Step 4: Publish packages with JFrog CLI](#step-4-publish-packages-with-jfrog-cli)
* [Step 5: Publish build info to Artifactory](#step-5-publish-build-info-to-artifactory)
* [Step 6: Run other pnpm subcommands (pass-through)](#step-6-run-other-pnpm-subcommands-pass-through)

### Step 1: Register Artifactory in the CLI

**To register Artifactory in the JFrog CLI:**

1. Run **`jf config add`** and complete the prompts. A server is added so **`jf`** can reach **JFrog Artifactory**. During setup, choose or note a **server ID** for later use.

   ```bash
   jf config add
   ```

   When setup completes, **`jf`** can resolve optional flags such as **`--server-id`** on **`jf pnpm`**.

2. Optional: Use the short form **`jf c add`**. The **`jfrog`** executable name is equivalent to **`jf`** in v2.

**CI and automation:** `jf config add` is interactive by default. For pipelines, configure the server **non-interactively** (for example with **`JFROG_CLI_HOME`**, environment variables such as **`JF_URL`** and **`JF_ACCESS_TOKEN`** when using **setup-jfrog-cli**, or the flags your JFrog CLI version supports for **`jf config add`**). For more information, see the [JFrog CLI](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli) documentation for the options available in your release.

***

### Step 2: Point pnpm at Artifactory

**To point pnpm at Artifactory:**

**`.npmrc` is required** for **pnpm** to reach **Artifactory** with the correct registry and credentials. Complete this step before **`jf pnpm install`** or **`jf pnpm publish`**.

1. Configure registry and authentication outside this procedure's **`jf`** syntax (for example **`.npmrc`** in the project or user home, or **`pnpm config set`**). Registry URLs typically follow this pattern:

   ```text
   https://<host>/artifactory/api/npm/<repository_key>/
   ```

2. For token-based authentication, set the token value to a real secret at runtime. Do not paste tokens into documentation or source control. Example shape only:

   ```text
   //<host>/artifactory/api/npm/<repository_key>/:_authToken=<Token>
   ```

***

### Step 3: Install dependencies with JFrog CLI

**To install dependencies with JFrog CLI integration:**

**CLI command**

```bash
jf pnpm install [<pnpm_arguments>] [--server-id <server_id>] [--build-name <build_name>] [--build-number <build_number>] [--project <project_key>] [--module <module_name>]
```

| Placeholder        | Description                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<pnpm_arguments>` | Optional. Flags and options passed to **pnpm install** (for example **`--frozen-lockfile`**, **`--store-dir=<path>`**).                                           |
| `<server_id>`      | Optional. CLI server configuration used for build-info and related Artifactory access. Parsed from the argument list (see **`jf pnpm --help`** for your version). |
| `<build_name>`     | Optional. Build name for build-info collection.                                                                                                                   |
| `<build_number>`   | Optional. Build number; use with **`<build_name>`**. Both are required for collection.                                                                            |
| `<project_key>`    | Optional. JFrog **Project** key.                                                                                                                                  |
| `<module_name>`    | Optional. Module name in build-info.                                                                                                                              |

**Full example (sample values)**

```bash
jf pnpm install --frozen-lockfile --build-name my-application --build-number 2026.03.30.1
```

If **pnpm install** succeeds but build-info collection fails, the CLI may log a **warning** and still exit successfully for the install.

***

### Step 4: Publish packages with JFrog CLI

**To publish packages with JFrog CLI integration:**

**CLI command**

```bash
jf pnpm publish [<pnpm_arguments>] [--server-id <server_id>] [--build-name <build_name>] [--build-number <build_number>] [--project <project_key>] [--module <module_name>]
```

**Short form:** `jf pnpm p` with the same optional JFrog arguments.

| Placeholder        | Description                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| `<pnpm_arguments>` | Optional. **pnpm publish** flags (for example **`--no-git-checks`**, **`-r`** for recursive workspace publish). |
| `<server_id>`      | Same as Step 3.                                                                                                 |
| `<build_name>`     | Same as Step 3.                                                                                                 |
| `<build_number>`   | Same as Step 3.                                                                                                 |
| `<project_key>`    | Same as Step 3.                                                                                                 |
| `<module_name>`    | Same as Step 3.                                                                                                 |

**Full example (sample values)**

```bash
jf pnpm publish --no-git-checks --build-name my-application --build-number 2026.03.30.1
```

**Workspace example (sample values)**

```bash
jf pnpm publish -r --no-git-checks --build-name my-application --build-number 2026.03.30.1
```

For workspace publishes with build-info, the implementation may use **`pnpm-publish-summary.json`** (**`--report-summary`**).

***

### Step 5: Publish build info to Artifactory

**To publish build info to Artifactory:**

After **`jf pnpm install`** and/or **`jf pnpm publish`** with both **`<build_name>`** and **`<build_number>`**, publish the collected build info.

**CLI command**

```bash
jf rt build-publish <build_name> <build_number>
```

**Alias:** `jf rt bp <build_name> <build_number>`

| Placeholder      | Description                            |
| ---------------- | -------------------------------------- |
| `<build_name>`   | Same value as used with **`jf pnpm`**. |
| `<build_number>` | Same value as used with **`jf pnpm`**. |

**Full example (sample values)**

```bash
jf rt build-publish my-application 2026.03.30.1
```

***

### Step 6: Run other pnpm subcommands (pass-through)

**To run other pnpm subcommands through JFrog CLI:**

**CLI command**

```bash
jf pnpm <subcommand> [<pnpm_arguments>]
```

| Placeholder        | Description                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `<subcommand>`     | Any pnpm subcommand other than **`install`**, **`i`**, **`publish`**, or **`p`** (for example **`ci`**, **`add`**, **`run`**). |
| `<pnpm_arguments>` | Arguments passed to native **pnpm**.                                                                                           |

**`pnpm add`:** **`jf pnpm add`** is a **direct pass-through** to **pnpm**. The CLI does **not** collect or adjust **build-info** for **`add`**—use **`jf pnpm install`** (after lockfile changes) when you need integrated build-info.

**Full example (sample values)**

```bash
jf pnpm run build
jf pnpm ci
jf pnpm add lodash
```

For build-info collection, use **`jf pnpm install`** (or **`jf pnpm publish`**) as in Steps 3–4.

***

## Where Can You Get More Help?

### Built-in help

```bash
jf pnpm --help
```

If **`jf pnpm --help`** fails, your CLI build does not include the **`pnpm`** integration yet. Upgrade to a release that includes it.

### CI/CD example (GitHub Actions)

Use **pnpm 10** and a compatible **Node.js** version (for pnpm 10, **Node 20+**). Supply registry auth via **`.npmrc`** or your secret store. Do not commit **`<Token>`** values.

The steps that invoke **`jf pnpm install`** require a JFrog CLI build that provides **`jf pnpm`**.

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: pnpm/action-setup@v4
    with:
      version: 10
  - uses: actions/setup-node@v4
    with:
      node-version: "20"
      cache: "pnpm"
  - uses: jfrog/setup-jfrog-cli@v4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}
  - run: jf pnpm install --build-name=my-app --build-number=${{ github.run_number }}
  - run: jf rt build-publish my-app ${{ github.run_number }}
```

### Troubleshooting

| Symptom                                         | What to check                                                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **`jf pnpm` is not a command**                  | Your CLI build may not include **`pnpm`** yet. Run **`jf pnpm --help`**. Use a newer release or a custom build from your team. |
| Wrong **pnpm** version                          | **pnpm 10.x** only. Confirm with **`pnpm --version`** and that **`pnpm`** is installed.                                        |
| **Node** prerequisite errors                    | **Node 20+**.                                                                                                                  |
| **401** / **403**                               | **`.npmrc`** / **pnpm** auth and **`jf config`** credentials.                                                                  |
| **404** or wrong packages                       | Registry URL and repository keys.                                                                                              |
| Publish OK but artifact missing                 | **`publishConfig.registry`**, **pnpm** config, repository type.                                                                |
| No build info from **`jf pnpm ci`** / **`add`** | Only **`install`** and **`publish`** collect build-info. All other subcommands are pass-through.                               |
| Git **URL** dependencies / git-based resolution | Not aligned with **Artifactory** tarballs; see [Important limitations and behaviors](#important-limitations-and-behaviors).    |
| Workspace setup fails in **pnpm**               | Prefer **`pnpm-workspace.yaml`**. The **`workspaces`** field in **`package.json`** (npm-style) may fail in **pnpm** itself.    |
| **`pnpm patch`** not visible in build-info      | Local patches without a **published** version bump are not considered; publish a new version for **Artifactory**.              |
| **Optional dependencies** skewing reports       | Avoid where possible; can cause false-positive dependency scenarios.                                                           |
| More detail                                     | `export JFROG_CLI_LOG_LEVEL=DEBUG`                                                                                             |
| Upgrade message on every command                | The CLI may warn that a newer version is available. To hide it: `export JFROG_CLI_AVOID_NEW_VERSION_WARNING=TRUE`              |

### Integrated subcommands (summary)

| First argument         | Integrated JFrog behavior  |
| ---------------------- | -------------------------- |
| **`install`**, **`i`** | Yes — optional build info  |
| **`publish`**          | Yes — optional build info  |
| **All others**         | No — forwarded to **pnpm** |

### Next steps

* Publish or promote builds according to your [JFrog CLI](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli) and **JFrog Artifactory** documentation.
* Compare with **`jf npm`** and **`jf yarn`** on the same documentation site if you maintain multiple package managers.

## Frequently Asked Questions

### Why does `jf pnpm` say the command is not found?

Your CLI build might not include the **pnpm** integration yet. Upgrade to a release that includes **`jf pnpm`**.

### Which pnpm and Node.js versions are supported?

**pnpm 10.x** and a compatible **Node.js** version (**Node 20+** for pnpm 10). See [What Do You Need Before You Start?](#what-do-you-need-before-you-start).

### How do I collect build info?

Pass **`--build-name`** and **`--build-number`** to **`jf pnpm install`** or **`jf pnpm publish`**, then run **`jf rt build-publish`**. See [Step 5](#step-5-publish-build-info-to-artifactory).

### Why is `.npmrc` mandatory?

**`jf pnpm`** relies on **pnpm** for registry resolution. **`.npmrc`** supplies the **Artifactory** registry URL and auth. See [Step 2](#step-2-point-pnpm-at-artifactory).

### Are git dependencies or `pnpm patch` supported for build-info?

No. See [Important limitations and behaviors](#important-limitations-and-behaviors).

## Related Topics

* [JFrog CLI](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli)
* [Package managers integration](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli/binaries-management-with-jfrog-artifactory/package-managers-integration) ( **`jf npm`**, **`jf yarn`**, and related topics on the same site)
* **JFrog Artifactory** npm repository documentation on [docs.jfrog.com](https://docs.jfrog.com/)
* [Native mode](https://docs.jfrog.com/artifactory/docs/native-mode) (comparison context for npm clients; **`jf pnpm`** does not use the same native flags as **`jf npm`**)