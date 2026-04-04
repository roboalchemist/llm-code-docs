# Source: https://maven.apache.org/guides/development/guide-testing-development-plugins.html

Title: Guide to Testing Development Versions of Plugins – Maven

URL Source: https://maven.apache.org/guides/development/guide-testing-development-plugins.html

Markdown Content:
[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)
Why would I want to do this?[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html#why-would-i-want-to-do-this)
----------------------------------------------------------------------------------------------------------------------------------------------

If a bug you are encountering has been reported as fixed but not yet released, you can confirm that it has been fixed for you. Or perhaps you just like to live on the bleeding edge.

You are highly encouraged to join the development list for the project and provide your feedback, or help promote release of the plugin in question.

_Note:_ This is **not** recommended as an everyday or in production practice! Snapshots are for testing purposes only and are not official releases. For more information, see [the Releases FAQ](http://www.apache.org/dev/release.html#what).

[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)
How do I do this?[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html#how-do-i-do-this)
------------------------------------------------------------------------------------------------------------------------

Development versions of Maven plugins are periodically published to the repository: [https://repository.apache.org/snapshots/](https://repository.apache.org/snapshots/).

_Note:_ Currently, this is not done automatically by our continuous integration setup. This is coming soon.

Other sites may publish their own - for example, the MojoHaus project hosts theirs at [https://oss.sonatype.org/content/repositories/snapshots/](https://oss.sonatype.org/content/repositories/snapshots/)

The first step is to include this in your project:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<pluginRepositories>`
4.   `<pluginRepository>`
5.   `<id>apache.snapshots</id>`
6.   `<url>https://repository.apache.org/snapshots/</url>`
7.   `</pluginRepository>`
8.   `</pluginRepositories>`
9.   `...`
10.   `</project>`

After this is included, there are three ways to use the updated versions:

*   Set the appropriate version in the plugin, eg `2.0.1-SNAPSHOT`

*   If you have not specified a version, use the `-U` switch to update plugins for the given Maven run

*   You can have Maven automatically check for updates on a given interval, for example:

    1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
    2.   `...`
    3.   `<pluginRepositories>`
    4.   `<pluginRepository>`
    5.   `<id>apache.snapshots</id>`
    6.   `<url>https://repository.apache.org/snapshots/</url>`
    7.   `<snapshots>`
    8.   `<enabled>true</enabled>`
    9.   `<updatePolicy>interval:15</updatePolicy>`
    10.   `</snapshots>`
    11.   `</pluginRepository>`
    12.   `</pluginRepositories>`
    13.   `...`
    14.   `</project>`

_Note:_ These last two techniques mean that _every_ plugin will be updated to the latest snapshot version.

The development version will stop being used if the `<pluginRepository>` element is removed from your POM and the version is set back to the release version. If you are using the command line or an unspecified version, you will also need to remove the version from the local repository.

[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)
Using Settings without Modifying the Project[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html#using-settings-without-modifying-the-project)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using the goals from the command line on a number of projects, you should include this in your `settings.xml` file instead.

You need to modify your `${user.home}/.m2/settings.xml` file to include two new profiles and then when you need access to the plugin snapshots use `-Papache`. The profile only needs to be enabled once so that the plugins can be downloaded into you local repository. Once in your local repository Maven can successfully resolve the dependencies and the profile no longer needs to be activated.

1.   `<settings>`
2.   `...`
3.   `<profiles>`
4.   `<profile>`
5.   `<id>apache</id>`
6.   `<pluginRepositories>`
7.   `<pluginRepository>`
8.   `<id>apache.snapshots</id>`
9.   `<name>Maven Plugin Snapshots</name>`
10.   `<url>https://repository.apache.org/snapshots/</url>`
11.   `<releases>`
12.   `<enabled>false</enabled>`
13.   `</releases>`
14.   `<snapshots>`
15.   `<enabled>true</enabled>`
16.   `</snapshots>`
17.   `</pluginRepository>`
18.   `</pluginRepositories>`
19.   `</profile>`
20.   `</profiles>`
21.   `...`
22.   `</settings>`

When invoking Maven for Apache profile, do it like this:

```
mvn -Papache <phase|goal>
```
[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)
Using a Repository Manager[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html#using-a-repository-manager)
-------------------------------------------------------------------------------------------------------------------------------------------

In addition to the above you may want to use a repository manager so that you can retain the builds you have been using. For information on this technique, see the [Guide to Testing Staged Releases](https://maven.apache.org/guides/development/guide-testing-releases.html).

[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html)
How do I make changes to the source and test development versions of the plugins?[](https://maven.apache.org/guides/development/guide-testing-development-plugins.html#how-do-i-make-changes-to-the-source-and-test-development-version)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For information on this, see the [Guide to Maven Development](https://maven.apache.org/guides/development/guide-maven-development.html).
