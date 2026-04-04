# Source: https://docs.anyscale.com/dependency-management/private-git-image-example.md

# Run code from a private Git repo on Anyscale

[View Markdown](/dependency-management/private-git-image-example.md)

# Run code from a private Git repo on Anyscale

This page provides the steps to run code from a private Git repository on Anyscale using a custom image.

The following table provides an overview of the features used in this pattern and provides a link back to documentation for each feature.

| Feature         | Link                                                                          |
| --------------- | ----------------------------------------------------------------------------- |
| Init scripts    | [Use init scripts with custom images](/dependency-management/init-scripts.md) |
| Secrets manager | [Secret management on Anyscale](/secrets.md)                                  |
| Custom images   | [Custom images on Anyscale](/container-image/custom-image.md)                 |

## Build an Anyscale container image from a private Git repo[​](#build-from-git "Direct link to Build an Anyscale container image from a private Git repo")

* AWS
* Google Cloud

To retrieve a [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) stored in Amazon Secrets Manager and clone a private GitHub repository, follow these steps:

1. Create a personal access token in GitHub with permissions to access your private repository.

2. Create a `github_clone.sh` script like the one below:

   ```
   #/bin/bash

   # Prereqs: awscli, jq
   # Env variables required: ANYSCALE_WORKING_DIR, SECRET_NAME, PRIVATE_REPO_NAME, AWS_DEFAULT_REGION

   # Create and navigate to the working directory.
   mkdir -p $ANYSCALE_WORKING_DIR
   cd $ANYSCALE_WORKING_DIR

   # Retrieve and extract the GitHub token from AWS Secrets Manager.
   SECRET_VALUE=$(aws secretsmanager get-secret-value --secret-id ${SECRET_NAME} | jq -r .SecretString)
   GITHUB_TOKEN=$(echo ${SECRET_VALUE} | jq -r .github_token)

   # Clone the private repository.
   git clone https://${GITHUB_TOKEN}@github.com/${PRIVATE_REPO_NAME}
   ```

3. Build a container image hosted in ECR. Below is an example `Dockerfile`:

   ```
   # Use Anyscale base image.
   FROM anyscale/ray:2.30.0-slim-py310

   # Create the init directory.
   RUN sudo mkdir -p /anyscale/init

   # Install necessary packages.
   RUN sudo apt-get update && sudo apt-get install -y axel nfs-common zip unzip && sudo apt-get clean
   RUN sudo apt-get install -y jq git curl && sudo apt-get clean

   # Install AWS CLI v2.
   RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   RUN unzip awscliv2.zip && sudo ./aws/install

   # Install Python dependencies.
   RUN pip install --no-cache-dir -U sympy anyscale

   # Add the GitHub clone init script to the Anyscale init directory.
   ADD ./github_clone.sh /anyscale/init/github_clone.sh
   RUN sudo chmod +x /anyscale/init/github_clone.sh

   # (Optional) Verify base image dependencies.
   RUN echo "Testing Ray Import..." && python -c "import ray"
   RUN ray --version
   RUN jupyter --version
   RUN anyscale --version
   RUN sudo supervisord --version
   RUN aws --version
   ```

4. Once you've built the image, you can use it on Anyscale. See [Use container images from an external registry](/container-image/image-registry.md).

To retrieve a [GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) stored in Google Secret Manager and clone a private GitHub repository into the working directory, follow these steps:

1. Create a personal access token in GitHub with permissions to access your private repository.

2. Create a `github_clone.sh` script like the one below:

   ```
   #/bin/bash

   # Prereqs: gcloud, jq
   # Env variables required: ANYSCALE_WORKING_DIR, SECRET_NAME, PRIVATE_REPO_NAME

   # Create and navigate to the working directory.
   mkdir -p $ANYSCALE_WORKING_DIR
   cd $ANYSCALE_WORKING_DIR

   # Retrieve and extract the GitHub token from Google Secrets Manager.
   SECRET_VALUE=$(gcloud secrets versions access latest --secret=$SECRET_NAME)
   GITHUB_TOKEN=$(echo ${SECRET_VALUE} | jq -r .github_token)

   # Clone the repo.
   git clone https://${GITHUB_TOKEN}@github.com/${PRIVATE_REPO_NAME}
   ```

3. Build a container image hosted in Google Artifact Registry. Below is an example `Dockerfile`:

   ```
   # Use Anyscale base image.
   FROM anyscale/ray:2.30.0-slim-py310

   # Create the init directory.
   RUN sudo mkdir -p /anyscale/init

   # Install necessary packages.
   RUN sudo apt-get update && sudo apt-get install -y axel nfs-common zip unzip jq git curl && sudo apt-get clean

   # Install Google Cloud SDK for accessing Google Cloud services.
   RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
   RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
   RUN sudo apt-get update && sudo apt-get install -y google-cloud-sdk

   # Install Python dependencies.
   RUN pip install --no-cache-dir -U sympy anyscale

   # Add the GitHub clone init script to the Anyscale init directory.
   ADD ./github_clone.sh /anyscale/init/github_clone.sh
   RUN sudo chmod +x /anyscale/init/github_clone.sh

   # (Optional) Verify base image dependencies
   RUN echo "Testing Ray Import..." && python -c "import ray"
   RUN ray --version
   RUN jupyter --version
   RUN anyscale --version
   RUN sudo supervisord --version
   RUN gcloud --version
   ```

4. Once you've built the image, you can use it on Anyscale. See [Use container images from an external registry](/container-image/image-registry.md).
