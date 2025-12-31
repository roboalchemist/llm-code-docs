# Source: https://firebase.google.com/docs/reference/app-indexing/index-builders.md.txt

### Stickers

This is an overview of the most important properties to include when indexing stickers or sticker packs for integration with Gboard. See the[App Indexing sample](https://github.com/firebase/quickstart-android/tree/master/app-indexing)on Github for an example.

|    Property     |                                                    Description                                                    |                  Example                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| **name**        | Name or keyword used for search --- not displayed.                                                                | "Snoopy Sticker Pack"                      |
| **url**         | URL linking to the sticker or sticker pack in the app.                                                            | "http://sticker/pack/canonical/url/snoopy" |
| **image**       | The sticker or sticker pack graphic. For optimal image quality, use square images sized 320 pixels or 500 pixels. | "http://link/to/the/image/bye"             |
| **description** | Accessibility label for your sticker or sticker pack.                                                             | "A pack of Snoopy stickers"                |

#### Example: Sticker pack

```scilab
// Build and index the sticker objects on first run after update or install
// to minimize lag between sticker install and stickers surfacing in Gboard.

FirebaseAppIndex.update(new Indexable.Builder("StickerPack")
   .setName("Snoopy Pack")
   .setImage("content://sticker/pack/canonical/image")
   // see: Support links to your app content section
   .setUrl("http://sticker/pack/canonical/url/snoopy")
   // Set the accessibility label for the sticker pack.
   .setDescription("A sticker pack of Snoopy")
   .put("hasSticker",
        new Indexable.Builder("Sticker")
          .setName("Hey")
          .setImage("http://link/to/the/image/hey")
          .setDescription("A Snoopy hey sticker.")
          .build(),
       new Indexable.Builder("Sticker")
          .setName("Bye")
          .setImage("http://link/to/the/image/bye")
          .setDescription("A Snoopy bye sticker.")
          .build())
   .build());
```

#### Example: Individual sticker

```css+lasso
Indexable[] stickers = new Indexable[]{
      new Indexable.Builder("Sticker")
   .setName("Hey")
   .setImage("http://www.snoopysticker.com?id=1234")
   // see: Support links to your app content section
   .setUrl("http://sticker/canonical/image/hey")
   // Set the accessibility label for the sticker.
   .setDescription("A sticker for hi")
   // Add search keywords.
   .put("keywords", "hey", "snoopy", "hi", "hello")
   .put("isPartOf",
        new Indexable.Builder("StickerPack")
          .setName("Snoopy Pack"))
          .build())
   .build()),
new Indexable.Builder("Sticker")
   .setName("Bye")
   .setImage("http://www.snoopysticker.com?id=4567")
   // see: Support links to your app content section
   .setUrl("http://sticker/canonical/image/bye")
   // Set the accessibility label for the sticker.
   .setDescription("A sticker for Bye")
   // Add search keywords.
   .put("keywords", "bye", "snoopy", "see ya", "good bye")
   .put("isPartOf",
        new Indexable.Builder("StickerPack")
          .setName("Snoopy Pack")
          .build())
   .build())};
// Make sure we update stickers in batch
FirebaseAppIndex.update(stickers);
```

### Message

This is an overview of the most important properties that should be specified by an app when indexing a message.

|           Property            |                                                                     Description                                                                      |               Example                |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| **`url`**                     | The URL linking to the message in the app.                                                                                                           | "myapp://messages/42"                |
| **`name`**                    | The subject line of the message, or directly the message itself, if it does not have a separate subject line.                                        | "Re: lunch"                          |
| **`text`**                    | **Optional.**The body of the message, if applicable. For instant messaging type of messages without a separate subject line, use "name" (see above). | "Are you free for lunch?"            |
| **`dateReceived`**            | The time the message was received, for incoming messages.                                                                                            | new Date(2016, 6, 2, 23, 43, 00)     |
| **`dateSent`**                | The time the message was sent, for outgoing messages.                                                                                                | new Date(2016, 6, 2, 23, 43, 00)     |
| **`isPartOf.id`**             | An ID for the conversation or thread that the message is a part of.                                                                                  | "42"                                 |
| **`sender`**                  | The sender of the message.                                                                                                                           |                                      |
| **`sender.name`**             | The name of the sender.                                                                                                                              | "Alice"                              |
| **`sender.url`**              | **Optional.**The URL linking to the person in the app.                                                                                               | "http://example.net/profiles/alice"  |
| **`sender.image`**            | **Optional.**An image of the sender. Either a web URL or Content URI may be used.                                                                    | "http://example.net/alice.jpg"       |
| **`sender.email`**            | **Optional.**The email address of the sender.                                                                                                        | "alice@example.net"                  |
| **`sender.telephone`**        | **Optional.**The phone number of the sender.                                                                                                         | "+16502530000"                       |
| **`sender.isSelf`**           | Indication of whether the user is the sender. The default is false.                                                                                  | false                                |
| **`recipient`**               | One or multiple recipients of the message.                                                                                                           |                                      |
| **`recipient.name`**          | The name of the recipient.                                                                                                                           | "Bob"                                |
| **`recipient.url`**           | **Optional.**The URL linking to the person in the app.                                                                                               | "http://example.net/profiles/bob"    |
| **`recipient.image`**         | **Optional.**An image of the recipient. Either a web URL or Content URI may be used.                                                                 | "http://example.net/bob.jpg"         |
| **`recipient.email`**         | **Optional.**The email address of the sender.                                                                                                        | "bob@example.net"                    |
| **`recipient.telephone`**     | **Optional.**The phone number of the sender.                                                                                                         | "+16502530000"                       |
| **`recipient.isSelf`**        | Indication of whether the user is the recipient. The default is false.                                                                               | true                                 |
| **`messageAttachment`**       | **Optional.**One or multiple attachments to the message.                                                                                                                                   ||
| **`messageAttachment.name`**  | The name of the attachment to the message.                                                                                                           | "Sticker"                            |
| **`messageAttachment.image`** | An image representing the attachment. Either a web URL or Content URI may be used.                                                                   | "http://example.net/stickers/23.png" |

#### Example: Incoming message

```carbon
Indexable message = Indexables.messageBuilder()
    .setUrl("myapp://messages/42")
    .setText("Are you free for lunch?")
    .setDateReceived(new Date(2016, 6, 2, 23, 44, 00))
    .setIsPartOf(Indexables.conversationBuilder().setId("42")
    .setSender(Indexables.personBuilder()
        .setName("Alice")
        .setImage("http://example.net/alice.jpg")
        .setEmail("alice@example.net")
        .setTelephone("+16502530000"))
    .setRecipient(Indexables.personBuilder()
        .setName("Bob")
        .setImage("http://example.net/bob.jpg")
        .setEmail("bob@people.net")
        .setTelephone("+16502530000")
        .setIsSelf(true))
    .build();
 
```

**For email messages,** use`Indexables.emailMessageBuilder()`instead. There is no difference in the supported fields, but the result UI will be different (e.g. highlighting the subject line of the email).

### Note

This is an overview of the most important properties that should be specified by an app when indexing a note.

|     Property      |                                                  Description                                                  |              Example              |
|-------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------|
| **`url`**         | The URL linking to the note in the app.                                                                       | "myapp://notes/42"                |
| **`name`**        | The title of the note, or directly the note text itself, if it does not have a separate title.                | "Shopping list"                   |
| **`text`**        | **Optional.**The text of the note, if applicable. For notes without a separate title, use "name" (see above). | "steak, pasta, wine"              |
| **`image`**       | An image representing the note. Either a web URL or Content URI may be used.                                  | "http://example.net/shopping.jpg" |
| **`dateCreated`** | The creation time of the note.                                                                                | new Date(2016, 6, 2, 23, 43, 00)  |
| **`author`**      | **Optional.**The author of the note.                                                                                                             ||
| **`author.name`** | The name of the note's author.                                                                                | "Bob"                             |

#### Example: Note

```css+lasso
Indexable note = Indexables.noteDigitalDocumentBuilder()
    .setUrl("myapp://notes/42")
    .setName("Shopping list")
    .setText("steak, pasta, wine")
    .setImage("http://example.net/shopping.jpg")
    .setDateCreated(new Date(2016, 6, 2, 23, 43, 00))
    .build();
```