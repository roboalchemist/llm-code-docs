# JavaScript support

Source: https://semgrep.dev/docs/languages/javascript

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported languages- JavaScript**On this page- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [Node.js](/docs/tags/node-js)- [javascript](/docs/tags/javascript)JavaScript support
tipSemgrep’s JavaScript coverage leverages framework-specific analysis capabilities that are not present in Semgrep Community Edition (CE). As a result, many framework specific Pro rules will **fail** to return findings if run on Semgrep CE. To ensure full security coverage, run: `semgrep login &amp;&amp; semgrep ci`.

## JavaScript support in Semgrep Code[​](#javascript-support-in-semgrep-code)
Semgrep Code is a static application security testing (SAST) tool that detects security vulnerabilities in your first-party code.

### Analyses and frameworks[​](#analyses-and-frameworks)

- Framework-specific control flow analysis
- Interfile analysis (cross-file)
- Interprocedural analysis (cross-function)

- All analyses performed by [Semgrep Community Edition (CE)](#javascript-support-in-semgrep-ce)

### Coverage[​](#coverage)
Semgrep aims to provide comprehensive and accurate detection of common OWASP Top 10 issues in source code. Semgrep uses **rules**, which are instructions based on which it detects patterns in code. These rules are usually organized in rulesets.

By default, Semgrep Code provides you with the [** `p/comment`](https://semgrep.dev/p/comment) and [** `p/default`](https://semgrep.dev/p/default) rulesets. These rulesets provide the most accurate and comprehensive coverage across Semgrep&#x27;s supported languages.

In addition to rules, the Semgrep engine itself can analyze code and implicit dataflows in the context of the following supported frameworks:

Supported frameworksType of frameworkExpressWeb frameworkKoaWeb frameworkHapiWeb frameworkNestJSWeb frameworkNextJSWeb framework
**Semgrep Code supports 50+ libraries &amp; frameworks based on their overall popularity.**Supported librariesType of library`axios`Network library`nodemail`Network library`node-fetch`Network library`needle`Network library`http`Network library`https`Network library`net`Network library`http2`Network library`got`Network library`request`Network library`marked`Markdown library`dot`Template engine`child-process`OS interaction library`nestjs`Web framework`express`Web framework`koa`Web framework`hapi`Web framework`sqlite`Database library`sqlite3`Database library`typeorm`Database library`mongoose`Database library`mongodb`Database library`knex`Database library`mikro-orm`Database library`@mikro-orm/core`Database library`@mikro-orm/better-sqlite`Database library`@mikro-orm/entity-generator`Database library`@mikro-orm/knex`Database library`@mikro-orm/libsql`Database library`@mikro-orm/mariadb`Database library`@mikro-orm/migrations-mongodb`Database library`@mikro-orm/migrations`Database library`@mikro-orm/mongodb`Database library`@mikro-orm/mssql`Database library`@mikro-orm/mysql`Database library`@mikro-orm/postgresql`Database library`@mikro-orm/reflection`Database library`@mikro-orm/seeder`Database library`@mikro-orm/sqlite`Database library`pg`Database library`pg-native`Database library`pg-pool`Database library`mysql`Database library`mysql2`Database library`sequelize`Database library`libxml`XML parsing library`xpath`XML parsing library`puppeteer`Library with code execution capabilities`vm2`Library with code execution capabilities`vm`Library with code execution capabilities`rimraf`File System Library`papaparse`File system library`fs-extra`File system library`fs`File system library`sharp`File system library`path`File system library`webcrypto`Cryptographic library`crypto`Cryptographic library`http-body`Express middleware`cors`Express middleware`express-session`Express middleware`helmet`Express middleware`@koa/cors`Koa middleware`lodash`Utility library`validator`String validation library`escape-string-regexp`String sanitization library`date-fns`Date manipulation library`moment`Date manipulation library`luxon`Date manipulation library`dayjsfns`Date manipulation library`mongo-sanitize`String sanitization library`express-mongo-sanitize`String sanitization library
#### Benchmark results exclusive of [AI](/docs/semgrep-assistant/overview) processing[​](#benchmark-results-exclusive-of-ai-processing)
Semgrep&#x27;s benchmarking process involves scanning open source repositories, triaging the findings, and making iterative rule updates. This process was developed and is used internally by the Semgrep security research team to monitor and improve rule performance.

Results as of **February 25, 2025**:

BenchmarkValueTrue positive rate (before AI processing) for latest `p/default` ruleset63%Lines of code scanned~8 millionRepositories scanned153Findings triaged to date~600
## JavaScript support in Semgrep Supply Chain[​](#javascript-support-in-semgrep-supply-chain)
Semgrep Supply Chain is a software composition analysis (SCA) tool that detects security vulnerabilities in your codebase introduced by open source dependencies.

### Supported package managers[​](#supported-package-managers)
Semgrep supports the following JavaScript package managers:

- npm
- Yarn
- pnpm

### Analyses and features[​](#analyses-and-features)
The following analyses and features are available for JavaScript:

Reachability analysisReachability refers to whether or not a vulnerable code pattern from a dependency is used in the codebase that imports it. In Semgrep Supply Chain, both a dependency&#x27;s vulnerable version and code pattern must match for a vulnerability to be considered reachable.

License detectionSemgrep Supply Chain&#x27;s **license compliance** feature enables you to explicitly allow or disallow (block) a package&#x27;s use in your repository based on its license. For example, your company policy may disallow the use of packages with the Creative Commons Attribution-NonCommercial (CC-BY-NC) license. Semgrep can help enforce this restriction.

Malicious dependency detectionSemgrep is able to detect malicious dependencies in your projects and in pull requests (PRs) or merge requests (MRs).

SBOM generationSemgrep enables you to generate a software bill of materials (SBOM) to assess your third-party dependencies and comply with auditing procedures. Semgrep Supply Chain (SSC) can generate an SBOM for each repository you have added to Semgrep AppSec Platform.

## JavaScript support in Semgrep CE[​](#javascript-support-in-semgrep-ce)
Semgrep CE is a fast, lightweight program analysis tool that can help you detect bugs in your code. It makes use of Semgrep&#x27;s LGPL 2.1 open source engine.

### Analyses[​](#analyses)

- Single-file, cross-function constant propagation
- Single-function taint analysis
- Semantic analysis

### Coverage[​](#coverage)
tip
- Check the `license` of a rule to ensure it meets your licensing requirements. See [Licensing](/docs/licensing) for more details.

The Semgrep Registry provides the following JavaScript rulesets:

- [** `p/javascript`](https://semgrep.dev/p/javascript)
- [** `p/eslint`](https://semgrep.dev/p/eslint)
- [** `p/expressjs`](https://semgrep.dev/p/expressjs)
- [** `p/hapi`](https://semgrep.dev/p/hapi)
- [** `p/headless-browser`](https://semgrep.dev/p/headless-browser)
- [** `p/koa`](https://semgrep.dev/p/koa)
- [** `p/nextjs`](https://semgrep.dev/p/nextjs)
- [** `p/nestjs`](https://semgrep.dev/p/nestjs)
- [** `p/nodejs`](https://semgrep.dev/p/nodejs)
- [** `p/typescript`](https://semgrep.dev/p/typescript)

Sample usage:

`semgrep scan --config p/javascript`Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Code](/docs/tags/semgrep-code)- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)- [Node.js](/docs/tags/node-js)- [javascript](/docs/tags/javascript)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/languages/javascript.md)Last updated on **Sep 30, 2025**