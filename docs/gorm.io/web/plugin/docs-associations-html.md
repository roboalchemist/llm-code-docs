# Source: https://gorm.io/docs/associations.html

Title: Associations

URL Source: https://gorm.io/docs/associations.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://gorm.io/docs/associations.html#Auto-Create-Update "Auto Create/Update")Auto Create/Update
----------------------------------------------------------------------------------------------------

GORM automates the saving of associations and their references when creating or updating records, using an upsert technique that primarily updates foreign key references for existing associations.

### [](https://gorm.io/docs/associations.html#Auto-Saving-Associations-on-Create "Auto-Saving Associations on Create")Auto-Saving Associations on Create

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

db.Create(&user)

db.Save(&user)

### [](https://gorm.io/docs/associations.html#Updating-Associations-with-FullSaveAssociations "Updating Associations with FullSaveAssociations")Updating Associations with `FullSaveAssociations`

For scenarios where a full update of the associated data is required (not just the foreign key references), the `FullSaveAssociations` mode should be used.

db.Session(&gorm.Session{FullSaveAssociations: true}).Updates(&user)

Using `FullSaveAssociations` ensures that the entire state of the model, including all its associations, is reflected in the database, maintaining data integrity and consistency throughout the application.

[](https://gorm.io/docs/associations.html#Skip-Auto-Create-Update "Skip Auto Create/Update")Skip Auto Create/Update
-------------------------------------------------------------------------------------------------------------------

GORM provides flexibility to skip automatic saving of associations during create or update operations. This can be achieved using the `Select` or `Omit` methods, which allow you to specify exactly which fields or associations should be included or excluded in the operation.

### [](https://gorm.io/docs/associations.html#Using-Select-to-Include-Specific-Fields "Using Select to Include Specific Fields")Using `Select` to Include Specific Fields

The `Select` method lets you specify which fields of the model should be saved. This means that only the selected fields will be included in the SQL operation.

user := User{

 

}

db.Select("Name").Create(&user)

### [](https://gorm.io/docs/associations.html#Using-Omit-to-Exclude-Fields-or-Associations "Using Omit to Exclude Fields or Associations")Using `Omit` to Exclude Fields or Associations

Conversely, `Omit` allows you to exclude certain fields or associations when saving a model.

db.Omit("BillingAddress").Create(&user)

db.Omit(clause.Associations).Create(&user)

> **NOTE:**
> 
> For many-to-many associations, GORM upserts the associations before creating join table references. To skip this upserting, use `Omit` with the association name followed by `.*`:
> 
> 
> 
> db.Omit("Languages.*").Create(&user)
> 
> 
> To skip creating both the association and its references:
> 
> 
> 
> db.Omit("Languages").Create(&user)

Using `Select` and `Omit`, you can fine-tune how GORM handles the creation or updating of your models, giving you control over the auto-save behavior of associations.

[](https://gorm.io/docs/associations.html#Select-Omit-Association-fields "Select/Omit Association fields")Select/Omit Association fields
----------------------------------------------------------------------------------------------------------------------------------------

In GORM, when creating or updating records, you can use the `Select` and `Omit` methods to specifically include or exclude certain fields of an associated model.

With `Select`, you can specify which fields of an associated model should be included when saving the primary model. This is particularly useful for selectively saving parts of an association.

Conversely, `Omit` lets you exclude certain fields of an associated model from being saved. This can be useful when you want to prevent specific parts of an association from being persisted.

user := User{

 Name: "jinzhu",

 BillingAddress: Address{Address1: "Billing Address - Address 1", Address2: "addr2"},

 ShippingAddress: Address{Address1: "Shipping Address - Address 1", Address2: "addr2"},

}

db.Select("BillingAddress.Address1", "BillingAddress.Address2").Create(&user)

db.Omit("BillingAddress.Address2", "BillingAddress.CreatedAt").Create(&user)

[](https://gorm.io/docs/associations.html#Delete-Associations "Delete Associations")Delete Associations
-------------------------------------------------------------------------------------------------------

GORM allows for the deletion of specific associated relationships (has one, has many, many2many) using the `Select` method when deleting a primary record. This feature is particularly useful for maintaining database integrity and ensuring related data is appropriately managed upon deletion.

You can specify which associations should be deleted along with the primary record by using `Select`.

db.Select("Account").Delete(&user)

db.Select("Orders", "CreditCards").Delete(&user)

db.Select(clause.Associations).Delete(&user)

db.Select("Account").Delete(&users)

> **NOTE:**
> 
> It’s important to note that associations will be deleted only if the primary key of the deleting record is not zero. GORM uses these primary keys as conditions to delete the selected associations.
> 
> 
> 
> db.Select("Account").Where("name = ?", "jinzhu").Delete(&User{})
> 
> 
> 
> 
> 
> 
> 
> db.Select("Account").Where("name = ?", "jinzhu").Delete(&User{ID: 1})
> 
> 
> 
> 
> 
> 
> 
> db.Select("Account").Delete(&User{ID: 1})

[](https://gorm.io/docs/associations.html#Association-Mode "Association Mode")Association Mode
----------------------------------------------------------------------------------------------

Association Mode in GORM offers various helper methods to handle relationships between models, providing an efficient way to manage associated data.

To start Association Mode, specify the source model and the relationship’s field name. The source model must contain a primary key, and the relationship’s field name should match an existing association.

var user User

db.Model(&user).Association("Languages")

error := db.Model(&user).Association("Languages").Error

### [](https://gorm.io/docs/associations.html#Finding-Associations "Finding Associations")Finding Associations

Retrieve associated records with or without additional conditions.

db.Model(&user).Association("Languages").Find(&languages)

codes := []string{"zh-CN", "en-US", "ja-JP"}

db.Model(&user).Where("code IN ?", codes).Association("Languages").Find(&languages)

### [](https://gorm.io/docs/associations.html#Appending-Associations "Appending Associations")Appending Associations

Add new associations for `many to many`, `has many`, or replace the current association for `has one`, `belongs to`.

db.Model(&user).Association("Languages").Append([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Append(&Language{Name: "DE"})

db.Model(&user).Association("CreditCard").Append(&CreditCard{Number: "411111111111"})

### [](https://gorm.io/docs/associations.html#Replacing-Associations "Replacing Associations")Replacing Associations

Replace current associations with new ones.

db.Model(&user).Association("Languages").Replace([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Replace(Language{Name: "DE"}, languageEN)

### [](https://gorm.io/docs/associations.html#Deleting-Associations "Deleting Associations")Deleting Associations

Remove the relationship between the source and arguments, only deleting the reference.

db.Model(&user).Association("Languages").Delete([]Language{languageZH, languageEN})

db.Model(&user).Association("Languages").Delete(languageZH, languageEN)

### [](https://gorm.io/docs/associations.html#Clearing-Associations "Clearing Associations")Clearing Associations

Remove all references between the source and association.

db.Model(&user).Association("Languages").Clear()

### [](https://gorm.io/docs/associations.html#Counting-Associations "Counting Associations")Counting Associations

Get the count of current associations, with or without conditions.

db.Model(&user).Association("Languages").Count()

codes := []string{"zh-CN", "en-US", "ja-JP"}

db.Model(&user).Where("code IN ?", codes).Association("Languages").Count()

### [](https://gorm.io/docs/associations.html#Batch-Data-Handling "Batch Data Handling")Batch Data Handling

Association Mode allows you to handle relationships for multiple records in a batch. This includes finding, appending, replacing, deleting, and counting operations for associated data.

*   **Finding Associations**: Retrieve associated data for a collection of records.

db.Model(&users).Association("Role").Find(&roles)

*   **Deleting Associations**: Remove specific associations across multiple records.

db.Model(&users).Association("Team").Delete(&userA)

*   **Counting Associations**: Get the count of associations for a batch of records.

db.Model(&users).Association("Team").Count()

*   **Appending/Replacing Associations**: Manage associations for multiple records. Note the need for matching argument lengths with the data.

var users = []User{user1, user2, user3}

db.Model(&users).Association("Team").Append(&userA, &userB, &[]User{userA, userB, userC})

db.Model(&users).Association("Team").Replace(&userA, &userB, &[]User{userA, userB, userC})

[](https://gorm.io/docs/associations.html#Delete-Association-Record "Delete Association Record")Delete Association Record
-------------------------------------------------------------------------------------------------------------------------

In GORM, the `Replace`, `Delete`, and `Clear` methods in Association Mode primarily affect the foreign key references, not the associated records themselves. Understanding and managing this behavior is crucial for data integrity.

*   **Reference Update**: These methods update the association’s foreign key to null, effectively removing the link between the source and associated models.
*   **No Physical Record Deletion**: The actual associated records remain untouched in the database.

### [](https://gorm.io/docs/associations.html#Modifying-Deletion-Behavior-with-Unscoped "Modifying Deletion Behavior with Unscoped")Modifying Deletion Behavior with `Unscoped`

For scenarios requiring actual deletion of associated records, the `Unscoped` method alters this behavior.

*   **Soft Delete**: Marks associated records as deleted (sets `deleted_at` field) without removing them from the database.

db.Model(&user).Association("Languages").Unscoped().Clear()

*   **Permanent Delete**: Physically deletes the association records from the database.

db.Unscoped().Model(&user).Association("Languages").Unscoped().Clear()

[](https://gorm.io/docs/associations.html#Association-Tags "Association Tags")Association Tags
----------------------------------------------------------------------------------------------

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
