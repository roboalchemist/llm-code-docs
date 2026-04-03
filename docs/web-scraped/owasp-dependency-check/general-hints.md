Resolving False Negatives – dependency-check-maven


[Fork me on GitHub](https://github.com/dependency-check/DependencyCheck)

# OWASP dependency-check

---

* [OWASP](https://www.owasp.org/)/
* [Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check)/
* [documentation](../)/
* Resolving False Negatives
* | Last Published: 2026-01-09
* Version: 12.2.0

* OWASP dependency-check
* [General](../index.html)
  + [How it Works](../general/internals.html)
  + [Reading the Report](../general/thereport.html)
  + [False Positives](../general/suppression.html)
  + False Negatives
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



# Resolving False Negatives

Due to how dependency-check identifies libraries, false negatives may occur (a CPE was NOT identified for a library). Identifying these false negatives can be accomplished using the HTML report. In the report, click on the “Display: Showing Vulnerable Dependencies (click to show all)” link. You can then browse the dependencies and review the CPEs that are there for accuracy. You can also review the dependencies where no CPE match was made. Using the CPE dictionary search manually to verify that there is a CPE to match is a good verification that a false negative has been found. If you identify a dependency that is missing a CPE you can add evidence to help identify the correct CPE.

A possible reason for false negatives is re-naming of either the vendor or library name over time. Another case is when an artifact has missing info (manifest with no vendor).

Dependency Check has a built in [hints](https://github.com/dependency-check/DependencyCheck/blob/main/core/src/main/resources/dependencycheck-base-hint.xml) file that is used in every check to help correct well known false negatives.

A sample hints file that add a product name and possible vendors for Spring framework dependencies would look like:

```
<?xml version="1.0" encoding="UTF-8"?>
<hints xmlns="https://jeremylong.github.io/DependencyCheck/dependency-hint.1.1.xsd">
    <hint>
        <given>
            <evidence type="product" source="Manifest" name="Implementation-Title" value="Spring Framework" confidence="HIGH"/>
            <evidence type="product" source="Manifest" name="Implementation-Title" value="org.springframework.core" confidence="HIGH"/>
            <evidence type="product" source="Manifest" name="Implementation-Title" value="spring-core" confidence="HIGH"/>
        </given>
        <add>
            <evidence type="product" source="hint analyzer" name="product" value="springsource_spring_framework" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="SpringSource" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="vmware" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="pivotal" confidence="HIGH"/>
        </add>
    </hint>
</hints>
```

The above XML file will add the 4 evidence entries to any dependency that matches any one of the 3 givens.

The following shows some other ways to add evidence

```
<?xml version="1.0" encoding="UTF-8"?>
<hints xmlns="https://jeremylong.github.io/DependencyCheck/dependency-hint.1.1.xsd">
   <hint>
        <given>
            <evidence type="product" source="jar" name="package name" value="springframework" confidence="LOW"/>
            <fileName contains="spring"/>
        </given>
        <add>
            <evidence type="product" source="hint analyzer" name="product" value="springsource_spring_framework" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="SpringSource" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="vmware" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="pivotal" confidence="HIGH"/>
        </add>
   </hint>
   <hint>
        <given>
            <fileName contains="my-thelib-.*\.jar" regex="true" caseSensitive="true"/>
        </given>
        <add>
            <evidence type="product" source="hint analyzer" name="product" value="thelib" confidence="HIGH"/>
            <evidence type="vendor" source="hint analyzer" name="vendor" value="thevendor" confidence="HIGH"/>
        </add>
  </hint>
</hints>
```

The full schema for hints files can be found here: [dependency-hint.xsd](https://github.com/dependency-check/DependencyCheck/blob/main/core/src/main/resources/schema/dependency-hint.1.1.xsd "Hint Schema")

Please see the appropriate configuration option in each interfaces configuration guide:

* [Command Line Tool](../dependency-check-cli/arguments.html)
* [Maven Plugin](../dependency-check-maven/configuration.html)
* [Gradle Plugin](../dependency-check-gradle/configuration.html)
* [Ant Task](../dependency-check-ant/configuration.html)
* [Jenkins Plugin](../dependency-check-jenkins/index.html)

---



© 2012–2025 [OWASP](https://www.owasp.org)

![](https://static.scarf.sh/a.png?x-pxid=90c74bb8-b6d1-4464-a9b6-754067afe126)