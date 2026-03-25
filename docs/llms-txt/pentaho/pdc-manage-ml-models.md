# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-ml-models.md

# Manage Machine Learning (ML) Models

With the Machine Learning (ML) Models feature in Pentaho Data Catalog, you can connect to ML model servers and import their components, import ML metadata, and organize models, experiments, versions, and runs within a structured hierarchy. It brings machine learning workflows into the cataloging ecosystem, enabling seamless tracking, discoverability, and governance of ML assets alongside enterprise data. For more information, see the **Machine Learning (ML) Models** section in the Use Pentaho Data Catalog document.

Additionally, you can add an ML model server and its components locally and build out the entire ML Models hierarchy, including models, versions, experiments, and runs, without requiring a live connection to an MLflow or other tracking server. It helps data stewards to curate internal-only model components, manage legacy models, or maintain records of decommissioned ML assets that no longer exist in the original server. This local creation capability supports metadata completeness and governance readiness, enabling organizations to align their machine learning metadata with business policies and cataloging standards.

In Data Catalog, you can manage ML Models to maintain clarity, control, and consistency across the ML lifecycle. By creating, editing, and removing ML components as needed, you ensure that the catalog remains clean, up-to-date, and relevant to current analytical and business needs. Additionally, you can also import and export ML Model hierarchies to reuse, back up, and migrate ML assets across environments.

## Import ML model server components into Data Catalog

In Data Catalog, you can configure a connection to an ML model server as an external data source and import machine learning model metadata, including models, versions, experiments, runs, parameters, metrics, artifacts, and schemas, into the ML Models hierarchy. For configuration instructions, see Configure for ML Model Servers.

By importing these components, you can catalog, explore, and govern ML assets alongside other enterprise data. This supports reproducibility, transparency, and collaboration by making ML model metadata searchable and accessible within a centralized platform.

Perform the following steps to import ML model server components into Data Catalog:

