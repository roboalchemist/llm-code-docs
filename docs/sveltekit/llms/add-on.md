# add-on

> [!NOTE]
> Community add-ons are currently **experimental**. The API may change. Don't use them in production yet!

This guide covers how to create, test, and publish community add-ons for `sv`.

## Quick start

The easiest way to create an add-on is using the addon template:

```sh
npx sv create --template addon my-addon
cd my-addon
```

## Add-on structure

Typically, an add-on looks like this:

_hover keywords in the code to have some more context_

```js
import { parse, svelte } from '@sveltejs/sv-utils';
import { defineAddon, defineAddonOptions } from 'sv';

// Define options that will be prompted to the user (or passed as arguments)
const options = defineAddonOptions()
 .add('who', {
  question: 'To whom should the addon say hello?',
  type: 'string' // boolean | number | select | multiselect
 })
 .build();

// your add-on definition, the entry point
export default defineAddon({
 id: 'your-addon-name',

 options,

 // preparing step, check requirements and dependencies
 setup: ({ dependsOn }) => {
  dependsOn('tailwindcss');
 },

 // actual execution of the addon
 run: ({ kit, cancel, sv, options }) => {
  if (!kit) return cancel('SvelteKit is required');

  // Add "Hello [who]!" to the root page
  sv.file(kit.routesDirectory + '/+page.svelte', (content) => {
   const { ast, generateCode } = parse.svelte(content);

   svelte.addFragment(ast, `<p>Hello ${options.who}!</p>`);

   return generateCode();
  });
 }
});
```

## Development with `file:` protocol

While developing your add-on, you can test it locally using the `file:` protocol:

```sh