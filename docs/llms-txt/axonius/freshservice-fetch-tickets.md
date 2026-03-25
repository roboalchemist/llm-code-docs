# Source: https://docs.axonius.com/docs/freshservice-fetch-tickets.md

# Freshservice Fetch Tickets

Freshservice is a cloud-based IT help desk and service management solution that enables organizations to simplify their IT operations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Tickets

## Parameters

1. **Freshservice Domain** *(required)* - The hostname or IP address of the Freshservice server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings)\[dd]`{target=`\_blank`}`.

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **Throttle API Requests** - Select this option to delay requests by 10 seconds if they're below 10% of the maximum limit.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Freshservice Fetch Tickets.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Freshservice%20Fetch%20Tickets.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Freshservice URL Parameters in JSON format** - Enter a JSON file with Freshservice URL parameters to add to the Request URL sent to fetch tickets.
  If your JSON is in the following format:
  ```json
  {"updated_since":"2025-01-17", "workspace_id":3, "filter": "my_custom_filter"}
  ```
  it is added to the URL:
  [https://domain.com/tickets?\*\*\*updated\_since=2025-01-17\&workspace\_id=3\&filter=my\_custom\_filter](https://domain.com/tickets?***updated_since=2025-01-17\&workspace_id=3\&filter=my_custom_filter)\*\*\*

* **Tickets Status Description Mapping** - Expand this section to define the various statuses that a ticket can have within the system by mapping each **Status** number to a descriptive **Status Description**. This enables users to easily understand the meaning of each status.
  * Click `+` to create a new entry for a status.
  * In **Status**, click the Up/Down arrow to select a unique numerical value. This number serves as the system's identifier for that specific ticket status.
  * In **Status Description**, type a clear and concise explanation of what the selected Status number represents.

<Callout icon="📘" theme="info">
  Note

  It is recommended to assign the following Status Descriptions to the specified Status numbers as defined in the [Freshservice API](https://api.freshservice.com/#create_ticket):

  * Status **2`-`Open**

  * Status **3`-`Pending**

  * Status **4`-`Resolved**

  * Status **5`-`Closed**
</Callout>

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Freshservice API](https://api.freshservice.com/#intro).

## Locate API Key

**To locate your API Key**

1. Log in to your **Support Portal**.
2. Click on your profile picture on the top right corner of your portal.
3. Go to the **Profile Settings** page. Your API Key is displayed below the **Change Password** section on the right side.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.59.1