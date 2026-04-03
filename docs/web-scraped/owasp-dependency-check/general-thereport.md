How To Read The Reports – dependency-check-maven


[Fork me on GitHub](https://github.com/dependency-check/DependencyCheck)

# OWASP dependency-check

---

* [OWASP](https://www.owasp.org/)/
* [Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check)/
* [documentation](../)/
* How To Read The Reports
* | Last Published: 2026-01-09
* Version: 12.2.0

* OWASP dependency-check
* [General](../index.html)
  + [How it Works](../general/internals.html)
  + Reading the Report
  + [False Positives](../general/suppression.html)
  + [False Negatives](../general/hints.html)
  + [Internet Access Required](../data/index.html)
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



# How To Read The Reports

The top of the report contains a list of the identified vulnerable components. By clicking the ‘Showing Vulnerable
Dependencies’ link the list will be expanded to include all of the dependencies scanned. The table lists:

* Dependency - the file name of the dependency scanned.
* CPE - any Common Platform Enumeration identifiers found.
* GAV - the Maven Group, Artifact, Version (GAV).
* Highest Severity - the highest severity of any associated CVEs.
* CVE Count - the number of associated CVEs.
* CPE Confidence - a ranking of how confident dependency-check is that the CPE was identified correctly.
* Evidence Count - the quantity of data extracted from the dependency that was used to identify the CPE.

There is a lot of information contained in the HTML version of the report. When analyzing the results, the first
thing one should do is determine if the identified CPE is correct. Due to the way dependency-check works (see
[How it works](./internals.html) for more information) the report may contain false positives. These false positives
are primarily on the CPE values. If the CPE value is wrong, this is usually obvious, one should use the suppression
feature in the report to generate a suppression XML file that can be used on future scans. In addition to looking
at the CPE values in comparison to the name of the dependency one may also consider the confidence of the CPE
(as discussed in [How does dependency-check work](./internals.html)). See the [Suppressing False Positives](./suppression.html)
page for more information on how to generate and use the suppression file.

Once you have weeded out any obvious false positives one can then look at the remaining entries and determine if
any of the identified CVE entries are actually exploitable in your environment. Determining if a CVE is exploitable
in your environment can be tricky, for this we do not currently have any tips other then upgrade the library if you
can just to be safe. Note, some CVE entries can be fixed by either upgrading the library or changing configuration
options.

One item that dependency-check flags that many may think is a false positive are old database drivers. One thing to
consider about an old database driver is that the CPE/CVEs identified are usually for the server rather then the driver.
However, the presence of an old driver may indicate that you have an older version of the server running in your
environment and that server may need to be patched or upgraded. However, in some cases the old database drivers are
actually unused, transitive dependencies.

# Regarding False Negatives

As stated above, due to the nature of dependency-check there may be publicly disclosed vulnerabilities in the project
dependencies scanned by dependency-check that
are not identified. With the current version of dependency-check the HTML report has a table at the top that initially
displays just the dependencies with identified vulnerabilities. This can be toggled to show all dependencies. If you
examine the rows that do not have identified CPE/CVE entries you will see an “evidence count”. If the evidence count
is extremely low (0-5 entries) then there may not have been enough information contained in the dependency to identify
a CPE and associated CVEs.

It should be noted that while the false positives described above are bad, more concerning is that there may be vulnerabilities within the project dependencies that
have yet to be publicly known. If one has the resources consider performing security assessments on the project dependencies.

---



© 2012–2025 [OWASP](https://www.owasp.org)

![](https://static.scarf.sh/a.png?x-pxid=90c74bb8-b6d1-4464-a9b6-754067afe126)