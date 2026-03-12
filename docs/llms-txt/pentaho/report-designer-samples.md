# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/report-designer-samples.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/report-designer-samples.md

# Report Designer samples

The following samples show how to render Report Designer reports in various web applications.

## Execute a report from a HTML form (POSTing parameters)

This sample renders a Report Designer (PRPT) report by posting the report parameters to the report REST URL:

`http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/generatedContent`

The POST request contains all parameters the report expects, plus the additional rendering parameter **output-target**, which controls the rendering format (HTML, PDF, XLS, etc.)

The following output formats are supported:

| **Option**                                                                         | **Purpose**                                                                       |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `table/html;page-mode=stream`                                                      | HTML as a single page, all report pagebreaks are ignored.                         |
| `table/html;page-mode=page`                                                        | HTML as a sequence of physical pages, manual and automatic pagebreaks are active. |
| `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;page-mode=flow` | Excel 2007 XLSX Workbook                                                          |
| `table/excel;page-mode=flow`                                                       | Excel 97 Workbook                                                                 |
| `table/csv;page-mode=stream`                                                       | CSV output                                                                        |
| `table/rtf;page-mode=flow`                                                         | Rich text format                                                                  |
| `pageable/pdf`                                                                     | PDF output                                                                        |
| `pageable/text`                                                                    | Plain text                                                                        |
| `pageable/xml`                                                                     | Pageable layouted XML                                                             |
| `table/xml`                                                                        | Table-XML output                                                                  |
| `pageable/X-AWT-Graphics;image-type=png`                                           | A single report page as PNG.                                                      |
| `mime-message/text/html`                                                           | MIME email with HTML as body text and all style and images as inline attachments. |

## Render a report in an IFRAME

This sample renders a PRPT report using a regular GET request, by populating an HTML IFRAME with the report REST URL:

`http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/generatedContent?*&lt;parameters&gt;*`

The request contains all parameters as part of the URL.

## Render report viewer with available parameters and executed report

The sample renders the **Pentaho Report Viewer IU** by populating an HTML IFRAME with the report REST URL:

`http://localhost:8080/pentaho/api/repos/**&lt;path&gt;**/viewer?**&lt;parameters&gt;**`

The request contains the initial report parameters as part of the URL.
