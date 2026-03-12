# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/interactive-reports-samples.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/interactive-reports-samples.md

# Interactive Reports samples

The following samples show how to embed Interactive Reports into other web applications.

## Display Interactive Reports

This sample renders a PRPTI report using a regular `GET` request, by populating an HTML IFRAME with the report REST URL. The viewer has limited possibilities for interaction and cannot edit the report. The example below shows how to do this by replacing the path within the <> with the URL for the report that you want to view.

```
http://localhost:8080/pentaho/api/repos/*&lt;%3Ayour%3Apath%3Agoes%3Ahere.prpti&gt;*/prpti.view
```

You can use the `prpti.edit` end-point instead, to allow more user interaction with the report.

```
http://localhost:8080/pentaho/api/repos/*&lt;%3Ayour%3Apath%3Agoes%3Ahere.prpti&gt;*/prpti.edit
```

## Create new Interactive Reports

The sample prepares a new report by populating an HTML IFRAME with the report REST URL.

```
http://localhost:8080/pentaho/api/repos/pentaho-interactive-reporting/prpti.new

```

In order to show the toolbar buttons so that users can create, open, or save Interactive reports, add the following to the end of the URL.

```
?showRepositoryButtons=true

```

Users will be prompted to select the data source they want to work with.

## Integrate into a custom web application via an IFRAME

The sample opens a new page that mimics a parent application that integrates the Interactive Reports editor using an IFrame. The parent application has a set of buttons interacting with the **Interactive Reporting UI** in the embedded IFRAME. Studying this page is a good starting point, if you are trying to deeply integrate Interactive Reports into your own web application.
