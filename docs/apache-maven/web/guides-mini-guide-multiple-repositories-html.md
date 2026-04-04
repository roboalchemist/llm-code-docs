# Source: https://maven.apache.org/guides/mini/guide-multiple-repositories.html

Title: Setting up Multiple Repositories – Maven

URL Source: https://maven.apache.org/guides/mini/guide-multiple-repositories.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)
There are two different ways that you can specify the use of multiple repositories. The first way is to specify in a POM which repositories you want to use. That is supported both inside and outside of build profiles:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<repositories>`
4.   `<repository>`
5.   `<id>my-repo1</id>`
6.   `<name>your custom repo</name>`
7.   `<url>http://jarsm2.dyndns.dk</url>`
8.   `</repository>`
9.   `<repository>`
10.   `<id>my-repo2</id>`
11.   `<name>your custom repo</name>`
12.   `<url>http://jarsm2.dyndns.dk</url>`
13.   `</repository>`
14.   `</repositories>`
15.   `...`
16.   `</project>`

**NOTE:** You will also get the standard set of repositories as defined in the [Super POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html#Super_POM).

The other way you can specify multiple repositories is by creating a profile in the `${user.home}/.m2/settings.xml` or `${maven.home}/conf/settings.xml` file like the following:

1.   `<settings>`
2.   `...`
3.   `<profiles>`
4.   `...`
5.   `<profile>`
6.   `<id>myprofile</id>`
7.   `<repositories>`
8.   `<repository>`
9.   `<id>my-repo2</id>`
10.   `<name>your custom repo</name>`
11.   `<url>http://jarsm2.dyndns.dk</url>`
12.   `</repository>`
13.   `</repositories>`
14.   `</profile>`
15.   `...`
16.   `</profiles>`

18.   `<activeProfiles>`
19.   `<activeProfile>myprofile</activeProfile>`
20.   `</activeProfiles>`
21.   `...`
22.   `</settings>`

If you specify repositories in profiles you must remember to activate that particular profile! As you can see above we do this by registering a profile to be active in the `activeProfiles` element.

You could also activate this profile on the command like by executing the following command:

```
mvn -Pmyprofile ...
```

In fact the `-P` option will take a CSV list of profiles to activate if you wish to activate multiple profiles simultaneously.

**Note**: The settings descriptor documentation can be found on the [Maven Local Settings Model Website](https://maven.apache.org/maven-settings/settings.html).

[](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)
Repository Order[](https://maven.apache.org/guides/mini/guide-multiple-repositories.html#repository-order)
----------------------------------------------------------------------------------------------------------

Remote repository URLs are queried in the following order for artifacts until one returns a valid result:

1.   effective settings: 
    1.   Global `settings.xml`
    2.   User `settings.xml`

2.   local effective build POM: 
    1.   Local `pom.xml`
    2.   Parent POMs, recursively
    3.   Super POM

3.   effective POMs from dependency path to the artifact.

For each of these locations, the repositories within the profiles are queried first in the order outlined at [Introduction to build profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html).

Before downloading from a repository, [mirrors configuration](https://maven.apache.org/guides/mini/guide-mirror-settings.html) is applied.

Effective settings and local build POM, with profile taken into account, can easily be reviewed to see their repositories order with `mvn help:effective-settings` and `mvn help:effective-pom -Dverbose`.

[](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)
Repository IDs[](https://maven.apache.org/guides/mini/guide-multiple-repositories.html#repository-ids)
------------------------------------------------------------------------------------------------------

Each repository must have a **unique ID**. Clashing repository IDs within either effective settings or effective POMs lead to build failures. However, repositories from POM get overwritten by repositories with the same ID from effective settings. Repository IDs are also used in the [local repository metadata](https://maven.apache.org/ref/3-LATEST/maven-repository-metadata/).
