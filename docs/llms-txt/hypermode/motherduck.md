# Source: https://docs.hypermode.com/agents/connections/motherduck.md

# Using MotherDuck with Hypermode

> Connect your Hypermode agent to MotherDuck for powerful analytics and data warehouse operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=06f16902cc994adf01a17e2e015d54cd" alt="MotherDuck" width={48} height={48} width="264" height="191" data-path="images/agents/connections/icons/motherduck.png" srcset="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=280&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=0396a004a56ff295df0cf107bfbd0bfe 280w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=560&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=af5c62b96f8fdfa1d8acc82b605be382 560w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=840&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=bced234824b582439e96cc95afafae36 840w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=1100&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=498afbc30e4383bba728720b5b351e4f 1100w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=1650&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=8e00b6230488aa32904d27d816bd5efb 1650w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/motherduck.png?w=2500&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=1499df3e2d84fd019137fc69c238cd42 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">MotherDuck</h2>

    <p className="text-gray-600 m-0">
      Serverless analytics platform powered by DuckDB
    </p>
  </div>
</div>

## Overview

MotherDuck is a serverless analytics platform that combines the speed of DuckDB
with cloud convenience. This guide will walk you through connecting your
Hypermode agent to MotherDuck, enabling powerful data analytics, complex
queries, and insights generation using both your own data and MotherDuck's rich
sample datasets.

## Prerequisites

Before connecting MotherDuck to Hypermode, you'll need:

