# Source: https://docs.asapp.com/changelog/messaging-customer-channels.md

# ASAPP Messaging Updates - Customer Channels

> New updates and improvements for ASAPP Messaging - Customer Channels

<Update label="2024 - Form Messages for Apple Messages for Business">
  ASAPP enables Form Messages, a native Apple Messages for Business (AMB) format that replaces Omniforms (link to a web form) with a rich, multi-page interactive experience. You can gather customer information through customizable forms that present a single field per page and let your customers review their entries before submitting—all without leaving the Apple Messages application.

  This enables you to deliver a more seamless and aesthetically pleasing experience for your customers, consistent with other Apple applications.

  <Frame>
    <img style={{height: '500px'}} src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-370fec39-987b-612a-7820-2e213b049e32.gif?s=a2860e03c315c73c4c86c3941b62dc2b" alt="Entering and reviewing fields from a Form Message in Apple Messages for Business." data-og-width="886" width="886" data-og-height="1920" height="1920" data-path="image/uuid-370fec39-987b-612a-7820-2e213b049e32.gif" data-optimize="true" data-opv="3" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    Watch the video walkthrough below to learn more about Form Messages:

    <iframe width="560" height="315" src="https://fast.wistia.net/embed/iframe/d6la1ez6j4" />

    ### Supported Forms

    When a form is sent to a customer in Apple Messages for Business, supported forms will display as a Form Message, which has a single form field on each page and allows the customer to review their form entries before submitting.

    Examples of supported form field types include:

    * Text
    * Name
    * Location
    * Date
    * Phone Number
    * Numbers
    * Selectors

    ### Unsupported Forms

    Customers will be sent an Omniform rather than an AMB Form Message if one of the following is true:

    * The customer is not on an iOS version that supports Form Messages
    * It is a Secure Form
    * The flow node is configured to have the form disappear when a new message is sent
    * There are more than seven fields in the form; this limit exists because there is a known AMB Form Messages issue that requires a customer to start over if they background the Messages app while filling out a form and then return back to it
    * Any field has a prefilled value
    * Any field has password masking
    * If the form has more than one submit button
    * The form contains a scale, paragraph, or table field

    Contact your ASAPP account team to enable Form Messages and to determine which forms customers will receive as Form Messages.

    <Note>
      Form Messages for multilingual forms are not yet supported. If using a Spanish Virtual Agent, Form Messages are not available.
    </Note>

    ## FAQs

    1. **Why did I have to start filling out my form from the start after leaving and coming back to it?**

    There is a known AMB Form Messages issue that requires a customer to start over if they background the Messages app while filling out a form and then return back to it.

    2. **Can I enable/disable an individual form to be a Form Message?**

    No, it is a company-level configuration. If enabled, all supported forms will be sent as AMB Form Messages.
  </Accordion>
</Update>

