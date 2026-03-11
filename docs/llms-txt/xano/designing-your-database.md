# Source: https://docs.xano.com/the-database/designing-your-database.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Design Fundamentals

<Info>
  **Quick Summary**

  Good database design starts with organizing your information into logical groups, like putting customer details in one table and order history in another. These groups are then connected through common identifiers using a table reference field - like a customer ID that links a person to all their orders - which helps maintain accuracy and avoid duplicating information.
</Info>

Think of designing a database like organizing your home. Before you buy storage containers or rearrange your furniture, you need a plan. The same goes for databases - careful planning prevents headaches later.

<Info>
  **Hint**

  Use a tool like [**Excalidraw**](https://excalidraw.com/) to help you when designing your database.
</Info>

Start by listing everything you need to store. If you're building a bookstore database, you'll need to track books, authors, customers, and sales. Just like you wouldn't store your kitchen items in your bathroom, each type of information needs its own logical home in the database.

<Frame caption="Using Excalidraw to begin the database design process.">
    <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/af96a4d4-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=3a65cf062904849285e9463c84e1fc2a" alt="" width="766" height="529" data-path="images/af96a4d4-image.jpeg" />
</Frame>

Let's draw these to look like individual items — these will represent the tables that we'll create.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3214bab6-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=89774a2dea04d70e39656093866a10ba" alt="" width="1410" height="1130" data-path="images/3214bab6-image.jpeg" /></Frame>

## Table Relationships

<Info>
  To illustrate multiple examples, we've added a **Publishers** table to our
  visualization.
</Info>

Consider how these pieces connect. A book has one or more authors, and an author can write multiple books. A customer can buy many books, and a book can be bought by many customers. These relationships are crucial - they're like the hallways connecting rooms in your house, allowing you to move naturally between related information.

**One-to-One**

* Each thing on one side matches exactly one thing on the other side. Like a person and their social security number: one person has one number, and each number belongs to one person

**One-to-Many**

* One thing on one side can connect to multiple things on the other side, but those multiple things each only connect back to one thing. Like a mother and her children: one mother can have many children, but each child has only one mother

**Many-to-Many**

* Things on both sides can connect to multiple things on the other side. Like students and classes: one student takes many classes, and each class has many students

For our book store example, let's visualize the relationships between our tables.

<Frame>
  <iframe width="1000" height="500" src="https://demo.arcade.software/eYYLSo6Vi1ZVYOkLk5i8?embed" title="https://demo.arcade.software/eYYLSo6Vi1ZVYOkLk5i8?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

## Database Fields

**Think about the essential characteristics that describe each thing**. Just like how a person's profile might include their name, birthday, and contact info, each table should contain the core pieces of information that defines that thing. When referring to all of the fields in a database table as a whole, we'll call this **schema**.

Let's use our bookstore example:

* For Books: You'll want the ISBN (like a book's fingerprint), title, publication date, current price, and maybe format (hardcover/paperback). You don't need to store the author's name here - that's what the connection to the Authors table is for.
* For Authors: You'll store their name, perhaps birth date, nationality, and a brief biography. You don't need to store a list of their books - the relationship between tables handles that.
* For Customers: You'll want their name, contact information, shipping addresses, and maybe their preferences or a membership status. You don't need to store their purchase history here - that's tracked through the Sales table.

**"Does this information describe the core thing I'm tracking, or is it really about something else?"** If you find yourself wanting to store a list of things (like "all books by this author" or "all orders from this customer"), that's usually a sign you need a relationship between tables rather than storing that data directly.

**Consider whether the information might change over time**. For example, book prices change frequently, so you might want both a "currentPrice" in the Books table and a "salePrice" in the Sales Items table. This lets you track both what a book costs now and what customers actually paid for it in the past.

\*\*Watch out for duplicate information. \*\*If you're storing an author's contact details, store them once and reference them when needed, rather than copying them into every book record. This is like having one toolbox in your garage instead of keeping duplicate tools in every room. In Xano, this is accomplished with [table reference fields](/the-database/database-basics/field-types#table-reference).

**How many fields is 'too many'?** This is not a black-and-white question to answer. Some tables can have a significant number of fields, but the dataset is small — this is usually okay. If you expect this table to grow in size over time, it's always better to split data types into separate tables — for example, if users have companies attached, you should probably store those companies in a separate table and use [relationships](/the-database/designing-your-database#table-relationships).

## Planning for the Future

**Think about what information you'll need to find quickly.** Just as you might keep frequently used items in easily accessible drawers, consider what data you'll search for most often. This helps you decide how to organize and index your information.

**Think about how information might expand in the future.** Initially, you might only need basic book formats (hardcover and paperback). But what happens when you want to add audiobooks? You'll need new fields like runtime, narrator, and audio format. Instead of hard-coding format types, you could create a separate formats table, and use a table reference in your books table that lets you add new types without changing your core structure.

Suppose you create a database table for storing book formats directly within the books table:

**Books Table**

| BookID | Title | Author | Hardcover | Paperback | Audiobook |
| ------ | ----- | ------ | --------- | --------- | --------- |
|        |       |        |           |           |           |

This design is inflexible because each time you introduce a new format, you must alter the table structure. Instead, use a separate formats table and establish a relationship with the books table.

**Books Table**

| BookID | Title | Author |
| ------ | ----- | ------ |
|        |       |        |

**Formats Table**

| FormatID | FormatType |
| -------- | ---------- |
|          |            |

**BookFormats Table**

| BookID | FormatID |
| ------ | -------- |
|        |          |

This flexible table design allows you to add new formats easily without changing the core structure.

**Finally, remember that simple is usually better.** Like a well-organized home where everything has its place, a good database design should feel natural and intuitive. If you find yourself creating complicated structures to store simple information, step back and reconsider your approach.

Remember: **A well-designed database makes everything else easier.**


Built with [Mintlify](https://mintlify.com).