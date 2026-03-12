# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/embed-the-reporting-engine-into-a-java-application.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/embed-the-reporting-engine-into-a-java-application.md

# Embed the reporting engine into a Java application

This section shows in detail how to build a simple reporting application around the Pentaho Reporting engine. There are three classes for the two examples shown in this section:

1. `AbstractReportGenerator.java`
2. `Sample1.java`
3. `Sample2.java`

You can find the full example source code, plus the `.prpt` report file they use, in the `/source/org/pentaho/reporting/engine/classic/samples/` directory in the Pentaho Reporting SDK.

## Work with the reporting engine samples

In the samples, the interaction with the Pentaho Reporting engine follows these basic steps:

1. Boot (initialize)
2. Get the report definition
3. Get the data for the report (if it is created outside of the report definition)
4. (Optional) Get any report generation parameters
5. Generate the report output in the requested format

With the samples, this allows us to create an abstract base class for all the samples (`AbstractReportGenerator`). This class defines the abstract methods:

* `getReportDefinition()`: this loads/creates/returns the report definition
* `getDataFactory()`: this returns the data to be used by the reporting engine (if the report definition does not tell the engine how to retrieve the data).
* `getReportParameters()`: this returns the set of parameters the reporting engine will use while generating the report

The `generateReport()` method tells the reporting engine to generate the report using the above method, and creates the output in one of the following methods (using the **OutputType** parameter): HTML, PDF, or XLS (Excel). A full list of output types is listed later in this section, but to keep these examples simple, we'll concentrate on these three.

### Sample1.java

In this sample, the `getReportDefinition()` method loads the report definition from a PRPT file created using the Pentaho Report Designer. This report definition defines the following:

* Data Query (retrieving a list of customers based on a set of customer names)
* Report Title
* Report Header – set of 4 columns (Customer Number, Customer Name, Postal Code, Country)
* Report Data – set of 4 columns (Customer Number, Customer Name, Postal Code, Country)

The `getDataFactory()` method returns null to indicate that no data factory is required to be provided. In this example, the source of data is defined in the report definition.

The `getReportParameters()` method defines three parameters in a HashMap:

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>Parameter Name</td><td>Parameter Value</td><td>Description</td></tr><tr><td>Report Title</td><td>Simple Embedded Report Example with Parameters</td><td>The value of this parameter will be placed in the Report Title that is centered on the top of each page in the report. In the report definition, the Report Title field is a Text Field whose value is “Report Title”. This indicates that the field will use the value of the parameter “Report Title” when the report is generated.</td></tr><tr><td>Col Headers BG Color</td><td>yellow</td><td>The value of this parameter will be used as the background color of the column header fields. In the report definition, all four of the column header fields are defined with a bg-color style of “=[Col Headers BG Color]”. This indicates that the value of the “Col Header BG Color” parameter will be used as that value.</td></tr><tr><td>Customer Names</td><td><pre><code>"American Souvenirs Inc",
"Toys4GrownUps.com",
"giftsbymail.co.uk",
"BG&#x26;E Collectables",
"Classic Gift Ideas, Inc"
</code></pre></td><td><p>The value of this parameter defines a set of Customer Names that will be used in the data query. This allows the sample to define which customers will be used in the report at the time the report is generated.```<br>SELECT<br>"CUSTOMERS"."CUSTOMERNAME",<br>"CUSTOMERS"."POSTALCODE",<br>"CUSTOMERS"."COUNTRY",<br>"CUSTOMERS"."CUSTOMERNUMBER"<br>FROM<br>"CUSTOMERS"<br>WHERE<br>"CUSTOMERS"."CUSTOMERNAME" IN (${Customer Names})</p><pre><code>
&#x3C;/td>&#x3C;/tr>&#x3C;/tbody>
&#x3C;/table>The `main()` method creates an output filename in which the report will be generated and then starts the report generation process.

</code></pre></td></tr></tbody></table>

### Sample2.java

In this sample, the `getReportDefinition()` method creates a blank report and sets the query name to `ReportQuery`. It then adds a report pre-processor called `RelationalAutoGeneratorPreProcessor`.

Report pre-processors execute during the report generation process after the data query has been executed but before the report definition is used to determine the actual layout of the report. The benefit of this is that the `RelationalAutoGeneratorPreProcessor` will use the column information retrieved from the data query to add header fields in the **Page Header** and data fields in the **Item Band** of the report definition for each column of data in the result set.

The `getDataFactory()` method first defines the **DriverConnectionProvider** which contains all the information required to connect to the database. It then defines the **DataFactory** which will use the connection provider to connect to the database. The Data Factory then has the query set which will be used in report generation. The query name *ReportQuery* must match the query name defined when the report definition was created or else the report will contain no data.

The `getReportParameters()` method is not used in this example, so it returns null.

The `main()` method creates an output filename in which the report will be generated and then starts the report generation process.

## Sample 0: The base class

The `AbstractReportGenerator` class shown below is extended by the two primary example applications. It contains the basic logic that creates a report, leaving the details of input and output to the classes that extend it:

```
/*
 * This program is free software; you can redistribute it and/or modify it under the 
 * terms of the GNU Lesser General Public License, version 2.1 as published by the Free Software 
 * Foundation.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this 
 * program; if not, you can obtain a copy at http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html 
 * or from the Free Software Foundation, Inc., 
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * Copyright 2009 Pentaho Corporation.  All rights reserved.
 *
 * Created July 22, 2009 
 * @author dkincade
 */
