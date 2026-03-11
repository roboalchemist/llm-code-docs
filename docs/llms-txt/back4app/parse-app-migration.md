# Source: https://docs-containers.back4app.com/docs/app-migration/parse-app-migration.md

---
title: Parse Migration
slug: docs/app-migration/parse-app-migration
description: In this guide you will learn the steps to migrate to Back4App.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-26T12:54:13.757Z
updatedAt: 2025-01-17T14:25:52.958Z
---

# How can I migrate my Parse Server App to Back4App?

## Introduction

In this guide, you will learn how to migrate an existing Parse App to Back4App. Before moving your App, you’ll see how to test your Database, files, and cloud functions running on Back4App servers. Once validated, you will be ready to finish the migration and start using Back4App as your Parse provider. If you prefer to migrate using the CLI migration tool, please check [**this guide**](https://www.back4app.com/docs/app-migration/parse-cli-migration).

## Goal

Migrate a Parse App to Back4App servers.

## 1 - Create a New Back4App App

The first step is to create a Back4App App where you will migrate your current App. Check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Connect Back4App to your current Database

Go to the database section of your current hosting account’s control panel and copy your [**connection string**](https://docs.mongodb.com/manual/reference/connection-string/#standard-connection-string-format). Now you’ll use it to connect the Back4App Parse Server with your existing Database.

Open your Back4App Dashboard, go to the Server Settings > Core Settings > Settings, and then scroll to the bottom of the page to spot shown in the image:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_xNP4IArhoUyHEnby2U0-_image.png" signedSrc size="70" width="450" height="290" position="center" caption}

Next, click on the button Edit details, go to the Connection String, and click on the Change database URI link. By doing so, you will be able to update the connection string with the new copied value.

## 3 - Upload your Cloud Code

If your App has Cloud Code files, you will need to deploy them on Back4App to ensure that all the files are working correctly.

You can deploy your Cloud Code files in batch using the Back4App CLI ([**Command Line Interface**](https://www.back4app.com/docs/command-line-tool/parse-server-setup)) tool or manually using the Dashboard under Cloud Code Functions.

After uploading them, you can check the logs available at Server Settings > Logs > Settings > Server System Log.

## 4 - Migrate your Parse Files

If your App has files (images, documents, videos), you’ll need to migrate them to the Back4App (we are using Amazon AWS S3 as file storage). The process of migrating your files is manual. You should compact all the objects into a zip file or within your S3 bucket and contact us (at community\@back4app.com) to help you deploy them on Back4App servers.

:::hint{type="warning"}
**Note**: If you have files saved directly on the database please, let us know. The process is different in this case.
:::

## 5 - Updating your frontend

Now, you need to test if all your App features are working when connected to Back4App servers. Go to your frontend code and update your App keys and server URL of your App. Test all your app features to make sure that the migration has worked. You can now release a new App version to your users.

In this scenario, you will have two versions of your App: a new one with Back4App and the old one that uses your previous Parse hosting.

- The non-updated users will still be pointing to your “old” API;
- The updated users will be pointing to Back4app API;

You have to choose the best time to finish the migration and move your Database definitely to Back4App.

## 6 - To finish the process

It’s time to migrate your Database. We recommend proceeding with this step after making sure most of your users are using your Back4App App version and successfully concluding all the previous migration steps.

Now you can migrate the Database by yourself using the Back4App migration CLI or open a ticket on our [**support channel**](https://www.back4app.com/support), so we can do it for you.

If you decide to open a ticket, please provide your previous Parse hosting connection string and your Back4App App ID.

## It’s done!

With the guide described above, you’ll be able to migrate your Parse App to the Back4App and work with our various full-fledged, excellent features!

In case you need any help or a link doesn’t work, please [**contact our team via chat**](https://www.back4app.com/support)!
