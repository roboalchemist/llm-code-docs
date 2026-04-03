# Source: https://docs.jfrog.com/artifactory/docs/use-hugging-face-with-jfrog-cli.md

# Use Hugging Face with Jfrog CLI

Download or upload ML models and datasets from/to Hugging Face repositories hosted in JFrog Artifactory, with build information collection.

## **When to Use**

Use `jf hf` if your ML project uses Hugging Face models or datasets and you want to resolve them from or deploy them to Artifactory. This provides centralized artifact management, access control, and build traceability for ML pipelines.

Use `jf hf download` instead of calling `huggingface_hub.snapshot_download()` directly when you need build information collection (dependency tracking with checksums). Use `jf hf upload` instead of calling `HfApi.upload_folder()` directly when you need artifact tracking in build info.

If you only need to cache models locally without Artifactory integration, you can use either `jf hf` or the `huggingface_hub` Python library directly.

## **Supported Commands**

| Command          | Alias     | Description                                  |
| ---------------- | --------- | -------------------------------------------- |
| `jf hf download` | `jf hf d` | Download models or datasets from Artifactory |
| `jf hf upload`   | `jf hf u` | Upload a local folder to Artifactory         |

## **How It Works**

The `jf hf` commands wrap Python scripts that call the `huggingface_hub` library. When you run a command, JFrog CLI:

1. Locates a Python 3 interpreter on your system
2. Executes the appropriate Python script with your parameters
3. Reports the result (download path or upload confirmation)
4. Optionally collects build information for traceability

## **What Is Not Supported**

Only `download` and `upload` operations are supported. Artifactory does not currently support the full set of native `huggingface-cli` commands (such as `auth`, `cache`, `repo`, `spaces`, `collections`, `endpoints`, `jobs`, `models`, `papers`, `repo-files`, `skills`, `upload-large-folder`). Commands execute via Python scripts; the native `huggingface-cli` binary is not used. If Artifactory becomes compatible with the Hugging Face CLI in the future, all native commands can be supported.

***

## **Prerequisites**

* Python 3 or higher must be installed (the CLI searches for `python3` first, then `python`).
* The `huggingface_hub` Python library must be installed.
* Configure a server with `jf config add` or `jf c add`.
* Authentication to Artifactory is required.
* Optionally set `HF_ENDPOINT` and `HF_TOKEN` environment variables. If you have server details stored via `jf c add`, the CLI automatically sets `HF_TOKEN`. You can also provide the `--repo-key <repo-name>` flag in `jf hf` commands to have the CLI automatically set `HF_ENDPOINT`.

### **JFrog CLI**

Install and configure JFrog CLI. For installation options, see the [JFrog CLI documentation](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli/install).

Verify that JFrog CLI is installed:

```shell
jf --version
```

Configure a server connection:

```shell
jf config add <server-id> --url=<your-platform-url> --access-token=<your-token> --interactive=false
```

<br />

### **Python 3**

The Hugging Face commands require Python 3 or higher. The CLI searches for `python3` first, then falls back to `python`. If `python` is found, its version is verified and must be 3 or higher.

Verify your Python version:

```shell
python3 --version
```

Install Python 3:

