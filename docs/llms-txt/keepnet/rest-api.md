# Source: https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/rest-api.md

# REST API

## Why is REST API Needed?

This section explains the potential benefits available with the use of a REST API.

REST API allows you to configure the integration between the platform and other products, export all the data you see on the platform and add data to the platform with supported API requests. A REST API configuration will enable you to efficiently run and manage almost every function on the product off-platform.

## REST API Page

You can view, edit, or delete any API configurations at the **Company > Company Settings > Rest API** page.

<table><thead><tr><th width="169"></th><th width="579.1428571428571"></th></tr></thead><tbody><tr><td>Client Name</td><td>The REST API settings' name.</td></tr><tr><td>API Key</td><td>The API Key that belongs to the related REST API setting.</td></tr><tr><td>Status</td><td>The status can be set to inactive to not to use Rest API anymore.</td></tr><tr><td>Date Created</td><td>The date and time that REST API settings’ were created.</td></tr><tr><td>Action</td><td>REST API settings’ can be edited or deleted.</td></tr></tbody></table>

## How to Configure a REST API

Go to **Company > Company Settings > REST API** from the platform menu. Then click the **+ NEW** button to create a new REST API. The components of the REST API edit page are explained in detail in the table below.

<table><thead><tr><th width="150"></th><th width="579.1428571428571"></th></tr></thead><tbody><tr><td>Client Name</td><td>Name of the REST API configuration</td></tr><tr><td>Generate Client Credentials</td><td>Create Client ID and Client Secret keys by clicking the button</td></tr><tr><td>Client ID</td><td>Client ID key information</td></tr><tr><td>Client Secret</td><td><p>Client Secret key information</p><p>The secret key is only displayed at the time of creation. This information must be copied and saved in a safe place at this stage.</p></td></tr><tr><td>IP Restriction</td><td><p>You can limit access to the REST API with the Client ID and Client Secret information based on IP address.</p><p><strong>Allow all IPs =</strong> Any IP address can have the access to use Rest API.</p><p><strong>Restrict access by IP address =</strong> Only permitted IP addresses will have access to the REST API. You may add additional IP addresses if needed by clicking Add IP Address button.</p></td></tr><tr><td>Client Role</td><td><p>The standard roles are Reseller or Company Admin to access the API endpoints with the chosen role’s privilege.</p><p>You may create and define a custom <a href="../system-users/user-roles">role</a> with custom privileges.</p></td></tr><tr><td>Status</td><td>The status can be set to Inactive to not to use Rest API anymore.</td></tr></tbody></table>

## Video Tutorial

This tutorial explains the potential benefits available with the use of a REST API.

{% embed url="<https://youtu.be/rKRFEcpLTE0>" %}

## Use Cases

Use the address below to access the Swagger interface and authorize with **client\_id** and **client\_secret** information in order to use the endpoints, as described in these use case scenarios.

{% embed url="<https://api.keepnetlabs.com/docs/index.html>" %}
API Documentation
{% endembed %}

### Use Case 1: SOAR Integrations

API integration with your security orchestration, automation, and response (SOAR) solutions enables you to respond more efficiently to harmful emails.

If the [Incident Responder](https://keepnetlabs.com/products/incident-responder) API endpoints are integrated with your current SOAR products, such as antivirus, firewall, endpoint detection, and response, proxy services, etc., it will save valuable time in the response to a potential threat via API endpoints in comparison with a manual investigation of a reported email.

### Use Case 2: IAM - IDM Integration (​​User provisioning)

Identity and access management is critical to success; however, manually uploading target user information to the platform is a laborious, time-consuming process. I Using the platform's API pool makes it possible to automatically perform tasks such as creating, updating, or deleting a target user.

### Use Case 3: Password Management

The passwords of the system users registered with the platform must be changed at designated intervals. If your company does not support SAML integration, system users' passwords can be changed periodically using the platform's API pool.

### Use Case 4: SIEM Integration

The actions of all system admin users and service accounts on the platform are recorded in audit logs for auditability and accountability.

You can transfer the audit logs to your SIEM product in real-time to manage and see audit logs on the SIEM product. You can either do it with **REST API** or from the **Web Interface**.

## FAQ

### Q: I have an identity management (IDM) solution, can user provisioning be performed in real-time with the platform?

A: Yes. The API Target User can facilitate secure and effortless management of user information. You can find additional information on the API documentation.

### Q: How can I purposely expire a token so I can get a new one?

A: No, you can't expire the token. You can create as many token sessions as you want.

### Q: Can I request token validity period when I initially request a token instead of getting a default validity period?

A: No, you can't change the validity period of the token.

### Q: What is the default token validity period?

A: It is 24hr.
