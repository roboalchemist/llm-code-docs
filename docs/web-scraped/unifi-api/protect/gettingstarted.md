# gettingstarted

Source: https://developer.ui.com/protect/v6.2.83/gettingstarted

UniFi APIEndpoints combined into Ansible Modules for customized workflows.Introduction
Each UniFi Application has its own API endpoints running locally on each site, offering detailed analytics and control related to that specific application.
Authentication
An API Key serves as a unique identifier used to authenticate API requests. These keys are essential for securing access to your UniFi account and its associated devices. Each key is linked to the specific organization or UI account that generated it, ensuring secure and personalized API interactions.
Obtaining an API Key
Sign in to the UniFi Site Manager at unifi.ui.com.Navigate to the API configuration page:GA: Go to the API section.EA: Go to Settings → API Keys.Select "Create New API Key"Copy the generated key and store it securely, as it will only be displayed once.Ensure the key is properly hashed and securely stored.