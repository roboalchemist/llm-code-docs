# Source: https://maven.apache.org/guides/mini/guide-snippet-macro.html

Title: Guide to the Snippet Macro – Maven

URL Source: https://maven.apache.org/guides/mini/guide-snippet-macro.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
When generating your project website with Maven, you have the option of dynamically including _snippet_s of source code in your pages.

A _snippet_ is a section of a source code file that is surrounded by specially formatted comments.

This functionality is inspired by the [Confluence](http://www.atlassian.com/software/confluence/) snippet macro, and is provided by the Maven Doxia project by way of the Maven Site Plugin.

To include snippets of source code in your documentation, first add comments in the source document surrounding the lines you want to include, and then refer to the snippet by its id in the documentation file. Each snippet must be assigned an id, and the id must be unique within the source document. The id parameter is not required if you want to include the entire file.

Following are examples of snippets in various source documents, as well as the corresponding macros in the APT documentation format.

See the Doxia [Macros Guide](https://maven.apache.org/doxia/macros/index.html#Snippet_Macro) for more information and examples.

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
Snippets in Sources[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#snippets-in-sources)
--------------------------------------------------------------------------------------------------------

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
### Java[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#java)

1.   `// START SNIPPET: snip-id`
2.   `public static void main( String[] args )`
3.   `{`
4.   `System.out.println( "Hello World!" );`
5.   `}`
6.   `// END SNIPPET: snip-id`

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
### XML[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#xml)

1.   `<!-- START SNIPPET: snip-id -->`
2.   `<navigation-rule>`
3.   `<from-view-id>/logon.jsp</from-view-id>`
4.   `<navigation-case>`
5.   `<from-outcome>success</from-outcome>`
6.   `<to-view-id>/mainMenu.jsp</to-view-id>`
7.   `</navigation-case>`
8.   `</navigation-rule>`
9.   `<!-- END SNIPPET: snip-id -->`

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
### JSP[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#jsp)

1.   `<%-- START SNIPPET: snip-id --%>`
2.   `<ul>`
3.   `<li><a href="newPerson!input.action">Create</a> a new person</li>`
4.   `<li><a href="listPeople.action">List</a> all people</li>`
5.   `</ul>`
6.   `<%-- END SNIPPET: snip-id --%>`

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
Snippets in Documentation[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#snippets-in-documentation)
--------------------------------------------------------------------------------------------------------------------

[](https://maven.apache.org/guides/mini/guide-snippet-macro.html)
### APT[](https://maven.apache.org/guides/mini/guide-snippet-macro.html#apt)

1.   `%{snippet|id=snip-id|url=http://svn.example.com/path/to/Sample.java}`

3.   `%{snippet|id=snip-id|url=file:///path/to/Sample.java}`

As of doxia-core version 1.0-alpha-9, a ‘file’ parameter is also available. If a full path is not specified, the location is assumed to be relative to ${project.basedir}.

1.   `~~ Since doxia-core 1.0-alpha-9`
2.   `%{snippet|id=abc|file=src/main/webapp/index.jsp}`

*   Macros in apt **must not** be indented.
*   Exactly one of `url` or `file`**must** be specified.
