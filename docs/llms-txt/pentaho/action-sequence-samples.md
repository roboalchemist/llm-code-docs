# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/action-sequence-samples.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-pentaho-server-functionality-into-web-applications/action-sequence-samples.md

# Action sequence samples

The following samples show how to embed an action sequence into other web applications.

## Run an action sequence to generate a report

This sample renders an XACTION report using a regular `GET` request, by populating an HTML IFRAME with the report REST URL:

```
http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/generatedContent?*&lt;parameters&gt;*
```

The parameters for the xaction are passed as simple `GET` parameters on the URL.

## Run an action sequence to generate a report with prompts

The sample prepares a form to collect parameters and POSTs them to the xaction REST URL:

```
http://localhost:8080/pentaho/api/repos/*&lt;path&gt;*/generatedContent
```

The XACTION now retrieves its parameters from the POST request body.
