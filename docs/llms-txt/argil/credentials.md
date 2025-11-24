# Source: https://docs.argil.ai/pages/get-started/credentials.md

# API Credentials

> Create, manage and safely store your Argil's credentials

<Info>
  `Prerequisite` You should have access to Argil's app with a paid plan to
  complete this step.
</Info>

<Steps>
  <Step title="Go to the API integration page from the app">
    Manage your API keys by clicking [here](https://app.argil.ai/developers) or
    directly from the app's sidebar.
  </Step>

  <Step title="Create your API Key">
    From the UI, click on `New API key` and follow the process.

    <Frame>
      <img src="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=9b2425b5bb6269a0f906860fa26fe4aa" style={{ borderRadius: "0.5rem" }} data-og-width="1576" width="1576" data-og-height="419" height="419" data-path="images/api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=280&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=bad0eb248a6d3d131202b3d0a7ec33f4 280w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=560&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=949fc3af500b7ef591cba3f8ce9a348a 560w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=840&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=6d273bbb7c65a663400c7fef9be04f87 840w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=1100&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=95c5bc649f11eb9c7307a2546f82c6a8 1100w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=1650&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=bbe26c5fd2f43377887d5d4d74ba2c30 1650w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=2500&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=64f400cf311a3453b409c54729b1fc51 2500w" />
    </Frame>
  </Step>

  <Step title="Use it in your request headers">
    Authenticate your requests by including your API key in the `x-api-key`
    header. \`\`\`http x-api-key: YOUR\_API\_KEY. \`\`\`\`
  </Step>

  <Step title="Implementing Best Practices for Storage and API Key Usage">
    It is essential to adhere to best practices regarding the storage and usage
    of your API key. This information is sensitive and crucial for maintaining
    the security of your services.

    <Tip>
      If any doubt about the corruption of your key, delete it and create a new
      one.
    </Tip>

    <Warning>
      Don't share your credentials with anyone. This API key enables video
      generation featuring your avatar, which may occur without your explicit
      authorization.
    </Warning>

    <Warning>Please note that Argil cannot be held responsible for any misuse of this functionality. Always ensure that your API key is handled securely to prevent unauthorized access.</Warning>
  </Step>
</Steps>

## Troubleshooting

Here's how to solve some common problems when working around your credentials setup.

<AccordionGroup>
  <Accordion title="Having troubles with your credentials setup?">
    Let us assist by [Mail](mailto:brivael@argil.ai) or
    [Discord](https://discord.gg/Xy5NEqUv).
  </Accordion>
</AccordionGroup>
