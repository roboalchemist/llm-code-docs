# Source: https://docs.xano.com/the-database/database-basics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Basics

> In this section, you'll learn about the basic concepts of what a database is, and how it works.

<Info>
  **Quick Definition**

  A database is a structured collection of information that's organized so you can easily access, manage, and update it - like a super-powered digital filing cabinet that can instantly find and sort your data.
</Info>

### What is a database?

Think of your database like a digital version of a filing cabinet that holds every piece of data your backend needs to run. Just as you organize papers in folders and drawers, a database organizes digital information in an organized way. This can include anything you need, such as...

* User account information (names, emails, passwords)
* Product information (names, prices, descriptions)
* Complex data structures, such as AI vectors, images/videos, and more

Your **database** is comprised of a few different components, detailed below.

### Database Tables

A table can be thought of like a drawer in your filing cabinet that is only meant to hold a certain type of information. You could have a separate drawer for users, products, and stores. Each table in Xano is comprised of a collection of **database records**.

### Database Records

Each table is comprised of 'records', which you can think of as individual folders inside of that drawer. Each folder contains all of the relevant data for that record. If we were looking at a drawer that held our user data, each folder might contain information like their name, email address, password, or physical location. These separate pieces of data are our **database fields**.

### Database Fields

Each record will have pieces of data separated into fields, or columns (the terms can be used interchangeably). A database field has at least a name to signal what is contained in that field, and a data type associated with it that dictates what can be stored in that field.

Xano offers several different data types that you can use, and you can review those [here](/the-database/database-basics/field-types), but for now, we'll focus on some of the more basic ones to get you started.

* **text** - Can hold any form of text, sometimes referred to as a string
* **integer** - Any number that does not include a decimal point
* **boolean** - A true or false value

<Card href="/the-database/database-basics/field-types">
  Field Types
</Card>

### How is data added to a database table?

Typically, your data comes from one of the following sources:

* Manually entering data in the database view
* User submitted data that is sent to your Xano APIs from your frontend
* A third party service, sending data to or being called from your Xano function stacks
* Imports from CSV files, other database platforms, or a direct database connection


Built with [Mintlify](https://mintlify.com).