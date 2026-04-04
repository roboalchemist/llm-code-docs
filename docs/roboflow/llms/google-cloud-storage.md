# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/adding-data/upload-data-from-aws-gcp-and-azure/google-cloud-storage.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/upload-data-from-aws-gcp-and-azure/google-cloud-storage.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/adding-data/upload-data-from-aws-gcp-and-azure/google-cloud-storage.md

# Source: https://docs.roboflow.com/datasets/adding-data/upload-data-from-aws-gcp-and-azure/google-cloud-storage.md

# Google Cloud Storage

When dealing with image data storage in Google Cloud Storage and uploading to Roboflow, you generally have two options: using signed URLs or manually downloading images locally (via the gsutil CLI) to upload them locally. The choice between these methods depends on your specific needs for data processing and management.

* **Signed URLs**: This method is particularly advantageous if you want to avoid the extra step and time consumption associated with downloading images to your local machine. With a signed URL, you can directly upload the image data from Google Cloud Storage to the Roboflow API without ever having to store it locally. This results in faster processing and less load on your local system.
* **CLI Locally**: There might be scenarios where you'd prefer to download the images to your local environment first. For instance, if you need to preprocess the images or manually check them before uploading to Roboflow, having local copies would be beneficial.

Selecting the right method will depend on your specific use-case requirements, like speed of data transfer, need for preprocessing, or manual inspection of images.

### Google Cloud JSON Key

Create a service account with appropriate permissions for the bucket and download the JSON key file. This file will contain the credentials used to authenticate your application.

### Option 1: Upload Via Signed URL:

You can generate signed URLs for your images in the Google Cloud Storage bucket by using the Google Cloud SDK in Python.

```python
def get_gcs_signed_url(bucket_name: str, blob_name: str) -> str:
    """Generate a signed URL for a GCS object."""
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    
    url = blob.generate_signed_url(
        version="v4",
        expiration=3600,  # 1 hour in seconds
        method="GET"
    )
    return url
```

In the code snippet above, you need the name of your Google Cloud Storage bucket and the blob name. The signed URL of the image is generated and returned.

Building around this, we can generate a complete solution that pulls all the available objects in the bucket, and then uploads them to Roboflow via the API. An outline for this solution can be seen below:

```python
from google.cloud import storage
import requests
import urllib.parse

# ************* SET THESE VARIABLES *************
GCS_BUCKET_NAME = "YOUR_GCS_BUCKET_NAME"
ROBOFLOW_API_KEY = "YOUR_ROBOFLOW_API_KEY"
ROBOFLOW_PROJECT_NAME = "YOUR_ROBOFLOW_PROJECT_NAME"
GOOGLE_APPLICATION_CREDENTIALS = "path/to/your-service-account-file.json"
# ***********************************************

def get_gcs_signed_url(bucket_name: str, blob_name: str) -> str:
    """Generate a signed URL for a GCS object."""
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    
    url = blob.generate_signed_url(
        version="v4",
        expiration=3600,  # 1 hour in seconds
        method="GET"
    )
    return url

def get_gcs_objects(bucket_name: str) -> list:
    """Fetch the list of object keys in the given GCS bucket."""
    storage_client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()

    object_names = []
    for blob in blobs:
        object_names.append(blob.name)
    return object_names

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
    available_blobs = get_gcs_objects(GCS_BUCKET_NAME)
    
    # Optional: Filter the blobs here
    # e.g., available_blobs = [blob for blob in available_blobs if "some_condition"]
    
    # Upload blobs to Roboflow
    for blob in available_blobs:
        blob_url = get_gcs_signed_url(GCS_BUCKET_NAME, blob)
        upload_to_roboflow(ROBOFLOW_API_KEY, ROBOFLOW_PROJECT_NAME, blob_url)

```

### Option 2: Download Data Locally from GCP

To download data from GCP, first install the GCP CLI. Then, authenticate with your GCP user account.

To download an image or folder of images, use the following command:

```bash
gsutil cp -r gs://mybucket/folder .
```

Replace `mybucket` with the name of your GCP storage bucket and `folder` with the destination of the file or folder you want to copy. This command will save the target file or folder to your current working directory (`.`).

### Upload Data to Roboflow

Now that we have downloaded data, we can upload it to Roboflow either by using the [Upload Web Interface](https://docs.roboflow.com/datasets/adding-data/..#upload-data-with-the-web-interface) or the [Roboflow CLI](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/command-line-interface/upload-a-dataset).

### See Also

* [Retrieve a Roboflow project ID](https://docs.roboflow.com/api-reference/workspace-and-project-ids)
