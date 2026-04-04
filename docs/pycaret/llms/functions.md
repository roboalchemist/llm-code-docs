# Source: https://pycaret.gitbook.io/docs/get-started/functions.md

# Functions

{% tabs %}
{% tab title="Initialize" %}

#### [setup](https://pycaret.gitbook.io/docs/get-started/initialize#setting-up-environment)

This function initializes the experiment in PyCaret and prepares the transformation pipeline based on all the parameters passed in the function. The setup function must be called before executing any other function. It only requires two parameters: `data` and `target`. All the other parameters are optional.
{% endtab %}

{% tab title="Train" %}

#### [compare\_models](https://pycaret.gitbook.io/docs/get-started/train#compare_models)

This function trains and evaluates the performance of all the models available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores.

#### [create\_model](https://pycaret.gitbook.io/docs/get-started/train#create_model)&#x20;

This function trains and evaluates the performance of a given model using cross-validation. The output of this function is a scoring grid with cross-validated scores along with mean and standard deviation.
{% endtab %}

{% tab title="Optimize" %}

#### [tune\_model](https://pycaret.gitbook.io/docs/get-started/optimize#tune_model)

This function tunes the hyperparameters of a given model. The output of this function is a scoring grid with cross-validated scores of the best model. Search spaces are pre-defined with the flexibility to provide your own. The search algorithm can be random, bayesian, and a few others with the ability to scale on large clusters.

#### [ensemble\_model](https://pycaret.gitbook.io/docs/get-started/optimize#ensemble_model)

This function ensembles a given model. The output of this function is a scoring grid with cross-validated scores of the ensembled model. Two methods `Bagging` or `Boosting` can be used for ensembling.

#### [blend\_models](https://pycaret.gitbook.io/docs/get-started/optimize#blend_models)

This function trains a Soft Voting / Majority Rule classifier for given models in a list. The output of this function is a scoring grid with cross-validated scores of a Voting Classifier or Regressor.

#### [stack\_models](https://pycaret.gitbook.io/docs/get-started/optimize#stack_models)

This function trains a meta-model over given models in a list. The output of this function is a scoring grid with cross-validated scores of a Stacking Classifier or Regressor.

#### [optimize\_threshold](https://pycaret.gitbook.io/docs/get-started/optimize#optimize_threshold)

This function optimizes the probability threshold for a given model. It iterates over performance metrics at different probability thresholds and returns a plot with performance metrics on the y-axis and threshold on the x-axis.

#### [calibrate\_model](https://pycaret.gitbook.io/docs/get-started/optimize#calibrate_model)

This function calibrates the probability of a given model using isotonic or logistic regression. The output of this function is a scoring grid with cross-validated scores of calibrated classifier.
{% endtab %}

{% tab title="Analyze" %}

#### [plot\_model](https://pycaret.gitbook.io/docs/get-started/analyze#plot_model)

This function analyzes the performance of a trained model on the hold-out set. It may require re-training the model in certain cases.

#### [evaluate\_model](https://pycaret.gitbook.io/docs/get-started/analyze#evaluate_model)

This function uses `ipywidgets` to display a basic user interface for analyzing the performance of a trained model.

#### [interpret\_model](https://pycaret.gitbook.io/docs/get-started/analyze#interpret_model)

This function analyzes the predictions generated from a trained model. Most plots in this function are implemented based on the SHAP (Shapley Additive exPlanations).

#### [dashboard](https://pycaret.gitbook.io/docs/get-started/analyze#dashboard)

This function generates the interactive dashboard for a trained model. The dashboard is implemented using the ExplainerDashboard project.

#### [check\_fairness](https://pycaret.gitbook.io/docs/get-started/analyze#check_fairness)

This function provides fairness-related metrics between different groups in the dataset for a given model. There are many approaches to evaluate fairness but this function uses the approach known as group fairness, which asks: which groups of individuals are at risk for experiencing harm.

#### [get\_leaderboard](https://pycaret.gitbook.io/docs/get-started/analyze#get_leaderboard)

