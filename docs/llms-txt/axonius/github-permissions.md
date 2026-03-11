# Source: https://docs.axonius.com/docs/github-permissions.md

# GitHub Permissions

The permissions required to successfully connect the GitHub adapter depend on the authentication method you use. In addition, some permissions are required only for fetching specific asset types.

## Permissions for Authenticating with an Authorization Token

### For all asset types except for Secrets, Alerts/Incidents, and Application Settings

**Repository Permissions:**

* Administration - Read-only
* Codespaces metadata - Read-only
* Commit statuses - Read-only
* Contents - Read-only
* Metadata - Read-only
* Pull requests - Read-only

**Account permissions:**

* Email addresses - Read-only
* Gists - Read-only
* Profile - Read-only

### For Fetching Secrets

**Repository Permissions:**

* Codespaces secrets - Read-only
* Secrets - Read-only

**Account permissions:**

* GPG keys - Read-only
* Git SSH keys - Read-only
* SSH signing keys - Read-only

### For Fetching Alerts/Incidents

**Repository AND Account permissions:**

* Code scanning - Read-only
* Secret scanning - Read-only

### For Fetching Application Settings and Licenses

The 'Plan - Read-only' Account permission is required.

## Permissions for Authenticating with a GitHub App

### For all asset types except for Secrets, Alerts/Incidents, and Application Settings

**Repository Permissions:**

* Administration - Read-only
* Codespaces metadata - Read-only
* Commit statuses - Read-only
* Contents - Read-only
* Metadata - Read-only
* Pull requests - Read-only

**Account permissions:**

* Email addresses - Read-only
* Gists - Read-only
* Profile - Read-only

**Organization permissions:**

* Administration - Read-only
* Custom Organization Roles - Read-only
* Custom properties - Read-only
* Custom repository roles - Read-only
* Members - Read-only
* Team discussions - Read-only
* Projects - Read-only **(Only if you fetch Application Resources)**

### For Fetching Secrets

**Repository Permissions:**

* Codespaces secrets - Read-only
* Secrets - Read-only

**Account permissions:**

* GPG keys - Read-only
* Git SSH keys - Read-only
* SSH signing keys - Read-only

**Organization permissions:**

* Personal access tokens - Read-only
* Secrets - Read-only

### For Fetching Alerts/Incidents

**Repository AND Account permissions:**

* Code scanning - Read-only
* Secret scanning - Read-only

### For Fetching Application Settings and Licenses

The 'Plan - Read-only' Account permission is required.