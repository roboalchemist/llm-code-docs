# Source: https://docs-containers.back4app.com/docs/database-hub/connect.md

---
title: Connect to a Database
slug: docs/database-hub/connect
description: Connecting to a Database using the Database Hub allows you to have access to the connected database structure and data from inside your App in Back4app.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T14:41:34.902Z
updatedAt: 2024-03-28T21:51:51.732Z
---

# Connect to a Database

## Introduction

Connecting a Database using the [**Database Hub**](https://www.back4app.com/database) allows you to have access to the source database structure and data from inside your App in Back4app.

This ensures any new updates for schemas and/or data are immediately delivered to your App so everything is up to date at any given moment.

This is also useful when big (a.k.a. in huge) databases are available, allowing you to use its data without having to fully copy the database to your account.

## Prerequisites

:::hint{type="info"}
**In order to use or share a database, you will need:**

- An app created at Back4App
- See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
:::

## 1 - Find a Database to connect

Go to the [**Database Hub list of databases**](https://www.back4app.com/database/search) and search for any topic that interests you.

For this tutorial, will be used the [**Database of World Continents, Countries and Cities**](https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities):

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HHatr99-x3cYyR-l3VHbH_image.png)

## **2 - Connect**

Click the Connect button on the top right corner of the screen. The counter on the right side shows how many Apps are using that database at the moment:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/FeitNM0xrlCPP_T-UiAwc_image.png)

The Connect dialog will appear. Then choose to which App, from one of your already existing apps, you want to connect. The chosen App in the drop down will have access to the Database that you are connecting to.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/30APUspPPLazNk8t3dqpw_image.png)

Then, success message will appear:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/a_UNZXmNa3fBo6cOtWXsE_image.png)

## 3 - Use the data

Go to the [**Dashboard**](https://parse-dashboard.back4app.com/apps) of the App you connected. You will notice the classes from the connected Database appear in the Database Browser in the following formats:

DatabaseName\_ClassName if it is a custom class
DatabaseName\_\_ClassName if it is a Parse class

The difference is that Parse classes have two \_ between the DatabaseName and ClassName:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AOVn_U6e13TnyjC41SVkG_image.png" signedSrc size="60" width="431" height="433" position="center" caption}

From now on you can query the data of the connected classes on your code, the API Console, the GraphQL console and even make relations and pointers among your App’s classes and the connected ones.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/fRFxAtAqx73t1bO9Chqe5_image.png" signedSrc size="60" width="498" height="370" position="center" caption}

