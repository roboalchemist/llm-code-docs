# Source: https://docs.aws.amazon.com/machine-learning/latest/dg/llms.txt

# Amazon Machine Learning Developer Guide

- [Setting Up Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/setting-up-amazon-machine-learning.html)
- [Monitoring Amazon ML with Amazon CloudWatch Metrics](https://docs.aws.amazon.com/machine-learning/latest/dg/cw-doc.html)
- [Logging Amazon ML API Calls with AWS CloudTrail](https://docs.aws.amazon.com/machine-learning/latest/dg/logging-using-cloudtrail.html)
- [Tagging Your Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/tagging-objects.html)
- [Resources](https://docs.aws.amazon.com/machine-learning/latest/dg/resources.html)
- [Document History](https://docs.aws.amazon.com/machine-learning/latest/dg/history.html)

## [What is Amazon Machine Learning?](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html)

- [Amazon Machine Learning Key Concepts](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html): This section summarizes the following key concepts and describes in greater detail how they are used within Amazon ML:
- [Accessing Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/accessing-amazon-machine-learning.html): Accessing Amazon Machine Learning
- [Regions and Endpoints](https://docs.aws.amazon.com/machine-learning/latest/dg/regions-and-endpoints.html): Amazon Machine Learning (Amazon ML) supports real-time prediction endpoints in the following two regions:
- [Pricing for Amazon ML](https://docs.aws.amazon.com/machine-learning/latest/dg/pricing.html): With AWS services, you pay only for what you use.


## [Machine Learning Concepts](https://docs.aws.amazon.com/machine-learning/latest/dg/machine-learning-concepts.html)

- [Solving Business Problems with Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/machine-learning-problems-in-amazon-machine-learning.html): You can use Amazon Machine Learning to apply machine learning to problems for which you have existing examples of actual answers.
- [When to Use Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/when-to-use-machine-learning.html): It is important to remember that ML is not a solution for every type of problem.

### [Building a Machine Learning Application](https://docs.aws.amazon.com/machine-learning/latest/dg/building-machine-learning.html)

Lists the tasks required to use Amazon ML.

- [Formulating the Problem](https://docs.aws.amazon.com/machine-learning/latest/dg/formulating-the-problem.html): The first step in machine learning is to decide what you want to predict, which is known as the label or target answer.
- [Collecting Labeled Data](https://docs.aws.amazon.com/machine-learning/latest/dg/collecting-labeled-data.html): ML problems start with dataâpreferably, lots of data (examples or observations) for which you already know the target answer.
- [Analyzing Your Data](https://docs.aws.amazon.com/machine-learning/latest/dg/analyzing-your-data.html): Before feeding your labeled data to an ML algorithm, it is a good practice to inspect your data to identify issues and gain insights about the data you are using.
- [Feature Processing](https://docs.aws.amazon.com/machine-learning/latest/dg/feature-processing.html): After getting to know your data through data summaries and visualizations, you might want to transform your variables further to make them more meaningful.
- [Splitting the Data into Training and Evaluation Data](https://docs.aws.amazon.com/machine-learning/latest/dg/splitting-the-data-into-training-and-evaluation-data.html): The fundamental goal of ML is to generalize beyond the data instances used to train models.

### [Training the Model](https://docs.aws.amazon.com/machine-learning/latest/dg/training-the-model.html)

You are now ready to provide the ML algorithm (that is, the learning algorithm) with the training data.

- [Linear Models](https://docs.aws.amazon.com/machine-learning/latest/dg/linear-models.html): There are a large number of ML models available.
- [Learning Algorithm](https://docs.aws.amazon.com/machine-learning/latest/dg/learning-algorithm.html): The learning algorithmâs task is to learn the weights for the model.
- [Training Parameters](https://docs.aws.amazon.com/machine-learning/latest/dg/training-parameters1.html): The Amazon ML learning algorithm accepts parameters, called hyperparameters or training parameters, that allow you to control the quality of the resulting model.

### [Evaluating Model Accuracy](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluating-model-accuracy.html)

The goal of the ML model is to learn patterns that generalize well for unseen data instead of just memorizing the data that it was shown during training.

- [Binary Classification](https://docs.aws.amazon.com/machine-learning/latest/dg/binary-classification.html): The actual output of many binary classification algorithms is a prediction score.
- [Multiclass Classification](https://docs.aws.amazon.com/machine-learning/latest/dg/multiclass-classification.html): Unlike the process for binary classification problems, you do not need to choose a score threshold to make predictions.
- [Regression](https://docs.aws.amazon.com/machine-learning/latest/dg/regression.html): For regression tasks, the typical accuracy metrics are root mean square error (RMSE) and mean absolute percentage error (MAPE).

### [Improving Model Accuracy](https://docs.aws.amazon.com/machine-learning/latest/dg/improving-model-accuracy.html)

Obtaining a ML model that matches your needs usually involves iterating through this ML process and trying out a few variations.

- [Model Fit: Underfitting vs. Overfitting](https://docs.aws.amazon.com/machine-learning/latest/dg/model-fit-underfitting-vs-overfitting.html): Understanding model fit is important for understanding the root cause for poor model accuracy.

### [Using the Model to Make Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/using-the-model-to-make-predictions.html)

Now that you have an ML model that performs well, you will use it to make predictions.

- [Batch Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/about-batch-predictions.html): Batch prediction is useful when you want to generate predictions for a set of observations all at once, and then take action on a certain percentage or number of the observations.
- [Online Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/online-predictions.html): Online prediction scenarios are for cases when you want to generate predictions on a one-by-one basis for each example independent of the other examples, in a low-latency environment.
- [Retraining Models on New Data](https://docs.aws.amazon.com/machine-learning/latest/dg/retraining-models-on-new-data.html): For a model to predict accurately, the data that it is making predictions on must have a similar distribution as the data on which the model was trained.
- [The Amazon Machine Learning Process](https://docs.aws.amazon.com/machine-learning/latest/dg/the-machine-learning-process.html): Table explaining how to accomplish ML functions and tasks using Amazon ML.


## [Tutorial: Using Amazon ML to Predict Responses to a Marketing Offer](https://docs.aws.amazon.com/machine-learning/latest/dg/tutorial.html)

- [Step 1: Prepare Your Data](https://docs.aws.amazon.com/machine-learning/latest/dg/step-1-download-edit-and-upload-data.html): Learn how to create an ML model with the Amazon ML tutorial.
- [Step 2: Create a Training Datasource](https://docs.aws.amazon.com/machine-learning/latest/dg/step-2-create-a-datasource.html): Learn how to create an ML model with the Amazon ML tutorial.
- [Step 3: Create an ML Model](https://docs.aws.amazon.com/machine-learning/latest/dg/step-3-create-an-ml-model.html): Learn how to create an ML model with the Amazon ML tutorial.
- [Step 4: Review the ML Model's Predictive Performance and Set a Score Threshold](https://docs.aws.amazon.com/machine-learning/latest/dg/step-4-review-model-and-set-cutoff.html): Learn how to create an ML model with the Amazon ML tutorial.
- [Step 5: Use the ML Model to Generate Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/step-5-create-predictions.html): Learn how to create an ML model with the Amazon ML tutorial.
- [Step 6: Clean Up](https://docs.aws.amazon.com/machine-learning/latest/dg/step-6-clean-up.html): Learn how to create an ML model with the Amazon ML tutorial.


## [Creating and Using Datasources](https://docs.aws.amazon.com/machine-learning/latest/dg/creating-and-using-datasources.html)

- [Understanding the Data Format for Amazon ML](https://docs.aws.amazon.com/machine-learning/latest/dg/understanding-the-data-format-for-amazon-ml.html): Input data is the data that you use to create a datasource.
- [Creating a Data Schema for Amazon ML](https://docs.aws.amazon.com/machine-learning/latest/dg/creating-a-data-schema-for-amazon-ml.html): A schema is composed of all attributes in the input data and their corresponding data types.
- [Splitting Your Data](https://docs.aws.amazon.com/machine-learning/latest/dg/splitting-types.html): The fundamental goal of an ML model is to make accurate predictions on future data instances beyond those used to train models.
- [Data Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/data-insights.html): Learn more about Data Insights for machine learning.
- [Using Amazon S3 with Amazon ML](https://docs.aws.amazon.com/machine-learning/latest/dg/using-amazon-s3-with-amazon-ml.html): Amazon Simple Storage Service (Amazon S3) is storage for the Internet.

### [Creating an Amazon ML Datasource from Data in Amazon Redshift](https://docs.aws.amazon.com/machine-learning/latest/dg/using-amazon-redshift-with-amazon-ml.html)

Use data stored in Amazon Redshift to create an Amazon ML datasource.

- [Required Parameters for the Create Datasource Wizard](https://docs.aws.amazon.com/machine-learning/latest/dg/redshift-parameters.html): To allow Amazon ML to connect to your Amazon Redshift database and read data on your behalf, you must provide the following:
- [Creating a Datasource with Amazon Redshift Data (Console)](https://docs.aws.amazon.com/machine-learning/latest/dg/create-datasource-from-redshift-procedure.html): The Amazon ML console provides two ways to create a datasource using Amazon Redshift data.
- [Troubleshooting Amazon Redshift Issues](https://docs.aws.amazon.com/machine-learning/latest/dg/troubleshooting.html): As you create your Amazon Redshift datasource, ML models, and evaluation, Amazon Machine Learning (Amazon ML) reports the status of your Amazon ML objects in the Amazon ML console.
- [Using Data from an Amazon RDS Database to Create an Amazon ML Datasource](https://docs.aws.amazon.com/machine-learning/latest/dg/using-amazon-rds-with-amazon-ml.html): Amazon ML allows you to create a datasource object from data stored in a MySQL database in Amazon Relational Database Service (Amazon RDS).


## [Training ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/training-ml-models.html)

- [Types of ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/types-of-ml-models.html): Amazon ML supports three types of ML models: binary classification, multiclass classification, and regression.
- [Training Process](https://docs.aws.amazon.com/machine-learning/latest/dg/training-process.html): To train an ML model, you need to specify the following:
- [Training Parameters](https://docs.aws.amazon.com/machine-learning/latest/dg/training-parameters.html): Explains the hyperparameters available in Amazon ML.
- [Creating an ML Model](https://docs.aws.amazon.com/machine-learning/latest/dg/creating-ml-model-on-the-amazon-ml-console.html): Create an ML model using the Amazon ML console.


## [Data Transformations for Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/data-transformations-for-machine-learning.html)

- [Importance of Feature Transformation](https://docs.aws.amazon.com/machine-learning/latest/dg/importance-of-feature-transformation.html): Consider a machine learning model whose task is to decide whether a credit card transaction is fraudulent or not.
- [Feature Transformations with Data Recipes](https://docs.aws.amazon.com/machine-learning/latest/dg/feature-transformations-with-data-recipes.html): There are two ways to transform features before creating ML models with Amazon ML: you can transform your input data directly before showing it to Amazon ML, or you can use the built-in data transformations of Amazon ML.
- [Recipe Format Reference](https://docs.aws.amazon.com/machine-learning/latest/dg/recipe-format-reference.html): Amazon ML recipes contain instructions for transforming your data as a part of the machine learning process.
- [Suggested Recipes](https://docs.aws.amazon.com/machine-learning/latest/dg/suggested-recipes.html): When you create a new datasource in Amazon ML and statistics are computed for that datasource, Amazon ML will also create a suggested recipe that can be used to create a new ML model from the datasource.
- [Data Transformations Reference](https://docs.aws.amazon.com/machine-learning/latest/dg/data-transformations-reference.html)
- [Data Rearrangement](https://docs.aws.amazon.com/machine-learning/latest/dg/data-rearrangement.html): Use DataRearrangemenbt to split your input data into multiple datasources.


## [Evaluating ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluating_models.html)

- [ML Model Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/ml-model-insights.html): When you evaluate an ML model, Amazon ML provides an industry-standard metric and a number of insights to review the predictive accuracy of your model.
- [Binary Model Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/binary-model-insights.html)
- [Multiclass Model Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/multiclass-model-insights.html)
- [Regression Model Insights](https://docs.aws.amazon.com/machine-learning/latest/dg/regression-model-insights.html)
- [Cross-Validation](https://docs.aws.amazon.com/machine-learning/latest/dg/cross-validation.html): Evaluate your Amazon ML model with cross-validation.
- [Evaluation Alerts](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluation-alerts.html): Amazon ML provides insights to help you validate whether you evaluated the model correctly.


## [Generating and Interpreting Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/interpreting_predictions.html)

- [Creating a Batch Prediction](https://docs.aws.amazon.com/machine-learning/latest/dg/creating-batch-prediction-objects.html): To create a batch prediction, you create a BatchPrediction object using either the Amazon Machine Learning (Amazon ML) console or API.
- [Reviewing Batch Prediction Metrics](https://docs.aws.amazon.com/machine-learning/latest/dg/working-with-batch-predictions.html): Review Amazon ML batch predictions metrics.
- [Reading the Batch Prediction Output Files](https://docs.aws.amazon.com/machine-learning/latest/dg/reading-the-batchprediction-output-files.html): Perform the following steps to retrieve the batch prediction output files:
- [Requesting Real-time Predictions](https://docs.aws.amazon.com/machine-learning/latest/dg/requesting-real-time-predictions.html): A real-time prediction is a synchronous call to Amazon Machine Learning (Amazon ML).


## [Managing Amazon ML Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/managing_objects.html)

- [Listing Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/listing-objects.html): List Amazon ML objects and their details.
- [Retrieving Object Descriptions](https://docs.aws.amazon.com/machine-learning/latest/dg/retrieving-object-descriptions.html): You can view detailed descriptions of any object through the console or through the API.
- [Updating Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/updating-objects.html): Each object type has an operation that updates the details of an Amazon ML object (See Amazon ML API Reference):
- [Deleting Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/deleting-objects.html): When you no longer need your datasources, ML models, evaluations, and batch predictions, you can delete them.


## [Amazon Machine Learning Reference](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-reference.html)

- [Granting Amazon ML Permissions to Read Your Data from Amazon S3](https://docs.aws.amazon.com/machine-learning/latest/dg/granting-amazon-ml-permissions-to-read-your-data-from-amazon-s3.html): To create a datasource object from your input data in Amazon S3, you must grant Amazon ML the following permissions to the S3 location where your input data is stored:
- [Granting Amazon ML Permissions to Output Predictions to Amazon S3](https://docs.aws.amazon.com/machine-learning/latest/dg/granting-amazon-ml-permissions-to-output-predictions-to-amazon-s3.html): To output the results of the batch prediction operation to Amazon S3, you must grant Amazon ML the following permissions to the output location, which is provided as input to the Create Batch Prediction operation:
- [Controlling Access to Amazon ML Resources -with IAM](https://docs.aws.amazon.com/machine-learning/latest/dg/controlling-access-to-amazon-ml-resources-by-using-iam.html): AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/machine-learning/latest/dg/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Dependency Management of Asynchronous Operations](https://docs.aws.amazon.com/machine-learning/latest/dg/dependency-management-of-asynchronous-operations.html): Batch operations in Amazon ML depend on other operations in order to complete successfully.
- [Checking Request Status](https://docs.aws.amazon.com/machine-learning/latest/dg/operation-request-status.html): Check the status of your Amazon ML request.
- [System Limits](https://docs.aws.amazon.com/machine-learning/latest/dg/system-limits.html): In order to provide a robust, reliable service, Amazon ML imposes certain limits on the requests you make to the system.
- [Names and IDs for all Objects](https://docs.aws.amazon.com/machine-learning/latest/dg/names-and-ids-for-all-objects.html): Every object in Amazon ML must have an identifier, or ID.
- [Object Lifetimes](https://docs.aws.amazon.com/machine-learning/latest/dg/object-lifetimes.html): Any datasource, ML model, evaluation, or batch prediction object that you create with Amazon ML will be available for your use for at least two years after creation.
