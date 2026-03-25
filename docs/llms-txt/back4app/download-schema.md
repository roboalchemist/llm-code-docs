# Source: https://docs-containers.back4app.com/docs/react-native/graphql/download-schema.md

---
title: Download Schema
slug: docs/react-native/graphql/download-schema
description: In this guide you will learn how to get the schema file and place it on you react native project.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T18:33:31.444Z
updatedAt: 2024-03-29T01:40:41.027Z
---

# Download the GraphQL Schema

## Introduction

In our previous guide we’ve learned more about the amazing GraphQL client: Relay. Now it’s time to understand how you can use Relay to fetch data from Back4App in order to use it on your React Native App. In this guide you will learn how to download the GraphQL schema file and place it on your react native project.

## Goal

To prepare your React Native project to use Back4App GraphQL API by downloading the schema.

## Prerequisites

:::hint{type="info"}
**This is not a tutorial yet, but to feel free confortable reading it you will need:**

- Basic JavaScript knowledge.
- Basic understand about GraphQL. If you don’t have, the [**GraphQL.js**](https://github.com/graphql/graphql-js) its a perfect place to start
- A React Native basic project running on your local environment.
:::

## 1 - Downloading the Schema

The schema is your source of truth from the server that will be located on your frontend. On Back4App the schema is an automatic file generated once you define your data model. To better understand the Back4App GraphQL schema you can open it on GraphQL console by doing the following steps:

- **go to your app Back4App dashboard;**
- **On the left menu, click on API Console, under the Core tab;**
- **Choose GraphQL and you will see something like this:**

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/KdHtTFz1mPU1egcwkRRPY_image.png" signedSrc size="50" width="301" height="381" position="center" caption}

Welcome to GraphQL playground. Here you can write and run queries, mutations using SDL language.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/McqyWZu540CO0FabPC8Ej_image.png)

On the top-right side you will see two tabs: DOCS and SCHEMA. On the DOCS tab you will find an easy to read documentation of the GraphQL API. The documentation is based on the object types that are generated once you build your data model on Back4App. For devs this is awesome because it can be used as a quick reference to build your query and mutations.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4UuV6znwUAYhlGGwU_pzH_image.png" signedSrc size="70" width="333" height="816" position="center" caption}

Back4App also also generates a specification to your GraphQL API: the popular known schema. The schema is found on the SCHEMA tab and is written using SDL(Schema Definition Language). The schema will be used as a source of truth on your frontend.

Go ahead, click over the SDL download and get the file to use on the next step.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/QK48B1doTZ_y9nABX-iD8_image.png" signedSrc size="70" width="350" height="816" position="center" caption}

## 2 - Pasting the Schema on React Native App

In order Relay can read the schema file on the React Native app you need to paste the schema file on a specific path. Let’s make this on your React Native project:

- Create a folder on your application root path and name it data.
- Paste the schema file (SDL) file on this folder

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/KKTHuylEAYseoozmu_dwp_image.png" signedSrc size="50" width="219" height="522" position="center" caption}

Done. Your frontend already has the source of truth from your backend with your GraphQL schema. The final configuration is shown below.

:::hint{type="danger"}
Important: Every time you change your data model on Back4App your schema file will change. It is very important to keep the schema file always UPDATED on your front-end so every time you change the schema you need to upload it again on your React Native App project
:::

## Conclusion

With the schema already placed on your react native application, now you will learn how to configure and prepare your environment to be able to fetch your components queries.
