# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot.md.txt

# DataSnapshot

public class **DataSnapshot** extends Object  
A DataSnapshot instance contains data from a Firebase Database location. Any time you read
Database data, you receive the data as a DataSnapshot.   

<br />


DataSnapshots are passed to the methods in listeners that you attach with `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)`, `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)`, or `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener)`.   

<br />


They are efficiently-generated immutable copies of the data at a Firebase Database location. They
can't be modified and will never change. To modify data at a location, use a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference` reference (e.g. with `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#setValueAsync(java.lang.Object)`).

### Public Method Summary

|---|---|
| [DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) | [child](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#child(java.lang.String))(String path) Get a DataSnapshot for the location at the specified relative path. |
| boolean | [exists](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#exists())() Returns true if the snapshot contains a non-null value. |
| Iterable\<[DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot)\> | [getChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getChildren())() Gives access to all of the immediate children of this snapshot. |
| long | [getChildrenCount](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getChildrenCount())() |
| String | [getKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getKey())() |
| Object | [getPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getPriority())() Returns the priority of the data contained in this snapshot as a native type. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getRef](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getRef())() Used to obtain a reference to the source location for this snapshot. |
| Object | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getValue(boolean))(boolean useExportFormat) getValue() returns the data contained in this snapshot as native types. |
| \<T\> T | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getValue(com.google.firebase.database.GenericTypeIndicator<T>))([GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator)\<T\> t) Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| Object | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getValue())() getValue() returns the data contained in this snapshot as native types. |
| \<T\> T | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getValue(java.lang.Class<T>))(Class\<T\> valueType) This method is used to marshall the data contained in this snapshot into a class of your choosing. |
| boolean | [hasChild](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#hasChild(java.lang.String))(String path) Can be used to determine if this DataSnapshot has data at a particular location |
| boolean | [hasChildren](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#hasChildren())() Indicates whether this snapshot has any children |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#toString())() |

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

#### public [DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot)
**child**
(String path)

Get a DataSnapshot for the location at the specified relative path. The relative path can
either be a simple child key (e.g. 'fred') or a deeper slash-separated path (e.g.
'fred/name/first'). If the child location has no data, an empty DataSnapshot is returned.

##### Parameters

| path | A relative path to the location of child data |
|---|---|

##### Returns

- The DataSnapshot for the child location

#### public boolean
**exists**
()

Returns true if the snapshot contains a non-null value.

##### Returns

- True if the snapshot contains a non-null value, otherwise false

#### public Iterable\<[DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot)\>
**getChildren**
()

Gives access to all of the immediate children of this snapshot. Can be used in native for
loops: `

for (DataSnapshot child : parent.getChildren()) {

...

}
`

##### Returns

- The immediate children of this snapshot

#### public long
**getChildrenCount**
()

<br />

##### Returns

- The number of immediate children in the this snapshot

#### public String
**getKey**
()

<br />

##### Returns

- the key name for the source location of this snapshot

#### public Object
**getPriority**
()

Returns the priority of the data contained in this snapshot as a native type. Possible return
types:

- Double
- String

Note that null is also allowed.

##### Returns

- the priority of the data contained in this snapshot as a native type

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getRef**
()

Used to obtain a reference to the source location for this snapshot.

##### Returns

- A DatabaseReference corresponding to the location that this snapshot came from

#### public Object
**getValue**
(boolean useExportFormat)

getValue() returns the data contained in this snapshot as native types. The possible types
returned are:

- Boolean
- String
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

This list is recursive; the possible types for `Object` in the above list is
given by the same list. These types correspond to the types available in JSON.

If useExportFormat is set to true, priority information will be included in the output.
Priority information shows up as a .priority key in a map. For data that would not otherwise be
a map, the map will also include a .value key with the data.

##### Parameters

| useExportFormat | Whether or not to include priority information |
|---|---|

##### Returns

- The data, along with its priority, in native types or null if there is no data at this location.

#### public T
**getValue**
([GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator)\<T\> t)

Due to the way that Java implements generics, it takes an extra step to get back a
properly-typed Collection. So, in the case where you want a `List` of Message
instances, you will need to do something like the following:


         GenericTypeIndicator<List<Message>> t = new GenericTypeIndicator<List<
         Message>>()
     {};
         List<Message> messages = snapshot.getValue(t);
     
It is important to use a subclass of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator` for more details

##### Parameters

| t | A subclass of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |
|---|---|

##### Returns

- A properly typed collection, populated with the data from this snapshot, or null if there is no data at this location.

#### public Object
**getValue**
()

getValue() returns the data contained in this snapshot as native types. The possible types
returned are:

- Boolean
- String
- Long
- Double
- Map\<String, Object\>
- List\<Object\>

This list is recursive; the possible types for `Object` in the above list
is given by the same list. These types correspond to the types available in JSON.

##### Returns

- The data contained in this snapshot as native types or null if there is no data at this location.

#### public T
**getValue**
(Class\<T\> valueType)

This method is used to marshall the data contained in this snapshot into a class of your
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
         Message m = snapshot.getValue(Message.class);
     
<br />

##### Parameters

| valueType | The class into which this snapshot should be marshalled |
|---|---|

##### Returns

- An instance of the class passed in, populated with the data from this snapshot, or null if there is no data at this location.

#### public boolean
**hasChild**
(String path)

Can be used to determine if this DataSnapshot has data at a particular location

##### Parameters

| path | A relative path to the location of child data |
|---|---|

##### Returns

- Whether or not the specified child location has data

#### public boolean
**hasChildren**
()

Indicates whether this snapshot has any children

##### Returns

- True if the snapshot has any children, otherwise false

#### public String
**toString**
()

<br />