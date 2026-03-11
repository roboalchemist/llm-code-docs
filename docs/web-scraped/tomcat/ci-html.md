# Source: https://tomcat.apache.org/ci.html

Title: Apache Tomcat® - Continuous Integration

URL Source: https://tomcat.apache.org/ci.html

Markdown Content:
Apache Tomcat® project uses several [automated build services](https://ci.apache.org/) provided by Apache Software Foundation. In short, those are:

*   [Apache Gump](https://tomcat.apache.org/ci.html#Gump)
*   [Buildbot](https://tomcat.apache.org/ci.html#Buildbot)
*   [Jenkins](https://tomcat.apache.org/ci.html#Jenkins)

[Apache Gump](http://gump.apache.org/) is used to test integration of Tomcat with latest versions of libraries it depends on. [Buildbot](https://ci.apache.org/buildbot.html) and [Jenkins](https://builds.apache.org/) are used to perform the usual nighty builds. The Buildbot also builds and publishes documentation snapshots for the currently developed not yet released versions of Tomcat.

The following are links to snapshots of Apache Tomcat documentation, prepared and published by ASF Buildbot, using the latest source code.

*   [Tomcat 11.0.x](https://nightlies.apache.org/tomcat/tomcat-11.0.x/docs/index.html) (main)
*   [Tomcat 10.1.x](https://nightlies.apache.org/tomcat/tomcat-10.1.x/docs/index.html)
*   [Tomcat 9.0.x](https://nightlies.apache.org/tomcat/tomcat-9.0.x/docs/index.html)

There are the following Apache Maven repositories that provide binaries for not-yet-released versions of Apache Tomcat

*   [Snapshots](https://repository.apache.org/content/repositories/snapshots/) repository.

 These binaries are updated with that each CI build done at ASF Buildbot.

 Browse: [arg.apache.tomcat : tomcat](https://repository.apache.org/content/repositories/snapshots/org/apache/tomcat/tomcat/). 
*   [Staging](https://repository.apache.org/content/groups/staging/) repository.

 It hosts release candidates. Binaries are uploaded here when a release vote is being called.

 Browse: [arg.apache.tomcat : tomcat](https://repository.apache.org/content/groups/staging/org/apache/tomcat/tomcat/). 

#### Buildbot

The following are projects built by [ASF Buildbot](https://ci.apache.org/buildbot.html):

**tomcat-11.0.x***   Source path: `https://github.com/apache/tomcat/tree/main`
*   [Build status page](https://ci2.apache.org/#/builders/112) for **tomcat-11.0.x**

This builder is triggered after each commit. It does a release build and runs tests.
*   [Build status page](https://ci2.apache.org/#/builders/113) for **tomcat-11.0.x-periodic**

This builder is triggered once a day. It runs tests and generates a coverage report.
*   [Published files](https://nightlies.apache.org/tomcat/tomcat-11.0.x/): 
    *   [Documentation](https://nightlies.apache.org/tomcat/tomcat-11.0.x/docs/index.html)
    *   [JUnit logs](https://nightlies.apache.org/tomcat/tomcat-11.0.x/logs/) by build number. The recent ones are at the bottom.
    *   [Coverage report](https://nightlies.apache.org/tomcat/tomcat-11.0.x/coverage/)
    *   [RAT report](https://nightlies.apache.org/tomcat/tomcat-11.0.x/rat-output.html)
**tomcat-10.1.x***   Source path: `https://github.com/apache/tomcat`
*   [Build status page](https://ci2.apache.org/#/builders/44) for **tomcat-10.1.x**

This builder is triggered after each commit. It does a release build and runs tests.
*   [Build status page](https://ci2.apache.org/#/builders/38) for **tomcat-10.1.x-periodic**

This builder is triggered once a day. It runs tests and generates a coverage report.
*   [Published files](https://nightlies.apache.org/tomcat/tomcat-10.1.x/): 
    *   [Documentation](https://nightlies.apache.org/tomcat/tomcat-10.1.x/docs/index.html)
    *   [JUnit logs](https://nightlies.apache.org/tomcat/tomcat-10.1.x/logs/) by build number. The recent ones are at the bottom.
    *   [Coverage report](https://nightlies.apache.org/tomcat/tomcat-10.1.x/coverage/)
    *   [RAT report](https://nightlies.apache.org/tomcat/tomcat-10.1.x/rat-output.html)
**tomcat-9.0.x***   Source path: `https://github.com/apache/tomcat/tree/9.0.x`
*   [Build status page](https://ci2.apache.org/#/builders/37) for **tomcat-9.0.x**

This builder is triggered after each commit. It does a release build and runs tests.
*   [Build status page](https://ci2.apache.org/#/builders/42) for **tomcat-9.0.x-periodic**

This builder is triggered once a day. It runs tests and generates a coverage report.
*   [Published files](https://nightlies.apache.org/tomcat/tomcat-9.0.x/): 
    *   [Documentation](https://nightlies.apache.org/tomcat/tomcat-9.0.x/docs/index.html)
    *   [JUnit logs](https://nightlies.apache.org/tomcat/tomcat-9.0.x/logs/) by build number. The recent ones are at the bottom.
    *   [Coverage report](https://nightlies.apache.org/tomcat/tomcat-9.0.x/coverage/)
    *   [RAT report](https://nightlies.apache.org/tomcat/tomcat-9.0.x/rat-output.html)

#### Gump

The following are projects built by [Apache Gump](http://gump.apache.org/):

| Module | Links |
| --- | --- |
| [tomcat-main](http://vmgump.apache.org/tomcat-main/) Tomcat 11.0.x | * Source path: `https://github.com/apache/tomcat` * **Projects:** * [tomcat-main](http://vmgump.apache.org/tomcat-main/tomcat-main/) * [tomcat-main-test-nio](http://vmgump.apache.org/tomcat-main/tomcat-main-test-nio/) * [tomcat-main-test-nio2](http://vmgump.apache.org/tomcat-main/tomcat-main-test-nio2/) * [tomcat-main-validate](http://vmgump.apache.org/tomcat-main/tomcat-main-validate/) * [tomcat-main-validate-eoln](http://vmgump.apache.org/tomcat-main/tomcat-main-validate-eoln/) * [TestServerInfo](http://vmgump.apache.org/tomcat-main/tomcat-main-test-nio/gump_file/TEST-org.apache.catalina.util.TestServerInfo.NIO.txt.html) result |
| [tomcat-10.1.x](http://vmgump.apache.org/tomcat-10.1.x/) Tomcat 10.1.x | * Source path: `https://github.com/apache/tomcat` * **Projects:** * [tomcat-10.1.x](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x/) * [tomcat-10.1.x-test-nio](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x-test-nio/) * [tomcat-10.1.x-test-nio2](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x-test-nio2/) * [tomcat-10.1.x-validate](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x-validate/) * [tomcat-10.1.x-validate-eoln](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x-validate-eoln/) * [TestServerInfo](http://vmgump.apache.org/tomcat-10.1.x/tomcat-10.1.x-test-nio/gump_file/TEST-org.apache.catalina.util.TestServerInfo.NIO.txt.html) result |
| [tomcat-9.0.x](http://vmgump.apache.org/tomcat-9.0.x/) Tomcat 9.0.x | * Source path: `https://github.com/apache/tomcat/tree/9.0.x` * **Projects:** * [tomcat-9.0.x](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x/) * [tomcat-tc9.0.x-test-apr](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-test-apr/) (with Tomcat Native 1.2.x and OpenSSL 1.1.1[x]) * [tomcat-tc9.0.x-test-nio](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-test-nio/) * [tomcat-tc9.0.x-test-nio2](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-test-nio2/) * [tomcat-tc9.0.x-validate](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-validate/) * [tomcat-tc9.0.x-validate-eoln](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-validate-eoln/) * [TestServerInfo](http://vmgump.apache.org/tomcat-tc9.0.x/tomcat-tc9.0.x-test-nio/gump_file/TEST-org.apache.catalina.util.TestServerInfo.NIO.txt.html) result |
| [tomcat-native-trunk](http://vmgump.apache.org/tomcat-native-trunk/) Tomcat Native 1.2.x uses: OpenSSL master APR 1.6.x | * Source path: `https://github.com/apache/tomcat-native` * **Projects:** * [tomcat-native-trunk-buildconf](http://vmgump.apache.org/tomcat-native-trunk/tomcat-native-trunk-buildconf/) * [tomcat-native-trunk-configure](http://vmgump.apache.org/tomcat-native-trunk/tomcat-native-trunk-configure/) * [tomcat-native-trunk-make](http://vmgump.apache.org/tomcat-native-trunk/tomcat-native-trunk-make/) - performs the actual build * [tomcat-native-trunk-make-install](http://vmgump.apache.org/tomcat-native-trunk/tomcat-native-trunk-make-install/) |
| [tomcat-native-1.2-3.0.x](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/) Tomcat Native 1.2.x uses: OpenSSL 3.0.x[x] APR 1.6.x | * Source path: `https://github.com/apache/tomcat-native` * **Projects:** * [tomcat-native-1.2-3.0.x-buildconf](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/tomcat-native-1.2-3.0.x-buildconf/) * [tomcat-native-1.2-3.0.x-configure](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/tomcat-native-1.2-3.0.x-configure/) * [tomcat-native-1.2-3.0.x-make](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/tomcat-native-1.2-3.0.x-make/) - performs the actual build * [tomcat-native-1.2-3.0.x-make-install](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/tomcat-native-1.2-3.0.x-make-install/) |
| [tomcat-native-1.2-3.0.x](http://vmgump.apache.org/tomcat-native-1.2-3.0.x/) Tomcat Native 1.2.x uses: OpenSSL 3.0.x[x] APR 1.6.x | * Source path: `https://github.com/apache/tomcat-native` * **Projects:** * [tomcat-native-1.2-1.1.1-buildconf](http://vmgump.apache.org/tomcat-native-1.2-1.1.1/tomcat-native-1.2-1.1.1-buildconf/) * [tomcat-native-1.2-1.1.1-configure](http://vmgump.apache.org/tomcat-native-1.2-1.1.1/tomcat-native-1.2-1.1.1-configure/) * [tomcat-native-1.2-1.1.1-make](http://vmgump.apache.org/tomcat-native-1.2-1.1.1/tomcat-native-1.2-1.1.1-make/) - performs the actual build * [tomcat-native-1.2-1.1.1-make-install](http://vmgump.apache.org/tomcat-native-1.2-1.1.1/tomcat-native-1.2-1.1.1-make-install/) |
| [tomcat-connectors-native](http://vmgump.apache.org/tomcat-connectors-native/) Tomcat Connectors (mod_jk) uses: Apache HTTP Server trunk | * Source path: `https://github.com/apache/tomcat-connectors` * **Projects:** * [tomcat-connectors-native](http://vmgump.apache.org/tomcat-connectors-native/tomcat-connectors-native/) * [tomcat-jk-native-buildconf](http://vmgump.apache.org/tomcat-connectors-native/tomcat-jk-native-buildconf/) * [tomcat-jk-native-configure](http://vmgump.apache.org/tomcat-connectors-native/tomcat-jk-native-configure/) * [tomcat-jk-native](http://vmgump.apache.org/tomcat-connectors-native/tomcat-jk-native/) - performs the actual build |
| [tomcat-taglibs](http://vmgump.apache.org/tomcat-taglibs/) Standard Taglib (JSTL 1.2) | * Source path: `/tomcat/taglibs/trunks` * **Projects:** * [taglibs-parent](http://vmgump.apache.org/tomcat-taglibs/taglibs-parent/) * [taglibs-standard-spec](http://vmgump.apache.org/tomcat-taglibs/taglibs-standard-spec/) |
