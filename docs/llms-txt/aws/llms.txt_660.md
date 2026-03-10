# Source: https://docs.aws.amazon.com/personalize/latest/dg/llms.txt

# Amazon Personalize Developer Guide

> Provides a conceptual overview of Amazon Personalize. Includes detailed instructions for using the features and provides a complete API reference for developers.

- [Amazon Personalize and generative AI](https://docs.aws.amazon.com/personalize/latest/dg/personalize-with-gen-ai.html)
- [Readiness checklist](https://docs.aws.amazon.com/personalize/latest/dg/readiness-checklist.html)
- [Creating a dataset group](https://docs.aws.amazon.com/personalize/latest/dg/data-prep-ds-group.html)
- [Creating a schema and a dataset](https://docs.aws.amazon.com/personalize/latest/dg/data-prep-creating-datasets.html)
- [Analyzing training data](https://docs.aws.amazon.com/personalize/latest/dg/analyzing-data.html)
- [Maintaining recommendation relevance](https://docs.aws.amazon.com/personalize/latest/dg/maintaining-relevance.html)
- [Replacing a dataset's schema](https://docs.aws.amazon.com/personalize/latest/dg/updating-dataset-schema.html)
- [Frequently asked questions](https://docs.aws.amazon.com/personalize/latest/dg/frequently-asked-questions.html)
- [Common error messages](https://docs.aws.amazon.com/personalize/latest/dg/error-messages.html)
- [Specifying resources with AWS CloudFormation](https://docs.aws.amazon.com/personalize/latest/dg/creating-resources-with-cloudformation.html)
- [Endpoints and quotas](https://docs.aws.amazon.com/personalize/latest/dg/limits.html)
- [Document history](https://docs.aws.amazon.com/personalize/latest/dg/document-history.html)

## [What is Amazon Personalize?](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html)

- [Guidance for first-time users](https://docs.aws.amazon.com/personalize/latest/dg/first-time-user.html): Provides the recommended order first-time users should follow when reading sections of the Amazon Personalize developer guide.
- [Working with AWS SDKs](https://docs.aws.amazon.com/personalize/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [How it works](https://docs.aws.amazon.com/personalize/latest/dg/how-it-works.html)

- [Amazon Personalize workflow](https://docs.aws.amazon.com/personalize/latest/dg/personalize-workflow.html): Learn about the Amazon Personalize workflow.
- [Amazon Personalize terms](https://docs.aws.amazon.com/personalize/latest/dg/terms.html): Explains Amazon Personalize terms related to data import, model training, and model deployment.
- [Amazon Personalize data](https://docs.aws.amazon.com/personalize/latest/dg/datasets.html): Learn about the types of data you can import into Amazon Personalize datasets


## [Setting up Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/setup.html)

### [Setting up permissions](https://docs.aws.amazon.com/personalize/latest/dg/aws-personalize-set-up-permissions.html)

Set up permissions so your users and Amazon Personalize can access your Amazon Personalize resources.

- [Giving Amazon Personalize permission to access your resources](https://docs.aws.amazon.com/personalize/latest/dg/set-up-required-permissions.html): Give Amazon Personalize permission to access your resources.
- [Giving users permission to access Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/grant-user-permissions.html): Give your users access to Amazon Personalize resources.
- [Giving Amazon Personalize access to Amazon S3 resources](https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html): Use policies to give Amazon Personalize access to your Amazon S3 resources.
- [Giving Amazon Personalize permission to use your AWS KMS key](https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-key-access.html): Use a key policy to give Amazon Personalize permission to use your AWS KMS key.
- [Setting up the AWS CLI](https://docs.aws.amazon.com/personalize/latest/dg/aws-personalize-set-up-aws-cli.html): Set up the AWS CLI to manage Amazon Personalize.
- [Setting up the AWS SDKs](https://docs.aws.amazon.com/personalize/latest/dg/aws-personalize-set-up-sdks.html): Download and install the AWS SDKs that you want to use.


## [Getting started tutorials](https://docs.aws.amazon.com/personalize/latest/dg/getting-started.html)

- [Getting started prerequisites](https://docs.aws.amazon.com/personalize/latest/dg/gs-prerequisites.html): Explains the prerequisites for the getting started exercises.

### [Getting started with a Domain dataset group](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-domain.html)

Start providing personalized movie recommendations for users with a Domain dataset group with recommenders for VIDEO_ON_DEMAND use cases.

- [Getting started with a Domain dataset group (console)](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-console-domain.html): Getting started exercise that uses the Amazon Personalize console to create Domain dataset group and VIDEO_ON_DEMAND recommenders.
- [Getting started with a Domain dataset group (SDK for Java 2.x)](https://docs.aws.amazon.com/personalize/latest/dg/domain-getting-started-java.html): Get started creating domain-based Amazon Personalize resources and get recommendations with the SDK for Java 2.x.
- [Getting started with a Domain dataset group (SDK for Python (Boto3))](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-domain-python.html): Get started creating domain-based Amazon Personalize resources and get recommendations with the SDK for Python (Boto3).
- [Getting started with a Domain dataset group (SDK for JavaScript v3)](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-domain-js.html): Get started creating domain-based Amazon Personalize resources and get recommendations with the SDK for JavaScript v3.

### [Getting started with a Custom dataset group](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-custom.html)

Start providing personalized movie recommendations for users with a Custom dataset group and the User-Personalization recipe.

- [Getting started (console)](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-console.html): Getting started exercise that uses the Amazon Personalize console.
- [Getting started (AWS CLI)](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-cli.html): Getting started exercise that uses the Amazon Personalize CLI.
- [Getting started (SDK for Python (Boto3))](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-python.html): Get started creating custom Amazon Personalize resources and get recommendations with the SDK for Python (Boto3).
- [Getting started (SDK for Java 2.x)](https://docs.aws.amazon.com/personalize/latest/dg/getting-started-java.html): Get started creating custom Amazon Personalize resources and get recommendations with the SDK for Java 2.x.


## [Matching your use case to Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/use-cases-and-recipes.html)

- [Use case and recipe features](https://docs.aws.amazon.com/personalize/latest/dg/use-case-recipe-features.html): Learn about the features Amazon Personalize uses to generate relevant recommendations and improve item discovery and engagement.

### [Choosing a use case](https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html)

Learn about the different recommender use cases available for each domain in a Domain dataset group.

- [VIDEO_ON_DEMAND use cases](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO_ON_DEMAND-use-cases.html): Learn about the different recommender use cases available for the VIDEO_ON_DEMAND domain
- [ECOMMERCE use cases](https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-use-cases.html): Learn about the different recommender use cases available for the ECOMMERCE domain

### [Choosing a recipe](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)

Learn about the Amazon Personalize recipes you can use to train a model and create a personalization system.

- [User-Personalization-v2](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-user-personalization-v2.html): Information about the User-Personalization-v2 custom recipe in Amazon Personalize.
- [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html): Information about the User-Personalization recipe
- [Trending-Now](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-trending-now.html): Use the Amazon Personalize Trending-Now recipe to generate recommendations for items gaining in popularity.
- [Popularity-Count](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-popularity.html): Popularity-Count recommends the most popular items based your interactions data.
- [Personalized-Ranking-v2](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-personalized-ranking-v2.html): Information about the Personalized-Ranking-v2 custom recipe in Amazon Personalize.
- [Personalized-Ranking](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-search.html)
- [Semantic-Similarity](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-semantic-similarity.html): Information about the Semantic-Similarity custom recipe in Amazon Personalize.
- [Similar-Items](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-similar-items.html): Use the Amazon Personalize Similar-Items recipe to generate recommendations for similar items based on interactions data and item metadata.
- [SIMS](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-sims.html)
- [Next-Best-Action](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-next-best-action.html): Use the Next-Best-Action recipe to generate recommendations for the next best actions for your users.
- [Item-Affinity](https://docs.aws.amazon.com/personalize/latest/dg/item-affinity-recipe.html): The Item-Affinity (aws-item-affinity) recipe is a USER_SEGMENTATION recipe that creates a user segment (group of users) for each item that you specify.
- [Item-Attribute-Affinity](https://docs.aws.amazon.com/personalize/latest/dg/item-attribute-affinity-recipe.html): Learn about creating a solution with the Item-Attribute-Affinity recipe to get user segments.

### [Legacy recipes](https://docs.aws.amazon.com/personalize/latest/dg/legacy-user-personalization-recipes.html)

Legacy HRNN recipes are no longer available.

- [AutoML and legacy recipes](https://docs.aws.amazon.com/personalize/latest/dg/training-solution-auto-ml.html): Amazon Personalize can automatically choose the most appropriate hierarchical recurrent neural network (HRNN) recipe based on its analysis of the input data.
- [HRNN](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-hrnn.html)
- [HRNN-Metadata](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-hrnn-metadata.html)
- [HRNN-Coldstart](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-hrnn-coldstart.html)


## [Preparing training data](https://docs.aws.amazon.com/personalize/latest/dg/preparing-training-data.html)

- [Item interaction data](https://docs.aws.amazon.com/personalize/latest/dg/interactions-datasets.html): Learn about item interaction data requirements and how to prepare it for training.
- [Item metadata](https://docs.aws.amazon.com/personalize/latest/dg/items-datasets.html): Learn about item metadata and how to prepare it for Amazon Personalize.
- [User metadata](https://docs.aws.amazon.com/personalize/latest/dg/users-datasets.html): Learn about user metadata requirements and how to prepare it for training.
- [Action metadata](https://docs.aws.amazon.com/personalize/latest/dg/actions-datasets.html): Learn about action metadata requirements and how to prepare it for training.
- [Action interaction data](https://docs.aws.amazon.com/personalize/latest/dg/action-interactions-datasets.html): Learn about action interaction data requirements and how to prepare it for training.


## [Creating schema JSON files](https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html)

### [VIDEO_ON_DEMAND datasets and schemas](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html)

Learn about Amazon Personalize dataset and schema requirements for a VIDEO_ON_DEMAND Domain dataset group.

- [Item interactions dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-interactions-dataset.html): Learn about the data requirements and default schema for Item interactions datasets for VIDEO_ON_DEMAND domains
- [Users dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-users-dataset.html): Learn about the requirements and default schema for Users datasets for VIDEO_ON_DEMAND domains
- [Items dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-items-dataset.html): Learn about the requirements and default schema for Items datasets for VIDEO_ON_DEMAND domains

### [ECOMMERCE datasets and schemas](https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-datasets-and-schemas.html)

Learn about Amazon Personalize dataset and schema requirements for a ECOMMERCE Domain dataset group.

- [Item interactions dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-interactions-dataset.html): Learn about the data requirements and default schema for Item interactions datasets for ECOMMERCE domains
- [Users dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-users-dataset.html): Learn about the requirements and default schema for Users datasets for ECOMMERCE domains
- [Items dataset requirements](https://docs.aws.amazon.com/personalize/latest/dg/ECOMMERCE-items-dataset.html): Learn about the requirements and default schema for Items datasets for ECOMMERCE domains

### [Custom datasets and schemas](https://docs.aws.amazon.com/personalize/latest/dg/custom-datasets-and-schemas.html)

Learn about Amazon Personalize dataset and schema requirements for Custom dataset groups.

- [Item interactions dataset schema requirements](https://docs.aws.amazon.com/personalize/latest/dg/interactions-dataset-requirements.html): Learn about Item interactions dataset schema requirements for Custom dataset groups.
- [Users dataset schema requirements](https://docs.aws.amazon.com/personalize/latest/dg/user-dataset-requirements.html): Learn about Users dataset schema requirements for Custom dataset groups;.
- [Items dataset schema requirements](https://docs.aws.amazon.com/personalize/latest/dg/item-dataset-requirements.html): Learn about Items dataset schema requirements for Custom dataset groups.
- [Actions dataset schema requirements](https://docs.aws.amazon.com/personalize/latest/dg/action-dataset-requirements.html): Learn about Actions dataset schema requirements for Custom dataset groups.
- [Action interactions dataset schema requirements](https://docs.aws.amazon.com/personalize/latest/dg/action-interactions-dataset-requirements.html): Learn about Action interactions dataset schema requirements.


## [Importing training data](https://docs.aws.amazon.com/personalize/latest/dg/import-data.html)

- [Importing bulk data](https://docs.aws.amazon.com/personalize/latest/dg/bulk-data-import-step.html): After you have formatted your input data (see ) and completed , you are ready to import your bulk data with a dataset import job.

### [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/personalize/latest/dg/preparing-importing-with-data-wrangler.html)

Use Amazon SageMaker AI Data Wrangler to import data from 40+ sources into Amazon Personalize datasets.

- [Setting up permissions](https://docs.aws.amazon.com/personalize/latest/dg/dw-data-prep-minimum-permissions.html): To prepare data with Data Wrangler, you must set up the following permissions:
- [Launching Data Wrangler from Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/dw-launch-dw-from-personalize.html): To launch Data Wrangler from Amazon Personalize, you use the Amazon Personalize console to configure a SageMaker AI domain and launch Data Wrangler.
- [Importing data into Data Wrangler](https://docs.aws.amazon.com/personalize/latest/dg/dw-import-data.html): After you configure a SageMaker AI domain and launch Data Wrangler in a new tab, you are ready to import data from your source into Data Wrangler.
- [Transforming data](https://docs.aws.amazon.com/personalize/latest/dg/dw-transform-data.html): To transform data in Data Wrangler, you add a Transform step to your data flow.
- [Generating visualizations and data insights](https://docs.aws.amazon.com/personalize/latest/dg/dw-analyze-data.html): After you import your data into Data Wrangler, you can use it to generate visualizations and data insights.
- [Processing data and importing it into Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/dw-export-data.html): When you are finished analyzing and transforming your data, you are ready to process it and import it into Amazon Personalize.

### [Importing individual records](https://docs.aws.amazon.com/personalize/latest/dg/incremental-data-updates.html)

Import small batches of interaction events, items, or users into an Amazon Personalize dataset before training.

- [Importing interactions individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-interactions.html): Import interaction events individually into an Amazon Personalize Interactions dataset.
- [Importing users individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-users.html): Individually import one or more users into an Amazon Personalize Users dataset before creating a solution and a solution version.
- [Importing items individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-items.html): Individually import one or more items into an Amazon Personalize Items dataset before creating a solution and a solution version.
- [Importing actions individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-actions.html): Individually import one or more actions into an Amazon Personalize Actions dataset before creating a solution and a solution version.


## [Domain recommenders](https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html)

- [Creating domain recommenders](https://docs.aws.amazon.com/personalize/latest/dg/creating-domain-recommenders.html): Learn how to create a recommender for an Amazon Personalize domain use case.
- [Enabling metadata in recommendations](https://docs.aws.amazon.com/personalize/latest/dg/create-recommender-return-metadata.html): Learn how to enable metadata in recommendations for a domain recommender.
- [Configuring columns used when training](https://docs.aws.amazon.com/personalize/latest/dg/create-recommender-configure-columns.html): When you create a recommender, you can modify the columns Amazon Personalize considers when training the models backing your recommender.
- [Configuring exploration for a domain recommender](https://docs.aws.amazon.com/personalize/latest/dg/create-recommender-configure-exploration.html): Learn how to configure a recommender's exploration.
- [Evaluating a domain recommender](https://docs.aws.amazon.com/personalize/latest/dg/evaluating-recommenders.html): Evaluate a Amazon Personalize recommender based on performance metrics.
- [Updating a recommender](https://docs.aws.amazon.com/personalize/latest/dg/updating-recommender.html): Learn about updating the configuration details of a recommender
- [Stopping a recommender](https://docs.aws.amazon.com/personalize/latest/dg/stopping-starting-recommender.html): Stop and start Amazon Personalize recommenders so that you only pay for recommenders that you use.


## [Custom resources](https://docs.aws.amazon.com/personalize/latest/dg/create-custom-resources.html)

### [Configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html)

Configure a custom Amazon Personalize solution before training to customize it for your business needs.

- [Creating a solution](https://docs.aws.amazon.com/personalize/latest/dg/create-solution.html): Learn how to create and configure a custom Amazon Personalize solution
- [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html): Learn how to configure automatic training and training frequency for an Amazon Personalize solution.
- [Configuring columns used when training](https://docs.aws.amazon.com/personalize/latest/dg/custom-config-columns.html): Configure the columns Amazon Personalize uses when creating a solution version (trained model)
- [Optimizing a solution for an additional objective](https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-for-objective.html): Optimize an Amazon Personalize solution for an objective in addition to maximum relevance, such as maximizing revenue, before training.
- [Optimizing a solution with events configuration](https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-events-config.html): Optimize an Amazon Personalize solution with events configuration.
- [Hyperparameters and HPO](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config-hpo.html): Provides information about overriding default parameters of a recipe and hyperparameter optimization.
- [Choosing the item interaction data used for training](https://docs.aws.amazon.com/personalize/latest/dg/event-values-types.html): Choose the item interaction data in an Item interactions dataset that Amazon Personalize uses to create a solution version (train a model)
- [Cloning a solution (console)](https://docs.aws.amazon.com/personalize/latest/dg/cloning-solution.html): Clone an Amazon Personalize solution to reuse the existing solution's configuration, including recipe and hyperparameters.
- [Updating a solution](https://docs.aws.amazon.com/personalize/latest/dg/updating-solution.html): Update an Amazon Personalize solution to change its automatic training configuration.
- [Manually creating a solution version](https://docs.aws.amazon.com/personalize/latest/dg/creating-a-solution-version.html): Train a model that Amazon Personalize will use to generate personalized recommendations.
- [Stopping the creation of a solution version](https://docs.aws.amazon.com/personalize/latest/dg/stop-solution-version.html): Stop creating an Amazon Personalize solution version (training a model).
- [Evaluating a solution version](https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html): Evaluate a Amazon Personalize solution version (model) based on performance metrics.
- [Creating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html): Create an Amazon Personalize campaign to deploy a solution version (trained model).
- [Updating a campaign](https://docs.aws.amazon.com/personalize/latest/dg/update-campaigns.html): Update an Amazon Personalize campaign's configuration.


## [Getting recommendations](https://docs.aws.amazon.com/personalize/latest/dg/getting-recommendations.html)

### [Real-time item recommendations](https://docs.aws.amazon.com/personalize/latest/dg/recommendations.html)

Get real-time recommendations from an Amazon Personalize recommender or campaign.

- [Getting real-time item recommendations](https://docs.aws.amazon.com/personalize/latest/dg/getting-real-time-item-recommendations.html): You can get real-time item recommendations from an Amazon Personalize recommender or custom campaign with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.
- [Getting item metadata with recommendations](https://docs.aws.amazon.com/personalize/latest/dg/getting-recommendations-with-metadata.html): Learn how to specify the metadata columns to include in Amazon Personalize recommendations.
- [Promoting items](https://docs.aws.amazon.com/personalize/latest/dg/promoting-items.html): Use a promotion to apply a filter to a configurable subset of items in recommendations.
- [Real-time action recommendations](https://docs.aws.amazon.com/personalize/latest/dg/get-action-recommendations.html): Get action recommendations from an Amazon Personalize custom campaign.

### [Getting a personalized ranking (custom resources)](https://docs.aws.amazon.com/personalize/latest/dg/rankings.html)

Get a re-ranked list of recommended items for a specific user from an Amazon Personalize campaign.

- [Getting a personalized ranking (console)](https://docs.aws.amazon.com/personalize/latest/dg/get-ranking-recommendations-console.html): Get a personalized ranking from a campaign using the Amazon Personalize console.
- [Getting a personalized ranking (AWS CLI)](https://docs.aws.amazon.com/personalize/latest/dg/get-personalized-rankings-cli.html): Get a personalized ranking from an Amazon Personalize campaign using the AWS CLI.
- [Getting a personalized ranking (AWS SDKs)](https://docs.aws.amazon.com/personalize/latest/dg/get-personalized-rankings-sdk.html): Get a personalized ranking from an Amazon Personalize campaign with the AWS SDKs.
- [Using contextual metadata](https://docs.aws.amazon.com/personalize/latest/dg/contextual-metadata.html): Learn how to increase recommendation relevance with contextual metadata.

### [Getting batch item recommendations](https://docs.aws.amazon.com/personalize/latest/dg/getting-batch-recommendations.html)

Learn about getting batch item recommendations in Amazon Personalize.

- [Batch recommendations with themes](https://docs.aws.amazon.com/personalize/latest/dg/themed-batch-recommendations.html): Get batch recommendations with themes when you use the Similar-Items recipe.
- [Preparing input data for batch recommendations](https://docs.aws.amazon.com/personalize/latest/dg/batch-data-upload.html): Learn about formatting the input JSON file that batch inference jobs use to make recommendations.
- [Creating a batch inference job](https://docs.aws.amazon.com/personalize/latest/dg/creating-batch-inference-job.html): Create batch inference jobs to get item recommendations based on batch input data.
- [Batch inference job output examples](https://docs.aws.amazon.com/personalize/latest/dg/batch-inference-job-output-examples.html): Learn about the format of the output JSON from a batch inference job.

### [Getting batch user segments](https://docs.aws.amazon.com/personalize/latest/dg/getting-user-segments.html)

Learn about getting user segments in Amazon Personalize.

- [Preparing input data for user segments](https://docs.aws.amazon.com/personalize/latest/dg/prepare-input-data-user-segment.html): Learn about formatting the input JSON file that batch segment jobs use to make user segments.
- [Creating a batch segment job](https://docs.aws.amazon.com/personalize/latest/dg/creating-batch-seg-job.html): Create batch segment jobs to get user segments grouped based on your item input data.
- [Batch segment job output format examples](https://docs.aws.amazon.com/personalize/latest/dg/batch-segment-job-output-examples.html): Learn about the format of the output JSON from a batch segment job.


## [Filtering results](https://docs.aws.amazon.com/personalize/latest/dg/filter.html)

### [Filter expressions](https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html)

Create filter expressions to include or exclude items from recommendations and users from user segments.

- [Guidelines and requirements](https://docs.aws.amazon.com/personalize/latest/dg/filter-expression-guidelines-requirements.html): Learn about the guidelines and requirements for creating Amazon Personalize filters.
- [Filter expression structure and elements](https://docs.aws.amazon.com/personalize/latest/dg/creating-filter-expressions.html): Learn about the structure of Amazon Personalize filter expressions and their elements

### [Filter expression examples](https://docs.aws.amazon.com/personalize/latest/dg/filter-expression-examples.html)

Use the filter expressions in the following sections to learn how to build your own filter expressions.

- [Item recommendation filter expression examples](https://docs.aws.amazon.com/personalize/latest/dg/item-recommendation-filter-examples.html): Lists examples you can use to get started filtering item recommendations.
- [User segment filter expressions](https://docs.aws.amazon.com/personalize/latest/dg/user-segment-filter-examples.html): Lists examples you can use to get started filtering user segments.
- [Action recommendation filter expression examples](https://docs.aws.amazon.com/personalize/latest/dg/action-recommendation-filter-examples.html): Lists examples you can use to get started filtering action recommendations.
- [Combining multiple expressions](https://docs.aws.amazon.com/personalize/latest/dg/multiple-expression-example.html): Learn how to create a filter with a combination of multiple filter expressions.
- [Filtering real-time recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter-real-time.html): Learn how to filter real-time recommendations from an Amazon Personalize campaign.
- [Filtering batch recommendations and user segments (custom resources)](https://docs.aws.amazon.com/personalize/latest/dg/filter-batch.html): Learn how to apply a Amazon Personalize filter to batch recommendations and user segments.


## [Recording events](https://docs.aws.amazon.com/personalize/latest/dg/recording-events.html)

### [Recording item interaction events](https://docs.aws.amazon.com/personalize/latest/dg/recording-item-interaction-events.html)

Use the PutEvents operation to influence Amazon Personalize item recommendations with real-time item interactions events.

- [Creating an item interaction event tracker](https://docs.aws.amazon.com/personalize/latest/dg/event-get-tracker.html): Create an item interaction event tracker so Amazon Personalize knows where to store your new item interaction data.
- [Recording a single item interaction event](https://docs.aws.amazon.com/personalize/latest/dg/putevents-example.html): Learn how use the AWS SDKs or AWS Command Line Interface to record a single event for Amazon Personalize.
- [Recording multiple item interaction events with event value data](https://docs.aws.amazon.com/personalize/latest/dg/recording-events-example-event-value.html): Learn how to stream multiple item interaction events with different event types and different event values.
- [Recording item interaction events with impressions data](https://docs.aws.amazon.com/personalize/latest/dg/putevents-including-impressions-data.html): Learn how to record impressions data in your PutEvents operation.
- [Event metrics and attribution reports](https://docs.aws.amazon.com/personalize/latest/dg/event-metrics.html): Learn how to monitor events sent to Amazon Personalize and generate metric attribution reports.

### [Recording action interaction events](https://docs.aws.amazon.com/personalize/latest/dg/recording-action-interaction-events.html)

Use the PutActionInteractions operation to record real-time action interaction events to influence Amazon Personalize action recommendations.

- [Action interaction event tracker ID](https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html): Learn how to find the ID of your event tracker.
- [Recording a single action interaction event](https://docs.aws.amazon.com/personalize/latest/dg/record-single-action-interaction.html): Learn how to use the AWS SDKs or AWS Command Line Interface to record a single action interaction event for Amazon Personalize.
- [Recording multiple action interaction events](https://docs.aws.amazon.com/personalize/latest/dg/recording-multiple-action-interactions.html): Learn how to stream multiple action interaction events with different event types.


## [Updating data in datasets after training](https://docs.aws.amazon.com/personalize/latest/dg/updating-datasets.html)

- [How new data influences real-time recommendations](https://docs.aws.amazon.com/personalize/latest/dg/how-new-data-influences-recommendations.html): Learn how Amazon Personalize uses data you import after you train a model.
- [How new data influences batch recommendations (custom resources)](https://docs.aws.amazon.com/personalize/latest/dg/how-new-data-influences-batch-recommendations.html): Learn how Amazon Personalize uses data you import after you train a model.


## [Exporting data](https://docs.aws.amazon.com/personalize/latest/dg/export-data.html)

- [Dataset export job permissions requirements](https://docs.aws.amazon.com/personalize/latest/dg/export-permissions.html): Learn about the permissions requirements for an Amazon Personalize dataset export job.
- [Creating a dataset export job in Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/create-dataset-export-job.html): Learn about how to create an Amazon Personalize dataset export job with the console, AWS CLI, or AWS SDKs.


## [Deleting resources](https://docs.aws.amazon.com/personalize/latest/dg/deleting-resources.html)

- [Deleting users](https://docs.aws.amazon.com/personalize/latest/dg/delete-records.html): Delete users and their data from your dataset group.
- [Deleting a dataset](https://docs.aws.amazon.com/personalize/latest/dg/delete-dataset.html): Delete a dataset to delete data you imported into Amazon Personalize.


## [Measuring impact of recommendations](https://docs.aws.amazon.com/personalize/latest/dg/measuring-recommendation-impact.html)

### [Measuring recommendation impact with a metric attribution](https://docs.aws.amazon.com/personalize/latest/dg/metric-attributions.html)

Create a metric attribution to measure the impact of recommendations from a campaign or a recommender.

- [Guidelines and requirements](https://docs.aws.amazon.com/personalize/latest/dg/metric-attribution-requirements.html): Requirements for using a metric attribution to measure the impact of recommendations
- [Creating a metric attribution](https://docs.aws.amazon.com/personalize/latest/dg/creating-metric-attribution.html): Create a metric attribution to start sending reports to CloudWatch and Amazon S3.
- [Updating a metric attribution](https://docs.aws.amazon.com/personalize/latest/dg/updating-metric-attribution.html): Learn about updating a metric attribution to add and remove metrics and modify the output configuration.
- [Deleting a metric attribution](https://docs.aws.amazon.com/personalize/latest/dg/deleting-metric-attribution.html): Learn about deleting metric attribution and stopping sending reports to CloudWatch.
- [Viewing graphs of metric data in CloudWatch](https://docs.aws.amazon.com/personalize/latest/dg/metric-attribution-results-cloudwatch.html): Learn how to view metrics for PutEvents data and incremental bulk data in CloudWatch.
- [Publishing metric attribution reports to Amazon S3](https://docs.aws.amazon.com/personalize/latest/dg/metric-attribution-results-s3.html): Learn how to publish metric attribution reports to Amazon S3.

### [Measuring recommendation impact with A/B testing](https://docs.aws.amazon.com/personalize/latest/dg/ab-testing-recommendations.html)

Learn how to perform A/B tests to measure the impact of Amazon Personalize recommendations.

- [A/B testing with CloudWatch Evidently](https://docs.aws.amazon.com/personalize/latest/dg/ab-testing-evidently.html): Learn about performing A/B testing on recommendations with CloudWatch Evidently.


## [Personalizing search results from OpenSearch](https://docs.aws.amazon.com/personalize/latest/dg/personalize-opensearch.html)

- [Plugin requirements](https://docs.aws.amazon.com/personalize/latest/dg/plugin-requirements.html): Learn about the guidelines and requirements for using the plugin to personalize results from OpenSearch.

### [Personalizing results from Amazon OpenSearch Service](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-service.html)

Learn how to personalize results from Amazon OpenSearch Service

### [Setting up permissions](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-granting-access-managed.html)

Set up access to your Amazon Personalize resources from Amazon OpenSearch Service.

- [Configuring permissions when resources are in the same account](https://docs.aws.amazon.com/personalize/latest/dg/service-role-managed.html): Create an IAM service role for OpenSearch Service and grant it the required permissions.
- [Configuring permissions when resources are in different accounts](https://docs.aws.amazon.com/personalize/latest/dg/configuring-multiple-accounts.html): If your OpenSearch Service and Amazon Personalize resources are in separate accounts, you create an IAM role in each account and grant the role access to the resources in the account.
- [Configuring Amazon OpenSearch Service domain security](https://docs.aws.amazon.com/personalize/latest/dg/domain-user-managed.html): Configure your OpenSearch Service so your user or role can get personalized search results.
- [Installing the plugin](https://docs.aws.amazon.com/personalize/latest/dg/open-search-install-managed.html): Learn how to install the Amazon Personalize Search Ranking plugin on an OpenSearch Service domain.
- [Creating a pipeline](https://docs.aws.amazon.com/personalize/latest/dg/managed-opensearch-plugin-pipeline-example.html): Create a search pipeline with a personalized_search_ranking response processor on an OpenSearch Service domain.
- [Applying the plugin](https://docs.aws.amazon.com/personalize/latest/dg/managed-apply-plugin.html): Learn how to apply the Amazon Personalize Search Ranking plugin to OpenSearch Service queries.
- [Comparing results](https://docs.aws.amazon.com/personalize/latest/dg/managed-comparing-results.html): Run OpenSearch Service queries with and without personalization and compare the results.
- [Monitoring the plugin](https://docs.aws.amazon.com/personalize/latest/dg/managed-monitor.html): Monitor the Amazon Personalize Search Ranking plugin with OpenSearch Service pipeline statistics.

### [Personalizing results from open source Open Search](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-open-source.html)

Learn how to personalize results from open source OpenSearch with Amazon Personalize

- [Setting up permissions](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-granting-access.html): Set up access to your Amazon Personalize resources from your open source OpenSearch cluster.
- [Manually installing the plugin on an existing OpenSearch cluster](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-manual-install.html): Learn how to manually install the Amazon Personalize Search Ranking plugin on an existing OpenSearch cluster
- [Creating a new cluster and installing the plugin with a script](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-install-with-script.html): Run a bash script that creates an OpenSearch cluster and installs the plugin.
- [Creating a pipeline](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-plugin-pipeline-example.html): Create a search pipeline with a personalized_search_ranking response processor on an open source OpenSearch cluster.
- [Applying the plugin](https://docs.aws.amazon.com/personalize/latest/dg/opensource-apply-plugin.html): Learn how to apply the Amazon Personalize Search Ranking plugin to queries in OpenSearch open source.
- [Comparing results](https://docs.aws.amazon.com/personalize/latest/dg/opensource-comparing-results.html): Compare results from open source with personalized results.
- [Monitoring the plugin](https://docs.aws.amazon.com/personalize/latest/dg/opensource-monitor.html): Monitor the Amazon Personalize Search Ranking plugin with open source OpenSearch pipeline statistics.
- [Personalized search ranking fields](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-plugin-pipeline-fields.html): Learn about the fields for the personalized_search_ranking response processor.
- [Pipeline metrics example](https://docs.aws.amazon.com/personalize/latest/dg/monitor-response.html): As you apply the Amazon Personalize Search Ranking plugin to OpenSearch queries, you can monitor the plugin by getting metrics for your search pipelines.


## [Tagging resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html)

- [Guidelines and requirements](https://docs.aws.amazon.com/personalize/latest/dg/personalize-managing-tags.html): Learn about AWS tags and their restrictions.
- [Adding tags to Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tags-add.html): Add AWS tags to new and existing Amazon Personalize resources, such as a dataset group.
- [Removing tags from Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tags-remove.html): Remove AWS tags from Amazon Personalize resources, such as a dataset group.
- [Using tags in IAM policies](https://docs.aws.amazon.com/personalize/latest/dg/tags-iam.html): Apply tag-based permissions to AWS Identity and Access Management (IAM) policies and API operations.


## [Code examples](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples.html)

### [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize.html)

Code examples that show how to use Amazon Personalize with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize_basics.html)

The following code examples show how to use the basics of Amazon Personalize with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize_actions.html)

The following code examples show how to use Amazon Personalize with AWS SDKs.

- [CreateBatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateBatchInferenceJob_section.html): Use CreateBatchInferenceJob with an AWS SDK
- [CreateBatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateBatchSegmentJob_section.html): Use CreateBatchSegmentJob with an AWS SDK
- [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateCampaign_section.html): Use CreateCampaign with an AWS SDK
- [CreateDataset](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateDataset_section.html): Use CreateDataset with an AWS SDK
- [CreateDatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateDatasetExportJob_section.html): Use CreateDatasetExportJob with an AWS SDK
- [CreateDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateDatasetGroup_section.html): Use CreateDatasetGroup with an AWS SDK
- [CreateDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateDatasetImportJob_section.html): Use CreateDatasetImportJob with an AWS SDK
- [CreateEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateEventTracker_section.html): Use CreateEventTracker with an AWS SDK
- [CreateFilter](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateFilter_section.html): Use CreateFilter with an AWS SDK
- [CreateRecommender](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateRecommender_section.html): Use CreateRecommender with an AWS SDK
- [CreateSchema](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateSchema_section.html): Use CreateSchema with an AWS SDK
- [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateSolution_section.html): Use CreateSolution with an AWS SDK
- [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_CreateSolutionVersion_section.html): Use CreateSolutionVersion with an AWS SDK
- [DeleteCampaign](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DeleteCampaign_section.html): Use DeleteCampaign with an AWS SDK
- [DeleteEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DeleteEventTracker_section.html): Use DeleteEventTracker with an AWS SDK
- [DeleteSolution](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DeleteSolution_section.html): Use DeleteSolution with an AWS SDK
- [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DescribeCampaign_section.html): Use DescribeCampaign with an AWS SDK
- [DescribeRecipe](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DescribeRecipe_section.html): Use DescribeRecipe with an AWS SDK
- [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_DescribeSolution_section.html): Use DescribeSolution with an AWS SDK
- [ListCampaigns](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_ListCampaigns_section.html): Use ListCampaigns with an AWS SDK
- [ListDatasetGroups](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_ListDatasetGroups_section.html): Use ListDatasetGroups with an AWS SDK
- [ListRecipes](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_ListRecipes_section.html): Use ListRecipes with an AWS SDK
- [ListSolutions](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_ListSolutions_section.html): Use ListSolutions with an AWS SDK
- [UpdateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/personalize_example_personalize_UpdateCampaign_section.html): Use UpdateCampaign with an AWS SDK

### [Amazon Personalize Events](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-events.html)

Code examples that show how to use Amazon Personalize Events with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-events_basics.html)

The following code examples show how to use the basics of Amazon Personalize Events with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-events_actions.html)

The following code examples show how to use Amazon Personalize Events with AWS SDKs.

- [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/personalize-events_example_personalize-events_PutEvents_section.html): Use PutEvents with an AWS SDK
- [PutItems](https://docs.aws.amazon.com/personalize/latest/dg/personalize-events_example_personalize-events_PutItems_section.html): Use PutItems with an AWS SDK
- [PutUsers](https://docs.aws.amazon.com/personalize/latest/dg/personalize-events_example_personalize-events_PutUsers_section.html): Use PutUsers with an AWS SDK

### [Amazon Personalize Runtime](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-runtime.html)

Code examples that show how to use Amazon Personalize Runtime with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-runtime_basics.html)

The following code examples show how to use the basics of Amazon Personalize Runtime with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/personalize/latest/dg/service_code_examples_personalize-runtime_actions.html)

The following code examples show how to use Amazon Personalize Runtime with AWS SDKs.

- [GetPersonalizedRanking](https://docs.aws.amazon.com/personalize/latest/dg/personalize-runtime_example_personalize-runtime_GetPersonalizedRanking_section.html): Use GetPersonalizedRanking with an AWS SDK
- [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/personalize-runtime_example_personalize-runtime_GetRecommendations_section.html): Use GetRecommendations with an AWS SDK


## [Security](https://docs.aws.amazon.com/personalize/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/personalize/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Personalize.

- [Data encryption in Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/data-encryption.html): Learn about where Amazon Personalize uses data encryption to protect your data.

### [Identity and Access Management](https://docs.aws.amazon.com/personalize/latest/dg/security-iam.html)

How to authenticate requests and manage access to your Amazon Personalize resources.

- [How Amazon Personalize works with IAM](https://docs.aws.amazon.com/personalize/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Personalize, learn what IAM features are available to use with Amazon Personalize.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/personalize/latest/dg/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Identity-based policy examples](https://docs.aws.amazon.com/personalize/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Personalize resources.
- [Troubleshooting](https://docs.aws.amazon.com/personalize/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Personalize and IAM.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/personalize/latest/dg/personalize-monitoring.html)

Learn about using Amazon CloudWatch to get metrics associated with Amazon Personalize

- [CloudWatch metrics for Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/cloudwatch-metrics.html): This section contains information about the Amazon CloudWatch metrics available for Amazon Personalize.
- [Logging Amazon Personalize API calls with AWS CloudTrail](https://docs.aws.amazon.com/personalize/latest/dg/logging-using-cloudtrail.html): Amazon Personalize is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Personalize.
- [Compliance validation](https://docs.aws.amazon.com/personalize/latest/dg/personalize-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/personalize/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Personalize features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/personalize/latest/dg/infrastructure-security.html): Learn how Amazon Personalize isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/personalize/latest/dg/vpc-interface-endpoints.html): Use an interface Amazon VPC endpoint to create a private connection between your VPC and Amazon Personalize.


## [API reference](https://docs.aws.amazon.com/personalize/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/personalize/latest/dg/API_Operations.html)

The following actions are supported by Amazon Personalize:

### [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/API_Operations_Amazon_Personalize.html)

The following actions are supported by Amazon Personalize:

- [CreateBatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateBatchInferenceJob.html): Generates batch recommendations based on a list of items or users stored in Amazon S3 and exports the recommendations to an Amazon S3 bucket.
- [CreateBatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateBatchSegmentJob.html): Creates a batch segment job.
- [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html)
- [CreateDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataDeletionJob.html): Creates a batch job that deletes all references to specific users from an Amazon Personalize dataset group in batches.
- [CreateDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html): Creates an empty dataset and adds it to the specified dataset group.
- [CreateDatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetExportJob.html): Creates a job that exports data from your dataset to an Amazon S3 bucket.
- [CreateDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html): Creates an empty dataset group.
- [CreateDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html): Creates a job that imports training data from your data source (an Amazon S3 bucket) to an Amazon Personalize dataset.
- [CreateEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateEventTracker.html): Creates an event tracker that you use when adding event data to a specified dataset group using the PutEvents API.
- [CreateFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateFilter.html): Creates a recommendation filter.
- [CreateMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateMetricAttribution.html): Creates a metric attribution.
- [CreateRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateRecommender.html): Creates a recommender with the recipe (a Domain dataset group use case) you specify.
- [CreateSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSchema.html): Creates an Amazon Personalize schema from the specified schema string.
- [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html)
- [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html): Trains or retrains an active solution in a Custom dataset group.
- [DeleteCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteCampaign.html): Removes a campaign by deleting the solution deployment.
- [DeleteDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html): Deletes a dataset.
- [DeleteDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDatasetGroup.html): Deletes a dataset group.
- [DeleteEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteEventTracker.html): Deletes the event tracker.
- [DeleteFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteFilter.html): Deletes a filter.
- [DeleteMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteMetricAttribution.html): Deletes a metric attribution.
- [DeleteRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteRecommender.html): Deactivates and removes a recommender.
- [DeleteSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSchema.html): Deletes a schema.
- [DeleteSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html): Deletes all versions of a solution and the Solution object itself.
- [DescribeAlgorithm](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeAlgorithm.html): Describes the given algorithm.
- [DescribeBatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeBatchInferenceJob.html): Gets the properties of a batch inference job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate the recommendations.
- [DescribeBatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeBatchSegmentJob.html): Gets the properties of a batch segment job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate segments.
- [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html): Describes the given campaign, including its status.
- [DescribeDataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataDeletionJob.html): Describes the data deletion job created by CreateDataDeletionJob, including the job status.
- [DescribeDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html): Describes the given dataset.
- [DescribeDatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetExportJob.html): Describes the dataset export job created by CreateDatasetExportJob, including the export job status.
- [DescribeDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetGroup.html): Describes the given dataset group.
- [DescribeDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDatasetImportJob.html): Describes the dataset import job created by CreateDatasetImportJob, including the import job status.
- [DescribeEventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeEventTracker.html): Describes an event tracker.
- [DescribeFeatureTransformation](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeFeatureTransformation.html): Describes the given feature transformation.
- [DescribeFilter](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeFilter.html): Describes a filter's properties.
- [DescribeMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeMetricAttribution.html): Describes a metric attribution.
- [DescribeRecipe](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecipe.html): Describes a recipe.
- [DescribeRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeRecommender.html): Describes the given recommender, including its status.
- [DescribeSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSchema.html): Describes a schema.
- [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html): Describes a solution.
- [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html): Describes a specific version of a solution.
- [GetSolutionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_GetSolutionMetrics.html): Gets the metrics for the specified solution version.
- [ListBatchInferenceJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListBatchInferenceJobs.html): Gets a list of the batch inference jobs that have been performed off of a solution version.
- [ListBatchSegmentJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListBatchSegmentJobs.html): Gets a list of the batch segment jobs that have been performed off of a solution version that you specify.
- [ListCampaigns](https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html): Returns a list of campaigns that use the given solution.
- [ListDataDeletionJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDataDeletionJobs.html): Returns a list of data deletion jobs for a dataset group ordered by creation time, with the most recent first.
- [ListDatasetExportJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetExportJobs.html): Returns a list of dataset export jobs that use the given dataset.
- [ListDatasetGroups](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetGroups.html): Returns a list of dataset groups.
- [ListDatasetImportJobs](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasetImportJobs.html): Returns a list of dataset import jobs that use the given dataset.
- [ListDatasets](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html): Returns the list of datasets contained in the given dataset group.
- [ListEventTrackers](https://docs.aws.amazon.com/personalize/latest/dg/API_ListEventTrackers.html): Returns the list of event trackers associated with the account.
- [ListFilters](https://docs.aws.amazon.com/personalize/latest/dg/API_ListFilters.html): Lists all filters that belong to a given dataset group.
- [ListMetricAttributionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_ListMetricAttributionMetrics.html): Lists the metrics for the metric attribution.
- [ListMetricAttributions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListMetricAttributions.html): Lists metric attributions.
- [ListRecipes](https://docs.aws.amazon.com/personalize/latest/dg/API_ListRecipes.html): Returns a list of available recipes.
- [ListRecommenders](https://docs.aws.amazon.com/personalize/latest/dg/API_ListRecommenders.html): Returns a list of recommenders in a given Domain dataset group.
- [ListSchemas](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSchemas.html): Returns the list of schemas associated with the account.
- [ListSolutions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html): Returns a list of solutions in a given dataset group.
- [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html): Returns a list of solution versions for the given solution.
- [ListTagsForResource](https://docs.aws.amazon.com/personalize/latest/dg/API_ListTagsForResource.html): Get a list of tags attached to a resource.
- [StartRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_StartRecommender.html): Starts a recommender that is INACTIVE.
- [StopRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_StopRecommender.html): Stops a recommender that is ACTIVE.
- [StopSolutionVersionCreation](https://docs.aws.amazon.com/personalize/latest/dg/API_StopSolutionVersionCreation.html): Stops creating a solution version that is in a state of CREATE_PENDING or CREATE IN_PROGRESS.
- [TagResource](https://docs.aws.amazon.com/personalize/latest/dg/API_TagResource.html): Add a list of tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/personalize/latest/dg/API_UntagResource.html): Removes the specified tags that are attached to a resource.
- [UpdateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateCampaign.html): Updates a campaign to deploy a retrained solution version with an existing campaign, change your campaign's minProvisionedTPS, or modify your campaign's configuration.
- [UpdateDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateDataset.html): Update a dataset to replace its schema with a new or existing one.
- [UpdateMetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateMetricAttribution.html): Updates a metric attribution.
- [UpdateRecommender](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateRecommender.html): Updates the recommender to modify the recommender configuration.
- [UpdateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html): Updates an Amazon Personalize solution to use a different automatic training configuration.

### [Amazon Personalize Events](https://docs.aws.amazon.com/personalize/latest/dg/API_Operations_Amazon_Personalize_Events.html)

The following actions are supported by Amazon Personalize Events:

- [PutActionInteractions](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutActionInteractions.html): Records action interaction event data.
- [PutActions](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutActions.html): Adds one or more actions to an Actions dataset.
- [PutEvents](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html): Records item interaction event data.
- [PutItems](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutItems.html): Adds one or more items to an Items dataset.
- [PutUsers](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutUsers.html): Adds one or more users to a Users dataset.

### [Amazon Personalize Runtime](https://docs.aws.amazon.com/personalize/latest/dg/API_Operations_Amazon_Personalize_Runtime.html)

The following actions are supported by Amazon Personalize Runtime:

- [GetActionRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetActionRecommendations.html): Returns a list of recommended actions in sorted in descending order by prediction score.
- [GetPersonalizedRanking](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetPersonalizedRanking.html): Re-ranks a list of recommended items for the given user.
- [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html): Returns a list of recommended items.

### [Data Types](https://docs.aws.amazon.com/personalize/latest/dg/API_Types.html)

The following data types are supported by Amazon Personalize:

### [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/API_Types_Amazon_Personalize.html)

The following data types are supported by Amazon Personalize:

- [Algorithm](https://docs.aws.amazon.com/personalize/latest/dg/API_Algorithm.html): Describes a custom algorithm.
- [AlgorithmImage](https://docs.aws.amazon.com/personalize/latest/dg/API_AlgorithmImage.html): Describes an algorithm image.
- [AutoMLConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html): When the solution performs AutoML (performAutoML is true in CreateSolution), Amazon Personalize determines which recipe, from the specified list, optimizes the given metric.
- [AutoMLResult](https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLResult.html): When the solution performs AutoML (performAutoML is true in CreateSolution), specifies the recipe that best optimized the specified metric.
- [AutoTrainingConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_AutoTrainingConfig.html): The automatic training configuration to use when performAutoTraining is true.
- [BatchInferenceJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJob.html): Contains information on a batch inference job.
- [BatchInferenceJobConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJobConfig.html): The configuration details of a batch inference job.
- [BatchInferenceJobInput](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJobInput.html): The input configuration of a batch inference job.
- [BatchInferenceJobOutput](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJobOutput.html): The output configuration parameters of a batch inference job.
- [BatchInferenceJobSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchInferenceJobSummary.html): A truncated version of the BatchInferenceJob.
- [BatchSegmentJob](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJob.html): Contains information on a batch segment job.
- [BatchSegmentJobInput](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJobInput.html): The input configuration of a batch segment job.
- [BatchSegmentJobOutput](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJobOutput.html): The output configuration parameters of a batch segment job.
- [BatchSegmentJobSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_BatchSegmentJobSummary.html): A truncated version of the BatchSegmentJob datatype.
- [Campaign](https://docs.aws.amazon.com/personalize/latest/dg/API_Campaign.html): An object that describes the deployment of a solution version.
- [CampaignConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignConfig.html): The configuration details of a campaign.
- [CampaignSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignSummary.html): Provides a summary of the properties of a campaign.
- [CampaignUpdateSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_CampaignUpdateSummary.html): Provides a summary of the properties of a campaign update.
- [CategoricalHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_CategoricalHyperParameterRange.html): Provides the name and range of a categorical hyperparameter.
- [ContinuousHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_ContinuousHyperParameterRange.html): Provides the name and range of a continuous hyperparameter.
- [DataDeletionJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DataDeletionJob.html): Describes a job that deletes all references to specific users from an Amazon Personalize dataset group in batches.
- [DataDeletionJobSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DataDeletionJobSummary.html): Provides a summary of the properties of a data deletion job.
- [Dataset](https://docs.aws.amazon.com/personalize/latest/dg/API_Dataset.html): Provides metadata for a dataset.
- [DatasetExportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJob.html): Describes a job that exports a dataset to an Amazon S3 bucket.
- [DatasetExportJobOutput](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJobOutput.html): The output configuration parameters of a dataset export job.
- [DatasetExportJobSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetExportJobSummary.html): Provides a summary of the properties of a dataset export job.
- [DatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetGroup.html): A dataset group is a collection of related datasets (Item interactions, Users, Items, Actions, Action interactions).
- [DatasetGroupSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetGroupSummary.html): Provides a summary of the properties of a dataset group.
- [DatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetImportJob.html): Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.
- [DatasetImportJobSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetImportJobSummary.html): Provides a summary of the properties of a dataset import job.
- [DatasetSchema](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetSchema.html): Describes the schema for a dataset.
- [DatasetSchemaSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetSchemaSummary.html): Provides a summary of the properties of a dataset schema.
- [DatasetSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetSummary.html): Provides a summary of the properties of a dataset.
- [DatasetUpdateSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_DatasetUpdateSummary.html): Describes an update to a dataset.
- [DataSource](https://docs.aws.amazon.com/personalize/latest/dg/API_DataSource.html): Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.
- [DefaultCategoricalHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_DefaultCategoricalHyperParameterRange.html): Provides the name and default range of a categorical hyperparameter and whether the hyperparameter is tunable.
- [DefaultContinuousHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_DefaultContinuousHyperParameterRange.html): Provides the name and default range of a continuous hyperparameter and whether the hyperparameter is tunable.
- [DefaultHyperParameterRanges](https://docs.aws.amazon.com/personalize/latest/dg/API_DefaultHyperParameterRanges.html): Specifies the hyperparameters and their default ranges.
- [DefaultIntegerHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_DefaultIntegerHyperParameterRange.html): Provides the name and default range of a integer-valued hyperparameter and whether the hyperparameter is tunable.
- [EventParameters](https://docs.aws.amazon.com/personalize/latest/dg/API_EventParameters.html): Describes the parameters of events, which are used in solution creation.
- [EventsConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_EventsConfig.html): Describes the configuration of events, which are used in solution creation.
- [EventTracker](https://docs.aws.amazon.com/personalize/latest/dg/API_EventTracker.html): Provides information about an event tracker.
- [EventTrackerSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_EventTrackerSummary.html): Provides a summary of the properties of an event tracker.
- [FeatureTransformation](https://docs.aws.amazon.com/personalize/latest/dg/API_FeatureTransformation.html): Provides feature transformation information.
- [FieldsForThemeGeneration](https://docs.aws.amazon.com/personalize/latest/dg/API_FieldsForThemeGeneration.html): A string to string map of the configuration details for theme generation.
- [Filter](https://docs.aws.amazon.com/personalize/latest/dg/API_Filter.html): Contains information on a recommendation filter, including its ARN, status, and filter expression.
- [FilterSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_FilterSummary.html): A short summary of a filter's attributes.
- [HPOConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_HPOConfig.html): Describes the properties for hyperparameter optimization (HPO).
- [HPOObjective](https://docs.aws.amazon.com/personalize/latest/dg/API_HPOObjective.html): The metric to optimize during hyperparameter optimization (HPO).
- [HPOResourceConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_HPOResourceConfig.html): Describes the resource configuration for hyperparameter optimization (HPO).
- [HyperParameterRanges](https://docs.aws.amazon.com/personalize/latest/dg/API_HyperParameterRanges.html): Specifies the hyperparameters and their ranges.
- [IntegerHyperParameterRange](https://docs.aws.amazon.com/personalize/latest/dg/API_IntegerHyperParameterRange.html): Provides the name and range of an integer-valued hyperparameter.
- [MetricAttribute](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribute.html): Contains information on a metric that a metric attribution reports on.
- [MetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttribution.html): Contains information on a metric attribution.
- [MetricAttributionOutput](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttributionOutput.html): The output configuration details for a metric attribution.
- [MetricAttributionSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_MetricAttributionSummary.html): Provides a summary of the properties of a metric attribution.
- [OptimizationObjective](https://docs.aws.amazon.com/personalize/latest/dg/API_OptimizationObjective.html): Describes the additional objective for the solution, such as maximizing streaming minutes or increasing revenue.
- [Recipe](https://docs.aws.amazon.com/personalize/latest/dg/API_Recipe.html): Provides information about a recipe.
- [RecipeSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_RecipeSummary.html): Provides a summary of the properties of a recipe.
- [Recommender](https://docs.aws.amazon.com/personalize/latest/dg/API_Recommender.html): Describes a recommendation generator for a Domain dataset group.
- [RecommenderConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_RecommenderConfig.html): The configuration details of the recommender.
- [RecommenderSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_RecommenderSummary.html): Provides a summary of the properties of the recommender.
- [RecommenderUpdateSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_RecommenderUpdateSummary.html): Provides a summary of the properties of a recommender update.
- [S3DataConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_S3DataConfig.html): The configuration details of an Amazon S3 input or output bucket.
- [Solution](https://docs.aws.amazon.com/personalize/latest/dg/API_Solution.html)
- [SolutionConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionConfig.html): Describes the configuration properties for the solution.
- [SolutionSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionSummary.html): Provides a summary of the properties of a solution.
- [SolutionUpdateConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionUpdateConfig.html): The configuration details of the solution update.
- [SolutionUpdateSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionUpdateSummary.html): Provides a summary of the properties of a solution update.
- [SolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionVersion.html): An object that provides information about a specific version of a Solution in a Custom dataset group.
- [SolutionVersionSummary](https://docs.aws.amazon.com/personalize/latest/dg/API_SolutionVersionSummary.html): Provides a summary of the properties of a solution version.
- [Tag](https://docs.aws.amazon.com/personalize/latest/dg/API_Tag.html): The optional metadata that you apply to resources to help you categorize and organize them.
- [ThemeGenerationConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_ThemeGenerationConfig.html): The configuration details for generating themes with a batch inference job.
- [TrainingDataConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_TrainingDataConfig.html): The training data configuration to use when creating a domain recommender or custom solution version (trained model).
- [TunedHPOParams](https://docs.aws.amazon.com/personalize/latest/dg/API_TunedHPOParams.html): If hyperparameter optimization (HPO) was performed, contains the hyperparameter values of the best performing model.

### [Amazon Personalize Events](https://docs.aws.amazon.com/personalize/latest/dg/API_Types_Amazon_Personalize_Events.html)

The following data types are supported by Amazon Personalize Events:

- [Action](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_Action.html): Represents action metadata added to an Action dataset using the PutActions API.
- [ActionInteraction](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_ActionInteraction.html): Represents an action interaction event sent using the PutActionInteractions API.
- [Event](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_Event.html): Represents item interaction event information sent using the PutEvents API.
- [Item](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_Item.html): Represents item metadata added to an Items dataset using the PutItems API.
- [MetricAttribution](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_MetricAttribution.html): Contains information about a metric attribution associated with an event.
- [User](https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_User.html): Represents user metadata added to a Users dataset using the PutUsers API.

### [Amazon Personalize Runtime](https://docs.aws.amazon.com/personalize/latest/dg/API_Types_Amazon_Personalize_Runtime.html)

The following data types are supported by Amazon Personalize Runtime:

- [PredictedAction](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_PredictedAction.html): An object that identifies an action.
- [PredictedItem](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_PredictedItem.html): An object that identifies an item.
- [Promotion](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_Promotion.html): Contains information on a promotion.
- [Common Errors](https://docs.aws.amazon.com/personalize/latest/dg/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/personalize/latest/dg/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