package org.pentaho.reporting.engine.classic.samples;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Map;

import org.pentaho.reporting.engine.classic.core.ClassicEngineBoot;
import org.pentaho.reporting.engine.classic.core.DataFactory;
import org.pentaho.reporting.engine.classic.core.MasterReport;
import org.pentaho.reporting.engine.classic.core.ReportProcessingException;
import org.pentaho.reporting.engine.classic.core.layout.output.​AbstractReportProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.pageable.​base.PageableReportProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.pageable.​pdf.PdfOutputProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.table.base​.FlowReportProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.table.base​.StreamReportProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.table.html​.AllItemsHtmlPrinter;
import org.pentaho.reporting.engine.classic.core.modules.output.table.html​.FileSystemURLRewriter;
import org.pentaho.reporting.engine.classic.core.modules.output.table.html​.HtmlOutputProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.table.html​.HtmlPrinter;
import org.pentaho.reporting.engine.classic.core.modules.output.table.html​.StreamHtmlOutputProcessor;
import org.pentaho.reporting.engine.classic.core.modules.output.table.xls.​FlowExcelOutputProcessor;
import org.pentaho.reporting.libraries.repository.ContentLocation;
import org.pentaho.reporting.libraries.repository.DefaultNameGenerator;
import org.pentaho.reporting.libraries.repository.stream.StreamRepository;

/**
 * This is the base class used with the report generation examples. It contains the actual <code>embedding</code>
 * of the reporting engine and report generation. All example embedded implementations will need to extend this class
 * and perform the following:
 * <ol>
 * <li>Implement the <code>getReportDefinition()</code> method and return the report definition (how the report
 * definition is generated is up to the implementing class).
 * <li>Implement the <code>getTableDataFactory()</code> method and return the data factory to be used (how
 * this is created is up to the implementing class).
 * <li>Implement the <code>getReportParameters()</code> method and return the set of report parameters to be used.
 * If no report parameters are required, then this method can simply return <code>null</code>
 * </ol>
 */
public abstract class AbstractReportGenerator
{
  /**
   * The supported output types for this sample
   */
  public static enum OutputType
  {
    PDF, EXCEL, HTML
  }

  /**
   * Performs the basic initialization required to generate a report
   */
  public AbstractReportGenerator()
  {
    // Initialize the reporting engine
    ClassicEngineBoot.getInstance().start();
  }

  /**
   * Returns the report definition used by this report generator. If this method returns <code>null</code>,
   * the report generation process will throw a <code>NullPointerException</code>.
   *
   * @return the report definition used by thus report generator
   */
  public abstract MasterReport getReportDefinition();

  /**
   * Returns the data factory used by this report generator. If this method returns <code>null</code>,
   * the report generation process will use the data factory used in the report definition.
   *
   * @return the data factory used by this report generator
   */
  public abstract DataFactory getDataFactory();

  /**
   * Returns the set of parameters that will be passed to the report generation process. If there are no parameters
   * required for report generation, this method may return either an empty or a <code>null</code> <code>Map</code>
   *
   * @return the set of report parameters to be used by the report generation process, or <code>null</code> if no
   *         parameters are required.
   */
  public abstract Map<String, Object> getReportParameters();

