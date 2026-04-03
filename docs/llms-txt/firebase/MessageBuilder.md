# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder.md.txt

# MessageBuilder

public final class **MessageBuilder** extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<[MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)\>  
Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
for a message.

For reference, see: <https://schema.org/Message>.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setDateRead](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setDateRead(java.util.Date))([Date](https://developer.android.com/reference/java/util/Date.html) dateRead) Sets the date on which the message was read.                                                                                                                                    |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setDateReceived](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setDateReceived(java.util.Date))([Date](https://developer.android.com/reference/java/util/Date.html) dateReceived) Sets the date on which the message was received.                                                                                                                    |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setDateSent](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setDateSent(java.util.Date))([Date](https://developer.android.com/reference/java/util/Date.html) dateSent) Sets the date on which the message was sent.                                                                                                                                    |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setMessageAttachment](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setMessageAttachment(com.google.firebase.appindexing.builders.IndexableBuilder<?>...))([IndexableBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\> attachments) Sets the attachments of the message. |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setRecipient](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setRecipient(com.google.firebase.appindexing.builders.PersonBuilder...))([PersonBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) recipients) Sets the recipients of the message.                                    |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setSender](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setSender(com.google.firebase.appindexing.builders.PersonBuilder))([PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) sender) Sets the sender of the message.                                                        |
| [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder) | [setText](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder#setText(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) text) Sets the textual content of the message.                                                                                                                                              |

### Inherited Method Summary

From class [com.google.firebase.appindexing.builders.IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)  

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)                                             | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#build())() Finalize building the object.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20boolean...))([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values) Sets one or multiple boolean values for a property, replacing its previous values.                                                                                                                                                                                                                                       |
| \<S extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\>\> T       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20S...))([String](https://developer.android.com/reference/java/lang/String.html) key, S... values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property.                                                                                                                                                                                |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20com.google.firebase.appindexing.Indexable...))([String](https://developer.android.com/reference/java/lang/String.html) key, [Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property, replacing its previous values. |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20java.lang.String...))([String](https://developer.android.com/reference/java/lang/String.html) key, [String...](https://developer.android.com/reference/java/lang/String.html) values) Sets one or multiple string values for a property, replacing its previous values.                                                                                                                                                               |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20long...))([String](https://developer.android.com/reference/java/lang/String.html) key, long... values) Sets one or multiple long values for a property, replacing its previous values.                                                                                                                                                                                                                                                |
| T                                                                                                                                                           | [setAlternateName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setAlternateName(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) alternateNames) Sets the alternate names for the content.                                                                                                                                                                                                                                                                      |
| final T                                                                                                                                                     | [setDescription](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setDescription(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) description) Sets the optional description of the content.                                                                                                                                                                                                                                                                               |
| T                                                                                                                                                           | [setId](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setId(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) id) Sets the ID for the Indexable.                                                                                                                                                                                                                                                                                                                         |
| final T                                                                                                                                                     | [setImage](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setImage(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) url) Sets the image of the content.                                                                                                                                                                                                                                                                                                                  |
| final \<S extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\>\> T | [setIsPartOf](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setIsPartOf(S...))(S... collections) Sets the sub-group or collection that this Indexable is part of.                                                                                                                                                                                                                                                                                                                                                 |
| final T                                                                                                                                                     | [setKeywords](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setKeywords(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) keywords) Sets the keywords of the Indexable.                                                                                                                                                                                                                                                                                            |
| T                                                                                                                                                           | [setMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setMetadata(com.google.firebase.appindexing.Indexable.Metadata.Builder))([Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) metadataBuilder) Sets the metadata.                                                                                                                                                                                              |
| final T                                                                                                                                                     | [setName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Sets the name of the content, must not be null.                                                                                                                                                                                                                                                                                                  |
| final T                                                                                                                                                     | [setSameAs](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setSameAs(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) webUrl) Sets the corresponding web URL.                                                                                                                                                                                                                                                                                                            |
| final T                                                                                                                                                     | [setUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setUrl(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) url) Sets the URL.                                                                                                                                                                                                                                                                                                                                       |

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Methods

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setDateRead** ([Date](https://developer.android.com/reference/java/util/Date.html) dateRead)

Sets the date on which the message was read.  

##### Parameters

| dateRead | The date on which the message was read. |
|----------|-----------------------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setDateReceived** ([Date](https://developer.android.com/reference/java/util/Date.html) dateReceived)

Sets the date on which the message was received.  

##### Parameters

| dateReceived | The date on which the message was received. |
|--------------|---------------------------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setDateSent** ([Date](https://developer.android.com/reference/java/util/Date.html) dateSent)

Sets the date on which the message was sent.  

##### Parameters

| dateSent | The date on which the message was sent. |
|----------|-----------------------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setMessageAttachment** ([IndexableBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\> attachments)

Sets the attachments of the message.  

##### Parameters

| attachments | The attachments of the message. |
|-------------|---------------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setRecipient** ([PersonBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) recipients)

Sets the recipients of the message.  

##### Parameters

| recipients | The recipients of the message. |
|------------|--------------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setSender** ([PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) sender)

Sets the sender of the message.  

##### Parameters

| sender | The sender of the message. |
|--------|----------------------------|

#### public [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**setText** ([String](https://developer.android.com/reference/java/lang/String.html) text)

Sets the textual content of the message.  

##### Parameters

| text | The textual content of the message. |
|------|-------------------------------------|