| Platform      | Command                                                       |
| ------------- | ------------------------------------------------------------- |
| macOS         | `brew install python3`                                        |
| Ubuntu/Debian | `sudo apt install python3`                                    |
| Windows       | Download from [python.org](https://www.python.org/downloads/) |

### **huggingface\_hub Library**

Install the `huggingface_hub` Python library:

```shell
pip install huggingface_hub
```

Verify the installation:

```shell
pip show huggingface_hub
```

<br />

### **Artifactory Repository**

Your JFrog Artifactory instance must have a Hugging Face repository configured. Contact your Artifactory administrator to create one if it does not already exist.

### **Why Set Environment Variables?**

Setting `HF_ENDPOINT` and `HF_TOKEN` tells the underlying `huggingface_hub` library to communicate with your Artifactory instance instead of the public Hugging Face Hub. However, these variables are optional if you have server details stored via `jf c add` (which automatically sets `HF_TOKEN`) and use the `--repo-key` flag (which automatically sets `HF_ENDPOINT`).

Shortcut: In CI/CD, set these as pipeline environment variables so every step has them automatically.

***

## **Environment Variables**

Set the following environment variables before running Hugging Face commands.

### **HF\_ENDPOINT**

The URL of your Hugging Face repository in JFrog Artifactory. This variable redirects the `huggingface_hub` Python library to use Artifactory instead of the public Hugging Face Hub.

```shell
export HF_ENDPOINT=
https://<your-instance>.jfrog.io/artifactory/api/huggingfaceml/<repo-key>

```

Format: The URL must point to the Hugging Face API endpoint in Artifactory. The last segment of the URL is used as the repository key for AQL queries during build info collection.

Example:

```shell
export HF_ENDPOINT="https://acme.jfrog.io/artifactory/api/huggingface/hf-local"
```

In this example, `hf-local` is the repository key.

### **HF\_TOKEN**

An authentication token for accessing the Hugging Face repository in Artifactory. This can be a JFrog access token or an identity token with appropriate permissions.

```shell
export HF_TOKEN="<your-token>"
```

### **How the CLI Uses These Variables**

| Variable      | Used For                                                                                                                                        |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `HF_ENDPOINT` | Passed to the `huggingface_hub` library to route requests to Artifactory. Also parsed by the CLI to extract the repository key for AQL queries. |
| `HF_TOKEN`    | Passed to the `huggingface_hub` library for authentication against the Artifactory Hugging Face repository.                                     |

### **Persistence**

To avoid setting these variables in every terminal session, add them to your shell profile:

```shell
# Add to ~/.bashrc, ~/.zshrc, or equivalent
export HF_ENDPOINT="https://acme.jfrog.io/artifactory/api/huggingface/hf-local"
export HF_TOKEN="<your-token>"
```

<br />

<Callout icon="❗️">
  Store tokens securely. Do not commit `HF_TOKEN` values to version control. Consider using a secrets manager or environment-specific configuration files excluded from source control.
</Callout>

## **Quick Start**

Get up and running with JFrog CLI Hugging Face commands in five minutes.

### **Step 1: Verify Your Setup**

```shell
jf --version
python3 --version
```

### **Step 2: Set Environment Variables**

```shell
export HF_ENDPOINT="https://<your-instance>.jfrog.io/artifactory/api/huggingface/<repo-key>"
export HF_TOKEN="<your-token>"
```

### **Step 3: Download a Model**

```shell
jf hf download sshleifer/tiny-gpt2
```

Expected output:

```
Downloaded successfully to: /home/user/.cache/huggingface/hub/models--sshleifer--tiny-gpt2/snapshots/abc123
```

To download a dataset instead:

```shell
jf hf download <organization>/<dataset-name> --repo-type=dataset
```

### **Step 4: Upload a Model**

```shell
jf hf upload ./my-model-files myorg/my-custom-model
```

Expected output:

```
Uploaded successfully to: myorg/my-custom-model
```

### **Step 5: Collect Build Information (Optional)**

```shell
jf hf download <organization>/<model-name> --build-name=my-ml-build --build-number=1
jf hf upload ./my-model-files <organization>/<model-name> --build-name=my-ml-build --build-number=1
jf rt build-publish my-ml-build 1
```

***

## **Command Reference: jf hf download**

Download models or datasets from a Hugging Face repository hosted in JFrog Artifactory.

### **Synopsis**

```

hf download <model-name>

jf hf download <repo_id> [options]

jf hf d <repo_id> [options]
```

### **Arguments**

| Argument  | Required | Description                                                                                                                             |
| --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `repo_id` | Yes      | The repository ID, formatted as `organization/name` (for example, `sshleifer/tiny-gpt2` or `hf-internal-testing/fixtures_image_utils`). |

### **Options**

| Flag                 | Default     | Description                                                                                                                                                                                                                                                 |
| -------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`--revision`**     | **`main`**  | **The specific revision, branch, tag, or commit hash to download.**                                                                                                                                                                                         |
| **`--repo-type`**    | **`model`** | **The repository type. Accepted values: `model`, `dataset`.**                                                                                                                                                                                               |
| **`--etag-timeout`** | **`86400`** | **Timeout in seconds for ETag validation. Set to control cache freshness checks. Default is 24 hours.**                                                                                                                                                     |
| **`--repo-key`**     | **--**      | **Repository key for the Hugging Face repository in Artifactory. Required if the** `HF_ENDPOINT` environment variable is not set. When provided, the CLI automatically constructs and sets **`HF_ENDPOINT` using the configured server's Artifactory URL.** |
| **`--server-id`**    | **--**      | **Server ID configured via `jf c add`. Used to resolve server details and automatically set `HF_TOKEN`.**                                                                                                                                                   |
| **`--build-name`**   | **--**      | **Build name for build info collection. Requires `--build-number`.**                                                                                                                                                                                        |
| **`--build-number`** | **--**      | **Build number for build info collection. Requires `--build-name`.**                                                                                                                                                                                        |
| **`--module`**       | **--**      | **Optional module name for the build info. Requires `--build-name` and `--build-number`.**                                                                                                                                                                  |
| **`--project`**      | **--**      | **JFrog project key for project-scoped build info.**                                                                                                                                                                                                        |

<br />

### **How It Works**

This command calls the `huggingface_hub.snapshot_download()` Python function:

```py
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="<MODEL_NAME>",
    revision="<REVISION_ID>",
    repo_type="<REPO_TYPE>",
    etag_timeout=86400
)
```

It downloads the entire repository snapshot (all files for the specified revision) to the local Hugging Face cache directory, typically `~/.cache/huggingface/hub/`.

When `--build-name` and `--build-number` are provided, the command queries Artifactory via AQL to collect dependency information (file names, checksums) and saves it to the local build info.

### **Examples**

#### **View Help**

```shell
jf hf --help
```

#### **Download a Model**

```shell
jf hf download sshleifer/tiny-gpt2
```

Expected output:

```
$ jf hf download sshleifer/tiny-gpt2
Downloaded successfully to: /home/user/.cache/huggingface/hub/models--sshleifer--tiny-gpt2/snapshots/abc123
```

#### **How to Verify**

After downloading, confirm the files exist in the Hugging Face cache:

```shell
ls ~/.cache/huggingface/hub/models--sshleifer--tiny-gpt2/snapshots/
```

#### **Download a Dataset**

```shell
jf hf download hf-internal-testing/fixtures_image_utils --repo-type=dataset
```

#### **Download a Specific Revision**

```shell
jf hf download <organization>/<model-name> --revision=v1.0
```

#### **Download with a Custom ETag Timeout**

```shell
jf hf download <organization>/<model-name> --etag-timeout=3600
```

#### **Download with Build Information**

```shell
jf hf download <organization>/<model-name> --build-name=ml-pipeline --build-number=42
```

Expected output:

```
$ jf hf download myorg/my-model --build-name=ml-pipeline --build-number=42
Downloaded successfully to: /home/user/.cache/huggingface/hub/models--myorg--my-model/snapshots/abc123
Build info saved locally.
```

#### **Download with Build Info and Module**

```shell
jf hf download <organization>/<model-name> --build-name=ml-pipeline --build-number=42 --module=inference-model
```

### **Download Errors**

| Error                                         | Cause                                         | Fix                                                                                                                 |
| --------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `repo_id cannot be empty`                     | No repository ID provided                     | Provide a repository ID as the first argument                                                                       |
| `neither python3 nor python found in PATH`    | Python 3 is not installed                     | Install Python 3 and add it to your PATH                                                                            |
| `HF_ENDPOINT environment variable is not set` | Missing environment variable                  | Export `HF_ENDPOINT` with your Artifactory repository URL, or provide the `--repo-key` flag to set it automatically |
| `Python script produced no output`            | Script execution failed silently              | Check Python installation and `huggingface_hub` library                                                             |
| 404 / repository not found                    | Invalid repository ID or model does not exist | Verify the repository ID and check that the model exists in Artifactory                                             |

<br />

<Callout icon="📘" theme="info">
  Download progress may appear slow for large files. This is due to the underlying `huggingface_hub` Python library, not JFrog CLI itself.
</Callout>

<br />

## **Command Reference: jf hf upload**

Upload a local folder containing models or datasets to a Hugging Face repository hosted in JFrog Artifactory.

### **Synopsis**

```
jf hf upload <folder_path> <repo_id> [options]
jf hf u <folder_path> <repo_id> [options]
```

### **Arguments**

| Argument      | Required | Description                                                                                 |
| ------------- | -------- | ------------------------------------------------------------------------------------------- |
| `folder_path` | Yes      | Path to the local folder containing the model or dataset files to upload.                   |
| `repo_id`     | Yes      | The repository ID, formatted as `organization/name` (for example, `myorg/my-custom-model`). |

### **Options**

<br />

| Flag                 | Default     | Description                                                                                                                                                                                                                                                 |
| -------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`--revision`**     | **`main`**  | **The specific revision, branch, or tag to upload to.**                                                                                                                                                                                                     |
| **`--repo-type`**    | **`model`** | **The repository type. Accepted values: `model`, `dataset`.**                                                                                                                                                                                               |
| **`--repo-key`**     | **--**      | **Repository key for the Hugging Face repository in Artifactory. Required if the** `HF_ENDPOINT` environment variable is not set. When provided, the CLI automatically constructs and sets **`HF_ENDPOINT` using the configured server's Artifactory URL.** |
| **`--server-id`**    | **--**      | **Server ID configured via `jf c add`. Used to resolve server details and automatically set `HF_TOKEN`.**                                                                                                                                                   |
| **`--build-name`**   | **--**      | **Build name for build info collection. Requires `--build-number`.**                                                                                                                                                                                        |
| **`--build-number`** | **--**      | **Build number for build info collection. Requires `--build-name`.**                                                                                                                                                                                        |
| **`--module`**       | **--**      | **Optional module name for the build info. Requires `--build-name` and `--build-number`.**                                                                                                                                                                  |
| **`--project`**      | **--**      | **JFrog project key for project-scoped build info.**                                                                                                                                                                                                        |

<br />

### **How It Works**

This command calls the `huggingface_hub.HfApi.upload_folder()` Python function:

```py
from huggingface_hub import HfApi
api = HfApi()
api.upload_folder(
    folder_path="<FOLDER_NAME>",
    repo_id="<PACKAGE_NAME>",
    revision="<REVISION_ID>",
    repo_type="<REPO_TYPE>"
)
```

It uploads the entire contents of the specified local folder to the target Hugging Face repository in Artifactory.

When `--build-name` and `--build-number` are provided, the command:

1. Queries Artifactory via AQL to find the uploaded files
2. Collects file metadata (name, type, SHA-1, MD5, SHA-256 checksums)
3. Records each file as an artifact in the build info module
4. Sets build properties on the uploaded folder in Artifactory

### **Examples**

#### **Upload a Model**

```shell
jf hf upload ./my-model-files myorg/my-custom-model
```

Expected output:

```
$ jf hf upload ./my-model-files myorg/my-custom-model
Uploaded successfully to: myorg/my-custom-model
```

#### **How to Verify**

After uploading, confirm the artifacts exist in Artifactory:

```shell
jf rt search "hf-local/models/myorg/my-custom-model/*"
```

Or browse the repository in the Artifactory UI under `hf-local > models > myorg > my-custom-model`.

#### **Upload a Dataset**

```shell
jf hf upload ./my-dataset-dir myorg/my-dataset --repo-type=dataset
```

#### **Upload to a Specific Revision**

```shell
jf hf upload ./my-model-files myorg/my-custom-model --revision=v2.0
```

#### **Upload with Build Information**

```shell
jf hf upload ./my-model-files myorg/my-custom-model --build-name=ml-pipeline --build-number=42
```

Expected output:

```
$ jf hf upload ./my-model-files myorg/my-custom-model --build-name=ml-pipeline --build-number=42
Uploaded successfully to: myorg/my-custom-model
Build info saved locally.
```

#### **Upload with Build Info and Project Scope**

```shell
jf hf upload ./my-model-files myorg/my-custom-model --build-name=ml-pipeline --build-number=42 --project=ml-team
```

### **Upload Errors**

| Error                                         | Cause                            | Fix                                                                                                                 |
| --------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `folder_path cannot be empty`                 | No folder path provided          | Provide the path to a local folder as the first argument                                                            |
| `repo_id cannot be empty`                     | No repository ID provided        | Provide a repository ID as the second argument                                                                      |
| `neither python3 nor python found in PATH`    | Python 3 is not installed        | Install Python 3 and add it to your PATH                                                                            |
| `HF_ENDPOINT environment variable is not set` | Missing environment variable     | Export `HF_ENDPOINT` with your Artifactory repository URL, or provide the `--repo-key` flag to set it automatically |
| `Python script produced no output`            | Script execution failed silently | Check Python installation and `huggingface_hub` library                                                             |
| Upload fails with empty directory             | Folder contains no files         | Verify the folder path contains the files to upload                                                                 |

***

<br />

## **Build Information**

Both `download` and `upload` commands support build information collection for ML pipeline traceability.

### **Enabling Build Info Collection**

Add `--build-name` and `--build-number` to any command:

```shell
jf hf download <repo_id> --build-name=<name> --build-number=<number>
jf hf upload <folder_path> <repo_id> --build-name=<name> --build-number=<number>
```

### **Build Info Flags**

| Flag             | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| `--build-name`   | Build name for build info collection. Requires `--build-number`. |
| `--build-number` | Build number for build info collection. Requires `--build-name`. |
| `--module`       | Optional module name for the build info.                         |
| `--project`      | JFrog project key for project-scoped builds.                     |

### **Publishing Build Information**

After running commands with build info flags, publish to Artifactory:

```shell
jf rt build-publish <build-name> <build-number>
```

<br />

### **What Build Info Contains**

For downloads (dependencies):

The download command queries Artifactory using AQL to find all files in the downloaded repository path and records:

* File name and type
* SHA-1, MD5, and SHA-256 checksums
* Repository information
* Module ID set to the value provided in the `--module` flag. If not provided, defaults to `huggingfaceml-model` or `huggingfaceml-dataset` depending on the repository type.

For uploads (artifacts):

The upload command queries Artifactory to find the uploaded files and records:

* File name and type
* SHA-1, MD5, and SHA-256 checksums
* Build properties (`build.name`, `build.number`, `build.timestamp`, `build.project`)
* Module ID set to the value provided in the `--module` flag. If not provided, defaults to `huggingfaceml-model` or `huggingfaceml-dataset` depending on the repository type.

### **Why Build Info Uses Artifactory Queries**

When uploading to Artifactory, a revision ID + timestamp directory is created (for example, `main_2026-02-24T18:52:40.655Z`). The timestamp is generated by Artifactory and cannot be predicted in advance. Therefore, the CLI queries Artifactory via AQL after the operation to collect the actual artifact paths and checksums.

***

<br />

## **Tutorial: Manage ML Models End to End**

This tutorial walks through a complete workflow: download a model, inspect it, upload a modified version, and collect build information.

### **Step 1: Verify Your Environment**

```shell
jf --version
python3 --version
pip show huggingface_hub
echo "HF_ENDPOINT=$HF_ENDPOINT"
jf config show
```

### **Step 2: Download a Model**

Download a model with build info collection:

```shell
jf hf download <organization>/<model-name> \
  --build-name=ml-pipeline \
  --build-number=1
```

Expected output:

```
Downloaded successfully to: /home/user/.cache/huggingface/hub/models--organization--model-name/snapshots/abc123
Build info saved locally.
```

### **Step 3: Inspect the Downloaded Files**

```shell
ls ~/.cache/huggingface/hub/models--<organization>--<model-name>/snapshots/
```

A typical model directory contains:

```
config.json
model.safetensors
tokenizer.json
tokenizer_config.json
special_tokens_map.json
```

### **Step 4: Prepare a Modified Model**

```shell
mkdir -p ./my-fine-tuned-model
cp ~/.cache/huggingface/hub/models--<organization>--<model-name>/snapshots/*/config.json ./my-fine-tuned-model/
```

Add or replace files as needed for your fine-tuned model.

### **Step 5: Upload the Modified Model**

```shell
jf hf upload ./my-fine-tuned-model <organization>/<new-model-name> \
  --build-name=ml-pipeline \
  --build-number=1
```

### **Step 6: Publish Build Information**

```shell
jf rt build-publish ml-pipeline 1
```

### **Step 7: Verify Build Information (Optional)**

```shell
jf rt curl -XGET "/api/build/ml-pipeline/1"
```

The build info contains:

* Dependencies: Model files downloaded in Step 2 (with checksums)
* Artifacts: Model files uploaded in Step 5 (with checksums)
* Module: The repository ID used for each command

### **Working with Datasets**

The same workflow applies to datasets. Add the `--repo-type=dataset` flag:

```shell
jf hf download <organization>/<dataset-name> --repo-type=dataset --build-name=data-pipeline --build-number=1
jf hf upload ./my-dataset-dir <organization>/<dataset-name> --repo-type=dataset --build-name=data-pipeline --build-number=1
jf rt build-publish data-pipeline 1
```

### **Clean Up**

```shell
rm -rf ./my-fine-tuned-model
```

<br />

***

## **Troubleshooting**

### **Detailed Errors**

#### **Python Not Found**

Error:

```
neither python3 nor python found in PATH. Please ensure Python 3 is installed and available in your PATH
```

Fix: Install Python 3 and ensure `python3` is available in your PATH.

#### **Python Version Too Low**

Error:

```
Python version 2 found, but version 3 or higher is required
```

Fix: Install Python 3. The CLI prefers `python3` over `python`.

#### **huggingface\_hub Library Not Installed**

Error:

```
ModuleNotFoundError: No module named 'huggingface_hub'
```

Fix:

```shell
pip install huggingface_hub
```

If you have multiple Python installations:

```shell
python3 -m pip install huggingface_hub
```

#### **HF\_ENDPOINT Not Set**

Error:

```
HF_ENDPOINT environment variable is not set
```

Fix:

Either export the variable manually or provide the --repo-key flag to have the CLI set it automatically.

```shell


# Option 1: Set the environment variable
export HF_ENDPOINT="https://<your-instance>.jfrog.io/artifactory/api/huggingface/<repo-key>"

# Option 2: Use the --repo-key flag
jf hf download <repo_id> --repo-key=<repo-key>

```

Note: This error occurs during the build info collection phase. The download or upload operation itself may succeed, but the build info step fails without HF\_ENDPOINT.

#### **Invalid HF\_ENDPOINT Format**

Error:

```
could not extract repo key from HF_ENDPOINT: <url>
```

Fix: Verify the URL format: `https://<instance>/artifactory/api/huggingface/<repo-key>`. The last segment is used as the repository key.

#### **Repository ID Cannot Be Empty**

Error:

```
Model/Dataset name is required. (when no argument is given) or Model/Dataset name cannot be empty. (when argument is an empty string)
```

Fix: Provide the repository ID: `jf hf download <organization>/<model-name>`

#### **Folder Path Cannot Be Empty**

Error:

```
Folder path and repository ID are required. (when fewer than 2 arguments given) or Folder path cannot be empty. (when first argument is empty string)
```

Fix: Provide the folder path and repository ID: `jf hf upload <folder-path> <organization>/<model-name>`

#### **Repository Not Found (404)**

Error:

```
404 Client Error: Not Found for url
```

Fix:

1. Verify the repository ID is correct (format: `organization/name`)
2. Check that the model or dataset exists in your Artifactory instance
3. Confirm that `HF_ENDPOINT` points to the correct repository
4. Verify your authentication token has read access

#### **Python Script Produced No Output**

Error:

```
Python script produced no output. The script may not be executing correctly.
```

Fix:

1. Update `huggingface_hub`: `pip install --upgrade huggingface_hub`
2. Test the Python function directly:

```py
from huggingface_hub import snapshot_download
snapshot_download(repo_id="<model-name>", revision="main", etag_timeout=86400)
```

3. Check stderr output for error details.

#### **Failed to Parse Python Script Output**

Error:

```
failed to parse Python script output: <error>, output: <raw-output>
```

Fix: Check the raw output for Python deprecation warnings or print statements from imported libraries.

#### **Slow Download Progress**

Symptom: Download progress bar moves very slowly for large files.

Cause: Known behavior of the `huggingface_hub` Python library. The download is proceeding normally.

#### **Build Info Not Saved**

Symptom: Command succeeds but no build info is collected.

Fix: Both `--build-name` and `--build-number` are required:

```shell
jf hf download <repo_id> --build-name=my-build --build-number=1
```

#### **Upload Fails with Empty Directory**

Symptom: Upload command fails when the source directory is empty.

Fix: Verify the folder path contains files: `ls -la <folder-path>`

#### **Authentication Errors**

Symptom: Command fails with authentication or permission errors.

Fix:

1. Verify `HF_TOKEN` is set: `echo $HF_TOKEN`
2. Regenerate the token if expired
3. Verify the token has read and write permissions

<br />