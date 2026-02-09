# gettingstarted

Source: https://developer.ui.com/network/v10.1.68/gettingstarted

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Introduction

Each UniFi Application has its own API endpoints running locally on each site, offering detailed analytics and control related to that specific application.

## Authentication

An API Key serves as a unique identifier used to authenticate API requests. These keys are essential for securing access to your UniFi account and its associated devices. Each key is linked to the specific organization or UI account that generated it, ensuring secure and personalized API interactions.

## Obtaining an API Key

1. Sign in to the UniFi Site Manager at [unifi.ui.com](https://unifi.ui.com).
2. Navigate to the API configuration page:
   * **GA:** Go to the **API** section.
   * **EA:** Go to **Settings → API Keys**.
3. Select "Create New API Key"
4. Copy the generated key and store it securely, as it will only be displayed once.
5. Ensure the key is properly hashed and securely stored.