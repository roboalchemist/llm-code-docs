# Source: https://www.hammerdb.com/docs4.0/ch11s04.html

Title: 4. Benchmarking Database Cloud Services

URL Source: https://www.hammerdb.com/docs4.0/ch11s04.html

Markdown Content:
In addition to the TPROC-H workload there are also a set of Cloud Analytic Queries made publicly available by Oracle for comparison of Cloud Analytic services. These queries run against a derived TPC-H schema and are included with HammerDB for running against Oracle, Amazon Aurora and Amazon Redshift with Amazon Aurora and Redshift being based upon and compatible with MySQL and PostgreSQL respectively. Note however that in similarity to MySQL Amazon Aurora does not have the features to support analytics such as parallel query or a column store option and therefore running the analytic tests against Aurora although possible is not likely to generate the best results. Amazon Redshift however is a column oriented database based on PostgreSQL and suitable for running analytic workloads.

For the Cloud Analytic workload the Oracle specification requires a schema size of 10TB, it is recommended to create the schema with HammerDB using the Generating and Bulk Loading Data feature and this guide details how to do this for both Oracle and Redshift and this is particularly recommended when uploading data to the cloud.

You are permitted to run both the in-built TPROC-H queries and the Cloud Analytic Queries against the same database. This new query set is enabled under the TPROC-H Driver Script Options dialog by selecting the Cloud Analytic Queries checkbox. This query set reports the geometric mean of the completed queries that returns rows for circumstances where the query set is run on a scale factor size of less than 10TB. Given the similarity of the Oracle implementation to the existing TPROC-H workload the following example illustrates running the workload against Amazon Redshift.

### [](https://www.hammerdb.com/docs4.0/ch11s04.html)4.1.Redshift Cloud Analytic Workload

Ensure that your Redshift cluster is active and note your Endpoint name given above the cluster properties.

**Figure 11.7.Redshift console**

![Image 1: Redshift console](https://www.hammerdb.com/docs4.0/resources/ch9-13.png)

Also ensure that access is enabled to the cluster both by defining a user and a security group and allowing access through your firewall.

**Figure 11.8.Create Security Group**

![Image 2: Create Security Group](https://www.hammerdb.com/docs4.0/resources/ch9-14.png)

Create the TPROC-H schema within Redshift using the HammerDB Generating and Bulk Loading Data feature. Under PostgreSQL TPROC-H Driver Options use the Redshift Endpoint as your PostgreSQL host and 5439 as your port. Set the user and password to the credentials you have set under the Amazon AWS console. To run the Cloud Analytic Workload with HammerDB refer to the following Chapter on How to run an Analytic Workload and select the Cloud Analytic Queries and Redshift Compatible Checkbox with the reported metric being the geometric mean of the query times that complete for the one Virtual User used. Note that when running the queries against data sets smaller than the specified 10TB this may result in some queries not returning rows, therefore for your calculations HammerDB calculates the geometric mean only of queries that returned rows.
