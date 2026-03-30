# Source: https://docs.xano.com/the-database/database-performance-and-maintenance/indexing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Indexing

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/hpb5PuFdki4" title="Database Indexing | Speed up your queries!" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

## **What is an Index?**

An index is a database feature that helps improve the speed and efficiency of queries made against a database table. They help when searching through large, unordered data sets and give the database search engine a quick way to sort and find specific data. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access to ordered records.

## **How do they work?**

A table index is very similar in practice to the index of a textbook. When there is a specific piece of information that you want to find, reading every page of that book to find what you are looking for can be very slow and inefficient. So, you would use the index at the back of the book to find exactly which page contains the information you need.

This is the same concept for a database table index. They create a special type of lookup table in the background that the database engine can use to retrieve the data faster than looking through each individual row for every search.

## **When to use an Index?**

Indexes are the most beneficial in the following scenario(s):

* You have a specific query that you want to ensure is as performant as possible

* The query uses simple operators in one or more conditions
  * **Yes**: Where user region = Canada
  * **No**: Where user ID is even, or user region is empty

* The table has 10,000 records or more

* The table is not frequently written to or updated
  * This is because when a table is indexed and frequently written to, the performance of inserting new data can suffer because the index has to be updated at the same time. You can index a table that has frequent writes, but use caution.

## How do I apply an index properly?

It’s important to construct your index based on the query being performed that you are trying to address. We will use the an example scenario to explain an approach to indexing. All scenarios were built and performed on a Launch plan instance with no additional load or processing. Your results may vary based on other factors related to your specific instance or the plan you are on.

#### Example Table: 515,195 records, with the following schema

| id | name | region | country | profession | firstname | lastname | email | birthday |
| -- | ---- | ------ | ------- | ---------- | --------- | -------- | ----- | -------- |
|    |      |        |         |            |           |          |       |          |

#### Example Query: Find all users in a specific country, with a specific profession

<Frame caption="Example query with no indexing">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4859a3cf-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=39d03ab8a576c22d63f932550fda7ae8" width="1600" height="842" data-path="images/4859a3cf-image.jpeg" />
</Frame>

With no indexing applied, this query takes **0.62** seconds to complete.

Because these two pieces of data can exist independently of each other -- meaning we don't need to know a country to determine a profession, and vice versa, we will apply two separate indexes to our table, one for each field.

<Frame caption="Indexes applied based on the sample query">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a64bde39-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=9f343e6589bd1b9e6374df7a64794b5c" width="654" height="509" data-path="images/a64bde39-image.jpeg" />
</Frame>

With these indexes applied, the example query now executes in **0.05** seconds, a **95% increase in query speed.**

<Frame caption="Example query with indexing applied">
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1a3d4577-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=7a47f4d1d13a2abc296016d85b603a29" width="1600" height="811" data-path="images/1a3d4577-image.jpeg" />
</Frame>

### When should I index a single field by itself vs multiple fields in the same index?

This is based on the hierarchy of the query being performed, and what makes the most sense in terms of your data set. It is also important to understand how multi-field indexes are executed.

**The order of fields in your index matters.** When building a multi-field index, you want to start with the field that contains the \*\*least \*\*amount of unique values, moving forward to finishing with the field that has the **most** unique values.

With a multi-field index, each 'step' (field) is essentially placed into a new bucket that the database knows it can use to potentially find matching data. Using an example of location data where we have a `city`, `state`, and `country` field, we know that country has the least unique values. This means that when we're building our index, we'd add the country field first. Moving on from there, we would add our states, and then finally the cities, so when the database builds the index, it builds the most efficient bucketing possible.

In an adverse example, consider an index on a timestamp field. Timestamps in Xano use milliseconds, which obviously means that these values will almost be unique for every single record. If we built a multi-field index that started with this timestamp field, we are creating that many buckets right away before trying to look for less specific data, which means that the query becomes extremely inefficient.

It is also important to note that if you have multiple fields defined in a single index, but are not using both of those fields in your query, the index will not provide any benefit to the performance of that query. Indexes are only useful if you are indexing based on the queries you are making, and the hierarchy of your query makes sense.

You can use a field in a double-field index as well as a single-field index, but it is important to consider the storage requirement for each index you create. In addition, it is possible to ‘trap’ yourself into a situation where you have too many indexes, and it becomes more difficult to determine what is helping and what is not.

**Example Query: Find all users who are part of a specific subset of artists**

<Frame caption="Example query with no indexing">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/791ff17f-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=ee39f752d4c49e8eb3a34b5f6e0c2421" width="1600" height="810" data-path="images/791ff17f-image.jpeg" />
</Frame>

Executing the example query, with no indexing applied, takes **1.44s**.

Because we know that the artist\_service field requires the profession field to make sense in the context of our query, we will place both of those fields, in order, in the same index.

<Frame caption="Applying the index for the example query">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e18878e2-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=5c3bab74ec478c171bddb32155b9084c" width="638" height="544" data-path="images/e18878e2-image.jpeg" />
</Frame>

<Frame caption="Example query results with indexing applied">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/5183d627-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=94aa2db8221036062531895e7862fad0" width="1600" height="808" data-path="images/5183d627-image.jpeg" />
</Frame>