  /**
   * Generates the report in the specified <code>outputType</code> and writes it into the specified
   * <code>outputFile</code>.
   *
   * @param outputType the output type of the report (HTML, PDF, HTML)
   * @param outputFile the file into which the report will be written
   * @throws IllegalArgumentException  indicates the required parameters were not provided
   * @throws IOException               indicates an error opening the file for writing
   * @throws ReportProcessingException indicates an error generating the report
   */
  public void generateReport(final OutputType outputType, File outputFile)
      throws IllegalArgumentException, IOException, ReportProcessingException
  {
    if (outputFile == null)
    {
      throw new IllegalArgumentException("The output file was not specified");
    }

    OutputStream outputStream = null;
    try
    {
      // Open the output stream
      outputStream = new BufferedOutputStream(new FileOutputStream(outputFile));

      // Generate the report to this output stream
      generateReport(outputType, outputStream);
    }
    finally
    {
      if (outputStream != null)
      {
        outputStream.close();
      }
    }
  }

  /**
   * Generates the report in the specified <code>outputType</code> and writes it into the specified
   * <code>outputStream</code>.
   * <p/>
   * It is the responsibility of the caller to close the <code>outputStream</code>
   * after this method is executed.
   *
   * @param outputType   the output type of the report (HTML, PDF, HTML)
   * @param outputStream the stream into which the report will be written
   * @throws IllegalArgumentException  indicates the required parameters were not provided
   * @throws ReportProcessingException indicates an error generating the report
   */
  public void generateReport(final OutputType outputType, OutputStream outputStream)
      throws IllegalArgumentException, ReportProcessingException
  {
    if (outputStream == null)
    {
      throw new IllegalArgumentException("The output stream was not specified");
    }

    // Get the report and data factory
    final MasterReport report = getReportDefinition();
    final DataFactory dataFactory = getDataFactory();

    // Set the data factory for the report
    if (dataFactory != null)
    {
      report.setDataFactory(dataFactory);
    }

    // Add any parameters to the report
    final Map<String, Object> reportParameters = getReportParameters();
    if (null != reportParameters)
    {
      for (String key : reportParameters.keySet())
      {
        report.getParameterValues().put(key, reportParameters.get(key));
      }
    }

    // Prepare to generate the report
    AbstractReportProcessor reportProcessor = null;
    try
    {
      // Greate the report processor for the specified output type
      switch (outputType)
      {
        case PDF:
        {
          final PdfOutputProcessor outputProcessor =
              new PdfOutputProcessor(report.getConfiguration(), outputStream, report.getResourceManager());
          reportProcessor = new PageableReportProcessor(report, outputProcessor);
          break;
        }

        case EXCEL:
        {
          final FlowExcelOutputProcessor target =
              new FlowExcelOutputProcessor(report.getConfiguration(), outputStream, report.getResourceManager());
          reportProcessor = new FlowReportProcessor(report, target);
          break;
        }

        case HTML:
        {
          final StreamRepository targetRepository = new StreamRepository(outputStream);
          final ContentLocation targetRoot = targetRepository.getRoot();
          final HtmlOutputProcessor outputProcessor = new StreamHtmlOutputProcessor(report.getConfiguration());
          final HtmlPrinter printer = new AllItemsHtmlPrinter(report.getResourceManager());
          printer.setContentWriter(targetRoot, new DefaultNameGenerator(targetRoot, "index", "html"));
          printer.setDataWriter(null, null);
          printer.setUrlRewriter(new FileSystemURLRewriter());
          outputProcessor.setPrinter(printer);
          reportProcessor = new StreamReportProcessor(report, outputProcessor);
          break;
        }
      }

      // Generate the report
      reportProcessor.processReport();
    }
    finally
    {
      if (reportProcessor != null)
      {
        reportProcessor.close();
      }
    }
  }
}
```

## Sample 1: Static report definition, JDBC input, PDF output

The simplest embedding scenario produces a static report (no user input regarding a data source or query), with JDBC input from the Pentaho-supplied SampleData HSQLDB database, and produces a PDF on the local filesystem.

```
/*
 * This program is free software; you can redistribute it and/or modify it under the 
 * terms of the GNU Lesser General Public License, version 2.1 as published by the Free Software 
 * Foundation.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this 
 * program; if not, you can obtain a copy at http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html 
 * or from the Free Software Foundation, Inc., 
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * Copyright 2009 Pentaho Corporation.  All rights reserved.
 *
 * Created July 22, 2009 
 * @author dkincade
 */
