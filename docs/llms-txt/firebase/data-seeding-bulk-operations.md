# Source: https://firebase.google.com/docs/data-connect/data-seeding-bulk-operations.md.txt

<br />

InFirebase Data Connect, you can perform bulk data loads and updates in different ways depending on your workflows and environments:

- In**local prototyping** , when you are trying alternative schemas, data seeding mutations can be created and called in a local development environment using the VS Code extension, theData Connectemulator, and a local database instance.

- In**production development**, with a stable schema, when you're performing larger CI/CD flows and managing production data, you have two options:

  - The preferred approach is to use theFirebaseAdmin SDK, a set of libraries that run in privileged environments.

  - You can also use SQL tools with your Cloud SQL instance to perform bulk loads and updates, as long as you are modifying*data* and not your*database schema* . Modifying your database schema directly with SQL tools can break yourData Connectschema and connectors.

## Local prototyping: seed data in local instances

In the[Get started guide](https://firebase.google.com/docs/data-connect/quickstart), you set up an app to add a single record to a single table using an ad hoc insert mutation.

To be usable, the movie review app needs data for movies, reviews, and users for prototyping queries and mutations that use joins and other operations on multiple tables with realistic data. You can expand your schema and seed your database.
| **Tip:** You can access the sample data and code used in this guide by checking out one of ourData Connectquickstarts.

Your prototyping environment needs code to perform data seeding. This guide provides some samples, illustrating:

- Use of`_insertMany`and`_upsertMany`on individual tables
- Use of`_insertMany`on related tables

### Update the movie review app schema

You can use`_insertMany`and`_upsertMany`mutations to update individual database tables one at a time, or update multiple tables related by join relationships. An expanded movie review app schema that helps illustrate these use cases and examples is shown below. It expands`schema.gql`beyond the starting`Movie`type to include`Actor`and`MovieActor`types, so we can prototype more complex queries.
| **Note:** The schema for the movie review app is covered in detail in the[guide for schemas, queries and mutations](https://firebase.google.com/docs/data-connect/schemas-queries-mutations).
**Note:** If you're prototyping with your production service, remember to deploy your schema updates before inserting data and testing new operations.  

    # Actors
    # Suppose an actor can participate in multiple movies and movies can have multiple actors
    # Movie - Actors (or vice versa) is a many to many relationship
    type Actor @table {
      id: UUID!
      imageUrl: String! 
      name: String! @col(name: "name", dataType: "varchar(30)")
    }

    # Join table for many-to-many relationship for movies and actors
    # The 'key' param signifies the primary key(s) of this table
    # In this case, the keys are [movieId, actorId], the generated fields of the reference types [movie, actor]
    type MovieActor @table(key: ["movie", "actor"]) {
      # @ref creates a field in the current table (MovieActor) that holds the primary key of the referenced type
      # In this case, @ref(fields: "movieId", references: "id") is implied
      movie: Movie!
      # movieId: UUID! <- this is created by the implied @ref
      actor: Actor!
      # actorId: UUID! <- this is created by the implied @ref
      role: String! # "main" or "supporting"
    }

### Write mutations to seed zero state data

During prototyping, when your queries and mutations need to be tested against a range of discrete values, you can populate data with multiple records. For example, you might want to add multiple movie records with different types of genres and ratings for testing comparisons and filtering.

#### Seed data into the`Movie`and`Actor`tables

Depending on your stage of prototyping, you can use the same technique introduced in the Get started guide to insert one or two records: that is, you can use CodeLenses in the VS Code extension to create`_insert`mutations, hard-code data, and[**Run**those mutations in VS Code](https://firebase.google.com/docs/data-connect/quickstart#add_data_to_your_tables).

Eventually, it makes more sense to add many records into a table using an`_insertMany`operation. In the movie review app example, this inserts an initial set of data in`Movie`and`Actor`.

To execute the following mutations, using the VS Code Firebase extension, in the appropriate file editor view, click the**Run (Production)** or**Run (Local)**CodeLens buttons, depending on whether you are prototyping with your production service or a local database.  

    # insertMany for Movie
    # 2 records shown
    mutation {
      movie_insertMany(data: [
        {
          id: "550e8400-e29b-41d4-a716-446655440000",
          title: "Inception",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Finception.jpg?alt=media&token=07b09781-b302-4623-a5c3-1956d0143168",
          genre: "sci-fi",
        },
        {
          id: "550e8400-e29b-41d4-a716-446655440001",
          title: "The Matrix",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Fthe_matrix.jpg?alt=media&token=4975645d-fef8-409e-84a5-bcc1046e2059",
          genre: "action",
        }
      ])
    }

    # insertMany for Actor
    # 2 records shown
    mutation {
      actor_insertMany(data: [
        {
          id: "123e4567-e89b-12d3-a456-426614174000",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/actors%2Fdicaprio.jpeg?alt=media&token=452e030a-efa5-4ef4-bb81-502b23241316",
          name: "Leonardo DiCaprio"
        },
        {
          id: "123e4567-e89b-12d3-a456-426614174001",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/actors%2Fkeanu.jpg?alt=media&token=6056520c-ef3e-4823-aad0-108aab163115",
          name: "Keanu Reeves"
        }
       ])
    }

#### Seed data into`MovieActor`join table

To test queries and mutations using joins and other complex operations, you can add multiple records to the`MovieActor`table.

Here, when you are updating multiple tables in this kind of relation, you can add the`@transaction`directive to ensure the update completes properly.
**Note:** Correct records in`Movie`and`Actor`must exist for the`_insertMany`operations to succeed.  

    mutation @transaction {
      movie_insertMany(data: [
        {
          id: "550e8400-e29b-41d4-a716-446655440000",
          title: "Inception",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Finception.jpg?alt=media&token=07b09781-b302-4623-a5c3-1956d0143168",
          genre: "sci-fi",
        },
        {
          id: "550e8400-e29b-41d4-a716-446655440001",
          title: "The Matrix",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Fthe_matrix.jpg?alt=media&token=4975645d-fef8-409e-84a5-bcc1046e2059",
          genre: "action",
        }
      ])

      actor_insertMany(data: [
        {
          id: "123e4567-e89b-12d3-a456-426614174000",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/actors%2Fdicaprio.jpeg?alt=media&token=452e030a-efa5-4ef4-bb81-502b23241316",
          name: "Leonardo DiCaprio"
        },
        {
          id: "123e4567-e89b-12d3-a456-426614174001",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/actors%2Fkeanu.jpg?alt=media&token=6056520c-ef3e-4823-aad0-108aab163115",
          name: "Keanu Reeves"
        }
      ])
    }

### Write a mutation to reset seed data

While prototyping and performing CI/CD, resetting the data to a zero state for executing a new series of tests on a new set of data can be useful.

To do so, if your prototype code does't add records to your tables, use the`_upsertMany`mutation provided byData Connect.
| **Note:** Alternatively, you can call`_deleteMany(all:true)`followed by`_insertMany`to reset your data.

In the following example,`movie_upsertMany`is called with the initial values to update movie records to their original state.  

    mutation {
      # Execute an upsertMany operation to update the Movie table
      movie_upsertMany(data: [
        {
          id: "550e8400-e29b-41d4-a716-446655440000",
          title: "Inception",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Finception.jpg?alt=media&token=07b09781-b302-4623-a5c3-1956d0143168",
          genre: "sci-fi",
        },
        {
          id: "550e8400-e29b-41d4-a716-446655440001",
          title: "The Matrix",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Fthe_matrix.jpg?alt=media&token=4975645d-fef8-409e-84a5-bcc1046e2059",
          genre: "action",
        }
       ...
    }

## Production development: use theAdmin SDKto populate and update

TheFirebaseAdmin SDKis available for when you want to work from privileged environments. This is an important use case when you want to load thousands of records, given the critical nature of bulk data operations on your production data.

### Install theFirebaseAdmin SDK

Even if you mainly work locally, Firebase recommends setting up theAdmin SDKso you can useFirebase Data Connectfrom a privileged environment, including your local environment. You'll need to[set up theAdmin SDK](https://firebase.google.com/docs/admin/setup)for Node.js.

You can learn more about[using the Admin SDK in otherData Connectuse cases](https://firebase.google.com/docs/data-connect/admin-sdk).

### Perform bulk loads and updates of production data

The API for bulk data management builds GraphQL mutations on your behalf, rather than asking you to build`mutation {...}`strings with the`executeGraphQL`API described earlier for adding a few rows here and there locally.

A major benefit of the administrative API is the ability to separately manage and re-use arrays of data for CI/CD flows, or set up large bulk data files for production data.

The following snippets demonstrate how to set up a bulk-data script.  

    import { initializeApp } from 'firebase-admin/app';
    import { getDataConnect } from 'firebase-admin/data-connect';

    const app = initializeApp();

    const dc = getDataConnect({ location: "us-west2", serviceId: "my-service" });

    const data = [
     {
          id: "550e8400-e29b-41d4-a716-446655440000",
          title: "Inception",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Finception.jpg?alt=media&token=07b09781-b302-4623-a5c3-1956d0143168",
          genre: "sci-fi",
      },
      {
          id: "550e8400-e29b-41d4-a716-446655440001",
          title: "The Matrix",
          imageUrl: "https://firebasestorage.googleapis.com/v0/b/fdc-quickstart-web.appspot.com/o/movies%2Fthe_matrix.jpg?alt=media&token=4975645d-fef8-409e-84a5-bcc1046e2059",
          genre: "action",
        }
    ];

    // Methods of the bulk operations API
    const resp = await dc.insert("movie" /*table name*/, data[0]);
    // Or
    const resp = await dc.insertMany("movie" /*table name*/, data);

    // Or
    const resp = await dc.upsert("movie" /*table name*/, data[0]);
    // Or
    const resp = await dc.upsertMany("movie" /*table name*/, data);

## Production development: use SQL for bulk data updates

When you're working with a stable schema in production, and are not modifying your schema, you can work in your Cloud SQL instance to manage data loads and updates.
| **Note:** Modifying your database*schema* directly with SQL tools can break yourData Connectschema and connectors.

Refer to the[Cloud SQL for PostgreSQL guide for importing data](https://cloud.google.com/sql/docs/postgres/import-export/import-export-dmp).

## What's next?

- Learn about[integrating theAdmin SDKinto yourData Connectprojects](https://firebase.google.com/docs/data-connect/admin-sdk).