# Source: https://docs.hypermode.com/agents/connections/attio.md

# Using Attio with Hypermode

> Connect your Hypermode agent to Attio for CRM operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=0f9ae3db85a96fe5931b7c830e3fa1f8" alt="Attio" width={48} height={48} width="400" height="400" data-path="images/agents/connections/icons/attio.png" srcset="https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=280&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=5b8a882e22adf863974a64b1c0fc1ab0 280w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=560&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=382a0c3c8225eaa2fa274a8fdf35d1f6 560w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=840&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=69ce3a07add0183fbc32df84f146ce13 840w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=1100&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=feef1b97f205f786b7bb47ff5e447158 1100w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=1650&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=7968b003eaaaca6bbe429c842f16c7fe 1650w, https://mintcdn.com/hypermode/Bu7AIG01ktGbhJIf/images/agents/connections/icons/attio.png?w=2500&fit=max&auto=format&n=Bu7AIG01ktGbhJIf&q=85&s=b6ead06f47f48ebd072850a649a34be7 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">Attio</h2>

    <p className="text-gray-600 m-0">
      Highly customizable, modern CRM platform
    </p>
  </div>
</div>

## Overview

Attio is a modern, highly customizable CRM platform that helps businesses manage
customer relationships, track deals, and organize data in a flexible way. This
guide will walk you through connecting your Hypermode agent to Attio for
automated CRM operations.

## Prerequisites

Before connecting Attio to Hypermode, you'll need:

