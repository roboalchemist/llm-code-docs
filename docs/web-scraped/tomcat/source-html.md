# Source: https://tomcat.apache.org/source.html

Title: Apache Tomcat® - Repository Access

URL Source: https://tomcat.apache.org/source.html

Markdown Content:
### Table of Contents

*   [Version Control](https://tomcat.apache.org/source.html#Version_Control)
*   [Git](https://tomcat.apache.org/source.html#Git)
*   [tomcat.git](https://tomcat.apache.org/source.html#tomcat.git)
*   [tomcat-connectors.git](https://tomcat.apache.org/source.html#tomcat-connectors.git)
*   [tomcat-native.git](https://tomcat.apache.org/source.html#tomcat-native.git)
*   [tomcat-training.git](https://tomcat.apache.org/source.html#tomcat-training.git)
*   [tomcat-taglibs-parent.git](https://tomcat.apache.org/source.html#tomcat-taglibs-parent.git)
*   [tomcat-taglibs-standard.git](https://tomcat.apache.org/source.html#tomcat-taglibs-standard.git)
*   [tomcat-taglibs-rdc.git](https://tomcat.apache.org/source.html#tomcat-taglibs-rdc.git)
*   [tomcat-taglibs-site.git](https://tomcat.apache.org/source.html#tomcat-taglibs-site.git)
*   [tomcat-maven-plugin.git](https://tomcat.apache.org/source.html#tomcat-maven-plugin.git)
*   [Subversion Repository](https://tomcat.apache.org/source.html#Subversion_Repository)
    1.   [Line endings](https://tomcat.apache.org/source.html#Line_endings)

### Version Control

The Apache Tomcat® project is in the process of migrating from Subversion to Git for version control. The following components use Git:

*   Apache Tomcat 11.0.x
*   Apache Tomcat 10.1.x
*   Apache Tomcat 9.0.x
*   Apache Tomcat 8.5.x
*   Apache Tomcat Connectors
*   Apache Tomcat Native
*   Apache Tomcat Training
*   Apache Tomcat migration tool for Jakarta EE
*   Taglibs
*   Tomcat Maven plugin

The following components currently use Subversion as the primary version control system:

*   Tomcat web site
*   archive

### Git

The ASF operates a dual primary system for repositories that use Git as their primary version control system. This means committers may commit to either gitbox.apache.org or GitHub.

For repositories that are mirrored to Git from Subversion, the mirrors may be found at git.apache.org or GitHub and are read-only for everyone.

### tomcat.git

This is the Git repository that contains the Apache Tomcat source code. There are currently four branches:

*   main
*   10.1.x
*   9.0.x
*   8.5.x

main is the primary development branch. Apache Tomcat 11.0.x releases are tagged from this branch. Development work generally occurs in this branch first.

10.1.x is the stable release branch for Apache Tomcat 10.1.x. Generally, fixes are cherry picked from main into this branch.

9.0.x is the stable release branch for Apache Tomcat 9.0.x. Generally, fixes are cherry picked from 10.0.x into this branch.

8.5.x is the stable release branch for Apache Tomcat 8.5.x. Generally, fixes are cherry picked from 9.0.x into this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat).

### tomcat-connectors.git

This is the Git repository that contains the Apache Tomcat Connectors source code. This includes mod_jk and isapi. There is currently one active branch:

*   main

main is the primary development branch. Apache Tomcat Connectors 1.2.x releases are tagged from this branch. Development work generally occurs in this branch first.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-connectors).

### tomcat-native.git

This is the Git repository that contains the Apache Tomcat Native source code. There is currently one active branch:

*   main

main is the primary development branch. Apache Tomcat Native 1.2.x releases are tagged from this branch. Development work generally occurs in this branch first.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-native).

### tomcat-training.git

This is the Git repository that contains the Apache Tomcat training material source code. There is currently one active branch:

*   main

main is the primary development branch. Apache Tomcat training courses are tagged from this branch. Development work generally occurs in this branch first.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-training).

### tomcat-taglibs-parent.git

This is the Git repository that contains the parent POM for the Apache Tomcat Tag Libraries. There is currently one active branch:

*   main

main is the only development branch. All development work occurs in this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-taglibs-parent).

### tomcat-taglibs-standard.git

This is the Git repository that contains the Apache Tomcat Standard Tag Library. There is currently one active branch:

*   main

main is the only development branch. All development work occurs in this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-taglibs-standard).

### tomcat-taglibs-rdc.git

This is the Git repository that contains the Apache Tomcat RDC Tag Library. There is currently one active branch:

*   main

main is the only development branch. All development work occurs in this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-taglibs-rdc).

### tomcat-taglibs-site.git

This is the Git repository that contains the web site for the Apache Tomcat Tag Libraries. There is currently one active branch:

*   main

main is the only development branch. All development work occurs in this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-taglibs-site).

### tomcat-maven-plugin.git

This is the The Apache Tomcat Maven Plugin source code and web site. Libraries. There are currently one active branch:

*   trunk

trunk is the only development branch. All development work occurs in this branch.

A web based view of this repository is available via [GitHub](https://github.com/apache/tomcat-maven-plugin).

### Subversion Repository

The root of the repository is [http://svn.apache.org/repos/asf/tomcat](http://svn.apache.org/repos/asf/tomcat).

_Note:_ there is also ViewVC-powered [web view of the repository](http://svn.apache.org/viewvc/tomcat/).

The directories below this level are:

| Directory | Contents |
| --- | --- |
| [`/archive/`](http://svn.apache.org/repos/asf/tomcat/archive) | Modules that are no longer maintained or have been moved to git |
| [`/sandbox/`](http://svn.apache.org/repos/asf/tomcat/sandbox) | An area where Tomcat committers can experiment with new ideas. |
| [`/site/`](http://svn.apache.org/repos/asf/tomcat/site) | The Apache Tomcat website. |

#### Line endings

The repositories are configured so that when you check out from svn, you get the line ending appropriate for your platform for all files. The thinking behind this is that, for example, if you need to fix a typo in a .bat file from MacOS, it is easier if the .bat file has MacOS line-endings.

When you build locally, line-endings are not changed. The expectation is that the source has the correct line-endings for your platform so all the files that matter on your platform will have the correct line endings. When you are on Windows it doesn't matter if the .sh files have Windows line-endings since you'll never use them on Windows.
