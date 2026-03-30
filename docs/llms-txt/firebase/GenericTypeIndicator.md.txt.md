# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator.md.txt

# GenericTypeIndicator

public abstract class **GenericTypeIndicator** extends Object  
Due to the way that Java implements generics (type-erasure), it is necessary to use a slightly
more complicated method to properly resolve types for generic collections at runtime. To solve
this problem, Firebase Database accepts subclasses of this class in calls to getValue (`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot#getValue(com.google.firebase.database.GenericTypeIndicator<T>)`, `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData#getValue(com.google.firebase.database.GenericTypeIndicator<T>)`) and returns a properly-typed generic collection.

As an example, you might do something like this to get a list of Message instances from a
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot`:   

<br />



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

         // Later ...

         GenericTypeIndicator<List<Message>> t = new GenericTypeIndicator<List<
         Message>>()
     {};
         List<Message> messages = snapshot.getValue(t);

     
<br />

### Public Constructor Summary

|---|---|
|   | [GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator#GenericTypeIndicator())() |

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

## Public Constructors

#### public
**GenericTypeIndicator**
()

<br />