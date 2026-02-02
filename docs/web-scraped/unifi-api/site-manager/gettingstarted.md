# gettingstarted

Source: https://developer.ui.com/site-manager/v1.0.0/gettingstarted

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Site Manager API v1.0 (Official)
Getting Started

The Site Manager API empowers developers to programmatically monitor and manage UniFi deployments at scale. It provides comprehensive tools to access and control your UniFi devices' data, enabling you to retrieve detailed information, monitor performance metrics, and efficiently manage your network infrastructure.

The Site Manager API primarily focuses on extracting data from the UniFi Site Manager (unifi.ui.com). Subsequent versions will extend functionality to include more granular configurations, facilitating the management of individual sites and their associated devices.

Your feedback at https://unifi.ui.com/api is invaluable in helping us enhance and tailor the API to better address your specific requirements.

Authentication

An API Key serves as a unique identifier used to authenticate API requests. These keys are essential for securing access to your UniFi account and its associated devices. Each key is linked to the specific UI account that generated it, ensuring secure and personalized API interactions.

Obtaining an API Key
Sign in to the UniFi Site Manager at unifi.ui.com.
Navigate to the API configuration page:
GA: Go to the API section.
EA: Go to Settings → API Keys.
Select "Create New API Key"
Copy the generated key and store it securely, as it will only be displayed once.
Ensure the key is properly hashed and securely stored.
Use the API Key

Incorporate the API key into the X-API-Key header for all requests. Follow the example provided, replacing YOUR_API_KEY with your actual API key.

Note: The API key is currently read-only. When write endpoints become available, you'll be able to enable write access as needed, and the existing key won't be updated automatically. A manual update will be required.

curl -X GET 'https://api.ui.com/v1/hosts' \
 -H 'X-API-KEY: YOUR_API_KEY' \
 -H 'Accept: application/json'
Rate Limiting

The API rate limits are enforced based on the API version:

Early Access (EA) version:
100 requests per minute
v1 stable release:
10,000 requests per minute

If you exceed these limits, the server will respond with a 429 Too Many Requests status code. The response will include a Retry-After header indicating the number of seconds to wait before making additional requests, following the RFC specification.