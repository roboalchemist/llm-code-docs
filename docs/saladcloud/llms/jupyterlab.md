# Source: https://docs.salad.com/container-engine/tutorials/machine-learning/jupyterlab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run JupyterLab

*Last Updated: February 28, 2025*

By running JupyterLab over SaladCloud, college students and professionals in the AI and Data Science industry can access
the world’s most affordable GPU-accelerated platform to learn CUDA and PyTorch/TensorFlow programming, as well as to
test and research various AI models for training, fine-tuning and inference. This not only contributes to cost reduction
by eliminating the need to purchase expensive hardware but also saves time and effort associated with building dedicated
development environments. Additionally, it fosters collaboration by providing a platform for sharing insights and
collaborating with peers.

SaladCloud offers several pre-built JupyterLab container images in Docker Hub, designed to fulfill general requirements.
You have the option to run these images directly on SaladCloud for your AI/ML tasks. Alternatively, you can customize
them to meet specific needs by utilizing the Dockerfile templates available on our GitHub repository.

[Docker Hub repository](https://hub.docker.com/r/saladtechnologies/jupyterlab)

[GitHub repository](https://github.com/SaladTechnologies/jupyterlab)

| Container Image                                                         | Features                                                                                                                                                                                       |
| :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| saladtechnologies/jupyterlab:1.0.0-pytorch-tensorflow-cpu-aws-azure-gcp | JupyterLab; Hugging Face transformers and datasets; AutoAWQ 0.1.6; PyTorch 2.1 GPU; Python 3.10; CUDA 11.8 and cuDNN 8.7; Integration with AWS S3, Azure Storage Account and GCP Cloud Storage |
| saladtechnologies/jupyterlab:1.0.0-pytorch-gpu-aws-azure-gcp            | JupyterLab; Hugging Face transformers and datasets; TensorFlow 2.13 GPU; Python 3.8; CUDA 11.2 (NVCC) and cuDNN 8.1; Integration with AWS S3, Azure Storage Account and GCP Cloud Storage      |
| saladtechnologies/jupyterlab:1.0.0-tensorflow-gpu-aws-azure-gcp         | JupyterLab; Hugging Face transformers and datasets; PyTorch 2.1 CPU; TensorFlow 2.15 CPU; Python 3.10; Integration with AWS S3, Azure Storage Account and GCP Cloud Storage                    |

# The construction of the JupyterLab container images

SaladCloud is designed to execute stateless container workloads. To ensure data persistence while using JupyterLab, we
leverage storage services from public cloud platforms. The integration with major public cloud platforms, such as AWS,
Azure, and GCP, is already implemented into the pre-built JupyterLab container images. Initial setup involves
provisioning cloud storage in the chosen cloud platform, followed by using environment variables to pass the storage
resource name and its access credentials to the container during launch.

We create a folder named 'data' within the /root directory of the container, acting as the current working directory
that needs the data persistence. During the initial launch of the instance, a script file named ‘start.sh’ is executed,
and all data is synchronized from the chosen cloud platform to the /root/data directory by use of Cloud-specific CLIs,
the storage resource name and access credentials. Following this, the script continuously monitors the /root/data
directory, and any changes (create, delete or modify) in this directory or its subfolders trigger the synchronization
back to the cloud.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ea126b6e6286a8ef2abdfceef453f418" data-og-width="743" width="743" data-og-height="542" height="542" data-path="container-engine/images/bfebac8-tech_doc_1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d35b213c6059713cee0654479e581842 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f7ec8618d446a3aab2feeef27796cd70 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e6dacd01a6d5cf62cfd3fc3735dc3814 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=99dd491a94af229a3e963d279bfb9150 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f60687c7807bac0ebb9c80a39d835a0e 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bfebac8-tech_doc_1.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e9bafa7f5eb3eb329ee3beb925270557 2500w" />

Under the hood, we employ the inotifywait command-line tool that uses the inotify Linux kernel subsystem to watch for
changes in the /root/data directory. Every time files are manually saved through the JupyterLab menu, or automatically
saved by the JupyterLab’s autosave feature, the inotifywait command captures events such as create, delete or modify.
Subsequently, the script triggers synchronization. All three public cloud platforms offer sync commands that can make
the contents under the source the same as the content under the destination by calculating and copying only the
differences instead of duplicating the entire directory. This integrated solution is highly effective, minimizing API
calls to the cloud and reducing data transfer to the cloud to the minimum.

Models and datasets that are dynamically downloaded from Hugging Face or TensorFlow Hub are stored in the /root/.cache
or /root/.keras hidden folders; and these data will be not synchronized to the cloud platform unless they are explicitly
saved into the /root/data directory. Given that cloud storage typically incurs a charge of around \$0.02 per GB Month
(similar across all three cloud providers), the associated cost would be negligible if we mainly utilize the cloud
storage for storing code.

For utilizing the pre-built JupyterLab container images, specific environment variables are required to pass information
to containers. The Cloud-related environment variables can be omitted if data persistence is not required.

| Environment Variable                                                          | Description                                                                             |
| :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| JUPYTERLAB\_PW                                                                | Define the password for JupyterLab. Can be omitted, and the default password is ‘data’. |
| AWS\_S3\_BUCKET\_FOLDER; AWS\_ACCESS\_KEY\_ID; AWS\_SECRET\_ACCESS\_KEY       | Provide the AWS-related info to access a folder within an AWS S3 bucket.                |
| AZURE\_CONTAINER\_URL; AZURE\_BLOB\_SAS\_TOKEN                                | Provide the Azure-related info to access a container within an Azure storage account.   |
| GOOGLE\_BUCKET\_FOLDER; GOOGLE\_APPLICATION\_CREDENTIALS; GOOGLE\_PROJECT\_ID | Provide the GCP-related info to access a folder within a GCP Cloud Storage bucket.      |

For the Dockerfile templates and the start.sh script file, please refer to our GitHub repository.

All major public cloud platforms, such as AWS, Azure, and GCP, offer the object storage service suitable for preserving
data for the JupyterLab containers. The integration methods with the three cloud platforms are similar: provision the
storage resource, obtain its access credentials, and then pass this information to launch a container.

If you are a business customer, such as a college, offering the JupyterLab service to numerous users, and each user
requires exclusive access their own data, we recommend AWS. It provides a straightforward and simple implementation that
allows multiple users to access their individual folders named with their usernames within the same bucket. In the event
that a user's access credentials are compromised, the impact is confined to that specific user, safeguarding others from
any potential consequences.

For individual customers, there is little significant difference among the three cloud platforms, and you can choose the
cloud provider based on your preference.

# Provision the cloud storage in AWS

### Step 1: Create an AWS S3 bucket and a folder inside the S3 bucket

Log into the AWS Console, and create an AWS S3 bucket ('rxjupyterlab') with the default settings in one of the AWS
Regions, and create a folder named with an AWS IAM username ('user1') within the S3 bucket. This folder will be
synchronized with the /root/data directory inside a JupyterLab container running on SaladCloud. If an organization is
providing the JupyterLab service for numerous users and aims to ensure exclusive access to their own data, creating one
folder per user within the same bucket is a recommended approach in AWS.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a1db4c93498e33b63f192e646a0960e5" data-og-width="751" width="751" data-og-height="551" height="551" data-path="container-engine/images/2009ed8-tech_doc_2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6ad83a18c0495bf55dab0fe42c570b0e 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=96c0b7d439637a7965bff7995eb5913f 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3d66d591903239f0abfb53eac234f8fd 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=221683b83807048de15680beb0b1356e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=88dad7056badab9bb7e30aafa7f26cbf 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2009ed8-tech_doc_2.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fcbd9c63bd2c2f4930884ec041f00668 2500w" />

### Step 2: Create an AWS IAM policy for exclusive access

Create an AWS IAM policy ('access\_its\_own\_folder') using the provided JSON file. This policy will be attached to AWS IAM
users, ensuring that each user can exclusively access their own folder in the same S3 bucket.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=14bcbd8dcac30cb0201984ec083cffe1" data-og-width="758" width="758" data-og-height="335" height="335" data-path="container-engine/images/0e960c6-tech_doc_3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6843cb119802ce46d064a281d94c9eb4 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a6e5242ddd817a506e30ef887f6cc08d 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3ae66f9ef62a7b1eaf4017d75a6fd215 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5194be2e1240f3d0dbec68e995225f8e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0858ecd6f52e6a57e5203dcbfbfbb184 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/0e960c6-tech_doc_3.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2db20c9257a895494b5710c515a1da4a 2500w" />

Replace 'rxjupyterlab' with your AWS S3 bucket name in the JSON file:

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::rxjupyterlab/${aws:username}/*"
    },
    {
      "Sid": "AllowListBucketOfASpecificUserPrefix",
      "Action": "s3:ListBucket",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::rxjupyterlab",
      "Condition": {
        "StringLike": {
          "s3:prefix": ["${aws:username}/*"]
        }
      }
    }
  ]
}
```

### Step 3: Create an AWS IAM user and generate its credentials

Create an AWS IAM user ('user1') without the AWS Console access and attach the customer-managed AWS IAM policy
('access\_its\_own\_folder') to the user.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=fa65aee1c2b2f72515f9519500aa7374" data-og-width="770" width="770" data-og-height="359" height="359" data-path="container-engine/images/e1b930e-tech_doc_4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2a5aacba8de4ec3b4a33aefb3aa88296 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f55943bd0e949cf53f3b64167f0436d6 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=64f5cd3ac6ae49bcf4b5fc593d6c8c20 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=83f29457b2941ccdf5fb26c5a0848e85 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=102b2f263dbc8d8cfe3223d9d39d0c6e 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e1b930e-tech_doc_4.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=d11541cb6f861beb604c74afed7e0bc9 2500w" />

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=27d97f7f35b5a374ed935b9ba7cdb460" data-og-width="792" width="792" data-og-height="460" height="460" data-path="container-engine/images/07a9f96-tech_doc_5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=259e8b8bce2b7d6b84550e863dcb7f8f 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=ee761d831297ca07666e22d0597b94da 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6f55ab1720cd39be7e798c62655eab1c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=64a72ad7406564d2ae446fb2a93d0eb8 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3211c0565baa9a0822d8397fd65637e1 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07a9f96-tech_doc_5.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=ff0221a9b7ad0f08a2a1754435df72e7 2500w" />

Generate the access key ID/secret access key for the AWS IAM user ('user1'). Copy and securely keep the credentials in a
safe location.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a138919870db0f57fcacb62b5ac5979a" data-og-width="924" width="924" data-og-height="514" height="514" data-path="container-engine/images/3c0975e-tech_doc_6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=14b772edf303fc10c186965c6bd70afc 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=27f606793eea83859e55c16d5876bb08 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=ea71c9303c3f617ba9d6e2a05937f6b2 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6b139295f01f992af817e7d3cf4a174f 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1dd82d2784184b8942bf1fec2bc89256 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3c0975e-tech_doc_6.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=781d6d30a37eb45e389ddd0c1906476a 2500w" />

When running the JupyterLab containers on SaladCloud with AWS as the backend cloud storage, three AWS-related
environment variables are utilized to pass the access key ID/access key secret, as well as the bucket and folder name to
the container.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=66e053ba5756c3d230798e9b0616a2bc" data-og-width="401" width="401" data-og-height="424" height="424" data-path="container-engine/images/1c7bad0-tech_doc_7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=73900f216d6421fdf900bf6c96f4ee7c 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b9aacc867951d5e3c24383387e8c6759 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=326e17b262861369c8a506a575890af2 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=412d0bd7aa93ff0883e503545180553a 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=540fe2bebf8c678ce3d489e037923b8a 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1c7bad0-tech_doc_7.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=650cfc964bf11cb6cf4ae839b8b8f3a4 2500w" />

# Provision the cloud storage in Azure

### Step 1: Create an Azure storage account and a container inside the storage account

Log into the Azure Console, and create an Azure Storage Account ('rxjupyterdata') with the default settings in one of
the Azure Regions, and create a container ('data') within the storage account. This container will be synchronized with
the /root/data directory inside a JupyterLab container running on SaladCloud. If an organization is providing the
JupyterLab service for numerous users and aims to ensure exclusive access to their own data, creating one container per
user within the same storage account is a recommended approach in Azure.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=57cf38e395e26af65aed7d24f24d9439" data-og-width="826" width="826" data-og-height="416" height="416" data-path="container-engine/images/4e89d2d-tech_doc_8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0d6fe5174bd9dda6df49c73c0d315b60 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cfb63a8665d66f3ddbe2a5e70ce9ae86 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=46021c9b301187a9c4d789900779ba3c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4f987353c6360c858776235bbc15e7ed 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e970ae3f07fb0c5d2df60012bf2dabbb 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4e89d2d-tech_doc_8.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=96e2479588173a09c1e5dedb68a995c4 2500w" />

Navigate to the “Properties” menu on the left panel, and copy the container URL.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fe7bddbe578a4de9676d035cec38be38" data-og-width="826" width="826" data-og-height="396" height="396" data-path="container-engine/images/9042ffc-tech_doc_9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d855fe063b81062a767ee51b9151c649 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=40a456a518fe624ac1091eb5fa2de35c 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=55f0b728346d4f7eeaf1ae46f4b52461 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=54f6a1961e098169b29fe1ada0ab6abf 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=6bb8147d357aef16b00f0ccf924f5df8 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/9042ffc-tech_doc_9.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=90aaa6a1e556ffd8780946840ccd00fe 2500w" />

### Step 2: Create an access policy and a shared access token for the Azure storage account container

For the access policy, you can define the start time, expiry time and permissions; all the 6 permissions are necessary
for the data persistence of JupyterLab containers.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6844886eb49fd3317623d4f44c4deaef" data-og-width="826" width="826" data-og-height="468" height="468" data-path="container-engine/images/07728a3-tech_doc_10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3b74f7d18016d566075800438479dc2f 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c83f50b9ee5bb26eca314b5054d8731b 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=62ba43cb9b4b37a70f6d464ab39c3a7e 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=73218904ba02d786e9e4f5831333b9be 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=508ce0bb75a3259994cee978aa3114d9 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/07728a3-tech_doc_10.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6758b3651053189510bf73d859e42ef7 2500w" />

After creating the access policy for the Azure storage account container, generate the shared access token. Copy and
securely keep the Blob SAS token in a safe location.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3bd78ce92297d018b1e1d98ed94fb68d" data-og-width="808" width="808" data-og-height="750" height="750" data-path="container-engine/images/3afd7e5-tech_doc_11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fd49922976c6661fd491643b61bc749f 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c2ce8b89192e680a9cada393f9688fb3 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=832d248ee6a17b02cb4d108208bbe4b4 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e369759c637dfaa6b05f8ede36760e7a 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fe7bcb1bb40aa179ab6797bda3c12c94 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3afd7e5-tech_doc_11.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=8115a3be4d29a11323b239200cca4364 2500w" />

When running the JupyterLab containers on SaladCloud with Azure as the backend cloud storage, two Azure-related
environment variables are utilized to pass the container URL and Blob SAS token to the container.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a9812577a323bd8680439feca9537a6d" data-og-width="440" width="440" data-og-height="368" height="368" data-path="container-engine/images/207b332-tech_doc_12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=16d84748fb8e1fb774ece12f82bac9a8 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d01fdec4bbc5a902aa89a1204a107dfc 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4d5407d5ef9022105ec1faaad5bfde91 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=20811828d2003e226ed7e7d2151b729c 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b67917a6a6ed86eca55d8f7b4d048bed 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/207b332-tech_doc_12.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3b877244408dcb2c2a4a2d9cdb3c83e9 2500w" />

# Provision the cloud storage in GCP

### Step 1: Create a GCP cloud storage bucket and a folder in the bucket

Log into the GCP Console, and create a GCP Cloud Storage bucket ('rxjupyterlab') with the default settings in one of the
GCP Regions, and create a folder ('sa1') within the bucket. This folder will be synchronized with the /root/data
directory inside a JupyterLab container running on SaladCloud. If an organization is providing the JupyterLab service
for numerous users and aims to ensure exclusive access to their own data, creating one bucket per user is a recommended
approach in GCP.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=42199f52781d82dc12874df1345fab5a" data-og-width="842" width="842" data-og-height="428" height="428" data-path="container-engine/images/f2c9a5d-tech_doc_13.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=898f08e4d910d10d583a9dcbb8dc253c 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=36737c11bbfdb07fba108c2d080db0c5 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=0d3e0a47516ecf24306b34f70efea03d 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=7e8d3e0f51f455ccd8ade512a9b3aaf9 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=1a7c7e77c5843e7dfdb19fd51a200743 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f2c9a5d-tech_doc_13.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=7522e7d3ec6575107acc79c45931a926 2500w" />

### Step 2: Create a service account and generate its credentials

Create a service account (‘sa1’) without permissions, and add a key for the service account. Download the key’s JSON
file and securely keep it in a safe location.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=6e2215ac466b5f2d19d6a26ef7770c2a" data-og-width="842" width="842" data-og-height="410" height="410" data-path="container-engine/images/c089355-tech_doc_14.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=95dabba00d6996589ef3ee803530b39c 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f62b38f7d42f75d7f7d724916a9deae6 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=de281d400bf1914b0c6d6b624e4bd833 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=950886aca08e355b07c2ae5f9da26f6f 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=871a5ddd06588f75309c65db878f915e 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/c089355-tech_doc_14.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=143c6f4142d10334f2636e4a931eb208 2500w" />

### Step 3: Grant access to the bucket for the service account

Navigate to the “rxjupyterlab” bucket again and grant the “Storage Admin” role to the sa1 service account. Unlike AWS,
GCP does not provide an easy way to grant access only to a specific folder inside the bucket. With the above role
assignment, the sa1 service account will have access to the entire bucket.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=80a1a46bce8f209dfb65f93898217019" data-og-width="878" width="878" data-og-height="549" height="549" data-path="container-engine/images/95b3117-tech_doc_15.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=df226d86282d022fde89539b45d91e45 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=0d17897ff1c7d646f6baf1335e801833 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fcee943b3ba59f01ea792fc181658083 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=35f508a5d183d947f981e479f6f1e3c1 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=04d829c2984e1bef4188867cbfbbf1b5 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/95b3117-tech_doc_15.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=8a69c765e5ba7e6de639443057070475 2500w" />

When running the JupyterLab containers on SaladCloud with GCP as the backend cloud storage, three GCP-related
environment variables are utilized to pass the credentials (content of the downloaded JSON file), the bucket and folder
name, and project ID to the container.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d83664a5ee54a310f1483361953910ff" data-og-width="440" width="440" data-og-height="383" height="383" data-path="container-engine/images/7cdc53a-tech_doc_16.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c43bf7dafcc27979f1bb455fecd1b564 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=44509c157a384a5b609ebc201b2ed8c4 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=8cc891d9678a31199a95c8e332a8564d 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d0f5c7d50cebb6d85c0bee834bb6f27a 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5e39291451d8db2b112356399bf562a5 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7cdc53a-tech_doc_16.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=523dd785110e7b8d502b322c5e552676 2500w" />

# Run JupyterLab over SaladCloud

To run a JupyterLab instance on SaladCloud, you can log in the SaladCloud Console and deploy the JupyterLab instance by
selecting 'Deploy a Container Group' with the following parameters:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6d817388087ee4e9be90ce97ceaa1664" data-og-width="2276" width="2276" data-og-height="1032" height="1032" data-path="container-engine/images/13b07e0-tech_doc_17-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d6a77869845dd8540957730303d5ac9a 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f9f75bfd0333335d3237362bff3bea8b 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=60f3a3b65285342cb2c3dc9492b02054 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0e0ee333dbe8aa2a36f7c4f4ab85c4a4 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=79aac6cf7528b20c020a88d0bb2e4b46 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/13b07e0-tech_doc_17-1.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=68276e0fb29653d57877a9c0a6b86e29 2500w" />

| Parameter             | Value                                                                                                                                                                                                                                                                                                                    |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Container Group Name  | jupyterlab001, or any name you prefer.                                                                                                                                                                                                                                                                                   |
| Image Source          | saladtechnologies/jupyterlab:1.0.0-pytorch-tensorflow-cpu-aws-azure-gcp, or your tailored JupyterLab image.                                                                                                                                                                                                              |
| Replica Count         | 1, can only be 1.                                                                                                                                                                                                                                                                                                        |
| vCPU                  | 2, based on the task need.                                                                                                                                                                                                                                                                                               |
| Memory                | 4, Based on the task need.                                                                                                                                                                                                                                                                                               |
| GPU                   | RTX 1650 (4 GB), RTX 2080 (8 GB), RTX 3060 (12 GB) or others. You can choose multiple GPU types simultaneously, and SaladCloud will then select a node that matches one of the selected types.                                                                                                                           |
| Container Gateway     | Enable, Port:8000, Use Authentication: No; and **make sure the option "Limit each server to a single,active connection" is not selected.**                                                                                                                                                                               |
| Environment Variables | Provide the corresponding environment variables based on your needs. JupyterLab Password:JUPYTERLAB\_PW; AWS:AWS\_ACCESS\_KEY\_ID,AWS\_SECRET\_ACCESS\_KEY,AWS\_S3\_BUCKET\_FOLDER; Azure:AZURE\_CONTAINER\_URL,AZURE\_BLOB\_SAS\_TOKEN; GCP:GOOGLE\_APPLICATION\_CREDENTIALS,GOOGLE\_BUCKET\_FOLDER,GOOGLE\_PROJECT\_ID |

SaladCloud would take a few minutes to download the image to the selected node and run the container. Using the Console,
you can determine whether the JupyterLab instance is ready to use.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=fe8cd4b44f483d8962f568823d8934a5" data-og-width="749" width="749" data-og-height="459" height="459" data-path="container-engine/images/e657944-tech_doc_18.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=e88c2748fadc520c51d5c5bead7a44ed 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=59248b2b04f23c54d752842134f701d9 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b2d0c4bda5993eba3925c37afdf77679 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6f5821124ecbc6ce5166776282e66ec2 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2542747c54006eafd8c67eb10fcf8a85 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e657944-tech_doc_18.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=c6c30c2b3179958e70fd5729890e9b94 2500w" />

After the instance is running, you can type the generated Access Domain Name in the browser’s address bar, enter the
password provided by the JUPYTERLAB\_PW environment variable, and begin using the JupyterLab service.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fd88f9a33d36310303b07b0cd69c473d" data-og-width="754" width="754" data-og-height="322" height="322" data-path="container-engine/images/4b5c193-tech_doc_19.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=03015c1e6d5492eaeda8504edd54965f 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9819713cc237e609f00c53a186ff986d 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=413f9194283489c457cd555a307e3f01 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=70b329a9be4c8e273b293f7386281277 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0aa5c4100dc5c34911467e1da9e9b9b2 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4b5c193-tech_doc_19.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=880d29914d47eb5d33e3c99b1554b1fc 2500w" />

Now you can write Python code to learn, test, fine-tune or train the popular AI models from Hugging Face. In case any
libraries or dependencies are missing, you can install them online in the notebook or terminal. You may also build your
own container images to include specific libraries and dependencies based on the provided Dockerfile templates.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a8b519c2d4b3150d27b1c451789621a1" data-og-width="817" width="817" data-og-height="737" height="737" data-path="container-engine/images/a0383df-tech_doc_20.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=3550deeb1c5119d9721715e59a9112b8 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=140d0e29fc455d7cf45306d8230c7e14 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=40e6d90e5c0cde52f6a8323b09b5674c 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fcfbc2a79bd1a85959a84cc68a3ceeea 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=509b51325d6afc9e398634c532035e45 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a0383df-tech_doc_20.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=1e754bc9b0d88e096efa7d3defeca496 2500w" />

In the JupyterLab terminal, you have the flexibility to use SH and BASH, and switch between them. Additionally, you can
engage in C/C++ and CUDA programming by utilizing gcc and nvcc.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=49f0e3b9a93c25c91ef45ec311a30fac" data-og-width="863" width="863" data-og-height="731" height="731" data-path="container-engine/images/6599a2b-tech_doc_21.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=60392d75e675d5369aff0f2026de4c91 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2e87d3072b52a7f5df5c9b399661ee76 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=71f06a2969f3f513136058db0378b1ce 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=88c07434aa1e80eed56c7ab6b7115bb9 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=520f8418e01e82a6c4039cd98f3776b4 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6599a2b-tech_doc_21.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cfde7030bc408e7c22ebcd850c1fcad7 2500w" />

By sharing access to the JupyterLab instance, a team can collaborate on editing the same notebook or using the same
terminal from different locations. Regarding the the JupyterLab terminal, any modifications made by one team member in
the terminal will promptly reflect in another member’s browser and vice versa, similar to the screen sharing on WebEx or
Zoom.
