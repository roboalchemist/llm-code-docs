# Source: https://docs.jfrog.com/artifactory/docs/set-up-a-build-tool-with-jfrog-artifactory.md

# Connect a Build Tool to Artifactory with JFrog CLI

Connect a build tool to JFrog Artifactory using JFrog CLI. This tutorial walks through the full workflow with npm, then shows how to adapt for any supported build tool.

This topic covers the following tasks:

* [How do I configure npm for Artifactory?](#how-do-i-configure-npm-for-artifactory)
* [How do I install dependencies through Artifactory?](#how-do-i-install-dependencies-through-artifactory)
* [How do I publish a package to Artifactory?](#how-do-i-publish-a-package-to-artifactory)
* [How do I enrich and publish build information?](#how-do-i-enrich-and-publish-build-information)

***

## Prerequisites

* **JFrog CLI installed** — [Installation guide](/integrations/docs/download-and-install-the-jfrog-cli)
* **JFrog CLI authenticated** — Run `jf config add` to configure a server connection ([Configuring the CLI](/integrations/docs/configuring-the-cli))
* **npm installed** — Or your build tool of choice
* **An npm project** with `package.json` — or create a minimal one for testing with `npm init -y`
* **A git repository** — required to use `jf rt build-add-git` (the command reads `.git` to attach commit info to build-info; run `git init && git commit` if your project is not yet under source control)

***

## What You Will Do

1. Configure npm to use Artifactory
2. Install npm dependencies via Artifactory
3. Publish an npm package
4. Collect and publish build information

***

## How do I configure npm for Artifactory?

Generate npm configuration that points your project to Artifactory for resolving and deploying packages. Run this in your project directory.

**To configure npm for Artifactory:**

1. In your project directory, run `jf npm-config` interactively or with flags.

   For interactive configuration:

   ```bash
   cd <your-project-dir>
   jf npm-config
   ```

   Running `jf npm-config` without flags starts an interactive wizard that prompts for your server ID and the resolve and deploy repository names.

   For scripts and CI pipelines, use non-interactive flags:

   ```bash
   jf npm-config --server-id-resolve=<server-id> --repo-resolve=<repo-name> --server-id-deploy=<server-id> --repo-deploy=<repo-name>
   ```

   Where:

   * \<server-id>: The server ID configured with `jf config add`
   * \<repo-name>: The Artifactory repository key for resolve or deploy

   For example:

   ```bash
   jf npm-config --server-id-resolve=my-server --repo-resolve=npm-virtual --server-id-deploy=my-server --repo-deploy=npm-local
   ```

   This creates or updates `.jfrog/projects/npm.yaml` in your project.

2. Optional — to list all `jf npm-config` options:

   ```bash
   jf npm-config --help
   ```

***

## How do I install dependencies through Artifactory?

Install dependencies through Artifactory. The CLI records build information when you pass `--build-name` and `--build-number`.

**To install dependencies through Artifactory:**

1. From the project directory, run install (with or without build-info flags).

   With build information:

   ```bash
   jf npm install --build-name=<build-name> --build-number=<build-number>
   ```

   Where:

   * \<build-name>: A name for this build (for example, `my-app`)
   * \<build-number>: A build identifier (for example, `1` or `$BUILD_NUMBER`)

   For example:

   ```bash
   jf npm ci --build-name=my-app --build-number=$BUILD_NUMBER
   ```

2. Or install without recording build information:

   ```bash
   jf npm install
   ```

***

## How do I publish a package to Artifactory?

Publish your package to the configured Artifactory repository. Include build information for traceability.

**To publish the package to Artifactory:**

* Run:

  ```bash
  jf npm publish --build-name=<build-name> --build-number=<build-number>
  ```

  Where:

  * \<build-name>: A name for this build (for example, `my-app`)
  * \<build-number>: A build identifier (for example, `1`)

  For example:

  ```bash
  jf npm publish --build-name=my-app --build-number=1
  ```

***

## How do I enrich and publish build information?

After running npm commands with `--build-name` and `--build-number`, enrich the build-info with environment and Git context, then publish.

**To enrich and publish build information:**

1. Optional — capture environment variables (CI build URL, job name, and so on):

   ```bash
   jf rt build-collect-env <build-name> <build-number>
   ```

2. Optional — attach Git commit metadata (requires a `.git` directory in the current or a parent directory):

   ```bash
   jf rt build-add-git <build-name> <build-number>
   ```

3. Publish the build-info to Artifactory:

   ```bash
   jf rt build-publish <build-name> <build-number>
   ```

   Where:

   * \<build-name>: The same value you passed to npm commands with `--build-name`
   * \<build-number>: The same value you passed with `--build-number`

   For example:

   ```bash
   jf rt build-collect-env my-app 1
   jf rt build-add-git my-app 1
   jf rt build-publish my-app 1
   ```

   (`jf rt bp` is an alias for `jf rt build-publish`.)

> The `build-collect-env` and `build-add-git` steps are optional but recommended in CI/CD pipelines. They add traceability to your builds — linking each build to its source commit and build environment.

**Simplified alternative:** If you do not need fine-grained control over each step, use a single publish command:

```bash
jf rt build-publish my-app 1 --collect-env --collect-git-info
```

`--collect-env` replaces `build-collect-env` and `--collect-git-info` replaces `build-add-git`. The `--collect-git-info` flag also requires a `.git` directory. Use `--dry-run` to preview the build-info before publishing:

```bash
jf rt build-publish my-app 1 --collect-env --collect-git-info --dry-run
```

***

## Complete Workflow Example

```bash
# 1. Configure npm (run once per project)
jf npm-config --server-id-resolve=my-server --repo-resolve=npm-virtual --server-id-deploy=my-server --repo-deploy=npm-local

# 2. Install dependencies
jf npm install --build-name=my-app --build-number=1

# 3. Publish the package
jf npm publish --build-name=my-app --build-number=1

# 4. Enrich and publish build information (requires .git directory)
jf rt build-publish my-app 1 --collect-env --collect-git-info
```

***

## Verifying Success

After completing the workflow, confirm that artifacts and build-info are visible in Artifactory.

**To verify the workflow:**

1. Confirm artifacts were uploaded (adjust the repository path and package name as needed):

   ```bash
   jf rt search npm-local/my-package/
   ```

2. Confirm build-info was published:

   ```bash
   jf rt curl -XGET "/api/build/my-app/1"
   ```

   > **Note:** `jf rt curl` always exits with code 0, even on HTTP 4xx or 5xx responses. In CI scripts, do not rely on `$?` to confirm success — inspect the response body for an `"errors"` array instead.

3. Or open **Artifactory UI > Builds > my-app > 1** to view the build-info with dependencies, artifacts, environment variables, and Git context.

***

## CI/CD Integration

### Bash (Jenkins / GitLab CI)

```bash
jf config add ci-server --url=$JFROG_URL --access-token=$JFROG_ACCESS_TOKEN --interactive=false
jf npm-config --server-id-resolve=ci-server --repo-resolve=npm-virtual --server-id-deploy=ci-server --repo-deploy=npm-local
jf npm ci --build-name=$BUILD_NAME --build-number=$BUILD_NUMBER
jf npm publish --build-name=$BUILD_NAME --build-number=$BUILD_NUMBER
jf rt build-publish $BUILD_NAME $BUILD_NUMBER --collect-env --collect-git-info
```

### GitHub Actions

```yaml
# .github/workflows/build.yml
steps:
  - uses: actions/checkout@v4
  - name: Setup JFrog CLI
    uses: jfrog/setup-jfrog-cli@v4
    env:
      JF_URL: ${{ vars.JF_URL }}
      JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}
  - name: Configure npm
    run: jf npm-config --server-id-resolve=setup-jfrog-cli-server --repo-resolve=npm-virtual --server-id-deploy=setup-jfrog-cli-server --repo-deploy=npm-local
  - name: Install dependencies
    run: jf npm ci --build-name=my-app --build-number=${{ github.run_number }}
  - name: Enrich and publish build info
    run: jf rt build-publish my-app ${{ github.run_number }} --collect-env --collect-git-info
```

<Callout icon="📘" theme="info">
  Coming from the UI?

  If you have been configuring build tool integrations through the Artifactory UI under **Administration > Repositories**, the `*-config` commands create the same association between your project and Artifactory repositories — but locally, so your builds resolve dependencies through Artifactory automatically.
</Callout>

***

## Adapting for Other Build Tools

This tutorial uses npm, but the pattern is the same for all build tools:

| Build Tool | Config Command     | Build Command              | Publish Command     |
| ---------- | ------------------ | -------------------------- | ------------------- |
| npm        | `jf npm-config`    | `jf npm install`           | `jf npm publish`    |
| Maven      | `jf mvn-config`    | `jf mvn clean install`     | Via `deploy` goal   |
| Gradle     | `jf gradle-config` | `jf gradle build`          | Via publish tasks   |
| pip        | `jf pip-config`    | `jf pip install`           | `jf twine upload`   |
| Go         | `jf go-config`     | `jf go build`              | `jf go-publish`     |
| Docker     | —                  | `jf docker pull` / `build` | `jf docker push`    |
| Yarn       | `jf yarn-config`   | `jf yarn install`          | —                   |
| NuGet      | `jf nuget-config`  | `jf nuget restore`         | —                   |
| Poetry     | `jf poetry-config` | `jf poetry install`        | `jf poetry publish` |

Always finish with `jf rt build-publish <name> <number>` to send build information to Artifactory.

### End-to-End: Python (pip + twine)

```bash
# Configure
jf pip-config --server-id-resolve=my-server --repo-resolve=pypi-virtual \
    --server-id-deploy=my-server --repo-deploy=pypi-local

# Install dependencies
jf pip install -r requirements.txt --build-name=my-python-app --build-number=1

# Build and publish the package
python -m build
jf twine upload dist/* --build-name=my-python-app --build-number=1

# Enrich and publish build-info (requires .git directory)
jf rt build-publish my-python-app 1 --collect-env --collect-git-info
```

### End-to-End: Java (Maven)

```bash
# Configure
jf mvn-config --server-id-resolve=my-server \
    --repo-resolve-releases=libs-release --repo-resolve-snapshots=libs-snapshot \
    --server-id-deploy=my-server \
    --repo-deploy-releases=libs-release-local --repo-deploy-snapshots=libs-snapshot-local

# Build (artifacts deploy automatically at install phase)
jf mvn clean install -DskipTests --build-name=my-java-app --build-number=1

# Enrich and publish build-info (requires .git directory)
jf rt build-publish my-java-app 1 --collect-env --collect-git-info
```

### End-to-End: Go

```bash
# Configure
jf go-config --server-id-resolve=my-server --repo-resolve=go-virtual \
    --server-id-deploy=my-server --repo-deploy=go-local

# Build
jf go build --build-name=my-go-app --build-number=1

# Publish the module
jf go-publish v1.0.0 --build-name=my-go-app --build-number=1

# Enrich and publish build-info (requires .git directory)
jf rt build-publish my-go-app 1 --collect-env --collect-git-info
```

### End-to-End: Docker

```bash
# Login to the Docker registry
jf docker login acme.jfrog.io

# Build and push
jf docker build -t acme.jfrog.io/docker-local/my-app:1.0.0 .
jf docker push acme.jfrog.io/docker-local/my-app:1.0.0 \
    --build-name=my-docker-app --build-number=1

# Enrich and publish build-info (requires .git directory)
jf rt build-publish my-docker-app 1 --collect-env --collect-git-info
```

***

## Common Issues and Fixes

| Problem                                | Fix                                                                                                                                                                     |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "no config file was found"             | Run `jf <tool>-config` in the project directory first                                                                                                                   |
| Resolution fails with 404              | Check that the repo name in config matches an existing Artifactory repository                                                                                           |
| Build info shows 0 dependencies        | Ensure you passed `--build-name` and `--build-number` to the build command                                                                                              |
| `jf rt build-publish` fails            | Verify your server configuration has a valid access token with deploy permissions                                                                                       |
| `build-add-git`: "Could not find .git" | The command requires a `.git` directory. Run `git init && git add . && git commit -m "init"` first, or omit `--collect-git-info` if the project is not a git repository |

### Build Succeeded but Nothing Was Deployed

JFrog CLI invokes your package manager and passes native flags through unchanged. If your build finishes successfully but no artifacts appear in Artifactory (or only build-info is recorded), check whether your native tool requires you to select a target to publish:

* **Gradle (Artifactory Gradle plugin):** You must tell the plugin which publication(s) to deploy.
* **Maven:** Make sure you run a phase/goal that actually deploys (for example, `deploy`, or `install` if your setup deploys during install). The CLI accepts Maven args as-is.
* **npm / Yarn:** Install only resolves. Use `jf npm publish` (or `jf rt upload`) to push a package.

***

## Frequently Asked Questions

### What is the difference between `jf npm install` and `jf npm ci`?

`jf npm install` resolves dependencies from `package.json` and may update `package-lock.json`. `jf npm ci` installs strictly from `package-lock.json` without modifying it — preferred in CI/CD for reproducible builds. Both collect build-info when `--build-name` and `--build-number` are provided.

### How do I see available flags for `jf npm install`?

Unlike most JFrog CLI commands, `jf npm install` and `jf npm ci` forward all flags directly to the underlying npm process. Running `jf npm install --help` does **not** display JFrog CLI help — it passes `--help` to npm and attempts to contact Artifactory. To discover JFrog-specific flags (such as `--build-name` and `--build-number`), run `jf npm --help` to see the subcommand list, or `jf npm publish --help` for publish-specific options.

### Do I need to run `jf rt build-publish` after every build?

Only if you want build-info stored in Artifactory. The `--build-name` and `--build-number` flags collect build-info locally. Running `jf rt build-publish` uploads that record to Artifactory, enabling traceability, promotion, and Xray scanning.

### Can I adapt this tutorial for Maven, Gradle, or other tools?

Yes. The three-step pattern (configure, build, publish build-info) is identical for all tools.

### What if my build succeeds but no artifacts appear in Artifactory?

Check whether your build tool requires an explicit publish step. For npm, run `jf npm publish`. For Gradle, configure the Artifactory plugin's publication target.

### Is the `--run-native` flag still supported?

The `--run-native` flag on `jf npm publish` is deprecated. Use the environment variable `JFROG_RUN_NATIVE=true` instead if you need native client behaviour.

***

## Related Topics

* [Native Mode](/artifactory/docs/native-mode) — Wrapped vs Native execution modes