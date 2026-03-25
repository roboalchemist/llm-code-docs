# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/analyzer-samples.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/analyzer-samples.md

# Analyzer samples

The following samples show how to embed Analyzer reports into other web applications.

## Display a report in viewer mode

This sample renders a display using a regular `GET` request, by populating an HTML IFRAME with the report REST URL:

```
http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/viewer
```

The viewer has limited possibilities for interaction and does not allow changing the report.

## Display a report in editor mode

The sample renders a full **Analyzer IU** by populating an HTML IFRAME with the report REST URL:

```
http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/editor
```

The IFRAME now renders the full Analyzer user interface, allowing users to interact with the data.

## Create a new Analyzer report

The sample prepares a new Analyzer report by populating an HTML IFRAME with the report REST URL:

```
http://localhost:8080/pentaho/api/repos/xanalyzer/editor?catalog=*&lt;Schema&gt;*&cube=*&lt;CubeName&gt;*
```

The mandatory **catalog** and **cube** parameters specify the analysis schema and cube to use for the new report.

## Integrate into a custom web application via an IFRAME

The sample opens a new page that mimics a parent application that integrates Analyzer using an IFrame. The parent application has a set of buttons interacting with the **Analyzer UI** in the embedded IFRAME. Studying this page is a good starting point, if you are trying to deeply integrate analyzer into your own web application.

## Specify the select schema service

The sample is opened with a specified data service.

```
http://localhost:8080/pentaho/api/repos/xanalyzer/service/selectSchema
```

After a data service is selected, the sample opens and shows an unsaved Analyzer report using that data service.
