# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/adding-data/upload-data-from-aws-gcp-and-azure/azure-blob-storage.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/upload-data-from-aws-gcp-and-azure/azure-blob-storage.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/adding-data/upload-data-from-aws-gcp-and-azure/azure-blob-storage.md

# Source: https://docs.roboflow.com/datasets/adding-data/upload-data-from-aws-gcp-and-azure/azure-blob-storage.md

# Azure Blob Storage

When dealing with image data storage in Azure Blob Storage and uploading to Roboflow, you generally have two options: using signed URLs or manually downloading images locally (via the Azure CLI) to upload them locally. The choice between these methods depends on your specific needs for data processing and management.

* **Signed URLs**: This method is particularly advantageous if you want to avoid the extra step and time consumption associated with downloading images to your local machine. With a signed URL, you can directly upload the image data from Azure Blob Storage to the Roboflow API without ever having to store it locally. This results in faster processing and less load on your local system.
* **CLI Locally**: There might be scenarios where you'd prefer to download the images to your local environment first. For instance, if you need to preprocess the images or manually check them before uploading to Roboflow, having local copies would be beneficial.

Selecting the right method will depend on your specific use-case requirements, like speed of data transfer, need for preprocessing, or manual inspection of images.

### Azure Connection String

After creating a Storage Account, you can find the access keys or connection string in the "Access keys" section under "Security + networking" in the Azure portal. These credentials are used to authenticate your application.

### Option 1: Upload Via Signed URL:

You can generate signed URLs for your images in the Azure Blob Storage by the Azure SDK in Python.

```python
def get_blob_sas_url(blob_service_client, container_name: str, blob_name: str) -> str:
    """Generate a SAS URL for an Azure Blob."""
    from azure.storage.blob import generate_blob_sas, BlobSasPermissions
    from datetime import datetime, timedelta

    sas_token = generate_blob_sas(
        blob_service_client.account_name,
        container_name,
        blob_name,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    return blob_url
```

In the code snippet above, you need the blob service client, the container name, and the blob name. The signed URL of the image is generated and returned.

Building around this, we can generate a complete solution that pulls all the available objects in the Azure Blob Storage, and then uploads them to Roboflow via the API. An outline for this solution can be seen below:

```python
from azure.storage.blob import BlobServiceClient
import requests
import urllib.parse

# ************* SET THESE VARIABLES *************
AZURE_CONNECTION_STRING = "YOUR_AZURE_CONNECTION_STRING"
AZURE_CONTAINER_NAME = "YOUR_AZURE_CONTAINER_NAME"
ROBOFLOW_API_KEY = "YOUR_ROBOFLOW_API_KEY"
ROBOFLOW_PROJECT_NAME = "YOUR_ROBOFLOW_PROJECT_NAME"
# ***********************************************

def get_blob_sas_url(blob_service_client, container_name: str, blob_name: str) -> str:
    """Generate a SAS URL for an Azure Blob."""
    from azure.storage.blob import generate_blob_sas, BlobSasPermissions
    from datetime import datetime, timedelta

    sas_token = generate_blob_sas(
        blob_service_client.account_name,
        container_name,
        blob_name,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    return blob_url

def get_azure_blob_objects(container_name: str) -> list:
    """Fetch the list of blob names in the given Azure Blob container."""
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(container_name)
    
    blobs = []
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        blobs.append(blob.name)
    return blobs

def upload_to_roboflow(api_key: str, project_name: str, presigned_url: str, img_name='', split="train"):
    """Upload an image to Roboflow."""
    API_URL = "https://api.roboflow.com"
    if img_name == '':
        img_name = presigned_url.split("/")[-1]

    upload_url = "".join([
        API_URL + "/dataset/" + project_name + "/upload",
        "?api_key=" + api_key,
        "&name=" + img_name,
        "&split=" + split,
        "&image=" + urllib.parse.quote_plus(presigned_url),
    ])
    response = requests.post(upload_url)

    # Check response code
    if response.status_code == 200:
        print(f"Successfully uploaded {img_name} to {project_name}")
        return True
    else:
        print(f"Failed to upload {img_name}. Error: {response.content.decode('utf-8')}")
        return False

if __name__ == "__main__":
    # Fetch list of available blobs
    available_blobs = get_azure_blob_objects(AZURE_CONTAINER_NAME)
    
    # Optional: Filter the blobs here
    # e.g., available_blobs = [blob for blob in available_blobs if "some_condition"]
    
    # Initialize Azure Blob Service Client
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    
    # Upload blobs to Roboflow
    for blob in available_blobs:
        blob_url = get_blob_sas_url(blob_service_client, AZURE_CONTAINER_NAME, blob)
        upload_to_roboflow(ROBOFLOW_API_KEY, ROBOFLOW_PROJECT_NAME, blob_url)

```

### Option 2: Download Data Locally from Azure

First, install the `azcopy` command line utility. This utility allows you to download files and folders from Azure Storage. Then, authenticate with your Azure account using a [Shared Access Signature](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) token. You can learn more about [how to retrieve an SAS token](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) in the azcopy documentation.

Once you have `azcopy` set up, run the following command to download a file or folder:

```bash
azcopy copy "C:\local\path" <sas-token> --recursive=true
```

Replace `C:\local\path` with the path of the folder or file you want to download. Replace the `<sas-token>` value with an SAS token for authentication. If you want to download files and folders recursively, specify the `--recursive=true` argument as above. Otherwise, remove this argument.

### Upload Data to Roboflow

Now that we have downloaded data, we can upload it to Roboflow either by using the [Upload Web Interface](https://docs.roboflow.com/datasets/adding-data/..#upload-data-with-the-web-interface) or the [Roboflow CLI](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/command-line-interface/upload-a-dataset).

### See Also

* [Retrieve a Roboflow project ID](https://docs.roboflow.com/api-reference/workspace-and-project-ids)
