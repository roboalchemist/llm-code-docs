# Source: https://docs-containers.back4app.com/docs/app-migration/parse-cli-migration.md

---
title: CLI Migration
slug: docs/app-migration/parse-cli-migration
description: In this guide you will learn the steps to migrate to Back4App.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-26T12:59:08.613Z
updatedAt: 2025-01-17T01:09:50.920Z
---

# Migrate your Parse App to Back4App using CLI

## Introduction

In this guide, you will learn how to migrate your Parse App to Back4App using the migration CLI.

The migration process consists of transferring the Database, cloud functions, and files from your current Parse App to a Back4App App. The CLI migration tool will help you with the Database and files migration.&#x20;

It will pick a copy of your database (a dump file) and restore the data in your Back4App App. Then will pick your files from a local folder and upload them to Back4App S3 Bucket. The Cloud Code migration is not covered for this CLI migration tool but you can use the [**Back4App CLI**](https://www.back4app.com/docs/platform/parse-cli) (other CLI) to migrate them or do it manually using the Dashboard.

## Prerequisites

:::hint{type="info"}
**To begin with this tutorial, you will need:**

- A dump of your Parse App in your own machine.
- [**Node JS (>=8.0)&#x20;**](https://nodejs.org/en/)and [**NPM**](https://docs.npmjs.com/getting-started).
:::

## 1 - Install our CLI Tool

First of all, it’s necessary to install @back4app/m2b4a on your machine. As described below:

:::BlockQuote
npm install -g @back4app/m2b4a
:::

## 2 - Start the Parse App Migration

You will now migrate your Database. Go to your current Parse App and download a copy of your Database. Then go to the folder that contains your dump files and run:

:::BlockQuote
migrate-to-back4app
:::

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VpC-RFB0Yx7swgG1uDUWg_image.png)

## 3 - Access your Account

You can sign up or log in to your account and choose if you want to save your session. Then, the next time you use this tool you won’t need to put your account credentials again.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/zpsCrjT1ppBqkmStGbOuu_image.png)

## 4 - Choose a Back4App App

You can migrate your Parse App to an existing app or a new one.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/aERuzGAQUZI3LUBqZ9ux3_image.png)

If you decide to use an existing app, be careful, it’s possible to decide if you’ll overwrite the existing data or just insert new objects.

For new apps, you must set a name and press ENTER.

## 5 - Restore your data

Once you’re already in the folder where your dump files are, you just need to press ENTER.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/zvjxl4vEjtSsmoW2XO2O3_image.png)

## 6 - Migrate your Parse Files

In case you have Parse Files, browse in the folder where your files are, and press ENTER to continue. The files will be automatically associated with your Parse Objects.

Otherwise, just type n to skip this step and start the restoration process.

Here’s what the end of the migration will look like:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/W-sLU5PGCZ2RCPlEDFhEe_image.png)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/CWc_z5WYj6PX87rFGP2Eb_image.png)

:::hint{type="danger"}
Never share these credentials to anyone. You can [**add collaborators**](https://help.back4app.com/hc/en-us/articles/115000808951-How-to-add-Collaborators-to-my-app-) in your project and they can get these keys [**here**](https://help.back4app.com/hc/en-us/articles/115000754772-Where-are-my-Keys-and-ID-).
:::

## 7 - Test your cloud code

Check [**this guide**](https://www.back4app.com/docs/platform/parse-cli) to learn how to deploy your cloud code files.

Here are some pieces of information you must know:

1 - Back4App uses 2 main folders: public/ to public files, like HTML, CSS, etc., and cloud/ to private cloud code.

2 - Inside cloud/ Back4App import 2 files. One named app.js for your custom API (app.get(‘/my-custom-api’) for ex.) and main.js for Parse.Cloud functions and jobs.

3 - **VERY IMPORTANT!** app (the express.js instance) and Parse variables are global. **Do not install them** on your package.json or require them in your cloud code.

4 - **Do not use&#x20;**&#x72;equire('express')**&#x20;or&#x20;**&#x72;equire('parse/node')**, just use app and Parse variables**.

## 8 - Connect your current API to your new database at Back4App

Once you finished all App tests, it’s time to point your current Parse Server to use the Back4App Database. You have two possibilities here. The first is to point the Parse Server to the Back4App Database and then make an incremental Database restore (as described in **Step 5**). The second is to turn off your Parse Server, make a complete database restore, and then turn it on again, pointing to the Back4App Database. Our suggestion here is the first step, which will avoid downtime to your App.

To proceed with the first option, copy your Back4App Connection String at Server Settings > Settings > Core Settings > Connection String and paste it into your old Parse App settings.

Now you need to make a new dump of your data and restore them in your application **(step 5)**, but, instead of creating a new app, choose YES, I want to update one of them! and NO! Only insert new ids, afterward. It will help to prevent data inconsistency for your users.

After concluding this step, your users will be using the Back4App Database instead of the old one.

## 9 - Updating your frontend

Now, you need to update your front end to connect to the Back4App App. You can get your app ID, keys, and API Address in the core settings section at Server Settings > Settings > Core Settings. Update your frontend/App connection (pointing to Back4App now) and release a new application version to your users.

Now you have a new app pointing to the Back4App API and database and an old app pointing to the previous Parse API but using the Back4App database.

## 10 - Finishing the process

We recommend only turning off your old Parse API when most of your users are using the new App version (pointing to Back4App API). Once you turn off the old API, users who use the old version will lose access to the backend.

## It’s done!

Now you know how to migrate your Parse App to the Back4App using the CLI. In case you need any help or a link doesn’t work, please [**contact our team!**](https://www.back4app.com/support)