1. An [Attio workspace](https://attio.com/)
2. Admin permissions to generate API credentials
3. A [Hypermode workspace](https://hypermode.com/)

## Getting started with Attio

### Step 1: Sign up for Attio

If you don't have an Attio account yet, you'll need to create one first. Visit
the Attio homepage to get started:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=1d198aa6e0122e8499a490d41c4df274" alt="Attio Homepage" width="3456" height="1980" data-path="images/connections/attio/homepage.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=630524550be80d11d9b6580ef038c66a 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c220232954fa97d91f0c02a5c4fbd02e 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=148e5c0965856d2e2bfea12347dc7fe1 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=11cfa8bfebfd5ec0f3ebcf51327336b0 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=244dbd981caaaabf32e57a1e225ad1b0 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/homepage.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a99aafd3d674c87ec8628ef2ec6e1713 2500w" data-optimize="true" data-opv="2" />

Click "Sign up" to create your new Attio workspace. You'll need admin access to
generate the API credentials required for the Hypermode integration.

### Step 2: Note your workspace domain

Your Attio workspace URL will be in the format
`https://[workspace-name].attio.com`. Make note of your workspace name as you'll
authenticate through Attio when adding the connection to Hypermode.

## Creating your Attio agent

### Step 1: Create a new agent

From the Hypermode interface, create a new agent:

1. Click the agent dropdown menu
2. Select "Create new Agent"

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c4e9de8896b34b050919e22e926bdccb" alt="Navigate to create agent" width="2542" height="1948" data-path="images/connections/attio/navigate-create-agent.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3d8ab68ff222c6d8c1033345c4c07ae3 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4911c14ae7bb30ccae89080acb603bcc 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d9cf8cdaac9c51b3996513b454ca1181 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=cd54f188df57e99692ae1b30dc097a07 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=30371f513ab2b2b1319bc86f056cb9f8 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/navigate-create-agent.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6d665f6794bba6a7e1bd9f6fbcae5659 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure agent settings

Use these recommended settings for your Attio CRM agent:

* **Agent Name**: CRMAgent
* **Agent Title**: Attio CRM Manager
* **Description**: Manages customer relationships and deal tracking in Attio CRM
* **Instructions**: You have a connection to Attio CRM. You can create and
  update companies and deals, search for existing records, manage deal
  pipelines, and track customer interactions. Always confirm data before making
  changes and provide clear summaries of actions taken.
* **Model**: GPT-4.1 - Default - Optionally, use Claude for best results

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=28d33653baef47e7744c953bc6b612a1" alt="Create agent modal" width="3456" height="1980" data-path="images/connections/attio/create-agent-modal.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=9ee4553cd6c5f4c541654d1061f68836 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f272923fe0cff2d8e8a9ae6419ef3367 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=95f4585a8145a28b9676efb7acccb24f 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=daa841204a4c1070162b32547b6fbbc9 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=44cc7172cdf55d020b7558b550cbe30a 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-agent-modal.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7acc0503eb5dc40c4215731cd20be9bc 2500w" data-optimize="true" data-opv="2" />

### Step 3: View your agent profile

Once created, navigate to your agent's settings page:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=cd68ed21c241a51d1bf81a5b82161a0d" alt="Agent profile" width="3102" height="1946" data-path="images/connections/attio/agent-profile.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f31f19cffb9a89bd3c49fc1803b76a22 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4eff85e190cbcee39ead02a963557ae6 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=191eb501fa369b9390e12a4f4b8034dc 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8671e4648fb4162dbc9f5c4e4f5aeabf 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=871a76764bc2d3157003fc79fceb6baf 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/agent-profile.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=649020a7160519e0088e6eec2e1897fb 2500w" data-optimize="true" data-opv="2" />

## Connecting to Attio

### Step 1: Add the Attio connection

Navigate to the **Connections** tab and add Attio:

1. Click "Add connection"
2. Search for "Attio" in the available connections

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e27fd3d8420608258833733cb64137c5" alt="Add Attio connection" width="3456" height="1980" data-path="images/connections/attio/add-attio-connection.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d30ffcdf6c8a2886d0947fbeeb51c93f 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5d347824e12b2dc4a8c07626d2d3677b 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=092dfafea1ccda10fc2460572c347fdc 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=17f9a959363f4f8379ec09a52c4c040f 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=88fffa377443629882ecd5fdab8f7c03 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-attio-connection.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=bdd54bd4bc106f9799d2d79108101602 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure connection with OAuth

When you select Attio, you'll be prompted to authenticate via OAuth. This will
redirect you to Attio's authorization page:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d389de625044abbe9fba3cb9d2511202" alt="Attio App Request" width="3106" height="1950" data-path="images/connections/attio/attio-app-request.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=9d5e3e1fa8b634b0010cc220f05237d7 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5329d17eb2d3f2fe9735683512b61575 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2fb41c604f64da82f6d78ea03197f289 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=eb9dbb69931799a0c5aad67e693bd95f 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=45f381ccd7fbc3c804a055a6c3101e2e 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/attio-app-request.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=26642b678d5664ed49a0ae46544de1e9 2500w" data-optimize="true" data-opv="2" />

Follow the OAuth flow to grant Hypermode access to your Attio workspace. This
secure process ensures your credentials are never directly stored in Hypermode.

<Note>
  The OAuth flow ensures secure authentication without exposing your API
  credentials. You'll be redirected back to Hypermode once authorization is
  complete.
</Note>

## Understanding Attio's data model

Attio uses a flexible data model that includes:

* **Companies**: Organizations and account details
* **Deals**: Sales opportunities and their progress through pipelines
* **Custom Objects**: Any custom data types you've created
* **Lists**: Collections of records with shared characteristics
* **Attributes**: Custom fields that can be added to any object type

This flexibility makes Attio perfect for:

* Complex sales pipeline management
* Detailed customer relationship tracking
* Custom workflow automation
* Advanced reporting and analytics

## Testing the connection

### Test 1: Search for existing companies

Start a new thread with your agent and test the connection:

```text
Can you show me the first 10 companies in our Attio CRM?
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c56dde6266701580156fe005fbf5c078" alt="Search companies result" width="3106" height="1950" data-path="images/connections/attio/first-companies.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f93301315b5eba61bcfdf4523a2b05ad 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=587caed843dd50feda226659c79e7781 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=67081552503c27f598b22d017b107067 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e7e321ebe92bb1a08f9419361b8c6b7e 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5e09a00f5b66ef2031bd1987dcd98c4d 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/first-companies.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c9e1d891be4414fc980f599f06bc09e2 2500w" data-optimize="true" data-opv="2" />

### Test 2: Create a new company

Try adding a new company to your CRM:

```text
Introspect the workspace and create a new company in Attio with the following details:

Name: Tech Solutions Inc
Website (domain): techsolutions.com
Industry/Category: Software
Employee Range: 50-100
Description: A leading provider of innovative tech solutions.
Primary Location: San Francisco, CA
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fb423f0d4792c58f248a1c8540f23dcb" alt="Create company" width="3102" height="1946" data-path="images/connections/attio/create-company.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8313269b96b3b301a3727c55e33fe2a0 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6461a0adf3bba7d9d0ea69cb94baec8e 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f915b96bdcfdae485b7a2bf3d626f821 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8c1104d4e86e94806086a37b2afba7e8 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=247f96bef814b9d4152753158a369f65 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-company.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c502ad36fde8a24641a33984f8fa1b8b 2500w" data-optimize="true" data-opv="2" />

### Test 3: Create and manage a deal

Create a sales opportunity and track its progress:

```text
Create a new deal in Attio:
- Deal name: "Q1 Enterprise Software License"
- Company: Tech Solutions Inc
- Value: $50,000
- Stage: Discovery
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a6d8bed90f990b646f7be8468ccf8643" alt="Create deal" width="3102" height="1946" data-path="images/connections/attio/create-deal.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2627cfd666869a2e27f859364c0c0dc1 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e6b1da45ca8b269a7573d81c1250ed58 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f1ec87ea493d16aa0bf4a7e73f6e5f80 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=387691f93e5de2b73c84e078c3c81280 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4c76ee37f2de1a2053f9f2d4a3709178 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/create-deal.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=06379f126306ee401191f3437ff2950c 2500w" data-optimize="true" data-opv="2" />

### Test 4: Update deal status

Move the deal through your pipeline:

```text
Add a note about the "Enterprise Software License - TechCorp" deal that the demo completed yesterday.
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b1de2bf86e201a569c7ca9b0a3b67317" alt="Add note" width="3102" height="1946" data-path="images/connections/attio/add-note.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3477eb1f092d2eadf40ba56d12f1c605 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8d81f04199eed62ff473d6cff0493a96 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b5011f3024f6de66f337231da17aded1 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=abe70446e4280301f0e9def6cc847545 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2f49f56e3623db7ce806a67fa15b36a3 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/attio/add-note.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=55adb4b21677a17284fb8b1a1ebf57cc 2500w" data-optimize="true" data-opv="2" />

## What you can do

With your Attio connection established, your agent can:

* **Manage companies**: Create, update, and search for organizations and account
  details
* **Track deals**: Create opportunities, update pipeline stages, and manage deal
  values
* **Organize data**: Use lists and custom attributes to categorize records
* **Search and filter**: Find records based on various criteria
* **Generate reports**: Analyze pipeline health and company data
* **Integrate workflows**: Combine CRM operations with other tools like email,
  calendar, and project management

<Note>
  The Attio connection provides access to a comprehensive set of tools for CRM
  management focused on companies and deals. The available tools may vary as we
  optimize the connection for the most commonly used operations.
</Note>

## Troubleshooting

### Common issues

#### OAuth authentication failed

* Ensure you have admin permissions in your Attio workspace
* Try clearing your browser cache and cookies
* Make sure you're logged into the correct Attio workspace during OAuth flow

#### "Workspace not found" error

* Confirm you completed the OAuth flow successfully
* Check that your workspace domain is spelled correctly
* Verify you have access to the workspace

#### Record creation failures

* Ensure required fields are provided for the object type
* Check that attribute names match exactly (case-sensitive)
* Verify that enum values are valid for dropdown fields

## Learn more

* [Attio Documentation](https://developers.attio.com/)
* [Attio API Reference](https://developers.attio.com/reference)
* [CRM Best Practices](https://attio.com/blog)

<Tip>
  Combine Attio with other Hypermode connections to build powerful sales
  workflows. For example, use Gmail to automatically log email interactions, or
  Google Calendar to schedule follow-up meetings directly from deal records.
</Tip>
