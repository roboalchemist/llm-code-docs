# Source: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/

Title: Java | Quickstarts | PDF Extract API

URL Source: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/

Published Time: Wed, 11 Mar 2026 12:09:56 GMT

Markdown Content:
To get started using Adobe PDF Extract API, let's walk through a simple scenario - taking an input PDF document and running PDF Extract API against it. Once the PDF has been extracted, we'll parse the results and report on any major headers in the document. In this guide, we will walk you through the complete process for creating a program that will accomplish this task.

Prerequisites[](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/#prerequisites)
----------------------------------------------------------------------------------------------------------------------------------------

* * *

To complete this guide, you will need:

* [Java](http://www.oracle.com/technetwork/java/javase/downloads/index.html) - Java 11 or higher is required.
* [Maven](https://maven.apache.org/install.html)
* An Adobe ID. If you do not have one, the credential setup will walk you through creating one.
* A way to edit code. No specific editor is required for this guide.

Step One: Getting credentials[](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/#step-one-getting-credentials)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

1) To begin, open your browser to [https://acrobatservices.adobe.com/dc-integration-creation-app-cdn/main.html?api=pdf-extract-api](https://acrobatservices.adobe.com/dc-integration-creation-app-cdn/main.html?api=pdf-extract-api). If you are not already logged in to Adobe.com, you will need to sign in or create a new user. Using a personal email account is recommend and not a federated ID.

![Image 1: Sign in](https://developer.adobe.com/document-services/docs/static/3b0d32040b6b20e4343cb27657c7b00a/e9985/shot1.png)

1) After registering or logging in, you will then be asked to name your new credentials. Use the name, "New Project".

2) Change the "Choose language" setting to "Java".

3) Also note the checkbox by, "Create personalized code sample." This will include a large set of samples along with your credentials. These can be helpful for learning more later.

4) Click the checkbox saying you agree to the developer terms and then click "Create credentials."

![Image 2: Project setup](https://developer.adobe.com/document-services/docs/static/01c7555e7e8ab8a127b405119d784603/bbbf7/shot2_spc.png)

1) After your credentials are created, they are automatically downloaded:

![Image 3: alt](https://developer.adobe.com/document-services/docs/static/cc29d100498a1a222eeb2f85faf651ff/bbbf7/shot3_spc.png)

Step Two: Setting up the project[](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/#step-two-setting-up-the-project)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

1) In your Downloads folder, find the ZIP file with your credentials: PDFServicesSDK-JavaSamples.zip. If you unzip that archive, you will find a folder of samples and the `pdfservices-api-credentials.json` file.

![Image 4: alt](https://developer.adobe.com/document-services/docs/static/ab2017d1b9d12b9ba06277b11d5f9f0b/80d88/shot5_spc.png)

1) Take the `pdfservices-api-credentials.json` file and place it in a new directory.

2) In this directory, create a new file named `pom.xml` and copy the following content:

Copied to your clipboard

<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

<modelVersion>4.0.0</modelVersion>

<groupId>com.adobe.documentservices</groupId>

<artifactId>pdfservices-sdk-extract-guide</artifactId>

<version>1</version>

<name>PDF Services Java SDK Samples</name>

<properties>

<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>

<maven.compiler.source>11</maven.compiler.source>

<maven.compiler.target>11</maven.compiler.target>

<pdfservices.sdk.version>4.3.0</pdfservices.sdk.version>

</properties>

<dependencies>

<dependency>

<groupId>com.adobe.documentservices</groupId>

<artifactId>pdfservices-sdk</artifactId>

<version>${pdfservices.sdk.version}</version>

</dependency>

<dependency>

<groupId>org.apache.logging.log4j</groupId>

<artifactId>log4j-slf4j-impl</artifactId>

<version>2.21.1</version>

</dependency>

</dependencies>

<build>

<plugins>

<plugin>

<groupId>org.apache.maven.plugins</groupId>

<artifactId>maven-compiler-plugin</artifactId>

<version>3.8.0</version>

<configuration>

<source>${maven.compiler.source}</source>

<target>${maven.compiler.target}</target>

</configuration>

</plugin>

<plugin>

<groupId>org.codehaus.mojo</groupId>

<artifactId>exec-maven-plugin</artifactId>

<version>1.5.0</version>

<executions>

<execution>

<goals>

<goal>java</goal>

</goals>

</execution>

</executions>

</plugin>

</plugins>

</build>

</project>

This file will define what dependencies we need and how the application will be built.

Our application will take a PDF, `Adobe Extract API Sample.pdf` (downloadable from [here](https://developer.adobe.com/document-services/docs/Adobe%20Extract%20API%20Sample.pdf)) and extract it's contents. The results will be saved as a ZIP file, `ExtractTextInfoFromPDF.zip`. We will then parse the results from the ZIP and print out the text of any `H1` headers found in the PDF.

1) In your editor, open the directory where you previously copied the credentials, and create a new directory, `src/main/java`. In that directory, create `ExtractTextInfoFromPDF.java`.

Now you're ready to begin coding.

Step Three: Creating the application[](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/#step-three-creating-the-application)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* * *

1) We'll begin by including our required dependencies:

Copied to your clipboard

import com.adobe.pdfservices.operation.PDFServices;

import com.adobe.pdfservices.operation.PDFServicesMediaType;

import com.adobe.pdfservices.operation.PDFServicesResponse;

import com.adobe.pdfservices.operation.auth.Credentials;

import com.adobe.pdfservices.operation.auth.ServicePrincipalCredentials;

import com.adobe.pdfservices.operation.exception.SDKException;

import com.adobe.pdfservices.operation.exception.ServiceApiException;

import com.adobe.pdfservices.operation.exception.ServiceUsageException;

import com.adobe.pdfservices.operation.io.Asset;

import com.adobe.pdfservices.operation.io.StreamAsset;

import com.adobe.pdfservices.operation.pdfjobs.jobs.ExtractPDFJob;

import com.adobe.pdfservices.operation.pdfjobs.params.extractpdf.ExtractElementType;

import com.adobe.pdfservices.operation.pdfjobs.params.extractpdf.ExtractPDFParams;

import com.adobe.pdfservices.operation.pdfjobs.result.ExtractPDFResult;

import org.apache.commons.io.IOUtils;

import org.json.JSONArray;

import org.json.JSONObject;

import org.slf4j.Logger;

import org.slf4j.LoggerFactory;

import java.io.File;

import java.io.IOException;

import java.io.InputStream;

import java.io.OutputStream;

import java.nio.file.Files;

import java.nio.file.Paths;

import java.util.Arrays;

import java.util.Scanner;

import java.util.zip.ZipEntry;

import java.util.zip.ZipFile;

1) Now let's define our main class:

Copied to your clipboard

public class ExtractTextInfoFromPDF {

private static final org.slf4j.Logger LOGGER = LoggerFactory.getLogger(ExtractTextInfoFromPDF.class);

public static void main(String[] args) {

}

}

1) Set the environment variables `PDF_SERVICES_CLIENT_ID` and `PDF_SERVICES_CLIENT_SECRET` by running the following commands and replacing placeholders `YOUR CLIENT ID` and `YOUR CLIENT SECRET` with the credentials present in `pdfservices-api-credentials.json` file:

