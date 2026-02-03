# Source: https://docs.frigade.com/guides/only-target-new-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide: Targeting New Users

> Learn how to use Frigade's [targeting](/platform/targeting) feature to only show a Flow to new users

### Targeting a Flow to new users

When building product onboarding, the brand new user experience is often one of the first experiences teams focus on. In this guide, we'll show you how to set up your Flow so that your new user experience is only shown to new users.

There are several ways to approach this, but we'll cover one of the most straight forward and popular methods.

<Steps>
  <Step title="Write sign up dates to Frigade user properties">
    First, we'll want begin passing user signup or account created dates to Frigade. You can do this by sending the property to Frigade with the SDK. The documentation on [User Hook](/sdk/hooks/user) has more details, but below is a code snippet with an example.

    ```tsx  theme={"system"}
    import { useUser } from '@frigade/react';

    const { addProperties } = useUser();

    addProperties({
      // Pull this number from your database or auth provider
      createdAt: '2023-08-01T00:00:00.000Z',
    });
    ```

    Once a property is written to Frigade, it will begin to show up in the user properties section of the user detail page and you'll be able to access it for Frigade targeting and dynamic variables.

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=70d3ab7238176d7b7bee44c2d47b4b9f" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="1262" width="1262" data-og-height="830" height="830" data-path="images/guides/targeting/user-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=96b3ecb80b417e9a9b70c90edec0872e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=dbafc7b4523c4b552e23bf4cdea360e3 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1f900f6cdfa0722484e3395d7724c830 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8dec08c9c7485d10493779b4c381e72f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d04228b21bf0e0ae0e84bbdcb8446d80 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/user-properties.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7db1a9b33f4cecf8738daa91ee5f2de9 2500w" />
  </Step>

  <Step title="Add targeting to your Flow">
    Next, open the **Targeting** tab of the Flow detail page. Click `Add filter`, then choose `User property`, and then choose our `createdAt` field we just set for account creation date. Once selected, we can set the logic so only shows it to new users.

    By choosing `is greater than` we can tell Frigade to only show this Flow to users whose sign up date is on or after a specific day, such as the day we roll the experience out. We could also choose an option like `within the last X days` to show an experience to users within a relative time period.

    You can of course adjust and combine the properties and periods to further refine your targeting (e.g. isEnterprise, completedSetup, etc.).

    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=18a1ba27a4a2c0648a809537554b071d" alt="User detail page" className="rounded-md" style={{border: '1px solid #E8EBF0',}} data-og-width="1380" width="1380" data-og-height="802" height="802" data-path="images/guides/targeting/audience-targeting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b07aa401a1bfe3c39fdf8982e01c21f6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fb1fe0fc047edc93a9301790fcc082af 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=703e4eb660d9e672095c0a631dd3f319 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=bb8340884bca79dc515d54be9f1d0c90 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e2ae69dbc192a06ac17f8a11c5a03ed0 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/targeting/audience-targeting.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=12d78458757e707a0ff69ff8ee00032a 2500w" />

    And that's it! Now your Flow will only be shown to users who signed up in the period you specified. If you already have audiences set up with another analytics tool, be sure to check out our [Integrations](/integrations) to connect and use them in Frigade.
  </Step>
</Steps>
