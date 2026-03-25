# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-02-19-spcs-model-serving-auto-suspend.md

# Feb 19, 2025: Snowflake ML Model Serving Automatic Suspension (*Preview*)

Snowflake is pleased to announce that model inference services created by Snowflake ML Model Serving now automatically
suspend after thirty minutes of inactivity. They are restarted upon the next incoming request. To allow models to be
available at all times to service requests from the public Internet, automatic suspension is disabled for services with
HTTP ingress enabled.

For more information, see [Deploy models for Real time Inference (REST API)](../../../developer-guide/snowflake-ml/inference/real-time-inference-rest-api.md).