* **Windows:**

  * `set PDF_SERVICES_CLIENT_ID=<YOUR CLIENT ID>`
  * `set PDF_SERVICES_CLIENT_SECRET=<YOUR CLIENT SECRET>`

* **MacOS/Linux:**

  * `export PDF_SERVICES_CLIENT_ID=<YOUR CLIENT ID>`
  * `export PDF_SERVICES_CLIENT_SECRET=<YOUR CLIENT SECRET>`

1) Next, we can create our credentials and use them to create a PDF Services instance

Copied to your clipboard

Credentials credentials = new ServicePrincipalCredentials(

System.getenv("PDF_SERVICES_CLIENT_ID"),

System.getenv("PDF_SERVICES_CLIENT_SECRET"));

PDFServices pdfServices = new PDFServices(credentials);

1) Now, let's upload the asset:

Copied to your clipboard

Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());

we define what PDF will be extracted. (You can download the source we used [here](https://developer.adobe.com/document-services/docs/Adobe%20Extract%20API%20Sample.pdf).) In a real application, these values would be typically be dynamic.

1) Now, let's create the job:

Copied to your clipboard

ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPdfParamsBuilder()

.addGetStylingInfo(false)

.addElementsToExtract(Arrays.asList(ExtractElementType.TEXT))

.build();

ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)

.setParams(extractPDFParams);

This set of code defines what we're doing (an Extract operation), it defines parameters for the Extract job. PDF Extract API has a few different options, but in this example, we're simply asking for the most basic of extractions, the textual content of the document.

1) The next code block submits the job and gets the job result:

Copied to your clipboard

String location = pdfServices.submit(extractPDFJob);

PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);

Asset resultAsset = pdfServicesResponse.getResult().getResource();

StreamAsset streamAsset = pdfServices.getContent(resultAsset);

This code runs the Extraction process, gets the content of the result zip in stream asset.

1) The next code block saves the result at the specified location:

Copied to your clipboard

String zipFileOutputPath = "output/ExtractTextInfoFromPDF.zip";

OutputStream outputStream = Files.newOutputStream(new File(zipFileOutputPath).toPath());

IOUtils.copy(streamAsset.getInputStream(), outputStream);

1) In this block, we read in the ZIP file, extract the JSON result file, and parse it:

Copied to your clipboard

ZipFile resultZip = new ZipFile(zipFileOutputPath);

ZipEntry jsonEntry = resultZip.getEntry("structuredData.json");

InputStream is = resultZip.getInputStream(jsonEntry);

