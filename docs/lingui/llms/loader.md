# Source: https://lingui.dev/ref/loader.md

# Webpack Loader

The `@lingui/loader` is a Webpack loader for Lingui message catalogs. It offers an alternative to the [`lingui compile`](/ref/cli.md#compile) and compiles catalogs on the fly.

It enables you to `import` `.po` files directly, instead of running `lingui compile` and `import`ing the resulting JavaScript (or TypeScript) files.

## Installation[​](#installation "Direct link to Installation")

Install `@lingui/loader` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/loader
```

```
yarn add --dev @lingui/loader
```

```
pnpm add --save-dev @lingui/loader
```

## Usage[​](#usage "Direct link to Usage")

Simply prepend `@lingui/loader!` in front of path to message catalog you want to import.

Here's an example of dynamic import:

```
export async function dynamicActivate(locale: string) {
  const { messages } = await import(`@lingui/loader!./locales/${locale}/messages.po`);
  i18n.load(locale, messages);
  i18n.activate(locale);
}
```

Remember that the file extension is mandatory.

note

Catalogs with the `.json` extension are treated differently by Webpack. They load as ES module with default export, so your import should look like this:

```
const { messages } = (await import(`@lingui/loader!./locales/${locale}/messages.json`)).default;
```

## See Also[​](#see-also "Direct link to See Also")

* [Dynamic Loading of Message Catalogs](/guides/dynamic-loading-catalogs.md)
* [Catalog Formats](/ref/catalog-formats.md)
