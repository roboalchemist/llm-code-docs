# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/dimensional-modeling.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/dimensional-modeling.md

# Dimensional modeling

With the initial data structure in place, you can use dimensional modeling to design a descriptive layer. Dimensional modeling is the process of transforming data from multiple sources in non-human-friendly formats into a single data source that is organized to support business analytics. Below is a typical workflow for developing a dimensional model:

1. Collect user requirements for business logic and processes.
2. Considering the entirety of your data, break it down into subjects.
3. Isolate groups of facts into one or more fact tables.
4. Design dimensional tables which draw relationships between levels (fact groups).
5. Determine which members of each level are useful for each dimensional table.
6. Build and publish a Mondrian (Pentaho Analyzer) schema and collect feedback from users.
7. Refine your model based on user feedback, continue iterating through this list until users are productive.

Or, expressed as a series of questions:

1. What topics or subjects are important to the users who are analyzing the data? What do your users need to learn from the data?
2. What are the important details your users will need to examine in the data?
3. How should each data column relate to other data columns?
4. How should datasets be grouped and organized?
5. What are some useful short descriptions for each dimensional level in a hierarchy (for each element, decide what is useful within that element; for instance, in a dimensional table representing time, your levels might be year, month, and day, and your members for the year level might be 2003, 2004, 2005).
6. How effective is this dimensional model for the intended user base? How can it be improved?

Pentaho Data Integration offers data inspection tools to make dimensional modeling much easier than more traditional methods. Through PDI, you can quickly adjust your business logic, the granularity of your fact tables, and the attributes of your dimension tables, then generate a new model and push it out to a test environment for evaluation. See the **Pentaho Data Integration** document for details.
