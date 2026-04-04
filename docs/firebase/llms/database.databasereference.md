# Source: https://firebase.google.com/docs/reference/js/database.databasereference.md.txt

# DatabaseReference interface

A `DatabaseReference` represents a specific location in your Database and can be used for reading or writing data to that Database location.

You can reference the root or child location in your Database by calling `ref()` or `ref("child/path")`.

Writing is done with the `set()` method and reading can be done with the `on*()` method. See <https://firebase.google.com/docs/database/web/read-and-write>

**Signature:**  

    export declare interface DatabaseReference extends Query 

**Extends:** [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface)

## Properties

|                                                   Property                                                    |                                                                 Type                                                                 |                                                                                       Description                                                                                       |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [key](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereferencekey)       | string \| null                                                                                                                       | The last part of the `DatabaseReference`'s path.For example, `"ada"` is the key for `https://<DATABASE_NAME>.firebaseio.com/users/ada`.The key of a root `DatabaseReference` is `null`. |
| [parent](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereferenceparent) | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) \| null | The parent location of a `DatabaseReference`.The parent of a root `DatabaseReference` is `null`.                                                                                        |
| [root](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereferenceroot)     | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface)         | The root `DatabaseReference` of the Database.                                                                                                                                           |

## DatabaseReference.key

The last part of the `DatabaseReference`'s path.

For example, `"ada"` is the key for `https://<DATABASE_NAME>.firebaseio.com/users/ada`.

The key of a root `DatabaseReference` is `null`.

**Signature:**  

    readonly key: string | null;

## DatabaseReference.parent

The parent location of a `DatabaseReference`.

The parent of a root `DatabaseReference` is `null`.

**Signature:**  

    readonly parent: DatabaseReference | null;

## DatabaseReference.root

The root `DatabaseReference` of the Database.

**Signature:**  

    readonly root: DatabaseReference;