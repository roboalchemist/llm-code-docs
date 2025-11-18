# Source: https://www.plain.com/docs/ui-components/plain-text.md

# PlainText

> Useful when you want to show any text that should not have any formatting (is not Markdown). If you want markdown please use [Text](/ui-components/text).

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c3b25fca68dd58308a79128904ee16b8" alt="Example link button" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-plain-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=cf15eca8cc5d5e2b58b8995622c4108c 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=595d8edc4dd88bf4a1a7762ec18c8540 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5b6c590c08bc94c3f374cf07310c55c9 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=240514eced321a6b141dcd7c2e9b6625 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=fd59d1a5000113cead2414bb690a9ab0 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-plain-text.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=c227c92d97fc1b292bd6e8313e0db1d2 2500w" /></Frame>

The plain text component has the following properties:

* `plainText`: the plain text
* `plainTextSize` (optional): one of `S`, `M`, `L`, defaults to `M`
* `plainTextColor` (optional): one of `NORMAL`, `MUTED`, `SUCCESS`, `WARNING`, `ERROR`, defaults to `NORMAL`

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-plain-text.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-plain-text.mdx" />
  </Tab>
</Tabs>
