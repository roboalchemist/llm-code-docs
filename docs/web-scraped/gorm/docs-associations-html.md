# Source: https://gorm.io/docs/associations.html

Title: Associations

URL Source: https://gorm.io/docs/associations.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
Associations | GORM - The fantastic ORM library for Golang, aims to be developer friendly.
===============

[![Image 1: GORM](https://gorm.io/gorm.svg)](https://gorm.io/)
==============================================================

[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)

English 

[](https://gorm.io/docs/associations.html)

Associations
============

[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/associations.md "Improve this page")

[](https://gorm.io/docs/associations.html#Auto-Create-Update "Auto Create/Update")Auto Create/Update[](https://gorm.io/docs/associations.html#Auto-Create-Update)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM automates the saving of associations and their references when creating or updating records, using an upsert technique that primarily updates foreign key references for existing associations.

### [](https://gorm.io/docs/associations.html#Auto-Saving-Associations-on-Create "Auto-Saving Associations on Create")Auto-Saving Associations on Create[](https://gorm.io/docs/associations.html#Auto-Saving-Associations-on-Create)

When you create a new record, GORM will automatically save its associated data. This includes inserting data into related tables and managing foreign key references.

user := User{

 Name: "jinzhu",

 BillingAddress: Address{Address1: "Billing Address - Address 1"},

 ShippingAddress: Address{Address1: "Shipping Address - Address 1"},

 Emails: []Email{

 {Email: "jinzhu@example.com"},

 {Email: "jinzhu-2@example.com"},

 },

 Languages: []Language{

 {Name: "ZH"},

 {Name: "EN"},

 },

}

// Creating a user along with its associated addresses, emails, and languages

db.Create(&user)

// BEGIN TRANSACTION;

// INSERT INTO "addresses" (address1) VALUES ("Billing Address - Address 1"), ("Shipping Address - Address 1") ON DUPLICATE KEY DO NOTHING;

// INSERT INTO "users" (name,billing_address_id,shipping_address_id) VALUES ("jinzhu", 1, 2);

// INSERT INTO "emails" (user_id,email) VALUES (111, "jinzhu@example.com"), (111, "jinzhu-2@example.com") ON DUPLICATE KEY DO NOTHING;

// INSERT INTO "languages" ("name") VALUES ('ZH'), ('EN') ON DUPLICATE KEY DO NOTHING;

// INSERT INTO "user_languages" ("user_id","language_id") VALUES (111, 1), (111, 2) ON DUPLICATE KEY DO NOTHING;

// COMMIT;

db.Save(&user)

### [](https://gorm.io/docs/associations.html#Updating-Associations-with-FullSaveAssociations "Updating Associations with FullSaveAssociations")Updating Associations with `FullSaveAssociations`[](https://gorm.io/docs/associations.html#Updating-Associations-with-FullSaveAssociations)

For scenarios where a full update of the associated data is required (not just the foreign key references), the `FullSaveAssociations` mode should be used.

// Update a user and fully update all its associations

db.Session(&gorm.Session{FullSaveAssociations: true}).Updates(&user)

// SQL: Fully updates addresses, users, emails tables, including existing associated records

Using `FullSaveAssociations` ensures that the entire state of the model, including all its associations, is reflected in the database, maintaining data integrity and consistency throughout the application.

[](https://gorm.io/docs/associations.html#Skip-Auto-Create-Update "Skip Auto Create/Update")Skip Auto Create/Update[](https://gorm.io/docs/associations.html#Skip-Auto-Create-Update)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM provides flexibility to skip automatic saving of associations during create or update operations. This can be achieved using the `Select` or `Omit` methods, which allow you to specify exactly which fields or associations should be included or excluded in the operation.

### [](https://gorm.io/docs/associations.html#Using-Select-to-Include-Specific-Fields "Using Select to Include Specific Fields")Using `Select` to Include Specific Fields[](https://gorm.io/docs/associations.html#Using-Select-to-Include-Specific-Fields)

The `Select` method lets you specify which fields of the model should be saved. This means that only the selected fields will be included in the SQL operation.

user := User{

 // User and associated data

}

// Only include the 'Name' field when creating the user

db.Select("Name").Create(&user)

// SQL: INSERT INTO "users" (name) VALUES ("jinzhu");

### [](https://gorm.io/docs/associations.html#Using-Omit-to-Exclude-Fields-or-Associations "Using Omit to Exclude Fields or Associations")Using `Omit` to Exclude Fields or Associations[](https://gorm.io/docs/associations.html#Using-Omit-to-Exclude-Fields-or-Associations)

Conversely, `Omit` allows you to exclude certain fields or associations when saving a model.

// Skip creating the 'BillingAddress' when creating the user

db.Omit("BillingAddress").Create(&user)

// Skip all associations when creating the user

db.Omit(clause.Associations).Create(&user)

> **NOTE:**
> 
> For many-to-many associations, GORM upserts the associations before creating join table references. To skip this upserting, use `Omit` with the association name followed by `.*`:
> 
> 
> // Skip upserting 'Languages' associations
> 
> db.Omit("Languages.*").Create(&user)
> 
> To skip creating both the association and its references:
> 
> 
> // Skip creating 'Languages' associations and their references
> 
> db.Omit("Languages").Create(&user)

Using `Select` and `Omit`, you can fine-tune how GORM handles the creation or updating of your models, giving you control over the auto-save behavior of associations.

[](https://gorm.io/docs/associations.html#Select-Omit-Association-fields "Select/Omit Association fields")Select/Omit Association fields[](https://gorm.io/docs/associations.html#Select-Omit-Association-fields)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In GORM, when creating or updating records, you can use the `Select` and `Omit` methods to specifically include or exclude certain fields of an associated model.

With `Select`, you can specify which fields of an associated model should be included when saving the primary model. This is particularly useful for selectively saving parts of an association.

Conversely, `Omit` lets you exclude certain fields of an associated model from being saved. This can be useful when you want to prevent specific parts of an association from being persisted.

user := User{

 Name: "jinzhu",

 BillingAddress: Address{Address1: "Billing Address - Address 1", Address2: "addr2"},

 ShippingAddress: Address{Address1: "Shipping Address - Address 1", Address2: "addr2"},

}

// Create user and his BillingAddress, ShippingAddress, including only specified fields of BillingAddress

db.Select("BillingAddress.Address1", "BillingAddress.Address2").Create(&user)

// SQL: Creates user and BillingAddress with only 'Address1' and 'Address2' fields

// Create user and his BillingAddress, ShippingAddress, excluding specific fields of BillingAddress

db.Omit("BillingAddress.Address2", "BillingAddress.CreatedAt").Create(&user)

// SQL: Creates user and BillingAddress, omitting 'Address2' and 'CreatedAt' fields

[](https://gorm.io/docs/associations.html#Delete-Associations "Delete Associations")Delete Associations[](https://gorm.io/docs/associations.html#Delete-Associations)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

GORM allows for the deletion of specific associated relationships (has one, has many, many2many) using the `Select` method when deleting a primary record. This feature is particularly useful for maintaining database integrity and ensuring related data is appropriately managed upon deletion.

You can specify which associations should be deleted along with the primary record by using `Select`.

// Delete a user's account when deleting the user

db.Select("Account").Delete(&user)

// Delete a user's Orders and CreditCards associations when deleting the user

db.Select("Orders", "CreditCards").Delete(&user)

// Delete all of a user's has one, has many, and many2many associations

db.Select(clause.Associations).Delete(&user)

// Delete each user's account when deleting multiple users

db.Select("Account").Delete(&users)

> **NOTE:**
> 
> It’s important to note that associations will be deleted only if the primary key of the deleting record is not zero. GORM uses these primary keys as conditions to delete the selected associations.
> 
> 
> // This will not work as intended
> 
> db.Select("Account").Where("name = ?", "jinzhu").Delete(&User{})
> 
> // SQL: Deletes all users with name 'jinzhu', but their accounts won't be deleted
> 
> 
> 
> // Correct way to delete a user and their account
> 
> db.Select("Account").Where("name = ?", "jinzhu").Delete(&User{ID: 1})
> 
> // SQL: Deletes the user with name 'jinzhu' and ID '1', and the user's account
> 
> 
> 
> // Deleting a user with a specific ID and their account
> 
> db.Select("Account").Delete(&User{ID: 1})
> 
> // SQL: Deletes the user with ID '1', and the user's account

[](https://gorm.io/docs/associations.html#Association-Mode "Association Mode")Association Mode[](https://gorm.io/docs/associations.html#Association-Mode)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Association Mode in GORM offers various helper methods to handle relationships between models, providing an efficient way to manage associated data.

To start Association Mode, specify the source model and the relationship’s field name. The source model must contain a primary key, and the relationship’s field name should match an existing association.

var user User

db.Model(&user).Association("Languages")

// Check for errors

error := db.Model(&user).Association("Languages").Error

### [](https://gorm.io/docs/associations.html#Finding-Associations "Finding Associations")Finding Associations[](https://gorm.io/docs/associations.html#Finding-Associations)

Retrieve associated records with or without additional conditions.

// Simple find

db.Model(&user).Association("Languages").Find(&languages)

// Find with conditions

codes := []string{"zh-CN", "en-US", "ja-JP"}

db.Model(&user).Where("code IN ?", codes).Association("Languages").Find(&languages)

### [](https://gorm.io/docs/associations.html#Appending-Associations "Appending Associations")Appending Associations[](https://gorm.io/docs/associations.html#Appending-Associations)

Add new associations for `many to many`, `has many`, or replace the current association for `has one`, `belongs to`.

// Append new languages

db.Model(&user).Association("Languages").Append([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Append(&Language{Name: "DE"})

db.Model(&user).Association("CreditCard").Append(&CreditCard{Number: "411111111111"})

### [](https://gorm.io/docs/associations.html#Replacing-Associations "Replacing Associations")Replacing Associations[](https://gorm.io/docs/associations.html#Replacing-Associations)

Replace current associations with new ones.

// Replace existing languages

db.Model(&user).Association("Languages").Replace([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Replace(Language{Name: "DE"}, languageEN)

### [](https://gorm.io/docs/associations.html#Deleting-Associations "Deleting Associations")Deleting Associations[](https://gorm.io/docs/associations.html#Deleting-Associations)

Remove the relationship between the source and arguments, only deleting the reference.

// Delete specific languages

db.Model(&user).Association("Languages").Delete([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Delete(languageZH, languageEN)

### [](https://gorm.io/docs/associations.html#Clearing-Associations "Clearing Associations")Clearing Associations[](https://gorm.io/docs/associations.html#Clearing-Associations)

Remove all references between the source and association.

// Clear all languages

db.Model(&user).Association("Languages").Clear()

### [](https://gorm.io/docs/associations.html#Counting-Associations "Counting Associations")Counting Associations[](https://gorm.io/docs/associations.html#Counting-Associations)

Get the count of current associations, with or without conditions.

// Count all languages

db.Model(&user).Association("Languages").Count()

// Count with conditions

codes := []string{"zh-CN", "en-US", "ja-JP"}

db.Model(&user).Where("code IN ?", codes).Association("Languages").Count()

### [](https://gorm.io/docs/associations.html#Batch-Data-Handling "Batch Data Handling")Batch Data Handling[](https://gorm.io/docs/associations.html#Batch-Data-Handling)

Association Mode allows you to handle relationships for multiple records in a batch. This includes finding, appending, replacing, deleting, and counting operations for associated data.

*   **Finding Associations**: Retrieve associated data for a collection of records.

db.Model(&users).Association("Role").Find(&roles)

*   **Deleting Associations**: Remove specific associations across multiple records.

db.Model(&users).Association("Team").Delete(&userA)

*   **Counting Associations**: Get the count of associations for a batch of records.

db.Model(&users).Association("Team").Count()

*   **Appending/Replacing Associations**: Manage associations for multiple records. Note the need for matching argument lengths with the data.

var users = []User{user1, user2, user3}

// Append different teams to different users in a batch

// Append userA to user1's team, userB to user2's team, and userA, userB, userC to user3's team

db.Model(&users).Association("Team").Append(&userA, &userB, &[]User{userA, userB, userC})

// Replace teams for multiple users in a batch

// Reset user1's team to userA, user2's team to userB, and user3's team to userA, userB, and userC

db.Model(&users).Association("Team").Replace(&userA, &userB, &[]User{userA, userB, userC})

[](https://gorm.io/docs/associations.html#Delete-Association-Record "Delete Association Record")Delete Association Record[](https://gorm.io/docs/associations.html#Delete-Association-Record)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In GORM, the `Replace`, `Delete`, and `Clear` methods in Association Mode primarily affect the foreign key references, not the associated records themselves. Understanding and managing this behavior is crucial for data integrity.

*   **Reference Update**: These methods update the association’s foreign key to null, effectively removing the link between the source and associated models.
*   **No Physical Record Deletion**: The actual associated records remain untouched in the database.

### [](https://gorm.io/docs/associations.html#Modifying-Deletion-Behavior-with-Unscoped "Modifying Deletion Behavior with Unscoped")Modifying Deletion Behavior with `Unscoped`[](https://gorm.io/docs/associations.html#Modifying-Deletion-Behavior-with-Unscoped)

For scenarios requiring actual deletion of associated records, the `Unscoped` method alters this behavior.

*   **Soft Delete**: Marks associated records as deleted (sets `deleted_at` field) without removing them from the database.

db.Model(&user).Association("Languages").Unscoped().Clear()

*   **Permanent Delete**: Physically deletes the association records from the database.

// db.Unscoped().Model(&user)

db.Unscoped().Model(&user).Association("Languages").Unscoped().Clear()

[](https://gorm.io/docs/associations.html#Association-Tags "Association Tags")Association Tags[](https://gorm.io/docs/associations.html#Association-Tags)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Association tags in GORM are used to specify how associations between models are handled. These tags define the relationship’s details, such as foreign keys, references, and constraints. Understanding these tags is essential for setting up and managing relationships effectively.

| Tag | Description |
| --- | --- |
| `foreignKey` | Specifies the column name of the current model used as a foreign key in the join table. |
| `references` | Indicates the column name in the reference table that the foreign key of the join table maps to. |
| `polymorphic` | Defines the polymorphic type, typically the model name. |
| `polymorphicValue` | Sets the polymorphic value, usually the table name, if not specified otherwise. |
| `many2many` | Names the join table used in a many-to-many relationship. |
| `joinForeignKey` | Identifies the foreign key column in the join table that maps back to the current model’s table. |
| `joinReferences` | Points to the foreign key column in the join table that links to the reference model’s table. |
| `constraint` | Specifies relational constraints like `OnUpdate`, `OnDelete` for the association. |

[![Image 2: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)

Last updated: 2026-01-31[Prev](https://gorm.io/docs/polymorphism.html "Polymorphism")[Next](https://gorm.io/docs/preload.html "Preloading (Eager Loading)")

Gold Sponsors
=============

[![Image 3: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 4: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 5: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 6: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Gold Sponsors
=============

[![Image 7: Encore](https://gorm.io/sponsors-imgs/encore.png)](https://www.encore.dev/?utm_source=github&utm_medium=github-gorm-sponsor-logo&utm_campaign=gorm-20231215 "Encore")

[![Image 8: Incident.io](https://gorm.io/sponsors-imgs/incident-io.svg)](https://incident.io/ "Incident.io")

[![Image 9: Seats.aero](https://gorm.io/sponsors-imgs/seats.aero.svg)](https://seats.aero/ "Seats.aero")

[![Image 10: Bytebase](https://gorm.io/sponsors-imgs/bytebase.png)](https://www.bytebase.com/?utm_source=gorm.io "Bytebase")

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

Platinum Sponsors
=================

[Become a Sponsor!](https://gorm.io/contribute.html#Donations "Help to deliver a better GORM!")

**Contents**
1.   [Auto Create/Update](https://gorm.io/docs/associations.html#Auto-Create-Update)
    1.   [Auto-Saving Associations on Create](https://gorm.io/docs/associations.html#Auto-Saving-Associations-on-Create)
    2.   [Updating Associations with FullSaveAssociations](https://gorm.io/docs/associations.html#Updating-Associations-with-FullSaveAssociations)

2.   [Skip Auto Create/Update](https://gorm.io/docs/associations.html#Skip-Auto-Create-Update)
    1.   [Using Select to Include Specific Fields](https://gorm.io/docs/associations.html#Using-Select-to-Include-Specific-Fields)
    2.   [Using Omit to Exclude Fields or Associations](https://gorm.io/docs/associations.html#Using-Omit-to-Exclude-Fields-or-Associations)

3.   [Select/Omit Association fields](https://gorm.io/docs/associations.html#Select-Omit-Association-fields)
4.   [Delete Associations](https://gorm.io/docs/associations.html#Delete-Associations)
5.   [Association Mode](https://gorm.io/docs/associations.html#Association-Mode)
    1.   [Finding Associations](https://gorm.io/docs/associations.html#Finding-Associations)
    2.   [Appending Associations](https://gorm.io/docs/associations.html#Appending-Associations)
    3.   [Replacing Associations](https://gorm.io/docs/associations.html#Replacing-Associations)
    4.   [Deleting Associations](https://gorm.io/docs/associations.html#Deleting-Associations)
    5.   [Clearing Associations](https://gorm.io/docs/associations.html#Clearing-Associations)
    6.   [Counting Associations](https://gorm.io/docs/associations.html#Counting-Associations)
    7.   [Batch Data Handling](https://gorm.io/docs/associations.html#Batch-Data-Handling)

6.   [Delete Association Record](https://gorm.io/docs/associations.html#Delete-Association-Record)
    1.   [Modifying Deletion Behavior with Unscoped](https://gorm.io/docs/associations.html#Modifying-Deletion-Behavior-with-Unscoped)

7.   [Association Tags](https://gorm.io/docs/associations.html#Association-Tags)

[Improve this page](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/associations.md)[Back to Top](https://gorm.io/docs/associations.html#)

**Getting Started**[Overview](https://gorm.io/docs/index.html)[Declaring Models](https://gorm.io/docs/models.html)[Connecting to Database](https://gorm.io/docs/connecting_to_the_database.html)[GORM CLI](https://gorm.io/cli/index.html)[The Generics Way](https://gorm.io/docs/the_generics_way.html)**CRUD Interface**[Create](https://gorm.io/docs/create.html)[Query](https://gorm.io/docs/query.html)[Advanced Query](https://gorm.io/docs/advanced_query.html)[Update](https://gorm.io/docs/update.html)[Delete](https://gorm.io/docs/delete.html)[Raw SQL & SQL Builder](https://gorm.io/docs/sql_builder.html)**Associations**[Belongs To](https://gorm.io/docs/belongs_to.html)[Has One](https://gorm.io/docs/has_one.html)[Has Many](https://gorm.io/docs/has_many.html)[Many To Many](https://gorm.io/docs/many_to_many.html)[Polymorphism](https://gorm.io/docs/polymorphism.html)[Association Mode](https://gorm.io/docs/associations.html)[Preloading (Eager Loading)](https://gorm.io/docs/preload.html)**Tutorials**[Context](https://gorm.io/docs/context.html)[Error Handling](https://gorm.io/docs/error_handling.html)[Method Chaining](https://gorm.io/docs/method_chaining.html)[Session](https://gorm.io/docs/session.html)[Hooks](https://gorm.io/docs/hooks.html)[Transactions](https://gorm.io/docs/transactions.html)[Migration](https://gorm.io/docs/migration.html)[Logger](https://gorm.io/docs/logger.html)[Generic Database Interface](https://gorm.io/docs/generic_interface.html)[Performance](https://gorm.io/docs/performance.html)[Customize Data Types](https://gorm.io/docs/data_types.html)[Scopes](https://gorm.io/docs/scopes.html)[Conventions](https://gorm.io/docs/conventions.html)[Settings](https://gorm.io/docs/settings.html)**Advanced Topics**[Database Resolver](https://gorm.io/docs/dbresolver.html)[Sharding](https://gorm.io/docs/sharding.html)[Serializer](https://gorm.io/docs/serializer.html)[Prometheus](https://gorm.io/docs/prometheus.html)[Hints](https://gorm.io/docs/hints.html)[Indexes](https://gorm.io/docs/indexes.html)[Constraints](https://gorm.io/docs/constraints.html)[Composite Primary Key](https://gorm.io/docs/composite_primary_key.html)[Security](https://gorm.io/docs/security.html)[GORM Config](https://gorm.io/docs/gorm_config.html)[Write Plugins](https://gorm.io/docs/write_plugins.html)[Write Driver](https://gorm.io/docs/write_driver.html)[ChangeLog](https://gorm.io/docs/changelog.html)[Community](https://gorm.io/community.html)[Contribute](https://gorm.io/contribute.html)[Translate current site](https://gorm.io/contribute.html#Translate-this-site)

 © 2013~2026 [Jinzhu](https://github.com/jinzhu)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

 感谢 [无闻](https://github.com/unknwon) 对域名 [gorm.cn](https://gorm.cn/) 的捐赠

[浙ICP备2020033190号-1](http://beian.miit.gov.cn/)

[](https://twitter.com/zhangjinzhu)[](https://github.com/go-gorm/gorm)

*   [Home](https://gorm.io/)
[Docs](https://gorm.io/docs/)[CLI](https://gorm.io/cli/)[Gen](https://gorm.io/gen/)[Community](https://gorm.io/community.html)[API](https://pkg.go.dev/gorm.io/gorm)[Contribute](https://gorm.io/contribute.html)
**Getting Started**[Overview](https://gorm.io/docs/index.html)[Declaring Models](https://gorm.io/docs/models.html)[Connecting to Database](https://gorm.io/docs/connecting_to_the_database.html)[GORM CLI](https://gorm.io/cli/index.html)[The Generics Way](https://gorm.io/docs/the_generics_way.html)**CRUD Interface**[Create](https://gorm.io/docs/create.html)[Query](https://gorm.io/docs/query.html)[Advanced Query](https://gorm.io/docs/advanced_query.html)[Update](https://gorm.io/docs/update.html)[Delete](https://gorm.io/docs/delete.html)[Raw SQL & SQL Builder](https://gorm.io/docs/sql_builder.html)**Associations**[Belongs To](https://gorm.io/docs/belongs_to.html)[Has One](https://gorm.io/docs/has_one.html)[Has Many](https://gorm.io/docs/has_many.html)[Many To Many](https://gorm.io/docs/many_to_many.html)[Polymorphism](https://gorm.io/docs/polymorphism.html)[Association Mode](https://gorm.io/docs/associations.html)[Preloading (Eager Loading)](https://gorm.io/docs/preload.html)**Tutorials**[Context](https://gorm.io/docs/context.html)[Error Handling](https://gorm.io/docs/error_handling.html)[Method Chaining](https://gorm.io/docs/method_chaining.html)[Session](https://gorm.io/docs/session.html)[Hooks](https://gorm.io/docs/hooks.html)[Transactions](https://gorm.io/docs/transactions.html)[Migration](https://gorm.io/docs/migration.html)[Logger](https://gorm.io/docs/logger.html)[Generic Database Interface](https://gorm.io/docs/generic_interface.html)[Performance](https://gorm.io/docs/performance.html)[Customize Data Types](https://gorm.io/docs/data_types.html)[Scopes](https://gorm.io/docs/scopes.html)[Conventions](https://gorm.io/docs/conventions.html)[Settings](https://gorm.io/docs/settings.html)**Advanced Topics**[Database Resolver](https://gorm.io/docs/dbresolver.html)[Sharding](https://gorm.io/docs/sharding.html)[Serializer](https://gorm.io/docs/serializer.html)[Prometheus](https://gorm.io/docs/prometheus.html)[Hints](https://gorm.io/docs/hints.html)[Indexes](https://gorm.io/docs/indexes.html)[Constraints](https://gorm.io/docs/constraints.html)[Composite Primary Key](https://gorm.io/docs/composite_primary_key.html)[Security](https://gorm.io/docs/security.html)[GORM Config](https://gorm.io/docs/gorm_config.html)[Write Plugins](https://gorm.io/docs/write_plugins.html)[Write Driver](https://gorm.io/docs/write_driver.html)[ChangeLog](https://gorm.io/docs/changelog.html)[Community](https://gorm.io/community.html)[Contribute](https://gorm.io/contribute.html)[Translate current site](https://gorm.io/contribute.html#Translate-this-site)

English
