# Source: https://www.plain.com/docs/ui-components/copy-button.md

# CopyButton

> Useful if you have any IDs or other details you want to copy for use in messages or outside of Plain.

<Frame><img src="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5bd714d7543fdbf68cd0fcaaa083e8c4" alt="Example copy button" data-og-width="1664" width="1664" data-og-height="300" height="300" data-path="public/images/ui-component-copy-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=280&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=3fe1ffdc916132f41747f147d7d2b776 280w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=560&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=8ec044f8c1dea26db21619ee9f96e8ed 560w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=840&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=d46c23227f0c4eb6c9652ac89f24a37b 840w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=1100&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=20cf5bb3f6465048c002ae636e7e2f71 1100w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=1650&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=4029bf2e012a22dd444ad5f7c0044ad3 1650w, https://mintcdn.com/plain/EjhjILX5S36Y2AF-/public/images/ui-component-copy-button.png?w=2500&fit=max&auto=format&n=EjhjILX5S36Y2AF-&q=85&s=5999b3cef45c547e413aa4ee8d185096 2500w" /></Frame>

A copy button has the following properties:

* `copyButtonTooltipLabel` (optional): the text that should be displayed on hover. Defaults to the value if not
  provided.
* `copyButtonValue`: the value that should be copied to the user's clipboard after clicking the button

For example:

<Tabs>
  <Tab title="Typescript SDK">
    <Snippet file="typescript-sdk/ui-copy-button.mdx" />
  </Tab>

  <Tab title="GraphQL">
    <Snippet file="graphql/ui-copy-button.mdx" />
  </Tab>
</Tabs>
