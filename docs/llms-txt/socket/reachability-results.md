# Source: https://docs.socket.dev/docs/reachability-results.md

# Reachability Results

Result categories for precomputed and full application reachability analyses

The reachability result types fall into 3 main categories based on the analysis outcome: **Concluded** (a result was found), **Awaiting Conclusion** (a result is expected later), or **Inconclusive** (no result is possible with the current reachability setup).

The CVE Reachability filter demonstrates this categorization:

<Image alt="Socket's CVE Reachability filter" align="center" width="350px" border={true} src="https://files.readme.io/9fbfc896f369cb4a09da3421c6fb54893b8fb806ec4cd3c40c1739b781f605e0-image.png">
  Socket's CVE Reachability filter
</Image>

### Concluded

#### Reachable (tier 1 only)

There is at least one chain of function calls from the application code through the dependencies that may trigger the CVE. This categorization is only possible when using tier 1 full application analysis.

API type: `'reachable'`

#### Potentially reachable (tier 2 only)

There is at least one chain of calls from either a direct dependency or a dependency at least 3 steps upstream from the vulnerable package in the dependency tree, that may trigger the CVE. This categorization is only possible when using the tier 2 precomputed analysis.

If you run a tier 1 full application analysis on projects with potentially reachable CVEs, these CVEs would either go to the `'reachable'` or the `'unreachable'` category, depending on how the application code interacts with its dependencies.

API type: `'maybe_reachable'`

#### Unreachable

There is no chain of calls that trigger the CVEs. Unreachable CVEs are unexploitable and therefore safe to ignore.

API type: `'unreachable'`

### Awaiting Conclusion

#### Pending precomputation (tier 2 only)

Socket does not have the reachability results precomputed for the particular chain of dependencies leading to the package with the CVE. Socket will queue the chains for analysis and then process them later. Under normal load scenarios, the chains will be processed within a few minutes.

Socket scans are currently immutable, so you will have to conduct a new scan for the CVEs to move out of the pending category.

API type: `'pending'`

#### Not yet supported

Socket's reachability team has not yet classified the functions in the vulnerable package responsible for the CVE. You can learn more about the process of curating CVEs with reachability information [here](static-reachability-analysis#how-does-socket-know-which-parts-of-a-package-are-affected-by-a-vulnerability).

API type: `'missing_support'`

### Inconclusive

#### Direct Dependency (tier 2 only)

The CVE is in a direct dependency, which makes it impossible to use the precomputed tier 2 analysis. This categorization should be seen as a special case of unknown reachability, only possible when using tier 2 analysis.

API type: `'direct_dependency'`

#### Not determinable

Socket's reachability team has analyzed the CVE and determined that reachability analysis is not possible. Most non-determinable CVEs affect CLIs or binaries that are not meant to be used from code.

API type: `'undeterminable_reachability'`

#### Unknown

CVEs can be classified as unknown for various reasons. Typically, it's because of issues encountered during a tier 1 analysis. A common example is when running a tier 1 analysis on a project that uses private dependencies where dependencies are not preinstalled. In this scenario, it's not possible for Socket to auto-install the missing dependencies, and any CVEs in private dependencies or dependencies of private dependencies will be classified as unknown.

You should consult your tier 1 analysis logs for more information if you have unknown CVEs.

API type: `'unknown'`

#### Error

An error prevented the reachability analysis from classifying the CVE. In the case of a tier 1 analysis, you can consult the logs for more information. For tier 2, reach out to Socket's support.

API type: `'error'`