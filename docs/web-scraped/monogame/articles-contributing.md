# Source: https://docs.monogame.net/articles/contributing

Title: Contributing to MonoGame Documentation | MonoGame

URL Source: https://docs.monogame.net/articles/contributing

Markdown Content:
Instructions on how to contribute to the documentation of the MonoGame Framework

Thank you for choosing to contribute to the MonoGame project! This page provides guidance on how you can help to improve the documentation for MonoGame.

Getting Started[](https://docs.monogame.net/articles/contributing#getting-started)
----------------------------------------------------------------------------------

### Articles and API References[](https://docs.monogame.net/articles/contributing#articles-and-api-references)

The MonoGame documentation contains two types of documents: articles and API references.

Articles include manuals, guides, and tutorials on how to use the MonoGame Framework to create games.

API references provide detailed explanation of each class and method found in the MonoGame Framework. The documentation is written in the [C# XML format](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/xmldoc/xml-documentation-comments) and is inline to the MonoGame source code.

### Generating the Documentation Site[](https://docs.monogame.net/articles/contributing#generating-the-documentation-site)

The pages for articles and API references are hosted on a documentation site that is generated using [DocFX](https://dotnet.github.io/docfx/).

To generate a local copy of the documentation site:

1. Fork the [docs.monogame.github.io](https://github.com/MonoGame/docs.monogame.github.io) repository.
2. Follow the instructions in the site's [readme](https://github.com/MonoGame/docs.monogame.github.io?tab=readme-ov-file#docsmonogamegithubio) for preparing your environment and generating the documentation.
3. If you intend to make contributions to the API References, then run `git submodule update --init --recursive` command to update the `external/MonoGame` submodule to your local fork.
4. Use the `dotnet docfx docfx.json --serve` command to serve a local copy of the documentation site.
5. Browse the running site from `http://localhost:xxxx`.

##### Tip

Verify your changes in your local documentation site before submitting a pull request with said changes. It is recommended to include screenshots of the pages in the pull request to help reviewers confirm these changes.

General Rules[](https://docs.monogame.net/articles/contributing#general-rules)
------------------------------------------------------------------------------

The following rules **must** be observed at all times when contributing documentation to the MonoGame project.

* Write in a neutral, technical tone.
* Avoid humor, personal opinions, and colloquial language.
* **Never** plagiarize any documentation from another source.
* Do not use automatic documentation tools as they are ineffective.

##### Warning

Breaking these rules can result in your contribution being rejected.

General Style Guide[](https://docs.monogame.net/articles/contributing#general-style-guide)
------------------------------------------------------------------------------------------

Because there are many contributors to the MonoGame documentation, it can be difficult to maintain a coherent writing style throughout the documentation site. In addition to the [General Rules](https://docs.monogame.net/articles/contributing#general-rules), this style guide serves to inform contributors of the conventions needed to maintain this writing style. So please review the following expectations before contributing any documentation.

### Every Word Should Contain Value[](https://docs.monogame.net/articles/contributing#every-word-should-contain-value)

Every word in the reference documentation should provide information beyond the API itself. Documentation that only rehashes or rephrases what is already apparent in the class, method, parameter, or property name has zero value and wastes time for both the writer and reader.

### The First Sentence Is the Most Important[](https://docs.monogame.net/articles/contributing#the-first-sentence-is-the-most-important)

There is no guarantee that the reader will read beyond the first sentence of the reference documentation. This is why that first sentence is the most important and should convey the most key piece of information. Take your time to write the most concise and clear first sentence possible. This helps users tremendously and goes a long way towards having great documentation.

### Surface Information Hidden in the Code[](https://docs.monogame.net/articles/contributing#surface-information-hidden-in-the-code)

Being inline with the code allows you to easily look for critical information within it that the user might not know from looking at the API alone. Take your time to explore inner method calls and platform specific sections of the code. The time to write the documentation is once you feel you fully understand the code you are documenting. If you don't feel you understand the code then leave the documentation for someone else to write.

### Focus on What Adds Value to the Consumer[](https://docs.monogame.net/articles/contributing#focus-on-what-adds-value-to-the-consumer)

Limit documentation to public methods and functions unless there is a specific reason to include internal methods, while documenting internals helps with the readability of the code, it provides limited use to consumers of the MonoGame Framework.

### Documentation Is Referenced Not Read[](https://docs.monogame.net/articles/contributing#documentation-is-referenced-not-read)

Remember that the user is searching for an answer for a specific question. It is your job to predict these questions and provide them clear answers.

### Descriptions Should Add Value and Understanding[](https://docs.monogame.net/articles/contributing#descriptions-should-add-value-and-understanding)

Describing a thing by naming the thing does not help the developer to understand what the concept is that you are describing, for example:

> "The Genre class provides information about a genre"

Which does not help someone reading the documentation if they do not know what a `Genre` is. Be descriptive and improve the readers understanding for what something is and WHY it is.

API Reference Style Guide[](https://docs.monogame.net/articles/contributing#api-reference-style-guide)
------------------------------------------------------------------------------------------------------

In addition to the [General Style Guide](https://docs.monogame.net/articles/contributing#general-style-guide), please consider the following conventions used for code associated with the API reference docs.

### XML Tag Guidance[](https://docs.monogame.net/articles/contributing#xml-tag-guidance)

By default, the standard [Microsoft recommendations](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/recommended-tags) should be used for filling in XML tags for each class, method and property.

With a few points to call out:

#### `<see>` and `<cref/>` should be used whenever an API reference is used in the documentation[](https://docs.monogame.net/articles/contributing#see-and-cref-should-be-used-whenever-an-api-reference-is-used-in-the-documentation)

To ensure that API documentation is linked to whichever reference is used, `<see>` and `<cref/>` references should be used. This helps users navigate the methods, especially when looking up initializers or use of a property or method.

#### Avoid self referencing `<cref/>` unless it provides value[](https://docs.monogame.net/articles/contributing#avoid-self-referencing-cref-unless-it-provides-value)

`<cref/>` blocks are there to add links and create references to other classes, functions and methods that help inform the developer for what those concepts are. Adding a `<cref/>` for the same class or property you are describing just creates a circular reference that does not add value.

References to other methods or properties in the same class is fine, just avoid self if possible.

#### Use descriptors in `<see/>` and `<cref/>` statements for better readability[](https://docs.monogame.net/articles/contributing#use-descriptors-in-see-and-cref-statements-for-better-readability)

By default, a `<cref/>` or `<see/>` reference will use only the type you are referencing when rendered to the user, e.g. `<cref="Album.Genre"/>` will render as `Genre`.

Instead, use the descriptor in the style to render what you actually mean, for example: `<cref="Album.Genre">Album.Genre</cref>` which will always render as `Album.Genre` which is much clearer, it is the same for `<see/>` tags.

Comments should be limited to **120** width, with overflow moving to the next line to make reading easier, for example:

```
<summary>
Packed vector type containing unsigned normalized values ranging from 0 to 1. The x and z components use 5 bits,
and the y component uses 6 bits.
</summary>
```

[](https://docs.monogame.net/articles/contributing# "Copy")

##### Note

If the `cref` description would cause the line to exceed the 120 recommendation, this is generally ok, so long as the rendered line does not exceed the limit. The limit however, is more of a guideline than a hard rule, so common sense should be applied to keep the limit near 120 characters.

#### Use the packed multi-line style with surrounding tags[](https://docs.monogame.net/articles/contributing#use-the-packed-multi-line-style-with-surrounding-tags)

To keep the documentation packed and readable, each parameter should be contained to a single line, for example:

```
<summary>
Creates a new instance of Bgr565.
</summary>
<param name="x">The x component</param>
<param name="y">The y component</param>
<param name="z">The z component</param>
```

[](https://docs.monogame.net/articles/contributing# "Copy")

### Interface Documentation[](https://docs.monogame.net/articles/contributing#interface-documentation)

If documentation is already provided by an interface or inherited class, then the `<inheritdoc />` tag should be used. Critically, **DO NOT** duplicate documentation as it increases maintenance later, for example:

```
/// <inheritdoc />
public void InterfaceDefinedMethod()

/// <inheritdoc cref="IDisposable.Dispose()"/>
public void Dispose()
```

[](https://docs.monogame.net/articles/contributing# "Copy")
This applies to all derived elements within a class, property or method.

### Inherited Properties[](https://docs.monogame.net/articles/contributing#inherited-properties)

Where a property or type is already documented in an `enum` or `static`, to avoid duplication the `<inheritdoc cref=""/>` style should be used, for example:

```
public struct VertexPositionColorNormalTexture : IVertexType
    {
        /// <inheritdoc cref="VertexPosition.Position" />
        public Vector3 Position;

        /// <inheritdoc cref="VertexPositionColor.Color" />
        public Color Color;

        /// <inheritdoc cref="VertexPositionNormalTexture.Normal" />
        public Vector3 Normal;

        /// <inheritdoc cref="VertexPositionTexture.Texture" />
        public Vector2 TextureCoordinate;

        /// <inheritdoc cref="IVertexType.VertexDeclaration" />
        public static readonly VertexDeclaration VertexDeclaration;
```

[](https://docs.monogame.net/articles/contributing# "Copy")

### Protected Methods Requiring Documentation by the Linter[](https://docs.monogame.net/articles/contributing#protected-methods-requiring-documentation-by-the-linter)

By default, we do not document Finalizers or other protected methods, the recommendation is to apply an empty `<summary />` tag to suppress the warnings raised by the linter, for example:

```
/// <summary />
~Foo() => Dispose(false);
```

[](https://docs.monogame.net/articles/contributing# "Copy")
License[](https://docs.monogame.net/articles/contributing#license)
------------------------------------------------------------------

All documentation contributed to the MonoGame project is subject to the [Creative Commons Attribution-NonCommercial-ShareAlike](http://creativecommons.org/licenses/by-nc-sa/4.0/) license. By contributing you are agreeing to the terms of that license.

[![Image 1: Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

MonoGame Documentation by the [MonoGame Team](http://www.monogame.net/) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
