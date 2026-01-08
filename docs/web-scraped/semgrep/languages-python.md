# Python support

Source: https://semgrep.dev/docs/languages/python

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- Python**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [python](/docs/tags/python)Python support
tipSemgrep’s Python coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## Python support in Semgrep Code[​](#python-support-in-semgrep-code)
Semgrep Code is a static application security testing (SAST) tool that detects security vulnerabilities in your first-party code.

### Analyses and frameworks[​](#analyses-and-frameworks)

- Framework-specific control flow analysis
- Interfile analysis (cross-file)
- Interprocedural analysis (cross-function)
- All analyses performed by [Semgrep Community Edition (CE)](#python-support-in-semgrep-ce)

## Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

In addition to rules, the Semgrep engine itself can analyze code and implicit dataflows in the context of the following supported frameworks:

**Framework / library****Category**DjangoWeb frameworkFlaskWeb frameworkFastAPIWeb framework
**In addition, Semgrep Code supports 100+ libraries &amp; frameworks based on their overall popularity.**NoLibraryCategory0bcryptCryptographic Library1cryptographyCryptographic Library2passlibCryptographic Library3pycryptoCryptographic Library4pycryptodomeCryptographic Library5pycryptodomexCryptographic Library6rsaCryptographic Library7aiomysqlDatabase Library8aiopgDatabase Library9aiosqliteDatabase Library10djangoDatabase Library11djangoormDatabase Library12mysql-connectorDatabase Library13mysqldbDatabase Library14peeweeDatabase Library15pep249Database Library16ponyormDatabase Library17psycopg2Database Library18pymongoDatabase Library19pymssqlDatabase Library20pymysqlDatabase Library21pyodbcDatabase Library22sqlalchemyDatabase Library23sqlobjectDatabase Library24dillDeserialization Library25joblibDeserialization Library26jsonpickleDeserialization Library27langDeserialization Library28numpyDeserialization Library29pandasDeserialization Library30pyyamlDeserialization Library31ruamelDeserialization Library32ruamel.yamlDeserialization Library33torchDeserialization Library34aiofileFile System Library35djangoFile System Library36fileinputFile System Library37fsFile System Library38ioFile System Library39linecacheFile System Library40openpyxlFile System Library41osFile System Library42pickleshareFile System Library43pillowFile System Library44shelveFile System Library45shutilFile System Library46stdlibFile System Library47stdlib2File System Library48stdlib3File System Library49tempfileFile System Library50tomlFile System Library51ldap3LDAP Library52stdlibLibrary With Code Execution Capabilities53stdlib2Library With Code Execution Capabilities54stdlib3Library With Code Execution Capabilities55aiohttpNetwork Library56boto3Network Library57botocoreNetwork Library58httplib2Network Library59httpxNetwork Library60paramikoNetwork Library61pycurlNetwork Library62requestsNetwork Library63urllib3Network Library64commandsOS Interaction Library65dotenvOS Interaction Library66osOS Interaction Library67paramikoOS Interaction Library68popen2OS Interaction Library69stdlibOS Interaction Library70stdlib2OS Interaction Library71stdlib3OS Interaction Library72subprocessOS Interaction Library73libxml2Regex Library74reRegex Library75regexRegex Library76stdlibRegex Library77stdlib2Regex Library78stdlib3Regex Library79aws-lambdaServerless Framework80aiohttpWeb Framework81cherrypyWeb Framework82djangoWeb Framework83django-crispy-formsWeb Framework84django_allauthWeb Framework85django_channelsWeb Framework86django_rest_frameworkapiWeb Framework87fastapiWeb Framework88flaskWeb Framework89flask-jwt-extendedWeb Framework90flask-loginWeb Framework91flask-sessionWeb Framework92flask-talismanWeb Framework93flask-wtfWeb Framework94langWeb Framework95pyramidWeb Framework96starletteWeb Framework97wtformsWeb Framework98libxml2XML Parsing Library99lxmlXML Parsing Library100saxXML Parsing Library101stdlibXML Parsing Library102stdlib2XML Parsing Library103stdlib3XML Parsing Library104xmlXML Parsing Library105xml.domXML Parsing Library106xml.dom.minidomXML Parsing Library107xml.dom.pulldomXML Parsing Library108xml.etreeXML Parsing Library109xml.saxXML Parsing Library
### Benchmark results exclusive of [AI](https://semgrep.dev/docs/semgrep-assistant/overview) processing[​](#benchmark-results-exclusive-of-ai-processing)
Semgrep&#x27;s benchmarking process involves scanning open source repositories, triaging the findings, and making iterative rule updates. This process was developed and is used internally by the Semgrep security research team to monitor and improve rule performance.

Results as of **September 9, 2024**:

Benchmark true positive rate (before AI processing) for latest ruleset**84%**Lines of code scanned**~20 million**Repositories scanned**192**Findings triaged to date**~1000**
## Python support in Semgrep Supply Chain[​](#python-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

No need for lockfilesSome Python projects can be scanned **without** the need for lockfiles. See [Scan a project without lockfiles (beta)](/docs/semgrep-supply-chain/getting-started#scan-a-project-without-lockfiles-beta).

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following Python package managers:

- pip
- pip-tools
- Pipenv
- Poetry
- uv

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for Python:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license. Semgrep can help enforce this restriction.

Malicious dependency detectionSemgrep is able to detect malicious dependencies in your projects and in pull requests (PRs) or merge requests (MRs).

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

## Python support in Semgrep CE[​](#python-support-in-semgrep-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine.

### Analyses[​](#analyses)

- Single-file, cross-function constant propagation
- Single-function taint analysis
- Semantic analysis

### Coverage[​](#coverage)
tip
- Check the `license` of a rule to ensure it meets your licensing requirements. See [Licensing](/docs/licensing) for more details.

The Semgrep Registry provides the following JavaScript rulesets:

- [** `p/default`](https://semgrep.dev/p/default)
- [** `p/python`](https://semgrep.dev/p/python)
- [** `p/trailofbits`](https://semgrep.dev/p/trailofbits)
- [** `p/xss`](https://semgrep.dev/p/trailofbits)

Sample usage:

`semgrep scan --config p/python`Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [python](/docs/tags/python)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/python.md)Last updated on **Sep 30, 2025**