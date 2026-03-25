# Source: https://maven.apache.org/plugins/index.html

Title: Available Plugins – Maven

URL Source: https://maven.apache.org/plugins/index.html

Markdown Content:
[](https://maven.apache.org/plugins/index.html)
Maven is - at its heart - a plugin execution framework; all work is done by plugins. Looking for a specific goal to execute? This page lists the core plugins and others. There are the build and the reporting plugins:

* **Build plugins** will be executed during the build and they should be configured in the `<build/>` element from the POM.
* **Reporting plugins** will be executed during the site generation and they should be configured in the `<reporting/>` element from the POM. Because the result of a Reporting plugin is part of the generated site, Reporting plugins should be both internationalized and localized. You can read more about the [localization of our plugins](https://maven.apache.org/plugins/localization.html) and how you can help.

[](https://maven.apache.org/plugins/index.html)
Supported By The Maven Project[](https://maven.apache.org/plugins/index.html#supported-by-the-maven-project)
------------------------------------------------------------------------------------------------------------

To see the most up-to-date list browse the Maven repository, specifically the [`org/apache/maven/plugins`](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/) subdirectory. _(Plugins are organized according to a directory structure that resembles the standard Java package naming convention)_

| **Plugin** | **Type*** | **Version** | **Release Date** | **Description** | **Source Repository** | **Issue Tracking** |
| --- | --- | --- | --- | --- | --- | --- |
| **Core plugins** |  |  | **Plugins corresponding to default core phases (ie. clean, compile). They may have multiple goals as well.** |
| [`clean`](https://maven.apache.org/plugins/maven-clean-plugin/) | B | 3.5.0 | 2025-05-27 | Clean up after the build. | [Git](https://gitbox.apache.org/repos/asf/maven-clean-plugin.git) / [GitHub](https://github.com/apache/maven-clean-plugin/) | [GitHub Issues](https://github.com/apache/maven-clean-plugin/issues) |
| [`compiler`](https://maven.apache.org/plugins/maven-compiler-plugin/) | B | 3.15.0 | 2026-01-27 | Compiles Java sources. | [Git](https://gitbox.apache.org/repos/asf/maven-compiler-plugin.git) / [GitHub](https://github.com/apache/maven-compiler-plugin/) | [GitHub Issues](https://github.com/apache/maven-compiler-plugin/issues) |
| [`compiler 4.x`](https://maven.apache.org/plugins/maven-compiler-plugin-4.x/) | B | 4.0.0-beta-4 | 2026-01-27 | Compiles Java sources. | [Git](https://gitbox.apache.org/repos/asf/maven-compiler-plugin.git) / [GitHub](https://github.com/apache/maven-compiler-plugin/) | [GitHub Issues](https://github.com/apache/maven-compiler-plugin/issues) |
| [`deploy`](https://maven.apache.org/plugins/maven-deploy-plugin/) | B | 3.1.4 | 2025-02-23 | Deploy the built artifact to the remote repository. | [Git](https://gitbox.apache.org/repos/asf/maven-deploy-plugin.git) / [GitHub](https://github.com/apache/maven-deploy-plugin/) | [GitHub Issues](https://github.com/apache/maven-deploy-plugin/issues) |
| [`failsafe`](https://maven.apache.org/surefire/maven-failsafe-plugin/) | B | 3.5.5 | 2026-02-18 | Run the JUnit integration tests in an isolated classloader. | [Git](https://gitbox.apache.org/repos/asf/maven-surefire.git) / [GitHub](https://github.com/apache/maven-surefire/) | [GitHub Issues](https://github.com/apache/maven-surefire/issues) |
| [`install`](https://maven.apache.org/plugins/maven-install-plugin/) | B | 3.1.4 | 2025-02-24 | Install the built artifact into the local repository. | [Git](https://gitbox.apache.org/repos/asf/maven-install-plugin.git) / [GitHub](https://github.com/apache/maven-install-plugin/) | [GitHub Issues](https://github.com/apache/maven-install-plugin/issues) |
| [`resources`](https://maven.apache.org/plugins/maven-resources-plugin/) | B | 3.5.0 | 2026-03-02 | Copy the resources to the output directory for including in the JAR. | [Git](https://gitbox.apache.org/repos/asf/maven-resources-plugin.git) / [GitHub](https://github.com/apache/maven-resources-plugin/) | [GitHub Issues](https://github.com/apache/maven-resources-plugin/issues) |
| [`site`](https://maven.apache.org/plugins/maven-site-plugin/) | B | 3.21.0 | 2024-10-18 | Generate a site for the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-site-plugin.git) / [GitHub](https://github.com/apache/maven-site-plugin/) | [GitHub Issues](https://github.com/apache/maven-site-plugin/issues) |
| [`surefire`](https://maven.apache.org/surefire/maven-surefire-plugin/) | B | 3.5.5 | 2026-02-18 | Run the JUnit unit tests in an isolated classloader. | [Git](https://gitbox.apache.org/repos/asf/maven-surefire.git) / [GitHub](https://github.com/apache/maven-surefire/) | [GitHub Issues](https://github.com/apache/maven-surefire/issues) |
| [`verifier`](https://maven.apache.org/plugins/maven-verifier-plugin/) | B | 1.1 | 2015-04-14 | Useful for integration tests - verifies the existence of certain conditions. | [Git](https://gitbox.apache.org/repos/asf/maven-verifier-plugin.git) / [GitHub](https://github.com/apache/maven-verifier-plugin/) | [GitHub Issues](https://github.com/apache/maven-verifier-plugin/issues) |
| **Packaging types/tools** |  |  | **These plugins relate to packaging respective artifact types.** |
| [`ear`](https://maven.apache.org/plugins/maven-ear-plugin/) | B | 3.4.0 | 2025-06-16 | Generate an EAR from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-ear-plugin.git) / [GitHub](https://github.com/apache/maven-ear-plugin/) | [GitHub Issues](https://github.com/apache/maven-ear-plugin/issues) |
| [`ejb`](https://maven.apache.org/plugins/maven-ejb-plugin/) | B | 3.3.0 | 2025-11-16 | Build an EJB (and optional client) from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-ejb-plugin.git) / [GitHub](https://github.com/apache/maven-ejb-plugin/) | [GitHub Issues](https://github.com/apache/maven-ejb-plugin/issues) |
| [`jar`](https://maven.apache.org/plugins/maven-jar-plugin/) | B | 3.5.0 | 2025-11-11 | Build a JAR from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-jar-plugin.git) / [GitHub](https://github.com/apache/maven-jar-plugin/) | [GitHub Issues](https://github.com/apache/maven-jar-plugin/issues) |
| [`rar`](https://maven.apache.org/plugins/maven-rar-plugin/) | B | 3.1.0 | 2025-11-15 | Build a RAR from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-rar-plugin.git) / [GitHub](https://github.com/apache/maven-rar-plugin/) | [GitHub Issues](https://github.com/apache/maven-rar-plugin/issues) |
| [`war`](https://maven.apache.org/plugins/maven-war-plugin/) | B | 3.5.1 | 2025-11-24 | Build a WAR from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-war-plugin.git) / [GitHub](https://github.com/apache/maven-war-plugin/) | [GitHub Issues](https://github.com/apache/maven-war-plugin/issues) |
| [`app-client/acr`](https://maven.apache.org/plugins/maven-acr-plugin/) | B | 3.2.0 | 2025-11-25 | Build a JavaEE application client from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-acr-plugin.git) / [GitHub](https://github.com/apache/maven-acr-plugin/) | [GitHub Issues](https://github.com/apache/maven-acr-plugin/issues) |
| [`shade`](https://maven.apache.org/plugins/maven-shade-plugin/) | B | 3.6.2 | 2026-03-02 | Build an Uber-JAR from the current project, including dependencies. | [Git](https://gitbox.apache.org/repos/asf/maven-shade-plugin.git) / [GitHub](https://github.com/apache/maven-shade-plugin/) | [GitHub Issues](https://github.com/apache/maven-shade-plugin/issues) |
| [`source`](https://maven.apache.org/plugins/maven-source-plugin/) | B | 3.4.0 | 2025-11-22 | Build a source-JAR from the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-source-plugin.git) / [GitHub](https://github.com/apache/maven-source-plugin/) | [GitHub Issues](https://github.com/apache/maven-source-plugin/issues) |
| [`jlink`](https://maven.apache.org/plugins/maven-jlink-plugin/) | B | 3.3.0 | 2026-03-09 | Build Java Run Time Image. | [Git](https://gitbox.apache.org/repos/asf/maven-jlink-plugin.git) / [GitHub](https://github.com/apache/maven-jlink-plugin/) | [GitHub Issues](https://github.com/apache/maven-jlink-plugin/issues) |
| [`jmod`](https://maven.apache.org/plugins/maven-jmod-plugin/) | B | 3.0.0 | 2025-12-22 | Build Java JMod files. | [Git](https://gitbox.apache.org/repos/asf/maven-jmod-plugin.git) / [GitHub](https://github.com/apache/maven-jmod-plugin/) | [GitHub Issues](https://github.com/apache/maven-jmod-plugin/issues) |
| **Reporting plugins** |  |  | **Plugins which generate reports, are configured as reports in the POM and run under the site generation lifecycle.** |
| [`changelog`](https://maven.apache.org/plugins/maven-changelog-plugin/) | R | 3.0.0-M1 | 2024-12-30 | Generate a list of recent changes from your SCM. | [Git](https://gitbox.apache.org/repos/asf/maven-changelog-plugin.git) / [GitHub](https://github.com/apache/maven-changelog-plugin/) | [GitHub Issues](https://github.com/apache/maven-changelog-plugin/issues) |
| [`changes`](https://maven.apache.org/plugins/maven-changes-plugin/) | B+R | 3.0.0-M3 | 2025-05-12 | Generate a report from an issue tracker or a change document. | [Git](https://gitbox.apache.org/repos/asf/maven-changes-plugin.git) / [GitHub](https://github.com/apache/maven-changes-plugin/) | [GitHub Issues](https://github.com/apache/maven-changes-plugin/issues) |
| [`checkstyle`](https://maven.apache.org/plugins/maven-checkstyle-plugin/) | B+R | 3.6.0 | 2024-10-22 | Generate a Checkstyle report. | [Git](https://gitbox.apache.org/repos/asf/maven-checkstyle-plugin.git) / [GitHub](https://github.com/apache/maven-checkstyle-plugin/) | [GitHub Issues](https://github.com/apache/maven-checkstyle-plugin/issues) |
| [`doap`](https://maven.apache.org/plugins/maven-doap-plugin/) | B | 3.0.0-M1 | 2025-11-24 | Generate a Description of a Project (DOAP) file from a POM. | [Git](https://gitbox.apache.org/repos/asf/maven-doap-plugin.git) / [GitHub](https://github.com/apache/maven-doap-plugin/) | [GitHub Issues](https://github.com/apache/maven-doap-plugin/issues) |
| [`javadoc`](https://maven.apache.org/plugins/maven-javadoc-plugin/) | B+R | 3.12.0 | 2025-09-16 | Generate Javadoc for the project. | [Git](https://gitbox.apache.org/repos/asf/maven-javadoc-plugin.git) / [GitHub](https://github.com/apache/maven-javadoc-plugin/) | [GitHub Issues](https://github.com/apache/maven-javadoc-plugin/issues) |
| [`jdeps`](https://maven.apache.org/plugins/maven-jdeps-plugin/) | B | 3.2.0 | 2025-12-28 | Run JDK's JDeps tool on the project. | [Git](https://gitbox.apache.org/repos/asf/maven-jdeps-plugin.git) / [GitHub](https://github.com/apache/maven-jdeps-plugin/) | [GitHub Issues](https://github.com/apache/maven-jdeps-plugin/issues) |
| [`jxr`](https://maven.apache.org/jxr/maven-jxr-plugin/) | R | 3.6.0 | 2024-10-22 | Generate a source cross reference. | [Git](https://gitbox.apache.org/repos/asf/maven-jxr.git) / [GitHub](https://github.com/apache/maven-jxr/) | [GitHub Issues](https://github.com/apache/maven-jxr/issues) |
| [`pmd`](https://maven.apache.org/plugins/maven-pmd-plugin/) | B+R | 3.28.0 | 2025-10-07 | Generate a PMD/CPD report. | [Git](https://gitbox.apache.org/repos/asf/maven-pmd-plugin.git) / [GitHub](https://github.com/apache/maven-pmd-plugin/) | [GitHub Issues](https://github.com/apache/maven-pmd-plugin/issues) |
| [`plugin-report`](https://maven.apache.org/plugin-tools/maven-plugin-report-plugin/) | R | 3.15.2 | 2025-10-20 | Create a plugin documentation for any mojos found in the source tree. | [Git](https://gitbox.apache.org/repos/asf/maven-plugin-tools.git) / [GitHub](https://github.com/apache/maven-plugin-tools/) | [GitHub Issues](https://github.com/apache/maven-plugin-tools/issues) |
| [`project-info-reports`](https://maven.apache.org/plugins/maven-project-info-reports-plugin/) | R | 3.9.0 | 2025-02-23 | Generate standard project reports. | [Git](https://gitbox.apache.org/repos/asf/maven-project-info-reports-plugin.git) / [GitHub](https://github.com/apache/maven-project-info-reports-plugin/) | [GitHub Issues](https://github.com/apache/maven-project-info-reports-plugin/issues) |
| [`surefire-report`](https://maven.apache.org/surefire/maven-surefire-report-plugin/) | R | 3.5.5 | 2026-02-18 | Generate a report based on the results of unit tests. | [Git](https://gitbox.apache.org/repos/asf/maven-surefire.git) / [GitHub](https://github.com/apache/maven-surefire/) | [GitHub Issues](https://github.com/apache/maven-surefire/issues) |
| **Tools** |  |  | **These are miscellaneous tools available through Maven by default.** |
| [`antrun`](https://maven.apache.org/plugins/maven-antrun-plugin/) | B | 3.2.0 | 2025-10-17 | Run a set of ant tasks from a phase of the build. | [Git](https://gitbox.apache.org/repos/asf/maven-antrun-plugin.git) / [GitHub](https://github.com/apache/maven-antrun-plugin/) | [GitHub Issues](https://github.com/apache/maven-antrun-plugin/issues) |
| [`artifact`](https://maven.apache.org/plugins/maven-artifact-plugin/) | B | 3.6.1 | 2025-09-29 | Manage artifacts tasks like buildinfo. | [Git](https://gitbox.apache.org/repos/asf/maven-artifact-plugin.git) / [GitHub](https://github.com/apache/maven-artifact-plugin/) | [GitHub Issues](https://github.com/apache/maven-artifact-plugin/issues) |
| [`archetype`](https://maven.apache.org/archetype/maven-archetype-plugin/) | B | 3.4.1 | 2025-10-03 | Generate a skeleton project structure from an archetype. | [Git](https://gitbox.apache.org/repos/asf/maven-archetype.git) / [GitHub](https://github.com/apache/maven-archetype/) | [GitHub Issues](https://github.com/apache/maven-archetype/issues) |
| [`assembly`](https://maven.apache.org/plugins/maven-assembly-plugin/) | B | 3.8.0 | 2025-11-22 | Build an assembly (distribution) of sources and/or binaries. | [Git](https://gitbox.apache.org/repos/asf/maven-assembly-plugin.git) / [GitHub](https://github.com/apache/maven-assembly-plugin/) | [GitHub Issues](https://github.com/apache/maven-assembly-plugin/issues) |
| [`dependency`](https://maven.apache.org/plugins/maven-dependency-plugin/) | B+R | 3.10.0 | 2026-02-05 | Dependency manipulation (copy, unpack) and analysis. | [Git](https://gitbox.apache.org/repos/asf/maven-dependency-plugin.git) / [GitHub](https://github.com/apache/maven-dependency-plugin/) | [GitHub Issues](https://github.com/apache/maven-dependency-plugin/issues) |
| [`enforcer`](https://maven.apache.org/enforcer/maven-enforcer-plugin/) | B | 3.6.2 | 2025-09-28 | Environmental constraint checking (Maven Version, JDK etc), User Custom Rule Execution. | [Git](https://gitbox.apache.org/repos/asf/maven-enforcer.git) / [GitHub](https://github.com/apache/maven-enforcer/) | [GitHub Issues](https://github.com/apache/maven-enforcer/issues) |
| [`gpg`](https://maven.apache.org/plugins/maven-gpg-plugin/) | B | 3.2.8 | 2025-06-28 | Create signatures for the artifacts and poms. | [Git](https://gitbox.apache.org/repos/asf/maven-gpg-plugin.git) / [GitHub](https://github.com/apache/maven-gpg-plugin/) | [GitHub Issues](https://github.com/apache/maven-gpg-plugin/issues) |
| [`help`](https://maven.apache.org/plugins/maven-help-plugin/) | B | 3.5.1 | 2024-10-18 | Get information about the working environment for the project. | [Git](https://gitbox.apache.org/repos/asf/maven-help-plugin.git) / [GitHub](https://github.com/apache/maven-help-plugin/) | [GitHub Issues](https://github.com/apache/maven-help-plugin/issues) |
| [`invoker`](https://maven.apache.org/plugins/maven-invoker-plugin/) | B+R | 3.9.1 | 2025-06-23 | Run a set of Maven projects and verify the output. | [Git](https://gitbox.apache.org/repos/asf/maven-invoker-plugin.git) / [GitHub](https://github.com/apache/maven-invoker-plugin/) | [GitHub Issues](https://github.com/apache/maven-invoker-plugin/issues) |
| [`jarsigner`](https://maven.apache.org/plugins/maven-jarsigner-plugin/) | B | 3.1.0 | 2024-09-03 | Signs or verifies project artifacts. | [Git](https://gitbox.apache.org/repos/asf/maven-jarsigner-plugin.git) / [GitHub](https://github.com/apache/maven-jarsigner-plugin/) | [GitHub Issues](https://github.com/apache/maven-jarsigner-plugin/issues) |
| [`jdeprscan`](https://maven.apache.org/plugins/maven-jdeprscan-plugin/) | B | 3.0.0 | 2025-12-22 | Run JDK's JDeprScan tool on the project. | [Git](https://gitbox.apache.org/repos/asf/maven-jdeprscan-plugin.git) / [GitHub](https://github.com/apache/maven-jdeprscan-plugin/) | [GitHub Issues](https://github.com/apache/maven-jdeprscan-plugin/issues) |
| [`plugin`](https://maven.apache.org/plugin-tools/maven-plugin-plugin/) | B | 3.15.2 | 2025-10-20 | Create a Maven plugin descriptor for any mojos found in the source tree, to include in the JAR. | [Git](https://gitbox.apache.org/repos/asf/maven-plugin-tools.git) / [GitHub](https://github.com/apache/maven-plugin-tools/) | [GitHub Issues](https://github.com/apache/maven-plugin-tools/issues) |
| [`release`](https://maven.apache.org/plugins/maven-release-plugin/) | B | 3.3.1 | 2025-12-09 | Release the current project - updating the POM and tagging in the SCM. | [Git](https://gitbox.apache.org/repos/asf/maven-release.git) / [GitHub](https://github.com/apache/maven-release/) | [GitHub Issues](https://github.com/apache/maven-release/issues) |
| [`remote-resources`](https://maven.apache.org/plugins/maven-remote-resources-plugin/) | B | 3.3.0 | 2024-12-30 | Copy remote resources to the output directory for inclusion in the artifact. | [Git](https://gitbox.apache.org/repos/asf/maven-remote-resources-plugin.git) / [GitHub](https://github.com/apache/maven-remote-resources-plugin/) | [GitHub Issues](https://github.com/apache/maven-remote-resources-plugin/issues) |
| [`scm`](https://maven.apache.org/scm/maven-scm-plugin/) | B | 2.2.1 | 2025-09-19 | Execute SCM commands for the current project. | [Git](https://gitbox.apache.org/repos/asf/maven-scm.git) / [GitHub](https://github.com/apache/maven-scm/) | [GitHub Issues](https://github.com/apache/maven-scm/issues) |
| [`scm-publish`](https://maven.apache.org/plugins/maven-scm-publish-plugin/) | B | 3.3.0 | 2024-06-16 | Publish your Maven website to a scm location. | [Git](https://gitbox.apache.org/repos/asf/maven-scm-publish-plugin.git) / [GitHub](https://github.com/apache/maven-scm-publish-plugin/) | [GitHub Issues](https://github.com/apache/maven-scm-publish-plugin/issues) |
| [`scripting`](https://maven.apache.org/plugins/maven-scripting-plugin/) | B | 3.1.0 | 2025-12-22 | The Maven Scripting Plugin wraps the Scripting API according to JSR223. | [Git](https://gitbox.apache.org/repos/asf/maven-scripting-plugin.git) / [GitHub](https://github.com/apache/maven-scripting-plugin/) | [GitHub Issues](https://github.com/apache/maven-scripting-plugin/issues) |
| [`stage`](https://maven.apache.org/plugins/maven-stage-plugin/) | B | 1.0 | 2015-03-03 | Assists with release staging and promotion. | [Git](https://gitbox.apache.org/repos/asf/maven-stage-plugin.git) / [GitHub](https://github.com/apache/maven-stage-plugin/) | [GitHub Issues](https://github.com/apache/maven-stage-plugin/issues) |
| [`toolchains`](https://maven.apache.org/plugins/maven-toolchains-plugin/) | B | 3.2.0 | 2024-04-21 | Allows to share configuration across plugins. | [Git](https://gitbox.apache.org/repos/asf/maven-toolchains-plugin.git) / [GitHub](https://github.com/apache/maven-toolchains-plugin/) | [GitHub Issues](https://github.com/apache/maven-toolchains-plugin/issues) |
| [`wrapper`](https://maven.apache.org/tools/wrapper/maven-wrapper-plugin/) | B | 3.3.4 | 2025-09-08 | Download and unpack the maven wrapper distribution | [Git](https://gitbox.apache.org/repos/asf/maven-wrapper-plugin.git) / [GitHub](https://github.com/apache/maven-wrapper/) | [GitHub Issues](https://github.com/apache/maven-wrapper/issues) |

* **B**uild or **R**eporting plugin

There are also some sandbox plugins into our [source repository](https://svn.apache.org/repos/asf/maven/sandbox/trunk/plugins).

Previous archived versions of plugins reference documentations are [located here](https://maven.apache.org/plugins-archives/).

[](https://maven.apache.org/plugins/index.html)
Retired[](https://maven.apache.org/plugins/index.html#retired)
--------------------------------------------------------------

| **Plugin** | **Type*** | **Version** | **Retired Date** | **Description** |
| --- | --- | --- | --- | --- |
| [`ant`](https://maven.apache.org/plugins/maven-ant-plugin/) | B | 2.4 | 2019-06-02 | Generate an Ant build file for the project. |
| [`docck`](https://maven.apache.org/plugins/maven-docck-plugin/) | B | 1.2 | 2023-10-22 | Documentation checker plugin. |
| [`eclipse`](https://maven.apache.org/plugins/maven-eclipse-plugin/) | B | 2.10 | 2015-10-07 | Generate an Eclipse project files for the current project. |
| [`idea`](https://maven.apache.org/plugins/maven-idea-plugin/) | B | 2.2.1 | 2013-07-26 | Create/update an IDEA workspace for the current project (individual modules are created as IDEA modules) |
| [`linkcheck`](https://maven.apache.org/plugins/maven-linkcheck-plugin/) | R | 1.2 | 2025-09-16 | Generate a Linkcheck report of your project's documentation. |
| [`one`](https://maven.apache.org/plugins/maven-one-plugin/) | B | 1.3 | 2013-07-30 | A plugin for interacting with legacy Maven 1.x repositories and builds. |
| [`patch`](https://maven.apache.org/plugins/maven-patch-plugin/) | B | 1.3 | 2024-12-10 | Use the gnu patch tool to apply patch files to source code. |
| [`pdf`](https://maven.apache.org/plugins/maven-pdf-plugin/) | B | 1.6.2 | 2025-03-04 | Generate a PDF version of your project's documentation. |
| [`reactor`](https://maven.apache.org/plugins/maven-reactor-plugin/) | B | 1.1 | 2014-03-24 | Build a subset of interdependent projects in a reactor (Maven 2 only). |
| [`repository`](https://maven.apache.org/plugins/maven-repository-plugin/) | B | 2.4 | 2019-04-30 | Plugin to help with repository-based tasks. |
[](https://maven.apache.org/plugins/index.html)
Outside The Maven Land[](https://maven.apache.org/plugins/index.html#outside-the-maven-land)

--------------------------------------------------------------------------------------------

### At MojoHaus (formerly known as [](https://maven.apache.org/plugins/index.html)codehaus.org)[](https://maven.apache.org/plugins/index.html#at-mojohaus-formerly-known-as-codehaus-org)

There are also [many plug-ins](https://www.mojohaus.org/plugins.html) available at the [MojoHaus](https://github.com/mojohaus) project at GitHub.

Here are a few common ones:

| **Plugin** (see [complete list with version](https://www.mojohaus.org/plugins.html)) | **Description** |
| --- | --- |
| [`animal-sniffer`](https://www.mojohaus.org/animal-sniffer/animal-sniffer-maven-plugin/) | Build signatures of APIs (JDK for example) and checks your classes against them. |
| [`build-helper`](https://www.mojohaus.org/build-helper-maven-plugin/) | Attach extra artifacts and source directories to build. |
| [`buildplan`](https://www.mojohaus.org/buildplan-maven-plugin/) | Inspect the lifecycle of your build. |
| [`castor`](https://www.mojohaus.org/castor-maven-plugin/) | Generate sources from an XSD using Castor. |
| [`clirr`](https://www.mojohaus.org/clirr-maven-plugin/) | Compare binaries or sources for compatibility using Clirr |
| [`javacc`](https://www.mojohaus.org/javacc-maven-plugin/) | Generate sources from a JavaCC grammar. |
| [`jdepend`](https://www.mojohaus.org/jdepend-maven-plugin/) | Generate a report on code metrics using JDepend. |
| [`nar-maven-plugin`](https://maven-nar.github.io/) | Compiles C, C++, Fortran for different architectures. |
| [`native`](https://www.mojohaus.org/maven-native/native-maven-plugin/) | Compiles C and C++ code with native compilers. |
| [`sql`](https://www.mojohaus.org/sql-maven-plugin/) | Executes SQL scripts from files or inline. |
| [`taglist`](https://www.mojohaus.org/taglist-maven-plugin/) | Generate a list of tasks based on tags in your code. |
| [`versions`](https://www.mojohaus.org/versions-maven-plugin/) | Manage versions of your project, its modules, dependencies and plugins. |
[](https://maven.apache.org/plugins/index.html)

### Misc[](https://maven.apache.org/plugins/index.html#misc)

A number of other projects provide their own Maven plugins. This includes:

| **Plugin** | **Maintainer** | **Description** |
| --- | --- | --- |
| [`cargo`](https://codehaus-cargo.github.io/) | [Cargo Project](https://codehaus-cargo.github.io/) | Start/stop/configure J2EE containers and deploy to them. |
| [`clover`](https://confluence.atlassian.com/display/CLOVER/Clover-for-Maven+2) | [Atlassian Clover](https://www.atlassian.com/software/clover/) | Generate a Clover report. |
| [`jetty`](https://www.eclipse.org/jetty/documentation/current/jetty-maven-plugin.html) | [Jetty Project](https://www.eclipse.org/jetty/) | Jetty Run a Jetty container for rapid webapp development. |
| [`jalopy`](http://www.triemax.com/products/jalopy/manual/plugin-maven.html) | [Triemax](http://www.triemax.com/) | Use Jalopy to format your source code. |
| [`rat`](https://creadur.apache.org/rat/) | [Apache Creadur Project](https://creadur.apache.org/) | Release Audit Tool (RAT) to verify files. |
| [`Genesis Plugins`](https://geronimo.apache.org/maven/genesis/plugins/tools-maven-plugin/index.html) | [Apache Geronimo Project](https://geronimo.apache.org/) | Verify legal files in artifacts. |
| [`Apache Tomcat`](https://tomcat.apache.org/maven-plugin.html) | [Apache Tomcat Project](https://tomcat.apache.org/maven-plugin.html) | Run an Apache Tomcat container for rapid webapp development. |
| [`OWASP dependency-check`](https://dependency-check.github.io/DependencyCheck/) | [OWASP Dependency-check Project](https://www.owasp.org/index.php/OWASP_Dependency_Check) | Run OWASP Dependency-Check, a utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities. |
| [`CycloneDX`](https://github.com/CycloneDX/cyclonedx-maven-plugin) | [CycloneDX Project](https://cyclonedx.org/) | Generate Software Bill of Materials (SBOM) in CycloneDX format. |
| [`pgpverify`](https://www.simplify4u.org/pgpverify-maven-plugin/) | [Simplify4U](https://www.simplify4u.org/) | Verify PGP signature of all project dependencies. |
[](https://maven.apache.org/plugins/index.html)
Resources[](https://maven.apache.org/plugins/index.html#resources)

------------------------------------------------------------------

1. [Guide to Configuring Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
