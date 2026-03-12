# Source: https://docs.pentaho.com/pdia-try-pdia/about-pentaho-workflows.md

# About Pentaho workflows

The route that you take with Pentaho depends on your expertise, business needs, and data. It also depends on what you want to analyze and report. During an evaluation, you might use both tracks.

All of the products are integrated to work smoothly together, regardless of which track you ultimately choose. We provide specific details within the workflow discussions, however, here are the high-level use cases for each track.

* Business Analytics (BA) Track: Great for analysis and reporting. Meant primarily for business users and does not require special skills to successfully use the components involved. This track enables anyone to build Pentaho solutions without using programming or having deep understanding of data structures.
* Data Integration (DI) Track: Meant for data design professionals and requires a working knowledge of data structures and modeling, as well as extract, transform, and load (ETL) processes. With this track, you can directly manipulate data from multiple sources, making it scalable and efficient for enterprise-wide analysis and reporting.

Each track has three workflows: one for Evaluation, one for Development, and one for Production.

* Evaluate and Learn: If you used the trial download on the Pentaho website and want to get a hands-on feel for the components that are best for your implementation, follow the Evaluation Workflow.
* Develop Pentaho Solutions: After you have figured out which components are best for you and how to use them, the Develop Workflow is the process you use to build, change, and test Pentaho solutions until they meet your production requirements.
* Go Live for Production: When your solution is working just right, the Go Live Workflow shows how to move your solution from development to production.

### In this topic

