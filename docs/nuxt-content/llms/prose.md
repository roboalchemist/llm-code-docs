# Source: https://content.nuxt.com/raw/docs/components/prose.md

# Prose Components

> A list of Prose components.

Prose components are replacements for HTML typography tags. Prose components provide a simple way to customize content UI.

To overwrite a prose component, create a component with the same name in your project `components/content/` directory (ex: `components/content/ProseA.vue`).

<note>

Prose components are originally part of [`@nuxtjs/mdc`](https://github.com/nuxt-modules/mdc).

</note>

## `ProseA`

<code-group>

```md [Code]
[Prose Components](/docs/components/prose)
```

<code-preview label="Preview" icon="i-lucide-eye">

[Prose Components](/docs/components/prose)

</code-preview>
</code-group>

## `ProseBlockquote`

<code-group>

```md [Code]
> Block quote
```

<code-preview label="Preview" icon="i-lucide-eye">

> Block quote

</code-preview>
</code-group>

## `ProsePre`

<code-group>

```md [Code]
```js [file.js]{2} meta-info=val
  export default () => {
    console.log('Code block')
  }
  ```
```

<code-preview label="Preview" icon="i-lucide-eye">

```js [file.js]
export default () => {
  console.log('Code block')
}
```

</code-preview>
</code-group>

Component properties will be:

```json
{
  code: "export default () => {\n    console.log('Code block')\n}"
  language: "js"
  filename: "file.js"
  highlights: [2]
  meta: "meta-info=val"
}
```

Check out the [highlight options](/docs/getting-started/configuration#highlight) for more about the syntax highlighting.

<callout type="warning">

If you want to use `]` in the filename, you need to escape it with 2 backslashes: `\\]`. This is necessary since JS will automatically escape the backslash in a string so `\]` will be resolved as `]` breaking our regex.

</callout>

## `ProseCode`

<code-group>

```md [Code]
`code`

`const code: string = 'highlighted code inline'`{lang="ts"}
```

<code-preview label="Preview" icon="i-lucide-eye">

`code`

`const code: string = 'highlighted code inline'`

</code-preview>
</code-group>

## `ProseH1`

<code-group>

```md [Code]
# H1 Heading
```

<code-preview label="Preview" className="pt-4">

# H1 Heading

</code-preview>
</code-group>

## `ProseH2`

<code-group>

```md [Code]
## H2 Heading
```

<code-preview label="Preview" icon="i-lucide-eye">

## H2 Heading

</code-preview>
</code-group>

## `ProseH3`

<code-group>

```md [Code]
### H3 Heading
```

<code-preview label="Preview" icon="i-lucide-eye">

### H3 Heading

</code-preview>
</code-group>

## `ProseH4`

<code-group>

```md [Code]
#### H4 Heading
```

<code-preview label="Preview" icon="i-lucide-eye">

#### H4 Heading

</code-preview>
</code-group>

## `ProseH5`

<code-group>

```md [Code]
##### H5 Heading
```

<code-preview label="Preview" icon="i-lucide-eye">

##### H5 Heading

</code-preview>
</code-group>

## `ProseH6`

<code-group>

```md [Code]
###### H6 Heading
```

<code-preview label="Preview" icon="i-lucide-eye">

###### H6 Heading

</code-preview>
</code-group>

## `ProseHr`

<code-group>

```md [Code]
Divider under.

---

Divider above.
```

<code-preview label="Preview" icon="i-lucide-eye">

Divider under.

---

Divider above.

</code-preview>
</code-group>

## `ProseImg`

<code-group>

```md [Code]
![A Cool Image](https://nuxt.com/assets/design-kit/icon-green.png)
```

<code-preview label="Preview" icon="i-lucide-eye">

![A Cool Image](https://nuxt.com/assets/design-kit/icon-green.png)

</code-preview>
</code-group>

## `ProseUl`

<code-group>

```md [Code]
- Just
- An
- Unordered
- List
```

<code-preview label="Preview" icon="i-lucide-eye">

- Just
- An
- Unordered
- List

</code-preview>
</code-group>

## `ProseLi`

<code-group>

```md [Code]
- List element
```

<code-preview label="Preview" icon="i-lucide-eye">

- List element

</code-preview>
</code-group>

## `ProseOl`

<code-group>

```md [Code]
1. Foo
2. Bar
3. Baz
```

<code-preview label="Preview" icon="i-lucide-eye">

1. Foo
2. Bar
3. Baz

</code-preview>
</code-group>

## `ProseP`

<code-group>

```md [Code]
Just a paragraph.
```

<code-preview label="Preview" icon="i-lucide-eye">

Just a paragraph.

</code-preview>
</code-group>

## `ProseStrong`

<code-group>

```md [Code]
**Just a strong paragraph.**
```

<code-preview label="Preview" icon="i-lucide-eye">

**Just a strong paragraph.**

</code-preview>
</code-group>

## `ProseEm`

<code-group>

```md [Code]
_Just an italic paragraph._
```

<code-preview label="Preview" icon="i-lucide-eye">

*Just an italic paragraph.*

</code-preview>
</code-group>

## `ProseTable`

<code-group>

```md [Code]
| Key | Type      | Description |
| --- | --------- | ----------- |
| 1   | Wonderful | Table       |
| 2   | Wonderful | Data        |
| 3   | Wonderful | Website     |
```

<code-preview label="Preview" icon="i-lucide-eye">
<table>
<thead>
  <tr>
    <th>
      Key
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      1
    </td>
    
    <td>
      Wonderful
    </td>
    
    <td>
      Table
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      Wonderful
    </td>
    
    <td>
      Data
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      Wonderful
    </td>
    
    <td>
      Website
    </td>
  </tr>
</tbody>
</table>
</code-preview>
</code-group>

## `ProseTbody`

Included in **ProseTable** example.

## `ProseTd`

Included in **ProseTable** example.

## `ProseTh`

Included in **ProseTable** example.

## `ProseThead`

Included in **ProseTable** example.

## `ProseTr`

Included in **ProseTable** example.

<callout icon="i-simple-icons-github" to="https://github.com/nuxt-modules/mdc/tree/main/src/runtime/components/prose">

Checkout the source code for these components on GitHub.

</callout>
