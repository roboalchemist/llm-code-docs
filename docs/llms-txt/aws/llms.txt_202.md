# Source: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/llms.txt

# Amazon CloudSearch Developer Guide

> Set up, manage, and scale a search solution for your website with the Amazon CloudSearch web service.

- [Migrating to the 2013-01-01 API](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/migrating.html)
- [Integrating with API Gateway](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/api-gateway.html)
- [Handling Errors](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/error-handling.html)
- [Troubleshooting](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/troubleshooting.html)
- [Limits](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/limits.html)
- [Resources](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/resources.html)
- [Document History](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/document-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/glossary.html)

## [What Is Amazon CloudSearch?](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/what-is-cloudsearch.html)

- [How Search Works](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/how-search-works.html): Describe your data as a batch of documents and upload the resulting batch to your search domain.
- [Automatic Scaling](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/concepts-scaling.html): Automatically scale the size and number of search instances with Amazon CloudSearch.


## [Getting Started](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started.html)

- [Before You Begin](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-sign-up.html): To use Amazon CloudSearch, you need an Amazon Web Services (AWS) account.
- [Step 1: Create a Search Domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-create-domain.html): An Amazon CloudSearch domain encapsulates a collection of data you want to search, the search instances that process your search requests, and a configuration that controls how your data is indexed and searched.
- [Step 2: Upload Data for Indexing](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-uploading-data.html): You upload the data you want to search to your domain so that Amazon CloudSearch can build and deploy a searchable index.
- [Step 3: Search Your Domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-search.html): You can use the search tester in the Amazon CloudSearch console to submit sample search requests and view the results.
- [Step 4: Delete Your Movies Domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-delete-domain.html): When you are finished experimenting with your movies domain, you must delete it to avoid incurring additional usage fees.


## [Creating and Managing Search Domains](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-managing-domains.html)

- [Creating a Search Domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html): Create a search domain that encapsulates your data, metadata, and index configuration options within Amazon CloudSearch.
- [Configuring Access](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html): Authorize access to Amazon CloudSearch.
- [Configuring Scaling Options](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html): Control how your search domain is scaled to accommodate changes in the document update rate, size of the index, and volume of query traffic.
- [Configuring Availability Options](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html): Configure an Amazon CloudSearch domain to be deployed across two availability zones to ensure the domain can be accessed in the event of a data center service disruption.
- [Configuring Domain Endpoint Options](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html): Amazon CloudSearch domains let you require that all traffic to the domain arrive over HTTPS.

### [Monitoring Search Domains](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/monitoring-domains.html)

Monitor your Amazon CloudSearch domains using the AWS Management Console.

- [Getting Domain Information](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html): Get information about your Amazon CloudSearch domain, such as domain name and index configuration.
- [Monitoring a Domain with Amazon CloudWatch](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/cloudwatch-monitoring.html): Monitoring a search domain with Amazon CloudWatch.
- [Logging Configuration API Calls](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/logging-config-api-calls.html): Learn about logging calls to the Amazon CloudSearch configuration API with AWS CloudTrail.
- [Tracking your Amazon CloudSearch Usage and Charges](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/tracking-usage.html): Track your Amazon CloudSearch usage and charges with the AWS account activity page.
- [Deleting a Domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html): Delete a search domain if you are no longer using it to avoid incurring additional usage fees for Amazon CloudSearch.
- [Tagging Amazon CloudSearch Domains](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/tagging-cloudsearch-domains.html): Use Amazon CloudSearch tags to attach metadata to your search domains.


## [Controlling How Data is Indexed](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/controlling-how-data-is-indexed.html)

- [Preparing Your Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/preparing-data.html): Prepare your data so you can upload it to an Amazon CloudSearch domain for indexing.
- [Configuring Index Fields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html): Define all of the document fields you want to include in your index in your domain configuration.
- [Using Dynamic Fields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/using-dynamic-fields.html): Dynamic fields provide a way to index documents without knowing in advance exactly what fields they contain.
- [Configuring Analysis Schemes](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html): Configure a language-specific analysis scheme that can be applied to your Amazon CloudSearch domain's text fields.

### [Text Processing](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html)

Describes the text processing that Amazon CloudSearch performs to determine what terms to add to the index.

- [Supported Languages](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/supported-languages.html): Lists the supported languages in Amazon CloudSearch.


## [Uploading and Indexing Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/uploading-and-indexing-data.html)

### [Uploading Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/uploading-data.html)

Upload data to an Amazon CloudSearch domain for indexing.

- [Submitting Document Upload Requests](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/submitting-doc-requests.html)
- [Indexing Document Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/indexing.html): Index the document data uploaded to your Amazon CloudSearch domain.


## [Searching Your Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching.html)

