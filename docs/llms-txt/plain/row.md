# Source: https://www.plain.com/docs/ui-components/row.md

# Row

> Useful when you need to show two things next to each-other.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=6ce2bf713d71187a30586c634d3bdcfc" alt="Example row" data-og-width="1664" width="1664" data-og-height="636" height="636" data-path="public/images/ui-component-row.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=920dff4f7347ed43b75a60ce23ee92a0 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=6032633c171f82101d8ba39f8c4ac276 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9a076c96015d9a4bbf570e02fb98ec08 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8ecd1afc79f1022fa2c963d69e6a5c0d 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=81f7e53adb543dbb7f99c3d456f99e65 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-row.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2d92c0a5437188bb3e418ed91c506430 2500w" /></Frame>

The row component has the following properties:

* `rowMainContent` (min 1): an array of row components
* `rowAsideContent` (min 1): an array of row components

The following components can be used in a row:

* [Badge](/ui-components/badge)
* [CopyButton](/ui-components/copy-button)
* [Divider](/ui-components/divider)
* [LinkButton](/ui-components/link-button)
* [Spacer](/ui-components/spacer)
* [Text](/ui-components/text)
* [PlainText](/ui-components/plain-text)

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-row.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-row.mdx" />
  </Tab>
</Tabs>
