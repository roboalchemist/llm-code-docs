# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.FirestoreDataConverter.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreDataConverter.md.txt

# FirestoreDataConverter | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- FirestoreDataConverter
\< T \>

Converter used by `withConverter()` to transform user objects of type T
into Firestore data.

Using the converter allows you to specify generic type arguments when
storing and retrieving objects from Firestore.

example
:

        class Post {
          constructor(readonly title: string, readonly author: string) {}

          toString(): string {
            return this.title + ', by ' + this.author;
          }
        }

        const postConverter = {
          toFirestore(post: Post): firebase.firestore.DocumentData {
            return {title: post.title, author: post.author};
          },
          fromFirestore(
            snapshot: firebase.firestore.QueryDocumentSnapshot,
            options: firebase.firestore.SnapshotOptions
          ): Post {
            const data = snapshot.data(options)!;
            return new Post(data.title, data.author);
          }
        };

        const postSnap = await firebase.firestore()
          .collection('posts')
          .withConverter(postConverter)
          .doc().get();
        const post = postSnap.data();
        if (post !== undefined) {
          post.title; // string
          post.toString(); // Should be defined
          post.someNonExistentProperty; // TS error
        }


### Type parameters

-

  #### T

## Index

### Methods

- [fromFirestore](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreDataConverter#fromfirestore)
- [toFirestore](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreDataConverter#tofirestore)

## Methods

### fromFirestore

- fromFirestore ( snapshot : [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.QueryDocumentSnapshot) , options : [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions) ) : T
- Called by the Firestore SDK to convert Firestore data into an object of
  type T. You can access your data by calling: `snapshot.data(options)`.

  #### Parameters

  -

    ##### snapshot: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/node/firebase.firestore.QueryDocumentSnapshot)

    A QueryDocumentSnapshot containing your data and metadata.
  -

    ##### options: [SnapshotOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SnapshotOptions)

    The SnapshotOptions from the initial call to `data()`.

  #### Returns T

### toFirestore

- toFirestore ( modelObject : T ) : [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)
- Called by the Firestore SDK to convert a custom model object of type T
  into a plain Javascript object (suitable for writing directly to the
  Firestore database). To use `set()` with `merge` and `mergeFields`,
  `toFirestore()` must be defined with `Partial<T>`.

  #### Parameters

  -

    ##### modelObject: T

  #### Returns [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)

- toFirestore ( modelObject : Partial \< T \> , options : [SetOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SetOptions) ) : [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)
-

  #### Parameters

  -

    ##### modelObject: Partial\<T\>

  -

    ##### options: [SetOptions](https://firebase.google.com/docs/reference/node/firebase.firestore.SetOptions)

  #### Returns [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)