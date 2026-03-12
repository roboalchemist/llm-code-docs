# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/get-started-with-the-pentaho-reporting-sdk.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/get-started-with-the-pentaho-reporting-sdk.md

# Get started with the Pentaho Reporting SDK

You can download the latest Pentaho Reporting software development kit (SDK) from the [Support Portal](https://support.pentaho.com).

Download the `pre-classic-sdk-10.2.0.0-xxx` file and unpack the Pentaho Reporting SDK archive to a convenient and accessible location. If you use the Eclipse or IntelliJ IDEA development environments, this directory will also serve as your workspace.

In an effort to reduce the size of the SDK, the source code of its constituent libraries is not included. If you need to see the source to any of the software distributed with the Pentaho Reporting SDK, see [Source Code Links](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/advanced-topics/source-code-links) for instructions.

## Use the included Eclipse project

If you use the Eclipse or IntelliJ IDEA development environments, you can use the Eclipse project included with the Pentaho Reporting SDK to work directly with the example source code. Simply select the unpacked Pentaho Reporting SDK directory as your workspace.

You can also launch the `Sample1.java` and `Sample2.java` example applications directly from the file browser in Eclipse.

## SDK directory structure

The following elements are delivered in the SDK directory structure:

```
/
/documentation
/licenses
/samples
/WebContent
/../META-INF
/../WEB-INF
/../../lib
/lib
/source
/../org
/../../pentaho
/../../../reporting
/../../../../engine
/../../../../../classic
/../../../../../../samples
/sql
```

| Directory            | Content Description                                                           |
| -------------------- | ----------------------------------------------------------------------------- |
| `Documentation`      | Where the "Embedding the Pentaho Reporting engine" PDF is located             |
| `Licenses`           | Contains text files with licensing information                                |
| `Samples`            | The eclipse project directory, which contains the samples shown in this guide |
| `Samples/WebContent` | WebContent information used with Sample 4 (mainly the `WEB-INF/web.xml`)      |
| `Samples/lib`        | The lib directory which makes up thePentaho Reporting engine SDK              |
| `Samples/source`     | The source files used to make up the four reporting samples                   |
| `Samples/sql`        | The file-based HSQLDB instance used with the samples                          |

## Content of the samples directory

The following files appear in the `Samples` directory:

| File               | Purpose                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| `build.properties` | Ant properties used with the build script                                |
| `build.xml`        | Ant build script                                                         |
| `common_build.xml` | Ant Build Script                                                         |
| `ivysettings.xml`  | Settings for Ivy (used with build)                                       |
| `ivy.xml`          | Dependencies for project (used with Ivy – used with build)               |
| `.project`         | Eclipse project file                                                     |
| `.classpath`       | Eclipse classpath file                                                   |
| `samples.iml`      | IntelliJ project file                                                    |
| `Sample*.bat`      | Runs the sample (1/2/3) program on Windows                               |
| `Sample *.launch`  | Runs the sample (1/2/3) program from within Eclipse                      |
| `Sample*.sh`       | Runs the sample (1/2/3) project on linux                                 |
| `Sample4.war`      | The WAR that can be dropped in a Servlet Container (Tomcat) and executed |
