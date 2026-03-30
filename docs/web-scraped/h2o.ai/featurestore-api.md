# Source: https://docs.h2o.ai/featurestore/api

Title: API | H2O Feature Store

URL Source: https://docs.h2o.ai/featurestore/api

Markdown Content:
[Skip to main content](https://docs.h2o.ai/featurestore/api#__docusaurus_skipToContent_fallback)

[![Image 1: H2O AI Cloud logo](https://docs.h2o.ai/featurestore/img/h2oai.png) **Documentation**](https://docs.h2o.ai/haic-documentation/)

[Platform](https://docs.h2o.ai/featurestore/api#)

*   [AI App Store](https://docs.h2o.ai/h2o-ai-cloud/)
*   [H2O Admin Center](https://docs.h2o.ai/wave-mc-admin-center/)
*   [H2O Drive](https://docs.h2o.ai/h2o-drive/)
*   [H2O Orchestrator](https://docs.h2o.ai/h2o-orchestrator/)
*   [HAIC Platform](https://docs.h2o.ai/haic-documentation/)

[Applications](https://docs.h2o.ai/featurestore/api#)

*   [H2O Notebook Labs](https://docs.h2o.ai/notebook/)
*   [H2O AI Unit Consumption](https://docs.h2o.ai/wave-apps/ai-unit-consumption/)
*   [H2O Drive](https://docs.h2o.ai/h2o-drive/)
*   [H2O Label Genie](https://docs.h2o.ai/wave-apps/h2o-label-genie/)
*   [H2O Model Analyzer](https://docs.h2o.ai/wave-apps/h2o-model-analyzer/)
*   [H2O Model Validation](https://docs.h2o.ai/wave-apps/h2o-model-validation/)
*   [H2O Model Security](https://docs.h2o.ai/wave-apps/h2o-model-security/)
*   [H2O Admin Analytics](https://docs.h2o.ai/wave-apps/admin-analytics/)

[Models](https://docs.h2o.ai/featurestore/api#)

*   [H2O eScorer](https://docs.h2o.ai/h2o-escorer/)
*   [H2O MLOps](https://docs.h2o.ai/mlops/)
*   [H2O Admin Analytics](https://docs.h2o.ai/wave-apps/admin-analytics/)
*   [H2O Model Analyzer](https://docs.h2o.ai/wave-apps/h2o-model-analyzer/)
*   [H2O Model Validation](https://docs.h2o.ai/wave-apps/h2o-model-validation/)
*   [H2O Model Security](https://docs.h2o.ai/wave-apps/h2o-model-security/)

[AI Engines](https://docs.h2o.ai/featurestore/api#)

*   [AI Engine Manager](https://docs.h2o.ai/ai-engine-manager/)
*   [H2O Driverless AI](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/index.html)
*   [H2O Document AI](https://docs.h2o.ai/h2o-document-ai/)
*   [H2O Hydrogen Torch](https://docs.h2o.ai/h2o-hydrogen-torch/)
*   [H2O-3](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/index.html)

[GenAI](https://docs.h2o.ai/featurestore/api#)

*   [H2O GPT](https://github.com/h2oai/h2ogpt#readme)
*   [Enterprise h2oGPTe](https://docs.h2o.ai/h2ogpte-docs/)
*   [H2O LLM DataStudio](https://docs.h2o.ai/h2o-llm-data-studio/)
*   [H2O LLM Studio](https://docs.h2o.ai/h2o-llmstudio/)
*   [H2O Eval Studio](https://docs.h2o.ai/eval-studio-docs/)

[Python APIs](https://docs.h2o.ai/featurestore/api#)

*   [Enterprise h2oGPTe](https://h2oai.github.io/h2ogpte/index.html)
*   [H2O Eval Studio](https://docs.h2o.ai/eval-studio-docs/py-client)
*   [H2O Feature Store](https://h2oai.github.io/featurestore/api/client_initialization)
*   [H2O Drive](https://docs.h2o.ai/h2o-drive/python-client-guide)
*   [H2O eScorer](https://docs.h2o.ai/h2o-escorer/python-client-guide/py-client-guide)
*   [H2O MLOps](https://docs.h2o.ai/mlops/py-client/overview)
*   [H2O Driverless AI](https://docs.h2o.ai/driverless-ai/pyclient/docs/html/index.html)
*   [H2O-3](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/index.html)

[v2.4.0](https://docs.h2o.ai/featurestore/api)

*   [v2.4.0](https://docs.h2o.ai/featurestore/api)
*   [v2.3.3](https://docs.h2o.ai/featurestore/v2.3.3/api)
*   [v2.2.1](https://docs.h2o.ai/featurestore/2.2.1/api)
*   [v2.1.0](https://docs.h2o.ai/featurestore/v2.1.0/api)
*   [v2.0.2](https://docs.h2o.ai/featurestore/v2.0.0/api)
*   [v1.2.0](https://docs.h2o.ai/featurestore/v1.2.0/api)

*   [](https://docs.h2o.ai/featurestore/)
*   API

Version: v2.4.0

Contents[​](https://docs.h2o.ai/featurestore/api#contents "Direct link to Contents")
------------------------------------------------------------------------------------

[📄️Credentials configuration ---------------------------- Different data sources require different credentials which users need to specify.](https://docs.h2o.ai/featurestore/api/client_credentials)[📄️Starting the client ---------------------- Explore the first steps on how to use the Feature Store client.](https://docs.h2o.ai/featurestore/api/client_initialization)[📄️Default naming rules ----------------------- Feature Store is configured to adhere to the restrictions on setting names for a project or a feature set as explained in this page.](https://docs.h2o.ai/featurestore/api/naming_conventions)[📄️Authentication ----------------- The Feature Store CLI provides 3 forms of authentication; Access token from external environment, Refresh token from identity provider, and Personal Access Tokens (PATs).](https://docs.h2o.ai/featurestore/api/authentication)[📄️Permissions -------------- Permissions determine the level of access that a user has to various components of the Feature Store. For example, depending on the level of permission granted, a user may be authorized to edit feature sets, while another user with limited view-only permission can only observe the feature set.](https://docs.h2o.ai/featurestore/api/permissions)[📄️Projects API --------------- Listing projects](https://docs.h2o.ai/featurestore/api/projects_api)[📄️Schema API ------------- A schema is extracted from a data source. The schema represents the features of the feature set.](https://docs.h2o.ai/featurestore/api/schema_api)[📄️Feature set API ------------------ Registering a feature set](https://docs.h2o.ai/featurestore/api/feature_set_api)[📄️Feature API -------------- Using FeatureType Enum](https://docs.h2o.ai/featurestore/api/feature_api)[📄️Ingest API ------------- Feature store ensures that data for each specific feature set does not contain duplicates. That means that only data which are unique to the feature set storage are ingested as part of the ingest operation. The rows that would lead to duplicates are skipped. Ingest can be run on instance of feature set representing any minor version. The data are always ingested on top of latest storage stage.](https://docs.h2o.ai/featurestore/api/ingest_api)[📄️Ingest history API --------------------- Getting the ingestion history](https://docs.h2o.ai/featurestore/api/ingest_history_api)[📄️Retrieve API --------------- Retrieval API overview.](https://docs.h2o.ai/featurestore/api/retrieve_api)[📄️Jobs API ----------- Listing jobs](https://docs.h2o.ai/featurestore/api/jobs_api)[📄️Create new feature set version API ------------------------------------- A feature set is a collection of features. Users can create a new version of an existing feature set for various reasons.](https://docs.h2o.ai/featurestore/api/feature_set_new_version)[📄️Asynchronous methods ----------------------- Several methods in the Feature Store Client API have asynchronous variants.](https://docs.h2o.ai/featurestore/api/async)[📄️Spark dependencies --------------------- Users can interact with Feature Store from a Spark session by adding several dependencies on the Spark Classpath. Supported Spark versions are 3.5.x.](https://docs.h2o.ai/featurestore/api/spark_dependencies)[📄️Recommendation API --------------------- A Recommendation API can be used to suggest personalized recommendations based on the data stored in the feature sets. If users have two different feature sets, they can use a Recommendation API to find similarities between the features in those sets and recommend features that are similar in nature or data type.](https://docs.h2o.ai/featurestore/api/recommendation_api)[📄️Feature set schedule API --------------------------- Users can schedule an ingestion job from Feature Store by using API available on the feature sets.](https://docs.h2o.ai/featurestore/api/feature_set_schedule)[📄️Feature set review API ------------------------- Feature set review process involves the reviewer's acceptance. Depending on the system configuration, all feature sets or only sensitive ones may be subject to review.](https://docs.h2o.ai/featurestore/api/feature_set_review_api)[📄️Dashboard API ---------------- Dashboard provides a short summary about the usage of Feature store.](https://docs.h2o.ai/featurestore/api/dashboard_api)

* * *

Feedback

*   [Submit and view feedback for this page](https://github.com/h2oai/docs-issues-requests/issues/new?assignees=shaunyogeshwaran&body=%23%23%23%20Documentation%20issue%2Frequest%0A%0A%3C!--%20Please%20provide%20a%20clear%20and%20concise%20description%20of%20the%20documentation%20issue%2Frequest%20--%3E%0A%0A%23%23%23%20Additional%20context%0A%0A%3C!--%20Please%20add%20any%20other%20context%20about%20the%20issue%2Frequest%20here%20(e.g.%2C%20images)%20--%3E%0A%0A%23%23%23%20Page%20details%20%0A%0A-%20Application%20name%3A%20H2O%20Feature%20Store%0A-%20Application%20version%3A%200.0.0%0A-%20Page%20title%3A%20/featurestore/api%20&title=%5BHAIC-APP%5D)
*   Send feedback about H2O Feature Store to [cloud-feedback@h2o.ai](mailto:cloud-feedback@h2o.ai)

[Previous Concepts](https://docs.h2o.ai/featurestore/concepts)[Next Credentials configuration](https://docs.h2o.ai/featurestore/api/client_credentials)
