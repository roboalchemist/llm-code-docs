# Source: https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md.txt

# FirestoreDataConverter interface

Converter used by `withConverter()` to transform user objects of type `AppModelType` into Firestore data of type `DbModelType`.

Using the converter allows you to specify generic type arguments when storing and retrieving objects from Firestore.

In this context, an "AppModel" is a class that is used in an application to package together related information and functionality. Such a class could, for example, have properties with complex, nested data types, properties used for memoization, properties of types not supported by Firestore (such as `symbol` and `bigint`), and helper functions that perform compound operations. Such classes are not suitable and/or possible to store into a Firestore database. Instead, instances of such classes need to be converted to "plain old JavaScript objects" (POJOs) with exclusively primitive properties, potentially nested inside other POJOs or arrays of POJOs. In this context, this type is referred to as the "DbModel" and would be an object suitable for persisting into Firestore. For convenience, applications can implement `FirestoreDataConverter` and register the converter with Firestore objects, such as `DocumentReference` or `Query`, to automatically convert `AppModel` to `DbModel` when storing into Firestore, and convert `DbModel` to `AppModel` when retrieving from Firestore.

**Signature:**  

    export declare interface FirestoreDataConverter<AppModelType, DbModelType extends DocumentData = DocumentData> 

## Methods

|                                                                           Method                                                                           |                                                                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromFirestore(snapshot, options)](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverterfromfirestore) | Called by the Firestore SDK to convert Firestore data into an object of type `AppModelType`. You can access your data by calling: `snapshot.data(options)`.Generally, the data returned from `snapshot.data()` can be cast to `DbModelType`; however, this is not guaranteed because Firestore does not enforce a schema on the database. For example, writes from a previous version of the application or writes from another client that did not use a type converter could have written data with different properties and/or property types. The implementation will need to choose whether to gracefully recover from non-conforming data or throw an error.To override this method, see . |
| [toFirestore(modelObject)](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconvertertofirestore)           | Called by the Firestore SDK to convert a custom model object of type `AppModelType` into a plain JavaScript object (suitable for writing directly to the Firestore database) of type `DbModelType`. To use `set()` with `merge` and `mergeFields`, `toFirestore()` must be defined with `PartialWithFieldValue<AppModelType>`.The `WithFieldValue<T>` type extends `T` to also allow FieldValues such as [deleteField()](https://firebase.google.com/docs/reference/js/firestore_.md#deletefield) to be used as property values.                                                                                                                                                                 |
| [toFirestore(modelObject, options)](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconvertertofirestore)  | Called by the Firestore SDK to convert a custom model object of type `AppModelType` into a plain JavaScript object (suitable for writing directly to the Firestore database) of type `DbModelType`. Used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad), and with `merge:true` or `mergeFields`.The `PartialWithFieldValue<T>` type extends `Partial<T>` to allow FieldValues such as [arrayUnion()](https://firebase.google.com/docs/reference/js/firestore_.md#arrayunion_7d853aa) to be used as property values. It also supports nested `Partial` by allowing nested fields to be omitted.                                                      |

## FirestoreDataConverter.fromFirestore()

Called by the Firestore SDK to convert Firestore data into an object of type `AppModelType`. You can access your data by calling: `snapshot.data(options)`.

Generally, the data returned from `snapshot.data()` can be cast to `DbModelType`; however, this is not guaranteed because Firestore does not enforce a schema on the database. For example, writes from a previous version of the application or writes from another client that did not use a type converter could have written data with different properties and/or property types. The implementation will need to choose whether to gracefully recover from non-conforming data or throw an error.

To override this method, see .

**Signature:**  

    fromFirestore(snapshot: QueryDocumentSnapshot<DocumentData, DocumentData>, options?: SnapshotOptions): AppModelType;

#### Parameters

| Parameter |                                                                                                                                                                                    Type                                                                                                                                                                                    |                         Description                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| snapshot  | [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\> | A `QueryDocumentSnapshot` containing your data and metadata. |
| options   | [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotoptions.md#snapshotoptions_interface)                                                                                                                                                                                                                                                   | The `SnapshotOptions` from the initial call to `data()`.     |

**Returns:**

AppModelType

## FirestoreDataConverter.toFirestore()

Called by the Firestore SDK to convert a custom model object of type `AppModelType` into a plain JavaScript object (suitable for writing directly to the Firestore database) of type `DbModelType`. To use `set()` with `merge` and `mergeFields`, `toFirestore()` must be defined with `PartialWithFieldValue<AppModelType>`.

The `WithFieldValue<T>` type extends `T` to also allow FieldValues such as [deleteField()](https://firebase.google.com/docs/reference/js/firestore_.md#deletefield) to be used as property values.

**Signature:**  

    toFirestore(modelObject: WithFieldValue<AppModelType>): WithFieldValue<DbModelType>;

#### Parameters

|  Parameter  |                                                     Type                                                     | Description |
|-------------|--------------------------------------------------------------------------------------------------------------|-------------|
| modelObject | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#withfieldvalue)\<AppModelType\> |             |

**Returns:**

[WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#withfieldvalue)\<DbModelType\>

## FirestoreDataConverter.toFirestore()

Called by the Firestore SDK to convert a custom model object of type `AppModelType` into a plain JavaScript object (suitable for writing directly to the Firestore database) of type `DbModelType`. Used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad), and with `merge:true` or `mergeFields`.

The `PartialWithFieldValue<T>` type extends `Partial<T>` to allow FieldValues such as [arrayUnion()](https://firebase.google.com/docs/reference/js/firestore_.md#arrayunion_7d853aa) to be used as property values. It also supports nested `Partial` by allowing nested fields to be omitted.

**Signature:**  

    toFirestore(modelObject: PartialWithFieldValue<AppModelType>, options: SetOptions): PartialWithFieldValue<DbModelType>;

#### Parameters

|  Parameter  |                                                            Type                                                            | Description |
|-------------|----------------------------------------------------------------------------------------------------------------------------|-------------|
| modelObject | [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#partialwithfieldvalue)\<AppModelType\> |             |
| options     | [SetOptions](https://firebase.google.com/docs/reference/js/firestore_.md#setoptions)                                       |             |

**Returns:**

[PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#partialwithfieldvalue)\<DbModelType\>

### Example

Simple Example  

    const numberConverter = {
        toFirestore(value: WithFieldValue<number>) {
            return { value };
        },
        fromFirestore(snapshot: QueryDocumentSnapshot, options: SnapshotOptions) {
            return snapshot.data(options).value as number;
        }
    };

    async function simpleDemo(db: Firestore): Promise<void> {
        const documentRef = doc(db, 'values/value123').withConverter(numberConverter);

        // converters are used with `setDoc`, `addDoc`, and `getDoc`
        await setDoc(documentRef, 42);
        const snapshot1 = await getDoc(documentRef);
        assertEqual(snapshot1.data(), 42);

        // converters are not used when writing data with `updateDoc`
        await updateDoc(documentRef, { value: 999 });
        const snapshot2 = await getDoc(documentRef);
        assertEqual(snapshot2.data(), 999);
    }

Advanced Example  

    // The Post class is a model that is used by our application.
    // This class may have properties and methods that are specific
    // to our application execution, which do not need to be persisted
    // to Firestore.
    class Post {
        constructor(
            readonly title: string,
            readonly author: string,
            readonly lastUpdatedMillis: number
        ) {}
        toString(): string {
            return `${this.title} by ${this.author}`;
        }
    }

    // The PostDbModel represents how we want our posts to be stored
    // in Firestore. This DbModel has different properties (`ttl`,
    // `aut`, and `lut`) from the Post class we use in our application.
    interface PostDbModel {
        ttl: string;
        aut: { firstName: string; lastName: string };
        lut: Timestamp;
    }

    // The `PostConverter` implements `FirestoreDataConverter` and specifies
    // how the Firestore SDK can convert `Post` objects to `PostDbModel`
    // objects and vice versa.
    class PostConverter implements FirestoreDataConverter<Post, PostDbModel> {
        toFirestore(post: WithFieldValue<Post>): WithFieldValue<PostDbModel> {
            return {
                ttl: post.title,
                aut: this._autFromAuthor(post.author),
                lut: this._lutFromLastUpdatedMillis(post.lastUpdatedMillis)
            };
        }

        fromFirestore(snapshot: QueryDocumentSnapshot, options: SnapshotOptions): Post {
            const data = snapshot.data(options) as PostDbModel;
            const author = `${data.aut.firstName} ${data.aut.lastName}`;
            return new Post(data.ttl, author, data.lut.toMillis());
        }

        _autFromAuthor(
            author: string | FieldValue
        ): { firstName: string; lastName: string } | FieldValue {
            if (typeof author !== 'string') {
                // `author` is a FieldValue, so just return it.
                return author;
            }
            const [firstName, lastName] = author.split(' ');
            return {firstName, lastName};
        }

        _lutFromLastUpdatedMillis(
            lastUpdatedMillis: number | FieldValue
        ): Timestamp | FieldValue {
            if (typeof lastUpdatedMillis !== 'number') {
                // `lastUpdatedMillis` must be a FieldValue, so just return it.
                return lastUpdatedMillis;
            }
            return Timestamp.fromMillis(lastUpdatedMillis);
        }
    }

    async function advancedDemo(db: Firestore): Promise<void> {
        // Create a `DocumentReference` with a `FirestoreDataConverter`.
        const documentRef = doc(db, 'posts/post123').withConverter(new PostConverter());

        // The `data` argument specified to `setDoc()` is type checked by the
        // TypeScript compiler to be compatible with `Post`. Since the `data`
        // argument is typed as `WithFieldValue<Post>` rather than just `Post`,
        // this allows properties of the `data` argument to also be special
        // Firestore values that perform server-side mutations, such as
        // `arrayRemove()`, `deleteField()`, and `serverTimestamp()`.
        await setDoc(documentRef, {
            title: 'My Life',
            author: 'Foo Bar',
            lastUpdatedMillis: serverTimestamp()
        });

        // The TypeScript compiler will fail to compile if the `data` argument to
        // `setDoc()` is _not_ compatible with `WithFieldValue<Post>`. This
        // type checking prevents the caller from specifying objects with incorrect
        // properties or property values.
        // @ts-expect-error "Argument of type { ttl: string; } is not assignable
        // to parameter of type WithFieldValue<Post>"
        await setDoc(documentRef, { ttl: 'The Title' });

        // When retrieving a document with `getDoc()` the `DocumentSnapshot`
        // object's `data()` method returns a `Post`, rather than a generic object,
        // which would have been returned if the `DocumentReference` did _not_ have a
        // `FirestoreDataConverter` attached to it.
        const snapshot1: DocumentSnapshot<Post> = await getDoc(documentRef);
        const post1: Post = snapshot1.data()!;
        if (post1) {
            assertEqual(post1.title, 'My Life');
            assertEqual(post1.author, 'Foo Bar');
        }

        // The `data` argument specified to `updateDoc()` is type checked by the
        // TypeScript compiler to be compatible with `PostDbModel`. Note that
        // unlike `setDoc()`, whose `data` argument must be compatible with `Post`,
        // the `data` argument to `updateDoc()` must be compatible with
        // `PostDbModel`. Similar to `setDoc()`, since the `data` argument is typed
        // as `WithFieldValue<PostDbModel>` rather than just `PostDbModel`, this
        // allows properties of the `data` argument to also be those special
        // Firestore values, like `arrayRemove()`, `deleteField()`, and
        // `serverTimestamp()`.
        await updateDoc(documentRef, {
            'aut.firstName': 'NewFirstName',
            lut: serverTimestamp()
        });

        // The TypeScript compiler will fail to compile if the `data` argument to
        // `updateDoc()` is _not_ compatible with `WithFieldValue<PostDbModel>`.
        // This type checking prevents the caller from specifying objects with
        // incorrect properties or property values.
        // @ts-expect-error "Argument of type { title: string; } is not assignable
        // to parameter of type WithFieldValue<PostDbModel>"
        await updateDoc(documentRef, { title: 'New Title' });
        const snapshot2: DocumentSnapshot<Post> = await getDoc(documentRef);
        const post2: Post = snapshot2.data()!;
        if (post2) {
            assertEqual(post2.title, 'My Life');
            assertEqual(post2.author, 'NewFirstName Bar');
        }
    }