This function returns the leaderboard of all models trained in the current setup.

#### [assign\_model](https://pycaret.gitbook.io/docs/get-started/analyze#assign_model)

This function assigns labels to the training dataset using the trained model. It is only available for unsupervised modules.
{% endtab %}

{% tab title="Deploy" %}

#### [predict\_model](https://pycaret.gitbook.io/docs/get-started/deploy#predict_model)

This function generates the label using a trained model.  When unseen data is not passed, it predicts the label and score on the holdout set.

#### [finalize\_model](https://pycaret.gitbook.io/docs/get-started/deploy#finalize_model)

This function refits a given model on the entire dataset.

#### [save\_model](https://pycaret.gitbook.io/docs/get-started/deploy#save_model)

This function saves the ML pipeline as a pickle file for later use.

#### [load\_model](https://pycaret.gitbook.io/docs/get-started/deploy#load_model)

This function loads a previously saved pipeline.

#### [save\_experiment](https://pycaret.gitbook.io/docs/get-started/deploy#save_experiment)

This function saves an experiment to a pickle file.

#### [load\_experiment](https://pycaret.gitbook.io/docs/get-started/deploy#load_experiment)

This function loads an experiment back into Python from a pickle file.&#x20;

#### [check\_drift](https://pycaret.gitbook.io/docs/get-started/deploy#check_drift)

This function generates a drift report file using the evidently library.&#x20;

#### [deploy\_model](https://pycaret.gitbook.io/docs/get-started/deploy#deploy_model)

This function deploys the entire ML pipeline on the cloud.&#x20;

#### [convert\_model](https://pycaret.gitbook.io/docs/get-started/deploy#convert_model)

This function transpiles the trained machine learning model's decision function in different programming languages such as Python, C, Java, Go, C#, etc.&#x20;

#### [create\_api](https://pycaret.gitbook.io/docs/get-started/deploy#create_api)

This function takes an input model and creates a POST API for inference. It only creates the API and doesn't run it automatically.

#### [create\_docker](https://pycaret.gitbook.io/docs/get-started/deploy#create_docker)

This function creates a Dockerfile and requirements.txt for deploying API.

#### [create\_app](https://pycaret.gitbook.io/docs/get-started/deploy#create_app)

This function creates a basic gradio app for inference.
{% endtab %}

{% tab title="Others" %}

#### [pull](https://pycaret.gitbook.io/docs/get-started/others#pull)

Returns the last printed scoring grid.

#### [models](https://pycaret.gitbook.io/docs/get-started/others#models)

Return a table containing all the models available in the imported module of the model library.

#### [get\_config](https://pycaret.gitbook.io/docs/get-started/others#get_config)

This function retrieves the global variables created by the setup function.&#x20;

#### [set\_config](https://pycaret.gitbook.io/docs/get-started/others#set_config)

This function resets the global variables.

#### [get\_metrics](https://pycaret.gitbook.io/docs/get-started/others#get_metrics)

Returns the table of all available metrics used for cross-validation.

#### [add\_metric](https://pycaret.gitbook.io/docs/get-started/others#add_metric)

Adds a custom metric to the metric container for cross-validation.

#### [remove\_metric](https://pycaret.gitbook.io/docs/get-started/others#remove_metric)

Removes a custom metric from the metric container.&#x20;

#### [automl](https://pycaret.gitbook.io/docs/get-started/others#automl)

This function returns the best model from all the models in the current setup.&#x20;

#### [get\_logs](https://pycaret.gitbook.io/docs/get-started/others#get_logs)

Returns a table of experiment logs. Only works when log\_experiment = True when initializing the setup function.&#x20;

#### [get\_current\_experiment](https://pycaret.gitbook.io/docs/get-started/others#get_current_experiment)

Obtain the current experiment object.&#x20;

#### [set\_current\_experiment](https://pycaret.gitbook.io/docs/get-started/others#set_current_experiment)

Set the current experiment to be used with the functional API.&#x20;
{% endtab %}
{% endtabs %}
