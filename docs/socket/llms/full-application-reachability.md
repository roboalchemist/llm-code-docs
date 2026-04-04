# Source: https://docs.socket.dev/docs/full-application-reachability.md

# Full Application Reachability

Full application Reachability enhances the precomputed reachability by filtering out CVEs that affect functions never called in both the application source code and the dependency code.

> 📘 See [Reachability Analysis](https://docs.socket.dev/docs/reachability-analysis) for an overview of all Reachability Analysis capabilities in Socket. This page is about just one of the reachability techniques that Socket offers.

The Precomputed reachability allows Socket to remove up to 60% of vulnerabilities by looking at how packages in your dependency graph call into other packages in your dependency graph.

Full application reachability uses the same underlying reachability analysis engine, but it scans both the application source code and the dependency code. **This allows the full application reachability to flag around 80% of vulnerabilities as irrelevant. For some ecosystems, the noise reduction rate is above 90%**.

The benefits of full application reachability analysis include:

* **Excellent noise reduction** – Up to 90% of all vulnerability alerts can be flagged as irrelevant.
* **Powerful triaging support** – Provides a precise list of function calls from your application source code that lead to reachable vulnerabilities, making it easier to assess impact and severity.
* **On-premise analysis** – While the analysis reads your application’s source code, it runs entirely on-premise (on your machine) and does **not** share any source code with Socket.
* **Phantom dependency detection** – [phantom dependencies](phantom-dependencies) are automatically detected and considered in the reachability analysis.

There are a few caveats to using the full application reachability analysis. It requires a small amount of manual configuration per repository and can be compute-intensive, depending on the programming language(s) and the size of the application.

Based on your organization’s security needs, you may choose to enable full application analysis for select repositories, while using [precomputed reachability analysis](precomputed-reachability) for others.

## When to use Full Application Reachability

Full application reachability is designed to be used selectively. Most customers start with precomputed reachability across their repositories and enable full application reachability only for a small number of production-critical or high-noise services where maximum precision is required.

Because full application reachability performs deep static analysis across both application code and dependencies, it is more compute-intensive by design. This trade-off allows Socket to deliver significantly higher signal and noise reduction, but it is not required to get value from reachability analysis overall.

## Running the Reachability Analysis

Make sure you have the [Socket CLI](socket-cli#how-can-i-get-my-hands-on-this)  installed.

There are also some requirements that depend on the programming language(s) used in the project scanned by the reachability analysis.

**Language-specific Requirements**

* Python
  * Python 3.11 or newer. [PyPy](https://pypy.org/) is recommended, as it can speed up the analysis 2-3x
  * [uv](https://docs.astral.sh/uv/) version 0.5 or newer
  * pyenv version 2.4 or newer is required if the system Python interpreter does not satisfy the version requirement of a project to be analyzed
* Maven (Java, Scala, Kotlin)
  * JDK 8 or newer
* Nuget (C#)
  * .NET 6 or newer
* Go
  * Same version as used to build to project

⚠️ If your project is using Gradle without a gradle.lockfile, or SBT, you must pre-generate a gradle.lockfile or CDX SBOM before invoking the reachability analysis. Learn how to do that on this [page](socket-manifest#generate-manifest-files).

To create a [scan](scans) with reachability information run:

```
socket scan create --reach
```

If you want to run the reachability analysis but not submit the scan to Socket:

```
socket scan reach
```

The reachability results are then written to a `.socket.facts.json` file in your current working directory.

## Resource and Performance Requirements

Full application reachability analysis is compute-intensive, with resource requirements varying by ecosystem and project size. This section provides guidance on memory allocation and expected analysis times.

### Factors Affecting Performance

Several factors influence the resource requirements and duration of the reachability analysis:

**Language type**

Dynamically typed languages such as JavaScript, Python, and Ruby are computationally more expensive to analyze than statically typed languages such as Java and Rust. Static type information allows the analysis to more precisely determine which functions may be called, reducing the amount of code that needs to be considered.

**Program size**

Larger programs require more resources. Program size includes not only your application code but also the size of your dependencies. A small application with many large dependencies may take longer to analyze than a large application with few dependencies.

**Number of CVEs**

The number of CVEs in your dependency graph affects performance. More CVEs typically means the analysis must consider a larger fraction of the codebase to determine reachability for each vulnerability.

**Project structure**

Splitting applications into smaller subprojects or workspaces typically results in better performance than having everything in a single project. For example, a JavaScript project with 5 million lines of code can be very computationally intensive to analyze as a single unit. However, if those 5 million lines are split across 100 workspaces, the analysis can process each workspace independently, which is typically much faster overall.

### Memory Requirements

All ecosystems require a minimum of 8 GB of memory. The recommended memory allocation depends on the ecosystem and project size:

| Ecosystem | Minimum Memory | Recommended Memory                    |
| --------- | -------------- | ------------------------------------- |
| npm       | 8 GB           | 32 GB (64 GB for very large projects) |
| Python    | 8 GB           | 32 GB                                 |
| Ruby      | 8 GB           | 32 GB                                 |
| Go        | 8 GB           | 16 GB                                 |
| Maven     | 8 GB           | 16 GB                                 |
| NuGet     | 8 GB           | 16 GB                                 |
| Cargo     | 8 GB           | 16 GB                                 |

### Expected Analysis Time

The table below shows expected analysis times across different ecosystems. Times are reported as percentiles across all scanned projects.

| Ecosystem | P50 (Median) | P90    | P99    |
| --------- | ------------ | ------ | ------ |
| npm       | 1 min        | 10 min | 40 min |
| Python    | 1 min        | 3 min  | 30 min |
| Ruby      | 1 min        | 3 min  | 30 min |
| Go        | 1 min        | 3 min  | 30 min |
| Maven     | 1 min        | 3 min  | 20 min |
| NuGet     | 1 min        | 3 min  | 20 min |
| Cargo     | 1 min        | 3 min  | 20 min |

<Callout icon="📘" theme="info">
  The reported times are per-project. If scanning a repository containing multiple subprojects (a monorepo), you need to multiply by the number of subprojects. Using the `--reach-concurrency` flag may be beneficial in this scenario.
</Callout>

### Troubleshooting Analysis Timeouts

If the reachability analysis is running slower than expected or is timing out, consider the following options:

**Increase the analysis timeout**

Use `--reach-analysis-timeout` to extend the analysis timeout beyond the default 10 minutes. When increasing the timeout, it is recommended to also allocate additional memory—approximately 10 GB of extra memory per additional 10 minutes of timeout.

```
socket scan create --reach --reach-analysis-timeout 1200
```

**Increase analysis memory**

Use `--reach-analysis-memory-limit` to increase the maximum available memory to the analysis (Default is 8GB). If running in CI, remember to consider if you need to use a larger runner.

```
socket scan create --reach --reach-analysis-memory-limit 32768
```

**Enable parallel workspace processing**

Use the `--reach-concurrency` flag to process multiple workspaces in parallel. This is useful for projects that contain multiple subprojects or workspaces, such as projects using npm workspaces or monorepos with subprojects located in different subdirectories.

```
socket scan create --reach --reach-concurrency 4
```

<Callout icon="⚠️" theme="warn">
  The `--reach-analysis-memory-limit` flag applies to each concurrent instance. For example, if you allocate 16 GB of memory per instance and run 4 concurrent instances, you should run the analysis on a machine with at least 64 GB of memory.
</Callout>

<br />

## How Full Application Function-level Reachability Works

### 1. Invoking the scan

The analysis is started using the [Socket CLI](socket-cli) as described [above](#running-the-reachability-analysis). You can set up the scan to run at regular intervals in your CI system or be triggered by other events depending on policy.

### 2. Scanning for CVEs

The analysis identifies all manifest files (`package.json`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`, and others) in your application. From these files, a complete list of direct and transitive dependencies, along with the dependency graph that connects them, is extracted.

Socket scans for CVEs in the dependency graph using a [standard vulnerability scan](https://docs.socket.dev/docs/vulnerability).

### 3. Computing Vulnerability Reachability

For every detected CVE, a static analysis is performed to check the reachability of the affected functions (You can learn more about Socket's static reachability analysis [here](static-reachability-analysis)).

This step involves constructing a model of your application called a call graph, which represents which functions call other functions throughout the application. Depending on the size and complexity of your codebase, this process may require significant memory and CPU resources, and can take up to a few minutes to complete for some CVEs.

### 4. Reachable vs Unreachable CVEs

If the affected function(s) are unreachable, the CVE is marked as unreachable. Unreachable CVEs are safe to ignore, as the vulnerable code cannot be invoked at runtime.

If the CVE is reachable through one or more paths, the vulnerability is flagged as *reachable*. For reachable CVEs, Socket shows the list of function calls in your dependencies that may trigger the vulnerability.

## Limitations

See the [Static Reachability Analysis](static-reachability-analysis#limitations)  for more information about what the static reachability analysis can and cannot detect.

## FAQ

### How does Socket determine which functions are affected by a CVE?

You can learn more about how the Socket team identifies functions affected by vulnerabilities in the FAQ section of the [Static Reachability Analysis](static-reachability-analysis#faq) page.

### How does *Full Application Reachability* compare to *Precomputed Reachability*

[Precomputed reachability](precomputed-reachability) analysis considers only the code within your dependencies, whereas the full application analysis also scans your application’s own source code. While the full application analysis provides better noise reduction and richer context for triaging reachable vulnerabilities, it comes with some trade-offs: it requires manual setup and is generally slower, as the static analysis is compute-intensive.