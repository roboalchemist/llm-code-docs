# Source: https://docs.jfrog.com/artifactory/docs/native-mode.md

# Native Mode

JFrog CLI provides two execution modes for package managers: **Wrapped Mode** (default) and **Native Mode** (opt-in). This page explains the difference, which tools support Native Mode, and how to configure each one.

***

## Prerequisites

Before using any build-tool command, ensure the following are in place:

| Requirement           | Details                                                                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JFrog CLI configured  | Run `jf config add` at least once. Verify with `jf config show`.                                                                                           |
| Tool installed        | Install the package manager you intend to use (Maven, Gradle, npm, Poetry, Docker).                                                                        |
| Tool-specific runtime | Maven and Gradle require **Java** in `PATH`. Verify with `java -version`.                                                                                  |
| Docker daemon running | Docker Native Mode requires the Docker daemon to be active. Verify with `docker info`.                                                                     |
| Artifactory access    | For Native Mode: a repository must exist and credentials must be configured via Artifactory **Set Me Up**. For Wrapped Mode: run `jf <tool>-config` first. |

<Callout icon="👍" theme="okay">
  Tip

  If you have multiple JFrog servers configured, identify your default server with `jf config show`. All `jf rt build-publish` and `jf rt bp` commands use the default server unless you pass `--server-id=<your-server-id>` explicitly.
</Callout>

***

## Build-Info Flags in Native Mode

The following flags are available on every build-tool command that supports build-info collection. They work in both Wrapped Mode and Native Mode.

| Flag             | Default | Description                                                                                                                                                 |
| ---------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--build-name`   | —       | A name for this build (for example, `my-web-app`). Required with `--build-number`.                                                                          |
| `--build-number` | —       | A number or identifier for this build run (for example, `42`, `$BUILD_NUMBER`). Required with `--build-name`.                                               |
| `--project`      | —       | JFrog Artifactory project key. Associates the build-info with a specific project.                                                                           |
| `--module`       | —       | Optional module name within the build-info. Use when a single build produces artifacts from multiple modules. Requires `--build-name` and `--build-number`. |

<Callout icon="📘" theme="info">
  Note

  `--build-name` and `--build-number` must always be provided together. If you supply one without the other, the CLI returns an error.
</Callout>

### `--module` Flag

The `--module` flag is used when a single build produces multiple logical components:

```bash
jf mvn clean install --build-name=my-app --build-number=1 --module=backend
jf mvn clean install --build-name=my-app --build-number=1 --module=frontend
jf rt build-publish my-app 1 --server-id=<your-server-id>
```

The resulting build-info for build `my-app #1` contains two modules (`backend` and `frontend`), each with their own dependency trees.

<Callout icon="📘" theme="info">
  Note

  `jf rt build-publish` uses your default configured server. If the build tool was configured with a different server, pass `--server-id=<your-server-id>` to target the correct server.
</Callout>

<Callout icon="📘" theme="info">
  Note

  The `--module` flag is functional for all build-tool commands. For some commands (Maven, Gradle), it does not appear in `jf <tool> --help` output but still works when passed on the command line.
</Callout>

<Callout icon="🚧" theme="warn">
  Known CLI limitation

  `jf npm install --help` does not display build-info flags (`--build-name`, `--build-number`, `--module`, `--project`). These flags are supported and work correctly — check `jf npm publish --help` to see them listed, or refer to this page.
</Callout>

### `--project` Flag

The `--project` flag associates the build-info with a JFrog Project — an organizational unit in the JFrog Platform that groups repositories, builds, and security policies.

```bash
jf npm install --build-name=my-app --build-number=1 --project=my-team
jf rt build-publish my-app 1 --project=my-team --server-id=<your-server-id>
```

<Callout icon="📘" theme="info">
  Note

  The JFrog Project (`--project`) must already exist in Artifactory before publishing. Create projects in the JFrog Platform UI under **Projects**.
</Callout>

***

## Wrapped Mode vs Native Mode