package org.pentaho.reporting.engine.classic.samples;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.Map;
import java.util.HashMap;

import org.pentaho.reporting.engine.classic.core.DataFactory;
import org.pentaho.reporting.engine.classic.core.MasterReport;
import org.pentaho.reporting.engine.classic.core.ReportProcessingException;
import org.pentaho.reporting.libraries.resourceloader.Resource;
import org.pentaho.reporting.libraries.resourceloader.ResourceException;
import org.pentaho.reporting.libraries.resourceloader.ResourceManager;

/**
 * Generates a report in the following scenario:
 * <ol>
 * <li>The report definition file is a .prpt file which will be loaded and parsed
 * <li>The data factory is a simple JDBC data factory using HSQLDB
 * <li>There are no runtime report parameters used
 * </ol>
 */
public class Sample1 extends AbstractReportGenerator
{
  /**
   * Default constructor for this sample report generator
   */
  public Sample1()
  {
  }

  /**
   * Returns the report definition which will be used to generate the report. In this case, the report will be
   * loaded and parsed from a file contained in this package.
   *
   * @return the loaded and parsed report definition to be used in report generation.
   */
  public MasterReport getReportDefinition()
  {
    try
    {
      // Using the classloader, get the URL to the reportDefinition file
      final ClassLoader classloader = this.getClass().getClassLoader();
      final URL reportDefinitionURL = classloader.getResource("org/pentaho/reporting/engine/classic/samples/Sample1.prpt");

      // Parse the report file
      final ResourceManager resourceManager = new ResourceManager();
      resourceManager.registerDefaults();
      final Resource directly = resourceManager.createDirectly(reportDefinitionURL, MasterReport.class);
      return (MasterReport) directly.getResource();
    }
    catch (ResourceException e)
    {
      e.printStackTrace();
    }
    return null;
  }

  /**
   * Returns the data factory which will be used to generate the data used during report generation. In this example,
   * we will return null since the data factory has been defined in the report definition.
   *
   * @return the data factory used with the report generator
   */
  public DataFactory getDataFactory()
  {
    return null;
  }

  /**
   * Returns the set of runtime report parameters. This sample report uses the following three parameters:
   * <ul>
   * <li><b>Report Title</b> - The title text on the top of the report</li>
   * <li><b>Customer Names</b> - an array of customer names to show in the report</li>
   * <li><b>Col Headers BG Color</b> - the background color for the column headers</li>
   * </ul>
   *
   * @return <code>null</code> indicating the report generator does not use any report parameters
   */
  public Map<String, Object> getReportParameters()
  {
    final Map parameters = new HashMap<String, Object>();
    parameters.put("Report Title", "Simple Embedded Report Example with Parameters");
    parameters.put("Col Headers BG Color", "yellow");
    parameters.put("Customer Names",
        new String [] {
            "American Souvenirs Inc",
            "Toys4GrownUps.com",
            "giftsbymail.co.uk",
            "BG&E Collectables",
            "Classic Gift Ideas, Inc",
        });
    return parameters;
  }

  /**
   * Simple command line application that will generate a PDF version of the report. In this report,
   * the report definition has already been created with the Pentaho Report Designer application and
   * it located in the same package as this class. The data query is located in that report definition
   * as well, and there are a few report-modifying parameters that will be passed to the engine at runtime.
   * <p/>
   * The output of this report will be a PDF file located in the current directory and will be named
   * <code>SimpleReportGeneratorExample.pdf</code>. 
   *
   * @param args none
   * @throws IOException indicates an error writing to the filesystem
   * @throws ReportProcessingException indicates an error generating the report
   */
  public static void main(String[] args) throws IOException, ReportProcessingException
  {
    // Create an output filename
    final File outputFilename = new File(Sample1.class.getSimpleName() + ".pdf");

    // Generate the report
    new Sample1().generateReport(AbstractReportGenerator.OutputType.PDF, outputFilename);

    // Output the location of the file
    System.err.println("Generated the report [" + outputFilename.getAbsolutePath() + "]");
  }
}
```

## Sample 2: Static report definition, JDBC input, HTML output

This example produces a static report (no user input regarding a data source or query), with JDBC input from the Pentaho-supplied SampleData HSQLDB database, and produces an HTML file on the local filesystem.

```
/*
 * This program is free software; you can redistribute it and/or modify it under the 
 * terms of the GNU Lesser General Public License, version 2.1 as published by the Free Software 
 * Foundation.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this 
 * program; if not, you can obtain a copy at http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html 
 * or from the Free Software Foundation, Inc., 
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * Copyright 2009 Pentaho Corporation.  All rights reserved.
 *
 * Created July 22, 2009 
 * @author dkincade
 */
