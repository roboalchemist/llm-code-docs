# Source: https://www.plain.com/docs/ui-components/container.md

# Container

> Useful when you need to create a bit of structure.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=0004c23b00a957648fc806df44b36c9a" alt="Example container" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-container.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=f06050e39d008bd20637613a6f24b70b 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=30fc9ef139fac29d52e45fee8eb4b0cb 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=bf34459725c80bed6fb0b53f539a78af 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=1a0720f29972fc7b46cab78cb7edf7ea 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=a3f93995d1ffd932ad709c8bf5dc3074 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-container.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=18ea07314d952e4aa1b6ca903bef573c 2500w" /></Frame>

A container has the following properties:

* `containerContent` (min 1): an array of components.

Allowed components within a Container are:

* [Badge](/ui-components/badge)
* [CopyButton](/ui-components/copy-button)
* [Divider](/ui-components/divider)
* [LinkButton](/ui-components/link-button)
* [Row](/ui-components/row)
* [Spacer](/ui-components/spacer)
* [Text](/ui-components/text)
* [PlainText](/ui-components/plain-text)

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-container.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-container.mdx" />
  </Tab>
</Tabs>
