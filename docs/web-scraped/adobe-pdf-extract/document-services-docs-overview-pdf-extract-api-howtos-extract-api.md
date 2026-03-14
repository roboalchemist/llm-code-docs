# Source: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/howtos/extract-api/

Title: Extract API | How Tos | PDF Extract API

URL Source: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/howtos/extract-api/

Markdown Content:
Adobe Developer
Products
Adobe Acrobat Services
APIs
Use Cases
Pricing
Resources
Documentation
REST APIs
Get credentials
Console
Sign in
Introduction
PDF Services API
PDF Accessibility Auto-Tag API
PDF Extract API
Overview
Getting Started
Quickstarts
How Tos
PDF Extract API
PDF to Markdown API
Document Generation API
PDF Electronic Seal API
PDF Embed API
Licensing and Usage Limits
Security, Privacy and Compliance
Version and Release Notes
Support
Technical FAQ
API Status
Legacy Documentation
Products
Adobe Acrobat Services
Documentation
Overview
PDF Extract API
Overview
How Tos
PDF Extract API
Edit in GitHub
Log an issue
Extract PDF
Structured Information Output Format

The output of an SDK extract operation is a zip package containing the following:

The structuredData.json file with the extracted content & PDF element structure. See the JSON schema for a description of the default output. (Please refer the Styling JSON schema for a description of the output when the styling option is enabled.)
A renditions folder(s) containing renditions for each element type selected as input. The folder name is either "tables" or "figures" depending on your specified element type. Each folder contains renditions with filenames that correspond to the element information in the JSON file.

The following is a summary of key elements in the extracted JSON(See additional descriptions in the JSON schema):

Elements : Ordered list of semantic elements (like headings, paragraphs, tables, figures) found in the document, on the basis of position in the structure tree of the document.The output does not include headers or footers.In addition, headings that repeat across pages are reported for the first occurrence only.

Bounds : Bounding box enclosing the content items forming this element. Not reported for elements which don't have any content items (like empty table cells). The bounds are as per PDF specification coordinates. PDF pages are generally specified in inches (like A4 page is 8.3 inches x 11.7 inches). If values are required in coordinates, we need a DPI value i.e. dots per inches. As per PDF specification, 72 DPI is used when creating a PDF. So, width of an A4 page is specified to be ~= 598 units (8.3 inches x 72) when creating the PDF. All values reported in Extract use this 72 dpi based coordinates. Again as per PDF spec, absolute values of bounds are in a coordinate system where origin is (0,0), up and right directions are positive. Going by this coordinate system, for all rects reported in Extract, bottom < top and left < right. In Extract JSON schema, all rects are of type #/definitions/rect and rect is defined as:

description: Rectangle/Box in PDF coordinate system (bottom-left is origin). Values are in PDF user space units. Order of values - left, bottom, right, top.

Font : Font description for the font associated with the first character. Only reported for text elements.

TextSize : Text size (in points) of the last character. Only reported for text elements.

Attributes: Includes additional properties like line height and text alignment.

Path : The Path describes the location of elements in the structure tree including the element type and the instance number. Path along with bounds defines the reading order of the document. Element types are based on the ISO standard , a summary is included below for convenience :

Aside : Content which is not part of regular content flow of the document
Figure : Non-reflowable constructs like graphs, images, flowcharts
Footnote : FootNote
H, H1, H2, etc : Heading Level
L : List
Li : List Item
Lbl : List Item label
Lbody : List item body
P : Paragraph
ParagraphSpan : Denotes part of a paragraph. Reported when paragraph is broken (generally due to page break or column break)
Reference : Link
Sect : Logical section of the document
StyleSpan : Denotes difference in styling of text relative to the parent container
Sub : Single line of a multiline paragraph (e.g. addresses). Such paras are created in html using \<br> inside \<p> tags
Table : Table
TD : Table cell
TH : Table header cell
TR : Table row
Title : Title of the document. This is the most prominent heading which can define the whole document.
TOC : Table of contents
TOCI : Table of contents item
Watermark : Watermark

