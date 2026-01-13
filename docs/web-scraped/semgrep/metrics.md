# Semgrep metrics

Source: https://semgrep.dev/docs/metrics

- [](/docs/)- [What&#x27;s Semgrep](/docs/faq/overview)- Semgrep metrics**On this pageSemgrep metrics
Semgrep CLI may collect aggregate metrics to help improve the product. This document describes:

- [the principles that guide our data-collection decisions](#principles)
- [how to change when Semgrep sends metrics](#automatic-collection-opt-in-and-opt-out)
- [what data is not collected](#data-not-collected)
- [what data is collected](#data-collected-as-metrics)

## Principles[​](#principles)
These principles inform our decisions around data collection:

- **Transparency**: Collect and use data in a way that is clearly explained to the user and benefits them
- **User control**: Put users in control of their data at all times
- **Limited data**: Collect what is needed, pseudoanonymize where possible, and delete when no longer necessary

## Automatic collection, opt-in, and opt-out[​](#automatic-collection-opt-in-and-opt-out)
`$ semgrep --config=myrule.yaml  # → no metrics (loading rules from local file)$ semgrep --config=p/python     # → metrics enabled (fetching Registry)$ semgrep login &amp;&amp; semgrep ci   # → metrics enabled (logged in to semgrep.dev)`
Semgrep does **not** enable metrics when running with only local configuration files or command-line search patterns.

Semgrep does enable metrics if rules are loaded from the [Semgrep Registry](https://semgrep.dev/r).
This helps maintainers improve the correctness and performance of registry rules.

Metrics may also be configured to be sent on every run, or never sent.

To configure metrics, pass the `--metrics` option to Semgrep:

- `--metrics auto`: (default) metrics are sent whenever rules are pulled from the [Semgrep Registry](https://semgrep.dev/r) or the user is logged in.
- `--metrics on`: metrics are sent on every Semgrep run
- `--metrics off`: metrics are never sent

Alternatively, set the `SEMGREP_SEND_METRICS` environment variable to `auto`, `on`, or `off`.

Note that certain Semgrep integrators turn on metrics for every run.
For example, [GitLab&#x27;s Semgrep SAST analyzer](https://gitlab.com/gitlab-org/security-products/analyzers/semgrep) uses `--metrics on` by default.

## Data NOT collected[​](#data-not-collected)
### Data NOT collected ever[​](#data-not-collected-ever)
We strive to balance our desire to collect data for improving Semgrep
with our users&#x27; need for privacy and security.
After all, we are a security tool!
The following never leave your environment and are not sent or shared with anyone.

- Source code
- Private rules

### Data NOT collected unless explicitly requested[​](#data-not-collected-unless-explicitly-requested)
The following data will never leave your environment as part of metrics.

- Filenames
- Git commit hashes, timestamps, messages, authors
- User-identifiable data about Semgrep’s findings in your code, including finding messages

This data will be sent to Semgrep AppSec Platform only if you explicitly request it,
such as with `semgrep login &amp;&amp; semgrep ci` to connect with Semgrep AppSec Platform.
Even in that case, your source code and private rules will never be sent.

## Data collected as metrics[​](#data-collected-as-metrics)
Semgrep CLI collects data to improve the user experience.
Five types of data are collected:

### Environmental[​](#environmental)
Environmental data provide contextual data about Semgrep CLI’s runtime environment, as well as information that helps debug any issues users may be facing; e.g.

- How long the command took to run
- The version of Semgrep CLI
- An [anonymous user ID](#anonymous-user-id) that identifies the machine
- IP address that triggers a run
- Value of the CI environment variable, if set
- Pseudoanonymized hash of the scanned project’s name
- Pseudoanonymized hash of the rule definitions run
- Pseduoanonymized hash of the config option.
*(Note that when a config option downloads a ruleset from the [https://semgrep.dev](https://semgrep.dev) registry, [feature usage metrics](#feature-usage) still include the ruleset name in plain text.)*

### Performance[​](#performance)
Performance data enable understanding of which rules and types of files are slow in the aggregate so Semgrep, Inc can improve the program-analysis engine, query optimizer, and debug slow rules; e.g.

- Runtime duration
- Duration of individual phases (e.g. parsing)
- Total number of rules
- Total number of files
- Project size in bytes

### Parse Rates[​](#parse-rates)
Aggregated parse rate information is reported on a per-language basis; e.g.,

- Number of targeted files
- Number of files without any parse-related error
- Number of bytes across targeted files
- Number of bytes without any parse-related error

### Errors[​](#errors)
High-level error and warning classes encountered when run; e.g.

- Semgrep’s return code
- The number of errors
- Compile-time error names, e.g., MaxFileSizeExceeded, SystemOutOfMemory, UnknownFileEncoding

### Value[​](#value)
Data that indicate how useful a run is for the end user; e.g.

- Number of raised findings
- Number of ignored findings
- Pseudoanonymized hashes of the rule definitions that yield findings
- The [features used](#feature-usage) during the scan
- The engine type requested for the scan

### Extension[​](#extension)
Additional data is reported when used in conjunction with an IDE integration, such as the [Semgrep VS Code Extension](https://github.com/semgrep/semgrep-vscode), that help us understand what IDEs are used and how helpful the integrations are for users; e.g.

- IDE being used
- Version of IDE integration
- Number of fixes triggered through the integration
- Number of findings ignored through the integration

Note: For all officially supported Semgrep IDE integrations, these metrics can be disabled via settings in the IDE. By default these settings follow any global telemetry/metrics settings the user may have already set for the IDE itself.

### Pseudoanonymization[​](#pseudoanonymization)
Certain identifying data (e.g. project URLs) are pseudoanonymized before being sent to the Semgrep, Inc backend.

&quot;Pseudoanonymized&quot; means the data are transformed using a deterministic cryptographically secure hash. When the input data are unknown, this hash is expensive to reverse. However, when input data are known, a reverse dictionary of identifiers to hashes can be built. Hence, data are anonymous only when the source values are unknown.

We use a deterministic hash to:

- Track performance and value improvements over successive runs on projects
- Remove test data from our metrics

Using a deterministic hash, however, implies:

- An entity that independently knows the value of an input datum AND who has access to Semgrep, Inc&#x27;s metrics data could access metrics for that known datum

Semgrep, Inc will:

- Treat collected metrics data as secret, using application-security best practices, including (but not limited to)

Encryption during transit and rest
- Strict access control to data-storage systems
- Application-security-policy requirements for third parties (e.g. cloud-service providers; see &quot;data sharing&quot; below)

- Only correlate hashed data to input data when these inputs are already known to Semgrep, Inc (e.g. publicly available project URLs for open-source projects, or projects that log in to the Semgrep Registry)

## Description of metrics fields[​](#description-of-metrics-fields)
CategoryFieldDescriptionUse CaseExample DatumTypeEnvironmentTimestamps (started/sent)Time when the event firedUnderstanding tool usage over time2021-05-10T21:05:06+00:00StringEvent IDA random UUID generated when sending the event.Deduplicating events in case of issues during transmission222bcccd-9dc2-4d10-ac3a-5692460e77eeString[Anonymous User ID](#anonymous-user-id)A random UUID generated on first run.Unique users per ruleset and feature. Understanding percentage of logged in users.5f52484c-3f82-4779-9353-b29bbd3193b6StringVersionSemgrep version being usedReproduce and debug issues with specific versions0.51.0StringProject hashOne-way hash of the project URLUnderstand performance and accuracy improvements`c65437265631ab2566802d4d90797b27fbe0f608dceeb9451b979d1671c4bc1a`StringRules hashOne-way hash of the rule definitionsUnderstand performance improvements`b03e452f389e5a86e56426c735afef13686b3e396499fc3c42561f36f6281c43`StringConfig hashOne-way hash of the config argumentUnderstand performance and accuracy improvements`ede96c41b57de3e857090fb3c486e69ad8efae3267bac4ac5fbc19dde7161094`StringIs authenticatedWhether the user logged in to semgrep.dev with `semgrep login`Understand popularity of logged in features`false`BooleanDeployment IDThe ID organization associated with the logged in accountUnderstand popularity of logged in features by organization1234NumberIntegration nameIf Semgrep is being called by another tool, optional name of that integrationReproduce and debug issues specific integrations`gitlab`StringCINotes if Semgrep is running in CI and the name of the providerReproduce and debug issues with specific CI providersGitLabCI v0.13.12StringClient IPIP address that triggered a runUnderstand broad ruleset usage0.0.0.0StringPerformanceDurationHow long the command took to runUnderstanding aggregate performance improvements and regressions14.13NumberTotal RulesCount of rulesUnderstand how duration is affected by #rules137NumberTotal FilesCount of filesUnderstand how duration is affected by #files4378NumberTotal BytesSummation of target file sizeUnderstand how duration is related to total size of all target files40838239NumberRule StatsPerformance statistics (w/ rule hashes) for slowest rulesDebug rule performance`[{&quot;ruleHash&quot;: &quot;7c43c962dfdbc52882f80021e4d0ef2396e6a950867e81e5f61e68390ee9e166&quot;,&quot;parseTime&quot;: 0,&quot;matchTime&quot;: 0.05480456352233887,&quot;runTime&quot;: 0.20836973190307617,&quot;bytesScanned&quot;: 0}]`StatsClass[]File StatsPerformance statistics for slowest filesDebug rule performance`[{&quot;size&quot;: 6725,&quot;numTimesScanned&quot;: 147,&quot;parseTime&quot;: 0.013289928436279297,&quot;matchTime&quot;: 0.05480456352233887,&quot;runTime&quot;: 0.20836973190307617}]`StatsClass[]ParsingTotal FilesCount of files, on a per-language basisUnderstand parsing performance143NumberTotal BytesSummation of target file size, likewise groupedUnderstand parsing performance41244NumberParsed FilesCount of files without parse errorsUnderstand parsing performance140NumberParsed BytesCount of bytes without any parse errorsUnderstand parsing performance40312NumberErrorsExit CodeNumeric exit codeDebug commonly occurring issues and aggregate error counts1NumberNumber of ErrorsCount of errorsUnderstanding avg #errors2NumberNumber of WarningsCount of warningsUnderstanding avg #warnings1NumberErrorsArray of Error Classes (compile-time-constant)Understand most common errors users encounter`[&quot;UnknownLanguage&quot;, &quot;MaxFileSizeExceeded&quot;] `ErrorClass[]WarningsArray of Warning Classes (compile-time-constant)Understand most common warnings users encounter`[&quot;TimeoutExceeded&quot;]`WarningClass[]ValueEngine requestedThe engine type requested by the userUnderstand which engines are being used; debug engine-specific problems`&quot;OSS&quot;`Engine configurationThe specific engine configurationUnderstand which engines are being used; debug engine-specific problems`{ analysis_type: &quot;Interfile&quot;, pro_langs: true, code_config: {} }`strInterfile languages usedThe languages for which the interfile engine was actually invokedUnderstand which interfile languages are being used; measure performance impact and errors`[&quot;C#&quot;]`str[Features used](#feature-usage)List of strings that identify Semgrep features usedUnderstand what features users find valuable, and what we could deprecate`[&quot;language/python&quot;, &quot;option/deep&quot;, &quot;option/no-git-ignore&quot;, &quot;key/metavariable-comparison&quot;]`ObjectRule hashes with findingsMap of rule hashes to number of findingsUnderstand which rules are providing value to the user; diagnose high false-positive rates`{&quot;7c43c962dfdbc52882f80021e4d0ef2396e6a950867e81e5f61e68390ee9e166&quot;: 4}`ObjectTotal FindingsCount of all findingsUnderstand if rules are super noisy for the user7NumberFindings per productCount of findings broken down by productUnderstand the value that each product provides to the user`{&quot;code&quot;: 5, &quot;secrets&quot;: 7, &quot;supply-chain&quot;: 10}`ObjectTotal NosemsCount of all `nosem` annotations that tell semgrep to ignore a findingUnderstand if rules are super noisy for the user3Number
|Extension||||||
|         |Machine ID|A random UUID generated by the IDE itself|Understanding number of unique users using IDE integrations|`222bcccd-9dc2-4d10-ac3a-5692460e77ee`|String|
|         |Is New App Install|If the user just installed the IDE integration|Understand common issues with setting up IDE integrations|`false`|Boolean|
|         |Session ID|A random UUID generated everytime the integration starts up, usually when opening a project|Understand errors that commonly happen together, deduplicate errors|`222bcccd-9dc2-4d10-ac3a-5692460e77ee`|String|

|         |Integration version|Current version of the IDE integration|Reproduce and debug issues with specific versions|`1.8.0`| String|
|         |Integration type|IDE being used|Reproduce and debug issues with specific integrations|`vscode`|String|
|         |Autofix count|How many autofixes have been triggered through the integration|Understand the value that the integration provides to the user in helping remediate code issue|10|Number|
|         |Ignore count|How many findings have been ignored by the user through the integration|Understand the quality and noisiness of rules|5|Number|

### Anonymous user ID[​](#anonymous-user-id)

`anonymous_user_id: &quot;5f52484c-3f82-4779-9353-b29bbd3193b6&quot;`

To help improve Semgrep products, the Semgrep CLI generates a Universally Unique Identifier (UUID) which is saved locally to a `~/.semgrep/settings.yml` file when the ID does not already exist.

The Semgrep team uses this ID to help answer the following questions:

- 

How many people use a given rule/ruleset/snippet?

This enables the Semgrep team to assess their performance,
and we&#x27;re planning to make these numbers public for all rule authors in the community.

- 

What percentage of users log in?

We use this to evaluate our success as we build new authenticated features for the Semgrep Cloud Platform.

- 

How often are individual subcommands and CLI features used?

This helps our product and developer experience teams measure feature adoption rate, analyze anonymized usage, and compare cohort behavior to improve our product offerings.

### Feature usage[​](#feature-usage)

`&quot;features&quot;: [&quot;language/python&quot;, &quot;option/deep&quot;, &quot;option/no-git-ignore&quot;, &quot;key/metavariable-comparison&quot;]`

Examples of such features are: languages scanned, CLI options passed, keys used in rules, or certain code paths reached, such as using an :include instruction in a .semgrepignore file.
These strings do NOT include user data or specific settings.
As an example, for `semgrep scan --output=secret.txt` Semgrep sends `&quot;option/output&quot;` but will NOT send `&quot;option/output=secret.txt&quot;`.

The list of features tracked as of June 2022 is:

- `language`: What languages were scanned
- `cli-flag`/`cli-envvar`: What options were configured (does NOT include their value)
- `config`: What method was used to retrieve rules (does NOT include any of the rule)
- `registry-query`: The value of a `--config r/foo.bar.baz` setting, limited to the first word (e.g. `r/foo..` in this example)
- `ruleset`: The value of a `--config p/foobar` setting
- `semgrepignore`: Whether an `:include` statement was used in a .semgrepignore file
- `subcommand`: What subcommand was used (e.g. `scan` or `ci`)

The Semgrep team uses this to answer the following questions:

- 

How many people use a given feature?

This guides our development,
and lets us decide when and how to deprecate features.

- 

How does feature usage affect finding counts, error counts, and performance?

We use this to evaluate experimental features
and understand their production-readiness.

Engine requested (OSS, Pro, Interfile)

The engine requested is stored separately from the other features. This is the
engine indicated by the user through app toggles or CLI flags. We use this for
debugging as well as to understand which engines people are using.

### Sample metrics[​](#sample-metrics)
This is a sample blob of the aggregate metrics described above:

`{    &quot;started_at&quot;: &quot;2021-05-10T21:05:06+00:00&quot;,    &quot;sent_at&quot;: &quot;2021-05-10T21:05:09+00:00&quot;,    &quot;event_id&quot;: &quot;222bcccd-9dc2-4d10-ac3a-5692460e77ee&quot;,    &quot;anonymous_user_id&quot;: &quot;5f52484c-3f82-4779-9353-b29bbd3193b6&quot;,    &quot;environment&quot;: {        &quot;version&quot;: &quot;0.51.0&quot;,        &quot;ci&quot;: &quot;true&quot;,        &quot;configNamesHash&quot;: &quot;ede96c41b57de3e857090fb3c486e69ad8efae3267bac4ac5fbc19dde7161094&quot;,        &quot;projectHash&quot;: &quot;c65437265631ab2566802d4d90797b27fbe0f608dceeb9451b979d1671c4bc1a&quot;,        &quot;rulesHash&quot;: &quot;b03e452f389e5a86e56426c735afef13686b3e396499fc3c42561f36f6281c43&quot;,        &quot;isAuthenticated&quot;: false    },    &quot;performance&quot;: {        &quot;runTime&quot;: 37.1234233823,        &quot;numRules&quot;: 2,        &quot;numTargets&quot;: 573,        &quot;totalBytesScanned&quot;: 33938923,        &quot;ruleStats&quot;: [{          &quot;ruleHash&quot;: &quot;7c43c962dfdbc52882f80021e4d0ef2396e6a950867e81e5f61e68390ee9e166&quot;,          &quot;parseTime&quot;: 0,          &quot;matchTime&quot;: 0.05480456352233887,          &quot;runTime&quot;: 0.20836973190307617,          &quot;bytesScanned&quot;: 0        }],        &quot;fileStats&quot;: [{          &quot;size&quot;: 6725,          &quot;numTimesScanned&quot;: 147,          &quot;parseTime&quot;: 0.013289928436279297,          &quot;matchTime&quot;: 0.05480456352233887,          &quot;runTime&quot;: 0.20836973190307617        }]    },    &quot;parse_rate&quot;: {      &quot;python&quot;: {        &quot;num_targets&quot;: 102,        &quot;targets_parsed&quot;: 101,        &quot;num_bytes&quot;: 985123,        &quot;bytes_parsed&quot;: 993419      },      &quot;ruby&quot;: {        &quot;num_targets&quot;: 12,        &quot;targets_parsed&quot;: 12,        &quot;num_bytes&quot;: 341027,        &quot;bytes_parsed&quot;: 341027      }    },    &quot;errors&quot;: {        &quot;returnCode&quot;: 1,        &quot;errors&quot;: [&quot;UnknownLanguage&quot;],        &quot;warnings&quot;: [&quot;MaxFileSizeExceeded&quot;, &quot;TimeoutExceeded&quot;]    },    &quot;value&quot;: {        &quot;ruleHashesWithFindings&quot;: {&quot;7c43c962dfdbc52882f80021e4d0ef2396e6a950867e81e5f61e68390ee9e166&quot;: 4},        &quot;numFindings&quot;: 7,        &quot;numIgnored&quot;: 3,        &quot;features&quot;: [&quot;language/python&quot;, &quot;option/deep&quot;, &quot;option/no-git-ignore&quot;, &quot;key/metavariable-comparison&quot;],        &quot;engineRequested&quot;: &quot;OSS&quot;,        &quot;engineConfig&quot;: { analysis_type: &quot;Intraprocedural&quot;, pro_langs: false }    }}`
## Data collected when explicitly requested[​](#data-collected-when-explicitly-requested)
For Semgrep AppSec Platform users running `semgrep ci` while logged in,
data is sent to power your dashboard, notification, dependency search, and finding management features.
These data are ONLY sent when using `semgrep ci` in a platform-connected mode
and are not sent when not logged in.

Three types of data are sent to Semgrep, Inc servers for this logged-in use case: scan data, findings data, and dependencies data.

**Scan data** provide information on the environment and performance.
They power dashboards, identify anomalies with the product, and are needed for billing.
The classes of scan data are:

- Project identity (e.g., name, URL)
- Scan environment (e.g., CI provider, OS)
- Author identity (e.g., committer email)
- Commit metadata (e.g., commit hash and timestamp)
- Review and review-requester identifying data (e.g., pull-request ID, branch, merge base, request author)
- Scan metadata, including type of scan and scan parameters (e.g., paths scanned and extensions of ignored files)
- Timing metrics (e.g., time taken to scan per-rule and per-path)
- Parse metrics (e.g., number of files targeted and parsed per-language)
- Semgrep CLI environment (e.g., version, interpreter, timestamp)

**Findings data** are used to provide human readable content for notifications and integrations,
as well tracking results as new, fixed, or duplicate. The classes of findings data are:

- Check ID and metadata (as defined in the rule definition; e.g., OWASP category, message, severity)
- Code location, including file path, that triggered findings
- A one-way hash of a unique code identifier that includes the triggering code content
- Dependency name and version (only sent when using Semgrep Supply Chain)
- Source code is NOT collected

**Dependencies data** are used to power Dependency Search and License Compliance. The classes of
dependencies data are:

- Package name (e.g., lodash)
- Package version (e.g., 1.2.3)
- File path for lockfile (e.g., frontend/yarn.lock)
- Analysis of external dependency calls. (e.g., from flask import Response, Response(status=204))

## Debugging data collected when traces are requested[​](#debugging-data-collected-when-traces-are-requested)
To help debug performance issues, Semgrep CLI can send traces, enabled via `--trace`.
Traces are never sent unless the `--trace` flag is included.

There are three modes of tracing.

- Info (`--trace`): basic tracing. Sends timings about each file as it undergoes pre-processing and then matching. Includes the file path and sometimes rule names.
- Debug (`--trace` with `SEMGREP_TRACE_LEVEL=debug`): debug tracing. Sends additional timings, particularly around functions run during taint analysis.
- Trace (`--trace` with `SEMGREP_TRACE_LEVEL=trace`): even more detailed debug tracing.

All traces are sent in Opentelemetry format and may include:

- Semgrep function currently running (e.g. `Match_tainting_mode.check_rules`)
- Start time (e.g. `1718775054055113`)
- Duration (e.g. `934956`)
- Path (e.g. `test/example/test_code.py`)
- Size of a file in bytes (e.g. `12927`)
- Rule name (e.g. `tainted-sql-from-http-request`)
- Is a taint rule (e.g. `true`)

Additionally, summary data is always included in the top level trace, such as:

- Repo name (e.g. `semgrep-app`)
- Folder name (e.g. `tests`)
- Number of matches (e.g. `2`)
- Number of errors (e.g. `1`)
- Number of OSS rules (e.g. `12`)
- Number of targets (e.g. `128`)
- Languages (e.g. `Java: true`)
- Is a diff scan (e.g. `false`)
- Is an interfile scan (e.g. `true`)
- Other scan settings of a similar nature. Summary data will only include information that `semgrep ci` has access to.

Additionally, informational, warning, and error logs will be included when
tracing is enabled, which may include:

- Stacktraces from when Semgrep crashes
- Warnings about high memory usage
- Informational logs about which stage of scanning Semgrep is performing

No information will be sent in the info mode that would not be sent by `semgrep ci`.

In debug and trace mode only, traces may also include:

- Hashed function names (e.g. `d40fdc8ef9bf7b7dd1b014533a58a05e9b98d7dd856784352201388fe5e22673`)
- Hashed variable names (e.g. `0268934f5c43d1b5fc7d52d9efe17c69f1144b108c384c3513cbe493043712b3`)

These data help us establish if a function is being analyzed for taint more times than expected.

Debug and trace mode are meant for one-off debugging of slow scans, and data from these trace modes will not be retained for more than a week.

## Registry fetches[​](#registry-fetches)
Certain Registry resources require log-in to the Semgrep Registry. Log in may be performed
using your project URL, or a Semgrep.dev API token. When using these resources, your project&#x27;s
identity will be recorded by the Semgrep Registry servers.

## Data sharing[​](#data-sharing)
We use some third party companies and services to help administer and provide Semgrep, for example for hosting, customer support, product usage analytics, and database management. These third parties are permitted to handle data only to perform these tasks in a manner consistent with this document and are obligated not to disclose or use it for any other purpose.

We do not share or sell the information provided to us with other organizations without explicit consent, except as described in this document.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/metrics.md)Last updated on Oct 13, 2021**