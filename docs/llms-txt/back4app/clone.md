# Source: https://docs-containers.back4app.com/docs/database-hub/clone.md

---
title: Clone a database
slug: docs/database-hub/clone
description: Cloning a Database using the Database Hub allows you to have a fully working snapshot to the shared database in Back4app.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-27T14:45:53.429Z
updatedAt: 2025-01-15T19:36:27.463Z
---

# Clone a Database

## Introduction

Cloning a Database using the [**Database Hub**](https://www.back4app.com/database) allows you to have a full copy of schemas and data cloned, delivered to your Back4app account.

Updates in the original datasource will NOT be delivered to your database, and updates you do will NOT be reflected to the source database.

This is useful when you want a copy of the database to manage the way you prefer.

## Prerequisites

:::hint{type="info"}
**In order to use or share a database, you will need:**

- An account created at Back4App.
:::

## 1 - Find a Database to clone

You can go to the [**Database Hub list of databases**](https://www.back4app.com/database/search) and search for any topic that interests you.

For this tutorial, will be used the [**Database of Car Models, Manufacturer, Category and Year**](https://www.back4app.com/database/back4app/car-make-model-dataset):

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Dwj88OqA2u79yf4iRNHmK_image.png)

## 2 - Clone

Click the Clone button on the top right corner of the screen. The counter on the right side shows how many Apps have cloned that database at the moment:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/tku75frvZHaMJna4JjwFY_image.png)

The Clone dialog will appear. Then choose a name for your cloned App.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vMZiSvM5kofuCoC0Wt_-q_image.png)

Then, a success message will appear:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wIphh1afIlteRIVJ4Sp-2_image.png)

## **&#x20;3 - Use the data**

Once cloned, go to the [**Dashboard**](https://parse-dashboard.back4app.com/apps) for your newly created App.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dpVjdQPyDBgCsRtA4eXNs_image.png" signedSrc size="50" width="587" height="709" position="center" caption}

From now on you can query the data of the cloned App.
