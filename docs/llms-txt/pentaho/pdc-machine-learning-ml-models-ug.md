# Source: https://docs.pentaho.com/pdc-use/pdc-machine-learning-ml-models-ug.md

# Machine Learning (ML) Models

In today's data-driven landscape, Machine Learning (ML) models play a crucial role in extracting insights, making predictions, and automating decision-making. Pentaho Data Catalog introduces ML Model Tracking, which allows organizations to manage, analyze, and track ML model metadata across the entire lifecycle—from experimentation to production deployment.

With ML Model Tracking, you can:

* Discover and manage ML model metadata within Data Catalog.
* Track model performance metrics across multiple experiments and runs.
* Ensure traceability by viewing model dependencies, artifacts, and lineage.
* Enhance collaboration by enabling teams to log, retrieve, and analyze ML model metadata.
* Ensure governance and compliance by monitoring data drift and performance degradation.

In ML Model Tracking, Data Catalog integrates with MLflow to import and catalog experiments, runs, model versions, parameters, metrics, and artifacts into a structured hierarchy known as **ML Models**. This enables organizations to:

* Centralize ML metadata management by storing and organizing ML Models in one place.
* Ensure experiment reproducibility by tracking datasets, parameters, and artifacts for each model version.
* Enhance collaboration by enabling data scientists, analysts, and business users to easily access ML model metadata.

PDC supports two categories of ML model servers:

## Pre-Production Model Servers

Integrating pre-production model servers such as MLflow into Data Catalog allows organizations to systematically capture and manage metadata from model development, testing, and validation. This integration improves early-stage lifecycle management by ensuring that experiments, runs, model versions, and associated datasets are traceable and reproducible.

* For Data Scientists – It simplifies experiment tracking by centralizing runs, parameters, and metrics, enabling efficient comparisons between models and faster selection of the best-performing candidates.
* For ML Engineers – It ensures that models moving toward deployment are well-documented, with clear lineage of datasets, artifacts, and configurations that can be validated before production release.
* For Compliance Officers and Governance Teams – It creates an audit trail for training activities, ensuring that sensitive data is used appropriately and that experiment history is available for regulatory review.

By providing visibility into training and experimentation, Data Catalog helps organizations build a strong foundation of trust before models progress into production environments.

## Production Model Servers

The integration of production model servers such as NVIDIA Triton into Data Catalog extends ML Model Tracking from experimentation to real-world deployment. This unified approach enhances model lifecycle management by integrating training metadata from pre-production servers, such as MLflow, with inference performance and health data from Triton.

* For Data Scientists – It ensures experiment reproducibility while providing feedback from live production models, enabling faster iteration and validation of hypotheses.
* For ML Engineers – It streamlines deployment monitoring with visibility into operational metrics such as latency, inference counts, and memory usage, helping optimize production workloads.
* For Compliance Officers and Governance Teams – It strengthens oversight by linking business terms, policies, and lineage across both training and production stages, ensuring transparency and regulatory compliance.

By combining pre-production and production perspectives, Data Catalog becomes a single trusted source for managing machine learning assets across their entire lifecycle.

## ML Models components

The **ML Models** section in Data Catalog organizes machine learning metadata in a hierarchical structure. This hierarchy differs depending on whether the metadata originates from a Pre-Production Model Server (such as MLflow) or a Production Model Server (such as NVIDIA Triton).

By supporting both pre-production hierarchies such as MLflow and production hierarchies such as Triton, Pentaho Data Catalog delivers a complete view of the machine learning lifecycle. It provides upstream visibility through experiment tracking, lineage, and reproducibility, while also offering downstream visibility into real-world inference performance, deployment status, and operational health. Governance and compliance are strengthened by enabling monitoring across both training and production environments. At the same time, collaboration is enhanced by giving data scientists, ML engineers, and business teams access to a single, trusted catalog of ML assets.

