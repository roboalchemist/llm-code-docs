# Source: https://docs.xano.com/building-backend-features/fuzzy-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fuzzy Search

Xano offers robust search capabilities, commonly referred to as *fuzzy search*, that you can utilize while querying records in a function stack. This includes normalization of words (ie. party vs parties), case-insensitive support, flexible expressions (words, phrases, and negations), and weighted priorities (ie. title vs description) for relevance.

The following demonstrates how to set up search in your database, the logic behind the search functionality, and best practices for utilizing search queries.

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/5_XkvyAX2C0" title="Fuzzy Search in Xano - NEW expanded search functionality!" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

[**Watch more videos on Fuzzy Search**](https://www.youtube.com/results?search_query=xano+fuzzy+search+)

### **Creating a Search Index**

First, create an [index](/the-database/database-performance-and-maintenance/indexing). Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. An index is used to define which fields of the database table you want to search. You can even build multiple search indexes on the same table to build different search criteria. For example, if you have both public and private data in the same table, you can build a "normal user" and an "administrator" search.

To create an index, click **Indexes** at the top of the table you would like to build search for, and then click **Create Index.**

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c9ade83d-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=351169cb441e869205c4b729802ade64" width="2304" height="1195" data-path="images/c9ade83d-image.jpeg" />
</Frame>

Choose **search** as the index type, and give the index a name. Next, specify the language for the data you are searching, the fields you are searching, and the ranking order of the fields being searched.

<Frame caption="An example of creating a search index.">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/31e43c6a-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=2040944200cfcdcf795a298d3dde19fb" width="890" height="617" data-path="images/31e43c6a-image.jpeg" />
</Frame>

In this example, we created a new search index on a database of movies called **search\_movies**, in English, and are searching two fields in that database: title and overview. The title field will rank higher than data in the overview field in the qualified search results.

Once ready, click **Save** and Xano will build your index. This can take a few minutes depending on the volume of data of the table.

### Building a Search API

After generating the index, it can be implemented it into a query in the function stack. Use the **Custom Query** feature in the **Filter** tab of the [**Query All Records**](/the-function-stack/functions/database-requests/query-all-records) function.

When adding a custom query, the newly created index is available in the expression builder, noted by the **\$** symbol. It is also labeled as *search* underneath the name.

<Frame caption="Look for the $ symbol as well as the word search to easily find your search index when configuring your query.">
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0132ae28-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=7b559ab8f99ba31a16140e605e0f7ab3" width="903" height="758" data-path="images/0132ae28-image.jpeg" />
</Frame>

Next, set the operator to **search** and specify the search query. In this example, we are using an input called **search\_query.**

<Frame caption="Setting the operator to Search and specifying our search query.">
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cc78a04c-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=ff92c2279a64b870c466c5cdd2ba0278" width="1743" height="365" data-path="images/cc78a04c-image.jpeg" />
</Frame>

Congratulations! 🥳 You've just implemented super-fast search inside your function stack.

### Ranking

You can implement a ranking system and sort the search results by this rank for more precise search results. To do this, go to the **Output** tab of the **Query All Records** function, add an **eval** on the search index, and apply the **search\_query** filter. This tells Xano to "use my search index to generate a ranking score of my results based on my search query".

<Frame caption="Create and Eval on the search index by applying the search_rank filter so we can sort by ranking.">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/ab880cb8-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=fd15d369046bc148216305de7f78f674" width="1194" height="1456" data-path="images/ab880cb8-image.jpeg" />
</Frame>

After, add a sort to the query using the newly created eval (in this example, called "rank"). You may also consider to enable paging especially on larger queries.

<Info>
  Add a Sort to the Query by clicking on the Return portion of the Output tab.
</Info>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/40bd3aeb-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5e9499907cb583a8dc1c2961328e8c86" width="662" height="539" data-path="images/40bd3aeb-image.jpeg" />
</Frame>

<Info>
  Order by in descending order will provide the most relevant search results first.
</Info>

### Different Search Methods

Search queries can be written in different ways to fulfill specific search requirements.

1. Words separated by a space imply an AND.<br />**Example:** A query of *"toy story"* means *search for toy AND story*

2. Exact phrase searches are possible using double quotes.<br />**Example:** If you wanted to search for *"Toy Story"* as an exact match, your query would be *"Toy Story" with the quotation marks*. **Note:** if you are entering this search expression directly into a JSON payload, then you may need to escape the quotes with a backslash. example: `{"search": "\"Toy Story\""}`

3. Partial phrase matching<br />**Example:** `"Toy * Story"` would return any results that contain Toy Story with one word in between. `"Toy *** Story"` would return any results that contain Toy Story with three words in between.

4. Wildcard matching<br />**Example:** `Sto:*` would return any results that contain words that start with sto.

5. Expression groups<br />**Example:** `(Woody or Buzz) Toy` would return multiple matches for the word Toy that also include either Woody or Buzz.

6. Negation of specific words is possible by using a - character.<br />**Example:** If you wanted to search for movies that have *Toy* in the title, but not *Toy Story*, your query would be `"toy -story"`.

7. You can also use a combination of these to get even more specific.<br />**Example:** Searching for `"toy story" day -night` would mean *search for the phrase Toy Story and the word day, without the word night.*

8. Priority targets allow you to specify which priority defined in your search index to use for the specific expression. This can be combined with wildcard matching as well.<br />**Example:** `Toy Story:2` would search for all records containing the word Toy, as well as the word Story in any fields representing priority 2 in your search index.<br />**Example:** `Toy Sto:*2` would search for all records containing the word Toy, as well as words starting with Sto in any fields representing priority 2 in your search index.

9. Single vs Plural is supported.<br />For example, *"toy"* will also return results that contain *"toys"*.

**Stop Words** -- are commonly used words such as articles, pronouns and prepositions.<br />For example: *is, and, an, or, the.* Stop words are not included in your search query.

### Search Results

Search results are returned just like any other API response and the data works just like any other variable inside Xano.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/341f9d58-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=d72290693b35d264f906c173c1d986c5" width="1219" height="1297" data-path="images/341f9d58-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).