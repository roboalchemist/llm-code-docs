# Source: https://docs.firehydrant.com/docs/markdown-support.md

# Markdown Support

You can use Markdown formatting to write structured content with FireHydrant. We support [basic Markdown syntax](https://www.markdownguide.org/basic-syntax/) with specific limits on which tags are supported. Here's a quick rundown of which tags are supported and the syntax you can use to create them.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Tag
      </th>

      <th style={{ textAlign: "left" }}>
        Markdown Syntax
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Bold/Strong
      </td>

      <td style={{ textAlign: "left" }}>
        `**bold**`or `__bold__`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Italic/Emphasis
      </td>

      <td style={{ textAlign: "left" }}>
        `*italic*` or `_italic_`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Link
      </td>

      <td style={{ textAlign: "left" }}>
        `[Display Text](https://your.url)`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Unordered List
      </td>

      <td style={{ textAlign: "left" }}>
        `- item`\
        `- item`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Ordered List
      </td>

      <td style={{ textAlign: "left" }}>
        `1. item`\
        `2. item`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Nested List
      </td>

      <td style={{ textAlign: "left" }}>
        `- Top-level`\
        \--->`- Nested (4 preceding spaces per level)`

        `1. Top-level`\
        \--->`1. Nested (4 preceding spaces per level)`

        `1. Mixed`\
        \--->`- Nested 4 spaces in`\
        \--->--->`1. Nested 8 spaces in`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Pull Quote
      </td>

      <td style={{ textAlign: "left" }}>
        `> text`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Inline Code
      </td>

      <td style={{ textAlign: "left" }}>
        `inline code`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Code Block
      </td>

      <td style={{ textAlign: "left" }}>
        ```
        `code block`  
        ```
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Horizontal Rule
      </td>

      <td style={{ textAlign: "left" }}>
        `---` or `***`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Images
      </td>

      <td style={{ textAlign: "left" }}>
        `![Alt Txt](https://imageurl.com)`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Tables
      </td>

      <td style={{ textAlign: "left" }}>
        `| Food | Type |`\
        `| ------|------|`\
        `| Apple | Fruit |`\
        `| Carrot | Vegetable |`
      </td>
    </tr>
  </tbody>
</Table>