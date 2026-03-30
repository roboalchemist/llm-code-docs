# Source: https://gorm.io/docs/has_one.html

Title: Has One

URL Source: https://gorm.io/docs/has_one.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/has_one.md "Improve this page")

[](https://gorm.io/docs/has_one.html#Has-One "Has One")Has One
--------------------------------------------------------------

A `has one` association sets up a one-to-one connection with another model, but with somewhat different semantics (and consequences). This association indicates that each instance of a model contains or possesses one instance of another model.

For example, if your application includes users and credit cards, and each user can only have one credit card.

### [](https://gorm.io/docs/has_one.html#Declare "Declare")Declare

type User struct {

 gorm.Model

 CreditCard CreditCard

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

### [](https://gorm.io/docs/has_one.html#Retrieve "Retrieve")Retrieve

func GetAll(db *gorm.DB) ([]User, error) {

 var users []User

 err := db.Model(&User{}).Preload("CreditCard").Find(&users).Error

 return users, err

}

[](https://gorm.io/docs/has_one.html#Override-Foreign-Key "Override Foreign Key")Override Foreign Key
-----------------------------------------------------------------------------------------------------

For a `has one` relationship, a foreign key field must also exist, the owner will save the primary key of the model belongs to it into this field.

The field’s name is usually generated with `has one` model’s type plus its `primary key`, for the above example it is `UserID`.

When you give a credit card to the user, it will save the User’s `ID` into its `UserID` field.

If you want to use another field to save the relationship, you can change it with tag `foreignKey`, e.g:

type User struct {

 gorm.Model

 CreditCard CreditCard `gorm:"foreignKey:UserName"`

 

}

type CreditCard struct {

 gorm.Model

 Number string

 UserName string

}

[](https://gorm.io/docs/has_one.html#Override-References "Override References")Override References
--------------------------------------------------------------------------------------------------

By default, the owned entity will save the `has one` model’s primary key into a foreign key, you could change to save another field’s value, like using `Name` for the below example.

You are able to change it with tag `references`, e.g:

type User struct {

 gorm.Model

 Name string `gorm:"index"`

 CreditCard CreditCard `gorm:"foreignKey:UserName;references:Name"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserName string

}

[](https://gorm.io/docs/has_one.html#CRUD-with-Has-One "CRUD with Has One")CRUD with Has One
--------------------------------------------------------------------------------------------

Please checkout [Association Mode](https://gorm.io/docs/associations.html#Association-Mode) for working with `has one` relations

[](https://gorm.io/docs/has_one.html#Eager-Loading "Eager Loading")Eager Loading
--------------------------------------------------------------------------------

GORM allows eager loading `has one` associations with `Preload` or `Joins`, refer [Preloading (Eager loading)](https://gorm.io/docs/preload.html) for details

[](https://gorm.io/docs/has_one.html#Self-Referential-Has-One "Self-Referential Has One")Self-Referential Has One
-----------------------------------------------------------------------------------------------------------------

type User struct {

 gorm.Model

 Name string

 ManagerID *uint

 Manager *User

}

[](https://gorm.io/docs/has_one.html#FOREIGN-KEY-Constraints "FOREIGN KEY Constraints")FOREIGN KEY Constraints
--------------------------------------------------------------------------------------------------------------

You can setup `OnUpdate`, `OnDelete` constraints with tag `constraint`, it will be created when migrating with GORM, for example:

type User struct {

 gorm.Model

 CreditCard CreditCard `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

You are also allowed to delete selected has one associations with `Select` when deleting, checkout [Delete with Select](https://gorm.io/docs/associations.html#delete_with_select) for details

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
