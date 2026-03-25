# Source: https://www.jenkins.io/doc/book/installing/

Title: Installing Jenkins

URL Source: https://www.jenkins.io/doc/book/installing/

Markdown Content:
Installing Jenkins
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
    *   [Docker](https://www.jenkins.io/doc/book/installing/docker/)
    *   [Kubernetes](https://www.jenkins.io/doc/book/installing/kubernetes/)
    *   [Linux](https://www.jenkins.io/doc/book/installing/linux/)
    *   [macOS](https://www.jenkins.io/doc/book/installing/macos/)
    *   [Windows](https://www.jenkins.io/doc/book/installing/windows/)
    *   [Other Systems](https://www.jenkins.io/doc/book/installing/other/)
    *   [WAR file](https://www.jenkins.io/doc/book/installing/war-file/)
    *   [Other Servlet Containers](https://www.jenkins.io/doc/book/installing/servlet-containers/)
    *   [Offline Installations](https://www.jenkins.io/doc/book/installing/offline/)
    *   [Initial Settings](https://www.jenkins.io/doc/book/installing/initial-settings/)

*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

[⇐ User Handbook Overview](https://www.jenkins.io/doc/book/getting-started)

[Index](https://www.jenkins.io/doc/book/)

[Docker ⇒](https://www.jenkins.io/doc/book/installing/docker)

Installing Jenkins
==================

 Chapter Sub-Sections 

*   [Docker](https://www.jenkins.io/doc/book/installing/docker)
*   [Kubernetes](https://www.jenkins.io/doc/book/installing/kubernetes)
*   [Linux](https://www.jenkins.io/doc/book/installing/linux)
*   [macOS](https://www.jenkins.io/doc/book/installing/macos)
*   [Windows](https://www.jenkins.io/doc/book/installing/windows)
*   [Other Systems](https://www.jenkins.io/doc/book/installing/other)
*   [WAR file](https://www.jenkins.io/doc/book/installing/war-file)
*   [Other Servlet Containers](https://www.jenkins.io/doc/book/installing/servlet-containers)
*   [Offline Installations](https://www.jenkins.io/doc/book/installing/offline)
*   [Initial Settings](https://www.jenkins.io/doc/book/installing/initial-settings)

The procedures in this chapter are for new installations of Jenkins.

Jenkins is typically run as a standalone application in its own process. The Jenkins WAR file bundles [Winstone](https://github.com/jenkinsci/winstone), a [Jetty](https://www.eclipse.org/jetty/) servlet container wrapper, and can be started on any operating system or platform with a version of Java supported by Jenkins.

Theoretically, Jenkins can also be run as a servlet in a traditional servlet container like [Apache Tomcat](https://tomcat.apache.org/) or [WildFly](https://www.wildfly.org/), but in practice this is largely untested and there are many caveats. In particular, support for WebSocket agents is only implemented for the Jetty servlet container. See the [Servlet Container Support Policy](https://www.jenkins.io/doc/book/platform-information/support-policy-servlet-containers) page for details.

* * *

[⇐ User Handbook Overview](https://www.jenkins.io/doc/book/getting-started)

[Index](https://www.jenkins.io/doc/book/)

[Docker ⇒](https://www.jenkins.io/doc/book/installing/docker)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/installing/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
