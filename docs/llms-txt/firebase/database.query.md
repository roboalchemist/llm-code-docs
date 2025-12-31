# Source: https://firebase.google.com/docs/reference/js/database.query.md.txt

# Query interface

A `Query` sorts and filters the data at a Database location so only a subset of the child data is included. This can be used to order a collection of data by some attribute (for example, height of dinosaurs) as well as to restrict a large list of items (for example, chat messages) down to a number suitable for synchronizing to the client. Queries are created by chaining together one or more of the filter methods defined here.

Just as with a `DatabaseReference`, you can receive data from a `Query` by using the `on*()` methods. You will only receive events and `DataSnapshot`s for the subset of the data that matches your query.

See <https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data> for more information.

**Signature:**  

    export declare interface Query 

## Properties

|                                    Property                                     |                                                             Type                                                             |                     Description                     |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [ref](https://firebase.google.com/docs/reference/js/database.query.md#queryref) | [DatabaseReference](https://firebase.google.com/docs/reference/js/database.databasereference.md#databasereference_interface) | The `DatabaseReference` for the `Query`'s location. |

## Methods

|                                             Method                                             |                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [isEqual(other)](https://firebase.google.com/docs/reference/js/database.query.md#queryisequal) | Returns whether or not the current and provided queries represent the same location, have the same query parameters, and are from the same instance of `FirebaseApp`.Two `DatabaseReference` objects are equivalent if they represent the same location and are from the same instance of `FirebaseApp`.Two `Query` objects are equivalent if they represent the same location, have the same query parameters, and are from the same instance of `FirebaseApp`. Equivalent queries share the same sort order, limits, and starting and ending points. |
| [toJSON()](https://firebase.google.com/docs/reference/js/database.query.md#querytojson)        | Returns a JSON-serializable representation of this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [toString()](https://firebase.google.com/docs/reference/js/database.query.md#querytostring)    | Gets the absolute URL for this location.The `toString()` method returns a URL that is ready to be put into a browser, curl command, or a `refFromURL()` call. Since all of those expect the URL to be url-encoded, `toString()` returns an encoded URL.Append '.json' to the returned URL when typed into a browser to download JSON-formatted data. If the location is secured (that is, not publicly readable), you will get a permission-denied error.                                                                                              |

## Query.ref

The `DatabaseReference` for the `Query`'s location.

**Signature:**  

    readonly ref: DatabaseReference;

## Query.isEqual()

Returns whether or not the current and provided queries represent the same location, have the same query parameters, and are from the same instance of `FirebaseApp`.

Two `DatabaseReference` objects are equivalent if they represent the same location and are from the same instance of `FirebaseApp`.

Two `Query` objects are equivalent if they represent the same location, have the same query parameters, and are from the same instance of `FirebaseApp`. Equivalent queries share the same sort order, limits, and starting and ending points.

**Signature:**  

    isEqual(other: Query | null): boolean;

#### Parameters

| Parameter |                                               Type                                               |          Description          |
|-----------|--------------------------------------------------------------------------------------------------|-------------------------------|
| other     | [Query](https://firebase.google.com/docs/reference/js/database.query.md#query_interface) \| null | The query to compare against. |

**Returns:**

boolean

Whether or not the current and provided queries are equivalent.

## Query.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): string;

**Returns:**

string

A JSON-serializable representation of this object.

## Query.toString()

Gets the absolute URL for this location.

The `toString()` method returns a URL that is ready to be put into a browser, curl command, or a `refFromURL()` call. Since all of those expect the URL to be url-encoded, `toString()` returns an encoded URL.

Append '.json' to the returned URL when typed into a browser to download JSON-formatted data. If the location is secured (that is, not publicly readable), you will get a permission-denied error.

**Signature:**  

    toString(): string;

**Returns:**

string

The absolute URL for this location.