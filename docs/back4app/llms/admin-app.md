# Source: https://docs-containers.back4app.com/docs/parse-dashboard/admin-app.md

---
title: Admin App
slug: docs/parse-dashboard/admin-app
description: Identify how many people are installing your app, how many are signing up to your platform per day, week or month over time.
image: https://www.back4app.com/_public/img/back4app-og.png
createdAt: 2024-02-06T14:02:36.985Z
updatedAt: 2025-01-27T20:04:22.055Z
---

# Admin App

## Introduction

The Admin App is a real-time administration panel without touching the code, it is readable of developers and even non-technical users at all levels.

By using this feature, you are allowing a non-tech user to perform an operation on a database resource and also manage your data.

In this guide, we are going to learn to enable and add some customizations to the Admin interface.

## Prerequisites

:::hint{type="info"}
**There are no pre-requisites to read or edit this page.**
:::

## **How to enable it?**

This video will efficiently walk you through the process to enable this interface:

::embed[]{url="https://www.youtube.com/watch?embeds_referring_euri=https%3A%2F%2Fwww.back4app.com%2F&source_ve_path=Mjg2NjQsMTY0NTAz&feature=emb_share&v=7CHdIniAACE"}

## Frequently Asked Question

Below you’ll find answer to the questions we get asked the most about Admin App.

::::ExpandableHeading
### **How to customize the Admin App's layout?**

Go to Dashboard > Core > Click at B4aSetting class and you might see something like below:

![](https://www.back4app.com/docs/assets/images/png/parse-dashboard/admin-classes.png)

:::hint{type="warning"}
Is one of these keys missing? Don’t worry, you can add a new row and insert the key and value.
:::

In order to prevent any typo error, you can copy and paste them below:

- isHomeHidden

This property will hide the “Home” section of your Admin app.

Type: Boolean Value: *true* or *false*.

- isFeedbackHidden

This property will hide the “Feedback button”.

Type: Boolean Value: *true* or *false*.

- isSupportButtonHidden

This property will hide the “Support button”.

Type: Boolean Value: *true* or *false*.

- customizeDefaultFields

This property will allow you to hide default fields as “Id”, “Created At” and “Updated At” columns.

Type: Boolean Value: *true* or *false*.

- logo

This property will allow you to change the default logo from Admin.

Type: String Value: Insert a URL of your logo.

- brandColor

This property will allow you to the admin’s column by using hexadecimal colors or its name.

Type: String Value: Type “#800080” or write “purple”.

- appName

This property will change the name of the app on Admin only.

Type: String
::::

:::ExpandableHeading
### **How to change the columns' order?**

Go to the Admin App > Custom Field at Admin App Setting.

You’ll see a populated class, but, you don’t need to worry, these registers help the admin’s ordenation, let’s keep focused to our original need.

Click to add a new register (+Add), it’s the green button at the top. The following window will appear:

::Image[]{src="https://www.back4app.com/docs/assets/images/png/parse-dashboard/admin-custom-field-object.png" size="90" width="1165" height="762" position="center" caption}

In order to move the column, please fill the following fields:

- ***Class*** - Select the class that you would like to change the ordination.
- ***Field&#x20;***- Select the column
- ***Title&#x20;***- Type the column name (To change the column name in the admin app, write a different value)
- ***Relevance*** - You need to know that it’s set as ascending order, so, fieldset with the higher relevance number will be on the left.

Now, you need to click on the Save button.
:::

:::ExpandableHeading
### **How to hide a column?**

Go to the Admin App > Custom Field at Admin App Setting.

Click to add a new register (+Add), it’s the green button at the top. The following window will appear:

::Image[]{src="https://www.back4app.com/docs/assets/images/png/parse-dashboard/admin-custom-field-object.png" size="90" width="1165" height="762" position="center" caption}

In order to move the column, please fill the following fields:

- ***Class*** - Select the class that you would like to hide the column.
- ***Field &#x20;***- Select the column that you would like to hide.
- ***Title&#x20;***- Retype the column name
- ***Is Table Hidden&#x20;****-  Select&#x20;*&#x59;E&#x53;*&#x20;option.*
- ***Relevance&#x20;***- Set as 0.

Now, you need to click on the Save button.
:::

:::ExpandableHeading
### **How to add more than one user?**

Go to Dashboard > Core > Click at Role class. You’ll see a Role called B4aAdminUser, which was automatically created when the Admin app was enabled.

Click on the users relation and you’ll see the following buttons:

- *Create a \_User and attach*

By choosing this option, you need to put the username and set a password.

- *Attach existing rows from \_User*

In this option, you can allow an existing user to access your Admin too. By clicking on this button, you must choose the user (object Id) that you want to add on the Admin.
:::

:::ExpandableHeading
### **How to reset the admin user password?**

Go to Dashboard > Core > Click at Role class, search for the Role “B4aAdminUser”, and click at View relation on its relation to the User class. Go to the password field and click on it to insert a new password to your admin user.


:::

