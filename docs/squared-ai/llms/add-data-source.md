# Source: https://docs.squared.ai/guides/add-data-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding a Data Source

> How to connect and configure a business data source in AI Squared.

AI Squared allows you to integrate data from databases, warehouses, and storage systems to power downstream AI insights and business workflows.

Follow the steps below to connect your first data source.

***

## Step 1: Navigate to Data Sources

1. Go to **Sources** → **Data Sources** in the left sidebar.
2. Click **“Add Source”**.
   <img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=ef2c3a591ca26320243f0b2ca663b6bd" alt="title" data-og-width="3442" width="3442" data-og-height="1298" height="1298" data-path="images/add-data-source/01.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=8b19b864b593691ba7f57045cb819c60 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=3e997d7f7afe0f8896b00dd940edccec 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6bb9a4b412c0f01dab05be2f265f3518 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=a24deeb51b9f327445c19969b245aa8e 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6c9e1649acf8715c3b63561175b559cc 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/01.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=8aaf0a2142d71a130e833b8d9789038b 2500w" />
3. Select your connector from the available list (e.g., Snowflake, BigQuery, PostgreSQL, etc.).

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=8c37a4088a9cecc862dc7d58eae1ad1d" alt="title" data-og-width="3434" width="3434" data-og-height="1526" height="1526" data-path="images/add-data-source/02.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=98a65d594b636c063170413aed17de98 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=97b2aa5c5cc8bbe726deaea20f3a8096 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=fee22415204d0f6d9364c023213586d1 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=5b56d5a6ad4c6f11ca60df69f8819f3b 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=0062f158a48b3db7958de99ff2c9876b 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/02.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=8302ef52cb2d643e40272b884be6be6f 2500w" />

***

## Step 2: Provide Connection Details

Each data source requires standard connection credentials. These typically include:

* **Source Name** – A descriptive label for your reference.
* **Host / Server URL** – Address of the database or data warehouse.
* **Port Number** – Default or custom port for the connection.
* **Database Name** – The name of the DB you want to access.
* **Authentication Type** – Options like password-based, token, or OAuth.
* **Username & Password / Token** – Credentials for access.
* **Schema (if applicable)** – Filter down to the relevant DB schema.

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=8253b211b2784f9086672d88b74419ee" alt="title" data-og-width="3422" width="3422" data-og-height="1752" height="1752" data-path="images/add-data-source/03.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=98c3b37d6c56d13f53682ef8346dbe78 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6f029ccebb9eb9a255336c4e63f105e0 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=b96ab512937de8ae51054dc13288b0f6 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=28e16cc16dc361afbc77591b1accbcda 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6ed2358397cf008ea06766f349955d38 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/03.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6bbdb30f10e8542930f37e478f0aa02c 2500w" />

***

## Step 3: Test the Connection

Click **“Test Connection”** to validate that your source credentials are correct and the system can access the data.

> ⚠️ Common issues include invalid credentials, incorrect hostnames, or firewall rules blocking access.

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=35cb6288e105be1a238fc455f8863d03" alt="title" data-og-width="3416" width="3416" data-og-height="1752" height="1752" data-path="images/add-data-source/04.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=32149117f64d7fd5903c0f220d9e0d96 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=86b6b4cc9202aba3accf31fe08e65a1f 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6648775acc880442ef3e88dd434fbd6a 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=0dd0f709dbbc1eadfa901a09ad0adfb3 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=e186deecd0ff54ed5b95e0ad65eab18d 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/04.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=16c60623b94c9ddb3f1b25cb552c5c1c 2500w" />

***

## Step 4: Save the Source

After successful testing:

* Click **Finish** to finalize the connection.
* The source will now appear under **Data Sources** in your account.

<img src="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=6196f5777f2593a7651c1703d85cad98" alt="title" data-og-width="3430" width="3430" data-og-height="1750" height="1750" data-path="images/add-data-source/05.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=280&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=f838bc6ad0015977ef35ce709d139b13 280w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=560&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=d3b809a68b298c539839c49dee839021 560w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=840&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=592e74f4a9d85491522a8b0a56186f4d 840w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=1100&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=abfe08b447e6cf1382cd073f617282fb 1100w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=1650&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=53b497b476f9378c2255dee73a7387ad 1650w, https://mintcdn.com/multiwoven-74/0cWhN_GlAyOtF2Qi/images/add-data-source/05.png?w=2500&fit=max&auto=format&n=0cWhN_GlAyOtF2Qi&q=85&s=e1e19d1c6bf6e3351e2066b3c701b9a6 2500w" />

***

## Step 5: Next Steps — Use the Source

Once added, your data source can be used to:

* Create **Data Models** (via SQL editor, dbt, or table selector)
* Build **Syncs** to move transformed data into downstream destinations
* Enable AI apps to reference live or transformed business data

> 📘 Refer to the [Data Modeling](../data-activation/data-modelling) section to begin querying your connected source.

***

## ✅ You're All Set!

Your data source is now ready for activation. Use it to power AI pipelines, syncs, and application-level insights.
