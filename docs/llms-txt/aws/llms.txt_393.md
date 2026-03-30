# Source: https://docs.aws.amazon.com/forecast/latest/dg/llms.txt

# Amazon Forecast Developer Guide

> Provides a conceptual overview of Amazon Forecast. Includes detailed instructions for using the features and provides a complete API reference for developers.

- [How Amazon Forecast Works](https://docs.aws.amazon.com/forecast/latest/dg/how-it-works.html)
- [Generating Forecasts](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-forecast.html)
- [Forecast Explainability](https://docs.aws.amazon.com/forecast/latest/dg/forecast-explainability.html)
- [Guidelines and Quotas](https://docs.aws.amazon.com/forecast/latest/dg/limits.html)
- [Reserved Field Names](https://docs.aws.amazon.com/forecast/latest/dg/reserved-field-names.html)
- [Document History](https://docs.aws.amazon.com/forecast/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/forecast/latest/dg/glossary.html)

## [What Is Amazon Forecast?](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/forecast/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Setting Up](https://docs.aws.amazon.com/forecast/latest/dg/setup.html)

- [Sign Up for AWS](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-set-up-aws-account.html): Learn how to set up a new AWS account.
- [Set Up AWS CLI](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-set-up-aws-cli.html): Set up the AWS CLI to manage Amazon Forecast.
- [Set Up Permissions](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-iam-roles.html): Learn how to set up the required IAM roles and policy to control access permissions to Amazon Forecast.


## [Getting Started](https://docs.aws.amazon.com/forecast/latest/dg/getting-started.html)

- [Getting Started (Console)](https://docs.aws.amazon.com/forecast/latest/dg/gs-console.html): Getting started exercise for using the Amazon Forecast console.
- [Getting Started (AWS CLI)](https://docs.aws.amazon.com/forecast/latest/dg/gs-cli.html): Use the AWS CLI to get started using Amazon Forecast.
- [Getting Started (Python Notebooks)](https://docs.aws.amazon.com/forecast/latest/dg/getting-started-python.html)


## [Tutorials](https://docs.aws.amazon.com/forecast/latest/dg/tutorials.html)

- [Automating with CloudFormation](https://docs.aws.amazon.com/forecast/latest/dg/tutorial-cloudformation.html): Tutorial on how to deploy an CloudFormation template for Amazon Forecast automation.


## [Importing Datasets](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html)

- [Related Time Series](https://docs.aws.amazon.com/forecast/latest/dg/related-time-series-datasets.html): Describes Amazon Forecast related time series datasets.
- [Item Metadata](https://docs.aws.amazon.com/forecast/latest/dg/item-metadata-datasets.html): Describes Amazon Forecast item metadata datasets, which provide context for data in target time-series datasets when you use the DeepAR+ algorithm to train a predictor.

### [Predefined Dataset Domains and Dataset Types](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html)

To train a predictor, you create one or more datasets, add them to a dataset group, and provide the dataset group for training.

- [RETAIL Domain](https://docs.aws.amazon.com/forecast/latest/dg/retail-domain.html): The RETAIL domain supports the following dataset types.
- [CUSTOM Domain](https://docs.aws.amazon.com/forecast/latest/dg/custom-domain.html): The CUSTOM domain supports the following dataset types.
- [INVENTORY_PLANNING Domain](https://docs.aws.amazon.com/forecast/latest/dg/inv-planning-domain.html): Use the INVENTORY_PLANNING domain for forecasting demand for raw materials and determining how much inventory of a particular item to stock.
- [EC2 CAPACITY Domain](https://docs.aws.amazon.com/forecast/latest/dg/ec2-capacity-domain.html): Use the EC2 CAPACITY domain for forecasting Amazon EC2 capacity.
- [WORK_FORCE Domain](https://docs.aws.amazon.com/forecast/latest/dg/workforce-domain.html): Use the WORK_FORCE domain to forecast workforce demand.
- [WEB_TRAFFIC Domain](https://docs.aws.amazon.com/forecast/latest/dg/webtraffic-domain.html): Use the WEB_TRAFFIC domain to forecast web traffic to a web property or a set of web properties.
- [METRICS Domain](https://docs.aws.amazon.com/forecast/latest/dg/metrics-domain.html): Use the METRICS domain for forecasting metrics, such as revenue, sales, and cash flow.
- [Updating Data](https://docs.aws.amazon.com/forecast/latest/dg/updating-data.html): Learn how to update data in Forecast.
- [Handling Missing Values](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-missing-values.html): Describes how to handle missing values in your source datasets.
- [Dataset Guidelines](https://docs.aws.amazon.com/forecast/latest/dg/dataset-import-guidelines-troubleshooting.html): Provides troubleshooting information for problems with importing Amazon Forecast datasets.


## [Training Predictors](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-predictor.html)

### [Data Aggregation](https://docs.aws.amazon.com/forecast/latest/dg/data-aggregation.html)

Learn about how Amazon Forecast generates forecasts for data frequencies that are higher than the predictor's forecast frequency.

- [How Aggregation Works](https://docs.aws.amazon.com/forecast/latest/dg/how-aggregation-works.html): Learn about how Forecast aggregates your data to align with the forecast frequency you specify when you create a predictor.
- [Data Aggregation Assumptions](https://docs.aws.amazon.com/forecast/latest/dg/aggregation-guidelines.html): Learn what Forecast assumes about your data during data aggregation.
- [Predictor Metrics](https://docs.aws.amazon.com/forecast/latest/dg/metrics.html): Describes the accuracy metrics for Amazon Forecast predictors.
- [Retraining Predictors](https://docs.aws.amazon.com/forecast/latest/dg/retrain-predictors.html): Retrain Amazon Forecast predictors with updated datasets.
- [Weather Index](https://docs.aws.amazon.com/forecast/latest/dg/weather.html): Use the Amazon Forecast Weather Index to incorporate historical and projected weather data into your model.
- [Holidays Featurization](https://docs.aws.amazon.com/forecast/latest/dg/holidays.html): Use the Holidays featurization to incorporate national holiday information for more than 250 countries into your Amazon Forecast model.
- [Predictor Explainability](https://docs.aws.amazon.com/forecast/latest/dg/predictor-explainability.html): Learn how to use Amazon Forecast Predictor Explainability.

### [Predictor Monitoring](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring.html)

Use Amazon Forecast predictor monitoring to detect changes in model performance as you import additional data and generate new forecasts.

- [Enabling Predictor Monitoring](https://docs.aws.amazon.com/forecast/latest/dg/enabling-predictor-monitoring.html): Learn how to enable predictor monitoring for new and existing auto predictors in Forecast.
- [Viewing Monitoring Results](https://docs.aws.amazon.com/forecast/latest/dg/predictor-monitoring-results.html): Learn how to view predictor monitoring results for an auto predictor in Forecast.

### [Forecast Algorithms](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html)

Learn more about the Amazon Forecast algorithms.

- [ARIMA](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-recipe-arima.html): Use the Amazon Forecast Autoregressive Integrated Moving Average (ARIMA) algorithm in Amazon Forecast to create forecasts.
- [CNN-QR](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-algo-cnnqr.html): Use the Amazon Forecast CNN-QR algorithm for time-series forecasts when your dataset contains hundreds of feature time series.
- [DeepAR+](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-recipe-deeparplus.html): Use the Amazon Forecast DeepAR+ algorithm for time-series forecasts when your dataset contains hundreds of feature time series.
- [ETS](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-recipe-ets.html): Exponential Smoothing (ETS) is a commonly-used local statistical algorithm for time-series forecasting.
- [NPTS](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-recipe-npts.html): The Amazon Forecast Non-Parametric Time Series (NPTS) algorithm is a scalable, probabilistic baseline forecaster.
- [Prophet](https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-recipe-prophet.html): Prophet is a popular local Bayesian structural time series model.


## [What-If Analysis](https://docs.aws.amazon.com/forecast/latest/dg/what-if.html)

- [Transformation Functions](https://docs.aws.amazon.com/forecast/latest/dg/data-transformations.html): Explains what time series transformation functions are, how Amazon Forecast uses them during what-if forecast creation, and how to specify your own transformations.
- [Replacement Dataset](https://docs.aws.amazon.com/forecast/latest/dg/replacement-series.html): Explains what replacement time datasets are, how Amazon Forecast uses them during what-if forecast creation, and how to specify your own replacement time series.


## [Managing Resources](https://docs.aws.amazon.com/forecast/latest/dg/manage-resources.html)

- [Stopping Resources](https://docs.aws.amazon.com/forecast/latest/dg/stop-resource.html): Stop Amazon Forecast resource jobs, for example, forecast jobs, dataset group import jobs, predictor training jobs, predictor backtest export jobs, and forecast export jobs.
- [Deleting Resources](https://docs.aws.amazon.com/forecast/latest/dg/delete-resource.html): Delete Amazon Forecast resources and resource trees.
- [Tagging Resources](https://docs.aws.amazon.com/forecast/latest/dg/tagging-forecast-resources.html): Learn about tagging in Amazon Forecast.
- [Receiving Notifications](https://docs.aws.amazon.com/forecast/latest/dg/notifications.html): Learn how to set up job status notifications for Amazon Forecast


## [Code examples](https://docs.aws.amazon.com/forecast/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/forecast/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of Forecast with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/forecast/latest/dg/service_code_examples_actions.html)

The following code examples show how to use Forecast with AWS SDKs.

- [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_CreateDataset_section.html): Use CreateDataset with an AWS SDK
- [CreateForecast](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_CreateForecast_section.html): Use CreateForecast with an AWS SDK
- [DeleteDataset](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_DeleteDataset_section.html): Use DeleteDataset with an AWS SDK
- [DeleteForecast](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_DeleteForecast_section.html): Use DeleteForecast with an AWS SDK
- [DescribeForecast](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_DescribeForecast_section.html): Use DescribeForecast with an AWS SDK
- [ListDatasetGroups](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_ListDatasetGroups_section.html): Use ListDatasetGroups with an AWS SDK
- [ListForecasts](https://docs.aws.amazon.com/forecast/latest/dg/example_forecast_ListForecasts_section.html): Use ListForecasts with an AWS SDK


## [Security](https://docs.aws.amazon.com/forecast/latest/dg/security.html)

- [Data Protection](https://docs.aws.amazon.com/forecast/latest/dg/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Forecast.

### [Identity and Access Management](https://docs.aws.amazon.com/forecast/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Forecast resources.

- [How Amazon Forecast works with IAM](https://docs.aws.amazon.com/forecast/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Forecast, learn what IAM features are available to use with Forecast.
- [Identity-based policy examples](https://docs.aws.amazon.com/forecast/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Forecast resources.
- [Troubleshooting](https://docs.aws.amazon.com/forecast/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Forecast and IAM.

### [Logging and Monitoring](https://docs.aws.amazon.com/forecast/latest/dg/logging-monitoring.html)

Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon Forecast applications.

- [Logging Forecast API Calls with AWS CloudTrail](https://docs.aws.amazon.com/forecast/latest/dg/logging-using-cloudtrail.html): Learn about logging Forecast with AWS CloudTrail.
- [CloudWatch Metrics for Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/cloudwatch-metrics.html): This section contains information about the Amazon CloudWatch metrics available for Amazon Forecast.
- [Compliance Validation](https://docs.aws.amazon.com/forecast/latest/dg/Forecast-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/forecast/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Forecast features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/forecast/latest/dg/infrastructure-security.html): Learn how Amazon Forecast isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/forecast/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Forecast without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [API Reference](https://docs.aws.amazon.com/forecast/latest/dg/api-reference.html)

### [Actions](https://docs.aws.amazon.com/forecast/latest/dg/API_Operations.html)

The following actions are supported by Amazon Forecast Service:

### [Amazon Forecast Service](https://docs.aws.amazon.com/forecast/latest/dg/API_Operations_Amazon_Forecast_Service.html)

The following actions are supported by Amazon Forecast Service:

- [CreateAutoPredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateAutoPredictor.html): Creates an Amazon Forecast predictor.
- [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html): Creates an Amazon Forecast dataset.
- [CreateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html): Creates a dataset group, which holds a collection of related datasets.
- [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html): Imports your training data to an Amazon Forecast dataset.
- [CreateExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainability.html)
- [CreateExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateExplainabilityExport.html): Exports an Explainability resource created by the operation.
- [CreateForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecast.html): Creates a forecast for each item in the TARGET_TIME_SERIES dataset that was used to train the predictor.
- [CreateForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateForecastExportJob.html): Exports a forecast created by the operation to your Amazon Simple Storage Service (Amazon S3) bucket.
- [CreateMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateMonitor.html): Creates a predictor monitor resource for an existing auto predictor.
- [CreatePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictor.html)
- [CreatePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreatePredictorBacktestExportJob.html): Exports backtest forecasts and accuracy metrics generated by the or operations.
- [CreateWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfAnalysis.html): What-if analysis is a scenario modeling technique where you make a hypothetical change to a time series and compare the forecasts generated by these changes against the baseline, unchanged time series.
- [CreateWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecast.html): A what-if forecast is a forecast that is created from a modified version of the baseline forecast.
- [CreateWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateWhatIfForecastExport.html): Exports a forecast created by the operation to your Amazon Simple Storage Service (Amazon S3) bucket.
- [DeleteDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDataset.html): Deletes an Amazon Forecast dataset that was created using the CreateDataset operation.
- [DeleteDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDatasetGroup.html): Deletes a dataset group created using the CreateDatasetGroup operation.
- [DeleteDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteDatasetImportJob.html): Deletes a dataset import job created using the CreateDatasetImportJob operation.
- [DeleteExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteExplainability.html): Deletes an Explainability resource.
- [DeleteExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteExplainabilityExport.html): Deletes an Explainability export.
- [DeleteForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteForecast.html): Deletes a forecast created using the operation.
- [DeleteForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteForecastExportJob.html): Deletes a forecast export job created using the operation.
- [DeleteMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteMonitor.html): Deletes a monitor resource.
- [DeletePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DeletePredictor.html): Deletes a predictor created using the or operations.
- [DeletePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DeletePredictorBacktestExportJob.html): Deletes a predictor backtest export job.
- [DeleteResourceTree](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteResourceTree.html): Deletes an entire resource tree.
- [DeleteWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfAnalysis.html): Deletes a what-if analysis created using the operation.
- [DeleteWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfForecast.html): Deletes a what-if forecast created using the operation.
- [DeleteWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DeleteWhatIfForecastExport.html): Deletes a what-if forecast export created using the operation.
- [DescribeAutoPredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeAutoPredictor.html): Describes a predictor created using the CreateAutoPredictor operation.
- [DescribeDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html): Describes an Amazon Forecast dataset created using the CreateDataset operation.
- [DescribeDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html): Describes a dataset group created using the CreateDatasetGroup operation.
- [DescribeDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html): Describes a dataset import job created using the CreateDatasetImportJob operation.
- [DescribeExplainability](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeExplainability.html): Describes an Explainability resource created using the operation.
- [DescribeExplainabilityExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeExplainabilityExport.html): Describes an Explainability export created using the operation.
- [DescribeForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeForecast.html): Describes a forecast created using the operation.
- [DescribeForecastExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeForecastExportJob.html): Describes a forecast export job created using the operation.
- [DescribeMonitor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeMonitor.html): Describes a monitor resource.
- [DescribePredictor](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribePredictor.html)
- [DescribePredictorBacktestExportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribePredictorBacktestExportJob.html): Describes a predictor backtest export job created using the operation.
- [DescribeWhatIfAnalysis](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfAnalysis.html): Describes the what-if analysis created using the operation.
- [DescribeWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfForecast.html): Describes the what-if forecast created using the operation.
- [DescribeWhatIfForecastExport](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeWhatIfForecastExport.html): Describes the what-if forecast export created using the operation.
- [GetAccuracyMetrics](https://docs.aws.amazon.com/forecast/latest/dg/API_GetAccuracyMetrics.html): Provides metrics on the accuracy of the models that were trained by the operation.
- [ListDatasetGroups](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html): Returns a list of dataset groups created using the CreateDatasetGroup operation.
- [ListDatasetImportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html): Returns a list of dataset import jobs created using the CreateDatasetImportJob operation.
- [ListDatasets](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html): Returns a list of datasets created using the CreateDataset operation.
- [ListExplainabilities](https://docs.aws.amazon.com/forecast/latest/dg/API_ListExplainabilities.html): Returns a list of Explainability resources created using the operation.
- [ListExplainabilityExports](https://docs.aws.amazon.com/forecast/latest/dg/API_ListExplainabilityExports.html): Returns a list of Explainability exports created using the operation.
- [ListForecastExportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListForecastExportJobs.html): Returns a list of forecast export jobs created using the operation.
- [ListForecasts](https://docs.aws.amazon.com/forecast/latest/dg/API_ListForecasts.html): Returns a list of forecasts created using the operation.
- [ListMonitorEvaluations](https://docs.aws.amazon.com/forecast/latest/dg/API_ListMonitorEvaluations.html): Returns a list of the monitoring evaluation results and predictor events collected by the monitor resource during different windows of time.
- [ListMonitors](https://docs.aws.amazon.com/forecast/latest/dg/API_ListMonitors.html): Returns a list of monitors created with the operation and operation.
- [ListPredictorBacktestExportJobs](https://docs.aws.amazon.com/forecast/latest/dg/API_ListPredictorBacktestExportJobs.html): Returns a list of predictor backtest export jobs created using the operation.
- [ListPredictors](https://docs.aws.amazon.com/forecast/latest/dg/API_ListPredictors.html): Returns a list of predictors created using the or operations.
- [ListTagsForResource](https://docs.aws.amazon.com/forecast/latest/dg/API_ListTagsForResource.html): Lists the tags for an Amazon Forecast resource.
- [ListWhatIfAnalyses](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfAnalyses.html): Returns a list of what-if analyses created using the operation.
- [ListWhatIfForecastExports](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfForecastExports.html): Returns a list of what-if forecast exports created using the operation.
- [ListWhatIfForecasts](https://docs.aws.amazon.com/forecast/latest/dg/API_ListWhatIfForecasts.html): Returns a list of what-if forecasts created using the operation.
- [ResumeResource](https://docs.aws.amazon.com/forecast/latest/dg/API_ResumeResource.html): Resumes a stopped monitor resource.
- [StopResource](https://docs.aws.amazon.com/forecast/latest/dg/API_StopResource.html): Stops a resource.
- [TagResource](https://docs.aws.amazon.com/forecast/latest/dg/API_TagResource.html): Associates the specified tags to a resource with the specified resourceArn.
- [UntagResource](https://docs.aws.amazon.com/forecast/latest/dg/API_UntagResource.html): Deletes the specified tags from a resource.
- [UpdateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html): Replaces the datasets in a dataset group with the specified datasets.

### [Amazon Forecast Query Service](https://docs.aws.amazon.com/forecast/latest/dg/API_Operations_Amazon_Forecast_Query_Service.html)

The following actions are supported by Amazon Forecast Query Service:

- [QueryForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_QueryForecast.html): Retrieves a forecast for a single item, filtered by the supplied criteria.
- [QueryWhatIfForecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_QueryWhatIfForecast.html): Retrieves a what-if forecast.

### [Data Types](https://docs.aws.amazon.com/forecast/latest/dg/API_Types.html)

The following data types are supported by Amazon Forecast Service:

### [Amazon Forecast Service](https://docs.aws.amazon.com/forecast/latest/dg/API_Types_Amazon_Forecast_Service.html)

The following data types are supported by Amazon Forecast Service:

- [Action](https://docs.aws.amazon.com/forecast/latest/dg/API_Action.html): Defines the modifications that you are making to an attribute for a what-if forecast.
- [AdditionalDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_AdditionalDataset.html): Describes an additional dataset.
- [AttributeConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_AttributeConfig.html): Provides information about the method used to transform attributes.
- [Baseline](https://docs.aws.amazon.com/forecast/latest/dg/API_Baseline.html): Metrics you can use as a baseline for comparison purposes.
- [BaselineMetric](https://docs.aws.amazon.com/forecast/latest/dg/API_BaselineMetric.html): An individual metric that you can use for comparison as you evaluate your monitoring results.
- [CategoricalParameterRange](https://docs.aws.amazon.com/forecast/latest/dg/API_CategoricalParameterRange.html): Specifies a categorical hyperparameter and it's range of tunable values.
- [ContinuousParameterRange](https://docs.aws.amazon.com/forecast/latest/dg/API_ContinuousParameterRange.html): Specifies a continuous hyperparameter and it's range of tunable values.
- [DataConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_DataConfig.html): The data configuration for your dataset group and any additional datasets.
- [DataDestination](https://docs.aws.amazon.com/forecast/latest/dg/API_DataDestination.html): The destination for an export job.
- [DatasetGroupSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_DatasetGroupSummary.html): Provides a summary of the dataset group properties used in the ListDatasetGroups operation.
- [DatasetImportJobSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_DatasetImportJobSummary.html): Provides a summary of the dataset import job properties used in the ListDatasetImportJobs operation.
- [DatasetSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_DatasetSummary.html): Provides a summary of the dataset properties used in the ListDatasets operation.
- [DataSource](https://docs.aws.amazon.com/forecast/latest/dg/API_DataSource.html): The source of your data, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast to access the data and, optionally, an AWS Key Management Service (KMS) key.
- [EncryptionConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_EncryptionConfig.html): An AWS Key Management Service (KMS) key and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.
- [ErrorMetric](https://docs.aws.amazon.com/forecast/latest/dg/API_ErrorMetric.html): Provides detailed error metrics to evaluate the performance of a predictor.
- [EvaluationParameters](https://docs.aws.amazon.com/forecast/latest/dg/API_EvaluationParameters.html): Parameters that define how to split a dataset into training data and testing data, and the number of iterations to perform.
- [EvaluationResult](https://docs.aws.amazon.com/forecast/latest/dg/API_EvaluationResult.html): The results of evaluating an algorithm.
- [ExplainabilityConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_ExplainabilityConfig.html): The ExplainabilityConfig data type defines the number of time series and time points included in .
- [ExplainabilityExportSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_ExplainabilityExportSummary.html): Provides a summary of the Explainability export properties used in the operation.
- [ExplainabilityInfo](https://docs.aws.amazon.com/forecast/latest/dg/API_ExplainabilityInfo.html): Provides information about the Explainability resource.
- [ExplainabilitySummary](https://docs.aws.amazon.com/forecast/latest/dg/API_ExplainabilitySummary.html): Provides a summary of the Explainability properties used in the operation.
- [Featurization](https://docs.aws.amazon.com/forecast/latest/dg/API_Featurization.html)
- [FeaturizationConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_FeaturizationConfig.html)
- [FeaturizationMethod](https://docs.aws.amazon.com/forecast/latest/dg/API_FeaturizationMethod.html): Provides information about the method that featurizes (transforms) a dataset field.
- [Filter](https://docs.aws.amazon.com/forecast/latest/dg/API_Filter.html): Describes a filter for choosing a subset of objects.
- [ForecastExportJobSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_ForecastExportJobSummary.html): Provides a summary of the forecast export job properties used in the operation.
- [ForecastSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_ForecastSummary.html): Provides a summary of the forecast properties used in the operation.
- [HyperParameterTuningJobConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_HyperParameterTuningJobConfig.html): Configuration information for a hyperparameter tuning job.
- [InputDataConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_InputDataConfig.html)
- [IntegerParameterRange](https://docs.aws.amazon.com/forecast/latest/dg/API_IntegerParameterRange.html): Specifies an integer hyperparameter and it's range of tunable values.
- [MetricResult](https://docs.aws.amazon.com/forecast/latest/dg/API_MetricResult.html): An individual metric Forecast calculated when monitoring predictor usage.
- [Metrics](https://docs.aws.amazon.com/forecast/latest/dg/API_Metrics.html): Provides metrics that are used to evaluate the performance of a predictor.
- [MonitorConfig](https://docs.aws.amazon.com/forecast/latest/dg/API_MonitorConfig.html): The configuration details for the predictor monitor.
- [MonitorDataSource](https://docs.aws.amazon.com/forecast/latest/dg/API_MonitorDataSource.html): The source of the data the monitor used during the evaluation.
- [MonitorInfo](https://docs.aws.amazon.com/forecast/latest/dg/API_MonitorInfo.html): Provides information about the monitor resource.
- [MonitorSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_MonitorSummary.html): Provides a summary of the monitor properties used in the operation.
- [ParameterRanges](https://docs.aws.amazon.com/forecast/latest/dg/API_ParameterRanges.html): Specifies the categorical, continuous, and integer hyperparameters, and their ranges of tunable values.
- [PredictorBacktestExportJobSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorBacktestExportJobSummary.html): Provides a summary of the predictor backtest export job properties used in the operation.
- [PredictorBaseline](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorBaseline.html): Metrics you can use as a baseline for comparison purposes.
- [PredictorEvent](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorEvent.html): Provides details about a predictor event, such as a retraining.
- [PredictorExecution](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorExecution.html): The algorithm used to perform a backtest and the status of those tests.
- [PredictorExecutionDetails](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorExecutionDetails.html): Contains details on the backtests performed to evaluate the accuracy of the predictor.
- [PredictorMonitorEvaluation](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorMonitorEvaluation.html): Describes the results of a monitor evaluation.
- [PredictorSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_PredictorSummary.html): Provides a summary of the predictor properties that are used in the operation.
- [ReferencePredictorSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_ReferencePredictorSummary.html): Provides a summary of the reference predictor used when retraining or upgrading a predictor.
- [S3Config](https://docs.aws.amazon.com/forecast/latest/dg/API_S3Config.html): The path to the file(s) in an Amazon Simple Storage Service (Amazon S3) bucket, and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access the file(s).
- [Schema](https://docs.aws.amazon.com/forecast/latest/dg/API_Schema.html): Defines the fields of a dataset.
- [SchemaAttribute](https://docs.aws.amazon.com/forecast/latest/dg/API_SchemaAttribute.html): An attribute of a schema, which defines a dataset field.
- [Statistics](https://docs.aws.amazon.com/forecast/latest/dg/API_Statistics.html): Provides statistics for each data field imported into to an Amazon Forecast dataset with the CreateDatasetImportJob operation.
- [SupplementaryFeature](https://docs.aws.amazon.com/forecast/latest/dg/API_SupplementaryFeature.html)
- [Tag](https://docs.aws.amazon.com/forecast/latest/dg/API_Tag.html): The optional metadata that you apply to a resource to help you categorize and organize them.
- [TestWindowSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_TestWindowSummary.html): The status, start time, and end time of a backtest, as well as a failure reason if applicable.
- [TimeAlignmentBoundary](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeAlignmentBoundary.html): The time boundary Forecast uses to align and aggregate your data to match your forecast frequency.
- [TimeSeriesCondition](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeSeriesCondition.html): Creates a subset of items within an attribute that are modified.
- [TimeSeriesIdentifiers](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeSeriesIdentifiers.html): Details about the import file that contains the time series for which you want to create forecasts.
- [TimeSeriesReplacementsDataSource](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeSeriesReplacementsDataSource.html): A replacement dataset is a modified version of the baseline related time series that contains only the values that you want to include in a what-if forecast.
- [TimeSeriesSelector](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeSeriesSelector.html): Defines the set of time series that are used to create the forecasts in a TimeSeriesIdentifiers object.
- [TimeSeriesTransformation](https://docs.aws.amazon.com/forecast/latest/dg/API_TimeSeriesTransformation.html): A transformation function is a pair of operations that select and modify the rows in a related time series.
- [WeightedQuantileLoss](https://docs.aws.amazon.com/forecast/latest/dg/API_WeightedQuantileLoss.html): The weighted loss value for a quantile.
- [WhatIfAnalysisSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_WhatIfAnalysisSummary.html): Provides a summary of the what-if analysis properties used in the operation.
- [WhatIfForecastExportSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_WhatIfForecastExportSummary.html): Provides a summary of the what-if forecast export properties used in the operation.
- [WhatIfForecastSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_WhatIfForecastSummary.html): Provides a summary of the what-if forecast properties used in the operation.
- [WindowSummary](https://docs.aws.amazon.com/forecast/latest/dg/API_WindowSummary.html): The metrics for a time range within the evaluation portion of a dataset.

### [Amazon Forecast Query Service](https://docs.aws.amazon.com/forecast/latest/dg/API_Types_Amazon_Forecast_Query_Service.html)

The following data types are supported by Amazon Forecast Query Service:

- [DataPoint](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_DataPoint.html): The forecast value for a specific date.
- [Forecast](https://docs.aws.amazon.com/forecast/latest/dg/API_forecastquery_Forecast.html): Provides information about a forecast.
- [Common Errors](https://docs.aws.amazon.com/forecast/latest/dg/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/forecast/latest/dg/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
