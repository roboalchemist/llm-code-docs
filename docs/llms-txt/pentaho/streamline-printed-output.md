# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/streamline-printed-output.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/streamline-printed-output.md

# Streamline printed output

Pentaho Reporting's overall performance is chiefly affected by the amount of printed content that it has to generate. The more content you generate, the more time the Pentaho Reporting engine will take to perform all layout computations.

Large inline subreports are notorious for poor performance. This is because the output layout of an inline subreport is always stored in memory. The master report's layouting pauses until the subreport is fully generated, then it's inserted into the master report's layout model and subsequently printed. Memory consumption for this layouting model is high because the full layout model is kept in memory until the report is finished. If there is a large amount of content in the subreport, you will run into `out of memory` exceptions.

An inline subreport that consumes the full width of the root-level band should be converted into a banded subreport. Banded subreports are layouted and all output is generated while the subreport is processed. The memory footprint for that is small because only the active band or the active page has to be held in memory.

When images are embedded from remote servers (HTTP/FTP sources), you must ensure that the server produces a `LastModifiedDate` header. The Pentaho Reporting engine uses that header as part of its caching system, and if it is missing, the remote images will not be cached, forcing the engine to retrieve them every time they're needed.

Caching must be configured properly via a valid ehcache configuration file, which is stored in the Pentaho Web app in the `/WEB-INF/classes/` directory. If caching is disabled or misconfigured, then there will be performance problems when loading reports and resources.

## Paginated exports

A pageable report generates a stream of pages. Each page has the same height, even if the page is not fully filled with content. When a page is filled, the layouted page will be passed over to the output target to render it in either a Graphics2D or a streaming output (PDF, Plaintext, HTML, etc.) context.

### Page break methods

When the content contains a manual page break, the page will be considered full. If the pagebreak is a before-print break, then the break will be converted to an after-break, the internal report states will be rolled back, and the report processing restarts to regenerate the layout with the new constraints. A similar rollback happens if the current band does not fit on the page. Because of this, you would generally prefer break-before over break-after.

So for large reports, you might consider removing manual page breaks and limiting the width of bands.

### Page states

When processing a pageable report, the Pentaho Reporting engine assumes that the report will be run in interactive mode, which allows for parameterization control. To make browsing through the pages faster, a number of page states will be stored to allow report end-users to restart output processing at the point in the report where they adjust the parameters.

Reports that are run to fully export all pages usually do not need to store those page states. A series of Pentaho Reporting engine settings controls the number and frequency of the page states stored:

* **org.pentaho.reporting.engine.classic.core.performance.pagestates.PrimaryPoolSize=20**
* **org.pentaho.reporting.engine.classic.core.performance.pagestates.SecondaryPoolFrequency=4**
* **org.pentaho.reporting.engine.classic.core.performance.pagestates.SecondaryPoolSize=100**
* **org.pentaho.reporting.engine.classic.core.performance.pagestates.TertiaryPoolFrequency=10**

The Pentaho Reporting engine uses three lists to store page states. The default configuration looks as follows:

1. The first 20 states (Pages 1 to 20) are stored in the primary pool. All states are stored with strong references and will not be garbage collected.
2. The next 400 states (pages 21 to 421) are stored into the secondary pool. Of those, every fourth state is stored with a strong reference and cannot be garbage collected as long as the report processor is open.
3. All subsequent states (pages > 421) are stored in the tertiary pool and every tenth state is stored as strong reference.

So for a 2000-page report, a total of about 270 states will be stored with strong references.

In server mode, the settings could be cut down to:

```
org.pentaho.reporting.engine.classic.core.performance.pagestates.PrimaryPoolSize=1
org.pentaho.reporting.engine.classic.core.performance.pagestates.
  SecondaryPoolFrequency=1
org.pentaho.reporting.engine.classic.core.performance.pagestates.SecondaryPoolSize=1
org.pentaho.reporting.engine.classic.core.performance.pagestates.
  TertiaryPoolFrequency=100
```

This reduces the number of states stored for a 2000-page report to 22, thus cutting the memory consumption for the page states to a 1/10th.

**Note:** In the current version full exports do not generate page states and thus these settings have no effect on such exports. They still affect the interactive mode.

## Table exports

A table export produces tabular output from a fully-layouted display model. A table export cannot handle overlapping elements and therefore has to remove them.

To support layout debugging, the Pentaho Reporting engine stores a lot of extra information in the layout model. This increases memory consumption but makes it easier to develop Reporting solutions. These Pentaho Reporting engine debug settings should never be enabled in production environments:

* **org.pentaho.reporting.engine.classic.core.modules.output.table.base.ReportCellConflicts**
* **org.pentaho.reporting.engine.classic.core.modules.output.table.base.VerboseCellMarkers**

**Note:** These settings are `false` by default. Report Designer comes with its own method to detect overlapping elements and does not rely on these settings.

## HTML exports

In HTML exports, there are a few Pentaho Reporting engine settings that can affect export performance. The first is **CopyExternalImages**:

```
org.pentaho.reporting.engine.classic.core.modules.output.table.html.CopyExternalImages=true
```

This controls whether images from HTTP/HTTPS or FTP sources are linked from their original source or copied (and possibly re-encoded) into the output directory. The default is true; this ensures that reports always have the same image. Set to `false` if the image is dynamically generated, in which case you'd want to display the most recent view.

The **Style** and **ForceBufferedWriting** settings control how stylesheets are produced and whether the generated HTML output will be held in a buffer until the report processing is finished:

```
org.pentaho.reporting.engine.classic.core.modules.output.table.html.ForceBufferedWriting=true
```

Style information can be stored inline, or in the \<head> element of the generated HTML file:

```
org.pentaho.reporting.engine.classic.core.modules.output.table.html.InlineStyles=true
```

Or in an external CSS file:

```
org.pentaho.reporting.engine.classic.core.modules.output.table.html.ExternalStyle=true
```

**ForceBufferedWriting** should be set to `true` if a report uses an external CSS file. Browsers request all resources they find in the HTML stream, so if a browser requests a style sheet that has not yet been fully generated, the report cannot display correctly. It is safe to disable buffering if the styles are inline because the browser will not need to fetch an external style sheet in that case. Buffered content will appear slower to the user than non-buffered content because browsers render partial HTML pages while data is still being received from the server. Buffering will delay that rendering until the report is fully processed on the server.
