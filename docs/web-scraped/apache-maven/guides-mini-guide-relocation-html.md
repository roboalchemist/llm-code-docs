# Source: https://maven.apache.org/guides/mini/guide-relocation.html

Title: Guide to relocation – Maven

URL Source: https://maven.apache.org/guides/mini/guide-relocation.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-relocation.html)
Sometimes it is necessary to relocate artifacts in the repository. One example of that is when a project moves from one groupId to a different groupId.

Making changes to the repository can have far reaching consequences. So it is best to get it right the first time, hence this guide.

**2020 rework in progress**, see [discussion on dev mailing list](https://lists.apache.org/thread.html/r5e940260cfe5234f540c20fdb7bb7dacbb63b911a4b902c75f4f0cd2%40%3Cdev.maven.apache.org%3E), still need analysis of issues, definition of improvements, and of course implementation…

[](https://maven.apache.org/guides/mini/guide-relocation.html)
How to relocate a Maven 2 artifact to a different groupId[](https://maven.apache.org/guides/mini/guide-relocation.html#how-to-relocate-a-maven-2-artifact-to-a-different-groupid)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The goal of the example below is for the `foo` project to relocate its groupId from `bar` to `org.bar`.

[](https://maven.apache.org/guides/mini/guide-relocation.html)
### Working on past versions[](https://maven.apache.org/guides/mini/guide-relocation.html#working-on-past-versions)

1.   Copy all `foo`-related files from `/bar/foo/` in your Maven 2 repository to a temporary location.

2.   Change the groupId to `org.bar` in all `foo`-related POM files in the temporary location.

3.   Copy all files from the temporary location to `/org/bar/foo/` in your Maven 2 repository.

4.   Create a minimal Maven 2 POM file for every old release of `foo` in your Maven 2 repository. The POM files only need to include `groupId`, `artifactId`, `version` and the relocation section.

**Note:** Before you replace your old POM files in `/bar/foo/` with these minimal POM files, make sure you have made backups!

The minimal POM file might look like this for version 1.0 of `foo`:

    1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
    2.   `<modelVersion>4.0.0</modelVersion>`
    3.   `<groupId>bar</groupId>`
    4.   `<artifactId>foo</artifactId>`
    5.   `<version>1.0</version>`
    6.   `<distributionManagement>`
    7.   `<relocation>`
    8.   `<groupId>org.bar</groupId>`
    9.   `</relocation>`
    10.   `</distributionManagement>`
    11.   `</project>`

In this case we are relocating because the groupId has changed. We only need to add the element that has changed to the `relocation` element. For information on which elements are allowed in the `relocation` element, see [the POM reference](https://maven.apache.org/ref/current/maven-model/maven.html#class_relocation).

5.   If your project uses MD5 or SHA1 checksums you must now create new checksums for the pom files in `/bar/foo/` in your Maven 2 repository. If the POM file needs to be signed, do that as well.

6.   If your project syncs with Central, you should now initiate that sync. This might happen automatically depending on your projects sync policy.

Your `foo`-artifacts are now available to Maven users with both the old and the new groupId. Projects using the old groupId will automatically be redirected to the new groupId and a warning telling the user to update their dependencies will be issued.

[](https://maven.apache.org/guides/mini/guide-relocation.html)
### Releasing the next version[](https://maven.apache.org/guides/mini/guide-relocation.html#releasing-the-next-version)

When the next release of `foo` is made, you should publish two Maven 2 POM files: first you should publish `foo`'s POM with the new groupId `org.bar`.

Because data in the repository is not supposed to change, Maven doesn't download POM files that it has already downloaded. Therefore you will also need to publish a relocation POM file with the old groupId `bar` for the new version: this should be a minimal relocation POM (as described in step 4 above), but for the new version of `foo`.

For the release after that, you only need to publish a Maven POM with a groupId of `org.bar`, since users of the previous version have been informed of the changed groupId.

[](https://maven.apache.org/guides/mini/guide-relocation.html)
Examples[](https://maven.apache.org/guides/mini/guide-relocation.html#examples)
-------------------------------------------------------------------------------

[](https://maven.apache.org/guides/mini/guide-relocation.html)
### Apache Ant[](https://maven.apache.org/guides/mini/guide-relocation.html#apache-ant)

1.   has published its releases until 1.6.5 to Maven 1-compliant `ant:ant` coordinates (see [repository content](https://repo.maven.apache.org/maven2/ant/ant/)),
2.   starting with 1.7.0, moved to reverse-DNS compliant Maven 2+ `org.apache.ant:ant` coordinates, (see [repository content](https://repo.maven.apache.org/maven2/org/apache/ant/ant/)),
3.   published one `ant:ant:1.7.0` relocation POM in old groupId to advertise about the move (see [repository content](https://repo.maven.apache.org/maven2/ant/ant/1.7.0/)).

Notice that past `ant:ant` versions POMs (until 1.6.5) have not been modified to advertise about the move: Central POM content is not expected to be changed once published (because initial content has been downloaded many times and is not expected to be re-loaded later).

[](https://maven.apache.org/guides/mini/guide-relocation.html)
### Apache POI[](https://maven.apache.org/guides/mini/guide-relocation.html#apache-poi)

1.   has published its releases until 3.0-alpha-3 to Maven 1-compliant `poi:poi` coordinates (see [repository content](https://repo.maven.apache.org/maven2/poi/poi/)),
2.   starting with 3.0-FINAL, moved to reverse-DNS compliant Maven 2+ `org.apache.poi:poi` coordinates, (see [repository content](https://repo.maven.apache.org/maven2/org/apache/poi/poi/)),
3.   published `poi:poi:3.0-FINAL` relocation POM **with jars** in old groupId to advertise about the move (see [repository content](https://repo.maven.apache.org/maven2/poi/poi/3.0-FINAL/)).
4.   published `poi:poi` relocation POMs for 3.0.1-FINAL, 3.0.2-beta1/beta2/FINAL and 3.1-beta1/beta2/FINAL in old groupId to advertise about the move (see [repository content](https://repo.maven.apache.org/maven2/poi/poi/)).

[](https://maven.apache.org/guides/mini/guide-relocation.html)
### Testing[](https://maven.apache.org/guides/mini/guide-relocation.html#testing)

Using `pom.xml`

1.   `<?xml version="1.0" encoding="UTF-8"?>`
2.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">`
3.   `<modelVersion>4.0.0</modelVersion>`

5.   `<groupId>test</groupId>`
6.   `<artifactId>relocation-test</artifactId>`
7.   `<version>1.0-SNAPSHOT</version>`

9.   `<dependencies>`
10.   `<dependency>`
11.   `<groupId>ant</groupId>`
12.   `<artifactId>ant</artifactId>`
13.   `<version>1.7.0</version><!-- https://repo.maven.apache.org/maven2/ant/ant/1.7.0/ -->`
14.   `</dependency>`
15.   `<dependency>`
16.   `<groupId>poi</groupId>`
17.   `<artifactId>poi</artifactId>`
18.   `<version>3.0-FINAL</version><!-- https://repo.maven.apache.org/maven2/poi/poi/3.0-FINAL/ -->`
19.   `</dependency>`
20.   `</dependencies>`
21.   `</project>`

Dependency resolution of these relocated artifacts follows to the new relocated coordinates, issuing a warning:

```
$ mvn dependency:list dependency:tree
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------< test:relocation-test >------------------------
[INFO] Building relocation-test 1.0-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[WARNING] The artifact ant:ant:jar:1.7.0 has been relocated to org.apache.ant:ant:jar:1.7.0
[WARNING] The artifact poi:poi:jar:3.0-FINAL has been relocated to org.apache.poi:poi:jar:3.0-FINAL
[INFO]
[INFO] --- dependency:3.6.0:list (default-cli) @ relocation-test ---
[INFO]
[INFO] The following files have been resolved:
[INFO]    org.apache.ant:ant:jar:1.7.0:compile -- module ant (auto)
[INFO]    org.apache.ant:ant-launcher:jar:1.7.0:compile -- module ant.launcher (auto)
[INFO]    org.apache.poi:poi:jar:3.0-FINAL:compile -- module poi (auto)
[INFO]    commons-logging:commons-logging:jar:1.1:compile -- module commons.logging (auto)
[INFO]    log4j:log4j:jar:1.2.13:compile -- module log4j (auto)
[INFO]
[INFO]
[INFO] --- dependency:3.6.0:tree (default-cli) @ relocation-test ---
[WARNING] The artifact ant:ant:jar:1.7.0 has been relocated to org.apache.ant:ant:jar:1.7.0
[WARNING] The artifact poi:poi:jar:3.0-FINAL has been relocated to org.apache.poi:poi:jar:3.0-FINAL
[INFO] test:relocation-test:jar:1.0-SNAPSHOT
[INFO] +- org.apache.ant:ant:jar:1.7.0:compile
[INFO] |  \- org.apache.ant:ant-launcher:jar:1.7.0:compile
[INFO] \- org.apache.poi:poi:jar:3.0-FINAL:compile
[INFO]    +- commons-logging:commons-logging:jar:1.1:compile
[INFO]    \- log4j:log4j:jar:1.2.13:compile
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
```
