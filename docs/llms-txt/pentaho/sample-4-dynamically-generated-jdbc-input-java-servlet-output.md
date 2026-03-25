# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/advanced-topics/sample-4-dynamically-generated-jdbc-input-java-servlet-output.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/advanced-topics/sample-4-dynamically-generated-jdbc-input-java-servlet-output.md

# Sample 4: Dynamically generated, JDBC input, Java servlet output

This example assumes you have a Java application server, such as Tomcat, installed, configured, running, and accessible to you.

`Sample4.java` is an HttpServlet which generates an HTML report similar to Sample2 (dynamically created report definition based on the data set, a static data set, and no parameters). In the `generateReport(…)` method, the report is generates as HTML into an output stream which is routed directly to the browser. As noted in the comments of this method, a small simple change can be made to generate PDF output instead of HTML output.

To execute Sample4, the following steps will deploy and run it using Tomcat:

1. Copy `Sample4.war` into the `webapps` directory of a working Tomcat instance
2. Start the Tomcat server (`bin/startup.sh` or `bin\startup.bat`)
3. In a browser, navigate to the following URL: `http://localhost:8080/Sample4/`

```java
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

import java.io.IOException;
import java.io.OutputStream;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.swing.table.AbstractTableModel;

import org.pentaho.reporting.engine.classic.core.ClassicEngineBoot;
import org.pentaho.reporting.engine.classic.core.MasterReport;
import org.pentaho.reporting.engine.classic.core.PageDefinition;
import org.pentaho.reporting.engine.classic.core.ReportProcessingException;
import org.pentaho.reporting.engine.classic.core.TableDataFactory;
import org.pentaho.reporting.engine.classic.core.modules.​output.table.html.HtmlReportUtil;
import org.pentaho.reporting.engine.classic.core.wizard.​RelationalAutoGeneratorPreProcessor;

/**
 * Servlet implementation which generates a report and returns the report as an HTML
 * stream back to the browser. 
 */
public class Sample4 extends HttpServlet
{
  /**
   * Default constructor for this sample servlet
   */
  public Sample4()
  {
  }
  
  /**
   * Initializes the servlet - we need to make sure the reporting engine has been initialized
   */
  public void init()
  {
    // Initialize the reporting engine
    ClassicEngineBoot.getInstance().start();
  }

  /**
   * Handles the GET request. We will handle both the GET request and POST request the same way.
   */
  protected void doGet(final HttpServletRequest req, final HttpServletResponse resp) throws ServletException, IOException
  {
    generateReport(req, resp);
  }

  /**
   * Handles the POST request. We will handle both the GET request and POST request the same way.
   */
  protected void doPost(final HttpServletRequest req, final HttpServletResponse resp) throws ServletException, IOException
  {
    generateReport(req, resp);
  }

  /**
   * Generates a simple HTML report and returns the HTML output back to the browser
   */
  private void generateReport(final HttpServletRequest req, final HttpServletResponse resp) throws ServletException, IOException
  {
    // Generate the report definition
    final MasterReport report = createReportDefinition();
    
    // Run the report and save the HTML output to a byte stream
    resp.setContentType("text/html"); // Change to "application/pdf" for PDF output
    OutputStream out = resp.getOutputStream();
    try
    {
      // Use the HtmlReportUtil to generate the report to a Stream HTML
      HtmlReportUtil.createStreamHTML(report, out); 
      
      //NOTE: Changing this to use PDF is simple:
      // 1. Change the above setContent call to use "application/pdf"
      // 2. Instead of HtmlReportUtil, use the following line:
      // PdfReportUtil.createPDF(report, out)
    }
    catch (ReportProcessingException rpe)
    {
      rpe.printStackTrace();
    }
    finally
    {
      out.close();
    }
  }
  
  private MasterReport createReportDefinition()
  {
    // Create a report using the autogenerated fields
    final MasterReport report = new MasterReport();
    report.addPreProcessor(new RelationalAutoGeneratorPreProcessor());
    
    // Add the data factory to the report
    report.setDataFactory(new TableDataFactory("Sample4Query", new Sample4TableModel()));
    report.setQuery("Sample4Query");

    // return
    return report;
  }

  /**
   * The table model used for this sample.
   * <br/>
   * In a real situation, this would never happen (a JNDI datasource connected up to 
   * customer data would be more normal). But for a sample, some hard coded
   * data is to be expected.
   */
  private static class Sample4TableModel extends AbstractTableModel
  {
    /**
     * The sample data
     */
    private static final Object[][] data = new Object[][]
    { 
      new Object[] { "Acme Industries", 2500, 18.75 }, 
      new Object[] { "Brookstone Warehouses", 5000, 36.1245 }, 
      new Object[] { "Cartwell Restaurants", 18460, 12.9 }, 
      new Object[] { "Domino Builders", 20625, 45.52 }, 
      new Object[] { "Elephant Zoo Enclosures", 750, 19.222 }, 
    };

    /**
     * Returns the number of columns of data in the sample dataset
     */
    public int getColumnCount()
    {
      return data[0].length;
    }

    /**
     * Returns the number of rows in the sample data
     */
    public int getRowCount()
    {
      return data.length;
    }

    /**
     * Returns the data value at the specific row and column index
     */
    public Object getValueAt(int rowIndex, int columnIndex)
    {
      if (rowIndex >= 0 && rowIndex < data.length && columnIndex >= 0 && columnIndex < data[rowIndex].length)
      {
        return data[rowIndex][columnIndex];
      }
      return null;
    }

  }
}
```
