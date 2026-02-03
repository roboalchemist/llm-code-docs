# Source: https://docs.frigade.com/guides/custom/flow-component.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flow Component

`<Flow>` is a generic wrapper that bootstraps all of the functionality of a Frigade Flow. We use it as the basis for building Flow-aware Components in our SDK, and we recommend it as the starting point when building your own custom components.

In this example, we will build a custom announcement component with an open source UI kit. We'll use `AnnouncementProps` and `Flow` from `@frigade/react` to get the data. We'll use [Sanity UI](https://www.sanity.io/ui) primarily to build the UI.

The final result looks like this:

<Frame>
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=29f4e0062593b174af3534d393efb510" style={{maxWidth: '700px'}} data-og-width="2716" width="2716" data-og-height="1527" height="1527" data-path="images/guides/custom/sanity-announcement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e03a17d57d8f684842ac66b9b8fc8393 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b77bf00b5db29d4c85fd940aad744e25 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b2cfd65376cb6331f7087b5a02eeb4f 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4415757676733008a0beecae3f61ba5f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5af6ae32caeb1b1e969f19942d927885 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/custom/sanity-announcement.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a8ef2dd0b39d0d431cfbdbf94e36993f 2500w" />
</Frame>

<Steps>
  <Step title="Create a new Announcement Flow">
    In the Frigade dashboard, tap "Create Flow" from the top right corner and select "Announcement" as the Flow type.
  </Step>

  <Step title="Update the Flow YAML">
    Next, we can update the YAML to include our desired announcement content. Here's an example we can start with:

    ```yaml  theme={"system"}
    steps:
      - id: announcement-page-one
        title: First page title
        subtitle: A space to share more details with users about your product update or announcement.
        primaryButton:
          title: Click me
          uri: https://www.frigade.com
          target: _blank
        secondaryButton:
          title: Next
        imageUri: https://frigade.com/img/grey-box-two.svg
      - id: announcement-page-two
        title: Second page title
        subtitle: This is also a space to share more details with users about your product update or announcement.
        imageUri: https://frigade.com/img/grey-box-two.svg
        primaryButton:
          title: Learn more
          uri: https://www.frigade.com
          target: _blank
    ```
  </Step>

  <Step title="Create a React component">
    Now let's create a React component to render our announcement in the product.

    We will import some components from `@frigade/react` and `@sanity/ui` to build the UI. Here are our imports:

    ```jsx  theme={"system"}
    "use client";
    import { Button, Card, Dialog, Flex, ThemeProvider } from "@sanity/ui";
    import { buildTheme } from "@sanity/ui/theme";
    import { AnnouncementProps, Flow, Progress, Text } from "@frigade/react";
    ```

    Next we have the announcement component. We use `flowId` to connect the component to our Frigade Flow. Then we use the Announcement props such as `step.title`, `step.subtitle`, `step.imageUri`, `step.primaryButton.title`, and `step.secondaryButton.title` to render the content where we like.

    We are using the Sanity UI `Dialog`, `Button`, `Card`, and `Flex` components to build the UI. Sanity doesn't have a component for progress, so we can import the `Progress` component from `@frigade/react` to render optional progress indicators for the current page.
    \`

    ```jsx  theme={"system"}
    export function AnnouncementWithFrigade({
      flowId,
      ...props
    }: AnnouncementProps) {
      return (
        <ThemeProvider theme={buildTheme()}>
          <Flow as={null} flowId={flowId} {...props}>
            {({
              flow,
              handleDismiss,
              handlePrimary,
              handleSecondary,
              parentProps: { dismissible },
              step,
            }) => (
              <Dialog
                __unstable_autoFocus={false}
                header={step.title}
                id="dialog-example"
                onClose={
                  dismissible
                    ? () => {
                        // @ts-expect-error - handleDismiss expects an event to be passed to it
                        handleDismiss();
                      }
                    : undefined
                }
                zOffset={1000}
              >
                <Flex
                  direction="column"
                  gap={4}
                  paddingRight={4}
                  paddingLeft={4}
                  paddingBottom={4}
                >
                  {step.imageUri && (
                    <Card radius={4} overflow="hidden">
                      <img src={step.imageUri} />
                    </Card>
                  )}

                  <Text.Body2>{step.subtitle}</Text.Body2>

                  <Progress.Dots
                    current={flow.getCurrentStepIndex() + 1}
                    marginInline="auto"
                    total={flow.getNumberOfAvailableSteps()}
                  />

                  <Flex direction="row" gap={3}>
                    {step.primaryButton?.title && (
                      <Button
                        onClick={handlePrimary}
                        text={step.primaryButton.title}
                        tone="primary"
                        width="fill"
                      />
                    )}
                    {step.secondaryButton?.title && (
                      <Button
                        onClick={handleSecondary}
                        mode="ghost"
                        space={3}
                        text={step.secondaryButton.title}
                        width="fill"
                      />
                    )}
                  </Flex>
                </Flex>
              </Dialog>
            )}
          </Flow>
        </ThemeProvider>
      );
    }
    ```
  </Step>

  <Step title="Place the component in your product">
    Now, if you've already installed Frigade via the [quick start guide](/quickstart), you can simply place the `AnnouncementWithFrigade` component in your product where you'd like the announcement to appear with the `Flow ID` we generated in the first step. Here's an example of how you might do that:

    ```jsx  theme={"system"}
    "use client";
    import { AnnouncementWithFrigade } from "@/components/Sanity/Announcement";

    const ECommerce: React.FC = () => {
      return (
        <>

          <AnnouncementWithFrigade dismissible={true} flowId="flow_VEJdWA2M" />

          {/* Your application here */}

        </>
      );
    };

    export default ECommerce;
    ```
  </Step>

  <Step title="You're done!">
    That's it! You've built a custom announcement component using the Frigade Engage React SDK and Sanity UI. If you visit the page you should now see your announcement in the product.

    As you interact with the Flow, you will see a user profile generated in the Frigade dashboard. You can delete the user or reset this specific Flow in the user profile page in order to see it again after completing it.

    Of course, you can always use targeting as well to ensure your announcement only shows up after a certain action or to a specific audience.
  </Step>
</Steps>
