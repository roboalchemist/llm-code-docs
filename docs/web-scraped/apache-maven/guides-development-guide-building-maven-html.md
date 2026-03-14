# Source: https://maven.apache.org/guides/development/guide-building-maven.html

Title: Building Maven – Maven

URL Source: https://maven.apache.org/guides/development/guide-building-maven.html

Markdown Content:
[](https://maven.apache.org/guides/development/guide-building-maven.html)[](https://maven.apache.org/guides/development/guide-building-maven.html)
Why would I want to build Maven?[](https://maven.apache.org/guides/development/guide-building-maven.html#why-would-i-want-to-build-maven)
-----------------------------------------------------------------------------------------------------------------------------------------

Building Maven (or a plugin, or any component) yourself is for one of two reasons:

*   to try out a bleeding edge feature or bugfix
*   to fix a problem you are having and submit a patch to the developers team.

Issues are tracked on the component's GitHub repository page. See the [issue management page](https://maven.apache.org/issue-management.html) for more details.

[](https://maven.apache.org/guides/development/guide-building-maven.html)
Checking out the sources[](https://maven.apache.org/guides/development/guide-building-maven.html#checking-out-the-sources)
--------------------------------------------------------------------------------------------------------------------------

The source code for Maven and its related libraries is managed in the ASF source code repositories. A full list of the repositories is listed on the [Getting Maven Source](https://maven.apache.org/scm.html) page.

[](https://maven.apache.org/guides/development/guide-building-maven.html)
Building Maven[](https://maven.apache.org/guides/development/guide-building-maven.html#building-maven)
------------------------------------------------------------------------------------------------------

[](https://maven.apache.org/guides/development/guide-building-maven.html)
### Building a Maven Plugin or Component[](https://maven.apache.org/guides/development/guide-building-maven.html#building-a-maven-plugin-or-component)

Building a Maven plugin or component is like any Maven build:

```
mvn verify
```
[](https://maven.apache.org/guides/development/guide-building-maven.html)
#### Running Integration Tests[](https://maven.apache.org/guides/development/guide-building-maven.html#running-integration-tests)

Before submitting a patch, it is advised to run the integration tests, which are available in the `run-its` profile:

```
mvn -Prun-its verify
```

See [Core ITs documentation](https://maven.apache.org/core-its/) for more options.

[](https://maven.apache.org/guides/development/guide-building-maven.html)
### Building Maven core[](https://maven.apache.org/guides/development/guide-building-maven.html#building-maven-core)

Until Maven 3.3, Maven core build could be bootstrapped with an Ant build. This bootstrap has been removed in Maven 3.5: you need a pre-built Maven to build Maven from source.

To do this, run from the source directory:

```
mvn install
```

The assemblies will be created in `apache-maven`, and can be manually unzipped to the location where you'd like the resulting Maven installed. If you want to have the resulting Maven directly copied to a directory, you can use the `distributionTargetDir` property:

```
mvn -DdistributionTargetDir="$HOME/app/maven/apache-maven-SNAPSHOT" install
```
