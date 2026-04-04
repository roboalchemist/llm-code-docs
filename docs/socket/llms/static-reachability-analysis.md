# Source: https://docs.socket.dev/docs/static-reachability-analysis.md

# Static Reachability Analysis

Socket’s reachability analysis is based on static analysis of both your application’s source code and its dependencies.

An important advantage of Socket's SCA over other traditional vulnerability scanners is its reachability analysis that determines which vulnerabilities are actually reachable from the entry points of your project. This is important because in most projects, the majority of vulnerabilities (typically more than 80%) are not reachable and thus not exploitable.

The Tier 1 and Tier 2 reachability analyses are powered by advanced static analysis techniques that, depending on the [analysis tier](reachability-analysis#reachability-maturity-levels), scan both your application’s source code and its dependencies. This enables the analysis to build a detailed model of how dependencies are used within your application.

Built on decades of cutting-edge research in static analysis, the tool is designed to handle complex language features effectively - including reflection in Java and dynamic reads and writes in JavaScript.

Socket’s reachability analysis can **identify vulnerabilities not just in direct dependencies, but also in indirect (transitive) ones** - including dependencies of dependencies, and so on, to any level of depth.

(Read more about Socket's approach to reachability analysis in [this blog post](https://www.coana.tech/resources/article/the-coana-approach-to-reachability-analysis)).

The advantages of the static reachability analysis used by Socket are:

* Unlike other vendors, you don't have to install disruptive runtime agents in your production environment to conduct reachability analysis.
* In [Tier 2](precomputed-reachability) and [Tier 3](module-reachability) modes, the reachability analysis is available to all existing Socket users on the *team* and *enterprise* plans without any additional setup. In [Tier 1](dependency-reachability) mode, it runs via the [Socket CLI](socket-cli) that automatically gathers all the information needed to perform the analysis on your project, making it extremely easy to adopt.
* It uses tailored static analysis for each programming language, making it exceptionally accurate and capable of reasoning about the reachability of vulnerabilities deep down in dependency graphs.

## Limitations

There are some limitations and caveats to the reachability analysis.

### Accuracy

We are committed to building highly accurate reachability analyses. However, no analysis is ever perfect, and in very rare cases, vulnerabilities may be incorrectly reported as unreachable.

To minimize these inaccuracies, we design language-specific static analyses capable of handling complex language features—such as reflection in Java and dynamic reads and writes in JavaScript—effectively.

Additionally, our reachability analysis is intentionally conservative: a vulnerability will only be marked as unreachable if there is strong confidence that it truly cannot be exploited.

### Performance

Reachability analysis is computationally more expensive than traditional vulnerability scanning, which may result in long-running scans for certain types of projects. This is only relevant for [tier 1 full application reachability](full-application-reachability).

### Scope

Socket's static reachability analysis examines how your code interacts with its dependencies, and how the code of those dependencies interacts with their own dependencies, continuing recursively through the entire dependency graph.

However, the analysis is limited to interactions that occur within code and does not consider uses of dependencies that happen outside of code. For example, if you have a dependency on a build tool that you only invoke through its command-line interface, the reachability analysis will mark all vulnerabilities downstream from that CLI tool as unreachable—since there is no code-level interaction to trace.

When a vulnerability exists in a package that is primarily intended to be used as a CLI tool, we classify its reachability status as [**not determinable**](reachability-results#not-determinable).

The analysis includes a best-effort mechanism to account for packages that are loaded through reflective mechanisms. For example, classes loaded via Java properties files are considered potentially reachable even though they are not directly referenced in application code.

## JVM and .NET

Socket’s static reachability analysis for JVM and .NET used in the [tier 1 and tier 2](reachability-analysis#reachability-maturity-levels) modes, does not operate at the function level. Instead, it constructs a cross-dependency module load graph.

This approach is chosen because it works effectively across both source code and bytecode. That flexibility is especially valuable in full application reachability mode, where it allows Socket to perform reachability analysis without requiring the application to be built, making both the analysis faster and the setup process significantly easier.

While this method isn’t true function-level analysis, it still achieves noise reduction rates comparable to function-level reachability in other ecosystems.

## FAQ

#### How does Socket know which parts of a package are affected by a vulnerability?

Our dedicated reachability team focuses specifically on answering that question. Here’s how the process works:

1. **Vulnerability disclosure:** When a new vulnerability is reported, the reachability team at Socket is alerted.
2. **In-depth investigation:** A team member conducts a detailed analysis to understand how the vulnerability impacts the package. This includes:
   * Reviewing the vulnerability advisory description.
   * Studying the documentation of the affected package.
   * Installing and inspecting the package’s code.
   * Using internal AI tools to extract as many insights as possible.
3. **Reachability specification:** The team creates a specification that clearly outlines which parts of the package, usually specific functions, are affected.
4. **Peer review:** Another team member reviews the specification before it’s published.

#### What happens if Socket's analysis doesn't yet have a specification for a vulnerability?

In that case the vulnerability is still included in the report, but it is marked with an *unknown* reachability status. We strive to add support for all new vulnerabilities within 24 hours of their public disclosure.

#### What if a vulnerability cannot be tied to a specific part of a package?

We use a fallback mechanism to handle cases where a vulnerability cannot be tied to a specific part of a package. This often includes vulnerabilities in packages used as Command Line Interface (CLI) tools rather than libraries. For these cases, we classify the reachability of the vulnerability as *unknown* and provide guidance on what you should manually check to determine whether your application is affected.

Many of these vulnerabilities are safe to ignore in most scenarios — for example, if the vulnerability is in a package typically used only during the application’s build phase, such as [CVE-2023-45133](https://github.com/advisories/GHSA-67hx-6x53-jw92). If your manual assessment concludes that a vulnerability is irrelevant to your context, we recommend using [alert triage](alert-actions-and-triage-functionality) to ignore it.