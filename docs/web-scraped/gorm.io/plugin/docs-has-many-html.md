# Source: https://gorm.io/docs/has_many.html

Title: Has Many

URL Source: https://gorm.io/docs/has_many.html

Published Time: 2026-01-31T07:58:03.918Z

Markdown Content:
[](https://github.com/go-gorm/gorm.io/edit/master/pages/docs/has_many.md "Improve this page")

[](https://gorm.io/docs/has_many.html#Has-Many "Has Many")Has Many
------------------------------------------------------------------

A `has many` association sets up a one-to-many connection with another model, unlike `has one`, the owner could have zero or many instances of models.

For example, if your application includes users and credit card, and each user can have many credit cards.

### [](https://gorm.io/docs/has_many.html#Declare "Declare")Declare

type User struct {

 gorm.Model

 CreditCards []CreditCard

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

### [](https://gorm.io/docs/has_many.html#Retrieve "Retrieve")Retrieve

func GetAll(db *gorm.DB) ([]User, error) {

 var users []User

 err := db.Model(&User{}).Preload("CreditCards").Find(&users).Error

 return users, err

}

[](https://gorm.io/docs/has_many.html#Override-Foreign-Key "Override Foreign Key")Override Foreign Key
------------------------------------------------------------------------------------------------------

To define a `has many` relationship, a foreign key must exist. The default foreign key’s name is the owner’s type name plus the name of its primary key field

For example, to define a model that belongs to `User`, the foreign key should be `UserID`.

To use another field as foreign key, you can customize it with a `foreignKey` tag, e.g:

type User struct {

 gorm.Model

 CreditCards []CreditCard `gorm:"foreignKey:UserRefer"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserRefer uint

}

[](https://gorm.io/docs/has_many.html#Override-References "Override References")Override References
---------------------------------------------------------------------------------------------------

GORM usually uses the owner’s primary key as the foreign key’s value, for the above example, it is the `User`‘s `ID`,

When you assign credit cards to a user, GORM will save the user’s `ID` into credit cards’ `UserID` field.

You are able to change it with tag `references`, e.g:

type User struct {

 gorm.Model

 MemberNumber string

 CreditCards []CreditCard `gorm:"foreignKey:UserNumber;references:MemberNumber"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserNumber string

}

[](https://gorm.io/docs/has_many.html#CRUD-with-Has-Many "CRUD with Has Many")CRUD with Has Many
------------------------------------------------------------------------------------------------

Please checkout [Association Mode](https://gorm.io/docs/associations.html#Association-Mode) for working with has many relations

[](https://gorm.io/docs/has_many.html#Eager-Loading "Eager Loading")Eager Loading
---------------------------------------------------------------------------------

GORM allows eager loading has many associations with `Preload`, refer [Preloading (Eager loading)](https://gorm.io/docs/preload.html) for details

[](https://gorm.io/docs/has_many.html#Self-Referential-Has-Many "Self-Referential Has Many")Self-Referential Has Many
---------------------------------------------------------------------------------------------------------------------

type User struct {

 gorm.Model

 Name string

 ManagerID *uint

 Team []User `gorm:"foreignkey:ManagerID"`

}

[](https://gorm.io/docs/has_many.html#FOREIGN-KEY-Constraints "FOREIGN KEY Constraints")FOREIGN KEY Constraints
---------------------------------------------------------------------------------------------------------------

You can setup `OnUpdate`, `OnDelete` constraints with tag `constraint`, it will be created when migrating with GORM, for example:

type User struct {

 gorm.Model

 CreditCards []CreditCard `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`

}

type CreditCard struct {

 gorm.Model

 Number string

 UserID uint

}

You are also allowed to delete selected has many associations with `Select` when deleting, checkout [Delete with Select](https://gorm.io/docs/associations.html#delete_with_select) for details

[![Image 1: GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/go-gorm/gorm?label=Latest%20GORM%20Release&color=red&&style=for-the-badge&logo=go&logoColor=red)](https://gorm.io/docs/v2_release_note.html)