Text : Text for the element in UTF-8 format, only reported for text elements. When inline elements are reported separately from parent block element, then this value has references to those inline elements.

Figures : Identified as a Figure in the Path attribute, saved as a PNG in the figures folder with the filename identified in the filePaths attribute.

Tables : Identified as a Table in the Path attribute, saved as a .CSV, .XLSX, and .PNG in the tables folder with the filename identified in the filePaths attribute.

FilePaths : List of file paths to additional output files (images and spreadsheets)

Pages : A list of properties for each page of the PDF including page number, width, height, and rotation.

Reading Order : The reading order of content within columns, across page breaks, and inclusive of asides is represented by the order of the elements in the Elements array. In the normal mode, exceptions can occur for elements extracted from their container (eg. A reference link in the middle of a paragraph). However, the order is preserved in Styling mode where all Elements and their Kids are represented in the natural reading order. Reading order is determined by Bounds and path element provided in the .json file.

API limitations

File size: Files up to a maximum of 100MB are supported.
Number of Pages: Non-scanned PDFs have a limit of 400 pages. Scanned PDFs have a limit of 150 pages or less. Limits may be lower for files with multiple tables. For larger files or those with complex layouts, it is recommended to split the file into smaller sections before processing.
Rate limits: Keep request rate below 25 requests per minutes.
Page Size: The API supports standard page sizes not to exceed 17.5” or less than 6” in either dimension.
Hidden Objects: PDF files that contain content that is not visible on the page like javascript, OCG (optional content groups), etc are not supported. Files that contain such hidden information may fail to process. For such cases, [removing hidden content](https://helpx.adobe.com/acrobat/using/removing-sensitive-content-pdfs.html) prior to processing files again may return a successful result.
Language: The API is currently optimized for English language content. Files containing content in other Latin languages should return good results, but may have issues with non-English punctuation.
OCR and Scan quality: The quality of text extracted from scanned files is dependent on the clarity of content in the input file. Conditions like skewed pages, shadowing, obscured or overlapping fonts, and page resolution less than 200 DPI can all result in lower quality text output.
Form fields: Files containing XFA and other fillable form elements are not supported.
Unprotected files: The API supports files that are unprotected or where security restrictions allow copying of content. Files that are secured and do not allow copying of content will not be processed.
Annotations: Content in PDF files containing annotations such as highlights and sticky notes will be processed, but annotations that obscure text could impact output quality. Text within annotations will not be included in the output.
PDF Producers: The Extract API is designed to extract content from files that contain text, table data, and figures. Files created from applications that produce other types of content like illustrations, CAD drawings or other types of vector art may not return quality results.
Error codes
SCENARIO ERROR CODE ERROR MESSAGE

Invalid API parameters
 
-
 
Invalid parameters

File size violation
 
DISQUALIFIED_FILE_SIZE
 
File exceeds size limit.

Page limit violation
 
DISQUALIFIED_PAGE_LIMIT
 
File exceeds page limit.

Scan page limit violation
 
DISQUALIFIED_SCAN_PAGE_LIMIT
 
Scanned file exceeds page limit.

Unsupported XFA file
 
DISQUALIFIED_XFA
 
File contains XFA form(s). Not supported for content extraction.

Encryption permission
 
DISQUALIFIED_PERMISSIONS
 
File permissions do not allow for content extraction.

Complex file
 
DISQUALIFIED_COMPLEX_FILE
 
File contents are too complex for content extraction.

Unsupported language
 
DISQUALIFIED_LANGUAGE
 
File content language is unsupported.

Bad PDF
 
BAD_PDF
 
Unable to extract content. File is corrupted, malformed or an empty PDF.

Invalid file type
 
BAD_PDF_FILE_TYPE
 
The input file is not a PDF file.

Damaged file
 
BAD_PDF_DAMAGED
 
The input file is damaged.

File contains complex table
 
BAD_PDF_COMPLEX_TABLE
 
The input file contains a table that is too complex to process.

File contains complex content
 
BAD_PDF_COMPLEX_INPUT
 
The input file contains content that is too complex to process.

File contains unsupported font
 
BAD_PDF_UNSUPPORTED_FONT
 
The input file contains font data that is corrupted or not supported.

Large PDF
 
BAD_PDF_LARGE_FILE
 
The input file size exceeds the maximum allowed.

Protected PDF
 
PROTECTED_PDF
 
Unable to extract content. File is password protected.

Empty or corrupted input
 
BAD_INPUT
 
Input is corrupted or empty.

Invalid input parameters
 
BAD_INPUT_PARAMS
 
Invalid input parameters.

Timeout
 
TIMEOUT
 
Processing timeout. Please try splitting the file into multiple files with fewer pages.

Unknown error / failure
 
ERROR
 
Unable to extract content - Internal error.
REST API

See our public API Reference for Extract PDF.

Extract Text from a PDF

The sample below extracts text element information from a PDF document and returns a JSON file.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextInfoFromPDF
  
 public class ExtractTextInfoFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextInfoFromPDF.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT)).build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextInfoFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextInfoFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
       