1. A [MotherDuck account](https://motherduck.com/)
2. MotherDuck API token for authentication
3. A [Hypermode workspace](https://hypermode.com/)

## Setting up MotherDuck

### Step 1: Create your MotherDuck account

If you haven't already, sign up for a MotherDuck account to access serverless
analytics capabilities.

### Step 2: Access your workspace

Once logged in, you'll see your MotherDuck workspace with access to:

* Your personal databases
* Sample datasets (NYC Taxi, TPC-H, etc.)
* Query editor and analytics tools

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d8b98b676d9fa14dc9fa94c11086da26" alt="MotherDuck workspace" width="2968" height="1856" data-path="images/connections/motherduck/motherduck-workspace.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8294fb910cfc918b4585906548ccaa1b 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2cfb8251ec89d5fd8d3fe7e7f7eca2a0 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=946fa5cd69760834dfc79409a971da93 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e2035fea8463d1141d4a73c2cede19a5 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ba315d4dedac02d7efdac1d1ee5a5049 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-workspace.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=1cb191dd02d1fd5ed1da91958f560f59 2500w" data-optimize="true" data-opv="2" />

### Step 3: Generate an API token

Create an API token for secure access:

1. Navigate to **Settings** → **Access Tokens** in your MotherDuck dashboard
2. Click **Create Token**
3. Give your token a descriptive name (for example, "Hypermode Integration")
4. Copy the generated token immediately

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=39a79c5c3d086f9b663d6e7a8e19e179" alt="Create API token" width="1774" height="976" data-path="images/connections/motherduck/create-api-token-1.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c8f06193a486b323f9af0a26230d8d48 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=43564aca28638fef2bc76fed8ee537d7 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=48e4c74a8c29d424f1139db7f17bff31 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4104f41d6ffc12f008fb79018818ad6a 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b3873e5141fefe803cfe468ea34aa2e9 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-1.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=604e85e701c744cc9a1c8e8bdb8771ef 2500w" data-optimize="true" data-opv="2" />

<Warning>
  Store your API token securely! You won't be able to see it again after
  creation, and it provides full access to your MotherDuck workspace.
</Warning>

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fe2526d525c00a156e3f9a3c5a8cb834" alt="Create API token" width="1414" height="806" data-path="images/connections/motherduck/create-api-token-2.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2b2bae047b80736474c957821f294255 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ca3ab8e2098957fdcf1609373032065f 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=02504298e5ad853d708015c9533834be 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=07372990768f38aa5a9af1d8f5937b00 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f766d8be4643073d7d3bcec779f9f397 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-api-token-2.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4c268e23c643ea568a97e1d7d485983e 2500w" data-optimize="true" data-opv="2" />

## Creating your MotherDuck agent

### Step 1: Create a new agent

From the Hypermode interface, create a new agent manually:

1. Click the agent dropdown menu
2. Select "Create new Agent"

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f415eef3e6b1802f43d3df54ba721cc9" alt="Navigate to create agent" width="1302" height="414" data-path="images/connections/motherduck/create-new.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=49d79c6c2483b806015f10db97fc5246 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c3ddca1c24f6184932391c090cbdee0e 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3c5e43fdfb80459a5fb94c7feab774e4 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=50dc4dc4c9039aa7c9e5a1840306515d 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f2f90254cbb438188af5a6c705161405 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-new.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b97a00fc2822b17db39450cd38d7bd7f 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure agent settings

Use these recommended settings for your MotherDuck agent:

* **Agent Name**: AnalyticsAgent
* **Agent Title**: Connects to MotherDuck Analytics
* **Description**: AnalyticsAgent performs data analysis and generates insights
* **Instructions**: You have a connection to MotherDuck and various other
  developer tools to perform advanced analytics, generate insights, and answer
  data questions. You can query large datasets, perform aggregations, and create
  data visualizations. You have access to sample datasets including NYC Taxi
  data, TPC-H benchmark data, and more.
* **Model**: GPT-4.1

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=aa1b4d3cd0d3ee1156719febf9142371" alt="Create agent modal" width="1728" height="1244" data-path="images/connections/motherduck/create-agent-details.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c7b6590284630668df440171fbc41850 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=92243b588d101d55734f43ebad98036b 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4d3bdd7ceb1a1f2766877e18c8e5ea9a 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4569b0fc9343cd616ecb46a37113f9fb 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a1326ebbc0d5f4e6484154428bb0168c 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/create-agent-details.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2630d26c1195c92cb5fe8f62a351b741 2500w" data-optimize="true" data-opv="2" />

### Step 3: View your agent profile

Once created, navigate to your agent's settings page to see the profile:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d1394879141c7b6ef51db792f144a7de" alt="Agent profile" width="2400" height="1830" data-path="images/connections/motherduck/agent-profile-details.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fb49d0b947d4840f083ab45abf43c9b6 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=9ee07af3eb2031fe3a37fdfe25a1352c 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8a42577620c4a320c01d0e58dc0e03ed 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=92c5450992f9257446a7bbd290207e04 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8fac9bd0c1b0c37cc0d6f7121d8c8a63 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/agent-profile-details.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fc9bfdab64f146610ec78e4527efdfc5 2500w" data-optimize="true" data-opv="2" />

## Connecting to MotherDuck

### Step 1: Add the MotherDuck connection

Navigate to the **Connections** tab and add MotherDuck:

1. Click "Add connection"
2. Select "MotherDuck" from the dropdown

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=46e36b9801e64fab6a1d3f22ab999a20" alt="Add MotherDuck connection" width="1138" height="522" data-path="images/connections/motherduck/add-motherduck-connection.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d11145d129945a873ddb40d920532671 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4c65d03851644358d406d75197c803fd 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4557fa04287a04cf986ea6d54c36606c 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2af156b24490d4018a42819b0c14815d 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e2595ce93944f1a593addec5e4b3c436 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/add-motherduck-connection.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4eda605a60b690810449740c5a90f841 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure credentials

Enter your MotherDuck credentials:

* **API Token**: Your MotherDuck API token created in the previous step

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b84b352df1460da954153b25fd6d4256" alt="MotherDuck connection modal" width="1166" height="726" data-path="images/connections/motherduck/motherduck-token.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6d53466adb1ff3321f74774e697b9398 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=1db7c808708ab0617f954a21ce369b3f 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5d195ccd1077ba9c93330230167e2393 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=9981b2125d7dbc2bfb2096bcfcc06a81 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=50658958b11609206e969aa3984ea390 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/motherduck-token.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8b59bfc5aa3064bf532fdab68289d91f 2500w" data-optimize="true" data-opv="2" />

## Verifying the MotherDuck connection

### Step 1: Test basic connectivity

Start a new thread and test the connection:

```text
What databases are available in my MotherDuck workspace?
```

**Expected result** Your agent will show the available databases:

* `md_information_schema` - System metadata
* `my_db` - Your personal database
* `sample_data` - Rich sample datasets

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=97616142da42f79828ea663889c229af" alt="Test connection" width="2214" height="1366" data-path="images/connections/motherduck/verify-connection.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=c646a4b6c28a77985dfefc5242db9c37 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a405a2d6d4e6a6181d7805e668798cf8 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=cf86bcbdf63639840d0cfd876e0fe96b 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=0978a6adb4b80161e6630afd3e783a91 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=82201194a906c721e864072ecd69dbc2 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/verify-connection.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=976daf417824a0c4b2ea1f4b6e80a87c 2500w" data-optimize="true" data-opv="2" />

### Step 2: Explore sample datasets

Test access to the sample datasets:

```text
What sample datasets are available? Can you show me the schemas and table structures?
```

**Expected result** Your agent will discover these sample datasets:

* **NYC data** (`sample_data.nyc`): taxi trips, service requests, rideshare data
* **Hacker News** (`sample_data.hn`): 3.8M posts and comments
* **Movies** (`sample_data.kaggle`): 41K movies with embeddings
* **WHO Air Quality** (`sample_data.who`): Global ambient air quality data
* **Stack Overflow Survey** (`sample_data.stackoverflow_survey`): Developer
  survey results

### Step 3: Query sample data

Test with a simple query on the NYC taxi dataset:

```text
Show me 3 sample taxi trips from the NYC dataset with their basic details
```

**Expected result** Your agent will return something like:

```text
VendorID: 2, Pickup: 2022-11-04 23:13:01, Dropoff: 2022-11-04 23:25:38
Trip Distance: 1.78 miles, Total Amount: $16.56, Passengers: 4
```

## Exploring built-in sample datasets

### NYC taxi dataset (3.2M records)

The NYC taxi dataset contains detailed trip information with 19 fields including
timestamps, locations, fares, and payment details:

```text
Analyze NYC taxi usage patterns by hour of day - when are the busiest times?
```

**Real results from the data:**

* **Peak hours**: 12-6 PM (157K-223K trips per hour)
* **Quietest time**: 3-4 AM (23K trips)
* **Highest average fares**: Early morning 4-6 AM (\$27-30) due to airport trips
* **Lowest average fares**: Mid-morning 9-11 AM (\~\$20-21)

### Hacker News dataset (3.8M posts)

Complete Hacker News data including stories, comments, scores, and timestamps:

```text
What are the highest-scoring Hacker News stories of all time?
```

**Real top stories include:**

{/* trunk-ignore-begin(vale/error) */}

1. **"Mechanical Watch"** - 4,298 points by todsacerdoti
2. **"Google Search Is Dying"** - 3,636 points by dbrereton
3. **"My First Impressions of Web3"** - 3,393 points by natdempk
4. **Major news**: "Queen Elizabeth II has died" - 2,827 points

{/* trunk-ignore-end(vale/error) */}

### Movies dataset (41K movies with embeddings)

Rich movie data with titles, overviews, and pre-computed embeddings for
similarity search:

```text
Find movies similar to "Toy Story" using semantic search
```

**Dataset includes:**

* Movie titles and plot overviews
* 512-dimensional embeddings for semantic similarity
* Popular films from Toy Story to modern releases

### WHO air quality dataset

Global ambient air quality measurements with PM2.5, PM10, and NO2
concentrations:

```text
Which cities have the highest air pollution levels?
```

**Features:**

* PM2.5 and PM10 particulate matter concentrations
* NO2 (nitrogen dioxide) levels
* Geographic coordinates for mapping
* Multi-year temporal data

## Setting up your data environment

### Step 1: Understand the data structure

Get familiar with the complete sample dataset structure:

```text
Give me a detailed overview of all sample datasets including row counts, key fields, and potential analysis opportunities
```

Your agent will discover:

* **NYC Taxi**: 3.2M trips with fare, location, and time data
* **Hacker News**: 3.8M posts with scores, authors, and content
* **Movies**: 41K films with embeddings for ML applications
* **Air Quality**: WHO data with pollution measurements globally

### Step 2: Create your own database (Optional)

You can create custom databases alongside the sample data:

```text
Create a new database called 'my_analytics' for custom analysis
```

### Step 3: Update agent instructions

Enhance your agent's capabilities with specific dataset knowledge:

```text
You are connected to MotherDuck with access to these verified sample datasets:

**NYC Data (sample_data.nyc.taxi)**: 3,252,717 taxi trip records from 2022
- Fields: pickup/dropoff times, locations (PULocationID/DOLocationID), fares, distances
- Great for: Time series analysis, location-based insights, revenue analysis

**Hacker News (sample_data.hn.hacker_news)**: 3,866,740 posts and comments
- Fields: title, score, author, timestamp, type (story/comment)
- Great for: Content analysis, trending topics, user behavior

**Movies (sample_data.kaggle.movies)**: 41,371 movies with embeddings
- Fields: title, overview, 512-dimensional embeddings
- Great for: Semantic similarity, recommendation systems

**WHO Air Quality (sample_data.who.ambient_air_quality)**: Global pollution data
- Fields: PM2.5/PM10/NO2 concentrations, coordinates, population
- Great for: Environmental analysis, geographic patterns

Always use the full table names with schema prefixes (e.g., sample_data.nyc.taxi).
```

## Testing analytical operations

### Test 1: Time series analysis with real data

Analyze actual taxi usage patterns:

```text
Show me NYC taxi demand by hour with average fares - what patterns do you see?
```

**Real insights from the data:**

* Clear daily patterns with rush hour peaks
* Early morning premium pricing (airport runs)
* Lowest activity 2-4 AM, highest 5-7 PM
* Weekend vs weekday patterns visible in the data

### Test 2: Content analysis

Explore Hacker News trending topics:

```text
What topics generate the highest engagement on Hacker News based on story titles and scores?
```

**Real findings:**

* Tech criticism ("Google Search Is Dying") scores highly
* Major news events (Queen Elizabeth, Musk/Twitter) get massive engagement
* Technical deep-dives ("Mechanical Watch") resonate with the community

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=58f8e879464be0c94dcd7338b1c622c9" alt="HN Analysis" width="1974" height="1586" data-path="images/connections/motherduck/hn-analysis.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2b0b341188e74ee29fced6b62dc15375 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3480107009678b1c4c9189d0eab6a0ee 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=19f3ab2ef6e29f024595e0b8b049dc59 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=06a8d477db80f341cd4cf0993810b784 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a46a0ff19ba76d590ff2162cf231bdfc 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/hn-analysis.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f3854746fb4234aa06272ce66c6f59e4 2500w" data-optimize="true" data-opv="2" />

### Test 3: Geospatial analysis potential

While location IDs need lookup tables, the data structure supports location
analysis:

```text
Analyze pickup and dropoff location patterns in the taxi data
```

### Test 4: Semantic similarity with embeddings

Leverage the pre-computed movie embeddings:

```text
Using the movie embeddings, find films similar to popular titles
```

The movies dataset includes 512-dimensional embeddings perfect for similarity
analysis and recommendation systems.

## What you can do

With your MotherDuck connection established, your agent can:

* **Perform complex analytics** on millions of records with DuckDB's speed
* **Generate business insights** from real-world datasets
* **Run time series analysis** on temporal data (taxi trips, HN posts)
* **Execute semantic search** using pre-computed embeddings
* **Analyze geographic patterns** with coordinate data
* **Process text data** from movie overviews and HN content
* **Handle big data efficiently** with columnar processing
* **Create statistical summaries** and trend analysis
* **Integrate with other tools** for comprehensive workflows

## Advanced analytical capabilities with real examples

### Window functions and analytical SQL

```text
Calculate running totals and moving averages for taxi revenue by day using the actual NYC data
```

### Text analysis on real content

```text
Analyze Hacker News story titles to identify trending topics and sentiment patterns
```

### Embeddings and similarity search

```text
Use the movie embeddings to build a recommendation system - find movies similar to "Toy Story"
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4a44cce12a4a355135ea83a338f4d0b9" alt="Movie Similarity" width="1782" height="1450" data-path="images/connections/motherduck/movie-similarity-1.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5e8804f65a89af42b4aa4e108a6a553c 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=28647fabb68d8fe809b3a39f5836e17f 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=00e3cef7370302e2184573515d3194c8 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ad6b686163dc73908f63d07cbdc9e5f8 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6a7b28a7947ca64f1c73e160969127bc 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-1.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7511bea68cd00adb158df7915f414cd7 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=feb74972a11e4ee79ebf2895f9e5e60b" alt="Movie Similarity" width="1570" height="758" data-path="images/connections/motherduck/movie-similarity-2.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f5802c9d7ff709f519775ec5da2f37c2 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ee6e83277e16caa1b65d393dcbe05aec 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=5b06786d2353ce1a223bbf49732ead65 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=30e87c7222b90b54d326531a01d0dc72 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=70a9c5b15c9945c2d3a0f6de5153a4e1 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/motherduck/movie-similarity-2.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2874c8e8b9dfd9bb12377c23c9e75766 2500w" data-optimize="true" data-opv="2" />

### Environmental data analysis

```text
Identify the most polluted cities globally using WHO air quality measurements
```

## Best practices for the sample datasets

1. **NYC Taxi Data**: Always filter by date ranges for performance; use
   appropriate aggregations for time-based analysis
2. **Hacker News**: Consider story vs comment types; use score thresholds for
   quality filtering
3. **Movies**: Leverage embeddings for similarity; combine with text analysis of
   overviews
4. **Air Quality**: Account for different measurement standards; filter by data
   quality indicators

## Sample analytical workflows with real data

### Peak demand prediction

```text
Using historical taxi patterns, predict optimal driver deployment times
```

**Real insight** The data shows 4-6 AM has highest fares but lowest volume -
perfect for premium positioning.

### Community engagement analysis

```text
Identify what content types perform best on Hacker News
```

**Real finding** Technical deep-dives and industry criticism generate highest
engagement scores.

### Environmental health correlation

```text
Correlate air quality data with population density to identify at-risk areas
```

### Content recommendation engine

```text
Build a semantic movie recommendation system using the pre-computed embeddings
```

## Advanced analytics examples

### Seasonal trend analysis

```text
Identify seasonal patterns in taxi usage and predict demand for different times of year
```

### A/B testing analysis

```text
Design and analyze A/B tests using statistical functions to determine significance of results
```

### Predictive analytics preparation

```text
Create features and prepare datasets for machine learning models to predict taxi demand or customer behavior
```

## Troubleshooting

### Common query issues with sample data

1. **Table not found errors**: Always use full schema names like
   `sample_data.nyc.taxi`
2. **Performance with large datasets**: Use `LIMIT` and appropriate `WHERE`
   clauses
3. **Memory constraints**: The taxi dataset has 3.2M rows - be mindful of result
   sizes
4. **Embedding queries**: Movie embeddings are 512-dimensional arrays - use
   appropriate similarity functions

### Query performance optimization

1. **Filter early**: NYC taxi data benefits from date/time filtering
2. **Use appropriate indexes**: MotherDuck optimizes automatically but be
   mindful of query patterns
3. **Batch large operations**: For analysis across millions of HN posts,
   consider sampling strategies

<Tip>
  The sample datasets are production-ready for analysis and perfect for learning
  advanced SQL patterns. Start with the NYC taxi data for time-series practice,
  use Hacker News for text analysis, leverage movie embeddings for ML
  applications, and explore WHO data for geospatial analysis.
</Tip>

The combination of real data scale (millions of records) with advanced DuckDB
features makes MotherDuck perfect for production-grade analytics learning and
development.

## Learn more

* [MotherDuck Documentation](https://motherduck.com/docs/)
* [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction)
* [Analytics Best Practices](https://motherduck.com/docs/guides/analytics)
* [Sample Dataset Documentation](https://motherduck.com/docs/sample-data)

<Tip>
  Combine MotherDuck with other Hypermode connections to create powerful
  data-driven workflows. For example, use Slack to share analytical insights,
  GitHub to version control your analytical queries, or Stripe to combine
  payment data with other business metrics for comprehensive reporting.
</Tip>
