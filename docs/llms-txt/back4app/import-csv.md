# Source: https://docs-containers.back4app.com/docs/parse-dashboard/core/import-csv.md

---
title: Importing CSV File
slug: docs/parse-dashboard/core/import-csv
description: Learn how to seamlessly import CSV files into Parse tables using Back4App with our comprehensive guide. This document provides step-by-step instructions, from setting up your Back4App application and creating a new class for your data to formatting your C
createdAt: 2025-01-17T18:18:58.474Z
updatedAt: 2025-01-27T20:04:15.822Z
---

## Introduction

Importing CSV files allow users to import data easily into Parse tables.

## Prerequisites

:::hint{type="info"}
**To begin with this tutorial, you will need:**

- An app created at Back4App.
  - See the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
:::

## 1 - Create a New Back4App App

First of all, it’s necessary to make sure that you have an existing app created at Back4App. However, if you are a new user, you can check [**this tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create one.

## 2 - Create a Class for importing data

In your newly created App, go to the Database Browser and click the Create a class button

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MIuWuylAQjxa-xjLXkykN_image.png" size="50" width="448" height="579" position="center" caption}

Choose to create a Custom class and give it a name. I called mine TestClass but you can call yours anything you like.
Remember that by convention classes start with an Uppercase letter, are CamelCase and does not contain special characters such as spaces and symbols.
Click Create class when you’re done.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/xzqZee4RmhJgZo1hoGClT_image.png" size="60" width="988" height="826" position="center" caption}

## 3 - Creating the CSV file

The CSV file must be in the correct format in order to be imported.

**Correct format parameters**:

Separation character must be a comma , and NOT a semicolon ;.


Adjust your Spreadsheet software to output commas as separation characters


First line will be the Column Names


Parse will automatically convert `Strings`, `Numbers` and `Booleans`


Dates must have two columns: `date.__typespecifies` the Date type, `date.isospecifies` the Date Format


GeoPoints must have three columns: `columnName.__typespecifies` the Geopoint type,
`columnName.latitudespecifies` the Latitude, `columnName.longitudespecifies` the Longitude.


Arrays are passed in double quotes


Pointers require three columns: `columnName.__typespecifies` the Pointer type, `columnName.classNamespecifies` the target class, `columnName.objectIdspecifies` the objectId of the target class

So, for your reference, a few examples:

Three columns: columnStringA will hold strings, columnStringB will also hold strings, columnNumberC will hold numbers

columnStringA,columnStringB,columnNumberC
stringA,StringB,12
stringA2,StringB2,13

Two columns: columnStringA will hold strings, columnBooleanB will hold Booleans

columnStringA,columnBooleanB
stringA,TRUE
stringA2,FALSE

Two columns: columnStringA and columnStringB will hold strings, columnArrayC will hold arrays

columnStringA,colmnStringB,columnArrayC
"stringA, with, commas",stringB,`"[1,2,3]"`
stringA2,"stringB, with, commas",`"["A", "B", "C"]"`

Two columns: columnStringA will hold strings, second column will hold a date in the ISO format

columnStringA,`date.__type`,`date.iso`
stringA,Date,2020-01-16
stringA2,Date,2020-01-17

Two columns: columnStringA will hold strings, second column will hold a GeoPoint

columnStringA,`geo.__type`,`geo.latitude`,`geo.longitude`
stringA,GeoPoint,1,2
stringA2,GeoPoint,-5,-6

You can find a sample CSV file for download here:

[**Download it here**](https://www.back4app.com/docs/assets/downloads/SampleCSVFile.csv)

For Pointers, please check the example below:

One column: holding a Pointer

`team.__type`,team.className,team.objectId
Pointer,Team,XWDSM4xxQ8
Pointer,Team,CD9nAlDaEG
Pointer,Team,kRGJPuZyXD

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/uE9mTlnoAR6UhMO1R2lwa_image.png" size="50" width="410" height="96" position="center" caption}

In this example, please consider that objectId correspond to the existing ones at the Team class.

Check the sample CSV file for download:

[**Download it here**](https://www.back4app.com/docs/assets/downloads/import-pointer-csv.csv)

## 4 - Importing the Data

With your newly created class selected in the Database Browser, on the top right corner of the screen, click the Notes button and select Import data

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/N3EnnPmrRItGfbN5Hz4_3_image.png" size="50" width="414" height="619" position="center" caption}

Click the Upload a file button, choose your CSV file and click the Import button

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/VakvVAlB0vKaCmJe6aWfA_image.png)

## 5 - Wait for an eMail confirmation

As CSV files can get quite big, an asynchronous operation is fired to import your data in background, which means you will not see any progress of importing nor success message.
At the end of the operation you will receive an email message either telling the operation was successful and your data was imported, or telling the operation wasn’t successful and explaining which columns/lines failed.

If you try to refresh your dashboard before receiving this email, you might see missing data or even no data at all, as the operation is still ongoing.

Once you get the email and if your import was successful, we recommend hard refreshing your browser (CMD + Shift + R on a Mac, CTRL + Shift + R in Windows, both for Chrome) to ensure the new schemas are retrieved and your data displays properly.