Extract Text and Tables

The sample below extracts text and table element information from a PDF document and returns a JSON file along with table data in XLSX format.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableInfoFromPDF
  
 public class ExtractTextTableInfoFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoFromPDF.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT, ExtractElementType.TABLES))
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
       
Extract Text and Tables (w/ Tables Renditions)

The sample below extracts text and table element information as well as table renditions from a PDF Document. Note that the output is a zip containing the structured information in a JSON file along with table renditions in PNG and XLSX format.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableInfoWithRenditionsFromPDF
  
 public class ExtractTextTableInfoWithRenditionsFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoWithRenditionsFromPDF.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT, ExtractElementType.TABLES))
                 .addElementToExtractRenditions(ExtractRenditionsElementType.TABLES)
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoWithRenditionsFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoWithRenditionsFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
Extract Text and Tables (w/ Tables and Figures Renditions)

The sample below extracts text and table elements information as well as table and figure renditions from a PDF Document. Note that the output is a zip containing the structured information in a JSON file along with figure renditions as PNGs and table renditions in PNG and XLSX format.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableInfoWithRenditionsFromPDF
  
 public class ExtractTextTableInfoWithFiguresTablesRenditionsFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoWithFiguresTablesRenditionsFromPDF.class);
     
     public static void main(String[] args) {
     
         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT, ExtractElementType.TABLES))
                 .addElementsToExtractRenditions(Arrays.asList(ExtractRenditionsElementType.TABLES, ExtractRenditionsElementType.FIGURES))
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoWithFiguresTablesRenditionsFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoWithFiguresTablesRenditionsFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
   }
Extract Text and Tables and Character Bounding Boxes (w/ Renditions)

The sample below extracts table renditions and bounding boxes for characters present in text blocks (paragraphs, list, headings), in addition to text and table element information from a PDF Document. Note that the output is a zip containing the structured information along with table renditions in PNG and XLSX format.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableInfoWithCharBoundsFromPDF
  
 public class ExtractTextTableInfoWithCharBoundsFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoWithCharBoundsFromPDF.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementToExtract(ExtractElementType.TEXT)
                 .addCharInfo(true)
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoWithCharBoundsFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoWithCharBoundsFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
Extract Text and Tables and Table Structure as CSV (w/ Renditions)

The sample below adds option to get CSV output for tables in addition to extracting text and table element information as well as table renditions from a PDF Document. Note that the output is a zip containing the structured information along with table renditions in PNG and CSV format.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableInfoWithTableStructureFromPdf
  
 public class ExtractTextTableInfoWithTableStructureFromPdf {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoWithTableStructureFromPdf.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT, ExtractElementType.TABLES))
                 .addElementToExtractRenditions(ExtractRenditionsElementType.TABLES)
                 .addTableStructureFormat(TableStructureType.CSV)
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoWithTableStructureFromPdf.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoWithTableStructureFromPdf.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
Extract Text and Tables and Styling Info