### [Submitting Search Requests](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/submitting-search-requests.html)

We recommend using one of the AWS SDKs or the AWS CLI to submit search requests.

- [Searching with the Search Tester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/search-tester.html): The search tester in the Amazon CloudSearch console enables you to submit sample search requests using any of the supported query parsers: simple, structured, lucene, or dismax.
- [Constructing Compound Queries](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-compound-queries.html): Use the structured query parser to combine matches against field using the specific operators (and, or, not).
- [Searching for Text in Amazon CloudSearch](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-text.html): Perform searches for terms, phrases, and literal strings by searching text, text-array, literal, and literal-array fields in Amazon CloudSearch.
- [Searching for Numbers](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-numbers.html): Search a numeric field for a particular value or range of values using a structured query.
- [Searching for Dates and Times](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-dates.html): Search a search enabled date field for a particular date and time or a date-time range using a structured query.
- [Searching for a Range of Values](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-ranges.html): You can use structured queries to search a field for a range of values.
- [Searching and Ranking Results by Geographic Location](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-locations.html): Search and rank results by implementing geographically-based searching and sorting in Amazon CloudSearch.
- [Searching DynamoDB Data](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/searching-dynamodb-data.html): Set up a search domain to use an Amazon DynamoDB table as a source when configuring indexing options and upload data from the DynamoDB table.
- [Filtering Matching Documents](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/filtering-results.html): You use the fq parameter to filter the documents that match the search criteria specified with the q parameter without affecting the relevance scores of the documents included in the search results.
- [Tuning Search Requests](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/tuning-search.html): Fine-tune your search requests to help reduce the processing overhead and the cost of running your search domain.


## [Querying For More Information](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/querying-for-more-info.html)

- [Retrieving Data from Index Fields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/retrieving-data.html): Specify the field data to include for the documents that match the search criteria.
- [Getting Statistics for Numeric Fields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/retrieving-stats.html): Get statistics such as the min and max values in a numeric field.
- [Getting and Using Facet Information](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/faceting.html): Request facet information to find out how many documents share the same value in a particular field.
- [Highlighting Search Hits](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/highlighting.html): Configure your search results to highlight where the search terms occur within a particular field of a matching document.
- [Getting Suggestions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html): This section describes how to configure suggesters so you can retrieve suggestions.


## [Controlling Search Results](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/controlling-search-results.html)

- [Sorting Results](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/sorting-results.html): By default, search results are sorted according to their relevance to the search request.
- [Using Relative Field Weighting to Customize Text Relevance](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/weighting-fields.html): Control how much matches in particular fields affect a document's relevance with relative field weighting for custom relevance ranking.

### [Configuring Expressions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html)

Define numeric expressions and use them to sort search results or specify constraints in search requests submitted to your Amazon CloudSearch domain.

- [Defining Expressions in Search Requests](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/defining-expressions-in-requests.html): Define and use expressions directly within search requests submitted to your Amazon CloudSearch domain.
- [Configuring Reusable Expressions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-reusable-expressions.html): Define an expression and add it to the domain configuration so you can reuse the expression in any search request submitted to your Amazon CloudSearch domain.
- [Comparing Expressions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/comparing-expressions.html): Compare expressions to see how changes to the expression and field weights affect how search results are sorted in Amazon CloudSearch.
- [Getting Results as XML](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-xml-results.html): By default, Amazon CloudSearch search responses are formatted in JSON.
- [Paginating Results](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/paginating-results.html): By default, Amazon CloudSearch returns the top ten hits according to the specified sort order.


## [Amazon CloudSearch API Reference](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/api-ref.html)

### [Configuration API Reference](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuration-api.html)

You use the Amazon CloudSearch Configuration API to create, configure, and manage search domains.

- [Submitting Configuration Requests](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/submitting-configuration-requests.html): Submit configuration requests in Amazon CloudSearch using the AWS Query protocol.

### [Actions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Operations.html)

The following actions are supported:

- [BuildSuggesters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_BuildSuggesters.html)
- [CreateDomain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_CreateDomain.html)
- [DefineAnalysisScheme](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineAnalysisScheme.html)
- [DefineExpression](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineExpression.html)
- [DefineIndexField](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineIndexField.html)
- [DefineSuggester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineSuggester.html)
- [DeleteAnalysisScheme](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteAnalysisScheme.html)
- [DeleteDomain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteDomain.html)
- [DeleteExpression](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteExpression.html)
- [DeleteIndexField](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteIndexField.html)
- [DeleteSuggester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteSuggester.html)
- [DescribeAnalysisSchemes](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAnalysisSchemes.html)
- [DescribeAvailabilityOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAvailabilityOptions.html)
- [DescribeDomains](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeDomains.html)
- [DescribeExpressions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeExpressions.html)
- [DescribeIndexFields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeIndexFields.html)
- [DescribeScalingParameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeScalingParameters.html)
- [DescribeDomainEndpointOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeDomainEndpointOptions.html)
- [DescribeServiceAccessPolicies](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeServiceAccessPolicies.html)
- [DescribeSuggesters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeSuggesters.html)
- [IndexDocuments](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexDocuments.html)
- [ListDomainNames](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ListDomainNames.html)
- [UpdateAvailabilityOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateAvailabilityOptions.html)
- [UpdateScalingParameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateScalingParameters.html)
- [UpdateDomainEndpointOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateDomainEndpointOptions.html)
- [UpdateServiceAccessPolicies](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateServiceAccessPolicies.html)

