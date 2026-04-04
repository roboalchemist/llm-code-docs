# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/prepare-your-data.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/prepare-your-data.md

# Prepare your data

To prepare data for use with the Pentaho Analyzer and Report Designer, you should perform the following basic tasks:

* **Design a Star or Snowflake Schema**

  The entire process starts with a data warehouse. This section will not attempt to explain how to build this structure -- there are entire books on the subject, and an entire consulting industry dedicated to it already. The end result should be data model in the star or snowflake schema pattern. You do not have to worry too much about getting the model exactly right on your first try. Just cover all of your anticipated business needs; part of the process is coming back to the data warehouse design step and making changes to your initial data model after you have discovered what your operational needs are.
* **Populate the Star/Snowflake Schema**

  Once your data model is designed, the next step is to populate it with actual data, thereby creating your data warehouse. The best tool for this job is Pentaho Data Integration, an enterprise-grade extract, transform, and load (ETL) application.
* **Build a Mondrian Schema**

  Now that your initial data warehouse project is complete, you must build a Mondrian schema to organize and describe it in terms that Pentaho Analyzer can understand. You can use the Pentaho Schema Workbench to create an analysis schema.
* **Initial Testing**

  At this point, you should have a multi-dimensional data structure with an appropriate metadata layer. You can now start using the data inspection tools to drill down into your data and see if your first attempt at data modeling was successful. See the **Pentaho Data Integration** document for details on our data inspection tools. In all likelihood, it will need some adjustment, so take note of all of the schema limitations that you are unhappy with during this initial testing phase. Do not be concerned with performance issues at this time, just concentrate on the completeness and comprehensiveness of the data model.
* **Adjust and Repeat Until Satisfied**

  Use the notes you took during the testing phase to redesign your data warehouse and Mondrian schema appropriately. Adjust hierarchies and relational measure aggregation methods. Create virtual cubes for analyzing multiple fact tables by conforming dimensions. Re-test the new implementation and continue to refine the data model until it matches your business needs perfectly.
* **Test for Performance**

  Once you are satisfied with the design and implementation of your data model, you should try to find performance problems and address them by tuning your data warehouse database, and by creating aggregation tables. The testing can only be reasonably done by hand, using Pentaho Analyzer. Take note of all of the measures that take an unreasonably long time to calculate. Also, enable SQL logging and locate slow-performing queries, and build indexes for optimizing query performance.
* **Create Aggregation Tables**

  Using your notes as a guide, create aggregation tables in Pentaho Aggregation Designer to store frequently computed Analyzer reports. Re-test and create new aggregation tables as necessary. If you are working with a relatively small data warehouse or a limited number of dimensions, you may not have a real need for aggregation tables. However, be aware of the possibility that performance issues may come up in the future. Check in with your users occasionally to see if they have any particular concerns about the speed of their content.
* **Deploy to Production**

  Your data warehouse and Mondrian schema have been created, tested, and refined. You're now ready to put it all into production. You may need to train or purchase Pentaho training for those in your organization who use Pentaho client tools.
