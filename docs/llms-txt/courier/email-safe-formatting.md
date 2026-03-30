# Source: https://www.courier.com/docs/platform/content/email-safe-formatting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email Safe Formatting

> Use inline CSS, simple HTML tags, and table-based layouts. Stick to email-safe fonts and image hosting guidelines. Test responsiveness and rendering across email clients to ensure consistent formatting.

Email clients vary widely in their HTML and CSS support. This guide covers the formatting techniques that render reliably across Gmail, Outlook, Apple Mail, and other major email clients.

## Inline CSS

Use inline CSS styles rather than external or internal stylesheets. This ensures that your styling is more likely to be rendered consistently across various email clients. You can also use the [brands designer](/platform/content/brands/brands-overview) to apply CSS styles to your email templates.

<Warning>
  Some email clients like [Gmail will only support](https://www.emailonacid.com/blog/article/email-development/12_things_you_must_know_when_developing_for_gmail_and_gmail_mobile_apps-2/#:~:text=link%20will%20appear.-,4.%20Gmail%20only%20supports%20%3Cstyle%3E%20in%20the%20%3Chead%3E,-Gmail%20does%20support) `<styles>` in the `<head>` element.
</Warning>

## Basic HTML Tags

Stick to basic HTML tags like `<p>`, `<div>`, `<span>`, `<a>`, `<strong>`, `<em>`, `<ul>`, `<ol>`, `<li>`, `<h1>` to `<h6>`, etc. These are widely supported across email clients.

## Tables

Tables are often used for layout in HTML emails because they are well-supported across different email clients. However, keep your table structures simple and avoid complex nesting.

Email clients like Gmail impose limitations on HTML tables:

* Handling of nested tables can be inconsistent, leading to layout distortions or unexpected behavior.
* Lack of support for conditional formatting within table cells, which limits dynamic content presentation.

## Inline Images

Embed images using the `<img>` tag and provide appropriate alt attributes for accessibility. Make sure to host your images on a reliable server.

<Note>
  Courier does not host images for `src` paths. The exception is [Image Blocks](/platform/content/content-blocks/image-blocks), which host the image on Courier's server.
</Note>

## Links

Use the `<a>` tag for hyperlinks. Ensure that all links are clickable and provide descriptive anchor text.

## Font Styles

Use CSS for basic font styles like color, size, family, and weight. Avoid using web fonts that may not be supported by all email clients.

### Web Fonts vs Email-Safe Fonts

Web fonts are stored online and downloaded by browsers via CSS (typically using the `@font-face` declaration). Most email clients do not support web fonts; only a handful do:

* Apple Mail
* iOS Mail
* Android Mail (not Gmail)
* Thunderbird
* Outlook for macOS

For reliable rendering across all email clients, use email-safe fonts:

| Font            | Category   | Email-Safe? | Web-Safe? |
| --------------- | ---------- | ----------- | --------- |
| Arial           | sans-serif | Yes         | Yes       |
| Verdana         | sans-serif | Yes         | Yes       |
| Helvetica       | sans-serif | No          | Yes       |
| Tahoma          | sans-serif | No          | Yes       |
| Trebuchet MS    | sans-serif | Yes         | Yes       |
| Times New Roman | serif      | Yes         | Yes       |
| Georgia         | serif      | Yes         | Yes       |
| Garamond        | serif      | No          | Yes       |
| Courier New     | monospace  | Yes         | Yes       |
| Brush Script MT | cursive    | No          | Yes       |

"Email-safe" fonts are the subset most likely to render consistently across email platforms. You can also [discover an email-safe font](https://www.emailonacid.com/blog/article/email-development/best-font-for-email-everything-you-need-to-know-about-email-safe-fonts/) that matches your brand's preferred typeface.

## Background Colors

You can set background colors for elements using CSS. Keep in mind that some email clients may not fully support background colors.

## Responsive Design

Use responsive design techniques to ensure that your email renders well on different devices and screen sizes. [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries) can adjust the layout based on the viewport size.

## Microsoft Outlook Compatibility

Microsoft Outlook 2019 and earlier versions use Microsoft Word's rendering engine, which has strict requirements and behaves differently from modern email clients. To ensure your emails render correctly in Outlook, you'll need to use MSO (Microsoft Office) conditional comments.

<Warning>
  Outlook 2019 does not respect `max-width` on `<div>` elements. You must use table-based layouts with explicit `width` attributes for Outlook compatibility.
</Warning>

### Using MSO Conditional Comments

MSO conditional comments let you provide Outlook-specific markup while keeping standard HTML for other email clients.

The standard pattern wraps your table structure with MSO conditionals:

```html  theme={null}
<!--[if mso]>
<table width="600" style="width:600px;">
  <tr><td>
<![endif]-->
<table width="100%" style="max-width:600px;">
  <!-- Email content -->
</table>
<!--[if mso]></td></tr></table><![endif]-->
```

### Formatting MJML for Outlook Compatibility

MJML compiles to div-based structures which Outlook doesn't handle well. For Outlook-critical sections, use `<mj-raw>` to inject raw HTML tables with MSO conditionals.

For [MJML brand footers](/platform/content/brands/brands-overview#custom-mjml/handlebars-template) that need MSO/Outlook compatibility, use `<mj-raw>` to inject Outlook-safe HTML:

```mjml  theme={null}
<mj-raw>
  <!--[if mso]>
  <table role="presentation" width="600" style="width:600px;">
    <tr><td>
  <![endif]-->
  <table role="presentation" width="100%" style="max-width:600px;">
    <tr>
      <td>
        Footer content
      </td>
    </tr>
  </table>
  <!--[if mso]></td></tr></table><![endif]-->
</mj-raw>
```

### Key Outlook Best Practices

* **Use table-based layouts**: Outlook 2019 doesn't respect `max-width` on divs. Always use `<table>` elements with explicit `width` attributes.
* **Maintain consistent widths**: If your email width is 600px, all sections (header, body, footer) should use 600px. Mixing different width values causes misalignment in Outlook.
* **Use `role="presentation"`**: Always include `role="presentation"` on layout tables to prevent screen readers from treating them as data tables.
* **Set background colors on tables**: Outlook may ignore background colors on divs. Set background colors on both `<table>` and `<td>` elements.

### Minification and MSO Comments

If your workspace has MJML minification enabled, the minifier may strip MSO conditional comments (`<!--[if mso]>...<![endif]-->`) from the compiled output. If your Outlook-specific layout tables disappear after sending, contact support to check whether the `minify-mjml` flag is active on your workspace.

Always verify the compiled HTML output to ensure Outlook compatibility, as MJML compilers may introduce unexpected CSS values or structures.

## CSS Properties to Avoid

Many modern CSS properties are unsupported or inconsistently rendered across email clients. Avoid these unless you have a tested fallback.

| Property                                | Support                              | Workaround                                |
| --------------------------------------- | ------------------------------------ | ----------------------------------------- |
| `animation`, `transition`               | Almost none                          | Use animated GIFs for motion              |
| `position: absolute/fixed`              | None                                 | Use table-based positioning               |
| `display: flex`, `display: grid`        | Minimal (Apple Mail only)            | Use `<table>` layouts                     |
| `box-shadow`                            | Partial (no Outlook)                 | Use border or image-based shadows         |
| `border-radius`                         | Partial (no Outlook on Windows)      | Accept square corners as fallback         |
| `opacity`                               | Partial (no Outlook)                 | Use transparent PNGs instead              |
| `calc()`                                | Minimal                              | Use fixed pixel values                    |
| `filter` (blur, grayscale, etc.)        | Almost none                          | Pre-process images before embedding       |
| `:hover`, `:focus`, `:before`, `:after` | Minimal                              | Avoid pseudo-elements and states entirely |
| `@media` queries                        | Partial (no Gmail app, some Outlook) | Design mobile-first at 600px max width    |
| `object-fit`                            | Almost none                          | Crop and size images before embedding     |
| `clip-path`, `mask`                     | None                                 | Use pre-cropped images                    |

<Warning>
  Outlook 2019 and earlier use Microsoft Word's rendering engine, which ignores most CSS beyond basic font, color, margin, padding, and border properties. Always test Outlook rendering separately.
</Warning>

## Converting Web HTML to Email HTML

If you're porting an existing web design to email, use this checklist to catch the most common issues.

1. **Replace flexbox/grid with tables.** Use `<table>`, `<tr>`, `<td>` for all layout. Add `role="presentation"` to layout tables for accessibility.
2. **Move all CSS inline.** External stylesheets and most `<style>` blocks are stripped by email clients. Exception: you can use `<style>` in the `<head>` for Gmail (see [Inline CSS](#inline-css)).
3. **Replace `div` containers with table cells.** Outlook ignores `max-width` on `<div>` elements.
4. **Set explicit widths in pixels.** Percentage widths are unreliable in nested tables. Use a 600px max width for the outer container.
5. **Use `!important` on class-based styles.** Courier's MJML compiler generates inline styles that take precedence. Your custom CSS classes need `!important` to override them (see [CSS Classnames](/platform/content/brands/css-classnames)).
6. **Host images externally.** Use absolute URLs. Courier does not host images for `src` paths (exception: [Image Blocks](/platform/content/content-blocks/image-blocks)).
7. **Add MSO conditionals for Outlook.** See [Microsoft Outlook Compatibility](#microsoft-outlook-compatibility) for the pattern.
8. **Test across clients.** Rendering can vary dramatically. See [Testing](#testing) below.

## Testing

Always [test your HTML emails](/platform/content/template-designer/how-to-preview-notification) across different email clients and devices to ensure consistent rendering. Tools like [Litmus](https://www.litmus.com/) and [Email on Acid](https://www.emailonacid.com/) can help with cross-client testing.

<CardGroup cols={2}>
  <Card title="Brand Designer" href="/platform/content/brands/brand-designer" icon="palette">
    Customize headers, footers, and CSS in your brand templates
  </Card>

  <Card title="CSS Classnames" href="/platform/content/brands/css-classnames" icon="paintbrush">
    Style Courier blocks with custom CSS class selectors
  </Card>

  <Card title="Template Blocks" href="/platform/content/content-blocks/template-blocks" icon="code">
    Write custom HTML and Handlebars in your templates
  </Card>

  <Card title="Image Blocks" href="/platform/content/content-blocks/image-blocks" icon="image">
    Add images with Courier-hosted URLs
  </Card>
</CardGroup>