The sample below adds an option to get styling information for each text element( Bold / Italics / Superscript etc) in addition to extracting text and table element information. Note that the output is a zip containing the structured information along with table renditions in PNG and XLSX format. Please see the Styling JSON schema for reference.

Please refer the API usage guide to understand how to use our APIs.

Java
.NET
Node JS
Python
REST API
Copy
 // Get the samples from https://www.adobe.com/go/pdftoolsapi_java_samples
 // Run the sample:
 // mvn -f pom.xml exec:java -Dexec.mainClass=com.adobe.pdfservices.operation.samples.extractpdf.ExtractTextTableWithStylingInfoFromPdf
  
 public class ExtractTextTableInfoWithStylingFromPDF {
 

     private static final Logger LOGGER = LoggerFactory.getLogger(ExtractTextTableInfoWithStylingFromPDF.class);
 

     public static void main(String[] args) {
 

         try (InputStream inputStream = Files.newInputStream(new File("src/main/resources/extractPdfInput.pdf").toPath())) {
             // Initial setup, create credentials instance
             Credentials credentials = new ServicePrincipalCredentials(
                 System.getenv("PDF_SERVICES_CLIENT_ID"),
                 System.getenv("PDF_SERVICES_CLIENT_SECRET"));
         
             // Creates a PDF Services instance
             PDFServices pdfServices = new PDFServices(credentials);
         
             // Creates an asset(s) from source file(s) and upload
             Asset asset = pdfServices.upload(inputStream, PDFServicesMediaType.PDF.getMediaType());
         
             // Create parameters for the job
             ExtractPDFParams extractPDFParams = ExtractPDFParams.extractPDFParamsBuilder()
                 .addElementsToExtract(Arrays.asList(ExtractElementType.TEXT, ExtractElementType.TABLES))
                 .addGetStylingInfo(true)
                 .build();
         
             // Creates a new job instance
             ExtractPDFJob extractPDFJob = new ExtractPDFJob(asset)
                 .setParams(extractPDFParams);
         
             // Submit the job and gets the job result
             String location = pdfServices.submit(extractPDFJob);
             PDFServicesResponse<ExtractPDFResult> pdfServicesResponse = pdfServices.getJobResult(location, ExtractPDFResult.class);
         
             // Get content from the resulting asset(s)
             Asset resultAsset = pdfServicesResponse.getResult().getResource();
             StreamAsset streamAsset = pdfServices.getContent(resultAsset);
         
             // Creates an output stream and copy stream asset's content to it
             Files.createDirectories(Paths.get("output/"));
             OutputStream outputStream = Files.newOutputStream(new File("output/ExtractTextTableInfoWithStylingFromPDF.zip").toPath());
             LOGGER.info("Saving asset at output/ExtractTextTableInfoWithStylingFromPDF.zip");
             IOUtils.copy(streamAsset.getInputStream(), outputStream);
             outputStream.close();
         } catch (ServiceApiException | IOException | SDKException | ServiceUsageException e) {
             LOGGER.error("Exception encountered while executing operation", e);
         }
     }
 }
How Tos
PDF to Markdown API
Last updated 5/22/2024
Was this helpful?
Yes
No
APIs and Services
Adobe Creative Cloud
Adobe Experience Platform
Adobe Document Cloud
Adobe Cloud Manager
Adobe Analytics
App Builder
View all
Community
Adobe Tech Blog
Adobe on GitHub
Adobe Developer on YouTube
Adobe Developer on X
Community Forums
Support
Adobe Developer support
Adobe Product support
Adobe Developer
Adobe Developer Console
Developer Distribution
Open source at Adobe
Download SDKs
Authentication
Careers
Privacy
Terms of Use
Cookie preferences
Do not sell or share my personal information
AdChoices
Copyright © 2026 Adobe. All rights reserved.
