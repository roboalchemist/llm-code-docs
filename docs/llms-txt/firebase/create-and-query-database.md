# Source: https://firebase.google.com/docs/firestore/enterprise/create-and-query-database.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

Learn how to create a Cloud Firestore with MongoDB compatibility database and connect to it with the`mongosh`tool.

## Before you begin

1. If you haven't already, create a Firebase project: In the[Firebaseconsole](https://console.firebase.google.com/), click**Add project** , then follow the on-screen instructions to create a Firebase project or to add Firebase services to an existingGoogle Cloudproject.
2. [Install the`mongosh`tool](https://www.mongodb.com/docs/mongodb-shell/install/)

<br />

## Create a Cloud Firestore with MongoDB compatibility database and retrieve the connection string

In theFirebaseconsole, create a new Firestore Enterprise edition database. Cloud Firestore with MongoDB compatibility requires Firestore Enterprise edition:

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Click the database that you want to authenticate.
3. In the**Explorer** panel, clickmore_vert**View more**.
4. Select**Connect using MongoDB tools**.
5. Copy the connection string.

The connection string depends on the UID of the database (system-generated) and the location of database:  

```text
UID.LOCATION.firestore.goog
```

## Create a user for SCRAM authentication

In the Google Cloud console, create a new database user and assign the user Identity and Access Management permissions.

1. In the Google Cloud console, go to the**Databases**page.

   [Go to Databases](https://console.cloud.google.com/firestore/databases)
2. Select the database from the list of databases.
3. In the navigation menu, click**Auth**.
4. Click**Add User**.
5. Enter a username.
6. Select an Identity and Access Management role for the user.
7. Click create. The database creates a user and shows you the user's generated password.**Copy and save this password. You will not be able to retrieve this password later.**.

## Connect using`mongosh`

Use the connection string, username, and password to connect to your database, run`mongosh`locally with the following configuration options.  

```gdscript
mongosh 'mongodb://<var translate="no">USERNAME</var>:<var translate="no">PASSWORD</var>@<var translate="no">CONNECTION_STRING</var>:443/<var translate="no">DATABASE_ID</var>?loadBalanced=true&authMechanism=SCRAM-SHA-256&tls=true&retryWrites=false'
```

Replace the following:

- <var translate="no">USERNAME</var>: the name of the database user you created.
- <var translate="no">PASSWORD</var>: the generated password for the database user you created.
- <var translate="no">CONNECTION_STRING</var>: the database connection string.
- <var translate="no">DATABASE_ID</var>: a database ID

Once connected, you can create and read data, for example:  

```text
db.pages.insertOne({ message: "Hello World!"})
db.pages.find({})
exit
```

## What's next

- [See a list of supported features](https://firebase.google.com/docs/firestore/enterprise/supported-data-types-drivers)
- [Learn about behavior differences in Cloud Firestore with MongoDB compatibility](https://firebase.google.com/docs/firestore/enterprise/behavior-differences)
- [Learn about additional authentication methods](https://firebase.google.com/docs/firestore/enterprise/connect)