package org.pentaho.reporting.engine.classic.samples;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import org.pentaho.reporting.engine.classic.core.DataFactory;
import org.pentaho.reporting.engine.classic.core.MasterReport;
import org.pentaho.reporting.engine.classic.core.ReportProcessingException;
import org.pentaho.reporting.engine.classic.core.PageDefinition;
import org.pentaho.reporting.engine.classic.core.wizard.&#8203;RelationalAutoGeneratorPreProcessor;
import org.pentaho.reporting.engine.classic.core.modules.&#8203;misc.datafactory.sql.SQLReportDataFactory;
import org.pentaho.reporting.engine.classic.core.modules.&#8203;misc.datafactory.sql.DriverConnectionProvider;

/**
 * Generates a report in the following scenario:
 * &lt;ol>
 * &lt;li>The report definition file is a .prpt file which will be loaded and parsed
 * &lt;li>The data factory is a simple JDBC data factory using HSQLDB
 * &lt;li>There are no runtime report parameters used
 * &lt;/ol>
 */
public class Sample2 extends AbstractReportGenerator
{
  private static final String QUERY_NAME = "ReportQuery";

  /**
   * Default constructor for this sample report generator
   */
  public Sample2()
  {
  }

  /**
   * Returns the report definition which will be used to generate the report. In this case, the report will be
   * loaded and parsed from a file contained in this package.
   *
   * @return the loaded and parsed report definition to be used in report generation.
   */
  public MasterReport getReportDefinition()
  {
    final MasterReport report = new MasterReport();
    report.setQuery(QUERY_NAME);
    report.addPreProcessor(new RelationalAutoGeneratorPreProcessor());
    return report;
  }

  /**
   * Returns the data factory which will be used to generate the data used during report generation. In this example,
   * we will return null since the data factory has been defined in the report definition.
   *
   * @return the data factory used with the report generator
   */
  public DataFactory getDataFactory()
  {
    final DriverConnectionProvider sampleDriverConnectionProvider = new DriverConnectionProvider();
    sampleDriverConnectionProvider.setDriver("org.hsqldb.jdbcDriver");
    sampleDriverConnectionProvider.setUrl("jdbc:hsqldb:./sql/sampledata");
    sampleDriverConnectionProvider.setProperty("user", "sa");
    sampleDriverConnectionProvider.setProperty("password", "");

    final SQLReportDataFactory dataFactory = new SQLReportDataFactory(sampleDriverConnectionProvider);
    dataFactory.setQuery(QUERY_NAME,
        "select CUSTOMERNAME, CITY, STATE, POSTALCODE, COUNTRY from CUSTOMERS order by UPPER(CUSTOMERNAME)");

    return dataFactory;
  }

  /**
   * Returns the set of runtime report parameters. This sample report does not use report parameters, so the
   * method will return &lt;code>null&lt;/code>
   *
   * @return &lt;code>null&lt;/code> indicating the report generator does not use any report parameters
   */
  public Map&lt;String, Object> getReportParameters()
  {
    return null;
  }

  public static void main(String[] args) throws IOException, ReportProcessingException
  {
    // Create an output filename
    final File outputFilename = new File(Sample2.class.getSimpleName() + ".html");

    // Generate the report
    new Sample2().generateReport(AbstractReportGenerator.OutputType.HTML, outputFilename);

    // Output the location of the file
    System.err.println("Generated the report [" + outputFilename.getAbsolutePath() + "]");
  }
}
```
