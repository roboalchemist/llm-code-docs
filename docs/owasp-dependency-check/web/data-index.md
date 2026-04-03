Internet Access Required – dependency-check-maven


[Fork me on GitHub](https://github.com/dependency-check/DependencyCheck)

# OWASP dependency-check

---

* [OWASP](https://www.owasp.org/)/
* [Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check)/
* [documentation](../)/
* Internet Access Required
* | Last Published: 2026-01-09
* Version: 12.2.0

* OWASP dependency-check
* [General](../index.html)
  + [How it Works](../general/internals.html)
  + [Reading the Report](../general/thereport.html)
  + [False Positives](../general/suppression.html)
  + [False Negatives](../general/hints.html)
  + Internet Access Required
    - [Proxy](../data/proxy.html)
    - [Mirroring NVD](../data/mirrornvd.html)
    - [Snapshotting the NVD](../data/cachenvd.html)
    - [Caching the Database](../data/cacheh2.html)
    - [Central DB](../data/database.html)
    - [Sonatype OSS Index](../data/ossindex.html)
  + [Related Work](../related.html)
  + [Project Presentation (pptx)](../general/dependency-check.pptx)
  + [Project Presentation (pdf)](../general/dependency-check.pdf)
  + [Sample Report](../general/SampleReport.html)
  + [How to Scan an ISO Image](../general/scan_iso.html)
* [File Type Analyzers](../analyzers/index.html)
* [Modules](../modules.html)
* Project Documentation
* [Project Information](../project-info.html)
* [Project Reports](../project-reports.html)

[Follow ctxt](https://twitter.com/ctxt)

[![JProfiler Java Profiler](https://dependency-check.github.io/DependencyCheck/images/logos/jprofiler.png)](https://www.ej-technologies.com/products/jprofiler/overview.html)
[![developed using IntelliJ](https://dependency-check.github.io/DependencyCheck/images/logos/logo_intellij_idea.png)](http://www.jetbrains.com/idea/)



# Internet Access Required

Dependency-check, by default, requires access to several externally
hosted resources.

## The NVD Database

OWASP dependency-check maintains a local copy of the NVD API's CVE data hosted by NIST. By default,
a local [H2 database](http://www.h2database.com/html/main.html) instance is used.
As each instance maintains its own copy of the NVD the machine will need access
to nvd.nist.gov in order to download the NVD data feeds. While the initial download of the NVD
data feed is large, if after the initial download the tool is run at least once every seven
days only two small XML files containing the recent modifications will need to be downloaded.

In some installations OpenJDK may not be able to access the NVD API. Please see the
[TLS Failures article](./tlsfailure.html) for more information.

If your build servers are using dependency-check and are unable to access the Internet you
have a few options:

1. Configure the [proxy settings](proxy.html) so that the build server can access the Internet
2. [Mirror the NVD](./mirrornvd.html) locally within your organization
3. Build the H2 database on one node and [cache the H2 database](./cacheh2.html).
4. Use a more robust [centralized database](./database.html) with a single update node
5. In GitHub Actions utilize the cache action; [example here](./cache-action.html).

## CISA Known Exploited Vulnerabilities

with version 8.0.0 access to the CISA Known Exploited Vulnerabilities Catalog is required.
If running on a system with limited network access there are three options:

1. Add `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` to the allow list.
2. Mirror `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` locally.
3. Disable the CISA Known Exploited Vulnerabilities Analyzer.

## Retire JS Repository

The RetireJS Analyzes must download the RetireJS Repository. If this is blocked users
must either mirror the [JS Repository](./mirrornvd.html) or disable the Retire JS Analyzer.

## Hosted base suppressions file

For a faster roundtrip time ([issue #4723](https://github.com/dependency-check/DependencyCheck/issues/4723)) to get false-positive report
solution out to the users dependency-check starting from version 8.0.0 is using an online hosted
[suppressions file](https://dependency-check.github.io/DependencyCheck/suppressions/publishedSuppressions.xml).
For environments with constraints to internet access this file can be locally mirrored by customizing the hostedsuppressions file URL.
See the tool-specific configuration documentation on the [github pages](https://dependency-check.github.io/DependencyCheck/index.html)
for the exact advanced configuration flag to specify the custom location.
Failure to download the hosted suppressions file will result in only a warning from the tool, but may result in false positives
being reported by your scan that have already been mitigated by the hosted suppressions file.

## Downloading Additional Information

### Central Repository

If the machine that is running dependency-check cannot reach the [Central Repository](http://search.maven.org)
the analysis may result in false negatives. This is because some POM files, that are not
contained within the JAR file itself, contain evidence that is used to accurately identify
a library. If using the Ant plugin or CLI and Central cannot be reached, it is highly recommended to setup a
Nexus server within your organization and to configure dependency-check to use the local
Nexus server. **Notes:**

1. If using any build plugin except Ant - there is no benefit to setting up a Nexus server for use by dependency-check.
2. Even with a Nexus server setup we have seen dependency-check CLI be
   re-directed to other repositories on the Internet to download the actual POM file; this
   happened due to a rare circumstance where the Nexus instance used by dependency-check
   was not the instance of Nexus used to build the application (i.e. the dependencies
   were not actually present in the Nexus used by dependency-check).

### Sonatype OSS Index

OWASP dependency-check includes support to consult the [Sonatype OSS Index](https://ossindex.sonatype.org)
to enrich the report with supplemental vulnerability information.

For more details on this integration see [Sonatype OSS Index](./ossindex.html).

## Telemetry

See the [telemetry documentation](../general/telemetry.html) for more information about telemetry data collection.

---



© 2012–2025 [OWASP](https://www.owasp.org)

![](https://static.scarf.sh/a.png?x-pxid=90c74bb8-b6d1-4464-a9b6-754067afe126)