# Source: https://selenium.dev/documentation/webdriver/drivers/remote_webdriver/

Title: Remote WebDriver

URL Source: https://selenium.dev/documentation/webdriver/drivers/remote_webdriver/

Markdown Content:
About
Downloads
Documentation
Projects
Support
Blog
English
Search
Registrations Open for SeleniumConf 2026 | May 06–08 | Join Us In-Person! Register now!
Documentation
Overview
WebDriver
Getting Started
Drivers
Options
HTTP Client
Service
Remote WebDriver
Browsers
Waits
Elements
Interactions
Actions API
BiDi
Support Features
Troubleshooting
Selenium Manager
Grid
IE Driver Server
IDE
Test Practices
Legacy
About
 Edit this page
 Create documentation issue
 Create project issue
 Print entire section
Basic Example
Uploads
Downloads
Enable Downloads in the Grid
Enable Downloads in the Client
List Downloadable Files
Download a File
Delete Downloaded Files
Browser specific functionalities
Tracing client requests
Add the required dependencies
Add/pass the required system properties while running the client
Documentation
WebDriver
Drivers
Remote WebDriver
v4.0
Remote WebDriver

Selenium lets you automate browsers on remote computers if there is a Selenium Grid running on them. The computer that executes the code is referred to as the client computer, and the computer with the browser and driver is referred to as the remote computer or sometimes as an end-node. To direct Selenium tests to the remote computer, you need to use a Remote WebDriver class and pass the URL including the port of the grid on that machine. Please see the grid documentation for all the various ways the grid can be configured.

Basic Example

The driver needs to know where to send commands to and which browser to start on the Remote computer. So an address and an options instance are both required.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
    ChromeOptions options = getDefaultChromeOptions();
    driver = new RemoteWebDriver(gridUrl, options);
View Complete Code
View on GitHub
Uploads

Uploading a file is more complicated for Remote WebDriver sessions because the file you want to upload is likely on the computer executing the code, but the driver on the remote computer is looking for the provided path on its local file system. The solution is to use a Local File Detector. When one is set, Selenium will bundle the file, and send it to the remote machine, so the driver can see the reference to it. Some bindings include a basic local file detector by default, and all of them allow for a custom file detector.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
Java does not include a Local File Detector by default, so you must always add one to do uploads.
    ((RemoteWebDriver) driver).setFileDetector(new LocalFileDetector());
    WebElement fileInput = driver.findElement(By.cssSelector("input[type=file]"));
    fileInput.sendKeys(uploadFile.getAbsolutePath());
    driver.findElement(By.id("file-submit")).click();
View Complete Code
View on GitHub
Downloads

Chrome, Edge and Firefox each allow you to set the location of the download directory. When you do this on a remote computer, though, the location is on the remote computer’s local file system. Selenium allows you to enable downloads to get these files onto the client computer.

Enable Downloads in the Grid

Regardless of the client, when starting the grid in node or standalone mode, you must add the flag:

--enable-managed-downloads true

Enable Downloads in the Client

The grid uses the se:downloadsEnabled capability to toggle whether to be responsible for managing the browser location. Each of the bindings have a method in the options class to set this.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
    ChromeOptions options = getDefaultChromeOptions();
    options.setEnableDownloads(true);
    driver = new RemoteWebDriver(gridUrl, options);
View Complete Code
View on GitHub
List Downloadable Files

Be aware that Selenium is not waiting for files to finish downloading, so the list is an immediate snapshot of what file names are currently in the directory for the given session.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
    List<String> files = ((HasDownloads) driver).getDownloadableFiles();
View Complete Code
View on GitHub
Download a File

Selenium looks for the name of the provided file in the list and downloads it to the provided target directory.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
    ((HasDownloads) driver).downloadFile(downloadableFile, targetDirectory);
View Complete Code
View on GitHub
Delete Downloaded Files

By default, the download directory is deleted at the end of the applicable session, but you can also delete all files during the session.

Java
Python
CSharp
Ruby
JavaScript
Kotlin
    ((HasDownloads) driver).deleteDownloadableFiles();
View Complete Code
View on GitHub
Browser specific functionalities

Each browser has implemented special functionality that is available only to that browser. Each of the Selenium bindings has implemented a different way to use those features in a Remote Session

Java
Python
CSharp
Ruby
JavaScript
Kotlin

Java requires you to use the Augmenter class, which allows it to automatically pull in implementations for all interfaces that match the capabilities used with the RemoteWebDriver

    driver = new Augmenter().augment(driver);
View Complete Code
View on GitHub

Of interest, using the RemoteWebDriverBuilder automatically augments the driver, so it is a great way to get all the functionality by default:

        RemoteWebDriver.builder()
            .address(gridUrl)
            .oneOf(getDefaultChromeOptions())
            .setCapability("ext:options", Map.of("key", "value"))
            .config(ClientConfig.defaultConfig())
            .build();
View Complete Code
View on GitHub
Tracing client requests

This feature is only available for Java client binding (Beta onwards). The Remote WebDriver client sends requests to the Selenium Grid server, which passes them to the WebDriver. Tracing should be enabled at the server and client-side to trace the HTTP requests end-to-end. Both ends should have a trace exporter setup pointing to the visualization framework. By default, tracing is enabled for both client and server. To set up the visualization framework Jaeger UI and Selenium Grid 4, please refer to Tracing Setup for the desired version.

For client-side setup, follow the steps below.

Add the required dependencies

Installation of external libraries for tracing exporter can be done using Maven. Add the opentelemetry-exporter-jaeger and grpc-netty dependency in your project pom.xml:

  <dependency>
      <groupId>io.opentelemetry</groupId>
      <artifactId>opentelemetry-exporter-jaeger</artifactId>
      <version>1.0.0</version>
    </dependency>
    <dependency>
      <groupId>io.grpc</groupId>
      <artifactId>grpc-netty</artifactId>
      <version>1.35.0</version>
    </dependency>

Add/pass the required system properties while running the client
Java
System.setProperty("otel.traces.exporter", "jaeger");
System.setProperty("otel.exporter.jaeger.endpoint", "http://localhost:14250");
System.setProperty("otel.resource.attributes", "service.name=selenium-java-client");

ImmutableCapabilities capabilities = new ImmutableCapabilities("browserName", "chrome");

WebDriver driver = new RemoteWebDriver(new URL("http://www.example.com"), capabilities);

driver.get("http://www.google.com");

driver.quit();

  

Please refer to Tracing Setup for more information on external dependencies versions required for the desired Selenium version.

More information can be found at:

OpenTelemetry: https://opentelemetry.io
Configuring OpenTelemetry: https://github.com/open-telemetry/opentelemetry-java/tree/main/sdk-extensions/autoconfigure
Jaeger: https://www.jaegertracing.io
Selenium Grid Observability
Last modified July 29, 2025: Adding trailing / to retrieve code from GitHub (48b97e9bf82)
Development Partners
Selenium Level Sponsors
Support the Selenium Project

Learn more or view the full list of sponsors.

LEARN MORE 
© 2026 Software Freedom Conservancy All Rights Reserved

About Selenium
