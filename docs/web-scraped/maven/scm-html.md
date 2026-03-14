# Source: https://maven.apache.org/scm.html

Title: Source Repository – Maven

URL Source: https://maven.apache.org/scm.html

Markdown Content:
[](https://maven.apache.org/scm.html)
Maven projects use [Git](http://git-scm.com/) to manage their source code.

Instructions on Git use can be found in the online book [Pro Git](http://git-scm.com/book/). Instructions for using the Apache Software Foundation Git repositories are at [GitBox - ASF Writable Git Services](https://git-wip-us.apache.org/).

[](https://maven.apache.org/scm.html)
Full Maven Sources[](https://maven.apache.org/scm.html#full-maven-sources)
--------------------------------------------------------------------------

As described in the next paragraphs, Maven full source code is dispatched in more than 100 Git repos: Maven core, but also plugins or components, skins, a few svn2git read-only mirrors…

To check out full Maven source code easily, we provide a simple way using additional [Google repo](https://android.googlesource.com/tools/repo) tool and an additional Git repository for tool's manifest:

| Content | Repository | Mirror |
| --- | --- | --- |
| Apache Maven [full source code](https://github.com/apache/maven-sources/blob/master/default.xml) | [`https://gitbox.apache.org/repos/asf/maven-sources.git`](https://gitbox.apache.org/repos/asf/maven-sources.git) | [GitHub](https://github.com/apache/maven-sources/) |

1. Install a Git client if needed and the [Google repo](https://android.googlesource.com/tools/repo) tool (see [manual install instructions](https://android.googlesource.com/tools/repo#install)).

2. Check out a new repo workspace and prepare master branch:

```
repo init -u https://github.com/apache/maven-sources.git
repo sync
repo start master --all
```
1. In your IDE, import the projects you're interested in from the repo workspace. Or directly build with command line the component you want.

[](https://maven.apache.org/scm.html)
Maven Sources Overview[](https://maven.apache.org/scm.html#maven-sources-overview)
----------------------------------------------------------------------------------

Each component has its own Jira project or component for issue tracking: see the [Issue Management report](https://maven.apache.org/issue-management.html) to get a summary.

[](https://maven.apache.org/scm.html)
Maven Site[](https://maven.apache.org/scm.html#maven-site)
----------------------------------------------------------

The sources for this site are available in a distinct Git repository.

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven Site](https://maven.apache.org/) | [`https://gitbox.apache.org/repos/asf/maven-site.git`](https://gitbox.apache.org/repos/asf/maven-site.git) | [GitHub](https://github.com/apache/maven-site/) | [GitHub Issues](https://github.com/apache/maven-site/issues/) |

_Note_: If you want to submit small site amendments, for example correct a spelling mistake, you don't have to install Git locally. You can simply hit the “Edit” ![Image 1: Edit button](https://maven.apache.org/images/accessories-text-editor.png) button after the page's title in the breadcrumb section on the top of the page. This will open the page's source file on GitHub, where you can edit it and easily open a pull request containing your change.

[](https://maven.apache.org/scm.html)
Maven Core[](https://maven.apache.org/scm.html#maven-core)
----------------------------------------------------------

The Git repository for [Maven](https://maven.apache.org/ref/current/) contains a master branch which is the current development version. There is also a branch for maven-2.2.X or maven-3.0.x. In addition, the [integration tests for the Maven core](https://maven.apache.org/core-its/) have their own repository.

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven](https://maven.apache.org/ref/current/) | [`https://gitbox.apache.org/repos/asf/maven.git`](https://gitbox.apache.org/repos/asf/maven.git) | [GitHub](https://github.com/apache/maven/) | [GitHub Issues](https://github.com/apache/maven/issues) |
| [Apache Maven Core ITs](https://maven.apache.org/core-its/) | [`https://gitbox.apache.org/repos/asf/maven-integration-testing.git`](https://gitbox.apache.org/repos/asf/maven-integration-testing.git) | [GitHub](https://github.com/apache/maven-integration-testing/) | N/A |
| [Apache Maven Build Cache Extension](https://maven.apache.org/extensions/maven-build-cache-extension/) | [`https://gitbox.apache.org/repos/asf/maven-build-cache-extension.git`](https://gitbox.apache.org/repos/asf/maven-build-cache-extension.git) | [GitHub](https://github.com/apache/maven-build-cache-extension/) | [GitHub Issues](https://github.com/apache/maven-build-cache-extension/issues) |
| [Apache Maven Daemon](https://github.com/apache/maven-mvnd) | [`https://gitbox.apache.org/repos/asf/maven-mvnd.git`](https://gitbox.apache.org/repos/asf/maven-mvnd.git) | [GitHub](https://github.com/apache/maven-mvnd/) | [GitHub Issues](https://github.com/apache/maven-mvnd/issues) |
| [Apache Maven Resolver](https://maven.apache.org/resolver/) | [`https://gitbox.apache.org/repos/asf/maven-resolver.git`](https://gitbox.apache.org/repos/asf/maven-resolver.git) | [GitHub](https://github.com/apache/maven-resolver/) | [GitHub Issues](https://github.com/apache/maven-resolver/issues) |
| [Apache Maven Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/) | [`https://gitbox.apache.org/repos/asf/maven-resolver-ant-tasks.git`](https://gitbox.apache.org/repos/asf/maven-resolver-ant-tasks.git) | [GitHub](https://github.com/apache/maven-resolver-ant-tasks/) | [GitHub Issues](https://github.com/apache/maven-resolver-ant-tasks/issues) |
| [Apache Maven Wrapper](https://maven.apache.org/wrapper/) | [`https://gitbox.apache.org/repos/asf/maven-wrapper.git`](https://gitbox.apache.org/repos/asf/maven-wrapper.git) | [GitHub](https://github.com/apache/maven-wrapper/) | [GitHub Issues](https://github.com/apache/maven-wrapper/issues) |
[](https://maven.apache.org/scm.html)
Other Components[](https://maven.apache.org/scm.html#other-components)

----------------------------------------------------------------------

The source repositories for the various plugins are in Git, listed in the documentation of the respective plugin, reachable via the [plugin index](https://maven.apache.org/plugins/index.html). There are also many shared components and subsystems with their own source repositories, mainly in Git, some in Subversion.

[](https://maven.apache.org/scm.html)

### Components in Git[](https://maven.apache.org/scm.html#components-in-git)

The components in Git are shown in the following table.

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven Archetype](https://maven.apache.org/archetype/) | [`https://gitbox.apache.org/repos/asf/maven-archetype.git`](https://gitbox.apache.org/repos/asf/maven-archetype.git) | [GitHub](https://github.com/apache/maven-archetype/) | [GitHub Issues](https://github.com/apache/maven-archetype/issues) |
| [Apache Maven Archetypes](https://maven.apache.org/archetypes/) | [`https://gitbox.apache.org/repos/asf/maven-archetypes.git`](https://gitbox.apache.org/repos/asf/maven-archetypes.git) | [GitHub](https://github.com/apache/maven-archetypes/) | [GitHub Issues](https://github.com/apache/maven-archetypes/issues) |
| [Apache Maven Artifact Resolver](https://maven.apache.org/resolver/) | [`https://gitbox.apache.org/repos/asf/maven-resolver.git`](https://gitbox.apache.org/repos/asf/maven-resolver.git) | [GitHub](https://github.com/apache/maven-resolver/) | [GitHub Issues](https://github.com/apache/maven-resolver/issues) |
| [Apache Maven Artifact Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/) | [`https://gitbox.apache.org/repos/asf/maven-resolver-ant-tasks.git`](https://gitbox.apache.org/repos/asf/maven-resolver-ant-tasks.git) | [GitHub](https://github.com/apache/maven-resolver-ant-tasks/) | [GitHub Issues](https://github.com/apache/maven-resolver-ant-tasks/issues) |
| [Apache Maven Distribution Checking Tool](https://ci-maven.apache.org/job/Maven/job/maven-box/job/maven-dist-tool/job/master/site/) | [`https://gitbox.apache.org/repos/asf/maven-dist-tool.git`](https://gitbox.apache.org/repos/asf/maven-dist-tool.git) | [GitHub](https://github.com/apache/maven-dist-tool/) | [GitHub Issues](https://github.com/apache/maven-dist-tool/issues) |
| [Apache Maven Enforcer](https://maven.apache.org/enforcer/) | [`https://gitbox.apache.org/repos/asf/maven-enforcer.git`](https://gitbox.apache.org/repos/asf/maven-enforcer.git) | [GitHub](https://github.com/apache/maven-enforcer/) | [GitHub Issues](https://github.com/apache/maven-enforcer/issues) |
| [Apache Maven JXR](https://maven.apache.org/jxr/) | [`https://gitbox.apache.org/repos/asf/maven-jxr.git`](https://gitbox.apache.org/repos/asf/maven-jxr.git) | [GitHub](https://github.com/apache/maven-jxr/) | [GitHub Issues](https://github.com/apache/maven-jxr/issues) |
| [Apache Maven Indexer](https://maven.apache.org/maven-indexer/) | [`https://gitbox.apache.org/repos/asf/maven-indexer.git`](https://gitbox.apache.org/repos/asf/maven-indexer.git) | [GitHub](https://github.com/apache/maven-indexer/) | [GitHub Issues](https://github.com/apache/maven-indexer/issues) |
| [Apache Maven Plugin Testing](https://maven.apache.org/plugin-testing/) | [`https://gitbox.apache.org/repos/asf/maven-plugin-testing.git`](https://gitbox.apache.org/repos/asf/maven-plugin-testing.git) | [GitHub](https://github.com/apache/maven-plugin-testing/) | [GitHub Issues](https://github.com/apache/maven-plugin-testing/issues) |
| [Apache Maven Plugin Tools](https://maven.apache.org/plugin-tools/) | [`https://gitbox.apache.org/repos/asf/maven-plugin-tools.git`](https://gitbox.apache.org/repos/asf/maven-plugin-tools.git) | [GitHub](https://github.com/apache/maven-plugin-tools/) | [GitHub Issues](https://github.com/apache/maven-plugin-tools/issues) |
| [Apache Maven Release](https://maven.apache.org/maven-release/) (Release api and plugin) | [`https://gitbox.apache.org/repos/asf/maven-release.git`](https://gitbox.apache.org/repos/asf/maven-release.git) | [GitHub](https://github.com/apache/maven-release/) | [GitHub Issues](https://github.com/apache/maven-release/issues) |
| [Apache Maven SCM](https://maven.apache.org/scm/) | [`https://gitbox.apache.org/repos/asf/maven-scm.git`](https://gitbox.apache.org/repos/asf/maven-scm.git) | [GitHub](https://github.com/apache/maven-scm/) | [GitHub Issues](https://github.com/apache/maven-scm/issues) |
| [Apache Maven Surefire](https://maven.apache.org/surefire/) | [`https://gitbox.apache.org/repos/asf/maven-surefire.git`](https://gitbox.apache.org/repos/asf/maven-surefire.git) | [GitHub](https://github.com/apache/maven-surefire/) | [GitHub Issues](https://github.com/apache/maven-surefire/issues) |
| [Apache Maven Wagon](https://maven.apache.org/wagon/) | [`https://gitbox.apache.org/repos/asf/maven-wagon.git`](https://gitbox.apache.org/repos/asf/maven-wagon.git) | [GitHub](https://github.com/apache/maven-wagon/) | [GitHub Issues](https://github.com/apache/maven-wagon/issues) |
[](https://maven.apache.org/scm.html)

#### Plugins[](https://maven.apache.org/scm.html#plugins)

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven ACR Plugin](https://maven.apache.org/plugins/maven-acr-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-acr-plugin.git`](https://gitbox.apache.org/repos/asf/maven-acr-plugin.git) | [GitHub](https://github.com/apache/maven-acr-plugin/) | [GitHub Issues](https://github.com/apache/maven-acr-plugin/issues) |
| [Apache Maven AntRun Plugin](https://maven.apache.org/plugins/maven-antrun-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-antrun-plugin.git`](https://gitbox.apache.org/repos/asf/maven-antrun-plugin.git) | [GitHub](https://github.com/apache/maven-antrun-plugin/) | [GitHub Issues](https://github.com/apache/maven-antrun-plugin/issues) |
| [Apache Maven Artifact Plugin](https://maven.apache.org/plugins/maven-artifact-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-artifact-plugin.git`](https://gitbox.apache.org/repos/asf/maven-artifact-plugin.git) | [GitHub](https://github.com/apache/maven-artifact-plugin/) | [GitHub Issues](https://github.com/apache/maven-artifact-plugin/issues) |
| [Apache Maven Assembly Plugin](https://maven.apache.org/plugins/maven-assembly-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-assembly-plugin.git`](https://gitbox.apache.org/repos/asf/maven-assembly-plugin.git) | [GitHub](https://github.com/apache/maven-assembly-plugin/) | [GitHub Issues](https://github.com/apache/maven-assembly-plugin/issues) |
| [Apache Maven Changelog Plugin](https://maven.apache.org/plugins/maven-changelog-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-changelog-plugin.git`](https://gitbox.apache.org/repos/asf/maven-changelog-plugin.git) | [GitHub](https://github.com/apache/maven-changelog-plugin/) | [GitHub Issues](https://github.com/apache/maven-changelog-plugin/issues) |
| [Apache Maven Changes Plugin](https://maven.apache.org/plugins/maven-changes-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-changes-plugin.git`](https://gitbox.apache.org/repos/asf/maven-changes-plugin.git) | [GitHub](https://github.com/apache/maven-changes-plugin/) | [GitHub Issues](https://github.com/apache/maven-changes-plugin/issues) |
| [Apache Maven Checkstyle Plugin](https://maven.apache.org/plugins/maven-checkstyle-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-checkstyle-plugin.git`](https://gitbox.apache.org/repos/asf/maven-checkstyle-plugin.git) | [GitHub](https://github.com/apache/maven-checkstyle-plugin/) | [GitHub Issues](https://github.com/apache/maven-checkstyle-plugin/issues) |
| [Apache Maven Clean Plugin](https://maven.apache.org/plugins/maven-clean-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-clean-plugin.git`](https://gitbox.apache.org/repos/asf/maven-clean-plugin.git) | [GitHub](https://github.com/apache/maven-clean-plugin/) | [GitHub Issues](https://github.com/apache/maven-clean-plugin/issues) |
| [Apache Maven Compiler Plugin](https://maven.apache.org/plugins/maven-compiler-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-compiler-plugin.git`](https://gitbox.apache.org/repos/asf/maven-compiler-plugin.git) | [GitHub](https://github.com/apache/maven-compiler-plugin/) | [GitHub Issues](https://github.com/apache/maven-compiler-plugin/issues) |
| [Apache Maven Dependency Plugin](https://maven.apache.org/plugins/maven-dependency-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-dependency-plugin.git`](https://gitbox.apache.org/repos/asf/maven-dependency-plugin.git) | [GitHub](https://github.com/apache/maven-dependency-plugin/) | [GitHub Issues](https://github.com/apache/maven-dependency-plugin/issues) |
| [Apache Maven Deploy Plugin](https://maven.apache.org/plugins/maven-deploy-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-deploy-plugin.git`](https://gitbox.apache.org/repos/asf/maven-deploy-plugin.git) | [GitHub](https://github.com/apache/maven-deploy-plugin/) | [GitHub Issues](https://github.com/apache/maven-deploy-plugin/issues) |
| [Apache Maven DOAP Plugin](https://maven.apache.org/plugins/maven-doap-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-doap-plugin.git`](https://gitbox.apache.org/repos/asf/maven-doap-plugin.git) | [GitHub](https://github.com/apache/maven-doap-plugin/) | [GitHub Issues](https://github.com/apache/maven-doap-plugin/issues) |
| [Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-ear-plugin.git`](https://gitbox.apache.org/repos/asf/maven-ear-plugin.git) | [GitHub](https://github.com/apache/maven-ear-plugin/) | [GitHub Issues](https://github.com/apache/maven-ear-plugin/issues) |
| [Apache Maven EJB Plugin](https://maven.apache.org/plugins/maven-ejb-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-ejb-plugin.git`](https://gitbox.apache.org/repos/asf/maven-ejb-plugin.git) | [GitHub](https://github.com/apache/maven-ejb-plugin/) | [GitHub Issues](https://github.com/apache/maven-ejb-plugin/issues) |
| [Apache Maven GPG Plugin](https://maven.apache.org/plugins/maven-gpg-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-gpg-plugin.git`](https://gitbox.apache.org/repos/asf/maven-gpg-plugin.git) | [GitHub](https://github.com/apache/maven-gpg-plugin/) | [GitHub Issues](https://github.com/apache/maven-gpg-plugin/issues) |
| [Apache Maven Help Plugin](https://maven.apache.org/plugins/maven-help-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-help-plugin.git`](https://gitbox.apache.org/repos/asf/maven-help-plugin.git) | [GitHub](https://github.com/apache/maven-help-plugin/) | [GitHub Issues](https://github.com/apache/maven-help-plugin/issues) |
| [Apache Maven Install Plugin](https://maven.apache.org/plugins/maven-install-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-install-plugin.git`](https://gitbox.apache.org/repos/asf/maven-install-plugin.git) | [GitHub](https://github.com/apache/maven-install-plugin/) | [GitHub Issues](https://github.com/apache/maven-install-plugin/isuess) |
| [Apache Maven Invoker Plugin](https://maven.apache.org/plugins/maven-invoker-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-invoker-plugin.git`](https://gitbox.apache.org/repos/asf/maven-invoker-plugin.git) | [GitHub](https://github.com/apache/maven-invoker-plugin/) | [GitHub Issues](https://github.com/apache/maven-invoker-plugin/issues) |
| [Apache Maven JAR Plugin](https://maven.apache.org/plugins/maven-jar-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jar-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jar-plugin.git) | [GitHub](https://github.com/apache/maven-jar-plugin/) | [GitHub Issues](https://github.com/apache/maven-jar-plugin/issues) |
| [Apache Maven Jarsigner Plugin](https://maven.apache.org/plugins/maven-jarsigner-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jarsigner-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jarsigner-plugin.git) | [GitHub](https://github.com/apache/maven-jarsigner-plugin/) | [GitHub Issues](https://github.com/apache/maven-jarsigner-plugin/issues) |
| [Apache Maven Javadoc Plugin](https://maven.apache.org/plugins/maven-javadoc-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-javadoc-plugin.git`](https://gitbox.apache.org/repos/asf/maven-javadoc-plugin.git) | [GitHub](https://github.com/apache/maven-javadoc-plugin/) | [GitHub Issues](https://github.com/apache/maven-javadoc-plugin/issues) |
| [Apache Maven JDepRScan Plugin](https://maven.apache.org/plugins/maven-jdeprscan-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jdeprscan-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jdeprscan-plugin.git) | [GitHub](https://github.com/apache/maven-jdeprscan-plugin/) | [GitHub Issues](https://github.com/apache/maven-jdeprscan-plugin/issues) |
| [Apache Maven JDeps Plugin](https://maven.apache.org/plugins/maven-jdeps-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jdeps-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jdeps-plugin.git) | [GitHub](https://github.com/apache/maven-jdeps-plugin/) | [GitHub Issues](https://github.com/apache/maven-jdeps-plugin/issues) |
| [Apache Maven JLink Plugin](https://maven.apache.org/plugins/maven-jlink-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jlink-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jlink-plugin.git) | [GitHub](https://github.com/apache/maven-jlink-plugin/) | [GitHub Issues](https://github.com/apache/maven-jlink-plugin/issues) |
| [Apache Maven JMod Plugin](https://maven.apache.org/plugins/maven-jmod-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-jmod-plugin.git`](https://gitbox.apache.org/repos/asf/maven-jmod-plugin.git) | [GitHub](https://github.com/apache/maven-jmod-plugin/) | [GitHub Issues](https://github.com/apache/maven-jmod-plugin/issues) |
| [Apache Maven PMD Plugin](https://maven.apache.org/plugins/maven-pmd-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-pmd-plugin.git`](https://gitbox.apache.org/repos/asf/maven-pmd-plugin.git) | [GitHub](https://github.com/apache/maven-pmd-plugin/) | [GitHub Issues](https://github.com/apache/maven-pmd-plugin/issues) |
| [Apache Maven Project Info Reports Plugin](https://maven.apache.org/plugins/maven-project-info-reports-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-project-info-reports-plugin.git`](https://gitbox.apache.org/repos/asf/maven-project-info-reports-plugin.git) | [GitHub](https://github.com/apache/maven-project-info-reports-plugin/) | [GitHub Issues](https://github.com/apache/maven-project-info-reports-plugin/issues) |
| [Apache Maven RAR Plugin](https://maven.apache.org/plugins/maven-rar-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-rar-plugin.git`](https://gitbox.apache.org/repos/asf/maven-rar-plugin.git) | [GitHub](https://github.com/apache/maven-rar-plugin/) | [GitHub Issues](https://github.com/apache/maven-rar-plugin/issues) |
| [Apache Maven Remote Resources Plugin](https://maven.apache.org/plugins/maven-remote-resources-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-remote-resources-plugin.git`](https://gitbox.apache.org/repos/asf/maven-remote-resources-plugin.git) | [GitHub](https://github.com/apache/maven-remote-resources-plugin/) | [GitHub Issues](https://github.com/apache/maven-remote-resources-plugin/issues) |
| [Apache Maven Resources Plugin](https://maven.apache.org/plugins/maven-resources-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-resources-plugin.git`](https://gitbox.apache.org/repos/asf/maven-resources-plugin.git) | [GitHub](https://github.com/apache/maven-resources-plugin/) | [GitHub Issues](https://github.com/apache/maven-resources-plugin/issues) |
| [Apache Maven SCM Publish Plugin](https://maven.apache.org/plugins/maven-scm-publish-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-scm-publish-plugin.git`](https://gitbox.apache.org/repos/asf/maven-scm-publish-plugin.git) | [GitHub](https://github.com/apache/maven-scm-publish-plugin/) | [GitHub Issues](https://github.com/apache/maven-scm-publish-plugin/issues) |
| [Apache Maven Scripting Plugin](https://maven.apache.org/plugins/maven-scripting-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-scripting-plugin.git`](https://gitbox.apache.org/repos/asf/maven-scripting-plugin.git) | [GitHub](https://github.com/apache/maven-scripting-plugin/) | [GitHub Issues](https://github.com/apache/maven-scripting-plugin/issues) |
| [Apache Maven Shade Plugin](https://maven.apache.org/plugins/maven-shade-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-shade-plugin.git`](https://gitbox.apache.org/repos/asf/maven-shade-plugin.git) | [GitHub](https://github.com/apache/maven-shade-plugin/) | [GitHub Issues](https://github.com/apache/maven-shade-plugin/issues) |
| [Apache Maven Site Plugin](https://maven.apache.org/plugins/maven-site-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-site-plugin.git`](https://gitbox.apache.org/repos/asf/maven-site-plugin.git) | [GitHub](https://github.com/apache/maven-site-plugin/) | [GitHub Issues](https://github.com/apache/maven-site-plugin/issues) |
| [Apache Maven Source Plugin](https://maven.apache.org/plugins/maven-source-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-source-plugin.git`](https://gitbox.apache.org/repos/asf/maven-source-plugin.git) | [GitHub](https://github.com/apache/maven-source-plugin/) | [GitHub Issues](https://github.com/apache/maven-source-plugin/issues) |
| [Apache Maven Stage Plugin](https://maven.apache.org/plugins/maven-stage-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-stage-plugin.git`](https://gitbox.apache.org/repos/asf/maven-stage-plugin.git) | [GitHub](https://github.com/apache/maven-stage-plugin/) | [GitHub Issues](https://github.com/apache/maven-stage-plugin/issues) |
| [Apache Maven Toolchains Plugin](https://maven.apache.org/plugins/maven-toolchains-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-toolchains-plugin.git`](https://gitbox.apache.org/repos/asf/maven-toolchains-plugin.git) | [GitHub](https://github.com/apache/maven-toolchains-plugin/) | [GitHub Issues](https://github.com/apache/maven-toolchains-plugin/issues) |
| [Apache Maven Verifier Plugin](https://maven.apache.org/plugins/maven-verifier-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-verifier-plugin.git`](https://gitbox.apache.org/repos/asf/maven-verifier-plugin.git) | [GitHub](https://github.com/apache/maven-verifier-plugin/) | [GitHub Issues](https://github.com/apache/maven-verifier-plugin/issues) |
| [Apache Maven WAR Plugin](https://maven.apache.org/plugins/maven-war-plugin/) | [`https://gitbox.apache.org/repos/asf/maven-war-plugin.git`](https://gitbox.apache.org/repos/asf/maven-war-plugin.git) | [GitHub](https://github.com/apache/maven-war-plugin/) | [GitHub Issues](https://github.com/apache/maven-war-plugin/issues) |
[](https://maven.apache.org/scm.html)

#### Parent POMs[](https://maven.apache.org/scm.html#parent-poms)

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Parent POM](https://maven.apache.org/pom/asf/) | [`https://gitbox.apache.org/repos/asf/maven-apache-parent.git`](https://gitbox.apache.org/repos/asf/maven-apache-parent.git) | [GitHub](https://github.com/apache/maven-apache-parent/) | [GitHub Issues](https://github.com/apache/maven-apache-parent/issues) |
| [Apache Maven Parent POMs](https://maven.apache.org/pom/maven/) | [`https://gitbox.apache.org/repos/asf/maven-parent.git`](https://gitbox.apache.org/repos/asf/maven-parent.git) | [GitHub](https://github.com/apache/maven-parent/) | [GitHub Issues](https://github.com/apache/maven-parent/issues) |
| [Apache Resource Bundles](https://maven.apache.org/apache-resource-bundles/) | [`https://gitbox.apache.org/repos/asf/maven-apache-resources.git`](https://gitbox.apache.org/repos/asf/maven-apache-resources.git) | [GitHub](https://github.com/apache/maven-apache-resources/) | [GitHub Issues](https://github.com/apache/maven-apache-resources/issues) |
[](https://maven.apache.org/scm.html)

#### Shared Components[](https://maven.apache.org/scm.html#shared-components)

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven Archiver](https://maven.apache.org/shared/maven-archiver/) | [`https://gitbox.apache.org/repos/asf/maven-archiver.git`](https://gitbox.apache.org/repos/asf/maven-archiver.git) | [GitHub](https://github.com/apache/maven-archiver/) | [GitHub Issues](https://github.com/apache/maven-archiver/issues) |
| [Apache Maven Artifact Resolver](https://maven.apache.org/shared/maven-artifact-resolver/) | [`https://gitbox.apache.org/repos/asf/maven-artifact-resolver.git`](https://gitbox.apache.org/repos/asf/maven-artifact-resolver.git) | [GitHub](https://github.com/apache/maven-artifact-resolver/) | [JIRA MRESOLVER](https://issues.apache.org/jira/projects/MRESOLVER) |
| [Apache Maven Common Artifact Filters](https://maven.apache.org/shared/maven-common-artifact-filters/) | [`https://gitbox.apache.org/repos/asf/maven-common-artifact-filters.git`](https://gitbox.apache.org/repos/asf/maven-common-artifact-filters.git) | [GitHub](https://github.com/apache/maven-common-artifact-filters/) | [GitHub Issues](https://github.com/apache/maven-common-artifact-filters/issues) |
| [Apache Maven Dependency Analyzer](https://maven.apache.org/shared/maven-dependency-analyzer/) | [`https://gitbox.apache.org/repos/asf/maven-dependency-analyzer.git`](https://gitbox.apache.org/repos/asf/maven-dependency-analyzer.git) | [GitHub](https://github.com/apache/maven-dependency-analyzer/) | [GitHub Issues](https://github.com/apache/maven-dependency-analyzer/issues) |
| [Apache Maven Dependency Tree](https://maven.apache.org/shared/maven-dependency-tree/) | [`https://gitbox.apache.org/repos/asf/maven-dependency-tree.git`](https://gitbox.apache.org/repos/asf/maven-dependency-tree.git) | [GitHub](https://github.com/apache/maven-dependency-tree/) | [GitHub Issues](https://github.com/apache/maven-dependency-tree/issues) |
| [Apache Maven Filtering](https://maven.apache.org/shared/maven-filtering/) | [`https://gitbox.apache.org/repos/asf/maven-filtering.git`](https://gitbox.apache.org/repos/asf/maven-filtering.git) | [GitHub](https://github.com/apache/maven-filtering/) | [GitHub Issues](https://github.com/apache/maven-filtering/issues) |
| [Apache Maven Invoker](https://maven.apache.org/shared/maven-invoker/) | [`https://gitbox.apache.org/repos/asf/maven-invoker.git`](https://gitbox.apache.org/repos/asf/maven-invoker.git) | [GitHub](https://github.com/apache/maven-invoker/) | [GitHub Issues](https://github.com/apache/maven-invoker/issues) |
| [Apache Maven Jarsigner](https://maven.apache.org/shared/maven-jarsigner/) | [`https://gitbox.apache.org/repos/asf/maven-jarsigner.git`](https://gitbox.apache.org/repos/asf/maven-jarsigner.git) | [GitHub](https://github.com/apache/maven-jarsigner/) | [GitHub Issues](https://github.com/apache/maven-jarsigner/issues) |
| [Apache Maven Mapping](https://maven.apache.org/shared/maven-mapping/) | [`https://gitbox.apache.org/repos/asf/maven-mapping.git`](https://gitbox.apache.org/repos/asf/maven-mapping.git) | [GitHub](https://github.com/apache/maven-mapping/) | [GitHub Issues](https://github.com/apache/maven-mapping/issues) |
| [Apache Maven Reporting API](https://maven.apache.org/shared/maven-reporting-api/) | [`https://gitbox.apache.org/repos/asf/maven-reporting-api.git`](https://gitbox.apache.org/repos/asf/maven-reporting-api.git) | [GitHub](https://github.com/apache/maven-reporting-api/) | [GitHub Issues](https://github.com/apache/maven-reporting-api/issues) |
| [Apache Maven Reporting Executor](https://maven.apache.org/shared/maven-reporting-exec/) | [`https://gitbox.apache.org/repos/asf/maven-reporting-exec.git`](https://gitbox.apache.org/repos/asf/maven-reporting-exec.git) | [GitHub](https://github.com/apache/maven-reporting-exec/) | [GitHub Issues](https://github.com/apache/maven-reporting-exec/issues) |
| [Apache Maven Reporting Implementation](https://maven.apache.org/shared/maven-reporting-impl/) | [`https://gitbox.apache.org/repos/asf/maven-reporting-impl.git`](https://gitbox.apache.org/repos/asf/maven-reporting-impl.git) | [GitHub](https://github.com/apache/maven-reporting-impl/) | [GitHub Issues](https://github.com/apache/maven-reporting-impl/issues) |
| [Apache Maven Script Interpreter](https://maven.apache.org/shared/maven-script-interpreter/) | [`https://gitbox.apache.org/repos/asf/maven-script-interpreter.git`](https://gitbox.apache.org/repos/asf/maven-script-interpreter.git) | [GitHub](https://github.com/apache/maven-script-interpreter/) | [GitHub Issues](https://github.com/apache/maven-script-interpreter/issues) |
| [Apache Maven Shared Incremental](https://maven.apache.org/shared/maven-shared-incremental/) | [`https://gitbox.apache.org/repos/asf/maven-shared-incremental.git`](https://gitbox.apache.org/repos/asf/maven-shared-incremental.git) | [GitHub](https://github.com/apache/maven-shared-incremental/) | [GitHub Issues](https://github.com/apache/maven-shared-incremental/issues) |
| [Apache Maven Shared IO](https://maven.apache.org/shared/maven-shared-io/) | [`https://gitbox.apache.org/repos/asf/maven-shared-io.git`](https://gitbox.apache.org/repos/asf/maven-shared-io.git) | [GitHub](https://github.com/apache/maven-shared-io/) | [GitHub Issues](https://github.com/apache/maven-shared-io/issues) |
| [Apache Maven Shared Jar](https://maven.apache.org/shared/maven-shared-jar/) | [`https://gitbox.apache.org/repos/asf/maven-shared-jar.git`](https://gitbox.apache.org/repos/asf/maven-shared-jar.git) | [GitHub](https://github.com/apache/maven-shared-jar/) | [GitHub Issues](https://github.com/apache/maven-shared-jar/issues) |
| [Apache Maven Shared Resources](https://maven.apache.org/shared/maven-shared-resources/) | [`https://gitbox.apache.org/repos/asf/maven-shared-resources.git`](https://gitbox.apache.org/repos/asf/maven-shared-resources.git) | [GitHub](https://github.com/apache/maven-shared-resources/) | [GitHub Isuess](https://github.com/apache/maven-shared-resources/issues) |
| [Apache Maven Shared Utils](https://maven.apache.org/shared/maven-shared-utils/) | [`https://gitbox.apache.org/repos/asf/maven-shared-utils.git`](https://gitbox.apache.org/repos/asf/maven-shared-utils.git) | [GitHub](https://github.com/apache/maven-shared-utils/) | [GitHub Issues](https://github.com/apache/maven-shared-utils/issues) |
| [Apache Maven Verifier](https://maven.apache.org/shared/maven-verifier/) | [`https://gitbox.apache.org/repos/asf/maven-verifier.git`](https://gitbox.apache.org/repos/asf/maven-verifier.git) | [GitHub](https://github.com/apache/maven-verifier/) | [GitHub Issues](https://github.com/apache/maven-verifier/issues) |
[](https://maven.apache.org/scm.html)

#### Skins[](https://maven.apache.org/scm.html#skins)

| Content | Repository | Mirror | Issues |
| --- | --- | --- | --- |
| [Apache Maven Fluido Skin](https://maven.apache.org/skins/maven-fluido-skin/) | [`https://gitbox.apache.org/repos/asf/maven-fluido-skin.git`](https://gitbox.apache.org/repos/asf/maven-fluido-skin.git) | [GitHub](https://github.com/apache/maven-fluido-skin/) | [GitHub Issues](https://github.com/apache/maven-fluido-skin/issues) |
[](https://maven.apache.org/scm.html)

#### Components in Subversion[](https://maven.apache.org/scm.html#components-in-subversion)

Everything in Subversion can be checked-out from a single entry point, referencing each part through svn:externals [`https://svn.apache.org/repos/asf/maven/trunks/`](https://svn.apache.org/repos/asf/maven/trunks/).

You can also check out every component separately. The components in Subversion are:

| Content | Repository | Mirror |
| --- | --- | --- |
| Maven Project (mainly KEYS) | [`https://svn.apache.org/viewvc/maven/project`](https://svn.apache.org/repos/asf/maven/project/) |  |
| Maven Sandbox | [`https://svn.apache.org/viewvc/maven/sandbox/trunk/`](https://svn.apache.org/repos/asf/maven/sandbox/trunk/) | [GitHub](https://github.com/apache/maven-sandbox/) |
| A variety of other subsystems (including obsolete trees replaced by git) | [`https://svn.apache.org/viewvc/maven/`](https://svn.apache.org/repos/asf/maven/) |  |
