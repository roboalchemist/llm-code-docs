# nextjs/no-duplicate-head

## What it does

Prevent duplicate usage of `<Head>` in \`pages/\_document.js\`\.

## Why is this bad?

This can cause unexpected behavior in your application.

## Examples

### Incorrect Code

Examples of **incorrect** code for this rule:

```jsx
import Document, { Html, Head, Main, NextScript } from "next/document";
class MyDocument extends Document {
  static async getInitialProps(ctx) {}
  render() {
    return (
      <Html>
        <Head />
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
export default MyDocument;
```

### Correct Code

Examples of **correct** code for this rule:

```jsx
import Document, { Html, Head, Main, NextScript } from "next/document";
class MyDocument extends Document {
  static async getInitialProps(ctx) {}
  render() {
    return (
      <Html>
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
export default MyDocument;
```

## How to Use

To **enable** this rule using the config file or in the CLI, you can use:

```json [Config (.oxlintrc.json)]
{
  "plugins": ["nextjs"],
  "rules": {
    "nextjs/no-duplicate-head": "error"
  }
}
```

```bash [CLI]
oxlint --deny nextjs/no-duplicate-head --nextjs-plugin
```

## References

* Rule Source