# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData.md.txt

# MutableData

public class **MutableData** extends Object  
Instances of this class encapsulate the data and priority at a location. It is used in
transactions, and it is intended to be inspected and then updated to the desired data at that
location.   

<br />


Note that changes made to a child MutableData instance will be visible to the parent and vice
versa.

### Public Method Summary

|---|---|
| [MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) | [child](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#child(java.lang.String))(String path) Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path. |
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#equals(java.lang.Object))(Object o) |
| Iterable\<[MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData)\> | [getChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getChildren())() Used to iterate over the immediate children at this location ` for (MutableData child : parent.getChildren()) { ...`` `` ` |
| long | [getChildrenCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getChildrenCount())() |
| String | [getKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getKey())() |
| Object | [getPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getPriority())() Gets the current priority at this location. |
| \<T\> T | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getValue(com.google.firebase.database.GenericTypeIndicator<T>))([GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator)\<T\> t) Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| Object | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getValue())() getValue() returns the data contained in this instance as native types. |
| \<T\> T | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getValue(java.lang.Class<T>))(Class\<T\> valueType) This method is used to marshall the data contained in this instance into a class of your choosing. |
| boolean | [hasChild](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#hasChild(java.lang.String))(String path) |
| boolean | [hasChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#hasChildren())() Returns true if the data at this location has children, and false otherwise. |
| void | [setPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#setPriority(java.lang.Object))(Object priority) Sets the priority at this location |
| void | [setValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#setValue(java.lang.Object))(Object value) Set the data at this location to the given value. |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#toString())() |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public [MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData)
**child**
(String path)

Used to obtain a MutableData instance that encapsulates the data and priority at the given
relative path.

##### Parameters

| path | A relative path |
|---|---|

##### Returns

- An instance encapsulating the data and priority at the given path

#### public boolean
**equals**
(Object o)

<br />

#### public Iterable\<[MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData)\>
**getChildren**
()

Used to iterate over the immediate children at this location `

for (MutableData child : parent.getChildren()) {

...

}
`

##### Returns

- The immediate children at this location

#### public long
**getChildrenCount**
()

<br />

##### Returns

- The number of immediate children at this location

#### public String
**getKey**
()

<br />

##### Returns

- The key name of this location, or null if it is the top-most location

#### public Object
**getPriority**
()

Gets the current priority at this location. The possible return types are:

- Double
- String

Note that null is allowed.

##### Returns

- The priority at this location as a native type

#### public T
**getValue**
([GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator)\<T\> t)

Due to the way that Java implements generics, it takes an extra step to get back a
properly-typed Collection. So, in the case where you want a `List` of Message
instances, you will need to do something like the following:


         GenericTypeIndicator<List<Message>> t =
             new GenericTypeIndicator<List<Message>>() {};
         List<Message> messages = mutableData.getValue(t);
     
It is important to use a subclass of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator` for more details

##### Parameters

| t | A subclass of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |
|---|---|

##### Returns

- A properly typed collection, populated with the data from this instance, or null if there is no data at this location.

#### public Object
**getValue**
()

getValue() returns the data contained in this instance as native types. The possible types
returned are:

- Boolean
- String
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

This list is recursive; the possible types for `Object` in the above list is
given by the same list. These types correspond to the types available in JSON.

##### Returns

- The data contained in this instance as native types, or null if there is no data at this location.

#### public T
**getValue**
(Class\<T\> valueType)

This method is used to marshall the data contained in this instance into a class of your
choosing. The class must fit 2 simple constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

An example class might look like:


         class Message {
             private String author;
             private String text;

             private Message() {}

             public Message(String author, String text) {
                 this.author = author;
                 this.text = text;
             }

             public String getAuthor() {
                 return author;
             }

             public String getText() {
                 return text;
             }
         }


         // Later
         Message m = mutableData.getValue(Message.class);
     
<br />

##### Parameters

| valueType | The class into which this data in this instance should be marshalled |
|---|---|

##### Returns

- An instance of the class passed in, populated with the data from this instance, or null if there is no data at this location.

#### public boolean
**hasChild**
(String path)

<br />

##### Parameters

| path | A relative path |
|---|---|

##### Returns

- True if data exists at the given path, otherwise false

#### public boolean
**hasChildren**
()

Returns true if the data at this location has children, and false otherwise.

#### public void
**setPriority**
(Object priority)

Sets the priority at this location

##### Parameters

| priority | The desired priority |
|---|---|

#### public void
**setValue**
(Object value)

Set the data at this location to the given value. The native types accepted by this method for
the value correspond to the JSON types:

- Boolean
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

<br />

<br />

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

<br />

<br />

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

Note that this overrides the priority, which must be set separately.

##### Parameters

| value | The value to set at this location |
|---|---|

##### Throws

| [DatabaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseException) |   |
|---|---|

#### public String
**toString**
()

<br />