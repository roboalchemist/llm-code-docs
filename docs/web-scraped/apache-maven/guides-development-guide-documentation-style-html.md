# Source: https://maven.apache.org/guides/development/guide-documentation-style.html

Title: Guide To Maven Documentation Style – Maven

URL Source: https://maven.apache.org/guides/development/guide-documentation-style.html

Markdown Content:
[](https://maven.apache.org/guides/development/guide-documentation-style.html)[](https://maven.apache.org/guides/development/guide-documentation-style.html)
Where did the style came from?[](https://maven.apache.org/guides/development/guide-documentation-style.html#where-did-the-style-came-from)
------------------------------------------------------------------------------------------------------------------------------------------

The documentation style guide was created to make our documentation more consistent and also to apply best practices to the documentation as well. The standard has just been started and will expand over time based on the suggestions made on the Maven dev mailing list. It is a community consensus of how we should write our documentation.

Each rule in this guide should come with a motivation as to why it exists. References to external sources are encouraged.

The styleguide might evolve over time.

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
Date format[](https://maven.apache.org/guides/development/guide-documentation-style.html#date-format)
-----------------------------------------------------------------------------------------------------

How people format a date varies around the world, sometimes making it hard for people to understand each other. The solution to this problem comes in the form of the ISO-8601 standard.

A date in our documentation must follow this standard:

**YYYY-MM-DD**

where **YYYY** is the year in the Gregorian calendar, **MM** is the month of the year between 01 (January) and 12 (December), and **DD** is the day of the month between 01 and 31.

**Note**: All documentation meta-data should respect this convention, for instance for this given APT document:

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
### References[](https://maven.apache.org/guides/development/guide-documentation-style.html#references)

*   [W3C Quality Web Tips](http://www.w3.org/QA/Tips/iso-date)
*   [ISO-8601](https://www.iso.org/standard/70908.html)
*   [Wikipedia](http://en.wikipedia.org/wiki/ISO_8601)

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
POM Snippet[](https://maven.apache.org/guides/development/guide-documentation-style.html#pom-snippet)
-----------------------------------------------------------------------------------------------------

A POM file must use 2 spaces for each indentation. Because POM snippets are often used in documentation to show the user how to configure something, it is important that these snippets aren't too wide. If they are too wide, the page is difficult to read on a smaller screen.

When you use a snippet of XML from the POM as an example in documentation, make sure that the example is properly indented. A user should be able to copy and paste the example into their own POM without changing the indentation.

Also, you should declare all parent POM elements to improve the comprehension. You could use ellipsis (i.e. `...`) if you don't want to specify elements.

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
### Example[](https://maven.apache.org/guides/development/guide-documentation-style.html#example)

The following is an example of how the distribution management of the Maven site is configured.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<distributionManagement>`
4.   `<site>`
5.   `<id>apache.website</id>`
6.   `<url>scp://people.apache.org/www/maven.apache.org/</url>`
7.   `</site>`
8.   `</distributionManagement>`
9.   `...`
10.   `</project>`

As you can see above the `<distributionManagement>` element is indented once (=2 spaces), the `<site>` element is indented twice (=4 spaces), and the `<id>` is indented three times (=6 spaces).

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
Naming Documentation Files[](https://maven.apache.org/guides/development/guide-documentation-style.html#naming-documentation-files)
-----------------------------------------------------------------------------------------------------------------------------------

All file names should replace space by a hyphen (`-`), for instance for this given APT document:

```
guide-documentation-style.md
```
[](https://maven.apache.org/guides/development/guide-documentation-style.html)
Updating Documentation Files[](https://maven.apache.org/guides/development/guide-documentation-style.html#updating-documentation-files)
---------------------------------------------------------------------------------------------------------------------------------------

A good practice is to update the date (with the correct date format) when you are updating documentation files.

[](https://maven.apache.org/guides/development/guide-documentation-style.html)
Write Thinking[](https://maven.apache.org/guides/development/guide-documentation-style.html#write-thinking)
-----------------------------------------------------------------------------------------------------------

Here are some pointers about English rules when typing material:

*   [Wikipedia:Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style), specifically [Punctuation Part](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Punctuation)
