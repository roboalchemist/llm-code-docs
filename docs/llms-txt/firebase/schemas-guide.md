# Source: https://firebase.google.com/docs/data-connect/schemas-guide.md.txt

<br />

WithFirebase Data Connect, you design a GraphQL schema that represents the data model required for your application.Data Connectconverts this schema to the Cloud SQL for PostgreSQL instance that backs your app. You then author queries and mutations to interface with the backend and bundle these operations into connectors for using your data from client code.

Data Connectoffers AI tooling to help you design and implement your schemas. This guide introduces important concepts of schema design to support and complement your standard and AI-assisted workflows when you[start developing an app](https://firebase.google.com/docs/data-connect/quickstart), and[beyond](https://firebase.google.com/docs/data-connect/ai-assistance).
| **Note:**Follow the complete series on building Data Connect schemas and connectors, which covers:
|
| - Schema development (this guide)
| - [Query development](https://firebase.google.com/docs/data-connect/queries-guide)
| - [Mutation development](https://firebase.google.com/docs/data-connect/mutations-guide)

The[Get started guide](https://firebase.google.com/docs/data-connect/quickstart)introduced a movie review app schema for PostgreSQL.

This guide develops that schema further and provides a[SQL listing](https://firebase.google.com/docs/data-connect/schemas-guide#equivalent-sql)equivalent to the final movie review app schema.

## The schema for a movie review app

Imagine you want to build a service that lets users submit and view movie reviews.

You need an initial schema for such an app to support basic queries. You will extend this schema later to create complex relational queries.

InData Connect, you'll define*GraphQL types*to define the shape of the data your clients can query and manipulate. When you write your schema, your types are translated to Cloud SQL for PostgreSQL tables, most often in a direct relationship between GraphQL types and database tables, though other mappings are possible. This guide shows some examples from basic to more advanced.

### Define a basic`Movie`type

You can start with a`Movie`type.

The schema for`Movie`contains core directives like:

- `@table(name)`and`@col(name)`to customize the SQL table and column names. Data Connect generates snake_case names if not specified.
- `@col(dataType)`to customize SQL column types.
- `@default`to configure SQL column default values during insert.

For more details, check out the reference docs for[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table),[`@col`](https://firebase.google.com/docs/reference/data-connect/gql/directive#col),[`@default`](https://firebase.google.com/docs/reference/data-connect/gql/directive#default).
**Note:** The underscore character,`_`, cannot be used in field names.Data Connectuses that character when it generates supplemental fields, and implicit queries and mutations.  

    # Movies
    type Movie @table(name: "movie", key: "id") {
      id: UUID! @col(name: "movie_id") @default(expr: "uuidV4()")
      title: String!
      releaseYear: Int
      genre: String @col(dataType: "varchar(20)")
      rating: Int
      description: String
    }

### Store important user data automatically in a`User`type

Your app will keep track of users, so you need a`User`type.

The`@default`directive is especially useful in this case. The`id`field here can automatically grab the user's ID from authentication: note the use of`@default(expr: "auth.uid")`in the following sample.  

    # Users
    # Suppose a user can leave reviews for movies
    type User @table {
      id: String! @default(expr: "auth.uid")
      username: String! @col(dataType: "varchar(50)")
    }

| **Tip:** The complete set of GraphQL language extensions forData Connectis[documented in the language reference guide](https://firebase.google.com/docs/reference/data-connect).

### Key scalars and server values

Before looking more at the movie review app, it's important to introduceData Connect*key scalars* and*server values*.

**Key scalars** are concise object identifiers thatData Connectautomatically assembles from key fields in your schemas. Key scalars are about efficiency, allowing you to find in a single call information about the identity and structure of your data. They are especially useful when you want to perform sequential actions on new records and need a unique identifier to pass to upcoming operations, and also when you want to access relational keys to perform additional more complex operations.

Using**server values** , you can effectively let the server dynamically populate fields in your tables using stored or readily-computable values according to particular server-side CEL expressions in the`expr`argument. For example, you can define a field with a timestamp applied when the field is accessed using the time stored in an operation request,`updatedAt: Timestamp!
@default(expr: "request.time")`.

### Handle many-to-many relationships in`Actor`and`MovieActor`types

With users handled, you can get back to modeling movie data.

Next, you want actors to star in your movies.

The`Actor`table is pretty straightforward.  

    # Actors
    # Suppose an actor can participate in multiple movies and movies can have multiple actors
    # Movie - Actors (or vice versa) is a many to many relationship
    type Actor @table {
      id: UUID! @default(expr: "uuidV4()")
      name: String! @col(dataType: "varchar(30)")
    }

If you want actors to be in multiple movies and movies to have multiple actors, you'll need a "join table."

The`MovieActor`table handles the**many-to-many** relationship, and its primary key is a combination of`[movie, actor]`(the foreign key fields from`movie`and`actor`).  

    # Join table for many-to-many relationship for movies and actors
    # The 'key' param signifies the primary keys of this table
    # In this case, the keys are [movieId, actorId], the foreign key fields of the reference fields [movie, actor]
    type MovieActor @table(key: ["movie", "actor"]) {
      movie: Movie!
      # movieId: UUID! <- implicitly added foreign key field
      actor: Actor!
      # actorId: UUID! <- implicitly added foreign key field
      role: String! # "main" or "supporting"
      # optional other fields
    }

When you define a SQL relationship on the table with a foreign key constraint,Data Connectautomatically generates the corresponding field on the other side. You don't need to define the reverse mapping field (e.g., from`Actor`back to`MovieActor`).
| **Note:** Relations are defined on one side, not both!Data Connectgenerates names with underscores (like`actors_on_movies`and`actors_via_actormovie`) to avoid clashes with your own field names.

### Handle one-to-one relationships in a`MovieMetadata`type

Now, keep track of movie directors, as well as set up a**one-to-one** relationship with`Movie`.

You can use the`@ref`directive to customize foreign key constraints:

- `@ref(fields)`specifies which foreign key fields to use.
- `@ref(references)`specifies the fields referenced in the target table (defaults to the primary key, but`@unique`fields work too). This is a more advanced option;Data Connectcan often infer this for you.

For more details, check out the reference docs for[`@ref`](https://firebase.google.com/docs/reference/data-connect/gql/directive#ref).  

    # Movie Metadata
    # Movie - MovieMetadata is a one-to-one relationship
    type MovieMetadata @table {
      # @unique ensures that each Movie only has one MovieMetadata.
      movie: Movie! @unique
      # Since it references to another table type, it adds a foreign key constraint.
      #  movie: Movie! @unique @ref(fields: "movieId", references: "id")
      #  movieId: UUID! <- implicitly added foreign key field
      director: String
    }

## Use fields generated from your schema to build operations

YourData Connectoperations will extend a set of fields automatically generated byData Connectbased on the types and type relationships in your schema. These fields are generated by local tooling whenever you edit your schema.
| **Tip:** To discover the generated fields while building operations, use the query editor in theFirebaseconsole, or our Visual Studio Code extension.

Assume your schema contains a`Movie`type and an associated`Actor`type.Data Connectgenerates`movie`,`movies`,`actors_on_movies`fields, and more.
**Note:** These query fields let you pass a*key scalar* type, here a`Movie_Key`, to identify records. These are created based on your schema.  

### Query with the
`movie`field

|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| The`movie`field represents a single record in the`Movie`table. | Use this field to query a single movie by its key. ```graphql query GetMovie($myKey: Movie_Key!) { movie(key: $myKey) { title } } ``` |

### Query with the
`movies`field

|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The`movies`field represents a list of records in the`Movie`table. | Use this field to query multiple movies, for example, all movies with a given year. ```graphql query GetMovies($myYear: Int!) { movies(where: { year: { eq: $myYear } }) { title } } ``` |

### Query with the
`actors_on_movies`field

|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The`actors_on_movies`field represents a list of records that connect`Actor`and`Movie`tables. Use this field to query all actors associated with a given movie. | Use this field to query all actors associated with a given movie. ```graphql query GetActorsOnMovie($myKey: Movie_Key!) { actors_on_movies(where: { movie: { key: { eq: $myKey } } }) { actor { name } } } ``` |

| **Tip:** The schema definition language also lets you explicitly control how names are generated for fields using[`singular`and`plural`arguments for the`@table`directive](https://firebase.google.com/docs/reference/data-connect/gql/directive#customizations_2).

With this in mind, you can read how to implement operations using these fields in the[guide to implementing queries](https://firebase.google.com/docs/data-connect/queries-guide)and[guide to implementing mutations](https://firebase.google.com/docs/data-connect/mutations-guide).
| **Note:** See the[quickstart guide](https://firebase.google.com/docs/data-connect/quickstart)or[local quickstart guide](https://firebase.google.com/docs/data-connect/quickstart-local)for more on how to discover auto-generated fields.

## More advanced schema concepts

### Enumeration fields

Data Connectsupports enumeration fields that map to PostgreSQL enumerated types. Enums let you quickly define a list of static, predefined values with a specific order.

To add an enum to your schema, declare the enum and its predefined values, then reference it in your type.
| **Note:** The following rules apply to enum fields.
|
| - By convention, the enum**name** :
|   - should start with a capital letter and be in PascalCase (e.g.,`ContentRating`or`AspectRatio`).
|   - cannot include an`_`(underscore) character.
| - Enum**values** :
|   - should be UPPER_SNAKE_CASE.
|   - may not begin or end with an`_`underscore character.
|   - can contain a description for inline documentation (not returned or modified by operations); any "string" values found above an enum value are considered its description.
- are case sensitive, such that Academy and ACADEMY would be two distinct values and are not considered equal.  

    enum AspectRatio {
       ACADEMY
       WIDESCREEN
       ANAMORPHIC
       IMAX
       "No information available on aspect ratio"
       UNAVAILABLE
    }

    type Movie
      @table {
      title: String! 
      genre: String
      description: String
      originalAspectRatio: AspectRatio! @default(value: WIDESCREEN)
      otherAspectRatios: [AspectRatio!]
      tags: [String]
      rating: Float
      imageUrl: String!
      releaseYear: Int
    }

In the`Movie`type, we added an enum field`originalAspectRatio`for the aspect ratio in which the movie was filmed, and another field`otherAspectRatios`for a list of other available aspect ratios.
| **Note:** enums can be required (using the`!`token), have default values (using the`@default`directive) and be used in lists (using`[]`syntax). In general, enums can be treated similarly to most other scalar data types such as strings and integers.

#### Manage changes to enumeration fields

You can add new values to your enum, but the order of the enum list is very meaningful, so insert your new values wisely. The only fully backwards-compatible change to an enum is adding a new value to the end of the list of value. Notably, inserting a new value between previously-published enums or reordering existing values changes the relative ordering when relative operators such as "less than" are used in queries. Removing or renaming values is always a backwards-incompatible change.

You should never reorder the values in the enum value list; the ordering is important as it changes how filtering is applied.
| **Note:** Inserting, renaming, reordering and removing enum values are breaking changes, since anyone using the latest version of your database will not be able to parse or receive these updated values.

Adjustments to enum values should be done carefully so as not to break older versions of your operation or client code. When removing or renaming an enum value, be sure there are no remaining instances in your current database.

#### Using your enum fields in operations and in client code

Now that you've added an enum field to your schema, you can use this field in queries and client code.

Learn more about writing queries using enums, and about how to write client to permit adjustments to your enums starting in the[queries guide](https://firebase.google.com/docs/data-connect/queries-guide#query-enumerations).

### Other advanced concepts

To move beyond basic but useful types and relationships, refer to examples in the[reference documentation](https://firebase.google.com/docs/reference/data-connect/gql/object).

## Supported data types

Data Connectsupports the following scalar data types, with assignments to PostgreSQL types using`@col(dataType:)`.
| **Note:** If you assign a PostgreSQL serial`dataType`in your schema (for example,`myField: Int @col(dataType: "serial")`). the corresponding database column is a PostgreSQL serial (autoincrementing) type.

| **Data Connecttype** | **GraphQL built-in type or Data Connectcustom type** |                          **Default PostgreSQL type**                          |                                           **Supported PostgreSQL types** **(alias in parentheses)**                                            |
|----------------------|------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| String               | GraphQL                                              | text                                                                          | text bit(n), varbit(n) char(n), varchar(n)                                                                                                     |
| Int                  | GraphQL                                              | int                                                                           | Int2 (smallint, smallserial), int4 (integer, int, serial)                                                                                      |
| Float                | GraphQL                                              | float8                                                                        | float4 (real) float8 (double precision) [numeric](https://www.postgresql.org/docs/current/datatype-numeric.html)(decimal)                      |
| Boolean              | GraphQL                                              | boolean                                                                       | boolean                                                                                                                                        |
| UUID                 | Custom                                               | [uuid](https://www.postgresql.org/docs/current/datatype-uuid.html)            | uuid                                                                                                                                           |
| Int64                | Custom                                               | bigint                                                                        | int8 (bigint, bigserial) [numeric](https://www.postgresql.org/docs/current/datatype-numeric.html)(decimal)                                     |
| Date                 | Custom                                               | [date](https://www.postgresql.org/docs/current/datatype-datetime.html)        | date                                                                                                                                           |
| Timestamp            | Custom                                               | [timestamptz](https://www.postgresql.org/docs/current/datatype-datetime.html) | timestamptz **Note:** Local timezone information is not stored. PostgreSQL converts and stores such timestamps as UTC.                         |
| Enumeration          | Custom                                               | [enum](https://www.postgresql.org/docs/current/datatype-enum.html)            | enum                                                                                                                                           |
| Vector               | Custom                                               | [vector](https://github.com/pgvector/pgvector)                                | vector See[Perform vector similarity search with Vertex AI](https://firebase.google.com/docs/data-connect/solutions-vector-similarity-search). |

- GraphQL`List`maps to a one-dimensional array.
  - For example,`[Int]`maps to`int5[]`,`[Any]`maps to`jsonb[]`.
  - Data Connectdoes not support nested arrays.

## Equivalent SQL schema

**Note:** This schema does not represent the DDL or transformation of theData Connectschema. It's provided for illustration only.  

    -- Movies Table
    CREATE TABLE Movies (
        movie_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        release_year INT,
        genre VARCHAR(30),
        rating INT,
        description TEXT,
        tags TEXT[]
    );
    -- Movie Metadata Table
    CREATE TABLE MovieMetadata (
        movie_id UUID REFERENCES Movies(movie_id) UNIQUE,
        director VARCHAR(255) NOT NULL,
        PRIMARY KEY (movie_id)
    );
    -- Actors Table
    CREATE TABLE Actors (
        actor_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        name VARCHAR(30) NOT NULL
    );
    -- MovieActor Join Table for Many-to-Many Relationship
    CREATE TABLE MovieActor (
        movie_id UUID REFERENCES Movies(movie_id),
        actor_id UUID REFERENCES Actors(actor_id),
        role VARCHAR(50) NOT NULL, # "main" or "supporting"
        PRIMARY KEY (movie_id, actor_id),
        FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
        FOREIGN KEY (actor_id) REFERENCES Actors(actor_id)
    );
    -- Users Table
    CREATE TABLE Users (
        user_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        user_auth VARCHAR(255) NOT NULL
        username VARCHAR(30) NOT NULL
    );
    -- Reviews Table
    CREATE TABLE Reviews (
        review_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        user_id UUID REFERENCES Users(user_id),
        movie_id UUID REFERENCES Movies(movie_id),
        rating INT,
        review_text TEXT,
        review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (movie_id, user_id)
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
    );
    -- Self Join Example for Movie Sequel Relationship
    ALTER TABLE Movies
    ADD COLUMN sequel_to UUID REFERENCES Movies(movie_id);

## Next steps

| **Note:**Follow the complete series on building Data Connect connectors, which covers:
|
| - Schema development (this guide)
| - [Query development](https://firebase.google.com/docs/data-connect/queries-guide)
| - [Mutation development](https://firebase.google.com/docs/data-connect/mutations-guide)

You may be interested in:

- Generating schemas for your apps using[AI assistance tools](https://firebase.google.com/docs/data-connect/ai-assistance)
- Reviewing the[syntax reference documentation](https://firebase.google.com/docs/reference/data-connect).