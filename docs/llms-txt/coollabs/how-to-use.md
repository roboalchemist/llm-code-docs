# Source: https://docs.coollabs.io/fonts/how-to-use.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.coollabs.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to use

> How to get started with Fonts

Change the domain name from `fonts.googleapis.com` to `api.fonts.coollabs.io` in your `<head>` tag; that's it!

Example:

Original `<head>` content:

```html  theme={null}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
```

Replaced `<head>` content:

```html  theme={null}
<link rel="preconnect" href="https://api.fonts.coollabs.io" crossorigin>
<link href="https://api.fonts.coollabs.io/css2?family=Roboto&display=swap" rel="stylesheet">
```

Or with `@import`:

From:

```css  theme={null}
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
</style>
```

To:

```css  theme={null}
<style>
@import url('https://api.fonts.coollabs.io/css2?family=Roboto&display=swap');
</style>
```

Currently, it only supports the css2 [API endpoint](https://developers.google.com/fonts/docs/css2).

## Icons

Currently, [Material Icons](https://fonts.google.com/icons) is supported.

Original `<head>` content:

```html  theme={null}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

Replaced `<head>` content:

```html  theme={null}
<link rel="preconnect" href="https://api.fonts.coollabs.io" crossorigin>
<link href="https://api.fonts.coollabs.io/icon?family=Material+Icons" rel="stylesheet">
```
