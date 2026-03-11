# Source: https://docs.xano.com/the-database/database-basics/relationships.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Relationships

> Database Relationships are used to define related data between one or more tables.

<Info>
  **Quick Definition**

  Database relationships show how different tables of data connect to each other - like how a customer's ID links their personal information to their complete order history. These relationships can be one-to-one (one person, one social security number), one-to-many (one customer, many orders), or many-to-many (many students can take many classes).
</Info>

## 🧑‍🤝‍🧑 Types of Relationships

In Xano, there are three primary ways tables can be related:

#### 1. One-to-One

This is like a person and their unique passport. Each data entry in one table relates to exactly one entry in another table.

#### 2. One-to-Many

Think of a parent and their children. A single entry in one table can relate to multiple entries in another. For example, one teacher can teach many students.

#### 3. Many-to-Many

Similar to students enrolling in various courses, any entry in one table can relate to multiple entries in another.

***

## ❓ Why Use Relationships?

* **Data Consistency**: Ensures all references are valid.

* **Reduced Redundancy**: Minimizes repeated data.

* **Efficient Data Retrieval**: Makes it easier to access related data.

Understanding these basic concepts can simplify how you view databases and highlight why tools like Xano are powerful for managing data.

***

## 👀 Using the Table Reference Field Type

When you add a table reference field to a database table, that field simply stores the IDs of the record(s) being referenced; the data is not actually duplicated. To access the actual data is typically done via an add-on as part of a function stack.

### Auto-Complete

Auto-Complete allows you to configure how the referenced records look inside of other tables.

For this example, we have two tables: `user` and `userRole`

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/230e7f34-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=804b4593ef8082618d0a6ac65bb91f6b" width="1451" height="685" data-path="images/230e7f34-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/492706ec-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=1ccba243947a619a96a029e80856da46" width="1813" height="433" data-path="images/492706ec-image.jpeg" />
</Frame>

<Frame>
  <iframe src="https://demo.arcade.software/RWmuIhxQkGk0OoOiBCdD?embed" title="https://demo.arcade.software/RWmuIhxQkGk0OoOiBCdD?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Navigate to the table you are referencing data from to adjust the Auto-Complete settings." />

  <Step title="Click the ⋮ icon and choose Auto-Complete" />

  <Step title="Click 'Customize' if this is your first time enabling Auto-Complete customization on this table." />

  <Step title="Click 'Add Column' to add a new field that will appear on tables that reference this one." />
</Steps>


Built with [Mintlify](https://mintlify.com).