# Source: https://maven.apache.org/install.html

Title: Installation – Maven

URL Source: https://maven.apache.org/install.html

Markdown Content:
[](https://maven.apache.org/install.html)
Apache Maven can be installed by most package managers, or manually by downloading the archive and adding it to your path.

[](https://maven.apache.org/install.html)
Prerequisites[](https://maven.apache.org/install.html#prerequisites)
--------------------------------------------------------------------

You need a Java Development Kit (JDK) installed. Either set the `JAVA_HOME` environment variable to the path of your JDK installation or have the `java` executable on your `PATH`.

The current stable version `3.9.14` requires JDK 8+, but any recent version will work just fine.

[](https://maven.apache.org/install.html)
Binary distribution[](https://maven.apache.org/install.html#binary-distribution)
--------------------------------------------------------------------------------

To install Apache Maven, extract the archive and add its bin directory to the `PATH`. This works on any operating system, but setting the path and environment variables depends on the OS.

Detailed steps are:

1. Download the Apache Maven [binary distribution archive](https://maven.apache.org/download.html).

2. Extract the distribution archive in any directory. Use `unzip apache-maven-3.9.14-bin.zip` or `tar xzvf apache-maven-3.9.14-bin.tar.gz` depending on the archive.

3. Add the `bin` directory of the created directory `apache-maven-3.9.14` to the `PATH` environment variable

4. Confirm with `mvn -v` in a new shell. The result should look similar to:

```
Apache Maven 3.9.14 (996c630dbc656c76214ce58821dcc58be960875b)
Maven home: /opt/apache-maven-3.9.14
Java version: 1.8.0_45, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.8.5", arch: "x86_64", family: "mac"
```

That’s it! Maven is now installed.

[](https://maven.apache.org/install.html)
macOS[](https://maven.apache.org/install.html#macos)
----------------------------------------------------

Installation on macOS is supported by [Homebrew](https://brew.sh/), [SDKMAN!](https://sdkman.io/) and [MacPorts](https://www.macports.org/).

[](https://maven.apache.org/install.html)

### Homebrew[](https://maven.apache.org/install.html#homebrew)

```
brew install maven
```

[](https://maven.apache.org/install.html)

### SDKMAN![](https://maven.apache.org/install.html#sdkman)

```
sdk install maven
```

[](https://maven.apache.org/install.html)

### MacPorts[](https://maven.apache.org/install.html#macports)

```
sudo port install maven3
```

[](https://maven.apache.org/install.html)
Linux[](https://maven.apache.org/install.html#linux)
----------------------------------------------------

The commands depend on the package manager of the Linux Distribution of your choice.

[](https://maven.apache.org/install.html)

### APT[](https://maven.apache.org/install.html#apt)

```
sudo apt install maven
```

[](https://maven.apache.org/install.html)

### DNF[](https://maven.apache.org/install.html#dnf)

```
sudo dnf install maven
```

[](https://maven.apache.org/install.html)

### YUM[](https://maven.apache.org/install.html#yum)

```
sudo yum install maven
```

[](https://maven.apache.org/install.html)
Windows[](https://maven.apache.org/install.html#windows)
--------------------------------------------------------

Installation on Windows is supported by [Chocolatey](https://chocolatey.org/) and [Scoop](https://scoop.sh/).

[](https://maven.apache.org/install.html)

### Chocolatey[](https://maven.apache.org/install.html#chocolatey)

```
choco install maven
```

[](https://maven.apache.org/install.html)

### Scoop[](https://maven.apache.org/install.html#scoop)

```
scoop install main/maven
```
