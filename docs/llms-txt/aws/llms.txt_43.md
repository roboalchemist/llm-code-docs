# Source: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/llms.txt

# Amazon SimpleDB Developer Guide

> Amazon SimpleDB is a highly available, scalable, and flexible non-relational data store that enables you to store and query data items using web services requests. This guide explains how to manage and query data in Amazon SimpleDB by using the Query and SOAP programming interfaces.

- [Welcome to Amazon SimpleDB](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Welcome.html)
- [Introduction to Amazon SimpleDB](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Introduction.html)
- [API Error Codes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APIError.html)
- [Document History](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DocumentHistory.html)

## [Amazon SimpleDB Concepts](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/concepts.html)

- [Data Model](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataModel.html): When using Amazon SimpleDB, you organize your structured data in domains within which you can put data, get data, or run queries.
- [Operations](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Operations.html): The following describes components of Amazon SimpleDB operations.
- [API Summary](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APISummary.html): The Amazon SimpleDB service consists of a small group of API calls that provide the core functionality you need to build your application.
- [Consistency](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ConsistencySummary.html): Amazon SimpleDB keeps multiple copies of each domain.
- [Limits](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDBLimits.html): Following is a table that describes current limits within Amazon SimpleDB.
- [Data Set Partitioning](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataSetPartitioningConcepts.html): Amazon SimpleDB is designed to support highly parallel applications.
- [AWS Identity and Access Management](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/IAM.html): is integrated with AWS Identity and Access Management (IAM), which offers a wide range of features:


## [Using Amazon SimpleDB](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/using.html)

- [Available Libraries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/AWSLibraries.html): AWS provides libraries (the AWS SDKs), which include sample code, tutorials, and other resources for software developers who prefer to build applications using language-specific APIs instead of writing their own HTTP requests.

### [Making API Requests](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APIRequests.html)

- [Region Endpoints](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Endpoints.html): To improve latency and to store data in a location that meets your requirements, Amazon SimpleDB enables you to select different region endpoints.
- [Making REST Requests](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/MakingRESTRequests.html)

### [Request Authentication](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/RequestAuthentication.html)

- [What Is Authentication?](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WhatIsAuthentication.html): Authentication is a process for identifying and verifying who is sending a request.
- [Creating an AWS Account](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/AboutAWSAccounts.html): To access any web service AWS offers, you must first create an AWS account at http://aws.amazon.com.
- [Managing Users of Amazon SimpleDB](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html)
- [Using Temporary Security Credentials](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html): In addition to creating users with their own security credentials, IAM also enables you to grant temporary security credentials to any user to allow the user to access your AWS services and resources.
- [HMAC-SHA Signature](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/HMACAuth.html)

### [Working with Domains](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomains.html)

This section describes how to work create, list, and delete domains.

- [Creating a Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsCreate.html): The following is an example of creating a domain using REST.
- [Verifying the Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsList.html): The following is an example of listing domains using REST.
- [Deleting a Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDomainsDelete.html): The following is an example of deleting a domain using REST.

### [Working with Data](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithData.html)

This section describes how to create, get, and delete attributes.

- [Putting Data into a Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataPut.html): The following is an example of putting data into a domain using REST.
- [Getting Data from a Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataGet.html): The following is an example of getting data from an item using REST.
- [Deleting Data from a Domain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/WorkingWithDataDelete.html): The following is an example of deleting data from an item using REST.

### [Conditionally Putting and Deleting Data](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ConditionalPutDelete.html)

This section describes how to update or delete data when a specific condition is met.

- [Performing a Conditional Put](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ConditionalPut.html): Conditional put enables you to insert or replace values for one or more attributes of an item if the existing value of an attribute matches a value that you specify.
- [Performing a Conditional Delete](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ConditionalDelete.html): Conditional delete enables you to delete an item or one or more attributes of an item if the existing value of an attribute matches a value that you specify.

### [Using Select to Create Amazon SimpleDB Queries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingSelect.html)

This section describes Select, a function that takes query expressions similar to the standard SQL SELECT statement.

- [Comparison Operators](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingSelectOperators.html): Comparison operators are applied to a single attribute and are lexicographical in nature.
- [Sample Query Data Set](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingSelectSampleDataset.html): The following table contains the data set used throughout this section.
- [Simple Queries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SimpleQueriesSelect.html): This section shows simple queries and their results.
- [Range Queries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/RangeQueriesSelect.html): Amazon SimpleDB enables you to execute more than one comparison against attribute values within the same predicate.
- [Queries on Attributes with Multiple Values](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/RangeValueQueriesSelect.html): One of the unique features of Amazon SimpleDB is that it allows you to associate multiple values with a single attribute.
- [Multiple Attribute Queries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/MultipleAttributeQueriesSelect.html): The previous examples show how to create expressions for single predicates.
- [Sort](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SortingDataSelect.html): Amazon SimpleDB supports sorting data on a single attribute or the item names, in ascending (default) or descending order.
- [Count](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/CountingDataSelect.html): If you want to count the number of items in a result set instead of returning the items, use count(*).
- [Select Quoting Rules](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/QuotingRulesSelect.html): Attribute values must be quoted with a single or double quote.

### [Working with Numerical Data](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/NumericalData.html)

- [Negative Numbers Offsets](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/NegativeNumbersOffsets.html): When choosing a numerical range, ensure that every number is positive.
- [Zero Padding](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/ZeroPadding.html): After all the numbers in a data set are positive, ensure they are properly represented for lexicographical comparisons.
- [Dates](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Dates.html): To convert dates to strings, we recommend following the ISO 8601 format, which supports lexicographical order comparisons.

### [Tuning Queries](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/TuningQueries.html)

- [Tuning Your Queries Using Composite Attributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/BoxUsageTuning.html): Careful implementation of attributes can increase the efficiency of query operations in terms of duration and complexity.
- [Data Set Partitioning](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/DataSetPartitioning.html): Amazon SimpleDB allows up to 250 domains per subscriber.
- [Working with XML-Restricted Characters](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/InvalidCharacters.html): You can store data in Amazon SimpleDB through the REST interface.


## [API Reference](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API.html)

- [API Usage](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APIUsage.html): This section provides a high-level overview of the Amazon SimpleDB API.
- [Common Parameters](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ParametersDescription.html): This section describes parameters used by Amazon SimpleDB operations.
- [Common Response Elements](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CommonResponseElements.html)
- [Common Error Responses](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CommonErrorResponses.html): Request authentication errors are described in .

### [Operations](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Operations.html)

- [BatchDeleteAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchDeleteAttributes.html)
- [BatchPutAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_BatchPutAttributes.html)
- [CreateDomain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_CreateDomain.html)
- [DeleteAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteAttributes.html)
- [DeleteDomain](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DeleteDomain.html)
- [DomainMetadata](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_DomainMetadata.html)
- [GetAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_GetAttributes.html)
- [ListDomains](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_ListDomains.html)
- [PutAttributes](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_PutAttributes.html)
- [Select](https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/SDB_API_Select.html)
