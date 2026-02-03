# Source: https://www.plain.com/docs/ui-components/text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5e22ab88c83d86088afaffa9c0387cca" alt="Example text" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=9a94b857b76cab657116c6c7ced35a23 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=2ef2faba55d5bd2156ed9a1677a2f983 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=99ec373848a5159a1ad129d44a5aee4f 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=e78285aa9c8ec2e65fa34ae39d5c653a 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=cc568e2b9891bda887eaf3b37f735cfa 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-text.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=997532481a6eef89e0847aa462e3b22a 2500w" /></Frame>

The text component has the following properties:

* `text`: the text. Can include a subset of markdown (bold, italic, and links).
* `textSize` (optional): one of `S`, `M`, `L`, defaults to `M`
* `textColor` (optional): one of `NORMAL`, `MUTED`, `SUCCESS`, `WARNING`, `ERROR`, defaults to `NORMAL`

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-text.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-text.mdx" />
  </Tab>
</Tabs>