* [Prepare for the evaluation](#prepare-for-the-evaluation)
* [Pentaho Data Integration workflows](#pentaho-data-integration-workflows)
* [Pentaho Business Analytics workflow](#pentaho-business-analytics-workflow)

### Prepare for the evaluation

This table guides you through the differences between the Business Analytics and Data Integration tracks. It also helps you decide which track to follow for evaluation. You may choose to follow one track, then the other, while you are exploring the software.

| Explore Considerations                                                                                                                        | Choose Options                                                                                                                                                                |                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Business Analytics Evaluation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/evaluate-and-learn-pentaho-business-analytics) | [Data Integration Evaluation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/evaluate-and-learn-pentaho-data-integration-pdi)                                 |                                                                                                                                                                                       |
| Expertise                                                                                                                                     | <ul><li>No special skills required</li><li>Knowledge of business requirements and what reports and analysis should show</li></ul>                                             | <ul><li>Knowledge of business requirements</li><li>Understanding of data structures and modeling</li><li>Knowledge of extract, transform, and load (ETL) processes</li></ul>          |
| Data Set Description                                                                                                                          | <ul><li>Single source of data</li><li>Data from multiple sources that have been transformed and joined into a single data mart or warehouse</li><li>Small data sets</li></ul> | <ul><li>Multiple sources of data</li><li>Data you want to transform and join in one or more data marts or warehouses</li><li>Large to enormously vast data sets</li></ul>             |
| Reporting Options                                                                                                                             | Offers a wide variety of visualization and reporting options.                                                                                                                 | Offers more limited but focused reporting options that help you visualize and analyze data. BA tools can be used to generate reports based on DI-processed data.                      |
| Data Storage Types                                                                                                                            | <ul><li>Relational databases</li><li>CSV data sources</li><li>SQL queries</li></ul>                                                                                           | <ul><li>Relational databases</li><li>NoSQL or Hadoop databases</li><li>Big data of any types</li><li>Data from a web service</li></ul>                                                |
| Recommendation                                                                                                                                | Best used by business analysts, managers, report designers, individual business units within an organization or enterprise                                                    | Best used by data scientists, data modelers, data integration and ETL developers, individual business units within an organization or enterprise, and enterprise-wide implementations |

Now that you have an idea of which track you want to follow for evaluation, choose an evaluation method. This decision table explains the different options for evaluation so you can pick the option that works best for you.

| Explore Considerations                            | Choose Options                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Hosted Demo](http://www.pentaho.com/hosted-demo) | [Custom Prototype](http://www.pentaho.com/helpmeout)                                                                                                                                                                                                                                                                                                                                                     | [Trial Download](http://www.pentaho.com/download)                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                           |
| Track                                             | Business Analytics                                                                                                                                                                                                                                                                                                                                                                                       | Business Analytics or Data Integration                                                                                                                                                                                                                                                                                                     | Business Analytics or Data Integration                                                                                                                                                                                                                                                                                                                                                    |
| Summary                                           | A cloud-based, hands-on, interactive exploration of Business Analytics reports, analysis, visualizations, and dashboards. Here you can see how easy and fun it can be to use Pentaho.                                                                                                                                                                                                                    | Work with Pentaho analysts and data integration specialists to plan and build a complimentary custom prototype that illustrates what Pentaho can do with your data. A representative will guide you through the entire process.                                                                                                            | Using our trial software, tutorials, and documentation, install and configure your own work environment. Then, build a prototype to get a complete Pentaho experience from installation and administration, through creating your first data models and build reports, analysis, dashboards, and data integration ETL transformations.                                                    |
| Data Source                                       | Pentaho sample data in CSV format                                                                                                                                                                                                                                                                                                                                                                        | Your sample data, including a range of typical data characteristics in CSV format.                                                                                                                                                                                                                                                         | Your sample data, including a range of typical data characteristics in the format that you commonly use                                                                                                                                                                                                                                                                                   |
| Hardware/Software Requirements                    | Web browser                                                                                                                                                                                                                                                                                                                                                                                              | Varies, depending on your requirements.                                                                                                                                                                                                                                                                                                    | One computer that meets the server requirements stated in the [Components Reference](https://docs.pentaho.com/pdia-try-pdia/components-reference).                                                                                                                                                                                                                                        |
| Recommendation                                    | <p>Any evaluator who wants an overview of Business Analytics features.</p><ul><li>Recommended for business analysts and report designers.</li></ul><p>We recommend that you try out the <a href="http://www.pentaho.com/resources/events/20121109-analytics-accelerator-program/">Custom Prototype</a> or <a href="http://www.pentaho.com/download">Trial Download</a> after you do the hosted demo.</p> | <p>All evaluators, particularly any big data or Data Integration evaluators.</p><ul><li>Recommended for evaluators who want to <a href="http://www.pentaho.com/accelerator-program">explore Business Analytics and Data Integration features</a> using a subset of their own data.</li><li>Limited to first-time customers only.</li></ul> | <p>Any evaluator who wants to independently work with Business Analytics, Data Integration tools, and big data. - Recommended for evaluators who want to explore Business Analytics and Data Integration features using their own data.</p><ul><li><a href="http://www.pentaho.com/service/technical-support">Technical support</a> is available to help if you have questions.</li></ul> |

### Pentaho Data Integration workflows

Pentaho Data Integration is a robust extract, transform, and load (ETL) tool that you can use to integrate, manipulate, and visualize your data. You can use PDI to import, transform, and export data from multiple data sources, including flat files, relational databases, Hadoop, NoSQL databases, analytic databases, social media streams, and operational stores. You can also use PDI to clean and enrich the data, move data between databases, and to visualize your data.

#### In this topic

* [Evaluate and learn PDI](#evaluate-and-learn-pdi)
* [Develop your PDI solution](#develop-your-pdi-solution)
* [Go Live for production - DI](#go-live-for-production---di)
* [Commonly used PDI steps and entries](#commonly-used-pdi-steps-and-entries)

#### Evaluate and learn PDI

As you explore Pentaho Data Integration (PDI), you will be introduced to the major components, watch videos, work through hands-on examples, and read about the different features.

Review the documentation and contact Pentaho [sales support](https://www.pentaho.com/services) if you have questions.

**PDI basics**

This section familiarizes you with PDI and introduces you to basic terminology and concepts. Then, you learn how to start and configure Spoon and take a spin through the interface.

* Get a basic understanding of what PDI does.
* View a video that explains how PDI fits into the [Business Analytics Platform](http://www.youtube.com/watch?v=hCMtrLCsBuE).
* Read about Pentaho Data Integration architecture in the **Pentaho Data Integration** document.

**Get acquainted with the PDI client**

Spoon is the PDI design tool. In this section you will set up Spoon, take a tour of the Spoon interface, and learn about the different Spoon perspectives.

* Check out the [hardware and software requirements](https://docs.pentaho.com/pdia-try-pdia/components-reference) for PDI.
* [Download trial version](http://www.pentaho.com/download) of the Pentaho Suite and install the software. (The platform includes PDI.)
* Learn how to install PDI only. See [Custom installation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/custom-installation) for details.
* Configure the Pentaho Server. Depending on your platform, see [Increase Pentaho Server memory limit for installations on Linux](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Increase%20Pentaho%20Server%20memory%20limit%20for%20installations%20on%20Linux=GUID-EBDD031B-404B-4E8C-B48E-75AC258CDF52=3=en=.md) or [Increase Pentaho Server memory limit for installations on Windows](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/increase-pentaho-server-memory-limit-for-installations-on-windows) for details.
* Start the Pentaho Server. Depending on your platform, see [Start and stop the Pentaho Server for configuration on Linux](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Start%20and%20stop%20the%20Pentaho%20Server%20for%20configuration%20on%20Linux=GUID-2AF5899D-DD81-4F5E-B884-BA998F6DBC2A=1=en=.md) or [Start and stop the Pentaho Server for configuration on Windows](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/start-and-stop-the-pentaho-server-for-configuration-on-windows) for details.
* Access the PDI client. See the **Pentaho Data Integration** document for details.
* Tour the PDI client perspectives. See the **Pentaho Data Integration** document for details.
* Read about terminology and basic concepts in the **Pentaho Data Integration** document.

**Build transformations and jobs**

Now that your environment is set up and you are familiar with the PDI client, you are ready to build transformations and jobs. Trying the following task may be helpful.

* Create a connection to the Pentaho Repository.
* Work through the exercise on [Creating a Transformation](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pdi-transformation-tutorial) that involves a flat file. Click through the links at the bottom of the page to complete the exercise.
* Create a job to execute the transformation.
* Schedule a job to execute the transformation at a later time.
* Review [commonly used steps and job entries](#commonly-used-pdi-steps-and-entries).

**Explore Big Data and Streamlined Data Refinery**

In this section, you will learn how to use transformation steps to connect to a variety of big data sources, including Hadoop, NoSQL, and analytical databases such as MongoDB. You can then try working through the detailed, step-by-step tutorials, and peruse the out-of-the-box steps that Spoon provides. Learn how to work with Streamlined Data Refinery. Then, you will have an opportunity to move beyond the basics and learn how to edit transformations and metadata models.

* Watch one of our [Big Data Videos](http://www.youtube.com/watch?v=vOMOFPMnXgk).
* Learn how to work with Streamlined Data Refinery. See **Pentaho Data Integration** for details.
* Learn how to auto model using the Build Model. See **Pentaho Data Integration** for details. job entry and how this feature intersects with Analyzer.
* Find out what big data steps are available out-of-the-box. See [Commonly used PDI steps and entries](#commonly-used-pdi-steps-and-entries) for details.
* Find out which Hadoop distributions are available and how to configure them. See [Pentaho, big data, and Hadoop](https://docs.pentaho.com/pdia-try-pdia/pentaho-big-data-and-hadoop) for details.

  **Note:** You should already have a cluster set up to perform this task.
* Edit transformations and metadata models. See **Pentaho Data Integration** for details.
* Watch a video about how to use PDI to [blend Big Data](http://www.youtube.com/watch?v=JyypUdwySrQ).

**About Kitchen, Pan, and Carte**

Kitchen, Pan, and Carte are command line tools for executing transformations and jobs modeled in the PDI client.

* Use Pan and Kitchen command line tools to work with transformations and jobs
* Use Carte clusters to:
  * Run transformations and jobs on a Carte cluster.
  * Schedule jobs to run on a remote Carte server.
  * Start or stop Carte from the command line interface or a URL.
  * Run transformations and jobs from the repository on the Carte server

See the **Pentaho Data Integration** document for details on Kitchen, Pan, and Carte.

**Learn more**

Now that you have completed an initial evaluation of PDI, dig a little deeper. Find out how to:

* Use newer steps and entries, like Spark Submit. See the **Pentaho Data Integration** document for details.
* Read about how to turn a transformation into a data service. See the **Pentaho Data Integration** document for details.
* Use the ETL Metadata Injection step. See the **Pentaho Data Integration** document for details.
* Check out our **What's New** document.
* Create other Data Integration solutions. See the **Pentaho Data Integration** document for details.
* Administer PDI. See the administration documentation for details.
* Integrate with different security protocols, like Pentaho security, LDAP, MSAD, and Kerberos. See the administration documentation for details.
* Check out our developer center section in the administration documentation.

#### Develop your PDI solution

This workflow helps you to set up and configure the DI development and test environments, then build, test, and tune your Pentaho DI solution prototype. This process is similar to the trial download evaluation experience, except that you will be completely configuring the Pentaho Server for data integration and working with your own ETL developers.

If you need extra help, Pentaho [professional services](https://www.pentaho.com/services) is available. The end result is to learn DI implementation best practices and deploy your DI solution to a production server. Most development and testing for DI occurs in Spoon.

Before you begin developing your DI solution, we recommend that you attend Pentaho [training classes](http://www.pentaho.com/service/training) to learn how to install and configure the Pentaho Server, as well as how to develop data models.

This section is grouped into parts that will guide you during the development of your DI solution. These parts are iterative and you might bounce between them during development. For example, as you tune a job, you might find that although you have built a solution that produces the right results, it takes a long time to run. You might need to rebuild and test a transformation to improve efficiency, and then retest it.

**Design DI solution**

Design helps you think critically about the problem you want to solve and possible solutions. Consider these questions as you gather your requirements and design the solution.

* **Output**

  What does the overall solution look like? What questions are posing and how do you want the answers formatted?
* **Data Sources**

  What type(s) of data sources are you querying? Where are they located? How much data do you need to process? Are you using big data? Are you using relational or non-relational data sources? Will you have a target data source? If so, where are they located?
* **Content/Processing**

  What data quality issues do you have? How is the input data mapped to the output data? Where do you want to process the content, in PDI or in the data source? What hardware will you include in your development environment? Will you need one or more quality assurance test environments or production environments?

Also, consider templates or standards, naming conventions, and other requirements of your end users if you have them. Consider how you will back up your data as well.

**Set up a development environment**

Setting up the environment includes installing and configuring PDI on development computers, configuring clustering if needed, and connecting to data sources. If you have one or more quality assurance environments, you will need to set those up also.

| Task                                    | Do This                                                                                                                                                                                                                                                               | Objective                                                                                                                                            |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Verify System Requirements              | <p>Consult the following references to verify requirements:- <a href="components-reference">Components Reference</a></p><ul><li><a href="https://help.hitachivantara.com/Documentation/Pentaho/9.3/Setup/JDBC_drivers_reference">JDBC Drivers Reference</a></li></ul> | <ul><li>Acquire one or more servers that meet the requirements.</li><li>Obtain the correct drivers for your system.</li></ul>                        |
| Obtain Software and Install PDI         | <p>See the <strong>Install Pentaho Data Integration and Analytics</strong> document for following instructions:- Installing PDI</p><ul><li>Starting the Pentaho Server</li><li>Starting the PDI client (also known as Spoon)</li></ul>                                | <ul><li>Get the software from your Sales Support representative.</li><li>Install the software.</li><li>Start the Pentaho Server and Spoon.</li></ul> |
| Install licenses for the Pentaho Server | See the **Administer Pentaho Data Integration and Analytics** document for instructions on installing licenses.                                                                                                                                                       | <ul><li>Add all acquired Pentaho licenses.</li></ul>                                                                                                 |
| Connect to the Pentaho Repository       | See the **Pentaho Data Integration** for instructions on connecting to the Pentaho Repository.                                                                                                                                                                        | <ul><li>Connect to the Pentaho Repository.</li></ul>                                                                                                 |
| Apply Advanced Security (if needed)     | See the **Administer Pentaho Data Integration and Analytics** document for details on Advanced Security.                                                                                                                                                              | <ul><li>Determine whether you need to apply Advanced Security.</li></ul>                                                                             |

**Build and test solution**

During this step, you develop transformations, jobs, and models, then test what you have developed. You will tune the transformations, jobs, and models for optimal performance.

Development occurs in the PDI client design tool. The PDI client's streamlined design tightly couples the build and test activities so that you can easily perform them iteratively. The PDI client has perspectives to help you perform ETL and visualize data. The PDI client also provides a scheduling perspective that can be used to automate testing. Testing encompasses verifying the quality of transformations and jobs, reviewing visualizations, and debugging issues. One common method of testing is to include steps in a transformation or job that calculates hash totals, checksums, record counts, and so forth to determine whether data is being properly processed. You can also visualize your data in analyzer and report designer and review the results as you develop. This can not only help you find errors and issues with processing but can help you get a jump on user acceptance testing if you show these reports to your customers or business analysts to get early feedback.

One basic question is how you can determine the number of transformations and jobs needed, as well as the order in which they should be executed. A good rule of thumb is to create one transformation for each combination of source system and target tables. You can often identify combinations in your mapping documents. Once you have identified the number of transformations that you need, you can use the same process to determine that number of jobs that you need. When considering the order of execution for transformations and jobs, consider how referential integrity is enforced. Run target table transformations that have no dependencies first, then run transformations that depend on those tables, and so forth.

| Task                                     | Do This                                                                                                                    | Objective                                                                                                                                                                                         |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand the Basics                    | <ul><li>Read the overview of the PDI client process in the <strong>Pentaho Data Integration</strong> document.</li></ul>   | <ul><li>Review information about the process and perspectives.</li></ul>                                                                                                                          |
| Review most often used steps and entries | <ul><li>Review <a href="#commonly-used-pdi-steps-and-entries">commonly-used steps and entries</a>.</li></ul>               | <ul><li>Review available transformations and determine how you can use them for your solution.</li><li>Review job step references to identify which steps can be used in your solution.</li></ul> |
| Create and Run Transformations           | <ul><li>Create and run a transformation. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul> | <ul><li>Identify the transformations needed for your job and implement them.</li><li>Save transformation.</li><li>Run transformations locally.</li></ul>                                          |
| Create and Run a Job                     | <ul><li>Create and run a job. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul>            | <ul><li>Create a job.</li><li>Arrange transformations in a job so that they execute logically.</li><li>Run a job.</li></ul>                                                                       |

**Tune solution**

Fine tune transformations and jobs to optimize performance. This involves using various tools such as the DI Operation and Audit Mart to determine where bottlenecks or other performance issues occur, and addressing them.

| Task                                                                                 | Do This                                                                                                                                                                                                                                                                                             | Objective                                                                                                                     |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Review the Performance Tuning Checklist and Make Changes to Transformations and Jobs | <ul><li>Review tuning tips. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for tuning tips.</li></ul>                                                                                                                                                          | <ul><li>Get familiar with things that you can do to optimize performance.</li><li>Apply tuning tips as needed.</li></ul>      |
| Consider other performance tuning options                                            | <ul><li>Read about transactional databases. See the <strong>Pentaho Data Integration</strong> document for details on transactional databases.</li><li>Read about using logs. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for details on logging.</li></ul> | <ul><li>Learn how to apply transactional databases.</li><li>Learn how to use logs to tune transformations and jobs.</li></ul> |

**Next steps**

These resources will be helpful to you as you prepare to Go Live for Production:

* Prepare to [Go Live for Production - DI](#go-live-for-production---di).
* [Support Portal](https://support.pentaho.com/hc/en-us): check with Support for service packs.

#### Go Live for production - DI

Go Live is the process by which you migrate a prototype to production. This process is divided into four parts:

* Setting up the production environment
* Deploying the solution
* Tuning the solution
* Scheduling the runs

**Set up production environment**

Setting up the environment includes installing the software on production computers, configuring clustering, and connecting to data sources. To set up the environment, install and configure the Pentaho Server, Spoon, and any plugins required. Then set up data sources and clusters.

| Task                                           | Do This                                                                                                                                                                                                                                                                                                                                                                                       | Objective                                                                                                                                                                          |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Verify system requirements                     | <ul><li>Consult the <a href="components-reference">Components Reference</a>.</li><li>Consult the <a href="https://help.hitachivantara.com/Documentation/Pentaho/9.3/Setup/JDBC_drivers_reference">JDBC Drivers Reference</a>.</li></ul>                                                                                                                                                       | <ul><li>Acquire one or more servers that meet the requirements.</li><li>Obtain the correct drivers for your system.</li></ul>                                                      |
| Obtain software and install the Pentaho Server | <ul><li>Download the Pentaho software.</li><li>Start the Pentaho Server. See <strong>Install Pentaho Data Integration and Analytics</strong> for details.</li><li>Start the PDI client. See <strong>Pentaho Data Integration</strong> for details.</li><li>Install the licenses (if necessary). See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul> | <ul><li>Get the software from your Sales Support representative.</li><li>Install the software.</li></ul>                                                                           |
| Change the Server Fully Qualified URL          | <ul><li>Change the ports and URLs. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul>                                                                                                                                                                                                                                                              | <ul><li>Change the server's URL so that you do not have a conflict.</li></ul>                                                                                                      |
| Connect to the Pentaho Repository              | <ul><li>Create a connection to the Pentaho Repository. See <strong>Pentaho Data Integration</strong> for details.</li></ul>                                                                                                                                                                                                                                                                   | <ul><li>Connect to the Pentaho Repository.</li></ul>                                                                                                                               |
| Set up clusters                                | <ul><li>Optional: Set up clusters. See <strong>Pentaho Data Integration</strong> for details.</li></ul>                                                                                                                                                                                                                                                                                       | <ul><li>Become familiar with clustering.</li><li>Set up clusters, if they are needed in your environment.</li></ul>                                                                |
| Copy configuration files                       | Copy `shared.xml`, `repositories.xml`, `kettle.properties`, and JAR files from the development environment to the production environment.                                                                                                                                                                                                                                                     | <ul><li>System is set up and ready for production.</li></ul>                                                                                                                       |
| Logging and monitoring your server             | <ul><li>Review logging and monitoring operations. See <strong>Pentaho Data Integration</strong> for details.</li><li>Enable logging. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li><li>Monitor PDI and SNMP traps. See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</li></ul>                                    | <ul><li><p>Learn about the different ways to log and monitor Pentaho Server operations:</p><ul><li>Log through Spoon and Carte</li><li>Use SNMP traps with PDI</li></ul></li></ul> |

**Deploy solution**

Export solutions from the Pentaho Repository that is in the development or test environments, to the Pentaho Repository that is in the production environment.

| Task                                 | Do This                                                                                                                                                                 | Objective                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Export and Import Pentaho Repository | <ul><li>See <strong>Export and Import Pentaho Repository Content</strong> in the <strong>Administer Pentaho Data Integration and Analytics</strong> document.</li></ul> | <ul><li>Export Pentaho Repository content from test environment</li><li>Import Pentaho Repository content to production environment</li></ul> |

**Tune solution**

Fine tune transformations and jobs to optimize performance. This involves using various tools such as the DI Operations and Audit Marts to determine where bottlenecks or other performance issues occur, and attempting to address them.

| Task                                                                                 | Do This                                                                                                                                                                                                                                                                                               | Objective                                                                                                                     |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Review the Performance Tuning Checklist and Make Changes to Transformations and Jobs | <ul><li>Consult the tuning tips. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for tuning tips.</li></ul>                                                                                                                                                       | <ul><li>Get familiar with things that you can do to optimize performance.</li><li>Apply tuning tips as needed.</li></ul>      |
| Consider other performance tuning options                                            | <ul><li>Learn about transactional databases. See the <strong>Pentaho Data Integration</strong> document for details on transactional databases.</li><li>Learn about using logs. See the <strong>Administer Pentaho Data Integration and Analytics</strong> document for details on logging.</li></ul> | <ul><li>Learn how to apply transactional databases.</li><li>Learn how to use logs to tune transformations and jobs.</li></ul> |

**Schedule runs**

Use the PDI client, Pan, or Kitchen to schedule executions of transformations and jobs.

| Task                                           | Do This                                                                                                                                                                                                                             | Objective                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Schedule Transformations and Jobs From Spoon   | <ul><li>Schedule transformations and jobs. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul>                                                                                                        | <ul><li>Schedule transformations and jobs</li></ul>                         |
| Command Line Scripting Through Pan and Kitchen | <ul><li>Learn about Pan's options. See the <strong>Pentaho Data Integration</strong> document for details.</li><li>Learn about Kitchen's options. See the <strong>Pentaho Data Integration</strong> document for details.</li></ul> | <ul><li>Use Pan and Kitchen to schedule transformations and jobs.</li></ul> |

**Next steps**

These resources will be helpful to you after your production server is live.

* Fine-tune Pentaho systems: Provides guidance on how to maintain and fine-tune your Pentaho Server. See the **Administer Pentaho Data Integration and Analytics** document for details.
* Pentaho [Training and Education](https://www.hitachivantara.com/en-us/services/training-certification.html)
* [Support Portal](https://support.pentaho.com/hc/en-us): Check with support for service packs.

#### Commonly used PDI steps and entries

Although there are over 330 transformation steps and job entries, some steps and entries are used more often than others. If you are creating a transformation and job, but do not know where to begin, this list might be helpful to you.

**Top ten transformation steps**

PDI transformation steps are documented in Pentaho Data Integration.

* Text File Input
* Table Input
* Microsoft Excel Input
* Text File Output
* Table Output
* Microsoft Excel writer
* Select Values
* Filter Rows
* Group By
* Stream Lookup

**Other commonly used transformation steps**

PDI transformation steps are documented in Documentation

* INPUT: Generate Rows, Data Grid, Get Data from XML, CSV File Input, Fixed File Input
* OUTPUT: XML Output
* TRANSFORM: Split Fields, Calculator, Add Constants, Add Sequence, Replacing Strings, Split Fields, Sort Rows, String Operations, Strings Cut
* SCRIPTING: User Defined Java Class, Modified Java Script Value, User Defined Java Expression
* FLOW: Abort, Append Streams, Block this step until steps finish, Blocking Step, Detect Empty Stream, Dummy, ETL Metadata Injection, Filter Rows, Identify Last Row in a Stream, Java Filter, Job Executor, Prioritize Streams, Single Threader, Switch/Case, Transformation Executor
* LOOKUP
* JOINS: Join Rows, Merge Join
* JOB: Get Variables, Set Variables

**Commonly used job entries**

PDI job entries are documented in documentation.

* GENERAL: Start, Job, Transformation, Success
* UTILITY: Abort
* MAIL: Mail
* FILE MANAGEMENT: Add filenames to result, Compare folders, Convert file between Windows and Unix, Copy Files, Create a folder, Create file, Delete file, Delete filenames from result, Delete files, Delete folders, File Compare, HTTP, Move Files, Process result filenames, Unzip file, Wait for file, Write to file, Zip file
* UTILITIES: Write to log

### Pentaho Business Analytics workflow

Pentaho Business Analytics is a combined business analytics and data integration platform that allows business users, data scientists, and IT administrators to easily access, explore, and visualize their data. Pentaho empowers business users to make information-driven decisions that positively impact their organization’s performance, data scientists to use a full-spectrum of tools to create robust data models, and IT to rapidly deliver a secure, scalable, flexible, and easy to manage business analytics platform for the broadest set of users.

#### Workflow stages

Use these sections to move from evaluation to production:

* [Evaluate and learn Pentaho Business Analytics](#evaluate-and-learn-pentaho-business-analytics)
* [Develop your BA environment](#develop-your-ba-environment)
* [Go live for production - BA](#go-live-for-production---ba)

#### Evaluate and learn Pentaho Business Analytics

As you explore Pentaho Business Analytics, you will be introduced to the major components, watch videos, work through hands-on examples, and learn about the different features.

Go at your own pace. Feel free to dig into the documentation or to contact Pentaho [sales support](https://www.pentaho.com/services) if you have questions.

Use the sections below to get familiar with Business Analytics:

* [Tour the User Console and create your first reports](#tour-the-user-console-and-create-your-first-reports)
* [Explore and learn data source basics](#explore-and-learn-data-source-basics)
* [Learn about Report Designer](#learn-about-report-designer)
* [Discover more about Pentaho Business Analytics](#discover-more-about-pentaho-business-analytics)
* [Next steps](#next-steps-evaluation)

**Tour the User Console and create your first reports**

The User Console is a web-based design environment where you can analyze data, create interactive reports, dashboard reports, and build integrated dashboards to share business intelligence solutions with others in your organization and on the internet. In addition to its design features, the User Console offers a wide variety of system administration features for configuring the Pentaho Server, managing Pentaho licenses, setting up security, managing report scheduling, and tailoring system performance to meet your requirements.

If you have installed the trial download on your laptop or desktop machine, you are ready to get started exploring. If you have the software installed on a server, and want to use your machine to point to it, see [Develop your BA environment](#develop-your-ba-environment) for details.

| Lesson                                   | Do This                                                                                                                                                                                       | Notes                                                                                                                                               |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tour the User Console                    | [Quick tour of the Pentaho User Console](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/quick-tour-of-the-pentaho-user-console-puc)                                           | <ul><li>Understand the features of the User Console</li><li>View the sample reports on the Samples tab of the Getting Started section</li></ul>     |
| Create Your First Reports and Dashboards | [Getting Started with Analyzer, Interactive Reports, and Dashboard Designer](https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer) | <ul><li>Created and saved an Interactive Report</li><li>Created and saved an Analysis Report</li><li>Created and saved a custom Dashboard</li></ul> |
| Schedule Your Report                     | <ul><li>Learn about scheduling reports. See the <strong>Pentaho Business Analytics</strong> document for details.</li></ul>                                                                   | <ul><li>Scheduled a report to run and email automatically.</li><li>Received your report through email after the schedule runs.</li></ul>            |

**Explore and learn data source basics**

If you have already worked with the Steel Wheels sample data and want to learn how to create your own data sources and data models with Pentaho, use the Data Source Wizard. The Data Source Wizard helps you define a data source that contains the data you want to use and guides you through the creation of your evaluation data model for use in creating reports.

After you define a data source, you can make it available to other evaluators so they can create reports and analysis by simply picking the data source from the data source list. Any number of reports can be created using a single data source.

| Lesson                                | Do This                                                                                                                                            | Notes                                                                                                                                                                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create Your First Data Source         | <ul><li>Create a Data Source</li><li>Tour the Data Source Wizard</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p> | <ul><li>Understand how the Pentaho Server and Data Source Wizard work together to create usable data sources and data models.</li><li>Explore the Data Source Wizard interface.</li><li>Learn the basics of creating a data source using the Data Source Wizard.</li></ul> |
| Choose Data Source Types              | <ul><li>Choose a data source type</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                                | <ul><li>Learn about the different data source types supported by the Data Source Wizard.</li></ul><p>We recommend using a CSV data source for evaluation.</p>                                                                                                              |
| Create Your First CSV Data Source     | <ul><li>Create a CSV data source</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                                 | <ul><li>Import a CSV data file using the Data Source Wizard.</li><li>Create the CSV data source.</li></ul><p>We recommend creating a report using this new CSV data source, then refining the data model with the Data Source Model Editor as needed.</p>                  |
| Refine Your Data Source Model         | <ul><li>Edit multidimensional data source models.</li></ul><p>See <strong>Pentaho Business Analytics</strong> for instructions.</p>                | (Optional) Edit your evaluation data source model using the Data Source Model Editor.                                                                                                                                                                                      |
| Inline Model Editing                  | <ul><li>Read <strong>Working with Analyzer measures</strong> in the <strong>Pentaho Business Analytics</strong> document.</li></ul>                | <ul><li>Learn how to edit your data models while working in Analyzer.</li></ul>                                                                                                                                                                                            |
| Learn about Streamlined Data Refinery | <ul><li>Learn how to work with Streamlined Data Refinery</li></ul><p>See <strong>Pentaho Data Integration</strong> for instructions.</p>           | <ul><li>Learn how Streamlined Data Refinery works.</li></ul>                                                                                                                                                                                                               |

**Learn about Report Designer**

Pentaho Report Designer is a report creation tool that you can use by itself, or as part of the Pentaho Suite. It allows professionals to create print-quality reports based on data from virtually any type of data source.

These resources in the **Pentaho Report Designer** document will help you get familiar with the Report Designer interface, and guide you through the creation and publishing of a print-quality report.

| Lesson                                | Section in document                                                       | Notes                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Explore the Report Designer Interface | <ul><li><strong>Explore Report Designer</strong></li></ul>                | <ul><li>Tour the Report Designer interface before you begin building reports.</li></ul>                                          |
| Report Designer Workflow Overview     | <ul><li><strong>Learn about Report Designer workflow</strong></li></ul>   | <ul><li>Look over the workflow concepts for Report Designer.</li></ul>                                                           |
| Create Your First Report              | <ul><li><strong>Create your first print-quality report</strong></li></ul> | <ul><li>Create a report.</li><li>Add a chart and parameters to your report.</li><li>View and then publish your report.</li></ul> |
| Refine the Look of Your Report        | <ul><li><strong>Design print-quality reports</strong></li></ul>           | <ul><li>Explore more advanced features of Report Designer, beginning with report elements.</li></ul>                             |
| Add a PDI Data Source                 | <ul><li><strong>Add a PDI data source</strong></li></ul>                  | <ul><li>Add a PDI data source and use it to create a report in Report Designer.</li></ul>                                        |

**Discover more about Pentaho Business Analytics**

* The Pentaho Analyzer, Interactive Reports, and Dashboard Designer plugins provide in-depth details about creating eye-catching business intelligence deliverables for your user community. See the **Pentaho Business Analytics** document for details.
* If you are a system administrator, check out the **Install Pentaho Data Integration and Analytics** document. Both have details on configuring and administering your Pentaho Server using the User Console, as well as a section on the variety of things you can do to maintain your server manually.

**Next steps (evaluation)**

* Contact [Pentaho](https://www.pentaho.com/helpmeout) to learn more about how Business Analytics can be tailored to meet your business needs.
* Continue with [Develop your BA environment](#develop-your-ba-environment).

#### Develop your BA environment

This workflow outlines how to set up a Pentaho Server for BA development. It also covers how to build, refine, and test BA content.

This workflow is similar to the Trial Download Evaluation experience. The difference is you configure the server fully. You also work with your own report designers and data scientists. You can also engage Pentaho [professional services](https://www.hitachivantara.com/en-us/services/big-data-analytics-services.html).

Before you start, consider Pentaho [training classes](https://www.hitachivantara.com/en-us/services/training-certification.html). Training helps you install and configure the server. Training also helps you build data models and BA applications.

**Set up your Pentaho Server**

Use this checklist to verify requirements. Then install and configure the Pentaho Server and BA design tools.

**Verify system requirements**

* Review required components in [Components Reference](https://docs.pentaho.com/pdia-try-pdia/components-reference).
* Review required drivers in [JDBC drivers reference](https://docs.pentaho.com/pdia-try-pdia/jdbc-drivers-reference).
* Acquire one or more servers that meet requirements.
* Obtain the correct drivers for your system.

**Obtain software and install the Pentaho Server**

* Download the Pentaho software from your Sales Support representative.
* Install the software using [Install the 30-day trial of Pentaho Data Integration and Analytics](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pentaho-evaluation).
* Sign in using [Quick tour of the Pentaho User Console](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/quick-tour-of-the-pentaho-user-console-puc).
* Tour **Administration**.
* Change the default administrator password.

**Change the Pentaho Server fully qualified URL**

* Follow **Administer Pentaho Data Integration and Analytics** instructions to change the server URL.
* If multiple machines point to one server, confirm all clients use the new URL.

**Configure the Pentaho Server**

* Manage licenses. See **Administer Pentaho Data Integration and Analytics**.
* Configure server data connections. See **Install Pentaho Data Integration and Analytics**.
* Configure email for scheduled reports. See **Pentaho Business Analytics**.
* Review schedule management. See **Pentaho Business Analytics**.

**Configure BA design tools**

Do this only on a development system. Do not configure design tools on your production server.

* Configure design tools and utilities. See **Install Pentaho Data Integration and Analytics**.
* Configure each tool’s data connections. See **Install Pentaho Data Integration and Analytics**.

**Import data sources and data models**

Create data sources and models that support agile BA development.

**Choose data source types**

* Choose a data source type. See **Pentaho Business Analytics**.
* Review relational versus multidimensional models.

**Create data sources and models**

* Tour the Data Source Wizard. See **Pentaho Business Analytics**.
* Learn how the server and wizard produce usable sources and models.

**Create database table data sources**

* Create a database table source. See **Pentaho Business Analytics**.
* Create initial data sources and preliminary models.

**Learn about Mondrian schemas**

* Create and modify Mondrian schemas. See **Pentaho Schema Workbench**.
* Add a Mondrian data source.
* Adapt the schema for Analyzer.
* Refine the schema in Schema Workbench.

**Create reports and further refine data models**

Work with data scientists and business analysts at this stage. This improves the quality of models and reports.

As you prepare to move to production, use data sources from:

* Pentaho Schema Workbench
* Pentaho Metadata Editor

**Create Analyzer reports, Interactive reports, and dashboards**

* Follow **Pentaho Business Analytics** instructions.
* Create Interactive and Analyzer reports.
* Create a dashboard.
* Verify results match what you need.
* If needed, refine models with your data team.

**Create a report with Report Designer (optional)**

* Follow **Pentaho Report Designer** instructions.

**Refine your data source model**

* Edit multidimensional models. See **Pentaho Business Analytics**.
* Refine Mondrian schemas. See **Pentaho Schema Workbench**.
* Refine relational models. See **Pentaho Metadata Editor**.
* Recreate reports to validate changes.
* Repeat until results meet requirements.

**Test environment quality**

If you do quality assurance testing, upload content to the Pentaho Repository. Then download it to the QA server. See **Administer Pentaho Data Integration and Analytics** for details.

Some organizations also run user acceptance testing after QA.

**Next steps (development)**

* Investigate security. See **Administer Pentaho Data Integration and Analytics**.
* Plan scheduling for production. See **Pentaho Business Analytics**.
* Decide what content to promote to production. See **Administer Pentaho Data Integration and Analytics**.
* Check the [Support Portal](https://support.pentaho.com/hc/en-us) for service packs.
* Prepare to [Go live for production - BA](#go-live-for-production---ba).

#### Go live for production - BA

This section explains how to move Pentaho content and server settings between servers.

This process usually uses two or three servers with identical configurations:

* BA content development
* Testing and QA (optional)
* Production

We recommend working with Pentaho [professional services](https://www.pentaho.com/services) during production deployment.

**Prepare for going live**

This section has two parts:

* A checklist for setting up a Pentaho Server
* Prerequisites to complete before you go live

If your production server is already set up, start with the prerequisites.

**Pentaho Server setup checklist**

| Task                                           | Do this                                                                                                                                                                                                                                                                                                        | Notes                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Verify system requirements                     | <p>Consult:<br>- <a href="components-reference">Components Reference</a><br>- <a href="jdbc-drivers-reference">JDBC drivers reference</a></p>                                                                                                                                                                  | <p>- Acquire one or more servers that meet requirements.<br>- Obtain the correct drivers.</p>                                                                                                                                                                      |
| Obtain software and install the Pentaho Server | <p>- Install Pentaho Suite. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Download and install the latest service pack. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Access the User Console. See <strong>Pentaho Business Analytics</strong>.</p> | <p>- Install the software.<br>- Install the latest service pack.<br>- Access the User Console, review <strong>Administration</strong>, and change the default administrator password.<br><br>If needed, change the fully qualified URL for the Pentaho Server.</p> |
| Change the server fully qualified URL          | Change the Pentaho Server fully qualified URL if needed. See **Administer Pentaho Data Integration and Analytics**.                                                                                                                                                                                            | If many machines point to one server, change the URL and verify connectivity.                                                                                                                                                                                      |
| Configure the server                           | <p>- Manage licenses. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Specify data connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Set up email for scheduled reports. See <strong>Pentaho Business Analytics</strong>.</p>                | <p>- Set up data connections.<br>- Configure email through <strong>Administration</strong>.</p>                                                                                                                                                                    |

**Prerequisites before you go live**

| Task                        | Do this                                                                                                                                                                                                                                                                                                  | Notes                                                                                                                                           |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Compare configuration files | <p>- Compare server configuration files.<br>- Verify and increase memory settings. See <strong>Administer Pentaho Data Integration and Analytics</strong>.</p>                                                                                                                                           | <p>- Identify configuration differences.<br>- Commit a unified properties file to version control.<br>- Increase memory settings as needed.</p> |
| Verify data sources         | <p>- Specify data connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.<br>- Define JNDI connections. See <strong>Install Pentaho Data Integration and Analytics</strong>.</p>                                                                                               | <p>- Confirm data sources can be promoted.<br>- Establish JNDI sources as replacements if needed.</p>                                           |
| Define security             | <p>- Define Pentaho Server security. See <strong>Administer Pentaho Data Integration and Analytics</strong>.<br>- Manage users and roles. See <strong>Pentaho Business Analytics</strong>.<br>- Implement advanced security. See <strong>Administer Pentaho Data Integration and Analytics</strong>.</p> | <p>- Implement security.<br>- Define users, roles, and permissions.</p>                                                                         |
| Upload content              | Upload and download from the Pentaho Repository. See **Administer Pentaho Data Integration and Analytics**.                                                                                                                                                                                              | - Upload files and folders.                                                                                                                     |

**Compare configuration files**

The most important server configuration settings are stored in the `/server/pentaho-server/pentaho-solutions/system/` directory.

Some core settings are also inside the Pentaho WAR archive deployed to your application server. These settings should not change after initial setup.

{% hint style="warning" %}
Do not change the names of content files, data sources, solution directories, or other file names during promotion.

Set names during solution development. Keep names consistent through promotion.

Renaming can cause issues that you will not detect immediately. This can break QA and production content.
{% endhint %}

To ensure you selected all server configuration files, compare these directories in full:

* `/pentaho-solutions/system/`
* `/WEB-INF/` inside your deployed `pentaho.war`
* `/META-INF/` inside your deployed `pentaho.war`

{% hint style="info" %}
Plugin directories for Analyzer, Dashboard Designer, Interactive Reports, and Community Dashboard Framework include binaries.

Binary differences usually indicate version differences. Focus on XML and properties files.

If you customized plugins, promote those changes too.
{% endhint %}

**Move content to production server**

This checklist summarizes best practices to promote Pentaho Server settings, data sources, and content.

Before you promote from development to production, complete the preparation and prerequisite tasks earlier in this page.

| Task                                | Do this                                                                       | Notes                                                                                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Download content                    | - Upload and download from the Pentaho Repository.                            | <p>- Move all desired content to production.<br>- See <strong>Administer Pentaho Data Integration and Analytics</strong> for details.</p>           |
| Set up schedules and blockout times | <p>- Manage schedules.<br>- Prevent scheduling by setting blockout times.</p> | <p>- Set up production schedules.<br>- Set up blockout times for maintenance.<br>- See <strong>Pentaho Business Analytics</strong> for details.</p> |

**Next steps (production)**

These resources are helpful after your production server is live:

* See **Administer Pentaho Data Integration and Analytics** for guidance on maintenance and tuning.
* Pentaho [Training and Education](https://www.hitachivantara.com/en-us/services/training-certification.html)
* [Support Portal](https://support.pentaho.com/hc/en-us) for service packs
