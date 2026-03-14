# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/gradle-dependency-resolution-in-ci-cd.md

# Gradle Dependency Resolution in CI/CD

Gradle projects require dependency resolution to run in the same environment where the project is built. Because `build.gradle` files can include executable logic, environment-specific paths, and private repositories, dependency analysis must occur inside the CI pipeline to ensure accurate results.

To support this, OX Security provides a CI-based dependency resolver that integrates directly into your Gradle build process.

Supported CI platforms include GitHub Actions, GitLab CI, Bitbucket Pipelines, Azure DevOps, and Jenkins, with minor configuration differences Gradle - CI\_CD integration.

Gradle dependency resolution cannot be reliably inferred through static analysis alone. Running the resolver inside the CI pipeline provides the following benefits:

* **Context awareness:** Uses the same credentials, environment variables, and repository access as the build.
* **Accurate dependency graphs:** Dependencies are captured directly from Gradle, without guessing or inference.
* **Improved SBOM quality:** The resulting SBOM reflects the dependencies actually used at build time.

This approach avoids common issues such as missing private dependencies or incorrect version resolution Gradle - CI\_CD integration.

## How the Gradle CI dependency flow works

During a typical CI run, Gradle resolves dependencies using credentials, environment variables, and internal repositories that are available only at build time. OX integrates into this flow by running a lightweight binary inside the same pipeline step.

This approach allows OX to:

* Capture the exact dependency tree resolved by Gradle.
* Generate accurate dependency graphs for each `build.gradle` file.
* Reuse collected dependency data in future scans.

A typical Gradle CI pipeline with OX integration follows these stages:

1. **Checkout source code:** The CI system pulls the repository from the source control platform.
2. **Materialize secrets:** Credentials and environment variables are injected for access to private repositories.
3. **Resolve dependencies and build:** Gradle resolves dependencies and builds the project using the native build context.
4. **Run OX dependency resolver:** The OX CI binary runs inside the pipeline and captures resolved dependency graphs.
5. **Publish artifacts:** Build artifacts are published if all verification steps succeed.

This flow ensures dependency resolution happens exactly as Gradle performs it during the build Gradle - CI\_CD integration.

## What happens after the first run

After the dependency graphs are successfully collected:

* OX stores them securely.
* Future scans reuse the stored graphs.
* The CI resolver does not need to run again unless dependencies change.

This keeps ongoing scans fast and reliable while maintaining accuracy.

## Configure Gradle Dependency Resolution in CI/CD

This procedure explains how to enable Gradle dependency resolution using the OX CI SBOM resolver.

Before you begin, make sure your Gradle project builds successfully in CI without OX.

### Step 1: Create an OX API key

[Create an API key for CI/CD integration](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines/integrating-source-control-platforms/direct-source-control-pipeline-integration/creating-ci-cd-integration-key), or reuse an existing key.

### Step 2: Store the API key as a repository secret

Define the following repository secret in your CI system:

* `OX_API_KEY=<your_api_key>`

The secret must be available to the pipeline stage that runs the OX CI resolver Gradle - CI\_CD integration.

### Step 3: Ensure Git metadata is available

OX requires Git metadata to associate dependency data with the correct repository and commit.

**Supported platforms**

The following CI platforms are supported natively and require no additional configuration:

* GitHub
* GitLab
* Bitbucket
* Azure DevOps

Git metadata is collected automatically.

**Jenkins pipelines**

For Jenkins, you must explicitly set the following environment variables:

* `GIT_URL`
* `GIT_BRANCH`
* `GIT_COMMIT`

Use the Jenkins Git plugin to populate these values. An example is provided in the appendix Gradle - CI\_CD integration.

### Step 4: Add a pipeline stage for the OX resolver

Add a new pipeline stage with the following placement rules:

* Run the stage **after** the Gradle build step
* Run the stage **before** any OX blocking or enforcement stages, if used

This ensures Gradle has fully resolved dependencies before OX collects them Gradle - CI\_CD integration.

### Step 5: Download and run the OX CI SBOM resolver

In the new pipeline stage:

1. Download the `ox-ci-sbom` binary for your runner architecture:

AMD64: <https://download.cloud.ox.security/latest/amd64/ox-ci-sbom>\
ARM64: <https://download.cloud.ox.security/latest/arm64/ox-ci-sbom>

1. Grant execute permissions.
2. Run the binary.

The resolver automatically detects all `build.gradle` files and captures the resolved dependency graph Gradle - CI\_CD integration.

### Step 6: Verify successful execution

After the pipeline runs:

* Confirm the `ox-ci-sbom` client completes successfully.
* Verify that a success message appears in the pipeline logs.

If the resolver fails, dependency data is not sent to OX Gradle - CI\_CD integration.

### Step 7: Enable the capability for your organization

After the first successful run, contact OX Support and request enablement of the Gradle CI SBOM resolver for your organization.

This step is required for results to appear in OX.

### \[Optional] Improve performance using parallel execution

The OX CI SBOM resolver can process Gradle dependency data in parallel to reduce execution time.

By default, the resolver runs with a conservative level of parallelism. You can explicitly allow it to use multiple CPU cores available on the CI runner.

This is useful for repositories with:

* Multiple `build.gradle` files
* Large dependency graphs
* Long Gradle resolution times

**How parallel execution works**

When enabled, the resolver runs multiple parsing threads in parallel.\
Each thread processes Gradle dependency data independently.

The maximum number of parallel threads is limited by the number of CPU cores available to the machine running the pipeline step, such as a container or pod in your CI environment.

**To enable parallel execution, define the following environment variable in your CI pipeline:**

```
OX_USE_CPUS_NUM=N
```

Where `N` is the number of CPU cores the resolver is allowed to use.

For example:

* `OX_USE_CPUS_NUM=2` limits execution to two cores
* `OX_USE_CPUS_NUM=4` allows up to four parallel threads

**Recommendations**

* Set this value based on the CPU resources allocated to your CI runner.
* Avoid setting a value higher than the number of available cores.
* Increasing this value improves performance but does not affect scan accuracy or results.

This setting is optional and can be adjusted without changing the pipeline structure.
