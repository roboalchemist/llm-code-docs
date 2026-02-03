# Source: https://docs.frigade.com/sdk/quickstart.md

# Source: https://docs.frigade.com/sdk/js/quickstart.md

# Source: https://docs.frigade.com/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Frigade Engage Quickstart Guide

> Get set up with Frigade Engage in less than 15 minutes

<img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c09c3a4cb253ff4c9dcd772251ddb095" className="rounded pointer-events-none" data-og-width="2171" width="2171" data-og-height="944" height="944" data-path="images/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5d7f6759b7f82b258948a7283b73e94c 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37420c9445b969bbba94e12b262d6a92 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=c48be5b63b0165f1023f2aa58d39abef 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f1515e30ee2abd4aacc10edfb9eac742 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f7827da35206c38e1ad7d9f85fb995ec 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/welcome.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2c56365efaebc0a0e0f41c3ee548d632 2500w" />

<Steps>
  <Step title="Sign up and install">
    <AccordionGroup>
      <Accordion title="Get your API key">
        The first thing to do is sign up for a Frigade account at [frigade.com](https://app.frigade.com/sign-up). Then, locate your Frigade public API key in the [Developer](https://app.frigade.com/developer) tab of the dashboard.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5e6542db65e287c2a4be1e72267acfaa" data-og-width="1408" width="1408" data-og-height="526" height="526" data-path="images/platform/developer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=87c8f99108fb020261cb82887b94b02f 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=80566e99244aba45a6433d99d4f78e10 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3f5ef5a43f1507d88f4a988dff376c90 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=dbc6918b6d9a8056bcf95d850cf2691b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=1dd626800e1591de19efba8aa8476b86 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/developer.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=911ce393220071c4f9640362a0b10327 2500w" />
        </Frame>
      </Accordion>

      <Accordion title="Install the React SDK">
        Install <a href="https://www.npmjs.com/package/@frigade/react" target="_blank" rel="noreferrer">@frigade/react</a> with your package manager.

        <CodeGroup>
          ```txt npm theme={"system"}
          npm install @frigade/react
          ```

          ```txt pnpm theme={"system"}
          pnpm install @frigade/react
          ```

          ```txt yarn theme={"system"}
          yarn add @frigade/react
          ```
        </CodeGroup>

        Next, add the Frigade `Provider` component to your app and plug in your public API key from earlier. We recommend wrapping your entire application to ensure that the SDK is available everywhere.
        Below are examples for how to install the Provider in popular React frameworks.

        <CodeGroup>
          ```tsx React theme={"system"}
          // Add this to your main application file, e.g., App.tsx or index.tsx
          import * as Frigade from "@frigade/react";

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          export const App: React.FC = () => {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                {/* ... */}
              </Frigade.Provider>
            );
          };
          ```

          ```tsx Next.js (App router) theme={"system"}
          // frigade-provider-wrapper.tsx
          "use client";
          import * as Frigade from "@frigade/react";
          import { ReactNode } from 'react';

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          interface FrigadeProviderWrapperProps {
            children: ReactNode;
          }

          const FrigadeProviderWrapper: React.FC<FrigadeProviderWrapperProps> = ({ children }) => {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                {children}
              </Frigade.Provider>
            );
          };

          // layout.tsx
          export default function Layout({ children }: { children: ReactNode }) {
            return (
              <FrigadeProviderWrapper>
                {children}
              </FrigadeProviderWrapper>
            );
          }
          ```

          ```tsx Next.js (Pages router) theme={"system"}
          // Add this to your _app.tsx file
          import * as Frigade from "@frigade/react";
          import { AppProps } from 'next/app';

          // Replace this with your Frigade public API key
          const FRIGADE_API_KEY = "api_public_abcd1234";

          function MyApp({ Component, pageProps }: AppProps) {
            return (
              <Frigade.Provider 
                apiKey={FRIGADE_API_KEY}
                // Replace this with the ID of the signed in user
                userId="my-user-id"
                userProperties={{
                  email: "john@doe.com",
                  name: "John Doe"
                }}
              >
                <Component {...pageProps} />
              </Frigade.Provider>
            );
          }

          export default MyApp;
          ```
        </CodeGroup>

        Great! Now you're ready to start building.
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Building and styling">
    <AccordionGroup>
      <Accordion title="Create a Flow">
        **Add a Flow to your application**

        For this example, let's add a `Banner` to our product.

        1. Click the **Create** button at the top of any page in the dashboard. Select the **Banner** component.
        2. On the Flow detail page, click the **Deploy** button. Copy the code snippet to your clipboard.
        3. Next, place the `<Frigade.Banner />` component in your application. Make sure to do this in a subcomponent of the `<Frigade.Provider />` component.

        ```tsx  theme={"system"}
        import * as Frigade from "@frigade/react";

        export const MyComponent = () => {
          return <Frigade.Banner flowId="flow_abcd1234" />;
        };
        ```

        **View the Flow**

        Tada! You should now see a shiny `Frigade Banner` where you placed it.

        <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1b065e68687f91cfec0edcd7a47f003f" data-og-width="1710" width="1710" data-og-height="401" height="401" data-path="images/platform/banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=23ebc8245b0210617488ac27208c526c 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6f9f99e204a5f18153d85e213e4f3a73 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=d17c648c9aa128313e66a8ab75ba5ca1 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a61e06b1f39289419b29e83e6f19cd2f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7916813a184b39e22f03adb76b3d3ed2 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/platform/banner.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=72e736a9754a0f0a77da00d02777bf3c 2500w" />

        **See users in the Flow**

        Once you interact with the Flow in your application, you should see your user appear in the users tab of the Flow detail page. You can reset a user's progress in the Flow from here, which is especially useful for testing.

        <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=2f0eb06f64cfd58dcb5b9558e538b2f4" data-og-width="2987" width="2987" data-og-height="521" height="521" data-path="images/platform/reset-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6aa273b976f50bde5547e6c2cad6ee34 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=90f28649e5d111df07d360bfc39426d6 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e1575f9fbe510e617578aefcc9c6027 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=27d5352ee8c1b2eef593d4f094e470b4 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=238e08f31e49911e3410a6e83a17f4ba 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/reset-user.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=242c5e83883be71a665f3c7ca49a78ce 2500w" />
      </Accordion>

      <Accordion title="Updating Flows">
        Once a Flow is created, you can update it at any time from the dashboard.

        1. Navigate to the [Flows](https://app.frigade.com/flows) page and select a Flow
        2. In the Editor tab you can make changes with the basic or advanced editor
        3. Make changes and click **Save** and Frigade will update the Flow in real-time

        Check out the documentation for each component to see all the configuration options. Check out the [Banner](/component/banner) component for this quickstart demo.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=fc40523ed27e6c6ced0882293f0e7ecc" data-og-width="4598" width="4598" data-og-height="2410" height="2410" data-path="images/platform/editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e10b2892db864e36792081193d199be0 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7985c658200915d98ff903edbd812c34 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7bcbeebc8e05529ab0d9ebbf7e6ab55b 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8a02113fd5d1826db7f4f39444871c2b 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=b8567865f7d8035a3d1b63fc83ffeffe 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/editor.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=0884c324dc8a5a18b4d586b8fd93ebfc 2500w" />
        </Frame>

        <Note>If you plan to make major changes to a Flow, we recommend [version control](/platform/versioning).</Note>
      </Accordion>

      <Accordion title="User targeting">
        Sometimes you only want to show an experience to a specific user or group of users. Frigade makes this easy with [targeting](/platform/targeting).

        1. Navigate to the Flows page and select a Flow
        2. In the **Targeting** tab you can define the targeting for the Flow
        3. Frigade makes sure the Flow is only shown to users that match your criteria

        Check out [integrations](/integrations) to connect other platforms and import existing user segments for targeting.

        <Frame>
          <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3ff629c1598a46737aad2579fcd342b1" data-og-width="3456" width="3456" data-og-height="1926" height="1926" data-path="images/platform/flow-detail-audience.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6be15fee4c76d9da2cd14014ff762843 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=59a1aeb9087ce79ce5e731351740b43f 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=6430d0069d4fb14ef1a4271bdee6c85f 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=25d1e7ec6bd9d9ffc8fd030b1a05a7f6 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5ad647ada4e6bf57add11f123df68e43 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/platform/flow-detail-audience.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=d05ba711ef7422ebb937b35ea9b75ad6 2500w" />
        </Frame>
      </Accordion>

      <Accordion title="Styling Flows">
        Frigade is fully customizable. You can style components to fit seamlessly within your application. Styling documentation is covered [here](/sdk/styling/). You can also see a live demo of the theming system at [demo.frigade.com](https://demo.frigade.com).

        <video autoPlay muted loop playsInline className="w-full aspect-video" src="https://app.frigade.com/images/marketing/img/themes-1.mp4" />
      </Accordion>

      <Accordion title="Custom components">
        When a pre-built Frigade UI component won't cut it, you can also build custom components with the Frigade SDK. See our custom component guide [here](/guides/custom).
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Nice work!">
    You've set up your first Frigade Flow. Our docs cover additional functionality like [analytics](/platform/analytics), [no-code deployments](/platform/collections), and [environments](/platform/environments).

    If you have questions or want to discuss your particular project, feel free to reach out to us at [support@frigade.com](mailto:support@frigade.com) or [book a demo](https://cal.com/team/frigade/frigade-demo).
  </Step>
</Steps>
