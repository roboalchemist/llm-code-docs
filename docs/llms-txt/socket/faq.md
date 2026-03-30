# Source: https://docs.socket.dev/docs/faq.md

# FAQ

Frequently Asked Questions

We're working to make Socket the best open source security tool.

If you have a question, [join the community](https://docs.socket.dev/docs/join-the-community) and ask!

## What is Socket?

Socket is a new security company that can protect your most critical apps from supply chain attacks. We are taking an entirely new approach to one of the hardest problems in security in a stagnant part of the industry that has historically been obsessed with just reporting on known vulnerabilities.

## Who built Socket?

Socket is built by a team of open source maintainers with over 1 billion monthly downloads. Everyone on the Socket team is an open source maintainer. We are all driven to defend the open source ecosystem from supply chain attacks and make it safe for everyone.

## What does Socket do?

Socket is unique because, unlike other tools, it detects and blocks supply chain attacks *before* they strike, mitigating the worst consequences:

1. **Supply Chain Attack Prevention:** Prevent compromised or hijacked packages from infiltrating your supply chain by monitoring all dependency changes in real-time.

2. **Package Behavior Analysis:** Detect when dependency updates introduce new risky API usage such as network, shell, filesystem, etc.

3. **Comprehensive Protection:** Block malware, typo-squatting, hidden code, misleading packages, permission creep, and [60+ red flags](https://socket.dev/npm/issue) in open source code. See [package issues](https://docs.socket.dev/docs/package-issues).

## How is Socket different from other code scanning tools?

The market is flooded with vulnerability scanners (which find CVEs in your dependencies) and static analysis tools (which analyze your app code).

Both of these approaches are less than helpful at detecting supply chain attacks of the sort we've seen exploding in the open source ecosystem.

* Vulnerability scanning tools merely look up the packages you're using and compare them to data in the public CVE databases such as [NVD](https://nvd.nist.gov/). When they find a match, they send you an alert to upgrade to a new version. This is too slow to stop an active supply chain attack.

* Traditional static analysis tools are way too noisy when run on third-party code, and don't provide actionable results. Most developers aren't running static analysis tools on their own code, let alone third-party code.

Socket is different. Socket was specifically designed to detect supply chain attacks in your dependencies. We built Socket specifically to help catch supply chain attacks such as these that you may have seen in the news: `ua-parser-js`, `coa`, `rc`, `colors`, `faker`, `event-stream`, `eslint-scope`, and hundreds more.

Unlike a traditional vulnerability scanner, Socket can actually detect an active supply chain attack. Unlike a traditional static analysis tool, Socket provides actionable feedback about dependency risk, instead of hundreds of meaningless alerts.

## How does Socket's code analysis work?

Socket analyzes the open source dependencies used in your software. Unlike traditional security tools that focus on finding vulnerabilities in your own code, Socket looks at the code of your third-party dependencies. This is important because attackers often target these dependencies as a way to infiltrate your software and access sensitive data or systems.

Socket uses static analysis, which is a technique that involves analyzing source code without actually executing it, to identify potential indicators of software supply chain attacks. This includes looking for new install scripts, network requests, environment variable access, telemetry, suspicious strings, obfuscated code, and dozens of other signals, all of which can be signs of malicious activity. We use a custom static analysis engine developed in-house to analyze every package across the entire npm ecosystem (and very soon, PyPI, Go, Maven, etc.).

In addition to static analysis, Socket also analyzes maintainer behavior. This means we look at who is maintaining the package and their activity history. This is important because a package with a history of questionable maintenance or a new maintainer with no track record can be a red flag for potential attacks. We also warn about unmaintained packages, trivial packages, and packages which have recently undergone major refactors.

Socket also analyzes package metadata to identify signs that a package is risky. For example, a package may load code from a remote git repository or a remote HTTP server, totally bypassing your package lockfile. This allows attackers to load whatever code they want, and even serve different packages to different IP addresses, making it really hard to have a reproducible build or figure out what code is actually going to be run when you install a package.

Another use of package metadata is to detect typosquats. We use Levenshtein distance and package download counts to detect packages which impersonate other legitimate packages. For example [webb3](https://socket.dev/npm/package/webb3/overview/1.2.0) is a malicious typo of [web3](https://socket.dev/npm/package/web3) because the name is similar and the legitimate package has 300,000 times as many downloads as the malicious one.

In total, we look for [70+ signals](https://socket.dev/npm/issue) in open source packages, which use different combinations of these 3 techniques – static analysis, package metadata analysis, and maintainer behavior analysis. By identifying attack indicators early, before the PR is merged, Socket helps prevent attacks before they can do any damage.

## How does Socket's capability detection work?

Socket uses static analysis (and soon, dynamic analysis) to characterize the behavior of a package and determine what capabilities it uses, which we call “capability detection”. For instance, to determine if an [npm package uses the network](https://socket.dev/npm/issue/networkAccess), Socket looks at whether `fetch()`, or Node's `net`, `dgram`, `dns`, or `http` or `https` modules are used within the package or – and this part is key – any of its dependencies.

Socket also uses static analysis to detect usage of privileged APIs such as shell, filesystem, eval(), and environment variables.

In total, Socket detects [70+ security red flags](https://socket.dev/npm/issue) in open source code, divided over [spectrum of issues](https://docs.socket.dev/docs/package-issues).

## What about side channels, such as maintainer behavior?

Some of the most valuable security signals come from side channels such as maintainer behavior. Socket detects “unstable ownership” which is when a new maintainer is given publish permission on a package. We also detect when packages are published out of chronological order because attackers often publish new patches on old major versions which still have a lot of usage.

Another example of an attack which goes beyond the code in a package is [typosquatting](https://socket.dev/npm/issue/didYouMean), which is one of the most common supply chain attack vectors. We define a typosquat as:

* Package name is 1-2 characters away from a more popular package
* The legit package has 1,000x more monthly downloads than the typo package

For example, look at how we handle the [bowserify](https://socket.dev/npm/package/bowserify) package which is a typo.

## Has Socket caught any notable malicious packages?

Yes. Socket has identified and reported multiple instances of malware, leading to their removal from the registry. Our proactive monitoring continues to uncover emerging threats, and we will be sharing more findings soon.

We are also working to open up Socket's powerful search tools to security researchers interested in hunting for malware on npm. If you're a researcher looking to collaborate, please get in touch.

For the latest security news, threat research, and insights, check out the [Socket Blog.](https://socket.dev/blog)

Socket's research has been featured in several publications, including **Forbes, TechCrunch, SecurityWeekly, The Hacker News, JavaScript Weekly, Risky Business News, and Bleeping Computer**.

Stay updated with our latest discoveries by subscribing to our blog [atom feed](https://socket.dev/api/blog/feed.atom) or [JSON feed](https://socket.dev/api/blog/feed.json).

## How do I use Socket? Where does it actually run?

When you install Socket as a [GitHub App](https://socket.dev/integrations), it will automatically evaluate all changes to package.json and other “package manifest” files. Whenever a new dependency is added in a Pull Request, Socket will evaluate it and leave a comment indicating if it is a security risk.

Socket can also be deployed using our [CLI](https://pypi.org/project/socketsecurity/) or [API](https://docs.socket.dev/reference/introduction-to-socket-api#/).

## What features are coming soon?

See what features we're working on by visiting the [Roadmap](https://feedback.socket.dev).

## Will Socket support additional ecosystems?

Yes. Socket currently provides robust support for **JavaScript, Python, Java, Ruby, .NET, Go, Rust, Scala, Kotlin and more**, with additional ecosystems **including PHP,  Swift, and Objective-C** in active development or planned soon. Our goal is to eventually support all major open-source language ecosystems.

Our full list of supported ecosystems can be found [here](https://docs.socket.dev/docs/language-support#/).

If your company relies on a language or package manager not yet supported by Socket, we'd love to hear from you, please [get in touch](https://docs.socket.dev/docs/contact-support).

Your feedback directly shapes our roadmap!

For the most up-to-date list of supported languages, visit our [Ecosystem Support](https://docs.socket.dev/docs/language-support) page.

## How much does Socket cost?

Open source package search with Socket Package Health Scores are **free to everyone** on our website, [https://socket.dev](https://socket.dev).

Socket is **free for open source repositories, forever**. For private repositories beyond the first, Socket is paid. See the [pricing page](https://socket.dev/pricing) for details.

## How can I report a security vulnerability in Socket?

If you believe you've found a security vulnerability in Socket, please [report it](https://socket.dev/security). We offer rewards of up to $1,000 for reporting a valid security issue. We will work with you to resolve the issue promptly. Thanks in advance!

## Does Socket capture any PII?

Socket does not process PII (personally-identifiable information) or touch your customer’s private information in any way. Socket analyzes open source dependencies (i.e. code that is publicly available) and reports our findings to customers. We do not analyze customer source code.

## Is my code safe?

Socket does not analyze, upload, or share customer source code. The only data we collect from the repository is the manifest file (i.e. “package.json” file, “requirements.txt” file) and associated lockfiles which primarily contain the list of open source dependencies in use by the customer. The list of dependencies is not very sensitive.

All communication is done through the API using HTTPS, so your manifest files are kept safe in transit.

## Got a question that isn't answered here?

[Join the community](https://docs.socket.dev/docs/join-the-community) to ask questions and get answers!