# Source: https://docs.frigade.com/platform/dynamic-variables.md

# Dynamic Variables

Sometimes you want to use a dynamic piece of content within your Flow such as an email address or a localized string for  [i18n](/platform/i18n). In these cases, you can use **dynamic variables** to personalize for each user.

### Setting Dynamic Variables

***

Flows support setting custom variables anywhere in the data defined from the Frigade dashboard with the `${variable}` pattern. For instance,
your Flow might look like this:

```yml
steps:
  - id: "announcement-page-1"
  - title: "Welcome to Acme, ${firstName}!"
```

Then using your React component of choice, you can set the `firstName` variable like so:

```tsx
<Frigade.Announcement
  ...
  variables={{
    firstName: 'Christian'
  }}
/>
```

Variables can also be added at the global level via the `<Frigade.Provider />`. This will make them accessible in all Flows and [Collections](/platform/collections).
To pass in variables globally, simply pass the `variables` object to the provider:

```tsx
<Frigade.Provider
  ...
  variables={{
    firstName: 'Christian'
  }}
/>
```

See the [Provider documentation](/sdk/provider#variables) for more details.
