# Source: https://docs.socket.dev/docs/socket-python-sdk.md

# Socket Python SDK

# Getting Started with the Socket Python SDK

## Introduction

The Socket Python SDK provides a convenient way to interact with the Socket.dev REST API using Python. This guide will help you get started with the SDK, covering installation, initialization, and usage of various functions.

For more detailed information and to view the source code, visit the [Socket Python SDK GitHub project](https://github.com/SocketDev/socket-sdk-python).

## Prerequisites

Before you begin, ensure you have the following:

* Python 3.6 or higher
* An API token from Socket.dev

## Installation

To install the Socket Python SDK, clone the GitHub repo:

```bash
git clone https://github.com/SocketDev/socket-sdk-python.git
```

## Initializing the SDK

To start using the SDK, initialize it with your API token:

```python
from socketdev import SocketDev

# Replace 'YOUR_API_KEY' with your actual API token
socket = SocketDev("YOUR_API_KEY")
```

## Usage Examples

### Fetching Issues for a Package

You can retrieve issues associated with a specific NPM package and version:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
issues = socket.npm.issues("hardhat-gas-report", "1.1.25")
print(issues)
```

### Fetching Score for a Package

To fetch the score of a specific NPM package and version:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
score = socket.npm.score("hardhat-gas-report", "1.1.25")
print(score)
```

### Retrieving Dependencies

To get the dependencies for the organization associated with your API token:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
dependencies = socket.dependencies.get(10, 0)
print(dependencies)
```

### Posting Dependencies

To post dependencies for the organization:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
file_names = ["path/to/package.json"]
params = {
    "repository": "username/repo-name",
    "branch": "dependency-branch"
}
response = socket.dependencies.post(file_names, params)
print(response)
```

### Getting Organization Information

Retrieve the organization information from Socket.dev:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
org_info = socket.org.get()
print(org_info)
```

### Checking Quota

To check the current quota available for your API token:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
quota = socket.quota.get()
print(quota)
```

### Managing Reports

#### Listing Reports

Retrieve the list of all reports for your organization:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
reports = socket.report.list()
print(reports)
```

#### Deleting a Report

Delete a specified report:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
response = socket.report.delete("report-id")
print(response)
```

#### Viewing a Report

Retrieve information for a specific Project Health Report:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
report = socket.report.view("report_id")
print(report)
```

#### Creating a Report

Create a new project health report with the provided files:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
files = ["/path/to/manifest/package.json"]
response = socket.report.create(files)
print(response)
```

### Managing Repositories

Retrieve information about the tracked repositories:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
repositories = socket.repositories.get()
print(repositories)
```

### Retrieving Organization Settings

Get the organization settings from Socket.dev:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
settings = socket.settings.get()
print(settings)
```

### Working with SBOM

Retrieve information for an SBOM report:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
sbom_report = socket.sbom.view("report_id")
print(sbom_report)
```

### Using PURL Post

Retrieve package information for a PURL post:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
license = "true"
components = [
    {"purl": "pkg:pypi/pyonepassword@5.0.0"},
    {"purl": "pkg:pypi/socketsecurity"}
]
response = socket.purl.post(license, components)
print(response)
```

### Managing Full Scans

#### Retrieving Full Scans

Retrieve full scans information for an organization:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
fullscans = socket.fullscans.get("org_slug")
print(fullscans)
```

#### Creating a Full Scan

Create a full scan from a set of package manifest files:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
files = ["/path/to/manifest/package.json"]
params = {
    "org_slug": "org_name",
    "repo": "TestRepo",
    "branch": "main",
    "commit_message": "Test Commit Message",
    "commit_hash": "",
    "pull_request": "",
    "committers": "commiter",
    "make_default_branch": False,
    "set_as_pending_head": False,
    "tmp": ""
}
response = socket.fullscans.post(files, params)
print(response)
```

#### Deleting a Full Scan

Delete an existing full scan:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
response = socket.fullscans.delete("org_slug", "full_scan_id")
print(response)
```

#### Streaming SBOM Artifacts

Stream all SBOM artifacts for a full scan:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
stream = socket.fullscans.stream("org_slug", "full_scan_id")
print(stream)
```

#### Getting Full Scan Metadata

Retrieve metadata for a single full scan:

```python
from socketdev import SocketDev

socket = SocketDev("YOUR_API_KEY")
metadata = socket.fullscans.metadata("org_slug", "full_scan_id")
print(metadata)
```

## Conclusion

This guide provides an overview of how to get started with the Socket Python SDK. For more detailed information and updates, refer to the [Socket Python SDK GitHub project](https://github.com/SocketDev/socket-sdk-python). Happy coding!