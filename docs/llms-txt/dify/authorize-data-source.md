# Source: https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/authorize-data-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Authorize Data Source

Dify supports connections to various external data sources. To ensure data security and access control, different data sources require appropriate authorization configurations. Dify provides two main authorization methods: **API Key** and **OAuth**.

## Accessing Data Source Authorization

In Dify, you can access data source authorization through the following two methods:

### I. Knowledge Pipeline Orchestration

When orchestrating a knowledge pipeline, select the data source node that requires authorization. Click **Connect** on the right panel.

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-1.PNG?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=e85d0e180bc24a78429b3ec16598a558" alt="Knowledge Pipeline Authorization" width="1280" height="435" data-path="images/knowledge-base/authorize-data-1.PNG" />

### II. Settings

Click your avatar in the upper right corner and select **Settings**. Navigate to **Data Sources** and find the data source you wish to authorize.

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-2.PNG?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=10fc039d69de4ae216fd99182e20aaca" alt="Settings Authorization" width="1280" height="619" data-path="images/knowledge-base/authorize-data-2.PNG" />

## Supported Data Source Authorization

| Data Source  | API Key | OAuth |
| ------------ | ------- | ----- |
| Notion       | ✅       | ✅     |
| Jina Reader  | ✅       |       |
| Firecrawl    | ✅       |       |
| Google Drive |         | ✅     |
| Dropbox      |         | ✅     |
| OneDrive     |         | ✅     |

## Authorization Processes

### API Key Authorization

API Key authorization is a key-based authentication method suitable for enterprise-level services and developer tools. You need to generate API Keys from the corresponding service providers and configure them in Dify.

#### Process

1. On the **Data Source** page, navigate to the corresponding data source. Click **Configure** and then **Add API Key**.

   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-3.PNG?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=0d6e202e0e1b86bb29934182085469b4" alt="Add API Key" width="1381" height="256" data-path="images/knowledge-base/authorize-data-3.PNG" />

2. In the pop-up window, fill in the **Authorization Name** and **API Key**. Click **Save** to complete the setup.

   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-4.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=3c38c6e7cac17a43ac1cd82e2eaf76dd" alt="API Key Configuration" width="1280" height="720" data-path="images/knowledge-base/authorize-data-4.png" />

The API key will be securely encrypted. Once completed, you can start using the data source (e.g., Jina Reader) for knowledge pipeline orchestration.

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-6.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=9920807bc2169b7d8324fc4a15018c8a" alt="API Key Complete" width="1328" height="256" data-path="images/knowledge-base/authorize-data-6.png" />

### OAuth Authorization

OAuth is an open standard authorization protocol that allows users to authorize third-party applications to access their resources on specific service providers without exposing passwords.

#### Process

1. On the **Data Source** page, select an OAuth-supported data source. Click **Configure** and then **Add OAuth**.

   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-7.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=7ed7d760fd45ddddab5cb0c696e78046" alt="Add OAuth" width="1280" height="305" data-path="images/knowledge-base/authorize-data-7.png" />

2. Review the permission scope and click **Allow Access**.

<div style={{display: 'flex', flexWrap: 'wrap', gap: '30px'}}>
  <div style={{flex: 1, minWidth: '300px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-8.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=aa178ea168624ce8e56c668ed7f0d06e" alt="OAuth Permissions" width="1242" height="1242" data-path="images/knowledge-base/authorize-data-8.png" />
  </div>

  <div style={{flex: 1, minWidth: '300px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-9.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=1cdde896b888e6135c5cccd587b15a46" alt="OAuth Allow" width="1280" height="1280" data-path="images/knowledge-base/authorize-data-9.png" />
  </div>
</div>

#### OAuth Client Settings

Dify provides two OAuth client configuration methods: **Default** and **Custom**.

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-10.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=6fa847da415eafdd3bd4553567b005a1" alt="OAuth Client Settings" width="1034" height="580" data-path="images/knowledge-base/authorize-data-10.png" />

<Tabs>
  <Tab title="Default">
    The default client is primarily supported in the SaaS version, using OAuth client parameters that are pre-configured and maintained by Dify. Users can add OAuth credentials with one click without additional configuration.
  </Tab>

  <Tab title="Custom">
    Custom client is supported across all versions of Dify. Users need to register OAuth applications on third-party platforms and obtain client parameters themselves. This is mainly suitable for data sources that don't have default configuration in the SaaS version, or when enterprises have special security compliance requirements.
  </Tab>
</Tabs>

**Process for Custom OAuth**

1. On the **Data Source** page, select an OAuth-supported data source. Click **Configure** and then the **Setting icon** on the right side of **Add OAuth**.

   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-11.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=8329ee62c4fee7be6b446dc132077d6f" alt="Custom OAuth Settings" width="1280" height="364" data-path="images/knowledge-base/authorize-data-11.png" />

2. Choose **Custom**, enter the **Client ID** and **Client Secret**. Click **Save and Authorize** to complete the authorization.

   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/authorize-data-12.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=b96222b52fdb37964b82658fdd149313" alt="Custom OAuth Configuration" width="1198" height="1240" data-path="images/knowledge-base/authorize-data-12.png" />


Built with [Mintlify](https://mintlify.com).