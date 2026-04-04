# Source: https://www.hammerdb.com/docs4.0/ch13.html

Title: Chapter 13. Generating and Loading Bulk Datasets

URL Source: https://www.hammerdb.com/docs4.0/ch13.html

Markdown Content:
For all workloads HammerDB can create the schema and generate and load the data without requiring a staging area, in many circumstances this is the preferred method of loading especially for OLTP workloads. Nevertheless in some circumstances it is preferable to create the data externally as flat files and then use a special database vendor provided bulk loading command to load the data into pre-created tables. This option may be preferred for example where the target database to load is located in the cloud or where the target database has a column structure meaning that load performance using batch inserts is poor. Additionally bulk loading can enable more flexibility to modify the schema according to preference and reload during testing. This chpater details how to generate and load large data sets with HammerDB.