### [Data Types](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Types.html)

The Amazon CloudSearch Configuration Service API contains several data types that various actions use.

- [AccessPoliciesStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AccessPoliciesStatus.html)
- [AnalysisOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AnalysisOptions.html)
- [AnalysisScheme](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AnalysisScheme.html)
- [AnalysisSchemeStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AnalysisSchemeStatus.html)
- [AvailabilityOptionsStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AvailabilityOptionsStatus.html)
- [BuildSuggestersResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_BuildSuggestersResult.html)
- [CreateDomainResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_CreateDomainResult.html)
- [DateArrayOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DateArrayOptions.html)
- [DateOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DateOptions.html)
- [DefineAnalysisSchemeResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineAnalysisSchemeResult.html)
- [DefineExpressionResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineExpressionResult.html)
- [DefineIndexFieldResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineIndexFieldResult.html)
- [DefineSuggesterResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineSuggesterResult.html)
- [DeleteAnalysisSchemeResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteAnalysisSchemeResult.html)
- [DeleteDomainResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteDomainResult.html)
- [DeleteExpressionResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteExpressionResult.html)
- [DeleteIndexFieldResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteIndexFieldResult.html)
- [DeleteSuggesterResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteSuggesterResult.html)
- [DescribeAnalysisSchemesResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAnalysisSchemesResult.html)
- [DescribeAvailabilityOptionsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAvailabilityOptionsResult.html)
- [DescribeDomainsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeDomainsResult.html)
- [DescribeExpressionsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeExpressionsResult.html)
- [DescribeIndexFieldsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeIndexFieldsResult.html)
- [DescribeScalingParametersResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeScalingParametersResult.html)
- [DescribeServiceAccessPoliciesResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeServiceAccessPoliciesResult.html)
- [DescribeSuggestersResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeSuggestersResult.html)
- [DocumentSuggesterOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DocumentSuggesterOptions.html)
- [DomainEndpointOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html)
- [DomainEndpointOptionsStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptionsStatus.html)
- [DomainStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainStatus.html)
- [DoubleArrayOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DoubleArrayOptions.html)
- [DoubleOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DoubleOptions.html)
- [Expression](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Expression.html)
- [ExpressionStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ExpressionStatus.html)
- [IndexDocumentsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexDocumentsResult.html)
- [IndexField](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexField.html)
- [IndexFieldStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexFieldStatus.html)
- [IntArrayOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IntArrayOptions.html)
- [IntOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IntOptions.html)
- [LatLonOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_LatLonOptions.html)
- [Limits](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Limits.html)
- [ListDomainNamesResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ListDomainNamesResult.html)
- [LiteralArrayOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_LiteralArrayOptions.html)
- [LiteralOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_LiteralOptions.html)
- [OptionStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_OptionStatus.html)
- [ScalingParameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html)
- [ScalingParametersStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParametersStatus.html)
- [ServiceEndpoint](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ServiceEndpoint.html)
- [Suggester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Suggester.html)
- [SuggesterStatus](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_SuggesterStatus.html)
- [TextArrayOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_TextArrayOptions.html)
- [TextOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_TextOptions.html)
- [UpdateAvailabilityOptionsResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateAvailabilityOptionsResult.html)
- [UpdateScalingParametersResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateScalingParametersResult.html)
- [UpdateServiceAccessPoliciesResult](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateServiceAccessPoliciesResult.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/CommonParameters.html): This section lists the request parameters that all actions use.
- [Common Errors](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/CommonErrors.html): This section lists the common errors that all actions return.

### [Document Service API Reference](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/document-service-api.html)

You use the document service API to add, replace, or delete documents in your Amazon CloudSearch domain.

### [documents/batch](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/documents-batch-resource.html)

This section describes the HTTP request and response messages for the documents/batch resource.

- [documents/batch XML API](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/documents-batch-xml.html)
- [Search API Reference](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/search-api.html)