To configure and import ML model server components, see the [Configure for ML model servers](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#configure-a-machine-learning-ml-server-connection-in-data-catalog) topic in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.

### Pre-Production Model Servers (MLflow)

Pre-production servers capture the metadata generated during model development, testing, and validation. In Data Catalog, MLflow integration provides a structured hierarchy to help users easily navigate, manage, and track machine learning models, their versions, experiments, and associated metadata. The hierarchy ensures that every component of an ML model server, such as ML models, versions, experiments, and runs, is well-organized and accessible.

The following table lists the components of the ML Models hierarchy in Data Catalog:

![ML Model Components](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-6d8adaddabe8c0e3af20304895636aa3bba101e2%2FML%20Models%20Components.png?alt=media)

```
ML Models
 └── Model Server (MLflow)
       ├── Model
       │     ├── Version
       │── Experiment
             │── Run
```

<table><thead><tr><th width="85.25" align="center">Item</th><th width="194.5">ML Models component</th><th>Description</th></tr></thead><tbody><tr><td align="center">1</td><td><strong>ML model server</strong></td><td>A centralized repository where machine learning (ML) models are trained, stored, and deployed, enabling model tracking, serving, and monitoring.</td></tr><tr><td align="center">2</td><td><strong>ML model</strong></td><td>A trained machine learning artifact that makes predictions based on data. Each model is created using algorithms, datasets, and hyperparameters, and it produces versions, runs, and artifacts during training.</td></tr><tr><td align="center">3</td><td><strong>Version</strong></td><td>An iteration of a model evolved over time through continuous training and experimentation.</td></tr><tr><td align="center">4</td><td><strong>Experiment</strong></td><td>A systematic process of training and evaluating a model with various configurations, datasets, or hyperparameters to identify the most effective version.</td></tr><tr><td align="center">5</td><td><strong>Run</strong></td><td><p>An individual training attempt of an ML model, where various parameters and datasets are used to evaluate different approaches.</p><p>Each run records:</p><ul><li><strong>ML Runs Tags:</strong> Key–value pairs associated with a specific ML run that provide additional metadata for tracking, searching, and organizing experiments in ML Model Tracking.</li><li><strong>Parameters:</strong> Hyperparameters used for training, such as learning rate and batch size.</li><li><strong>Metrics:</strong> Model evaluation results, such as accuracy, RMSE, and MSE.• <strong>Run ID:</strong> A unique identifier for the execution.</li></ul></td></tr></tbody></table>

### Production model servers

Production servers capture metadata about models actively deployed for inference. In Data Catalog, NVIDIA Triton integration provides a hierarchy focused on deployment and operational metrics. The hierarchy contains the model server, models, and respective versions. This hierarchy allows teams to monitor performance, validate deployment health, and optimize production inference workloads.

The following table lists the components of the ML Models hierarchy (imported from Production model server) in Data Catalog:

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FZQNAgCDmNVdE6PITktze%2Fimage.png?alt=media&#x26;token=2ed923ab-3ed7-4d4c-b48e-1df70090710c" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="84">Item</th><th width="200.75">ML Models Component</th><th>Descriptions</th></tr></thead><tbody><tr><td>1</td><td>ML Model server</td><td>Represents the Triton inference server. Includes environment (Development, QA, Production), status (Draft, Review, Accepted, Imported), health check, and server liveness.</td></tr><tr><td>2</td><td>ML Model</td><td>A deployed model registered in Triton, with details such as model name, backend framework (for example,  TensorRT, TensorFlow, ONNX), supported inputs/outputs, and batch configuration.</td></tr><tr><td>3</td><td>Version</td><td><p>A specific deployed version of the model. Each version includes:</p><ul><li>Configuration: platform, input/output tensors, max batch size, version policy, and instance group.</li><li>Statistics: last inference timestamp, inference count, execution count, batch statistics, and memory usage.</li><li>Metrics: request counts, latency breakdowns (queue, compute input, compute, compute output), success/failure counters, and histograms for response times.</li></ul></td></tr></tbody></table>

## Tour the ML Models page

In Data Catalog, the ML Models page provides a user-friendly interface for managing and viewing ML model servers and their components. To access and explore the ML Models page, in the left navigation menu, click **ML Models**. This page is divided into two primary areas: [navigation](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Use/PDC%20Machine%20Learning%20\(ML\)%20Models/PDC%20Machine%20Learning%20\(ML\)%20Models%20\(UG\)/PDC%20Tour%20the%20ML%20Models%20page/PDC%20ML%20Models%20navigation%20pane=GUID-C4A28C3E-320F-4663-8326-5DCC028CB47A=1=en=.md) and [content](#ml-models-content-pane) pane.

![ML Models Landing Page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-950ce74078530ae043a76535f3b863b9e6d490a0%2FML%20Models%20landing%20page.png?alt=media)

### ML Models navigation pane

In Data Catalog, on the left navigation pane, you see a list of **ML Model Servers** and their components, organized in a hierarchical tree structure. The hierarchy differs depending on the type of server:

* Pre-Production Model Servers (for example, MLflow) include ML Models, Versions, Experiments, and Runs. These nodes allow you to track training jobs, compare experiments, and analyze model versions.
* Production Model Servers (for example, NVIDIA Triton) include ML Models and Versions. These nodes allow you to view deployment details, configuration, and operational metrics for models actively serving inference.

You can explore this hierarchy to locate specific ML Model components for further analysis. Additionally, you can choose **View Table** or **View Galaxy** under **Actions** to understand the ML Models hierarchy. To configure and import ML Model server components, see [Configure for ML Model Servers](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp#configure-an-mlflow-server-connection) in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.&#x20;

If required, you can also manually create ML model server components using the following options available under **Actions**:

* [**Add New Model Server**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models#add-a-new-ml-model-server-locally-to-data-catalog)**:** Creates a new ML model server in Data Catalog to track and manage ML Models and their metadata.
* [**Add New Model**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models#add-a-new-ml-model-locally-to-data-catalog)**:** Creates a new ML model under a registered model server, which can be tracked, versioned, and managed within Data Catalog. For MLflow, this model can be versioned and linked to experiments and runs. For Triton, this model represents a deployed asset with configuration and performance metadata.
* [**Add New Experiment**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models#add-a-new-experiment-locally-to-data-catalog) (Pre-Production only)**:** Creates a new ML experiment within an ML model to log multiple training runs and compare different model configurations.
* [**Add New Version**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models#add-a-new-version-locally-to-data-catalog)**:** Adds a new ML model version, representing an improved or modified iteration of an existing model with updated parameters or datasets. In MLflow, this represents an iteration of a model with updated parameters or datasets. In Triton, this represents a deployed model version with inference statistics and metrics.
* [**Add New Run**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models#add-a-new-run-locally-to-data-catalog) (Pre-Production only): Logs a new ML run under an experiment, capturing metadata such as hyperparameters, metrics, artifacts, and execution details for tracking and evaluation.

Additionally, similar to other hierarchy assets in Data Catalog, you can import and export ML model components. For more information, see the [Manage Machine Learning (ML) Models](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-ml-models "mention") section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) guide.

### ML Models content pane

You can view detailed information about the selected ML Models component, including metadata specific to the chosen component. The details shown depend on whether the component originates from a pre-production model server (such as MLflow) or a production model server (such as NVIDIA Triton). For example, when a version is selected, the content pane shows its associated metadata, where you can clearly understand the data attributes and context.

The following table identifies the key details available in the content pane for an ML model:

![ML Models Content Pane](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-6d3df5ab41634cde8d93bb399e3abf7b4e14df3e%2FML%20Models%20Content%20Pane.png?alt=media)

<table><thead><tr><th width="81.22222900390625">Item</th><th width="148.5555419921875">Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Data banner</td><td>Shows the name, path, and type icon identifying the ML model server and its components. For MLflow, this includes the server, model, version, experiment, or run. For Triton, this includes the server, model, and version nodes. With these details, you can gain a clear understanding of the component's position within the hierarchy and its classification. The name and type attributes identifying the resource are provided.</td></tr><tr><td>2</td><td>Actions menu</td><td>Shows a menu of actionable options tailored to the selected ML Models component type. You can perform tasks such as copying the application path (hierarchy) to reference the asset’s location or switching to a Galaxy view to visualize the data alternately. For more information, see <a href="#ml-models-galaxy-view">ML Models Galaxy view</a>.</td></tr><tr><td>3</td><td>Data tabs</td><td><p>Get access to detailed information and metadata related to the selected ML Model components through the following tabs:</p><ul><li><a href="#summary-tab">Summary</a></li><li><a href="#custom-properties-tab">Custom Properties</a></li><li><a href="#business-terms-tab">Business Terms</a></li><li><a href="#data-elements-tab">Data Elements</a></li><li><a href="#comment-tab">Comment</a></li><li><a href="#applications-tab">Applications</a></li><li><a href="#policies-tab">Policies</a></li></ul><p>On each tab, you can get insights into specific attributes or relationships of the ML Models components, which can help to analyze and understand the ML Models hierarchy. To learn more about each tab, see <a href="#ml-models-hierarchy-view">ML Models hierarchy view</a>.</p></td></tr></tbody></table>

## Different views of the ML Models

In the **ML Models** section of Data Catalog, you can explore both pre-production and production ML Models in multiple views to understand the structure and relationships between models, versions, experiments, and runs in a way that best suits your needs.

By default, Data Catalog displays ML model server components in a hierarchical tree-structured format. For pre-production model servers such as MLflow, this hierarchy includes model servers, models, versions, experiments, and runs. For production model servers such as NVIDIA Triton, the hierarchy includes model servers, models, and versions, with additional performance and configuration metadata available at each level. This clear parent–child relationship helps users understand how ML components are interconnected across different lifecycle stages.

You can also switch to Table View or Galaxy View by selecting the **View Table** or **View Galaxy** option from the **Actions** menu in the navigation pane. In Table View, you can see ML model server components presented in a tabular format. For MLflow, the table includes models, versions, experiments, and runs, allowing detailed comparison of training jobs and results. For Triton, the table focuses on models and versions, displaying operational metadata such as status, inference counts, latency, and memory usage for easy monitoring and analysis.

In Galaxy View, you can visualize ML model server components in a spatial format. This visualization highlights relationships and patterns between components. For MLflow, Galaxy View helps trace lineage between experiments, runs, and versions. For Triton, it helps identify dependencies and connections between deployed models and their versions, making it ideal for gaining a broader, interconnected perspective of ML assets across both pre-production and production environments.

### ML Models hierarchy view

In Data Catalog, you can configure ML model servers and import their components into the ML Models section. In the hierarchy view of the ML Models page, you can manage them visually and intuitively. Additionally, you can sync ML model server components and maintain their associated details, ensuring clarity and consistency in data-related discussions. The following options are available on the ML Models page.

#### **ML Models component name**

The name of the ML Models component is displayed in the hierarchy view. For pre-production servers such as MLflow, this includes components like the model server, model, version, experiment, and run. For production servers such as NVIDIA Triton, the hierarchy includes the model server, model, and version nodes. This makes it easy to quickly identify and understand the specific ML Models component you are working with, whether it relates to development and testing or active production inference.

![ML Models component Name](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-232b8258fde344036f4733813a09e0504b4abffd%2FML%20Model%20Component%20Name.png?alt=media)

#### **Actions**

The **Actions** menu provides quick access to features that help you work with ML Model components.

<table><thead><tr><th width="148.44439697265625">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Copy Path</strong></td><td>Copies the hierarchical path of the ML Models component for quick reference or to share it with others.</td></tr><tr><td><strong>View Galaxy</strong></td><td>Takes you to the Galaxy view of the selected ML Models component. In Galaxy view, you can see the ML Models components and their related assets in a spatial layout. For MLflow, this highlights lineage between experiments, runs, and versions. For Triton, this highlights relationships between production models and their deployed versions. See <a href="pdc-galaxy-view">Galaxy view</a> for more details.</td></tr></tbody></table>

#### **Summary tab**

The **Summary** tab gives a consolidated view of the selected ML Models component. The information displayed depends on whether the component originates from a pre-production server such as MLflow or a production server such as NVIDIA Triton, and on which node in the hierarchy is selected (server, model, version, experiment, or run).

**Note:** The visible information depends on the ML Models component you have selected.

<table><thead><tr><th width="165.111083984375">Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Definition</strong></td><td>Update with a custom description of the registered model server that helps users understand its purpose, configuration, and role within their machine learning (ML) workflows.</td></tr><tr><td><strong>Assets</strong></td><td>Displays the child components associated with the selected ML Models component, such as <strong>ML Models</strong>, <strong>Versions</strong>, <strong>Experiments</strong>, and <strong>Runs</strong>. The table displays key details like component name, type, associated ML tags, parent component, status, and who created it and who updated the time, helping users track relationships, navigate the ML hierarchy, and manage metadata in Data Catalog.</td></tr><tr><td><strong>Additional Details</strong> (only for versions and runs)</td><td><p>Displays detailed metadata about the selected version and run.</p><p>For a version, it displays the following version-specific metadata so that the user can verify which ML run produced a model version, locate the stored artifacts, and verify if the version is ready for deployment:</p><ul><li><strong>Run ID</strong>: Unique identifier for the ML run that generated this version.</li><li><strong>Version Source</strong>: Path to the model artifacts stored in MLflow or an external system.</li><li><strong>Version Stage</strong>: Indicates the deployment stage of the model.</li><li><strong>Version Status</strong>: Shows whether the version is ready for use.</li><li><strong>Custom Properties</strong>: Displays any associated custom properties of the selected version.</li><li><strong>Created By</strong>: The user who created the selected version entry in Data Catalog.</li><li><strong>Updated By</strong>: The user who last updated the selected version. For a run, it displays the following additional metadata about the specific ML run:</li><li><strong>Artifact URI</strong>: A clickable link to access artifacts generated during the ML run.</li><li><strong>Run ID</strong>: Unique identifier for the ML run.</li><li><strong>Run Status</strong>: Indicates the completion status of the run (for example, <strong>FINISHED</strong> or <strong>FAILED</strong>).</li></ul></td></tr><tr><td><strong>Ratings</strong></td><td>Highlights the popularity of the resource by providing the average rating of all users for the selected ML Models component. A low rating highlights an issue with the resource, such as incomplete data.</td></tr><tr><td><strong>Properties</strong></td><td><p>Shows the properties of the selected ML Models component.</p><ul><li><strong>Domain</strong>: The specific area or domain within the organization to which the ML Models component belongs.</li><li><strong>Status</strong>: The current state of the selected ML Models, such as <strong>Imported</strong>, <strong>Accepted</strong>, <strong>Draft</strong>, <strong>Reviewed</strong>, <strong>Deprecated</strong>, and <strong>Unknown</strong>.</li><li><strong>Created By</strong>: The user who created the ML Models component entry in Data Catalog.</li><li><strong>Last Updated</strong>: The date and time when the ML Models component data was last updated.</li></ul></td></tr><tr><td><strong>Custom Properties</strong></td><td>Lists the custom properties associated with the resource. Custom properties refer to user-defined metadata attributes or fields that can be associated with various data assets. For more information, see <a href="../ldc-resource-properties-user-guide-cp#custom-properties">Custom properties</a>.</td></tr><tr><td><strong>Tags</strong></td><td>Lists the tags associated with the resource. In addition, you can click and start adding tags like “quality:45” (the key should be unique) to the resource, which helps to identify the resource with tagged keywords.</td></tr><tr><td><strong>Style</strong></td><td>Displays the icon, title, and color associated with the physical asset. With the data steward role, you can click the <strong>Edit</strong> (pencil) icon to select a different icon, update the title, and change the color. Then you can click <strong>Apply</strong>, the selected icon and color are updated immediately, and the updated title appears in the asset header and in the breadcrumb navigation. You can also choose <strong>Apply to all siblings</strong> to apply the same visual changes to all sibling assets at the same level.<br><br>▶️ Watch a guided walkthrough on <a href="https://assets.demos.hitachivantara.com/psl/d4h0ewc">editing icons, titles, and colors in the Style panel</a> in Data Catalog.</td></tr></tbody></table>

#### Custom Properties tab

You can use custom properties to annotate and categorize the ML models and components with additional context-specific information, enhancing the metadata available for data assets within Data Catalog. This tab lists the custom properties and values added to the component. You can also apply filters to refine the list.

For pre-production servers such as MLflow, you can apply custom properties to servers, models, versions, experiments, and runs. This helps add training-related context, such as the business use case, dataset source, or experimental conditions.

For production servers such as Triton, you can apply custom properties to servers, models, and versions. This enables you to capture deployment-specific information, such as resource allocation, deployment owner, or monitoring requirements.

To manage custom properties, select **Manage properties** to open the **Custom Properties** page in the **Management** section. For more information, see [Manage custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties) in [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

#### **Business Terms tab**

In the **Business Terms** tab, you can associate ML Models components with relevant business terms to define and categorize the components, ensuring consistency across the organization. It shows the names of associated terms, their parent categories, and the owners responsible for them. You can also apply filters to refine the list.

For pre-production servers such as MLflow, associating business terms helps provide context for experiments, runs, and model versions. For example, you can link a model run to a business term like *Churn Prediction* or *Fraud Detection*, ensuring that training activities are clearly aligned with business objectives.

For production servers such as Triton, associating business terms helps connect deployed models to their intended use cases and governance requirements. For example, you can tag a deployed version with business terms like *Regulatory Compliance* or *Customer Segmentation*, which makes it easier to monitor production assets against organizational standards.

To add a business term, click **Add Terms** and choose the business term you want to associate with the ML Models component. After you add any business term to the component, it creates a relationship between the term and the component. To get detailed information, click the term to view the business term in the canvas view with a highlighted focus. You can also click **Delete**, which only removes the association between the component and the business term but does not delete the actual business term in Data Catalog.

#### **Data Elements tab**

The **Data Elements** tab shows a detailed view of the data elements associated with a selected ML Models component. This tab shows data asset details such as the data source, item name, item type, parent, and associated tags which help you to understand the data structure, maintain metadata, and perform actions like adding, viewing, or deleting data elements. You can also apply filters to refine the list.

For pre-production servers, such as MLflow, data elements typically represent training datasets, input features, or artifacts used to create and validate model runs and experiments. Associating these elements with MLflow components ensures clear lineage and reproducibility of experiments.

For production servers such as Triton, data elements represent deployed input and output schemas. These include the input tensors that the model expects and the output tensors it generates, along with their types, shapes, and constraints. Associating data elements with Triton models or versions enables the monitoring of how deployed models interact with real-world data and ensures compatibility with downstream systems.

To add new data elements, click **Add Data Elements** and choose the data element you want to associate with the component. To get detailed information, click **View** to view the data element in the canvas view with a highlighted focus. You can also click **Delete**, which only removes the association between the component and the data element but does not delete the actual data element.

#### **Comment tab**

The **Comment** tab is a collaborative feature that allows users to discuss and provide feedback on specific data assets within Data Catalog. You can add comments, share suggestions, or ask questions directly in the tab using the provided text box, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the Mentions tab on the Data Catalog landing page, prompting them to respond if necessary. For more information, see [Tour of the Home page](https://docs.pentaho.com/pdc-use/ldc-quick-start-user-guide-cp#tour-of-the-home-page).

**Note:** In the Comment tab, you can:

* Tag users who have been configured in Data Catalog.
* Only delete the comments you posted.
* Delete any comment if you are an admin.

#### **Applications tab**

The **Applications** tab contains the third-party or external applications associated with the selected ML Models component and additional information associated with each application. By linking third-party applications and ML Models components, you can understand how external applications interact with specific ML Models components and the relationship between data and external systems to better assess its purpose and relevance. You can also apply filters to refine the list.

For pre-production servers such as MLflow, applications may include experiment tracking dashboards, training pipelines, or external notebooks that provide additional visibility into model development and evaluation. Associating these applications ensures that the context of experimentation is accessible from within PDC.

For production servers such as Triton, applications may include monitoring tools, deployment orchestrators, or downstream systems that consume model predictions. Associating these applications helps users see how deployed models are integrated into production workflows and business processes.

To add an application, click **Add Applications** and choose the application you want to link to the component. You can also click **Delete**, which removes the association between the application and the ML Models component but does not delete the actual application in Data Catalog.

#### **Policies tab**

In the context of an ML Models component, policies and standards are properties of a ML Models component, meaning a set of rules applied to the component. In the **Policies** tab, you can explore the standards and policies related to the component and additional information, such as name, parent, and owner. By associating policies and standards with ML Models components, you can give clarity on the policies and standards governing data usage and management and reduce the risk of non-compliance. You can also apply filters to refine the list.

For pre-production servers such as MLflow, policies typically govern training data usage, model lineage, and experiment reproducibility. Associating policies at this stage ensures that experiments are conducted with proper oversight, data quality requirements are met, and sensitive datasets are handled in accordance with organizational standards.

For production servers such as Triton, policies often focus on deployment, inference monitoring, and compliance with operational or regulatory standards. Associating policies with deployed models or versions helps organizations monitor live inference workloads, enforce performance thresholds, and ensure that production AI systems remain trustworthy and compliant.

To add a policy, click **Add Policy** and choose the standard and policy you want to link to the component. After you add any policy to the component, it creates a relationship between the policy and the component. You can also click **Delete**, which removes the association between the component and policy but does not delete the actual policy in Data Catalog.

### ML Models table view

In Data Catalog, the ML Models table view shows a structured, spreadsheet-like layout for browsing and managing ML Models components. This view enhances the way you interact with ML Models components. It provides a centralized overview to view all machine learning assets in single interface.&#x20;

For pre-production servers such as MLflow, the table view displays model servers, models, versions, experiments, and runs. This helps you review training history, compare experimental runs, and manage model iterations with clarity.

For production servers, such as NVIDIA Triton, the table view displays model servers, models, and their corresponding versions. In addition to general metadata, the table highlights operational details such as environment, status, health, inference counts, latency, and memory usage, enabling you to monitor deployed models effectively.

With this consolidated view, you can navigate easily and quickly search, sort, and filter through large volumes of ML Models components to locate the exact asset you need.

To access the **Table View** for ML Models, click **ML Models** in the left navigation. Then, the ML Models landing page appears. In the Navigation pane, click **Actions** and select **View Table** from the menu options. The ML Models table view appears, displaying all ML Models components in a grid layout for easier visibility and comparison.

![ML Models Table View](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-19c7f17bd8f02b54afee57afe37b9588b86d98c8%2FML%20Models%20Table%20view.png?alt=media)

The ML Models table view is organized into multiple tabs based on ML Models component types:

<table><thead><tr><th width="157.33331298828125">Tab Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>All</strong></td><td>Displays all ML Models components, including model servers, models, versions, experiments, and runs (for MLflow), or model servers, models, and versions (for Triton).</td></tr><tr><td><strong>Model Server</strong></td><td>Lists all registered ML model servers with their associated metadata. For MLflow, this includes experiment and run tracking configurations. For Triton, this includes environment, health, and liveness details.</td></tr><tr><td><strong>Model</strong></td><td>Displays ML models and their associated properties and tags. For MLflow, these models are linked to experiments and versions. For Triton, models include deployment metadata such as platform, input/output schemas, and maximum batch size.</td></tr><tr><td><strong>Experiment</strong><br>(Pre-production only)</td><td>Shows all experiments logged under various models or versions.</td></tr><tr><td><strong>Version</strong></td><td>Lists individual model versions and related tracking metadata. For MLflow, versions include linked parameters, datasets, and artifacts. For Triton, versions include production statistics such as inference counts, execution counts, latency, and memory usage.</td></tr><tr><td><strong>Run</strong><br>(Pre-production only)</td><td>Displays detailed execution-level run information for experiments.</td></tr></tbody></table>

Each tab in the table view displays common and component-specific attributes in column format. The following table lists such attributes:

<table><thead><tr><th width="187.33331298828125">Column Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>The name of the ML Models component.</td></tr><tr><td><strong>Type</strong></td><td>Indicates the component type such as model, run, experiment, and so on.</td></tr><tr><td><strong>ML Tags</strong></td><td>Metadata tags logged during training.</td></tr><tr><td><strong>Parent</strong></td><td>The parent entity to which the component belongs, such as a server or model.</td></tr><tr><td><strong>Custom Properties</strong></td><td>User-defined metadata fields.</td></tr><tr><td><strong>Created By</strong></td><td>The user who created or modified the asset.</td></tr><tr><td><strong>Updated By</strong></td><td>The user who last modified the asset.</td></tr></tbody></table>

In the ML Models table view, you can customize and personalize the display of ML Models components, making it easier to focus on relevant metadata and streamline workflows. You can click the filter icon and use the available filter inputs beneath each column header to search or select values, such as filter by model name, type, or ML model server. Additionally, you can tailor the table view to display only the information most relevant to your role by clicking the configure icon and using the checkboxes to show or hide columns based on your preference. You can also rearrange column order using the drag-and-drop handles.

### ML Models Galaxy view

In the Navigation pane, under **Actions**, selecting **View Galaxy** displays the ML Models components in the Galaxy view. The Galaxy view shows a different visual layout that is useful for exploring relationships and connections among ML Models components. You can use the Galaxy view feature to view the structure of the data and its details quickly. This feature is especially useful when you want to view information that is not easily visualized using the navigation tree. When you open ML Models components in the Galaxy view, you can see the relationships in the data from a bird's eye view and drill down into the data for specific details.&#x20;

![ML Models Galaxy View](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-5efefa984dea3cc7e109333006a6195199953837%2FML%20Models%20Galaxy%20view.png?alt=media)

For pre-production servers such as MLflow, the Galaxy view highlights lineage between experiments, runs, versions, and models. This helps you trace how training datasets, parameters, and artifacts contribute to model development and evaluation.

For production servers such as NVIDIA Triton, the Galaxy view emphasizes the relationship between deployed models and their versions. It enables you to visualize operational connections, such as which versions are currently live, their configuration, and how they are linked to inference performance metrics.

By supporting both perspectives, the Galaxy view allows you to navigate and analyze ML models across the entire lifecycle, from experimental runs in development to deployed models serving predictions in production.

To learn more about Galaxy view and its available functions, see [Galaxy View](https://docs.hitachivantara.com/r/en-us/pentaho-data-catalog/10.2.x/mk-95pdc000/galaxy-view).
