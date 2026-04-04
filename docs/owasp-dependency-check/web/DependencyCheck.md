# Source: https://jeremylong.github.io/DependencyCheck/

Title: About – dependency-check-maven

URL Source: https://jeremylong.github.io/DependencyCheck/

Markdown Content:
[](https://jeremylong.github.io/DependencyCheck/)
OWASP dependency-check is an open source solution to the OWASP Top 10 2021 entry: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/). Dependency-check can currently be used to scan software to identify the use of known vulnerable components. For a full list of supported languages/technologies please see the [File Type Analyzer](https://dependency-check.github.io/DependencyCheck/analyzers/index.html) page). Note that some of the analyzers are experimental and may produce more false positive and false negative rates. To use the experimental analyzers they must be specifically enabled via the appropriate _experimental_ configuration.

The problem with using known vulnerable components was covered in a paper by Jeff Williams and Arshan Dabirsiaghi titled, “[The Unfortunate Reality of Insecure Libraries](https://www.scribd.com/document/175866686/Aspect-Security-the-Unfortunate-Reality-of-Insecure-Libraries)” (registration required). The gist of the paper is that we as a development community include third party libraries in our applications that contain well known published vulnerabilities (such as those at the [National Vulnerability Database](http://web.nvd.nist.gov/view/vuln/search)).

More information about dependency-check can be found here:

*   [How does dependency-check work](https://dependency-check.github.io/DependencyCheck/general/internals.html)
*   [How to read the report](https://dependency-check.github.io/DependencyCheck/general/thereport.html)

**This product uses the NVD API but is not endorsed or certified by the NVD.**

OWASP dependency-check's core analysis engine can be used as:

*   [Ant Task](https://dependency-check.github.io/DependencyCheck/dependency-check-ant/index.html)
*   [Command Line Tool](https://dependency-check.github.io/DependencyCheck/dependency-check-cli/index.html)
*   [Gradle Plugin](https://dependency-check.github.io/DependencyCheck/dependency-check-gradle/index.html)
*   [Jenkins Plugin](https://dependency-check.github.io/DependencyCheck/dependency-check-jenkins/index.html)
*   [Maven Plugin](https://dependency-check.github.io/DependencyCheck/dependency-check-maven/index.html) - Maven 3.6.3 or newer required

Unofficial (Not endorsed by OWASP)

*   [SBT Plugin](https://github.com/nMoncho/sbt-dependency-check)

For help with dependency-check the following resource can be used:

*   Open a [github issue](https://github.com/dependency-check/DependencyCheck/issues)
