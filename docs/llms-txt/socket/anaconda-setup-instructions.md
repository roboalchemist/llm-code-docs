# Source: https://docs.socket.dev/docs/anaconda-setup-instructions.md

# Anaconda setup instructions

Generating a `requirements.txt` from a Conda Environment for Socket Scanning

## Overview

Socket supports scanning dependencies from a `requirements.txt` file to detect potential security risks in your project. If you're using Conda, you can generate a `requirements.txt` file from your environment and scan it using any of the Socket scanning methods:

* **API**: Upload the file for analysis.
* **CLI**: Scan the file directly from your local environment.
* **GitHub Integration**: Commit the file to your repository and let Socket for GitHub automatically scan it.

This guide walks you through generating a `requirements.txt` file from a Conda environment that Socket can analyze.

## Step 1: Activate Your Conda Environment

Before exporting dependencies, ensure you have the correct Conda environment activated. If you're unsure how to activate an environment, refer to \[How to Activate an Environment with Conda].

Run the following command, replacing `<env_name>` with the name of your environment:

```sh
conda activate <env_name>
```

## Step 2: Generate requirements.txt

Once the environment is active, list the installed packages and export them to a requirements.txt file:

```sh
conda list -e > requirements.txt
```

This will create a requirements.txt file containing all installed packages and their versions.

Example requirements.txt Output

```txt
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: linux-64

ca-certificates=2020.1.1=0
certifi=2020.4.5.1=py38_0
openssl=1.1.1f=h7b6447c_0
pip=20.0.2=py38_1
setuptools=46.1.3=py38_0
wheel=0.34.2=py38_0
```

## Step 3: Scan requirements.txt with Socket

### Option 1: Scan via Socket CLI

If you have the Socket CLI installed, you can scan the generated requirements.txt file with:

```sh
socket scan requirements.txt
```

### Option 2: Scan via Socket API

You can upload requirements.txt to Socket’s API for analysis. Refer to \[Socket API Documentation] for details on how to send the file.

### Option 3: Commit and Let Socket for GitHub Scan It

If you use Socket for GitHub, simply commit the `requirements.txt` file to your repository. Socket will automatically scan it for vulnerabilities and supply chain risks.

Additional Notes

* Conda’s `requirements.txt` format includes additional metadata (e.g., platform information and package builds). Socket scans focus on package names and versions relevant to security analysis.
* If your project uses both Conda and PyPI packages, consider using `pip freeze > requirements.txt` in a Conda environment with pip installed to generate a format that better matches PyPI expectations.

For more details on scanning methods, visit the rest of our docs pages (see sidebar).

## Note

Socket scans artifacts published to PyPI, with Anaconda Cloud support planned on Socket’s roadmap. Socket supports the PyPI registry and therefore we can report risks for any Anaconda package which is also published to PyPI. Since Anaconda packages are built from the same source as PyPI packages, most supply chain risks, vulnerabilities, quality, license, and maintenance issues can still be detected—but some supply chain threats may only be identified once Anaconda artifact scanning is supported. Socket supports the PyPI registry and therefore we can report risks for any Anaconda package which is also published to PyPI.