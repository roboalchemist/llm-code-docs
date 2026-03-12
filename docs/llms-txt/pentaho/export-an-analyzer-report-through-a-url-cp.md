# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/export-an-analyzer-report-through-a-url-cp.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/export-an-analyzer-report-through-a-url-cp.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/export-an-analyzer-report-through-a-url-cp.md

# Export an Analyzer report through a URL

You can export an Analyzer report as a PDF, CSV, Microsoft Excel, or JSON file from a Pentaho repository through a URL. This ability is useful when you want to export reports from a different scheduler.

In the URL, include a path to the repository containing your report. The default output is PDF. To specify a different output type, use the format parameter and specify either CSV, EXCEL, or JSON. To use the URL from a command line, include a call to the curl command with your `<Analyzer user>` and `<password>` before calling the URL.

The following examples show how to call Analyzer from an iframe, link, or button event in a third-party web application to export a file:

* **Default PDF export**

  `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export`
* **CSV export**

  `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export?format=CSV`
* **EXCEL export**

  `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export?format=EXCEL`
* **JSON export**

  `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export?format=JSON`

  **Note:** The dimensional structure of an exported JSON data table is similiar to a CSV export. However, subtotals are not included in a JSON data table. By default, you can export up to 10,000 rows. To adjust the default setting, use the `renderer.export.max.rows.json` parameter in the `analyzer.properties` file. See the **Administer Pentaho Data Integration and Analytics** document for details.

## Setting report parameters in the URL

You can also set report parameters while exporting an Analyzer report as a PDF, CSV, or Microsoft Excel file from a Pentaho repository through a URL.

* To set a range, specify the starting point as `<parameter name>_START` and an ending point as `<parameter name>_END`. For example, if your report has a YEAR parameter, the following sample URL would export an Analyzer report from 2004 to 2005 as a CSV file: `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export?YEAR_START=2004&YEAR_END=2005&format=CSV`
* To set multiple values for a given parameter, repeat the parameter in the call. For example, if your report has a TERRITORY parameter, the following sample URL would export an Analyzer report for both NA and EMEA as a PDF file: `http://localhost:8080/pentaho/api/repos/<repository path to report with xanalyzer extension>/service/export?TERRITORY=NA&TERRITORY=EMEA`
