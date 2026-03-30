# optuna.artifacts

The `artifacts` module provides the way to manage artifacts (output files) in Optuna.
Please also check Optuna Artifacts Tutorial and our article [https://medium.com/optuna/file-management-during-llm-large-language-model-trainings-by-optuna-v4-0-0-artifact-store-5bdd5112f3c7].
The storages covered by `artifacts` are the following:

Class Name

Supported Storage

FileSystemArtifactStore

Local File System, Network File System

Boto3ArtifactStore

Amazon S3 Compatible Object Storage

GCSArtifactStore

Google Cloud Storage

Note

The methods defined in each `ArtifactStore` are not intended to be directly accessed by library users.