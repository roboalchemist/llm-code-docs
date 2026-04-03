About – dependency-check-maven


[Fork me on GitHub](https://github.com/dependency-check/DependencyCheck)

# OWASP dependency-check

---

* [OWASP](https://www.owasp.org/)/
* [Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check)/
* [documentation](./)/
* About
* | Last Published: 2026-01-09
* Version: 12.2.0

* OWASP dependency-check
* General
  + [How it Works](general/internals.html)
  + [Reading the Report](general/thereport.html)
  + [False Positives](general/suppression.html)
  + [False Negatives](general/hints.html)
  + [Internet Access Required](data/index.html)
  + [Related Work](related.html)
  + [Project Presentation (pptx)](general/dependency-check.pptx)
  + [Project Presentation (pdf)](general/dependency-check.pdf)
  + [Sample Report](general/SampleReport.html)
  + [How to Scan an ISO Image](general/scan_iso.html)
* [File Type Analyzers](analyzers/index.html)
* [Modules](modules.html)
* Project Documentation
* [Project Information](project-info.html)
* [Project Reports](project-reports.html)

[Follow ctxt](https://twitter.com/ctxt)

[![JProfiler Java Profiler](https://dependency-check.github.io/DependencyCheck/images/logos/jprofiler.png)](https://www.ej-technologies.com/products/jprofiler/overview.html)
[![developed using IntelliJ](https://dependency-check.github.io/DependencyCheck/images/logos/logo_intellij_idea.png)](http://www.jetbrains.com/idea/)



# About

OWASP dependency-check is an open source solution to the OWASP Top 10 2021 entry:
[A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/).
Dependency-check can currently be used to scan software to identify the use of
known vulnerable components. For a full list of supported languages/technologies
please see the [File Type Analyzer](analyzers/index.html)
page). Note that some of the analyzers are experimental and may produce more false
positive and false negative rates. To use the experimental
analyzers they must be specifically enabled via the appropriate *experimental*
configuration.

The problem with using known vulnerable components was covered in a paper by
Jeff Williams and Arshan Dabirsiaghi titled, “[The Unfortunate Reality of
Insecure Libraries](https://www.scribd.com/document/175866686/Aspect-Security-the-Unfortunate-Reality-of-Insecure-Libraries)”
(registration required). The gist of the paper is that we as a development
community include third party libraries in our applications that contain well
known published vulnerabilities (such as those at the
[National Vulnerability Database](http://web.nvd.nist.gov/view/vuln/search)).

More information about dependency-check can be found here:

* [How does dependency-check work](general/internals.html)
* [How to read the report](general/thereport.html)

**This product uses the NVD API but is not endorsed or certified by the NVD.**

OWASP dependency-check's core analysis engine can be used as:

* [Ant Task](dependency-check-ant/index.html)
* [Command Line Tool](dependency-check-cli/index.html)
* [Gradle Plugin](dependency-check-gradle/index.html)
* [Jenkins Plugin](dependency-check-jenkins/index.html)
* [Maven Plugin](dependency-check-maven/index.html) - Maven 3.6.3 or newer required

Unofficial (Not endorsed by OWASP)

* [SBT Plugin](https://github.com/nMoncho/sbt-dependency-check)

For help with dependency-check the following resource can be used:

* Open a [github issue](https://github.com/dependency-check/DependencyCheck/issues)

---



© 2012–2025 [OWASP](https://www.owasp.org)

![](https://static.scarf.sh/a.png?x-pxid=90c74bb8-b6d1-4464-a9b6-754067afe126)