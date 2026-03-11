# Source: https://docs-containers.back4app.com/docs/local-development/parse-server-local.md

---
title: Local environment
slug: docs/local-development/parse-server-local
description: In this guide you will learn how to setup your development environment for Parse.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-01-25T15:38:19.203Z
updatedAt: 2025-01-27T19:44:50.936Z
---

The Back4app local development environment allows you to build and test apps locally using its core features, such as Database, Cloud Functions, Files, Authentication, and Web Hosting. This setup consists of the open-source Parse Server, Parse Dashboard, and a locally installed database, enabling you to prototype and iterate quickly.

This setup is ideal for prototyping, development, and continuous integration workflows.

## Goal

Set up a local development environment with Back4app.

For a more detailed explanation, you can watch the tutorial video:
[**Back4app Local Setup Guide.**](https://www.youtube.com/watch?v=Zy8k-B6FLzY)

## **1 - Connect Your Local Machine to Back4app Servers Using the CLI**

Follow the steps to connect an existing app to your local machine or create a new one.
See the CLI guide: [**Parse CLI Documentation**](https://www.back4app.com/docs/local-development/parse-cli)&#x20;

## **2 - Install and Run the Parse Server**

The easiest way to install Parse Server locally is by using NPM. Run the following command in your terminal:

:::BlockQuote
npm install -g parse-server mongodb-runner
:::

After installation, start the database so Parse Server can store data:

:::BlockQuote
mongodb-runner start
:::

Go to your Back4app dashboard and copy the APPLICATION\_ID, CLIENT\_KEY, and MASTER\_KEY from **Dashboard > App Settings > Security & Keys**. Use these values to start your Parse Server:

:::BlockQuote
parse-server --appId APPLICATION\_ID --clientKey CLIENT\_KEY --masterKey MASTER\_KEY --databaseURI mongodb://localhost/test
:::

## **3- Install Parse Dashboard**

To improve your development experience, install the Parse Dashboard for a user-friendly interface:

:::BlockQuote
npm install -g parse-dashboard
:::

Use the same credentials from the previous step and run the following command to start the dashboard:

:::BlockQuote
parse-dashboard --dev --appId APPLICATION\_ID --masterKey MASTER\_KEY --serverURL http\://localhost:1337/parse --appName MY\_APP
:::

If the Parse Dashboard fails to load, replace the URL `http://0.0.0.0:4040/` with `http://localhost:4040/`.

## 4 - Updating the Server URL

By default, the main server URL for Back4app is `https://parseapi.back4app.com`. However, for your local instance, you need to update your app's code to point to `http://localhost:1337/parse`.

## Troubleshooting

- **Common Dashboard Errors**: If you cannot access the Parse Dashboard locally, ensure you are using the correct localhost URL.
- **Database Issues**: Ensure the `mongodb-runner` service is running properly before starting the Parse Server.


Conclusion
----------

With your local Parse Server and Parse Dashboard set up, you now have a fully functional environment for developing and testing your Back4app applications. This local setup allows you to prototype new features, debug issues, and create apps faster without relying on a live environment.