Ensure that you have successfully configured the connection between Data Catalog and the ML model server. For more information, see [Configure a machine learning (ML) server connection in Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#configure-a-machine-learning-ml-server-connection-in-data-catalog)

1. On the left navigation menu, click **Management**.

   The Manage Your Environment page opens.
2. In the **Synchronize** card, click **View Synchronize**.

   The Synchronize page opens with a list of configured external data sources.
3. Identify the ML model server from which you want to import the metadata and components, and then click **Import**.

   The ML Models import worker starts the import process.

When the process is complete, you can view the imported ML model server components in the ML Models hierarchy. To know more, see the **Machine Learning (ML) Models** section in the **Use Pentaho Data Catalog** document.

## Add a new ML model server locally to Data Catalog

In Data Catalog, you can add an ML model server locally within the ML Models section, enhancing flexibility for managing machine learning assets. This feature is helpful when the ML model server has not yet been configured as an external data source or when you need to organize manually and curate ML model metadata for documentation, planning, or simulation purposes.

Perform the following steps to add a new ML model server locally to Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and then select **Add New Model Server**.

   The Create Model Server dialog box appears.
3. In the **Model Server Name** box, enter a name for the ML model server, and then click **Create**.

   The new ML model server appears on the ML Models list.

You have successfully added a new ML model server in Data Catalog locally in the ML Models hierarchy.

You can also add an ML model locally in Data Catalog. For more information, see [Add a new ML model locally to Data Catalog](#add-a-new-ml-model-server-locally-to-data-catalog).

## Add a new ML model locally to Data Catalog

Similar to [adding a new ML model server](#add-a-new-ml-model-server-locally-to-data-catalog), in Data Catalog, you can add an ML model locally within the ML Models hierarchy.

Perform the following steps to add a new ML model locally to Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and then select **Add New Model**.

   The Create Model dialog box appears.
3. In the **Model Name** box, enter a name for the ML model, select an appropriate ML model server in the **Parent** box, and then click **Create**.

   The new ML model appears on the ML Models hierarchy under the selected ML model server.

You have successfully added a new ML model in Data Catalog locally.

You can also add a version locally in Data Catalog. For more information, see [Add a new version locally to Data Catalog](#add-a-new-version-locally-to-data-catalog).

## Add a new experiment locally to Data Catalog

Similar to [adding a new ML model](#add-a-new-ml-model-locally-to-data-catalog), in Data Catalog, you can add an experiment to an ML model server locally within the ML Models hierarchy.

Perform the following steps to add a new experiment locally to Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and then select **Add New Experiment**.

   The Create Experiment dialog box appears.
3. In the **Experiment Name** box, enter a name for the experiment, select an appropriate ML model server in the **Parent** box, and then click **Create**.

   The new experiment appears on the ML Models hierarchy under the selected ML model server.

You have successfully added a new experiment in Data Catalog locally.

You can also add a run locally in Data Catalog. For more information, see [Add a new run locally to Data Catalog](#add-a-new-run-locally-to-data-catalog).

## Add a new version locally to Data Catalog

Similar to adding a new ML model, in Data Catalog, you can add a version to an ML model locally within the ML Models hierarchy.

Perform the following steps to add a new version locally to Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and then select **Add New Version**.

   The Create Version dialog box appears.
3. In the **Version Name** box, enter a name for the version, select an appropriate ML model in the **Parent** box, and then click **Create**.

   The new version appears on the ML Models hierarchy under the selected ML model.

You have successfully added a new version in Data Catalog locally.

## Add a new run locally to Data Catalog

Similar to [adding a new ML model](#add-a-new-ml-model-locally-to-data-catalog), in Data Catalog, you can add a run to an experiment locally within the ML Models hierarchy.

Perform the following steps to add a new run locally to Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and then select **Add New Run**.

   The Create Run dialog box appears.
3. In the **Run Name** box, enter a name for the run, select an appropriate experiment in the **Parent** box, and then click **Create**.

   The new run appears on the ML Models hierarchy under the selected experiment.

You have successfully added a new run in Data Catalog locally.

## Delete ML model server components

Over time, as models evolve, experiments become obsolete, or test data is no longer needed, and some components might lose their value or create clutter in Data Catalog. Additionally, Data Catalog users might want to remove incorrectly imported or manually added test components, correct metadata structure errors, and enforce internal data management policies.

In Data Catalog, you can delete ML model components, such as model servers, models, versions, experiments, or runs, from the ML Models hierarchy, allowing you to control the organization, accuracy, and relevance of machine learning metadata. It helps you to keep the catalog clean and focused, ensuring that only active, relevant, and trustworthy assets are visible and accessible.

Perform the following steps to delete an ML model component:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Select the ML model component you want to delete.
3. Click the **More** icon (three vertical dots) next to the component name and click **Delete**.

   A confirmation message appears.
4. Click **Confirm** to delete the component.

You have successfully deleted an ML model component in Data Catalog. However, it doesn’t remove the component from the original ML model server.

## Creating ML model relationships manually in ML Models hierarchy

In Data Catalog, you can manually link ML models from Training (ML Flow) to Production (Nvidia Triton Inference Server). This link helps track model lifecycle and improves governance, understanding, and trust in ML Model deployments. Users can discover and define relationships among ML models, enhancing data governance, model reproducibility, and insights into ML assets.

Perform the following steps to create an ML model relationship:

1. Navigate to **ML Models** service, click on Model in either in Training and Production server environment. The ML Models page opens.
2. On **Properties** card, click on pencil icon next to **Production Model**. Now it will open the Training Models. (if you come from Production environment you need to click on pencil icon for Training Model)
3. From the list, select a ML model that you want to create the relationship with. Now click on **Select**  button to save your changes.

You have successfully created a relationship between an ML model in production and training environment in Data Catalog. However, it doesn’t create these relationships in the original ML model server.

## Removing ML model relationships manually in ML Models hierarchy

In Data Catalog, you can manually unlink ML models from Training (ML Flow) to Production (Nvidia Triton Inference Server). This unlink helps create or override existing relationships in ML Model services.

Perform the following steps to remove an ML model relationship:

1. Navigate to **ML Models** service, click on Model in either in Training and Production server environment. The ML Models page opens.
2. On **Properties** card, click on pencil icon next to **Production Model**. Now it will open the Training Models. (if you come from Production environment you need to click on pencil icon for Training Model)
3. From the list, select a ML model that you want to remove the relationship with. Now click on **Remove**  button to save your changes.

You have successfully removed a relationship between an ML model in production and training environment in Data Catalog. However, it doesn’t remove these relationships in the original ML model server.

## Import ML model server components into ML Models hierarchy

In Data Catalog, you can import the ML model server components and bring entire ML model structures into the ML Models section from a file in one of the following file types:

* JSON Lines (Not JSON. See more here <https://jsonlines.org/>)
* Comma Separated Values (text/csv)

This includes importing ML model servers, models, versions, experiments, runs, parameters, metrics, artifacts, and schema definitions without rebuilding ML Models hierarchies manually in each environment, which is time-consuming and error-prone, especially when dealing with complex experiments, multiple versions, and extensive artifacts. Whether the hierarchy was exported from another Data Catalog instance or generated externally, you can restore or replicate it in just a few steps, preserving the metadata relationships and integrity.

Perform the following steps to import the ML model server components into the ML Models hierarchy:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and select **Import**.

   The Import Assets dialog box appears.
3. You can drag and drop the file or browse and select the file you want to import and click **Submit**.

   Ensure the file format and structure align with the requirements of the ML Models feature.

You have successfully imported the ML model server components into the Data Catalog ML Models section.

You can also export the ML Models hierarchy for Data Catalog. For more information, see [Export ML Models hierarchy](#export-ml-models-hierarchy).

## Export ML Models hierarchy

In Data Catalog, you can export the complete structure and metadata of ML models, including servers, models, versions, experiments, and runs, and save them into a structured file, CSV and JSON, making it easy to backup, share, or migrate ML model assets between environments or with other teams.

Perform the following steps to export ML model components from Data Catalog:

1. On the left navigation menu, click **ML Models**.

   The ML Models page opens.
2. Click **Actions** and select **Export**.

   The **Export Assets** dialog box appears.
3. Select what to export. Select individual ML model component, or choose **Select all** to export every ML model components in the list.\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
4. Select the file type (**CSV** or **JSON**) to which you want to export the ML Models hierarchy and then click **Submit**.

   The file containing the ML model server components in the selected format will be downloaded into the local folder.

You have successfully exported the ML model server components from Data Catalog.

You can also import ML model components into Data Catalog. For more information, see [Import ML model server components into ML Models hierarchy](#import-ml-model-server-components-into-ml-models-hierarchy).
