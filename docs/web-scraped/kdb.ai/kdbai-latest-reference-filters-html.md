# Source: https://code.kx.com/kdbai/latest/reference/filters.html

Title: About filters in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/reference/filters.html

Markdown Content:
_This page provides a detailed introduction to filters in KDB.AI, explaining their purpose, key concepts, and role in shaping and refining vector search behavior._

If you're already familiar with this topic, you can skip ahead to the [How-to guide](https://code.kx.com/kdbai/latest/use/filter.html).

In KDB.AI and vector databases in general, filters serve as specific parameters that refine the search process during a query or any type of search. They make targeted searches more efficient by eliminating vectors that don't match the provided criteria.

Example
Take, for instance, the act of searching for documents within a vector database with the intention of retrieving only those associated with a particular department.

*   By setting a filter such as `department == 'engineering'`, you effectively remove any documents not tagged with the `engineering` keyword. 
*   In a similar way, you can use date-based filters to either include recent documents or to discard those that are dated.

As a result, the implementation of filters is crucial for search results that are precise and highly relevant, particularly when sifting through extensive datasets.

To better understand how filters work in KDB.AI, let's go through the following key terms:

*   [Pre/post filtering](https://code.kx.com/kdbai/latest/reference/filters.html#prepost-filtering)
*   [Query language](https://code.kx.com/kdbai/latest/reference/filters.html#query-language): [operator](https://code.kx.com/kdbai/latest/reference/filters.html#filter-operators), [operand](https://code.kx.com/kdbai/latest/reference/filters.html#filter-operands), [parameter precedence](https://code.kx.com/kdbai/latest/reference/filters.html#parameter-precedence)
*   [Fuzzy filters](https://code.kx.com/kdbai/latest/reference/filters.html#fuzzy-filters)

Pre/post filtering
------------------

Pre-filtering and post-filtering are two techniques used in vector databases such as KDB.AI to manage and refine search results:

*   **Pre-filtering** screens potential matches before the main vector search. This preliminary filter reduces the search scope by eliminating results that don’t qualify from the start, enhancing both the speed and precision of the vector search. For example, in a database of images, you might pre-filter images based on simple features like color histograms or shapes before performing a detailed vector search. 
*   **Post-filtering** takes place after the main vector search by performing further filtering to refine the outcomes. Use this method when you want to apply complex filters that cannot be easily integrated into the initial search phase.

In conclusion, pre-filtering lightens the computational burden by weeding out non-essential data at the outset of the search and post-filtering provides a more detailed fine-tuning of the search outcomes after you had already performed the first query.

Real-world filtering scenario
In a financial vector database, applying pre-filtering and post-filtering can be crucial for managing and extracting meaningful insights from large datasets. Here’s a real-world scenario illustrating how you can use both:

**Scenario: Investment Opportunity Analysis**

Imagine you’re a financial institution that wants to identify potential investment opportunities in the technology sector. You have a vast vector database containing financial reports, news articles, and market data.

**Pre-Filtering**: Before conducting a vector search, you apply pre-filters to narrow down the dataset. This helps filter out documents based on:

*   Date range (for example, documents from the last quarter) 
*   Document type (for example, financial reports)
*   Specific financial metrics (for example, companies with revenue growth > 10%) 

This pre-filtering step ensures that you perform the subsequent vector search on a more relevant and manageable subset of data, improving efficiency and reducing computational load.

**Vector Search**: Conduct a vector search on the pre-filtered dataset to find documents that semantically match your criteria for investment opportunities, such as innovative projects, market expansion, or strong leadership teams.

**Post-Filtering**: After the vector search, apply post-filters to further refine the results. This might include filtering based on:

*   Company size (for example, market capitalization) 
*   Geographic location (for example, companies based in Silicon Valley) 
*   Industry-specific keywords (for example, “artificial intelligence”, “cloud computing”) 

The post-filtering step ensures that the final results are highly relevant to your investment strategy and goals.

By combining pre-filtering and post-filtering with vector search, financial institutions can efficiently sift through vast amounts of data to find the most promising investment opportunities that align with their criteria. This method improves accuracy, saves time, and supports more informed decision-making within the dynamic financial environment.

Query language
--------------

In vector databases, the terms filter operator, operand, and parameter precedence are essential components of a query language that help refine search results.

### Filter operators

Vector databases use filter operators to refine search results by including or excluding objects based on certain conditions. These symbols or keywords perform operations on one or more operands. Common filter operators include:

*   `Equal`: Matches objects where the specified field is equal to the provided value. 
*   `GreaterThan/LessThan`: Matches objects where the specified field is greater than or less than the provided value, respectively. 
*   `And/Or`: Logical operators used to combine multiple conditions. 
*   `Like`: Matches objects based on pattern matching, often used with wildcards. 

### Filter operands

An operand is the data or value that is being manipulated or compared by an operator. In the context of vector databases, operands are typically the values or properties of objects in the database that you want to filter by.

### Parameter precedence

In KDB.AI, parameter precedence refers to the order in which multiple filter conditions are applied to a dataset. When you specify multiple filters, they are applied sequentially in the order they are listed.

This means that the first filter in the list is applied to the dataset first, followed by the second filter, and so on. The sequence in which you apply filters is crucial, as the output from an initial filter can influence the data subset that later filters work on. If you change the order of the filters, you might get a different result.

To ensure that you get the right outcome, you should carefully plan the sequence of your filters based on the logic you want to apply to your data. Remember, in KDB.AI, there is no implicit precedence like in arithmetic operations; the filters are applied strictly in the order they are given. If you need to enforce a specific precedence, you should structure your filter list accordingly.

Example
For example, let’s consider the following filter:

```
filter=[("within", "price", [50, 100]), 
        ("<", "volume", 500)]
```

 The filter operators are the string values `within` and `<`. These operators define the type of filtering to apply. 
The filter operands are the column names and the values associated with them. For `within`, the operands are the column name `price` and the range `[50, 100]`. For `<`, the operands are the column name `volume` and the value `500`.

So, in this case:

*   `within` is the operator that checks if the price is within the specified range of 50 to 100. 
*   `<` is the operator that checks if the volume is less than 500.

The filter conditions are applied in the order they appear in the list, affecting the dataset sequentially:

1.   The `within` filter is applied first to select all records where the price is between `50` and ``#!python 100`. 
2.   Then, the `<` filter is applied to the result of the first filter to select records where the volume is less than `500`. 

Fuzzy filters
-------------

Fuzzy filters improve vector search efficiency and recall by narrowing down candidates based on specific criteria. Using fuzzy filters leads to more accurate results, even when dealing with imprecise or “fuzzy” queries.

### Benefits of fuzzy filters

Fuzzy filters are particularly useful when using data that may contain errors, typos, or variations. For example, if you apply fuzzy filters to searches, you can find documents that contain similar terms to a specified query, even if they're not exactly the same.

The addition of fuzzy filters provides the following benefits:

*   **Handling Typos:** fuzzy filters are essential for handling approximate or imprecise search terms. Users often make typos or minor spelling errors, and fuzzy search helps retrieve relevant results despite these variations.
*   **User-Friendly Experience:** by accommodating slight variations in search terms, fuzzy filters ensure a better user experience. Users don’t need to input the exact term to get meaningful results.
*   **Robustness:** fuzzy filters make your search system more robust by accounting for real-world data imperfections.
*   **Increased Recall:** fuzzy filters increase recall by capturing relevant documents that might have been missed due to minor differences in spelling or input errors.

### How do fuzzy filters work?

Fuzzy filter algorithms often rely on the concept of **distance**, which measures the minimum number of operations (insertions, deletions, substitutions) required to transform one string into another.

Common algorithms include Levenshtein distance and Damerau-Levenshtein distance. For example, the Levenshtein distance between “cat” and “cot” is 1 (substitute ‘a’ with ‘o’). Fuzzy queries expand the search to include terms within a specified distance.

The key concepts to understand fuzzy filters are:

*   [Distance](https://code.kx.com/kdbai/latest/reference/filters.html#distance)
*   [Levenshtein distance](https://code.kx.com/kdbai/latest/reference/filters.html#the-levenshtein-distance)

### Distance

In the context of fuzzy filters, distance is the number of one-character changes needed to transform one term into another. These changes can include:

*   Replacing a character: For example, turn “box” into “fox.”
*   Deleting a character: For instance, change “black” to “lack.”
*   Inserting a character: For example, turn “all” to “ball.”
*   Swapping two adjacent characters: For instance, change “act” to “cat.”

Fuzzy queries use distance (most commonly measured by the Levenshtein distance) to find terms similar to a search term. The query creates a set of all possible variations within a specified distance and returns exact matches for each expansion.

### The Levenshtein distance

The Levenshtein distance is a number that measures how different two strings are. The higher the Levenshtein distance, the more different the strings are.

For example, the Levenshtein distance between “bitten” and “fitting” is 3 because it takes 3 text edits to change one into the other:

1.   bitten → fitten (replace "b" with "f")
2.   fitten → fittin (replace "e" with "i")
3.   fittin → fitting (insert "g" at the end).

Check out the full [list of distance metrics](https://code.kx.com/kdbai/latest/use/filter.html#supported-distance-metrics) you can choose from.

### Use cases

Fuzzy filters are a powerful tool with various use cases across different domains. Here are some key applications of fuzzy filters:

*   **Spell Checking:** fuzzy filters are commonly used in algorithms to suggest corrections for misspelled words. They help users find the correct term even if there are minor typos or spelling mistakes.
*   **Data Cleaning:** in data deduplication processes, fuzzy filters identify and merge records that are likely duplicates but may have slight variations in names, addresses, or other fields.
*   **Autocomplete and Suggestions:** search engines, websites, or applications rely on fuzzy filters to predict and suggest relevant search terms, even if the user input contains errors or incomplete information.
*   **Information Retrieval:** fuzzy filters allow users to find documents, articles, or records that closely match their queries, even when the exact terms are not used.
*   **Product Matching in e-Commerce:** e-commerce platforms use fuzzy filters to improve product matching. Customers searching for a product may receive relevant results, even if they use synonyms or alternative terms.
*   **Name Matching in Databases:** fuzzy filters can identify and link records with similar names but slight variations, reducing the chance of missing relevant information.
*   **Geographic Search:** when searching for locations or addresses, fuzzy filters can accommodate variations in spelling or abbreviations, ensuring accurate results in geographic searches.
*   **Code Search:** in software development, fuzzy filters assist programmers in quickly locating code snippets, functions, or methods, especially when they only remember parts of the code.

Next steps
----------

Now that you're familiar with filters, try the following:

*   Visit our [Customize filters](https://code.kx.com/kdbai/latest/use/filter.html#customize-filters) page and follow the steps.
*   Learn [How to use fuzzy filters](https://code.kx.com/kdbai/latest/use/filter.html#how-to-use-fuzzy-filters).
*   Go to our [Learning hub](https://kdb.ai/learning-hub/) to read about [Optimizing vector search with metadata filtering](https://kdb.ai/learning-hub/articles/optimizing-vector-search-with-metadata-filtering/).
