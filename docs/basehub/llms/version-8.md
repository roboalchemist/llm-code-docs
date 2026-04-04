# Version 8

> Learn how to upgrade from v7 to v8.

```
pnpm i basehub@latest
```

## New Features

*   `basehub/events`: a new package used to interact with the [Event Block](https://docs.basehub.com/blocks/primitives/event).
    
*   `basehub` and `<Pump />` now automatically infer `draftMode` from Next.js.
    
*   `<Toolbar />` now includes a Branch Switcher!
    
*   Support for internal links in <RichText />
    

## SDK Breaking Changes

*   `basehub/analytics` has been deprecated in favour of `basehub/events` . They are slightly different things, but Events should be able to cover analytics use cases, and more.
    
*   <CodeBlock />: `lang` was renamed to `language` to better match the props of the `pre` handler in <RichText />
    
*   <RichText />: The `code` handler before received a prop named `isInline`, but now, it won’t receive that and it will just be used for inline code. The `pre` handler will be used for full code blocks.
    

## API Breaking Changes

*   Now, if a Reference Block has just one “allowed type”, we won't type it as a GraphQL Union, but rather, just return the end-type directly. this might break queries that did the `... on SomeType` thing.
    

```