Scanner s = new Scanner(is).useDelimiter("\\A");

String jsonString = s.hasNext() ? s.next() : "";

s.close();

JSONObject jsonData = new JSONObject(jsonString);

1) Finally we can loop over the result and print out any found element that is an `H1`:

Copied to your clipboard

JSONArray elements = jsonData.getJSONArray("elements");

for(int i=0; i < elements.length(); i++) {

JSONObject element = elements.getJSONObject(i);

String path = element.getString("Path");

if(path.endsWith("/H1")) {

String text = element.getString("Text");

System.out.println(text);

}

}

![Image 5: Example running in the command line](https://developer.adobe.com/document-services/docs/static/92b9e6b462ac478fbcf9b63a784f3d6b/bbbf7/shot9.png)

Here's the complete application (`src/main/java/ExtractTextInfoFromPDF.java`):

Copied to your clipboard

import com.adobe.pdfservices.operation.PDFServices;

import com.adobe.pdfservices.operation.PDFServicesMediaType;

import com.adobe.pdfservices.operation.PDFServicesResponse;

import com.adobe.pdfservices.operation.auth.Credentials;

import com.adobe.pdfservices.operation.auth.ServicePrincipalCredentials;

import com.adobe.pdfservices.operation.exception.SDKException;

import com.adobe.pdfservices.operation.exception.ServiceApiException;

import com.adobe.pdfservices.operation.exception.ServiceUsageException;

import com.adobe.pdfservices.operation.io.Asset;

import com.adobe.pdfservices.operation.io.StreamAsset;

import com.adobe.pdfservices.operation.pdfjobs.jobs.ExtractPDFJob;

import com.adobe.pdfservices.operation.pdfjobs.params.extractpdf.ExtractElementType;

import com.adobe.pdfservices.operation.pdfjobs.params.extractpdf.ExtractPDFParams;

import com.adobe.pdfservices.operation.pdfjobs.result.ExtractPDFResult;

import org.apache.commons.io.IOUtils;

import org.json.JSONArray;

import org.json.JSONObject;

import org.slf4j.Logger;

import org.slf4j.LoggerFactory;

import java.io.File;

import java.io.IOException;

import java.io.InputStream;

import java.io.OutputStream;

import java.nio.file.Files;

import java.nio.file.Paths;

import java.util.Arrays;

import java.util.Scanner;

import java.util.zip.ZipEntry;

import java.util.zip.ZipFile;

public class ExtractTextInfoFromPDF {

private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextInfoFromPDF.class);

public static void main(String[] args) {

try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/Adobe Extract API Sample.pdf").toPath())) {

Credentials credentials = new ServicePrincipalCredentials(

System.getenv("PDF_SERVICES_CLIENT_ID"),

System.getenv("PDF_SERVICES_CLIENT_SECRET"));

PDFServices pdfServices = new PDFServices(credentials);

Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());

ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()

.addElementsToExtract(Arrays.asList(ExtractElementType.TEXT)).build();

ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)

.setParams(extractPDFParams);

String location = pdfServices.submit(extractPDFJob);

PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);

Asset resultAsset = pdfServicesResponse.getResult().getResource();

StreamAsset streamAsset = pdfServices.getContent(resultAsset);

Files.createDirectories(Paths.get("output/"));

String zipFileOutputPath = "output/ExtractTextInfoFromPDF.zip";

OutputStream outputStream = Files.newOutputStream(new File(zipFileOutputPath).toPath());

LOGGER.info("Saving asset at output/ExtractTextInfoFromPDF.pdf");

IOUtils.copy(streamAsset.getInputStream(), outputStream);

outputStream.close();

ZipFile resultZip = new ZipFile(zipFileOutputPath);

ZipEntry jsonEntry = resultZip.getEntry("structuredData.json");

InputStream is = resultZip.getInputStream(jsonEntry);

Scanner s = new Scanner(is).useDelimiter("\\A");

String jsonString = s.hasNext() ? s.next() : "";

s.close();

JSONObject jsonData = new JSONObject(jsonString);

JSONArray elements = jsonData.getJSONArray("elements");

for(int i=0; i < elements.length(); i++) {

JSONObject element = elements.getJSONObject(i);

String path = element.getString("Path");

if(path.endsWith("/H1")) {

String text = element.getString("Text");

System.out.println(text);

}

}

} catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {

LOGGER.error("Exception encountered while executing operation", e);

}

}

}

Next Steps[](https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/quickstarts/extract-pdf/java/#next-steps)
----------------------------------------------------------------------------------------------------------------------------------

* * *

Now that you've successfully performed your first operation, [review the documentation](https://developer.adobe.com/document-services/docs/overview/pdf-services-api/) for many other examples and reach out on our [forums](https://community.adobe.com/t5/document-services-apis/ct-p/ct-Document-Cloud-SDK) with any questions. Also remember the samples you downloaded while creating your credentials also have many demos.

Was this helpful?
