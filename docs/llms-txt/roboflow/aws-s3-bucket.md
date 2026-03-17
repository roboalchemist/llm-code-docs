# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/adding-data/upload-data-from-aws-gcp-and-azure/aws-s3-bucket.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/adding-data/upload-data-from-aws-gcp-and-azure/aws-s3-bucket.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/adding-data/upload-data-from-aws-gcp-and-azure/aws-s3-bucket.md

# Source: https://docs.roboflow.com/datasets/adding-data/upload-data-from-aws-gcp-and-azure/aws-s3-bucket.md

# AWS S3 Bucket

When dealing with image data storage in AWS S3 and uploading to Roboflow, you generally have two options: using signed URLs or manually downloading images locally (via the AWS CLI) to upload them locally. The choice between these methods depends on your specific needs for data processing and management.

* **Signed URLs**: This method is particularly advantageous if you want to avoid the extra step and time consumption associated with downloading images to your local machine. With a signed URL, you can directly upload the image data from S3 to the Roboflow API without ever having to store it locally. This results in faster processing and less load on your local system.
* **CLI Locally**: There might be scenarios where you'd prefer to download the images to your local environment first. For instance, if you need to preprocess the images or manually check them before uploading to Roboflow, having local copies would be beneficial.

Selecting the right method will depend on your specific use-case requirements, like speed of data transfer, need for preprocessing, or manual inspection of images.

### AWS CLI Setup

Before using the script, ensure you've set up AWS CLI with the necessary authentication credentials. This will allow you to access and manage the desired S3 bucket.

* [Installing the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

#### Configuring the AWS CLI

1. Once you've installed the AWS CLI, open a terminal or command prompt.
2. Run the following command:

   ```bash
   aws configure
   ```
3. You'll be prompted to enter your AWS credentials:

   ```
   AWS Access Key ID [None]: YOUR_ACCESS_KEY
   AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
   Default region name [None]: YOUR_PREFERRED_REGION (e.g., us-west-1)
   Default output format [None]: json
   ```

### Option 1: Upload Via Signed URL:

You can generate signed URLs for your images in the S3 bucket by using boto3 in Python.

```python
def generate_presigned_url(bucket_name: str, object_name: str, region: str = 'us-east-2') -> str:
    """Generate a presigned URL for an S3 object."""
    s3 = boto3.client('s3', region_name=region, config=Config(signature_version='s3v4'))
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': bucket_name, 'Key': object_name},
                                    ExpiresIn=3600)
    return url
```

In the code snippet above, you need the name of your S3 bucket, the object name for the image in the S3 bucket, and the aws region. The signed URL of the image is generated and returned.

Building around this, we can generate a complete solution that pulls all the available objects in the S3 bucket, and then uploads them to Roboflow via the API. An outline for this solution can be seen below:

```python
import boto3
import requests
import urllib.parse
from botocore.config import Config

# ************* SET THESE VARIABLES *************
S3_BUCKET_NAME = "YOUR_S3_BUCKET_NAME"
ROBOFLOW_API_KEY = "YOUR_ROBOFLOW_API_KEY"
ROBOFLOW_PROJECT_NAME = "YOUR_ROBOFLOW_PROJECT_NAME"
# ***********************************************

def generate_presigned_url(bucket_name: str, object_name: str, region: str = 'us-east-2') -> str:
    """Generate a presigned URL for an S3 object."""
    s3 = boto3.client('s3', region_name=region, config=Config(signature_version='s3v4'))
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': bucket_name, 'Key': object_name},
                                    ExpiresIn=3600)
    return url

def get_s3_objects(bucket_name: str) -> list:
    """Fetch the list of object keys in the given S3 bucket."""
    s3 = boto3.client('s3')
    objects = []
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response['Contents']:
        objects.append(obj['Key'])
    return objects

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
    # Fetch list of available images
    available_images = get_s3_objects(S3_BUCKET_NAME)
    
    # Optional: Filter the images here
    # e.g., available_images = [img for img in available_images if "some_condition"]
    
    # Upload images to Roboflow
    for image in available_images:
        presigned_url = generate_presigned_url(S3_BUCKET_NAME, image)
        upload_to_roboflow(ROBOFLOW_API_KEY, ROBOFLOW_PROJECT_NAME, presigned_url)

```

### Option 2: Download Data Locally from AWS

To upload data from AWS, first install the `awscli` [command line tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). This tool allows you to interact with your AWS account on the command line. Once you have the command line tool installed, run the following command:

```bash
aws s3 sync s3://mybucket/folder_path .
```

Replace `mybucket` with the name of your bucket and `folder_path` with the name of the folder or file you want to export. This comamnd will download an asset from AWS to your current working directory (`.`).

### Upload Data to Roboflow

Now that we have downloaded data, we can upload it to Roboflow either by using the [Upload Web Interface](https://docs.roboflow.com/datasets/adding-data/..#upload-data-with-the-web-interface) or the [Roboflow CLI](https://app.gitbook.com/s/e5GEiPeDoFksvZv1vH3A/command-line-interface/upload-a-dataset).

### See Also

* [Retrieve a Roboflow project ID](https://docs.roboflow.com/api-reference/workspace-and-project-ids)