<Update label="2024 - WhatsApp Business">
  ASAPP supports [WhatsApp Business as a messaging channel](/messaging-platform/integrations/whatsapp-business), enabling your customers to interact with virtual agents and have conversations with live agents in their preferred messaging app.

  This expanded channel support gives you the ability to offer robust messaging experiences to your WhatsApp users, encouraging them to choose messaging more often and have more satisfying interactions in a familiar setting.

  <Frame>
    <img width="300px" src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4a569533ca4cb0a7f022ed036687ec8b" data-og-width="385" data-og-height="759" data-path="image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=595c6ca94a48b487229ff336863a1f0b 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e71dd0d2b480dc694bcfe7cfc1366d88 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4a70a149a1953e4b5212c66a34288e0b 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0cc83e6e2c299209785191ce4d29cd62 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=80723503c7fa094a084cdb0a700723f7 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bc3cef3-6ec9-36d9-f818-4e40140fe37d.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0de4de640127a6043068fe6d24bb4042 2500w" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    ASAPP's integration with WhatsApp Business supports similar functionality to what is available in other customer channels. At an overview level, see below for supported and unsupported features:

    **Support included:**

    * Automated flows
    * Deeplinked entry points
    * Free-text disambiguation
    * Estimated wait time
    * Live chat with agents
    * Push notifications
    * Secure forms
    * End-of-chat feedback forms

    **Not currently supported:**

    * Customer authentication
    * Customer history
    * Chat Instead entry point
    * Customer attributes for routing
    * Customer typing preview for agents, typing indicator for customers
    * Images sent by customers
    * Carousels, attachment, images in automated flows
    * New question/welcome back prompts
    * Proactive messaging
    * Co-browsing

    <Note>
      \[Integration documentation is published here]\(./messaging-plat. Reach out to your ASAPP account contact to get started with WhatsApp Business. They can also advise on specific expected behaviors for virtual agent and live chat features in WhatsApp Business as needed.
    </Note>

    ## FAQs

    1. **What are the basic setup steps for WhatsApp Business?**

    Enterprises start by [creating a general Business Manager (BM) account with Meta](https://www.facebook.com/business/help/1710077379203657?id=180505742745347) and verify their business.

    While this happens, ASAPP deploys backend services in support of the integration. After creating a BM account, completing business verification, and registering phone numbers, you can then create an official WhatsApp Business Account via the embedded signup flow in AI-Console.

    After setup, your ASAPP account team will work with you on modifying automated flows for use in WhatsApp and coordinate lower environment testing once changes are complete. The final step is to create entry point URL links and QR codes in the WhatsApp Business dashboard, and insert entry points as needed in your customer-facing web and social properties.

    2. **How will my current automated flows be displayed in WhatsApp Business?**

    The WhatsApp customer experience is distinct from ASAPP SDKs in several ways - some elements are displayed differently while others are not supported.

    Elements that are displayed differently use message text with links - this includes buttons for quick replies and external links. Similarly, both (a) forms sent by agents and (b) feedback forms at the end of chat also send messages with links to a separate page to complete the survey, after which time users are redirected back to WhatsApp.

    Quick replies in WhatsApp also have different limitations from ASAPP SDKs, supporting a maximum of three quick replies per node and 20 characters per quick reply. Your ASAPP account team will work with you to implement intent routing and flows to account for nodes with unsupported elements, such as authentication and attachments.

    3. **Will agents know they are chatting with a customer using WhatsApp?**

    Yes. Agents will see the WhatsApp icon in the left-hand panel of Agent Desk.

    4. **Where can I learn more about WhatsApp Business?**

    Visit [business.whatsapp.com](https://business.whatsapp.com/) for official reference material about this customer channel.
  </Accordion>
</Update>

<Update label="2024 - Authentication in Apple Messages for Business">
  ## Authentication in Apple Messages for Business Feature Release

  ASAPP now supports customer authentication in Apple Messages for Business. With this new functionality, customers can securely log in to their accounts during interactions, allowing them to access personalized experiences in automated flows and when speaking with agents.

  Customer authentication is intended for any interaction where making use of account information creates a better experience for the customer:

  * **Any live interaction with an agent:** Enable your agents to greet and validate who they're speaking with, review historical customer conversations, and quickly reference relevant account attributes.
  * **Automated flows:** Present data related to a customer's account (e.g., booking details) or take actions on behalf of the customer (e.g., make a payment).

  Identifying a customer in an interaction also adds valuable context when reviewing historical interactions in Insights Manager for reporting or compliance purposes.

  Expanding support for customer authentication in this channel should:

  1. Reduce the share of interactions that are directed to agents due to customers being unable to access automated flows that require authentication.
  2. Reduce the share of interactions that are directed to agents due to customers being unable to access automated flows that require authentication
  3. Expand the share of interactions with agents that benefit from account information and conversation history, reducing effort to identify customers and search for account information

  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | <Frame>  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=72f6032574e587037c7cad81c10dfba4" data-og-width="874" width="874" data-og-height="1736" height="1736" data-path="image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=b4c06b18746fe8560b4640386fcdf6ac 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=2148af7989e2e6fc39fdcda9aa316277 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=736e6edab15aa707b67d18115b58af37 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=af6c7b58a16e8fe3ba3b8551073fac36 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=9f87ec99a6a899033fc8907c60d56cb4 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-ff53644d-bae2-df1f-d681-7471f00e0c31.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e7c2aea6401e622894ce7faeaa2c03b6 2500w" /></Frame> | <Frame>  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=4aef316b2e55c3f3efca759c9789ede0" data-og-width="874" width="874" data-og-height="1736" height="1736" data-path="image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0b775249272f95cd9a1cda91c628535c 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=31dfda7247301403ebc791aa309a1ea9 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e0bf2e08611c34acdbe847aeba35bd62 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a248d7e4d05fa55a1120260537836882 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e877003dec964a7f921d889485368c72 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/image/uuid-f78a2f4b-1b19-9ee4-14c6-f68abfb4109e.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=ead61f711a3d9bd1c424105e0c015acb 2500w" /></Frame> |

  <Accordion title="How It Works">
    ## How It Works

    **User Experience**

    Once implemented, any instance in an ASAPP automated flow that triggers customer authentication today will do so during an interaction in Apple Messages for Business.

    When this occurs, Apple Messages for Business will ask the user to login via a button. Once the user clicks the button, they will be brought out of the iMessages app and redirected to a webpage/browser window to sign in. Users will have to sign-in with their credentials every time their authentication token expires.

    **Architecture**

    User Authentication in Apple Messages for Business utilizes a standards-based approach using an OAuth 2.0 flow with additional key validation and OAuth token encryption steps.

    This approach requires companies to implement and host a login page to which Apple Messages for Business will direct the user for authentication.

    Visit [Apple Messages for Business integration guide](/messaging-platform/integrations/apple-messages-for-business#customer-authentication) for more information.

    <Note>
      Reach out to your ASAPP account team to coordinate on the implementation of customer authentication in Apple Messages for Business.
    </Note>

    ## FAQs

    1. **What are the steps required to implement authentication?**

       This primarily depends on if a suitable login page and token endpoint already exists or requires customer development. Your ASAPP account team can provide exact details on the specifications these must meet.

       Configuration is required by ASAPP and on the Apple Business Register. Chat flows that use APIs may require modification to match the rendering capabilities of Apple Messages for Business but this can be done incrementally.

       Testing of the feature can be done in a lower environment prior to production launch. ASAPP implementation time is 6-12 weeks depending on flow complexity, and total customer integration time is dependent on customer dependencies.
    2. **If our user base has a broad range of device versions and iOS versions, will they all have the same authentication experience? If not, what needs to be done to ensure that they do?**

       Yes. For iOS versions 15 & 16+, the user experience for authentication will be the same. However, users with devices that run iOS versions earlier than 12 will not be able to access authentication.

       From a technical perspective, different token endpoints will need to be supported simultaneously to allow users across iOS versions 15 and 16+ to access authentication. More specifically, distinct endpoints will be needed to support users with iOS versions 15 or 16+, as well as devices running these iOS versions to test.

       <Note>
         For iOS versions 16+, ASAPP will soon support Apple's newest authentication architecture, which we strongly encourage implementing once it becomes available.
       </Note>
    3. **Does authentication happen inline within the chat experience?**

       No. In the current virtual agent experience, a user will see a login button and then be redirected to a webpage to enter their credentials and complete the login action. They will then be automatically redirected to the chat experience within 10 seconds of successfully authenticating.
    4. **How many attempts will a user be given to authenticate? Are there configurable limits to this?**

       This is governed by how many retries the customer login page allows.
    5. **When is conversation history carried across channels, both from the customer and agent's perspectives?**

       * If a customer is authenticated in the Apple Messages for Business channel, they will see their conversation history for previous authenticated Apple sessions but not their history from other channels.
       * If during an authenticated Apple session, the customer moves to another channel (e.g. Web SDK) and authenticates, the Apple conversation from that session will appear in the new channel. Additionally, as the customer engages via the Web SDK, agent responses will continue to appear in Apple Messages for Business until the token for the Apple session has expired.
       * In all other instances, the conversation history from Apple Messages for Business will not be visible to customers when they start subsequent conversations in other channels.
       * From the agent's perspective, conversation history from all channels is visible in Agent Desk so long as customers have signed in using the same credentials.
  </Accordion>
</Update>

<Update label="2024 - Quick Replies in Apple Messages for Business">
  ## Quick Replies in Apple Messages for Business Feature Release

  ASAPP's automated flows support quick replies for customers that use the Apple Messages for Business channel. Quick replies display response options directly in the messaging interface, allowing customers to make an inline choice with a single tap during an ongoing conversation.

  As in ASAPP's customer channels for web and mobile apps, quick replies are used to give customers a defined set of response options, each of which leads to a corresponding branch in an automated flow. Key use cases for quick replies in automated flows include the following:

  1. Discovery questions to better specify a customer issue or account detail
  2. Ensuring the customer's issue has been addressed by an automated flow

  Using quick replies in Apple Messages for Business is expected to reduce friction that can cause customer drop-off and frustration before fully completing a flow or reaching an agent to better assist with an issue.

  <Frame>
    <img width="300px" src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7c421cb53823052846958359d744a604" data-og-width="874" data-og-height="1736" data-path="image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=665d37a70cc0d4fc7b471f1a267fe615 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7dfe4eabf86fc489d011d99934028b78 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8973bf87a6e31f95f71aae9b985ff5f8 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=89d8dda7279106e9bf27288c6ea444f3 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=8a3839b3f89cb21242750e80b0de2cc2 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-c7100047-15f3-1551-bde7-49e5e9e8c3ba.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=d97f997f5fe9340f27c4b7479b39dca9 2500w" />
  </Frame>

  <Accordion title="How It Works">
    ## How It Works

    Quick reply support in Apple Messages for Business is expected to function similarly to quick replies in ASAPP SDKs for web and mobile apps, with the following differences:

    **Number of Quick Replies**\
    Apple Messages for Business supports a minimum of two quick replies and a maximum of five per node.

    **Push Notification and Selection Confirmation**\
    When quick reply options are sent, users receive a push notification if Messages is not open; the title of the message will be 'Choose an option'. Once the user selects a response option, Apple displays a checkmark beside text 'Choose an option' in the Messages UI. This is a default behavior and is not configurable.

    **Length of Quick Replies**\
    All quick replies will render as a single line of text with a maximum of 24 characters; if the text exceeds 24 characters, it will be truncated with ellipses after the first 21 characters.

    **OS Version Support**\
    Quick replies are supported in iOS 15.1 and macOS 12.0 or higher; prior operating systems will use the list picker interface.

    ## FAQs

    1. **Is there any work required to adapt existing automated flows to support quick replies in Apple Messages for Business?**\
       Once your ASAPP account team completes a small configuration change, all flows configured with quick replies today will automatically use them in Apple Messages for Business for supported iOS and macOS versions.

    <Note>
      Flows with nodes that have more than five quick reply options will need to be edited to use five or fewer quick replies - any quick replies in excess of the first five will not be visible in this channel. Flows with quick reply text that exceeds 24 characters will need to be shortened or will be shown with ellipses after the first 21 characters in this channel.
    </Note>

    2. **Can the list picker experience be selected in AI-Console for designated automated flows or are quick replies the only option?**\
       Currently, if quick replies are enabled, they will be the only supported option across automated flows. The list picker experience will be used for older versions of iOS and macOS.

    Visit the [Apple Messages for Business](/messaging-platform/integrations/apple-messages-for-business) integration guide for more information about this channel.
  </Accordion>
</Update>