| Aspect                         | Wrapped Mode (Default)                                          | Native Mode                                                                                                                           |
| ------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Repository configuration       | Injected by JFrog CLI from `.jfrog/projects/*.yaml`             | You must configure manually                                                                                                           |
| Project file modifications     | CLI may modify `settings.xml`, `pyproject.toml`, `.npmrc`, etc. | No project files are modified                                                                                                         |
| Build-info collection          | Automatic when `--build-name` / `--build-number` are provided   | Supported for Maven, Gradle, npm, Poetry, Docker, Helm, and Conan when `--build-name` / `--build-number` are provided via `jf <tool>` |
| Lock file changes              | Possible (for example, `poetry.lock` may be updated)            | Never modified                                                                                                                        |
| Requires `*-config` command    | Yes — run `jf <tool>-config` first                              | No — config is ignored                                                                                                                |
| Requires Artifactory Set Me Up | Optional                                                        | Required                                                                                                                              |

***

## Which Tools Support Native Mode?

| Package Manager                       | How to Enable                                                      | Build-Info in Native? | Notes                                                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [Maven](/artifactory/docs/jf-mvn)     | `export JFROG_RUN_NATIVE=true`                                     | **Yes**               | Bypasses `mvn-config` and `.jfrog/` YAML; no `settings.xml` injection; user must configure Maven manually                                     |
| [Gradle](/artifactory/docs/jf-gradle) | `export JFROG_RUN_NATIVE=true`                                     | **Yes**               | Bypasses `gradle-config` and `.jfrog/` YAML; no Artifactory plugin injection; pass `--server-id` for server resolution                        |
| [npm](#npm-native-mode)               | `export JFROG_RUN_NATIVE=true` (or deprecated `--run-native` flag) | **Yes**               | Bypasses `npm-config`; uses user's `.npmrc`; build-info **still works**                                                                       |
| [Poetry](/artifactory/docs/jf-poetry) | `export JFROG_RUN_NATIVE=true`                                     | **Yes**               | Bypasses `poetry-config` and `.jfrog/` YAML; no `pyproject.toml` source injection; no `poetry.lock` changes; build-info works via `jf poetry` |
| [Docker](/artifactory/docs/jf-docker) | `export JFROG_RUN_NATIVE=true`                                     | **Yes**               | For `jf docker build`: runs native Docker build directly; build-info still collected when `--build-name`/`--build-number` provided            |

**Native-only tools** (no wrapped mode; no `*-config` command):

| Package Manager         | Build-Info in Native? | Notes                                                                                |
| ----------------------- | --------------------- | ------------------------------------------------------------------------------------ |
| [Helm](/docs/jf-helm)   | **Yes**               | Always runs native Helm; configure via `helm registry login` or native Helm commands |
| [Conan](/docs/jf-conan) | **Yes**               | Always runs native Conan; configure via `conan remote add` and native Conan commands |

**Wrapped-only tools** (no Native Mode support):

Yarn, pip, Pipenv, Twine, Go, NuGet, .NET, Terraform, Ruby — these tools operate exclusively in Wrapped Mode.

***

## Maven Native Mode

When `JFROG_RUN_NATIVE=true` is set, `jf mvn` runs Maven without injecting a generated `settings.xml` or applying `.jfrog/projects/maven.yaml`. You must configure Maven to resolve from Artifactory yourself using the Artifactory **Set Me Up** instructions for your Maven repository. The **Set Me Up** page generates a `<server>` entry with your Artifactory URL and credentials that you add to your `~/.m2/settings.xml`.

<Callout icon="❗️" theme="error">
  Important — existing `mvn-config` users

  If you have previously run `jf mvn-config`, a `.jfrog/projects/maven.yaml` file exists in your project. When this file is present, `JFROG_RUN_NATIVE=true` is currently ignored and the CLI falls back to Wrapped Mode silently.
</Callout>

**To switch Maven to Native Mode when `.jfrog/projects/maven.yaml` exists:**

1. Remove the wrapped-mode project file:

   ```bash
   rm .jfrog/projects/maven.yaml
   ```

2. Enable Native Mode for the shell session:

   ```bash
   export JFROG_RUN_NATIVE=true
   ```

### Usage

**To run a Maven build in Native Mode:**

* Run:

  ```bash
  export JFROG_RUN_NATIVE=true
  jf mvn clean install --build-name=my-app --build-number=1 --server-id=<your-server-id>
  ```

  Where:

  * \<your-server-id>: The JFrog CLI server ID from `jf config add`

  For example:

  ```bash
  export JFROG_RUN_NATIVE=true
  jf mvn clean install --build-name=my-app --build-number=1 --server-id=my-server
  ```

### Expected output

When Native Mode is active (no `.jfrog/projects/maven.yaml` present), Maven runs directly and build-info is collected after the build completes:

```
[INFO] BUILD SUCCESS
[Info] Collecting build info for executed command...
[Info] Build info saved locally. Use 'jf rt bp my-app 1' to publish it to Artifactory.
```

<Callout icon="📘" theme="info">
  Note

  After Maven finishes, the CLI collects build-info from the build output. This post-build step can take several seconds. The `[Info] Build info saved locally` message confirms it is complete — the command is not hung.
</Callout>

### What changes

* No `settings.xml` injection
* No `.jfrog/projects/maven.yaml` is read (requires the file to be absent — see note above)
* Build-info is collected after the build completes (post-execution, not via extractor injection)
* All Maven configuration comes from your own `settings.xml`

***

## Gradle Native Mode

When `JFROG_RUN_NATIVE=true` is set, `jf gradle` runs Gradle without injecting the Artifactory Gradle plugin or applying `.jfrog/projects/gradle.yaml`. You must configure Gradle to resolve from Artifactory yourself using the Artifactory **Set Me Up** instructions, which generate the repository URL and credential configuration you add to your `build.gradle` or `gradle.properties`.

<Callout icon="❗️" theme="error">
  Important — existing `gradle-config` users

  If you have previously run `jf gradle-config`, a `.jfrog/projects/gradle.yaml` file exists in your project. When this file is present, you must remove it for Native Mode to take effect.
</Callout>

**To switch Gradle to Native Mode when `.jfrog/projects/gradle.yaml` exists:**

1. Remove the wrapped-mode project file:

   ```bash
   rm .jfrog/projects/gradle.yaml
   ```

2. Enable Native Mode for the shell session:

   ```bash
   export JFROG_RUN_NATIVE=true
   ```

### Usage

**To run a Gradle build in Native Mode:**

* Run:

  ```bash
  export JFROG_RUN_NATIVE=true
  jf gradle clean build --server-id=<your-server-id>
  ```

  Where:

  * \<your-server-id>: The JFrog CLI server ID to use for build-info (required in Native Mode)

  For example:

  ```bash
  export JFROG_RUN_NATIVE=true
  jf gradle clean build --server-id=my-server
  ```

<Callout icon="📘" theme="info">
  Note

  In Gradle Native Mode, pass `--server-id` to specify which configured JFrog server to use for build-info publishing. Without it, the CLI uses the default server.
</Callout>

### What changes

* No Artifactory Gradle plugin injection
* No `.jfrog/projects/gradle.yaml` is read (requires the file to be absent — see note above)
* Build-info is still collected when `--build-name` and `--build-number` are provided
* All Gradle configuration comes from your own build scripts

***

## npm Native Mode

When `JFROG_RUN_NATIVE=true` is set (or the deprecated `--run-native` flag is used), `jf npm` delegates entirely to the native npm client and uses your `.npmrc` for all configuration. You must configure your `.npmrc` with the Artifactory registry URL and authentication token using the Artifactory **Set Me Up** instructions for your npm repository.

### Usage

**To run npm commands in Native Mode:**

1. Enable Native Mode for the shell session:

   ```bash
   export JFROG_RUN_NATIVE=true
   ```

2. Run install or publish (examples):

   ```bash
   jf npm install --build-name=my-app --build-number=1
   jf npm publish --build-name=my-app --build-number=1 --server-id=<your-server-id>
   ```

   Where:

   * \<your-server-id>: The JFrog CLI server ID for publish operations when you have multiple servers configured

   For example:

   ```bash
   export JFROG_RUN_NATIVE=true
   jf npm install --build-name=my-app --build-number=1
   jf npm publish --build-name=my-app --build-number=1 --server-id=my-server
   ```

When Native Mode is active, the CLI confirms it at the start of execution:

```
[Info] Running npm in native mode (JFROG_RUN_NATIVE=true)
```

### What changes

* No temporary `.npmrc` is created by the CLI
* Your own `.npmrc` is used for all configuration
* Build-info collection still works (as with other tools in Native Mode)
* Publishing uses the native npm publish lifecycle (`prepublish`, `publish`, `postpublish` scripts run normally — no renaming needed)

<Callout icon="🚧" theme="warn">
  Deprecation notice

  The `--run-native` flag is deprecated. Use `export JFROG_RUN_NATIVE=true` instead. On npm 11.x, passing `--run-native` may also produce `npm warn Unknown cli config "--run-native"` from the npm client itself — this is harmless and does not affect behaviour.
</Callout>

<Callout icon="🚧" theme="warn">
  npm 11.x compatibility

  In Wrapped Mode, the JFrog CLI injects `always-auth` and `email` fields into the project's `.npmrc`. npm 11.x treats these as deprecated configuration keys and emits `npm warn Unknown project config "always-auth"` on every install. These warnings are harmless. To eliminate them, use Native Mode (`JFROG_RUN_NATIVE=true`) with a manually configured `.npmrc`.
</Callout>

<Callout icon="🚧" theme="warn">
  Known CLI limitation

  `jf npm install --help` does not display build-info flags. These flags are functional — use `jf npm publish --help` to see them listed, or refer to the [Build-Info Flags](#build-info-flags-in-native-mode) section above.
</Callout>

***

## Poetry Native Mode

When `JFROG_RUN_NATIVE=true` is set, `jf poetry` delegates to the native Poetry client without injecting Artifactory configuration or modifying project files. You can run Poetry commands through `jf poetry` (to benefit from build-info collection) or directly via `poetry` (without build-info). You must configure Poetry to use the Artifactory repository using the Artifactory **Set Me Up** instructions for your PyPI repository. The **Set Me Up** page generates the `poetry source add` command and credential configuration you add to your project.

### Usage

**To run Poetry with build-info in Native Mode:**

1. Enable Native Mode:

   ```bash
   export JFROG_RUN_NATIVE=true
   ```

2. Run installs and publishes through `jf poetry` when you need build-info, or use native `poetry` when you do not:

   * With build-info:

     ```bash
     jf poetry install --build-name=my-app --build-number=1
     jf poetry publish --build-name=my-app --build-number=1
     ```

   * Without build-info:

     ```bash
     poetry install
     poetry build
     poetry publish -r artifactory
     ```

<Callout icon="📘" theme="info">
  Note

  In Native Mode, you can use either `jf poetry install` (which delegates to native Poetry and collects build-info when `--build-name`/`--build-number` are provided) or `poetry install` directly (no build-info). Poetry must be configured via Artifactory's **Set Me Up** instructions for both approaches.
</Callout>

### What changes

* No `tool.poetry.source` entries are injected into `pyproject.toml`
* No `poetry update` is called implicitly
* No `poetry.lock` modifications
* No `.jfrog/projects/poetry.yaml` is read
* Build-info is still collected when using `jf poetry` with `--build-name` and `--build-number`
* All configuration comes from Poetry's own `config` and Artifactory Set Me Up

***

## Docker Native Mode

When `JFROG_RUN_NATIVE=true` is set, `jf docker build` runs the native Docker build directly instead of the legacy JFrog build flow. Build-info is still collected when `--build-name` and `--build-number` are provided. Prerequisites: the Docker daemon must be running (`docker info`), a JFrog server must be configured with `jf config add`, and you must be logged in to the Docker registry with `docker login <registry>` before running these commands. For details, see [`jf docker`](/docs/jf-docker).

### Usage

**To build and push a Docker image in Native Mode:**

1. Enable Native Mode, confirm the Docker daemon is running (`docker info`), and log in to the registry (`docker login <registry>`).

2. Run build, push, and publish build-info:

   ```bash
   export JFROG_RUN_NATIVE=true
   jf docker build -t <registry>/<image>:<tag> . --build-name=my-app --build-number=1
   jf docker push <registry>/<image>:<tag> --build-name=my-app --build-number=1
   jf rt bp my-app 1 --server-id=<your-server-id>
   ```

   Where:

   * \<registry>: Your Artifactory Docker registry host (for example, `acme.jfrog.io`)
   * \<image>: Image name (for example, `docker-local/my-app`)
   * \<tag>: Image tag (for example, `1.0.0`)
   * \<your-server-id>: The JFrog CLI server ID for `jf rt bp`

   For example:

   ```bash
   export JFROG_RUN_NATIVE=true
   jf docker build -t acme.jfrog.io/docker-local/my-app:1.0.0 . --build-name=my-app --build-number=1
   jf docker push acme.jfrog.io/docker-local/my-app:1.0.0 --build-name=my-app --build-number=1
   jf rt bp my-app 1 --server-id=my-server
   ```

### What changes

* Docker build runs via the native Docker client (no legacy JFrog build wrapper)
* Build-info is still collected when `--build-name` and `--build-number` are provided
* Push, pull, and scan behave the same in both modes

***

## Supported Client Versions

JFrog CLI (v2.92.0) is forward-compatible with modern package manager clients. The "Max Client" column represents the highest version certified for build-info collection and Native execution without schema errors.

| Package Manager  | Min Client | Max Client (Certified) | Build-Info | Mode               |
| ---------------- | ---------- | ---------------------- | ---------- | ------------------ |
| **Maven**        | 3.1.0      | 3.9.12+ (Rec: 3.9.x)   | Full       | Wrapped and Native |
| **Gradle**       | 5.0        | 9.0                    | Full       | Wrapped and Native |
| **npm**          | 6.x        | 11.x                   | Full       | Wrapped and Native |
| **Docker**       | 17.07.0    | 27.x (28 with BuildX)  | Full       | Wrapped and Native |
| **Poetry**       | 1.2.0      | 2.0                    | Full       | Wrapped and Native |
| **Conan V2**     | 2.0        | 2.11+                  | Full       | Native only        |
| **Helm (OCI)**   | 3.8.0      | 3.17                   | Full       | Native only        |
| **NuGet / .NET** | Core 2.0   | .NET 9.0               | Full       | Wrapped only       |
| **Go**           | 1.14       | 1.24                   | Full       | Wrapped only       |
| **pip**          | 20.x       | 25.x                   | Full       | Wrapped only       |
| **Terraform**    | 1.0        | 1.11                   | Full       | Wrapped only       |
| **Yarn**         | 1.x        | 3.x                    | Full       | Wrapped only       |

<Callout icon="📘" theme="info">
  Notes

  * **Yarn 4.x** is not supported.
  * **Docker BuildX** supports Docker engine up to v28 for multi-platform builds.
  * **Go** `--no-fallback` default is `true` (VCS fallback disabled by default).
</Callout>

***

## When to Use Which Mode

**Use Wrapped Mode when you want:**

* Integrated Artifactory resolution with zero manual configuration
* Automatic build-info capture
* Managed repository configuration via JFrog CLI
* Consistent, unified behaviour across machines and CI

**Use Native Mode when you need:**

* Strict lockfile fidelity (no modifications to `poetry.lock`, `package-lock.json`, etc.)
* Zero modification to project metadata (`pom.xml`, `pyproject.toml`, `settings.xml`, etc.)
* Full compatibility with the upstream package manager's behaviour
* Builds that must be fully deterministic across environments
* Custom or advanced workflows configured directly in the package manager

***

## Frequently Asked Questions

### How do I enable Native Mode?

Set the environment variable `JFROG_RUN_NATIVE=true` before running any `jf <tool>` command. This applies to all supported tools in the current shell session. Unset it or open a new terminal to return to Wrapped Mode.

### Does Native Mode still collect build-info?

Yes. When you run commands through `jf <tool>` with `--build-name` and `--build-number`, build-info is collected in both Wrapped and Native Mode. If you run the native tool directly (for example, `npm install` without the `jf` prefix), no build-info is collected.

### Which tools support Native Mode?

Maven, Gradle, npm, Poetry, and Docker support both Wrapped and Native Mode. Helm and Conan are native-only (no wrapped mode). All other tools (Yarn, pip, Pipenv, Twine, Go, NuGet, .NET, Terraform, Ruby) operate exclusively in Wrapped Mode.

### Will Native Mode modify my lockfiles or project files?

No. Native Mode never modifies `poetry.lock`, `package-lock.json`, `pyproject.toml`, `settings.xml`, or any other project file. This is the primary reason to choose Native Mode over Wrapped Mode.

### Can I use Native Mode for some tools and Wrapped Mode for others?

`JFROG_RUN_NATIVE=true` applies to all supported tools in the session. To mix modes, set the variable only before the commands that should run natively, then unset it before wrapped commands.

### How do I migrate an existing project from Wrapped Mode to Native Mode?

If you have previously run `jf <tool>-config`, a `.jfrog/projects/<tool>.yaml` file exists in your project directory. When this file is present, `JFROG_RUN_NATIVE=true` is currently ignored for Maven and Gradle and the CLI silently continues in Wrapped Mode.

**To migrate from Wrapped Mode to Native Mode:**

1. Delete the existing config file:

   ```bash
   rm .jfrog/projects/maven.yaml   # or gradle.yaml, npm.yaml, poetry.yaml
   ```

2. Configure your package manager to resolve from Artifactory manually (via Artifactory **Set Me Up**).

3. Set the environment variable and verify the mode switch in the CLI output:

   ```bash
   export JFROG_RUN_NATIVE=true
   jf mvn validate --build-name=test --build-number=1
   ```

   For Maven, look for `[Info] Build info saved locally. Use 'jf rt bp...' to publish.` For npm, look for `[Info] Running npm in native mode (JFROG_RUN_NATIVE=true)`.

### How can I tell that Native Mode is active?

For **npm**, the CLI prints `[Info] Running npm in native mode (JFROG_RUN_NATIVE=true)` at the start of each command.

For **Maven**, there is currently no startup confirmation message. You can confirm Native Mode is active by checking that the build output does **not** contain `Initializing Artifactory Build-Info Recording` and does contain `[Info] Collecting build info for executed command...` after the build finishes.

For **Gradle** and **Poetry**, refer to the absence of injected configuration in the build output.

<Callout icon="📘" theme="info">
  Note

  `JFROG_RUN_NATIVE` is not shown in `jf mvn --help` or `jf gradle --help`. This page and the FAQ are the primary discovery path for this environment variable.
</Callout>

***

## Related Topics

* [Build Tools Overview](/artifactory/docs/build-tool-commands) — Capabilities matrix and tool reference
* [Native Mode](/artifactory/docs/native-mode) — Supported packages with Native Mode

***

## Environment Variable Reference

| Variable           | Purpose                                     | Default           |
| ------------------ | ------------------------------------------- | ----------------- |
| `JFROG_RUN_NATIVE` | Enables Native Mode for all supported tools | `false` (not set) |

When this variable is set to `true`, it applies to all commands in the current shell session. Unset it or start a new session to return to Wrapped Mode.