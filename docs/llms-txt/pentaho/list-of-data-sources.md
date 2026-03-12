# Source: https://docs.pentaho.com/pba-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/list-of-data-sources.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/list-of-data-sources.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/data-sources-perspective-ctools-cde/list-of-data-sources.md

# List of data sources

This is the list of all the available data sources, grouped in the left pane:

* [**Wizards** ](#wizards)**-** A setup assistant to guide you through the steps of creating an OLAP selector or chart.
* [**Community Data Access**](#community-data-access) **(CDA) -** CDA allows data to be retrieved from multiple data sources and combined in a single output which can easily be passed on to dashboard components.
* [**Legacy Datasources**](#legacy-datasources) **-** Legacy data sources include PDI/Kettle transformations, OLAP MDX queries, SQL queries, and Xaction result sets.
* [**Pentaho App Builder Endpoints**](#the-pentaho-app-builder-endpoints) **-** The PAB's internal Kettle transformations and jobs.
* [**MDX Queries**](#mdx-queries) **-** You can retrieve data from a Mondrian cube via an [MDX](http://mondrian.pentaho.org/documentation/mdx.php) query.
* [**OLAP4J Queries** ](#olap4j-queries)**-** These data sources execute queries using the olap4j specification.
* [**Compound Queries**](#compound-queries) **-** These queries allows you to combine the result of two distinct queries. Compound queries can be either `JOIN` or `UNION`.
* [**SCRIPTING Queries**](#scripting-queries) **-** Create ad hoc result sets for prototyping purposes using [Beanshell](http://www.beanshell.org/) scripts.
* [**KETTLE Queries**](#kettle-queries) **-** Define a Kettle transformation file to fetch data.
* [**MQL Queries**](#mdx-queries) **-** Pentaho Metadata defines a business model and query implementation so business users can query data sources using Pentaho reporting tools.
* [**SQL Queries**](#sql-queries) **-** Use this type of data source to access data from SQL databases if you have a JNDI connection or a JDBC driver setup.
* [**XPATH Queries**](#xpath-queries) **-** Provides the ability to read data from any type of XML file using XPath specifications.

## Wizards

These wizards can be used to create either a selector or a chart by setting a few properties. You can use the following types of wizards:

* OLAP Selector wizard
* OLAP Chart wizard
* Saiku OLAP Wizard

Using the configuration pane, you can select an MDX Cube, and from that cube you can select measures and metrics to generate a result set which you want to display in a selector or chart. The configuration pane features a preview area where you can view how your chart or selector will work.

![OLAP Wizard](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-487b32f73a76e98f6c4f1957d285717d9e545564%2FolapSelectorWizard.png?alt=media)

There are specific settings which can be set for either the selector or the chart wizard. The selector wizard allows you pick from select, radio box, or multiple selector options whereas the chart wizard provides selection options for bar, pie, line, and dot charts. After setting your options, clicking **Ok** adds a `mdx over mondrianJndi` data source to the **Datasources** pane.

![The mdx over mondrainjndi data source](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-1f2e08b92a04b9058fa0803dd1543ef2cc8c6591%2FfocusOlapSelectorWizardHighlight.png?alt=media)

The wizard creates this data source, setting all the necessary parameters as well as the query for the data source to properly execute. The selector wizard also creates a parameter and a select component from the selections we made in the wizard, in the **Components** pane on the Components perspective.

![Selected data sources in Components pane](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-214703969ab3574f14c0f301108a072c05f06345%2FfocusComponentsOlapWizard.png?alt=media)

When creating a chart using the OLAP Chart wizard, a chart component is generated rather than the OLAP parameter and select component.

![Data source for OLAP Chart wizard](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-4b06a8e1ba550c404a449c6d43f1b89e543b51fb%2FolapChartWizardFocusChart.png?alt=media)

## Community Data Access

CDA allows you to access any of the many Pentaho data sources as well as allowing you to join different data sources just by editing an XML file, caching queries to boost performance, or delivering data in different file formats, such as CSV and XLS, through the Pentaho User Console. These tasks can be accomplished by selecting a CDA data source in this category.

## Legacy Datasources

The following options are available under this heading:

* **Kettle transformation**

  This data source executes a PDI (Kettle) transformation. Theoretically, you can get data from any source through a Kettle transformation, such as from plain files, Excel spreadsheets, and web services. To access data from Kettle, you will need to provide the name and location of the KTR file and the name of the transformation step which will provide the data. You will also need to define a **kettle.TransFromFile** connection.

  ![PDI (Kettle) properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-e9b1b4d3345b61368302bca14605ac786a199f80%2FkettleTransformProperties.png?alt=media)
* **OLAP MDX query**

  This data source executes an MDX query when you provide the JNDI connection string, the Mondrian schema, Mondrian cube, and the MDX query itself.

  ![OLAP MDX properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-7d77303d75eba43618e911fbf5413fddbfb6e2e9%2FolapMdxQueryProperties.png?alt=media)
* **SQL query**

  This data source executes a SQL query when you provide the JNDI connection string and the SQL query.

  ![SQL query properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-bc2358ded3e19c78e1d8bdaca2430d560794df5c%2FsqlQueryProperties.png?alt=media)
* **XAction result set**

  This data source retrieves a result set returned from an `Xaction` call to the Pentaho Server when you provide the location, path, parameters, and name of the `Xaction` you wish to execute.

  ![XAction properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-b8f0440d8daeb402aaaecec4018ac3ca36fdf816%2FxActionResultsetProperties.png?alt=media)

## The Pentaho App Builder endpoints

Pentaho App Builder (previously known as SPARKL) is a Community Plugin Kickstarter (CPK) plugin which allows you to easily build other CPK plugins. Kettle transformations or jobs of a CPK plugin are automatically exposed as rest endpoints. While you can view these endpoints in CDE, they are internal to Pentaho App Builder and are not necessary when developing dashboards.

## MDX Queries

You can fetch data from a Mondrian cube through an [MDX](http://mondrian.pentaho.org/documentation/mdx.php) query. To access the data through a Mondrian cube, provide the JNDI or JDBC connection properties, the name of the Mondrian schema file (XML), and the MDX query which will return the data. There are four types of MDX data sources:

* denormalizedMdx over mondrianJdbc
* denormalizedMdx over mondrianJndi
* mdx over mondrianJdbc
* mdx over mondrianJndi

MDX queries can be normalized or denormalized. The specifics of each type of query are detailed in the CDA documentation.

## OLAP4J Queries

These data sources execute queries using the olap4j specification, which is an open Java API for accessing OLAP data. This type of data source can be denormalizedOlap4j over olap4j or olap4j over olap4j.

As with the MDX queries, OLAP4J queries can be normalized or denormalized.

## Compound Queries

This type of query allows you to combine the result of two distinct queries. Compound queries can be one of two types, `JOIN` and `UNION`.

A `JOIN` compound query merges the result of two queries, using a specified set of keys. You can specify one of four join types: Inner, Left Outer, Right Outer, Full Outer. The result of this join will contain the columns of both queries if they are of the same type. Both the left and right side queries must be identified by an ID. You must also specify which keys (column IDs on the source queries) are used to join the data. This data source has the following properties:

| Property               | Description                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**               | The name of the compound query.                                                                                                                                                                                                                                                                                  |
| **Left**               | The first query.                                                                                                                                                                                                                                                                                                 |
| **Right**              | The second query.                                                                                                                                                                                                                                                                                                |
| **Parameters**         | Lists the parameters' name, default value (i.e., the default value if the parameter value is not specified when the data access is called), and type (String, Integer, Numeric, Date, StringArray, IntegerArray, NumericArray, and DateArray) which are passed on to the compound query.                         |
| **Calculated Columns** | The columns to be calculated by a given formula. Each calculated column requires two properties: **Name** (the name that will be output by CDA), and **Formula** (the column's definition itself). Formulas are written in [Open Formula](http://wiki.pentaho.com/display/Reporting/Formula+Expressions) format. |
| **Columns**            | Names of the columns, in case you want to rename a particular column.                                                                                                                                                                                                                                            |
| **Left Keys**          | The ID or IDs of the columns from the first query which are common to the second query.                                                                                                                                                                                                                          |
| **Output Columns**     | The IDs of the columns which will be the output from both queries in order, starting with the columns from the left query and then the columns from the right query.                                                                                                                                             |
| **Output Mode**        | The column's output mode, which will include or exclude the columns set above.                                                                                                                                                                                                                                   |
| **Right Keys**         | The ID or IDs of the columns from the second query which are common to the first query.                                                                                                                                                                                                                          |
| **Join Type**          | The join type to be used, such as Inner, Left Outer, Right Outer, or Full Outer.                                                                                                                                                                                                                                 |

A `UNION` compound query takes the results of two queries with the same number of columns and returns the compounded result set from both queries. A union query data source has the following properties:

| Property               | Description                                                                                                                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**               | The name of the compound query.                                                                                                                                                                                                                                                                                 |
| **Top**                | The ID of the query which will stay on top.                                                                                                                                                                                                                                                                     |
| **Bottom**             | The ID of the query which will stay on the bottom.                                                                                                                                                                                                                                                              |
| **Parameters**         | Lists the parameter's name, default value (i.e., the default value if the parameter value is not specified when the data access is called) and type (String, Integer, Numeric, Date, StringArray, IntegerArray, NumericArray, and DateArray) which are passed on to the compound query.                         |
| **Calculated Columns** | The columns to be calculated by a given formula. Each calculated column requires two properties: **Name** (the name that will be output by CDA), and **Formula** (the column's definition itself). Formulas are written in [Open Formula](http://wiki.pentaho.com/display/Reporting/Formula+Expressions)format. |
| **Columns**            | Names of the columns, in case you want to rename a particular column.                                                                                                                                                                                                                                           |

If the columns on both data sets have different names, the name of the column in the top result set will be used in the union’s resulting data set.

## SCRIPTING Queries

These data sources allow you to create ad hoc result sets, such as a small table, for prototyping purposes using [Beanshell](http://www.beanshell.org/) scripts. These result sets are useful during the dashboard development phase for generating data for a dashboard’s components when real data is not yet available. This data source can be one of two types:

* **scriptable over scripting**

  Using the Beanshell scripting language, we can define a data structure and then create a result set based on this same structure to use in a component. You will need to define the column names, column types, and the result set rows.

  ```java
  import org.pentaho.reporting.engine.classic.core.util.TypedTableModel;
  String[] columnNames = new String[]{
      "value","name2"
  };
  Class[] columnTypes = new Class[]{
      Integer.class,
      String.class
  };
  TypedTableModel model = new TypedTableModel(columnNames, columnTypes);
  model.addRow(new Object[]{ new Integer("0"), new String("Name") });
  return model;
  ```
* **JSONscriptable over scripting**

  This data source is similar to the scriptable data source in that it uses Beanshell script to generate a result set. However, rather than specifying the column names and column types, you just need to define the metadata and create the result set you want to use. This is simple and less prone to bugs than using the scriptable data source.

  ```javascript
  {
    "resultset":[
          ["Name", 0]
    ],
    "metadata":[
      {"colIndex":0,"colType":"String","colName":"value"},
      {"colIndex":1,"colType":"Integer","colName":"name2"}
    ]
  }
  ```

## KETTLE Queries

Using Pentaho Data Integration transformations, you can fetch data from virtually any data source such as plain text files, Excel spreadsheets, and web services.

* **kettle over kettleTransFromFile**

  To access data from Kettle, you will need to define the Kettle transformation file (KTR) you want to use and the name of the transformation step which will provide the data. You can also pass parameters and variables to the KTR transformation to filter the data.

  ![Kettle transformation file properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-b84b0692e710e4c708f0573caa2431a847f6797c%2FkettleOverKettleTransFromFileProperties.png?alt=media)

## MQL Queries

Pentaho Metadata defines a business model and query implementation which makes it easy for business users to query data sources in Pentaho tools such as Report Designer and Ad Hoc Reporting. This metadata can be accessed through a [MQL](http://wiki.pentaho.com/display/COM/The+Pentaho+Metadata+Project) query. MQL is the syntax Pentaho Metadata uses for generating SQL queries based on metadata.

* **mql over metadata**

  To access the data, provide the name and location of the metadata domain file (XMI) and the domain where the data belongs.

## SQL Queries

Use this type of data source to access data from SQL databases provided you have a JNDI connection or a JDBC driver setup. You can access a SQL database by defining the connection and providing the query to be executed.

* **sql over sqlJdbc**

  Besides specifying the query to be used, you also need to specify the information needed to access the data such as the driver, user name and password of a user with access to the data.

  ![The sql over sqlJdbc properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-4b80598705329b76e040e67de129f1f5da46747d%2FsqlOverJdbcProperties.png?alt=media)
* **sql over sqlJndi**

  This type of data source employs the Java Naming and Directory Interface (JNDI) which allows software clients to discover and look up data and object via a name, in this case a SQL database. To set up this type of data source you just need to specify the JNDI identifier and the query to be used.

  ![The sql over sqlJndi properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-f8f95d785e2548243f01c282d174703420dc7c4e%2FsqlOverJndiProperties.png?alt=media)

## XPATH Queries

This data source provides the ability to read data from any type of XML file using XPath specifications.

* **xPath over xPath**

  You need to provide a query as well as the path to the data file on which to apply the xPath query.

  ![The xPath over xPath properties](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-c1141491f0144f8ea1d0614b5f74974f3cc220f7%2FxpathOverXpathProperties.png?alt=media)