After applying the index shown, this query completes in **0.02 seconds, 98% faster.**

In this same scenario, if there was a world where we would potentially query **artist\_service** by itself, and it did not also need a **profession** to make sense based on the context of our query, we would want to create single-field indexes for these fields.

**Example 2: When to use Single-Field vs. Multi-Field Indexes**

We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named "Jack" in a specific region. We will not be building any other queries to search our table of people.

**In this example, we would build one index with both fields**. This is because we are not utilizing these fields in any other queries, and they are both required in the context of the query we are building.

**Example 3:** **When to use Single-Field vs Multi-Field Indexes**

We have a table of people, and each person lives in a specific region. We want to build a query where we find all people named "Jack" in a specific region. We also want to build a second query that just finds us all people named "Jack", and a third query that finds all people in a certain region without specifying a name.

**In this example, we would build two single-field indexes, one for each field.** This is because we are utilizing the fields in multiple different queries.

### Using the GIN Index to search complex data types

The GIN index is used specifically when searching through more complex data types, such as objects and arrays, as these fields can not be indexed using the methods described previously.

This index is automatically applied to all of your database tables; you do not need to add or maintain this.

Let's say, as an example, we have a list field called **my\_list**, and we want to find all records that contain a value of **special** inside of **my\_list.**

To use the GIN index in this query, we first need to create a variable with the following structure:

```json  theme={null}
{"my_list":[
    "special"
    ]
}
```

The structure starts with an object containing the name of the field, with the value being an empty array. We then use the **push** filter to add the value we are searching for inside of that list. You can use multiple push filters to search for multiple values.

<Frame caption="Constructing the variable to be used in our query">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/58efb566-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=308a9d1d94edee285ed1fb664c3f5487" width="602" height="442" data-path="images/58efb566-image.jpeg" />
</Frame>

Once we have our object constructed, we will set up our custom query by selecting the table on the left side, which leaves us with the 'contains' operator, and our constructed object on the right.

<Frame caption="An example of a GIN index query">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7a811b0c-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=b0a90ef220f7e6779905d581121323ed" width="1636" height="376" data-path="images/7a811b0c-image.jpeg" />
</Frame>

In this example, a query without indexing takes **0.23** seconds.

In this example, utilizing the GIN index, the query takes **0.02** seconds.

## How to Apply an Index in the Database View

In the database view, click on the table that you want to index. Choose "Indexes" from the top bar.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b36cabaa-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=0281b05f576d0d099cf74609c6b924b2" width="2304" height="283" data-path="images/b36cabaa-image.jpeg" />
</Frame>

Click "Create Index" to add a new index, or click on an existing index to manage it.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9d5821f5-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=9b52371b6241bd80137e38997d4adf9b" width="839" height="559" data-path="images/9d5821f5-image.jpeg" />
</Frame>

Choose the fields, sort, and index type. When done, click 'Save'.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8ec476d4-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=07cd338878feff6504a41c0b8f065db9" width="742" height="1322" data-path="images/8ec476d4-image.jpeg" />
</Frame>

<Warning>
  **Note**: Creating or updating an index can take several minutes depending on the complexity and the size of the database table.
</Warning>

<Warning>
  **Note**: Indexes will significantly increase the storage your database table requires. Please ensure you have enough free space (we recommend trying to stay around \~50% free space) before indexing your tables.
</Warning>

### Types of Indexes

* **Primary**
  * Automatically applied and maintained
  * Indexes the primary key (ID) of each record and enforces uniqueness
* **GIN**
  * Automatically applied and maintained
  * Most suitable for complex data types (JSON, lists, objects) and full-text search
* **Index**
  * The most common index type
  * Used when indexing for standard queries
* **Unique**
  * A special type of index to enforce unique values in a column’
* **Spatial**
  * A special type of index designed to optimize queries involving spatial data, such as geography fields.
* **Search**
  * A special type of index to be used in conjunction with Xano fuzzy search
* **Vector**
  * A unique indexing type used for working with the [Vector field type](/the-database/database-basics/field-types#vector).
  * Indexing should **always** be used on vector columns, regardless of the amount of records.
    * **L2 Distance** - Measures the Euclidean distance between vectors
    * **L1 Distance** - Measures the taxicab distance between vectors.
    * **Inner product** - Measures dissimilarity based solely on amplitude (recommended for OpenAI and other normalized vectors)
    * **Cosine Distance** - Measures dissimilarity between vectors, considering their length and amplitude

## When should you *not* use an index?

* Do not use an index on a table containing only a few records. They are most valuable when your record count approaches >5,000 records.

* Indexes should not be used on fields that have or will have a high number of **null** values, because that essentially means there is nothing to index on.

* You can not apply a normal index to an array or object field, so keep that in mind when designing your database structure. You can use the automatically maintained GIN index, detailed later on this page.

* If your field / column names are frequently changing, you should not index that field.

* If a table is frequently used to add / edit data, it may be best practice to not index this table. While your query speeds can still benefit, they can also slow the performance of adding to or editing data on this table given the nature of creating an index behind the scenes.


Built with [Mintlify](https://mintlify.com).