# Source: https://mikro-orm.io/api/sql/interface/ForeignKey.md

# ForeignKey<!-- -->

## Index[**](#index)

### Properties

* [**columnNames](#columnnames)
* [**constraintName](#constraintname)
* [**deferMode](#deferMode)
* [**deleteRule](#deleteRule)
* [**localTableName](#localtablename)
* [**referencedColumnNames](#referencedcolumnnames)
* [**referencedTableName](#referencedtablename)
* [**updateRule](#updateRule)

## Properties<!-- -->[**](#properties)

### [**](#columnnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L83)columnNames

**columnNames: string\[]

### [**](#constraintname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L84)constraintName

**constraintName: string

### [**](#deferMode)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L90)optionaldeferMode

**deferMode?

<!-- -->

: [DeferMode](https://mikro-orm.io/api/core/enum/DeferMode.md)

### [**](#deleteRule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L89)optionaldeleteRule

**deleteRule?

<!-- -->

: string

### [**](#localtablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L85)localTableName

**localTableName: string

### [**](#referencedcolumnnames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L87)referencedColumnNames

**referencedColumnNames: string\[]

### [**](#referencedtablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L86)referencedTableName

**referencedTableName: string

### [**](#updateRule)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L88)optionalupdateRule

**updateRule?

<!-- -->

: string
