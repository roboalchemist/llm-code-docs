# Source: https://docs.frigade.com/guides/only-target-new-users.md

# Guide: Targeting New Users

> Learn how to use Frigade's [targeting](/platform/targeting) feature to only show a Flow to new users

### Targeting a Flow to new users

When building product onboarding, the brand new user experience is often one of the first experiences teams focus on. In this guide, we'll show you how to set up your Flow so that your new user experience is only shown to new users.

There are several ways to approach this, but we'll cover one of the most straight forward and popular methods.

<Steps>
  <Step title="Write sign up dates to Frigade user properties">
    First, we'll want begin passing user signup or account created dates to Frigade. You can do this by sending the property to Frigade with the SDK. The documentation on [User Hook](/sdk/hooks/user) has more details, but below is a code snippet with an example.

    ```tsx
    import { useUser } from '@frigade/react';

    const { addProperties } = useUser();

    addProperties({
      // Pull this number from your database or auth provider
      createdAt: '2023-08-01T00:00:00.000Z',
    });
    ```

    Once a property is written to Frigade, it will begin to show up in the user properties section of the user detail page and you'll be able to access it for Frigade targeting and dynamic variables.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/guides/targeting/user-properties.png" className="rounded-md" style={{border: '1px solid #E8EBF0',}} />
  </Step>

  <Step title="Add targeting to your Flow">
    Next, open the **Targeting** tab of the Flow detail page. Click `Add filter`, then choose `User property`, and then choose our `createdAt` field we just set for account creation date. Once selected, we can set the logic so only shows it to new users.

    By choosing `is greater than` we can tell Frigade to only show this Flow to users whose sign up date is on or after a specific day, such as the day we roll the experience out. We could also choose an option like `within the last X days` to show an experience to users within a relative time period.

    You can of course adjust and combine the properties and periods to further refine your targeting (e.g. isEnterprise, completedSetup, etc.).

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/guides/targeting/audience-targeting.png" alt="User detail page" className="rounded-md" style={{border: '1px solid #E8EBF0',}} />

    And that's it! Now your Flow will only be shown to users who signed up in the period you specified. If you already have audiences set up with another analytics tool, be sure to check out our [Integrations](/integrations) to connect and use them in Frigade.
  </Step>
</Steps>
