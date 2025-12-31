# Unifygtm Documentation

Source: https://docs.unifygtm.com/llms-full.txt

---

# Best Practices: Optimizing Your Email Outreach
Source: https://docs.unifygtm.com/best-practices/deliverability



## Sequence Copy

1. **Keep an individual sequence to 4 email touches max -** Within a four-touch sequence, we recommend alternating the structure between 2 new threads and 2 follow-up replies. The copy of these follow-up replies can be short and limited to 1-2 sentences. Example: "Any thoughts on my previous note?"

2. **Alternate case studies and value props between new threads -** You should vary the copy and angle you're approaching to pitch your product in email steps 1 and 3. For example, you can highlight different customer case studies or statistics across both emails.

3. **Shorten subject line and use personalization -** Keep subject titles concise and add custom variables to increase variability. This approach will also help improve deliverability. Example: "Unify x (Your Company Name)"

4. **Include statistics and case studies for social proof -** Incorporating very numbers-driven, concise impact statements can catch your prospect's attention. We recommend adding concise blurbs from customer case studies into your sequence copy.

5. **Add personalization with snippets -** You can use Unify's smart snippets to personalize copy based on relevant value prop, job title, work description, industry, and more. This will make your sequence copy more compelling with targeted pain points, use cases, or case studies. More variance in email copy will also help with deliverability.

6. **Keep it concise, focus on a single product or pain point -** Don't try to fit too many points into your email - you want to be decisive and mention the most relevant product or pain point to that individual to capture their attention! Keep the language simple and avoid business jargon. We generally recommend keeping each email between 50-200 words.

7. **End with a compelling call to action (CTA) -** Conclude each email with a clear, specific, and actionable request. This could include scheduling a call, booking a demo, or asking the prospect to reply with a specific piece of information relevant to their needs.

## Deliverability

1. **Limit the links -** Try not to overload your emails with multiple or duplicate links. Too many links can set off spam alarms - we generally recommend limiting the email touch to include 1-2 links maximum.

2. **Check link safety -** Ensure the links you include are secure and no warnings are displayed by the browser when visiting them.

3. **Mix up subject lines -** Don't stick with the same old subject lines, use template variables to keep them dynamic and interesting.

4. **No all caps -** Using all caps anywhere in your email can make it look spammy, so stick to normal capitalization.

5. **Easy on the exclamation -** Too many exclamation points can trigger spam filters, especially in the subject line. Use them sparingly!

6. **Send from multiple email addresses -** Sending emails from multiple mailboxes improves deliverability by distributing volume across different IP addresses and domains. This approach reduces the risk of being flagged as spam and increases overall sending capacity.

7. **Proofread for Typos**: Typos can make your email look unprofessional, especially when you're emailing multiple contacts at a company. Make sure to proofread and catch any errors.


# Best Practices
Source: https://docs.unifygtm.com/best-practices/introduction

Unify's recommendations for high-performance GTM.

export const SequencesIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M10 14l11 -11"></path>
    <path d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5"></path>
  </svg>;

export const PlaysIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"></path>
    <path d="M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"></path>
    <path d="M11 19h5.5a3.5 3.5 0 0 0 0 -7h-8a3.5 3.5 0 0 1 0 -7h4.5"></path>
  </svg>;

<CardGroup cols={2}>
  <Card title="Book Meetings with Plays" icon={<PlaysIcon />} href="/best-practices/plays">
    Learn how to use Plays effectively to automate your outbound.
  </Card>

  <Card title="Optimizing Outreach" icon={<SequencesIcon />} href="/best-practices/deliverability">
    Design your Sequences to maximize response rates and deliverability.
  </Card>
</CardGroup>


# Best Practices: Plays to Book You Meetings
Source: https://docs.unifygtm.com/best-practices/plays



## Section 1: Best Practices

Unify is a sales engagement platform designed to help you generate pipeline. To ensure that you see the best results, we recommend a few general principles:

* **Act Quickly:** Act on intent signals within 24-48 hours to catch prospects before they make their decision. Intent gets stale quickly.
* **Engage with Every Lead:** Once you define your ICP in Unify, avoid selective outreach. Avoid introducing bias into how you prospect.
* **Multiple Touchpoints:** If you’ve found that a channel works best for your team, use Unify to lean into that. Unify excels at email - if that’s your preferred channel, great. If not, use email in addition to LinkedIn or phone outreach. See section 4 below to see our recommendations for email and LinkedIn outreach.

## Section 2: Actioning on Intent

There are two primary ways to act on intent data in Unify:

### Automatic Plays

* **When to use:** Both for low and high volume signals. Plays automate prospecting, qualifying, sequencing, and syncing leads to your CRM.
* **Benefits:** Reduce friction and improve intent to meeting booked conversion by immediately actioning on leads.
* Learn more about how to build Plays in [How to Create a Play](/tutorials/how-to-create-a-play).

### Manual Alerts

* **When to use:** Ideal for low volume, high value signals. It's important to ensure the sales team is accountable for acting on alerts to ensure hot leads don’t slip through the cracks.
* **Benefits:** Immediate and contextual information delivered to where your team is working.
* Most reps use Slack alerts to trigger manual workflows. Learn how to set these up in our [Slack Integration Guide](/reference/integrations/slack#slack-integration-guide)

## Section 3: Intent-Based Plays

Intent signals are indicators that there’s an opportunity to sell your product or book an intro meeting. Our customers have seen success with these intent-based Plays:

1. **Pricing Page Visits:** Checking out pricing pages indicates that prospects are seriously considering a purchase decision.
2. **[Repeat Buyers](https://www.unifygtm.com/plays/champion-tracking---outbound-to-past-customers-who-have-moved-jobs):** When someone you’ve sold to before is back on the website demonstrating high intent. This works well for businesses that have more transactional sales.
3. **[Inbound Form Submissions](https://www.unifygtm.com/plays/outbound-to-website-form-submitters):** A form submission is one of the strongest signs of intent. Convert those leads immediately by automating outreach as soon as they submit.
4. **[New Hires](https://www.unifygtm.com/plays/outbound-to-people-who-have-started-jobs-at-a-new-company):** People are more likely to purchase new tools in their first few months on a job. Targeting your ICPs that have just changed jobs can convert better.
5. **[Support Docs](https://www.unifygtm.com/plays/outbound-to-contacts-viewing-your-technical-docs):** Interest in support docs (e.g., integration details), suggests prospects are trying to understand how your product works and if it would work for them.
6. **[Social Content Engagement](https://www.unifygtm.com/plays/automate-outbound-to-linkedin-likers-commenters)**: Liking or commenting on your social posts signals that a prospect is interested in your company.
7. **[Product Tour Visits](https://www.unifygtm.com/plays/outbound-to-people-who-view-your-product-demo):** Interest in demo videos or product tours indicates a desire to understand specific product offerings in more granularity.
8. **[Retarget Paid Traffic](https://www.unifygtm.com/plays/retarget-paid-traffic):** Get more out of your spend on paid traffic by retargeting people based on UTM filters.
9. **[Closed-Lost Opportunities](https://www.unifygtm.com/plays/retarget-closed-lost-opportunities-when-they-revisit-website):** A revisit to your site by a closed-lost opportunities signals the prospect might be interested in re-engaging.

## Section 4: Section 4: Nailing Email or Linkedin Outreach

Nailing email and LinkedIn messages is key to booking the most possible meetings from Unify. A few guiding principles:

1. **Use Soft Messaging:** Use your judgement, but we typically recommend against direct mentions of website activity. Instead, tailor messages to address the pain points related to the product or service they showed interest in.
2. **Keep It Short:** Many senior leaders at your target accounts read emails on their phones, concise messages under 100 words are more likely to be read and understood. Remember that people are skimming emails.
3. **Persona-Specific Messaging:** Address specific pain points and perspectives of the different personas you sell to (e.g., sales and marketing for us). Avoid generic messages that try to cater to multiple personas, as they may resonate with none.
4. **Focus on One Product:** If you sell multiple products, pitch one per email. This approach minimizes the chances that your prospect gets confused about what you solve.
5. **Highlight Relevant Pain Points:** Rather than pitching your product, focus on speaking to a specific challenge or pain point that your prospect has. Educate the prospect on your product once you’re on the phone with them.


# Best Practices: Writing AI Prompts
Source: https://docs.unifygtm.com/best-practices/prompting



## Section 1: General Tips

Unify has multiple AI features that can be used to improve qualification and outreach outcomes. To set yourself up for success, we recommend a few general principles for prompting when using these features:

* **Clear Instructions:** Be explicit about what you want the AI to do. Providing a clear set of instructions will help the AI understand what you want to accomplish and what steps to follow to complete the task(s).
* **Length =/= Quality:** Writing an overly detailed or essay length prompt does not mean that the AI will provide a better response. Excessive information can be detrimental unless it is properly structured and explained, as it can lead to confusion and misinterpretation of the prompt.
* **Provide Context:** Assume AI does not know your industry, company, or product as well as you do. Provide relevant context as you reference information about your company or your goals. For example, if you are referencing a niche keyword, provide a brief explanation of what it means, how it relates to your business, and the task you are giving the AI.

## Section 2: AI Agents

There are two primary ways that you can provide information and instruction to Unify's AI Agents.

### Questions

* **Questions:** Questions are the minimum required input to run an AI Agent. You can ask any question about a Company or Person and select the type of response you want the Agent to provide (e.g., True/False, Text, Multi-Select, Number).
* **What information to provide:** In the question, only include the research question you want the Agent to answer. Avoid adding clarifying information or instructions to keep it focused.

### Guidance

* **When to use:** Guidance is an optional field for AI Agents that enables you to provide additional context or instructions to the AI Agent. When asking more complex questions, when you have a set of instructions or requirements that you want the AI Agent to follow, or when you want to provide clarification on the research question, guidance is the best way to provide that information.
* **How To Structure Guidance:** Similar to Prompts, Guidance should be clear, concise, and specific. Use the guidance to provide specific directions about each question that you are asking, and additional context if there is a specific way that you want the AI Agent to conduct its research. For example, if you want the AI Agent to only use information from a specific source, you can include that information in the guidance. Or, if you want to provide more direction on when the AI Agent should select a specific answer for a multi select response type, that information should also be included in the guidance.

## Section 3: Smart Snippets

Smart Snippets are a powerful way to personalize messaging to your prospects.

* **Provide Context (Again!):** The model can only act on what you provide. This means you should specify the information you want to create copy from, select template variables to reference, or add Agent template variables to the Smart Snippet. Additionally, provide context around the template variable to create a coherent prompt. Think of template variables as placeholders for information and write sentences or blurbs surrounding those variables.
* **Adding References:** A common mistake is referencing information that you haven't provided to the model, which can lead to incorrect responses. To prevent this, ensure that if you're referencing data provided through a template variable or Agent output, you include that template variable in the Snippet.

### Agent Outputs in Smart Snippets

Using Agents to conduct research and then incorporating that research into a Smart Snippet is a great way to hyper-personalize your messaging. To use this feature effectively:

* **Separation of Concerns:** Use the Agent to conduct research only, and use the Snippet to generate the copy. Each feature is optimized for its respective task.
* **Structure the Snippet prompt around the Agent variables:** When writing a Smart Snippet prompt with Agent output template variables, provide context and labels about what each Agent output contains so the Snippet can handle it accordingly. For example, if you have an Agent Question that asks for a True/False or Number answer, write your prompt using the Agent template variable as a placeholder in your sentences to provide context to the Snippet.
  * For example, if your Agent question was "What is the most recent product launch from this company?", your Snippet prompt should be something like: "Research indicates that this company just launched `{{Agent Question}}`. Write a sentence to congratulate them on the launch."

## Section 4: AI Research

AI Research is a powerful way to automate and customize research that you want to conduct about any company that you are engaging. AI Research is powered by Unify's Observation Model, which is the system that Unify uses to run completely customized research for your company on your prospects.

### Prompting AI Research

Writing prompts for AI Research is slightly different from writing prompts for AI Agents, as AI Research is designed to read as much relevant information as possible before generating a report for you. We recommend following the style of the Observation prompts we generated for you as a starting point. To prompt for AI Research, follow these guidelines:

* **Pick a General Signal:** The goal with an Observation prompt is to describe a specific piece of information to the system that you'd like to monitor for any given company. For example, if you know that a company using a specific technology has a high likelihood of becoming your customer, an Observation for that could be: "Company uses an outbound sequencer (Outreach, Salesloft, Apollo, etc.) and a data/intent source (ZoomInfo, 6sense, Bombora, Clearbit, Demandbase, G2 Intent)."

* **Test and Iterate:** Once you've written your prompt, take advantage of the settings page to generate examples and see what the resulting reports look like.


# Intent Client Usage
Source: https://docs.unifygtm.com/developers/intent-client/client-spec

Learn how to send events using the Unify Intent Client.

<Tip>
  The Unify Intent Client can be used to log user activity across multiple subdomains of the
  same top-level domain. For example, if a user visits your marketing website at `www.yoursite.com`
  and then logs into your production web application at `app.yoursite.com`, the activity in both
  places will be attributed to the same person.
</Tip>

## Page View Events

Website page views are an indicator of buyer intent. You can log this information to the Unify platform
for usage with the `page` method.

There are two ways to collect page data with the Unify intent client:

1. Automatic monitoring of the current page
2. Manually via the client `page` method

Utilizing both of these methods when appropriate is recommended to take full advantage of intent data
within Unify.

### Automatic Page Monitoring

The Unify intent client is capable of automatically monitoring the user's current page to trigger
page events. This will happen by default when the client is installed via the [Unify Website tag](./website-tag).
If the client is installed via a package manager, you must pass the `autoPage` configuration option
when instantiating the client. See [Configuration](#configuration) below for more details.

<Check>Automatic page monitoring works in Single Page Apps, too!</Check>

In either case, this behavior can be enabled or disabled programmatically via the `startAutoPage`
and `stopAutoPage` methods on the client:

```ts  theme={null}
// Initialize the client and tell it to automatically monitor pages
const unify = new UnifyIntentClient(
  'YOUR_PUBLIC_WRITE_KEY',
  { autoPage: true },
);
unify.mount();

// Tell the client to stop monitoring pages
unify.stopAutoPage();

// Tell the client to start monitoring pages again
unify.startAutoPage();
```

### Manual Page Logging

You can also manually trigger a page event with the `page` method on the client. This is useful
when you do not want to trigger page events for every page.

```ts  theme={null}
const unify = new UnifyIntentClient('YOUR_PUBLIC_WRITE_KEY');
unify.mount();

// Trigger a page event for whatever page the user is currently on
unify.page();

// Trigger a page event for a custom page other than the current page
unify.page({ pathname: '/some-custom-page' });
```

## Identify Events

All intent data collected for users by Unify is anonymous by default. When intent events are
logged, Unify will attempt to automatically de-anonymize the IP address of a user to associate
them with a specific company, but their personal identity will remain anonymous until an
identify event is triggered for them.

There are two ways to collect identity data with the Unify intent client:

1. Automatic monitoring of email input elements
2. Manually via the client `identify` method

Utilizing both of these methods when appropriate is recommended to take full advantage of intent
data within Unify.

### Automatic Input Monitoring

The Unify intent client is capable of automatically monitoring text and email input elements on
the page to collect user identity. This will happen by default when the client is installed via
the Unify JavaScript tag. If the client is installed via a package manager, you must pass the
`autoIdentify` configuration option when instantiating the client. See [Configuration](#configuration)
below for more details.

In either case, this behavior can be enabled or disabled programmatically via the `startAutoIdentify`
and `stopAutoIdentify` methods on the client:

```ts  theme={null}
// Initialize the client and tell it to automatically monitor inputs
const unify = new UnifyIntentClient(
  'YOUR_PUBLIC_WRITE_KEY',
  { autoIdentify: true },
);
unify.mount();

// Tell the client to stop monitoring inputs for now
unify.stopAutoIdentify();

// Tell the client to start monitoring inputs again
unify.startAutoIdentify();
```

### Manual Identification

You can also manually trigger an identify event with the identify method on the client. This is
useful when users log-in with OAuth or SSO, for example, because they do not enter their email
into an input on the page.

```ts  theme={null}
const unify = new UnifyIntentClient('YOUR_PUBLIC_WRITE_KEY');
unify.mount();

// However you determine the currently logged-in user
const currentUser = getCurrentUser();

// Identify the current user
unify.identify(currentUser.emailAddress);
```

## Configuration

The following configuration options can be passed when initializing the client:

<ParamField body="autoPage" type="boolean" default={false}>
  <Note>If installed via the [Unify Website tag](./website-tag) then the `autoPage` config will default to `true`.</Note>

  Tells the client to automatically log page events whenever the current page changes.
  Works for static websites and Single Page Apps. Also logs a page event for the initial page.
</ParamField>

<ParamField body="autoIdentify" type="boolean" default={false}>
  <Note>If installed via the [Unify Website tag](./website-tag) then the `autoIdentify` config will default to `true`.</Note>

  Tells the client to automatically monitor text and email input elements on the
  page for changes. When the current user enters a valid email address into an input, the client
  will log an identify event for that email address.
</ParamField>


# JavaScript Client
Source: https://docs.unifygtm.com/developers/intent-client/js-client

Install the Unify Intent client in a frontend web application framework.

<CardGroup cols={2}>
  <Card title="Github" icon="github" iconType="solid" href="https://github.com/unifygtm/intent-js-client" />

  <Card title="npm" icon="npm" iconType="solid" color="#BD0005" href="https://www.npmjs.com/package/@unifygtm/intent-client" />
</CardGroup>

## Installation

You can install the Unify Intent JS Client with your preferred package manager:

<CodeGroup>
  ```shell npm theme={null}
  npm install @unifygtm/intent-client
  ```

  ```shell yarn theme={null}
  yarn add @unifygtm/intent-client
  ```

  ```shell pnpm theme={null}
  pnpm add @unifygtm/intent-client
  ```
</CodeGroup>

## Usage

After installing the client, you must initialize it in your application code:

<Warning>You should only initialize the client one time in your application.</Warning>

```ts index.ts theme={null}
import { UnifyIntentClient, UnifyIntentClientConfig } from '@unifygtm/intent-client';

const writeKey = 'YOUR_PUBLIC_API_KEY';

const config: UnifyIntentClientConfig = {
  autoPage: true,
  autoIdentify: false,
};

const unify = new UnifyIntentClient(writeKey, config);

// Do not call mount during server side rendering. Only call it in a browser context.
unify.mount();
```

You can then use the resulting client instance to log intent data. See the
[Client Spec](./client-spec) for more details on how to use the client.

## Cleanup

When you are done using the client, if you wish to clean up the side effects
generated by it, you can do so with the `unmount` method:

```ts cleanup.ts theme={null}
import { UnifyIntentClient, UnifyIntentClientConfig } from '@unifygtm/intent-client';

const writeKey = 'YOUR_PUBLIC_API_KEY';

const unify = new UnifyIntentClient(writeKey);
unify.mount();

// Use the client for some time, then later...

unify.unmount();
```


# Intent Client Overview
Source: https://docs.unifygtm.com/developers/intent-client/overview

Learn how to start collecting website intent data in Unify.

Buyer intent data is at the core of what makes Unify tick. The easiest way to
start collecting this data is by installing the Unify Intent client on your
marketing website or web app.

# How it works

The Unify Intent client is a JavaScript library that allows you to collect
events from your website and send them to Unify. It currently supports Page and
Identify events. Track events are coming soon.

<CardGroup cols={3}>
  <Card title="Page Events" icon="memo-pad" iconType="duotone" color="#3378B8">
    e.g. a user visits the pricing page of your marketing website
  </Card>

  <Card title="Identify Events" icon="user-check" iconType="duotone" color="#22811A">
    e.g. a user logs into your web application with their email address
  </Card>

  <Card title="Track Events (coming soon)" icon="bullseye-pointer" iconType="duotone" color="#D23434">
    e.g. a user clicks a button to open a pricing calculator modal
  </Card>
</CardGroup>

When you install the Unify Intent client on your website, it can automatically
start collecting these events and sending them to Unify. You can also customize
this behavior by sending events manually using the client's API.

The Unify Intent client is fully open source and available on [GitHub](https://github.com/unifygtm/intent-js-client).

# Installation

There are several different ways to install the Unify Intent client on your
website. Choose the one that best suits your use case:

<CardGroup cols={1}>
  <Card title="Website Tag" icon="code" iconType="duotone" href="/developers/intent-client/website-tag" horizontal>
    Quickly set up the Unify Intent client on a static marketing website.
  </Card>

  <Card title="React Library" icon="react" iconType="solid" color="#4AB8D4" href="/developers/intent-client/react" horizontal>
    Install the Unify Intent client in a React app.
  </Card>

  <Card title="JavaScript Client" icon="square-js" iconType="solid" color="#E2CD3E" href="/developers/intent-client/js-client" horizontal>
    Install the Unify Intent client in a different frontend web application
    framework.
  </Card>
</CardGroup>

If you aren't sure, we recommend starting with the **Website Tag** installation
method. This is the simplest way to get started and all you need for most
marketing websites.

# Usage

If you install the client using the **React Library** or **JavaScript Client**
methods, see our [Usage Guide](/developers/intent-client/client-spec) to learn
how to use the client and start adding events.


# React
Source: https://docs.unifygtm.com/developers/intent-client/react

Install the Unify Intent client in a React app.

<CardGroup cols={2}>
  <Card title="Github" icon="github" iconType="solid" href="https://github.com/unifygtm/intent-react" />

  <Card title="npm" icon="npm" iconType="solid" color="#BD0005" href="https://www.npmjs.com/package/@unifygtm/intent-react" />
</CardGroup>

## Installation

You can install the Unify Intent React library with your preferred package manager:

<CodeGroup>
  ```shell npm theme={null}
  npm install @unifygtm/intent-react
  ```

  ```shell yarn theme={null}
  yarn add @unifygtm/intent-react
  ```

  ```shell pnpm theme={null}
  pnpm add @unifygtm/intent-react
  ```
</CodeGroup>

## Usage

First, wrap your React app in a `UnifyIntentProvider`:

```tsx index.tsx theme={null}
import {
  UnifyIntentClient,
  UnifyIntentClientConfig,
  UnifyIntentProvider,
} from '@unifygtm/intent-react';

const writeKey = 'YOUR_PUBLIC_API_KEY';

const config: UnifyIntentClientConfig = {
  autoPage: true,
  autoIdentify: false,
};

const intentClient = new UnifyIntentClient(writeKey, config);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement,
);

root.render(
  <UnifyIntentProvider intentClient={intentClient}>
    <App />
  </UnifyIntentProvider>
);
```

The `UnifyIntentProvider` automatically takes care of mounting and unmounting the client
for you whenever the component mounts and unmounts. So any components rendered in your app
can freely access and use the intent client using the `useUnifyIntent` hook:

```tsx Example.tsx theme={null}
import { useUnifyIntent } from '@unifygtm/intent-react';

const Example = () => {
  // Get the Unify Intent Client
  const unify = useUnifyIntent();

  // However you access the current user...
  const currentUser = useCurrentUser();

  useEffect(() => {
    if (currentUser?.emailAddress) {
      // Log an identify event for the current user
      unify.identify(currentUser.emailAddress);
    }
  }, [currentUser, unify]);

  ...
};

export default Example;
```

You can then use the resulting client instance to log intent data. See the
[Usage](./client-spec) page for more details on how to use the client.


# Website Tag
Source: https://docs.unifygtm.com/developers/intent-client/website-tag

Quickly set up the Unify Intent client on a static marketing website.

# Installation

You can automatically load and install the client by placing a `<script>` tag in the `<head>`
or `<body>` of your website's HTML. The minified script can be found [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
in Unify.

```html index.html theme={null}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <!-- Your Unify JavaScript tag here -->
  </head>
  <body>
    <!-- Or here... -->
  </body>
</html>
```

Once added, there's nothing else you need to do to start collecting intent data.
The website tag will automatically start collecting both page views and user
identifications.

<Warning>
  Be sure to only initialize the client one time on your website.
</Warning>

If you'd like to manually trigger events in specific places on your website, you
can do so by calling the client directly. When you include the tag in your HTML,
you will immediately be able to access the client at `window.unify` (or simply
`unify` since `window` is global).

```js Console theme={null}
// Trigger a `page` event
window.unify.page();
unify.page();

// Trigger an `identify` event
window.unify.identify("user@email.com");
unify.identify("user@email.com");
```

## Additional instructions

If you're using one of the tools below, you can follow the provider-specific
instructions for that tool to install the website tag.

<AccordionGroup>
  <Accordion title="Google Tag Manager">
    The Unify Intent website tag can be added using Google Tag Manager. This can
    be useful in certain situations, such as if you have lots of scripts on your
    website and prefer to manage them all in one place.

    Start by opening the Google Tag Manager console. Add a new tag by selecting
    **Tags -> New**. Click on the **Tag Configuration** section and choose the
    **Custom HTML** tag type.

    Copy the website tag script from the Unify settings page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
    and paste it into the HTML field. Once it's added, click **Save**.

    <Frame>
      <img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=70b042e703a2fa60a96e4ab8ec8389c7" data-og-width="3456" width="3456" data-og-height="1818" height="1818" data-path="images/developers/intent-client/google-tag-manager-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=eeaef22dd75d0290b76f5e161add140c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=11a5630d0ff610dcb5fcd63dd408a888 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f134f061fbf6d9d70e633b0527db859e 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9e4238c61c0c94f853e5743cd2976021 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4dc9d6fc34d853bc86653669d5a3cef1 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/google-tag-manager-install.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b93d87253807815c6abd22f1e30ff0cc 2500w" />
    </Frame>

    Lastly, be sure to enable support for `document.write` in the tag settings.
    This is required for the website tag to work correctly.

    For more information, see the official Google Tag Manager support docs
    [here](https://support.google.com/tagmanager/answer/6107167).
  </Accordion>

  <Accordion title="Webflow">
    Webflow has a dedicated section for adding custom code to your website. From
    the Webflow dashboard, navigate to the settings for your website and then
    select the **Custom code** tab in the sidebar.

    Under **Head code**, paste the website tag script from the Unify settings
    page [here](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent-client)
    in the text area. Be sure to create a new line between any existing code and
    the Unify script.

    <Frame>
      <img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=52a753bc219787d46885e76a5f54b326" data-og-width="1858" width="1858" data-og-height="410" height="410" data-path="images/developers/intent-client/webflow-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5d153df10eca89128e98dae41ff107fe 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=05f704ddbba9207397c81d161c71c891 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b6b3735a1ba5b3f03e7420836a669ce 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=85e7c9f271aede29cf1fca684eeccf79 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3c8d2905d30c80a4b7b30dfa9fd85d4f 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/developers/intent-client/webflow-install.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=32f69b885ca1475ee8aa59e6d85b23eb 2500w" />
    </Frame>

    When you're done, click **Save** and then publish your changes by selecting
    **Publish -> Publish to selected domains** in the top right corner.
  </Accordion>
</AccordionGroup>

# Usage

Once the website tag is installed, the Unify Intent client will automatically
start collecting events on your website. Most of the time, there is nothing else
you need to do.

For details on how this works and the available options, see [Configuration](/developers/intent-client/client-spec#configuration).


# Onboarding Guide
Source: https://docs.unifygtm.com/getting-started/onboarding-guide

Complete a few key steps to fully activate on Unify.

export const UnifyLogoLight = () => <svg className="block dark:hidden" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1.00985 11.8422C1.00985 10.6279 1.00985 9.41364 1.00985 8.19937C1.00985 7.70467 1.03983 7.19498 1.17475 6.71526C1.39961 5.93574 1.84934 5.30611 2.52393 4.8414C3.39341 4.25675 4.30786 3.73206 5.26728 3.29733C6.45157 2.74266 7.62086 2.83261 8.74518 3.44724C10.2293 4.25675 11.6984 5.09624 13.1675 5.92074C14.1119 6.46042 15.0564 6.9851 16.0158 7.52478C16.6604 7.89955 17.2001 8.37926 17.5599 9.03886C17.8447 9.54856 17.9796 10.1032 18.0246 10.6879C18.0396 10.8977 18.0396 11.1226 18.0396 11.3325C18.0396 13.806 18.0396 16.2795 18.0396 18.768C18.0396 19.3077 17.9946 19.8473 17.7997 20.357C17.5149 21.1516 17.0052 21.7962 16.2706 22.2309C15.4911 22.6956 14.7116 23.1603 13.9021 23.5651C12.7328 24.1647 11.5485 24.1348 10.3792 23.5351C9.97444 23.3252 9.58467 23.1004 9.19491 22.8755C7.18612 21.7362 5.17733 20.6119 3.15355 19.4726C2.5839 19.1578 2.0892 18.768 1.71442 18.2433C1.27968 17.6437 1.05482 16.9691 1.03983 16.2345C1.02484 15.5449 1.02484 14.8554 1.02484 14.1508C0.994856 13.3862 0.994856 12.6067 1.00985 11.8422ZM14.6666 22.3658C14.8165 22.3209 14.8615 22.2309 14.8615 22.096C14.8615 21.5863 14.8615 21.0616 14.8615 20.5519C14.8615 20.2071 14.7116 19.9523 14.3968 19.7724C12.5979 18.753 10.784 17.7336 8.98504 16.7292C8.74518 16.5943 8.50533 16.4744 8.26547 16.3245C7.50093 15.8448 6.91628 15.1852 6.58648 14.3307C6.37661 13.776 6.31665 13.2064 6.31665 12.6217C6.31665 10.6579 6.31665 8.67908 6.31665 6.71526C6.31665 6.4904 6.31665 6.26554 6.31665 6.02568C6.31665 5.72586 6.16674 5.51599 5.8969 5.36608C5.44717 5.11123 4.99744 4.87138 4.54771 4.61653C4.42779 4.55657 4.30786 4.51159 4.15795 4.43664C4.15795 4.55657 4.15795 4.64651 4.15795 4.73646C4.15795 7.34489 4.15795 9.95331 4.17294 12.5617C4.17294 13.2813 4.18793 14.0009 4.24789 14.7204C4.32285 15.6049 4.7276 16.3545 5.38721 16.9691C5.74699 17.2989 6.15175 17.5537 6.57149 17.7936C8.92507 19.1278 11.2787 20.462 13.6322 21.7962C13.977 21.9911 14.3368 22.1859 14.6666 22.3658ZM14.7715 16.3395C14.8015 16.1746 14.8315 16.0546 14.8315 15.9347C14.8315 14.8254 14.8465 13.716 14.8315 12.5917C14.8165 11.6773 14.4867 10.8528 13.8571 10.1632C13.4673 9.72845 12.9876 9.39865 12.4779 9.11382C11.5635 8.60413 10.649 8.07944 9.73458 7.56975C9.68961 7.53977 9.62965 7.52478 9.55469 7.4798C9.5397 7.77962 9.50972 8.03447 9.50972 8.30431C9.50972 9.02387 9.50972 9.74344 9.52471 10.463C9.52471 10.9877 9.52471 11.5274 9.65963 12.0371C9.92947 13.1464 10.5891 13.9859 11.5785 14.5705C12.4929 15.1102 13.4224 15.6199 14.3518 16.1446C14.4717 16.2195 14.6066 16.2645 14.7715 16.3395Z" fill="black" />
    <path d="M8.14551 1.67818C8.17549 1.66318 8.20547 1.64819 8.23545 1.6332C8.985 1.22845 9.70457 0.793708 10.4691 0.418935C11.5485 -0.12074 12.6578 -0.12074 13.7671 0.313998C13.887 0.358971 13.992 0.418935 14.1119 0.478898C16.5554 1.84308 18.984 3.20725 21.4275 4.57143C21.8173 4.79629 22.177 5.05114 22.4769 5.38094C22.9566 5.92062 23.2264 6.56523 23.3164 7.2698C23.3463 7.53964 23.3613 7.80948 23.3613 8.07931C23.3613 10.7027 23.3613 13.3262 23.3613 15.9496C23.3613 16.864 23.1065 17.6885 22.4919 18.3931C22.237 18.6929 21.9522 18.9478 21.6074 19.1426C20.8428 19.5924 20.0783 20.0271 19.2988 20.4768C19.2838 20.4918 19.2538 20.4918 19.2388 20.5068C19.2238 20.4918 19.2238 20.4918 19.2088 20.4768C19.2388 20.4169 19.2838 20.3719 19.3138 20.3119C19.8834 19.5774 20.1683 18.7529 20.1683 17.8234C20.1683 15.0651 20.1832 12.3068 20.1533 9.54843C20.1383 8.13928 19.4937 7.04494 18.2644 6.31038C17.0801 5.60581 15.8659 4.91622 14.6666 4.24163C13.4223 3.53705 12.1631 2.84747 10.9188 2.15789C10.0943 1.70816 9.20987 1.57324 8.28043 1.67818" fill="black" />
  </svg>;

export const UnifyLogoDark = () => <svg className="hidden dark:block" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1.00985 11.8422C1.00985 10.6279 1.00985 9.41364 1.00985 8.19937C1.00985 7.70467 1.03983 7.19498 1.17475 6.71526C1.39961 5.93574 1.84934 5.30611 2.52393 4.8414C3.39341 4.25675 4.30786 3.73206 5.26728 3.29733C6.45157 2.74266 7.62086 2.83261 8.74518 3.44724C10.2293 4.25675 11.6984 5.09624 13.1675 5.92074C14.1119 6.46042 15.0564 6.9851 16.0158 7.52478C16.6604 7.89955 17.2001 8.37926 17.5599 9.03886C17.8447 9.54856 17.9796 10.1032 18.0246 10.6879C18.0396 10.8977 18.0396 11.1226 18.0396 11.3325C18.0396 13.806 18.0396 16.2795 18.0396 18.768C18.0396 19.3077 17.9946 19.8473 17.7997 20.357C17.5149 21.1516 17.0052 21.7962 16.2706 22.2309C15.4911 22.6956 14.7116 23.1603 13.9021 23.5651C12.7328 24.1647 11.5485 24.1348 10.3792 23.5351C9.97444 23.3252 9.58467 23.1004 9.19491 22.8755C7.18612 21.7362 5.17733 20.6119 3.15355 19.4726C2.5839 19.1578 2.0892 18.768 1.71442 18.2433C1.27968 17.6437 1.05482 16.9691 1.03983 16.2345C1.02484 15.5449 1.02484 14.8554 1.02484 14.1508C0.994856 13.3862 0.994856 12.6067 1.00985 11.8422ZM14.6666 22.3658C14.8165 22.3209 14.8615 22.2309 14.8615 22.096C14.8615 21.5863 14.8615 21.0616 14.8615 20.5519C14.8615 20.2071 14.7116 19.9523 14.3968 19.7724C12.5979 18.753 10.784 17.7336 8.98504 16.7292C8.74518 16.5943 8.50533 16.4744 8.26547 16.3245C7.50093 15.8448 6.91628 15.1852 6.58648 14.3307C6.37661 13.776 6.31665 13.2064 6.31665 12.6217C6.31665 10.6579 6.31665 8.67908 6.31665 6.71526C6.31665 6.4904 6.31665 6.26554 6.31665 6.02568C6.31665 5.72586 6.16674 5.51599 5.8969 5.36608C5.44717 5.11123 4.99744 4.87138 4.54771 4.61653C4.42779 4.55657 4.30786 4.51159 4.15795 4.43664C4.15795 4.55657 4.15795 4.64651 4.15795 4.73646C4.15795 7.34489 4.15795 9.95331 4.17294 12.5617C4.17294 13.2813 4.18793 14.0009 4.24789 14.7204C4.32285 15.6049 4.7276 16.3545 5.38721 16.9691C5.74699 17.2989 6.15175 17.5537 6.57149 17.7936C8.92507 19.1278 11.2787 20.462 13.6322 21.7962C13.977 21.9911 14.3368 22.1859 14.6666 22.3658ZM14.7715 16.3395C14.8015 16.1746 14.8315 16.0546 14.8315 15.9347C14.8315 14.8254 14.8465 13.716 14.8315 12.5917C14.8165 11.6773 14.4867 10.8528 13.8571 10.1632C13.4673 9.72845 12.9876 9.39865 12.4779 9.11382C11.5635 8.60413 10.649 8.07944 9.73458 7.56975C9.68961 7.53977 9.62965 7.52478 9.55469 7.4798C9.5397 7.77962 9.50972 8.03447 9.50972 8.30431C9.50972 9.02387 9.50972 9.74344 9.52471 10.463C9.52471 10.9877 9.52471 11.5274 9.65963 12.0371C9.92947 13.1464 10.5891 13.9859 11.5785 14.5705C12.4929 15.1102 13.4224 15.6199 14.3518 16.1446C14.4717 16.2195 14.6066 16.2645 14.7715 16.3395Z" fill="white" />
    <path d="M8.14551 1.67818C8.17549 1.66318 8.20547 1.64819 8.23545 1.6332C8.985 1.22845 9.70457 0.793708 10.4691 0.418935C11.5485 -0.12074 12.6578 -0.12074 13.7671 0.313998C13.887 0.358971 13.992 0.418935 14.1119 0.478898C16.5554 1.84308 18.984 3.20725 21.4275 4.57143C21.8173 4.79629 22.177 5.05114 22.4769 5.38094C22.9566 5.92062 23.2264 6.56523 23.3164 7.2698C23.3463 7.53964 23.3613 7.80948 23.3613 8.07931C23.3613 10.7027 23.3613 13.3262 23.3613 15.9496C23.3613 16.864 23.1065 17.6885 22.4919 18.3931C22.237 18.6929 21.9522 18.9478 21.6074 19.1426C20.8429 19.5924 20.0783 20.0271 19.2988 20.4768C19.2838 20.4918 19.2538 20.4918 19.2388 20.5068C19.2238 20.4918 19.2238 20.4918 19.2088 20.4768C19.2388 20.4169 19.2838 20.3719 19.3138 20.3119C19.8834 19.5774 20.1683 18.7529 20.1683 17.8234C20.1683 15.0651 20.1833 12.3068 20.1533 9.54843C20.1383 8.13928 19.4937 7.04494 18.2644 6.31038C17.0801 5.60581 15.8659 4.91622 14.6666 4.24163C13.4223 3.53705 12.1631 2.84747 10.9188 2.15789C10.0943 1.70816 9.20987 1.57324 8.28043 1.67818" fill="white" />
  </svg>;

export const SixsenseLogoLight = () => <svg className="block dark:hidden" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.603 8.31196C14.5316 8.50714 15.4351 8.87062 16.2661 9.40665L13.5118 12.6791C12.0197 11.9955 10.1959 12.3568 9.08921 13.6715C7.98258 14.9851 7.94215 16.8377 8.87688 18.1833L6.1215 21.4558C3.42843 18.5695 3.25322 14.0681 5.86045 10.971L15.0982 0L18.3271 2.7004L13.603 8.31196Z" fill="#13BBB2" />
    <path d="M18.0446 21.1689C15.4365 24.2659 10.959 24.8762 7.63892 22.7335L10.3942 19.4609C11.8864 20.1445 13.7101 19.7841 14.8157 18.4695C15.9225 17.1548 15.9628 15.3024 15.0282 13.9567L17.7834 10.6841C20.4766 13.5704 20.6528 18.0718 18.0446 21.1689Z" fill="#192232" />
  </svg>;

export const SixsenseLogoDark = () => <svg className="hidden dark:block" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.603 8.31196C14.5316 8.50714 15.4351 8.87062 16.2661 9.40665L13.5118 12.6791C12.0197 11.9955 10.1959 12.3568 9.08921 13.6715C7.98258 14.9851 7.94215 16.8377 8.87688 18.1833L6.1215 21.4558C3.42843 18.5695 3.25322 14.0681 5.86045 10.971L15.0982 0L18.3271 2.7004L13.603 8.31196Z" fill="#13BBB2" />
    <path d="M18.0446 21.1689C15.4365 24.2659 10.959 24.8762 7.63892 22.7335L10.3942 19.4609C11.8864 20.1445 13.7101 19.7841 14.8157 18.4695C15.9225 17.1548 15.9628 15.3024 15.0282 13.9567L17.7834 10.6841C20.4766 13.5704 20.6528 18.0718 18.0446 21.1689Z" fill="white" />
  </svg>;

export const SegmentIcon = () => <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
      <g transform="matrix(.768307 0 0 .768307 0 2.304922)">
        <path d="M51.9 52.8H4c-2.2 0-4-1.8-4-4s1.8-4 4-4h47.9c2.2 0 4 1.8 4 4s-1.8 4-4 4z" fill="#99cfac" />
        <path d="M41.7 77.3c-3.9 0-7.8-.6-11.5-1.7-2.1-.7-3.3-2.9-2.6-5s2.9-3.3 5-2.6c2.9.9 6 1.4 9.1 1.4 13.6 0 25.4-8.7 29.3-21.7.6-2.1 2.9-3.3 5-2.7s3.3 2.9 2.7 5c-5.1 16.3-19.9 27.3-37 27.3z" fill="#49b881" />
        <path d="M79.3 32.5H31.4c-2.2 0-4-1.8-4-4s1.8-4 4-4h47.9c2.2 0 4 1.8 4 4s-1.8 4-4 4z" fill="#99cfac" />
        <path d="M8.5 32.5c-.4 0-.8-.1-1.2-.2-2.1-.6-3.3-2.9-2.7-5C9.7 11 24.5 0 41.7 0c3.9 0 7.8.6 11.5 1.7 2.1.7 3.3 2.9 2.6 5s-2.9 3.3-5 2.6c-2.9-.9-6-1.4-9.1-1.4-13.6 0-25.4 8.7-29.3 21.7-.6 1.8-2.2 2.9-3.9 2.9z" fill="#49b881" />
        <g fill="#99cfac">
          <circle r="4" cy="13.3" cx="65.4" />
          <circle r="4" cy="64.1" cx="17.9" />
        </g>
      </g>
    </svg>;

export const SalesforceLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M9.98736 5.83214C10.7614 5.02566 11.839 4.52545 13.0308 4.52545C14.6151 4.52545 15.9973 5.40886 16.7334 6.72031C17.373 6.43452 18.0811 6.27553 18.826 6.27553C21.6834 6.27553 24 8.6123 24 11.4947C24 14.3774 21.6834 16.7142 18.826 16.7142C18.4837 16.7144 18.1423 16.6803 17.8068 16.6126C17.1587 17.7688 15.9234 18.5501 14.5057 18.5501C13.9121 18.5501 13.3508 18.413 12.851 18.1692C12.1939 19.7148 10.6629 20.7986 8.87863 20.7986C7.02052 20.7986 5.43692 19.6229 4.82907 17.974C4.56344 18.0304 4.28822 18.0598 4.00581 18.0598C1.79351 18.0598 0 16.2479 0 14.0123C0 12.5142 0.805814 11.2061 2.00308 10.5063C1.75659 9.93915 1.61948 9.31315 1.61948 8.65502C1.61948 6.08408 3.70667 4 6.28103 4C7.79248 4 9.13574 4.71863 9.98736 5.83214Z" fill="#00A1E0" />
  </svg>;

export const PlaysIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"></path>
    <path d="M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"></path>
    <path d="M11 19h5.5a3.5 3.5 0 0 0 0 -7h-8a3.5 3.5 0 0 1 0 -7h4.5"></path>
  </svg>;

export const PersonasIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M4 4m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v1a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M4 13m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v3a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M14 4m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v3a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M14 15m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v1a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
  </svg>;

export const OutlookLogo = () => <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1831.085 1703.335" enable-background="new 0 0 1831.085 1703.335" xml:space="preserve">
    <path fill="#0A2767" d="M1831.083,894.25c0.1-14.318-7.298-27.644-19.503-35.131h-0.213l-0.767-0.426l-634.492-375.585  c-2.74-1.851-5.583-3.543-8.517-5.067c-24.498-12.639-53.599-12.639-78.098,0c-2.934,1.525-5.777,3.216-8.517,5.067L446.486,858.693  l-0.766,0.426c-19.392,12.059-25.337,37.556-13.278,56.948c3.553,5.714,8.447,10.474,14.257,13.868l634.492,375.585  c2.749,1.835,5.592,3.527,8.517,5.068c24.498,12.639,53.599,12.639,78.098,0c2.925-1.541,5.767-3.232,8.517-5.068l634.492-375.585  C1823.49,922.545,1831.228,908.923,1831.083,894.25z" />
    <path fill="#0364B8" d="M520.453,643.477h416.38v381.674h-416.38V643.477z M1745.917,255.5V80.908  c1-43.652-33.552-79.862-77.203-80.908H588.204C544.552,1.046,510,37.256,511,80.908V255.5l638.75,170.333L1745.917,255.5z" />
    <path fill="#0078D4" d="M511,255.5h425.833v383.25H511V255.5z" />
    <path fill="#28A8EA" d="M1362.667,255.5H936.833v383.25L1362.667,1022h383.25V638.75L1362.667,255.5z" />
    <path fill="#0078D4" d="M936.833,638.75h425.833V1022H936.833V638.75z" />
    <path fill="#0364B8" d="M936.833,1022h425.833v383.25H936.833V1022z" />
    <path fill="#14447D" d="M520.453,1025.151h416.38v346.969h-416.38V1025.151z" />
    <path fill="#0078D4" d="M1362.667,1022h383.25v383.25h-383.25V1022z" />
    <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="1128.4584" y1="811.0833" x2="1128.4584" y2="1.9982" gradientTransform="matrix(1 0 0 -1 0 1705.3334)">
      <stop offset="0" style={{
  "stop-color": "#35B8F1"
}} />
      <stop offset="1" style={{
  "stop-color": "#28A8EA"
}} />
    </linearGradient>
    <path fill="url(#SVGID_1_)" d="M1811.58,927.593l-0.809,0.426l-634.492,356.848c-2.768,1.703-5.578,3.321-8.517,4.769  c-10.777,5.132-22.481,8.029-34.407,8.517l-34.663-20.27c-2.929-1.47-5.773-3.105-8.517-4.897L447.167,906.003h-0.298  l-21.036-11.753v722.384c0.328,48.196,39.653,87.006,87.849,86.7h1230.914c0.724,0,1.363-0.341,2.129-0.341  c10.18-0.651,20.216-2.745,29.808-6.217c4.145-1.756,8.146-3.835,11.966-6.217c2.853-1.618,7.75-5.152,7.75-5.152  c21.814-16.142,34.726-41.635,34.833-68.772V894.25C1831.068,908.067,1823.616,920.807,1811.58,927.593z" />
    <path opacity="0.5" fill="#0A2767" enable-background="new    " d="M1797.017,891.397v44.287l-663.448,456.791L446.699,906.301  c0-0.235-0.191-0.426-0.426-0.426l0,0l-63.023-37.899v-31.938l25.976-0.426l54.932,31.512l1.277,0.426l4.684,2.981  c0,0,645.563,368.346,647.267,369.197l24.698,14.478c2.129-0.852,4.258-1.703,6.813-2.555  c1.278-0.852,640.879-360.681,640.879-360.681L1797.017,891.397z" />
    <path fill="#1490DF" d="M1811.58,927.593l-0.809,0.468l-634.492,356.848c-2.768,1.703-5.578,3.321-8.517,4.769  c-24.641,12.038-53.457,12.038-78.098,0c-2.918-1.445-5.76-3.037-8.517-4.769L446.657,928.061l-0.766-0.468  c-12.25-6.642-19.93-19.409-20.057-33.343v722.384c0.305,48.188,39.616,87.004,87.803,86.7c0.001,0,0.002,0,0.004,0h1229.636  c48.188,0.307,87.5-38.509,87.807-86.696c0-0.001,0-0.002,0-0.004V894.25C1831.068,908.067,1823.616,920.807,1811.58,927.593z" />
    <path opacity="0.1" enable-background="new    " d="M1185.52,1279.629l-9.496,5.323c-2.752,1.752-5.595,3.359-8.517,4.812  c-10.462,5.135-21.838,8.146-33.47,8.857l241.405,285.479l421.107,101.476c11.539-8.716,20.717-20.178,26.7-33.343L1185.52,1279.629  z" />
    <path opacity="0.05" enable-background="new    " d="M1228.529,1255.442l-52.505,29.51c-2.752,1.752-5.595,3.359-8.517,4.812  c-10.462,5.135-21.838,8.146-33.47,8.857l113.101,311.838l549.538,74.989c21.649-16.254,34.394-41.743,34.407-68.815v-9.326  L1228.529,1255.442z" />
    <path fill="#28A8EA" d="M514.833,1703.333h1228.316c18.901,0.096,37.335-5.874,52.59-17.033l-697.089-408.331  c-2.929-1.47-5.773-3.105-8.517-4.897L447.125,906.088h-0.298l-20.993-11.838v719.914  C425.786,1663.364,465.632,1703.286,514.833,1703.333C514.832,1703.333,514.832,1703.333,514.833,1703.333z" />
    <path opacity="0.1" enable-background="new    " d="M1022,418.722v908.303c-0.076,31.846-19.44,60.471-48.971,72.392  c-9.148,3.931-19,5.96-28.957,5.962H425.833V383.25H511v-42.583h433.073C987.092,340.83,1021.907,375.702,1022,418.722z" />
    <path opacity="0.2" enable-background="new    " d="M979.417,461.305v908.302c0.107,10.287-2.074,20.469-6.388,29.808  c-11.826,29.149-40.083,48.273-71.54,48.417H425.833V383.25h475.656c12.356-0.124,24.533,2.958,35.344,8.943  C962.937,405.344,979.407,432.076,979.417,461.305z" />
    <path opacity="0.2" enable-background="new    " d="M979.417,461.305v823.136c-0.208,43-34.928,77.853-77.927,78.225H425.833V383.25  h475.656c12.356-0.124,24.533,2.958,35.344,8.943C962.937,405.344,979.407,432.076,979.417,461.305z" />
    <path opacity="0.2" enable-background="new    " d="M936.833,461.305v823.136c-0.046,43.067-34.861,78.015-77.927,78.225H425.833  V383.25h433.072c43.062,0.023,77.951,34.951,77.927,78.013C936.833,461.277,936.833,461.291,936.833,461.305z" />
    <linearGradient id="SVGID_2_" gradientUnits="userSpaceOnUse" x1="162.7469" y1="1383.0741" x2="774.0864" y2="324.2592" gradientTransform="matrix(1 0 0 -1 0 1705.3334)">
      <stop offset="0" style={{
  "stop-color": "#1784D9"
}} />
      <stop offset="0.5" style={{
  "stop-color": "#107AD5"
}} />
      <stop offset="1" style={{
  "stop-color": "#0A63C9"
}} />
    </linearGradient>
    <path fill="url(#SVGID_2_)" d="M78.055,383.25h780.723c43.109,0,78.055,34.947,78.055,78.055v780.723  c0,43.109-34.946,78.055-78.055,78.055H78.055c-43.109,0-78.055-34.947-78.055-78.055V461.305  C0,418.197,34.947,383.25,78.055,383.25z" />
    <path fill="#FFFFFF" d="M243.96,710.631c19.238-40.988,50.29-75.289,89.17-98.495c43.057-24.651,92.081-36.94,141.675-35.515  c45.965-0.997,91.321,10.655,131.114,33.683c37.414,22.312,67.547,55.004,86.742,94.109c20.904,43.09,31.322,90.512,30.405,138.396  c1.013,50.043-9.706,99.628-31.299,144.783c-19.652,40.503-50.741,74.36-89.425,97.388c-41.327,23.734-88.367,35.692-136.011,34.578  c-46.947,1.133-93.303-10.651-134.01-34.067c-37.738-22.341-68.249-55.07-87.892-94.28c-21.028-42.467-31.57-89.355-30.745-136.735  C212.808,804.859,223.158,755.686,243.96,710.631z M339.006,941.858c10.257,25.912,27.651,48.385,50.163,64.812  c22.93,16.026,50.387,24.294,78.353,23.591c29.783,1.178,59.14-7.372,83.634-24.358c22.227-16.375,39.164-38.909,48.715-64.812  c10.677-28.928,15.946-59.572,15.543-90.404c0.33-31.127-4.623-62.084-14.649-91.554c-8.855-26.607-25.246-50.069-47.182-67.537  c-23.88-17.79-53.158-26.813-82.91-25.55c-28.572-0.74-56.644,7.593-80.184,23.804c-22.893,16.496-40.617,39.168-51.1,65.365  c-23.255,60.049-23.376,126.595-0.341,186.728L339.006,941.858z" />
    <path fill="#50D9FF" d="M1362.667,255.5h383.25v383.25h-383.25V255.5z" />
  </svg>;

export const HubspotLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.2421 17.2947C15.4495 17.2947 13.9963 15.8566 13.9963 14.0829C13.9963 12.3088 15.4495 10.8707 17.2421 10.8707C19.0348 10.8707 20.488 12.3088 20.488 14.0829C20.488 15.8566 19.0348 17.2947 17.2421 17.2947ZM18.2138 7.89901V5.04163C18.9675 4.68936 19.4954 3.93487 19.4954 3.05925V2.9933C19.4954 1.78482 18.4963 0.796098 17.2751 0.796098H17.2088C15.9876 0.796098 14.9885 1.78482 14.9885 2.9933V3.05925C14.9885 3.93487 15.5164 4.68966 16.2701 5.04194V7.89901C15.148 8.07068 14.1227 8.52868 13.2772 9.20272L5.34945 3.09994C5.40177 2.90114 5.43852 2.6965 5.43884 2.48137C5.44008 1.11293 4.32076 0.00185084 2.93734 1.60552e-06C1.55455 -0.00153942 0.43149 1.10646 0.429933 2.4752C0.428376 3.84395 1.54769 4.95503 2.93111 4.95657C3.38177 4.95719 3.7991 4.83051 4.16473 4.62463L11.9629 10.6282C11.2998 11.6188 10.9112 12.8053 10.9112 14.0829C10.9112 15.4202 11.3381 16.6573 12.0594 17.6747L9.68813 20.0217C9.50065 19.9659 9.30631 19.9271 9.10013 19.9271C7.96369 19.9271 7.04213 20.8387 7.04213 21.9634C7.04213 23.0883 7.96369 24 9.10013 24C10.2369 24 11.1581 23.0883 11.1581 21.9634C11.1581 21.76 11.1189 21.5673 11.0625 21.3818L13.4083 19.0604C14.4731 19.8645 15.7992 20.3478 17.2421 20.3478C20.7387 20.3478 23.5728 17.5428 23.5728 14.0829C23.5728 10.9506 21.2476 8.36286 18.2138 7.89901Z" fill="#FF7A59" />
  </svg>;

export const GoogleWorkspaceLogo = () => <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
    <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
    <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
    <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
    <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
    <path d="M1 1h22v22H1z" fill="none" />
  </svg>;

export const GmailLogo = () => <svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1.64075 21.0162H5.46917V11.7508L0 7.63281V19.3754C0 20.2762 0.739946 21.0162 1.64075 21.0162Z" fill="#4285F4" />
    <path d="M18.563 21.0162H22.3914C23.2922 21.0162 24.0322 20.2762 24.0322 19.3754V7.63281L18.563 11.7186" fill="#34A853" />
    <path d="M18.563 4.64079V11.7507L24.0322 7.66492V5.44508C24.0322 3.41827 21.7158 2.2601 20.1072 3.48262" fill="#FBBC04" />
    <path d="M5.46924 11.7505V4.64062L12.0322 9.56288L18.5631 4.64062V11.7505L12.0001 16.6406" fill="#EA4335" />
    <path d="M0 5.44515V7.63282L5.46917 11.7186V4.64086L3.92493 3.48268C2.31635 2.29233 0 3.45051 0 5.44515Z" fill="#C5221F" />
  </svg>;

export const ExclusionsIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
    <path d="M5.7 5.7l12.6 12.6"></path>
  </svg>;

export const ClearbitLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M17.5703 23.9994H6.43997H5.97931C4.10691 23.9697 3.34903 23.7467 2.60602 23.3307C1.7887 22.8997 1.16457 22.2607 0.718762 21.4434L0.6296 21.2651C0.272953 20.5369 0.0649091 19.7196 0.0500488 17.8175V6.40478C0.0500488 4.17574 0.287813 3.37329 0.718762 2.55597C1.14971 1.73865 1.7887 1.09966 2.60602 0.668713L2.78434 0.579553C3.5125 0.222906 4.31495 0.0148603 6.21707 0H17.5703C19.7845 0 20.587 0.237765 21.4043 0.668713C22.2216 1.09966 22.8457 1.73865 23.2915 2.55597L23.3807 2.7343C23.7374 3.46245 23.9454 4.27976 23.9603 6.18188V17.5946V18.0553C23.9305 19.9425 23.7076 20.6855 23.3064 21.4434C22.8755 22.2607 22.2365 22.8997 21.4191 23.3307L21.2408 23.4198C20.4681 23.8062 19.6359 23.9994 17.5703 23.9994Z" fill="#C4D3E0" fill-opacity="0.2" />
    <path d="M23.9452 12.0078V17.5953C23.9452 19.8243 23.7075 20.6268 23.2765 21.4441C22.8456 22.2614 22.2066 22.9004 21.3893 23.3314C20.5719 23.7623 19.7695 24.0001 17.5553 24.0001H11.9976V12.0078H23.9452Z" fill="url(#paint0_linear_239_59)" />
    <path d="M11.9976 0.0146484H17.5553C19.7695 0.0146484 20.5719 0.252413 21.3893 0.683362C22.2066 1.11431 22.8307 1.7533 23.2765 2.57062C23.7075 3.38793 23.9452 4.19039 23.9452 6.41943V12.0069H11.9976V0.0146484Z" fill="url(#paint1_linear_239_59)" />
    <path d="M6.43997 0.0146484H11.9977V23.9992H6.43997C4.22579 23.9992 3.42333 23.7614 2.60602 23.3304C1.7887 22.8995 1.16457 22.2605 0.718762 21.4432C0.287813 20.6259 0.0500488 19.8234 0.0500488 17.5944V6.41943C0.0500488 4.19039 0.287813 3.38793 0.718762 2.57062C1.14971 1.7533 1.7887 1.11431 2.60602 0.683362C3.42333 0.252413 4.22579 0.0146484 6.43997 0.0146484Z" fill="url(#paint2_linear_239_59)" />
    <defs>
      <linearGradient id="paint0_linear_239_59" x1="15.5715" y1="13.2151" x2="21.5827" y2="25.188" gradientUnits="userSpaceOnUse">
        <stop stop-color="#DEF2FE" />
        <stop offset="1" stop-color="#DBF1FE" />
      </linearGradient>
      <linearGradient id="paint1_linear_239_59" x1="13.5922" y1="-0.783111" x2="19.6034" y2="11.1898" gradientUnits="userSpaceOnUse">
        <stop stop-color="#57BCFD" />
        <stop offset="1" stop-color="#51B5FD" />
      </linearGradient>
      <linearGradient id="paint2_linear_239_59" x1="1.70069" y1="1.43981" x2="11.9197" y2="21.7937" gradientUnits="userSpaceOnUse">
        <stop stop-color="#1CA7FD" />
        <stop offset="1" stop-color="#148CFC" />
      </linearGradient>
    </defs>
  </svg>;

<Steps titleSize="h2">
  <Step title="Integrate your website">
    Connect Unify to your website traffic to start revealing visitors. There are several supported methods of integrating your website with Unify:

    <CardGroup cols={1}>
      <Card title="Website Tag (Recommended)" href="/developers/intent-client/website-tag" icon="code" horizontal>
        Add the Unify JavaScript snippet to your website with minimal setup.
      </Card>

      <Card title="Intent Client" href="/developers/intent-client/overview#installation" icon="brackets-curly" horizontal>
        For full customizability, install the Unify Intent client in your web app.
      </Card>

      <Card title="Segment" href="/reference/integrations/segment" icon={<SegmentIcon />} horizontal>
        Connect your existing Segment subscription to send traffic to Unify.
      </Card>
    </CardGroup>

    Typically this integration is owned by engineering or marketing.
  </Step>

  <Step title="Turn on website intent data">
    Turn on website intent data so that you start revealing the companies behind anonymous website traffic. Unify provides intent data out of the box with no configuration required:

    <Card
      title="Unify Intent"
      href="https://app.unifygtm.com/dashboard/settings/integrations/unify-intent"
      icon={
      <>
        <UnifyLogoDark />
        <UnifyLogoLight />
      </>
    }
      horizontal
    >
      Enable high-coverage website identification in just a few clicks. Unify Intent
      combines multiple data sources to achieve best-in-class coverage.
    </Card>
  </Step>

  <Step title="Connect your CRM">
    Connect your CRM of choice to begin running plays on your existing data, finding new prospects, tracking champions, and more:

    <CardGroup cols={2}>
      <Card title="Salesforce" href="/reference/integrations/salesforce/overview" icon={<SalesforceLogo />} horizontal>
        Connect your Salesforce instance.
      </Card>

      <Card title="HubSpot" href="/reference/integrations/hubspot/overview" icon={<HubspotLogo />} horizontal>
        Connect your HubSpot CRM.
      </Card>
    </CardGroup>

    Typically this integration is owned by a sales leader or sales/revenue operations team.
  </Step>

  <Step title="Connect mailboxes">
    Unify provides several ways of setting up mailboxes to start sending emails. If
    you have existing mailboxes, you can connect them in only a few clicks.

    <CardGroup cols={2}>
      <Card title="Gmail" href="/reference/integrations/gmail" icon={<GoogleWorkspaceLogo />} horizontal>
        Connect Gmail mailboxes.
      </Card>

      <Card
        title="Unify Managed"
        href="/reference/deliverability/overview"
        icon={
        <>
          <UnifyLogoDark />
          <UnifyLogoLight />
        </>
      }
        horizontal
      >
        Unify will create mailboxes for you.
      </Card>
    </CardGroup>

    If you plan on using Unify-managed mailboxes with, you'll need to add domain
    names and create new email addresses. See the [Deliverability](/reference/deliverability/overview)
    guide for setup instructions.
  </Step>

  <Step title="Browse tutorials">
    You're ready to start using Unify! We recommend checking out some of the [Tutorials](/tutorials).
    Here are a few of the most popular starting points:

    <CardGroup cols={3}>
      <Card title="Create an Exclusion" icon={<ExclusionsIcon />} href="/tutorials/how-to-create-an-exclusion">
        Prevent Unify from actioning on specific companies or people.
      </Card>

      <Card title="Define Personas" icon={<PersonasIcon />} href="/tutorials/how-to-use-personas">
        Create personas to prospect and reach out to your ideal buyers.
      </Card>

      <Card title="Create a Play" icon={<PlaysIcon />} href="/tutorials/how-to-create-a-play">
        Learn the fundamentals and build a Unify Play from start to finish.
      </Card>
    </CardGroup>

    You can also check out the [official YouTube channel](https://www.youtube.com/@Unifygtm)
    where there are a number of video tutorials covering everything from the basics
    to sophisticated growth campaigns.
  </Step>
</Steps>


# Welcome to Unify
Source: https://docs.unifygtm.com/getting-started/welcome

Unify is the all-in-one solution for sales, marketing, and go-to-market teams.

Whether you're new to Unify and looking to get started or an experienced user
aiming to get the most out of the platform, we have the resources you need to
succeed.

<CardGroup cols={2}>
  <Card title="Onboarding Guide (<30 min)" icon="forward-fast" iconType="sharp-regular" href="/getting-started/onboarding-guide">
    Complete a few key steps to fully activate on Unify. For new customers
    looking to get up and running quickly, this is the place to start.
  </Card>

  <Card title="Tutorials" icon="rocket-launch" iconType="sharp-regular" href="/tutorials/welcome">
    Hit the ground running with our most popular plays and best practices.
  </Card>

  <Card title="Reference" icon="book" iconType="sharp-regular" href="/reference/overview">
    Explore the full range of features available in Unify with our in-depth
    reference guide.
  </Card>

  <Card title="Knowledge Base" icon="circle-question" iconType="sharp-regular" href="https://support.unifygtm.com/">
    Find answers to common questions and troubleshooting tips in our help
    center.
  </Card>
</CardGroup>

<Tip>
  For Pro and Enterprise customers, Unify offers white glove onboarding and
  support. For more information, [book an intro
  call](https://www.unifygtm.com/get-started) or reach out to
  [support@unifygtm.com](mailto:support@unifygtm.com).
</Tip>


# Building an Agent
Source: https://docs.unifygtm.com/reference/agents/building-an-agent

Learn the fundamentals of building Agents in Unify.

## Agent configuration

Every Agent has three components:

1. **Record Type**: Specify whether this agent will run on Company records or Person records.
2. **Questions**: Define research questions for the agent to answer.
3. (Optional) **Guidance**: Provide additional context or advice to the agent to improve the results.

Once you've configured your Agent, test it by running it on example Companies or People.

<Frame caption="An empty Agent modal.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=99616e9820e84ac8aec22ee50ecd986c" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/agents/empty-agent-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=69b80e50f625afbd330c6b2a14873b88 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0f8f2db3383ce2a6588b9ccdba967521 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bfa69ea70d5b84d00b33f2d422e60335 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1f3de99ea6cf98d64fd34e29925dad4a 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=48f14d50d7dee050f7ed99838555d3b3 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/empty-agent-modal.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2a761d0d5d423f6a48128cad800addfd 2500w" />
</Frame>

### Record type

Agents can run on Companies or People. Data from Unify for the underlying records will be made
available to the Agent as it performs research to answer your questions.

For example, an agent intended to perform account qualification will run on company records.
On the other hand, an agent that researches individual people for lead qualification will run on person records.

<Warning>Once you save an Agent, you cannot change its record type.</Warning>

### Questions

Define a set of questions that the Agent will answer for you.
Every question has an expected response type. The available response types are:

* **True / False**
* **Number**
* **Select**

View the [response types documentation](/reference/agents/response-types) for more details and examples.
Try to keep your questions straightforward and concise.
Use a [guidance prompt](#guidance-prompt) to guide define any special
terms or concepts that the Agent should know.

### Guidance prompt

Optionally, you may provide a prompt to help guide your Agent's thought process.
If there is any context the Agent needs to answer your question, this is the place to include it.

In most cases, providing guidance for the Agent is unnecessary.
The Agent already knows that it will be answering questions about a company or person,
so you do not need to include that information in the prompt.

Examples of things to include in a guidance prompt:

* What your company does
* Where to find specific information about the Person or Company to research
* Definitions for specialized terms and concepts

<Tip>
  Unify provides deep customization of and visibility into Agents' thought processes.
  You can take advantage of this to tweak questions or guidance and dial in the accuracy.
</Tip>

## Testing your Agent

Unify gives you best-in-class visibility into an AI's chain-of-thought.
Leverage this to test your Agent, diagnose any issues, and iterate on your
questions and guidance prompts.

Upon providing a valid Agent configuration, an extension will appear and prompt
you to test your Agent. Use the search bar to find a specific Company or Person to test your Agent on,
or use the shuffle button to randomly select a Company or Person. The Agent will run,
explain its reasoning, and provide responses to your questions.

<Tip>
  Generate multiple examples simultaneously to speed up your workflow.
  Navigate through these examples using the arrows at the top of the screen.
</Tip>

<Frame caption="Run the Agent on multiple records concurrently and navigate using the arrows.">
  <video autoPlay muted loop playsInline src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/navigate-agent-examples.mp4?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5dc6a82150a1c52fbf980dede6513a1a" data-path="images/reference/agents/navigate-agent-examples.mp4" />
</Frame>


# Unify Agents
Source: https://docs.unifygtm.com/reference/agents/overview

Learn what Unify Agents are and how to use them.

## What are Agents?

Agents are tools that research and answer questions about Companies and People in Unify.
You provide questions, and Unify will provide answers.

Agents use state-of-the-art LLMs to automate research on your prospects.
If the answer to your question exists on the internet, Unify
Agents will find it for you.

<Frame caption="An example of an Agent answering questions about Unify.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4ed7d602a95ec7b827ad3c9b29c0afb7" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/agents/agent-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f0c62e19047eb333af5947e31ea2ea6a 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6f0bf27cdeffc3eac1b8cf2aa49b0182 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a8db58d0f4bac898add361709304a0ec 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a4c38548d8102c6a34dac6c002cc1ea5 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=de1c6c19951b9ebc677f5d2a206edd11 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-overview.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9d7122050199d43e535f8502adb28986 2500w" />
</Frame>

## Use cases

Agents are new to the Unify platform, and their range of use cases is quickly expanding.

* **Account qualification**: Agents can be used to qualify Companies that run
  through your [Plays](/reference/plays/overview).
* **Lead qualification**: Agents can be used to qualify People that run through
  your [Plays](/reference/plays/overview).

<Tip>Check out the [Agent qualification action](/reference/plays/actions#agent-qualification) to use Agents in your Plays.</Tip>


# Agent Response Types
Source: https://docs.unifygtm.com/reference/agents/response-types

Control how Unify Agents respond to your questions.

## Overview

A single Agent can answer multiple questions, each with different response types.
Unify ensures that Agents adhere to the response types you specify to give
you fine-grained control over AI.

<Tip>Unify Agents know what they don't know. If the Agent cannot find an
answer to your question, it will respond accordingly.</Tip>

<Frame caption="An example of an Agent using various response types.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=112343d2875c85a30d4e3c6a17572968" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/agents/agent-response-types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=00093adf2b7f7dcd417567a78120db5a 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b2037a079d72d9e8a4b0ccdf031f4037 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=08df70916e4de9ac5ae4213ec0c3a975 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=515e30938e02a1ec422e82038bfe1e75 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2f515386b92652ddf504209e82dbb60 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/agents/agent-response-types.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ccf3595d0092584d5a55e25b732d5611 2500w" />
</Frame>

## Response types

### True / False

Agents will respond with either `True` or `False` to a question of this type. This is best for simple questions:

* *Does this company have an office in San Francisco?*
* *Is there a pricing page on this company's website?*

### Number

Agents will respond with a number to a question of this type. This is best for questions that require a numerical answer:

* *What was the revenue for this company last year?*
* *How many years of full-time experience does this person have?*

### Select

Agents will respond with a *single* option from a list that you specify.
This is best for multiple-choice questions:

* *Is this company B2B, B2C, or B2G?*
  * Options: `B2B`, `B2C`, `B2G`
  * Answer: `B2B`

In some cases, you may want the Agent to respond with *multiple* options from the list you provided.
Click the `Allow multiple options` checkbox to enable this.
When enabled, the Agent will respond with zero, one, or multiple options.

* *Which of the following funding rounds has this company completed?*
  * Options: `Seed`, `Series A`, `Series B`, `Series C`, `Series D`, `Series E`
  * Answer: `Seed`, `Series A`


# Overview
Source: https://docs.unifygtm.com/reference/ai-research/overview

Learn about how AI Research works

## How does AI Research work?

When you onboard to Unify, our multi-agent system conducts research on your Company to understand your products, customers, and value proposition. The system uses this information about your Company to analyze and assess what insights you may consider important when evaluating prospect Companies, and creates Observations for those insights. These Observations are the default set of insights that Unify will use to generate AI Research reports for you.

<Tip>
  An Observation is a key piece of information that the system will try to find for a given Company.
</Tip>

<Frame caption="An example of an Observation in AI Research">
    <img src="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=f97e1de25ac86b2ed76d89fb91d57262" alt="" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/ai-research/ai-research.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=280&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=f5b6ca1e696cb63be5a1b38a5111f5e7 280w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=560&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=9284ae3c50d301afcd7d7b24d1397cbe 560w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=840&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=9e982a650f0b96a4358dd1b3c89c9f18 840w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=1100&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=d9d6d22dfc1c9bbac71a2c8416151e9b 1100w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=1650&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=bd54ea98f3d6bd613161ec6b77d0e5ba 1650w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/ai-research.png?w=2500&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=f6415982f514fc051dd95c0f95999ebb 2500w" />
</Frame>

When Unify generates an AI Research report for you, the multi-agent system takes the current Observations you have set (or that we have preset for you), and conducts research on each Observation to surface the most relevant insights for your team to read and reference.

<Frame caption="An example of Observations in the AI Research settings page">
    <img src="https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=78042b027ce1c8ab27bc27fae0498204" alt="" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/ai-research/ai-research-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=280&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=e3874c9b8c789c292bcbbdb5dc2378e6 280w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=560&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=688258be577ee0058aa1d3509eb4721b 560w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=840&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=75761f3b1552f73339481964ea054304 840w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=1100&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=ceae874ebeaab51138f821e839bb0d45 1100w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=1650&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=06e35a9caa4500aeb8ed2e27f4643978 1650w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/ai-research-settings.png?w=2500&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=0420d7ea28af2b2e7008ff192137a396 2500w" />
</Frame>

### Accessing AI Research

To access AI Research, you can click on the AI Research tab on any Task, Company, or Person page. AI Research will be automatically generated for Tasks,
but for Company and People pages, they can be generated on demand.

<Frame caption="An example of generating AI Research on demand for a Company">
    <img src="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=d395fa415243817edd3308b861536c98" alt="" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/ai-research/generate-ai-research.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=280&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=aa2a864e4609c389319e6d7552b38aa4 280w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=560&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=4fbad2de43f7501f32d180626428b99a 560w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=840&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=3c4bfd6c9949a77570b9adae0aa0b9cf 840w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=1100&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=f9df44b1ef82b1d69442481205f88767 1100w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=1650&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=8912d7701a445da56c56894426468eb2 1650w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/generate-ai-research.png?w=2500&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=0c17589c3df14b072d77be2d8682f75a 2500w" />
</Frame>

## Modifying your Observations

Admins have the ability to add Observations (up to a maximum of 8), edit Observations, and delete Observations. Additionally Admins can re-order the Observations in the AI Research settings page which will adjust the order of Observations that shows up in the AI Research panel.

Adding, Updating, or Deleting Observations will modify the AI Research that is generated for future AI Research generated in Task, People, and Company pages.

Once you have added a new Observation or made updates to an existing Observation,
you will also be able to regenerate existing AI Research on demand. AI Research that was based on old Observations will show a banner with a button to "regenerate" the AI Research.

<Frame caption="AI Research that can be regenerated after updating Observations">
    <img src="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=af9fb236037e3d78f96bb816c62bff78" alt="" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/ai-research/regenerate-ai-research.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=280&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=45ca2967b533604eb99693a3716b296b 280w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=560&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=a4e02264cb873bb4f1a035d060f37e4c 560w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=840&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=c20d4435a1fe4a2c1c548cbacb7d1179 840w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=1100&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=27b77eeb5ef41e9a2b952d8bab3e0938 1100w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=1650&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=b5327029096f2a726a7bb56b5560cc4f 1650w, https://mintcdn.com/unify-19/wO5FIzvyCqa7gdBX/images/reference/ai-research/regenerate-ai-research.png?w=2500&fit=max&auto=format&n=wO5FIzvyCqa7gdBX&q=85&s=8022cfae03f3c5b89e1dbef0d733f868 2500w" />
</Frame>

## Testing your Observations

After providing a valid Observation configuration (Observation name and prompt), you can test your Observation to see if the configuration retrieves what you are looking for. You can either generate Observations for specific companies, or select a random sample of companies to test on. Use this page to experiment and iterate on the Observation prompts until you are satisfied with the resulting AI Research.

<Tip>
  To get effective Observations, ensure that your prompt explains all of the context that is needed to retrieve the information that you are looking for.
</Tip>

<Frame caption="Run Observations on multiple companies to test your prompts">
    <img src="https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=a5d68cd466c51d0cd80de5fa6b5ae554" alt="" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/ai-research/testing-ai-research-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=280&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=7f0a1c112b3b2ef5967e50647cbe8b26 280w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=560&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=e9ffbb589fe11642f9df9452174b40ba 560w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=840&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=f8312273b1674ad53b1fb961074cfc63 840w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=1100&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=941b6de7a54ae5084ccea28bbc0180a6 1100w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=1650&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=d43179bb7eacb365de028109497ba847 1650w, https://mintcdn.com/unify-19/iWmGra0KpE0JpSSL/images/reference/ai-research/testing-ai-research-prompt.png?w=2500&fit=max&auto=format&n=iWmGra0KpE0JpSSL&q=85&s=7581a87cd50cff3d5b53712c87a6e34b 2500w" />
</Frame>


# HubSpot
Source: https://docs.unifygtm.com/reference/browser-extension/hubspot

Run the Unify Chrome extension in HubSpot.

While viewing Companies and Contacts in HubSpot, the extension will
automatically surface the corresponding Companies and People in Unify.

## HubSpot Company Page

From this view, you can view People in your Unify instance who work at this Company (and add
them to a Sequence) or instantly add this Company to a Play of your choosing.

## HubSpot Contact Page

From this view, you can check if this Person is currently enrolled in a Unify Sequence.
If they are not already enrolled, you can enroll them from here using any mailbox or
mailbox group in Unify. Additionally, you can instantly add this Person to any of the
Plays you’ve built. See more info on building Plays in Unify [here](/reference/plays/overview).


# Introduction
Source: https://docs.unifygtm.com/reference/browser-extension/installation

Get started with the Unify Chrome extension.

export const SalesforceLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M9.98736 5.83214C10.7614 5.02566 11.839 4.52545 13.0308 4.52545C14.6151 4.52545 15.9973 5.40886 16.7334 6.72031C17.373 6.43452 18.0811 6.27553 18.826 6.27553C21.6834 6.27553 24 8.6123 24 11.4947C24 14.3774 21.6834 16.7142 18.826 16.7142C18.4837 16.7144 18.1423 16.6803 17.8068 16.6126C17.1587 17.7688 15.9234 18.5501 14.5057 18.5501C13.9121 18.5501 13.3508 18.413 12.851 18.1692C12.1939 19.7148 10.6629 20.7986 8.87863 20.7986C7.02052 20.7986 5.43692 19.6229 4.82907 17.974C4.56344 18.0304 4.28822 18.0598 4.00581 18.0598C1.79351 18.0598 0 16.2479 0 14.0123C0 12.5142 0.805814 11.2061 2.00308 10.5063C1.75659 9.93915 1.61948 9.31315 1.61948 8.65502C1.61948 6.08408 3.70667 4 6.28103 4C7.79248 4 9.13574 4.71863 9.98736 5.83214Z" fill="#00A1E0" />
  </svg>;

export const HubspotLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.2421 17.2947C15.4495 17.2947 13.9963 15.8566 13.9963 14.0829C13.9963 12.3088 15.4495 10.8707 17.2421 10.8707C19.0348 10.8707 20.488 12.3088 20.488 14.0829C20.488 15.8566 19.0348 17.2947 17.2421 17.2947ZM18.2138 7.89901V5.04163C18.9675 4.68936 19.4954 3.93487 19.4954 3.05925V2.9933C19.4954 1.78482 18.4963 0.796098 17.2751 0.796098H17.2088C15.9876 0.796098 14.9885 1.78482 14.9885 2.9933V3.05925C14.9885 3.93487 15.5164 4.68966 16.2701 5.04194V7.89901C15.148 8.07068 14.1227 8.52868 13.2772 9.20272L5.34945 3.09994C5.40177 2.90114 5.43852 2.6965 5.43884 2.48137C5.44008 1.11293 4.32076 0.00185084 2.93734 1.60552e-06C1.55455 -0.00153942 0.43149 1.10646 0.429933 2.4752C0.428376 3.84395 1.54769 4.95503 2.93111 4.95657C3.38177 4.95719 3.7991 4.83051 4.16473 4.62463L11.9629 10.6282C11.2998 11.6188 10.9112 12.8053 10.9112 14.0829C10.9112 15.4202 11.3381 16.6573 12.0594 17.6747L9.68813 20.0217C9.50065 19.9659 9.30631 19.9271 9.10013 19.9271C7.96369 19.9271 7.04213 20.8387 7.04213 21.9634C7.04213 23.0883 7.96369 24 9.10013 24C10.2369 24 11.1581 23.0883 11.1581 21.9634C11.1581 21.76 11.1189 21.5673 11.0625 21.3818L13.4083 19.0604C14.4731 19.8645 15.7992 20.3478 17.2421 20.3478C20.7387 20.3478 23.5728 17.5428 23.5728 14.0829C23.5728 10.9506 21.2476 8.36286 18.2138 7.89901Z" fill="#FF7A59" />
  </svg>;

export const ChromeLogo = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" height="24" width="24">
    <defs>
      <linearGradient id="a" x1="3.2173" y1="15" x2="44.7812" y2="15" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#d93025" />
        <stop offset="1" stop-color="#ea4335" />
      </linearGradient>
      <linearGradient id="b" x1="20.7219" y1="47.6791" x2="41.5039" y2="11.6837" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#fcc934" />
        <stop offset="1" stop-color="#fbbc04" />
      </linearGradient>
      <linearGradient id="c" x1="26.5981" y1="46.5015" x2="5.8161" y2="10.506" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#1e8e3e" />
        <stop offset="1" stop-color="#34a853" />
      </linearGradient>
    </defs>
    <circle cx="24" cy="23.9947" r="12" fill="#fff" />
    <path d="M3.2154,36A24,24,0,1,0,12,3.2154,24,24,0,0,0,3.2154,36ZM34.3923,18A12,12,0,1,1,18,13.6077,12,12,0,0,1,34.3923,18Z" fill="none" />
    <path d="M24,12H44.7812a23.9939,23.9939,0,0,0-41.5639.0029L13.6079,30l.0093-.0024A11.9852,11.9852,0,0,1,24,12Z" fill="url(#a)" />
    <circle cx="24" cy="24" r="9.5" fill="#1a73e8" />
    <path d="M34.3913,30.0029,24.0007,48A23.994,23.994,0,0,0,44.78,12.0031H23.9989l-.0025.0093A11.985,11.985,0,0,1,34.3913,30.0029Z" fill="url(#b)" />
    <path d="M13.6086,30.0031,3.218,12.006A23.994,23.994,0,0,0,24.0025,48L34.3931,30.0029l-.0067-.0068a11.9852,11.9852,0,0,1-20.7778.007Z" fill="url(#c)" />
  </svg>;

<img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f990892daf71c67b7ff98ea46770ad9e" data-og-width="1280" width="1280" data-og-height="800" height="800" data-path="images/reference/browser-extension/hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b91d69edbe4322fc83db42c308e0dc8d 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d8c4a9feac84738886f169e94e685751 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=031efba30ac7e556c2e3023805ee6f76 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e9c310c8485d8dab977114fe1992b7f1 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b8dffbb42e6a4d75406498a4bfa92c46 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/hero.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b434d4053440f61e80d2eaaad64f6bd2 2500w" />

Unify offers a native Chrome extension.
Some notable features of the extension include the ability to:

* View details about any Company or Person in your Unify instance
* Enroll People into Sequences
* Add Companies and People to Plays
* Add People to Unify through enrichment
* Manually add new Companies and People to Unify

## Installation

<Card title="Install Unify on the Chrome Web Store" icon={<ChromeLogo />} href="https://chromewebstore.google.com/detail/unify/badmdkkfomlfkcbjegcfjaoeegifdbmm" arrow="true" />

## Usage

The extension can be used anywhere on the web. Let's explore a few examples:

<CardGroup cols={2}>
  <Card title="The web" icon="globe" href="/reference/browser-extension/web">
    Lookup Companies in Unify and add them to Plays as soon as you discover them
    on the web.
  </Card>

  <Card title="Salesforce" icon={<SalesforceLogo />} href="/reference/browser-extension/salesforce">
    Surface the corresponding Company or Person in Unify for Accounts, Contacts,
    & Leads in Salesforce.
  </Card>

  <Card title="HubSpot" icon={<HubspotLogo />} href="/reference/browser-extension/hubspot">
    Surface the corresponding Company or Person in Unify for Companies &
    Contacts in HubSpot.
  </Card>
</CardGroup>


# Salesforce
Source: https://docs.unifygtm.com/reference/browser-extension/salesforce

Run the Unify Chrome extension in Salesforce.

While viewing Accounts, Contacts & Leads in Salesforce, the extension will
automatically surface the corresponding Companies and People in Unify.

## Salesforce Account Page

From this view, you can view People in your Unify instance who work at this Company (and add
them to a Sequence) or instantly add this Company to a Play of your choosing.

<Frame caption="When viewing an Account in Salesforce, the extension will surface the corresponding Company in Unify.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b549be87de77a06da1646f8db2b0b8ae" data-og-width="2018" width="2018" data-og-height="1808" height="1808" data-path="images/reference/browser-extension/salesforce-company.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5cfb10cbfa6f1c2b0111ebe0c8b63323 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f1192fd488f3c1ecc2f485598e99816a 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ba2fe7519e5e2619fc31724d6f2efd53 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9052f15cf7df7fa4299d6596018fad90 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f5d18433fc4e4c32fb9101e7fa40deea 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-company.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f37f6193c22f425ce6f2773f81793f1c 2500w" />
</Frame>

## Salesforce Contact & Lead Pages

From this view, you can check if this Person is currently enrolled in a Unify Sequence.
If they are not already enrolled, you can enroll them from here using any mailbox or
mailbox group in Unify. Additionally, you can instantly add this Person to any of the
Plays you’ve built. See more info on building Plays in Unify [here](/reference/plays/overview).

<Frame caption="When viewing a Contact or Lead in Salesforce, the extension will surface the corresponding Person in Unify.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=22335837807ff06f23462713530175f9" data-og-width="2018" width="2018" data-og-height="1802" height="1802" data-path="images/reference/browser-extension/salesforce-person.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b25f8d960ebbc2884c2c12b5d3ea639d 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f261774bed909f1a01a0d727ff1033ca 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=41d09abc153f8a2893f2aa6d4f6a53e1 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=291c8b83a6d952e29ba094180a643f3d 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6b2219e4cf00cabd4bb73cf98047ff27 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/salesforce-person.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5ee7ccd3d8fadd0e29a0e74b60017d39 2500w" />
</Frame>


# Browsing the Web
Source: https://docs.unifygtm.com/reference/browser-extension/web

Run the Unify Chrome extension on other websites.

The extension can surface relevant information while browsing the web on
other sites, too. When you view a website with a domain that matches one
of the Companies in your Unify instance, the extension will automatically
surface details about that Company.

<Frame caption="For example, when viewing https://unifygtm.com you might see details about the company Unify.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7a32d999a9c0434326a37b95d1a4f8dd" data-og-width="2426" width="2426" data-og-height="1802" height="1802" data-path="images/reference/browser-extension/web-company.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=32a5c1b870c2c90a76ed0541c587e91a 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7a01a6a183ca76037b6b9ac3b20cc346 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=09cfcb570278bc68b48de463714cef6d 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=11140a9a5771e95d461bcd21b762b1de 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2eb3fa517c660e9993caa0e88ebe64cc 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=48707c50fc844cf344ef6311abb7cd30 2500w" />
</Frame>

<br />

<Frame caption="Or when viewing https://cursor.com you might see details about the company Cursor.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9e76485b5b13d7f459716cd56133c29a" data-og-width="2422" width="2422" data-og-height="1806" height="1806" data-path="images/reference/browser-extension/web-company-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=3edc566f8a9d554f11297f6d9d629c12 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c4fe39c6f2eac6c28371bdfdc56faf52 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=00d33225aebe891753c1590561d94981 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fbbf5ce53fea5cc8b19c788869d2e48f 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2ca457be5f12037945fcfbc80294911 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/browser-extension/web-company-2.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=db6ad94e67a2114ef3a6105410b3665c 2500w" />
</Frame>


# 6sense Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/6sense

Use your existing subscription to identify website visitors.

# Overview

Unify integrates with 6sense in two ways:

* If you already have a 6sense subscription, you can connect it to Unify by
  providing your API key to identify website visitors.
* [Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
  identifies website visitors out of the box and is powered by 6sense as well as
  other providers.

Unify uses 6sense along with various other providers to identify website
visitors. If you already have a 6sense subscription, you can connect it to Unify
by providing your API key.

# Setup

To connect your existing 6sense subscription to Unify, simply navigate to
[Settings -> Integrations -> 6sense](https://app.unifygtm.com/dashboard/settings/integrations/6sense)
and enter your API key. Unify will start using your 6sense account to identify
website visitors.

<Note>
  Some customers do not have their 6sense API token enabled by default. If you
  don't see website visitors being identified soon after entering your API key and
  setting up the website tag, this might be the case for you.

  You can reach out to [support@6sense.com](mailto:support@6sense.com) or your dedicated CSM with the following
  message:

  > Hi there,
  >
  > We need an API token to hit the reveal ([https://epsilon.6sense.com/v3/company/details](https://epsilon.6sense.com/v3/company/details)) API in a server to server (not from the browser) mode.
  >
  > Could you please provide the API key?
  >
  > Thanks,

  They should be able to enable access for you.
</Note>


# Clearbit Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/clearbit

Use your existing subscription to identify website visitors.

# Overview

Unify integrates with Clearbit in two ways:

* If you already have a Clearbit subscription, you can connect it to Unify by
  providing your API key to identify website visitors.
* [Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
  identifies website visitors out of the box and is powered by Clearbit as well
  as other providers.

Unify uses Clearbit along with various other providers to identify website
visitors. If you already have a Clearbit subscription, you can connect it to
Unify by providing your API key.

# Setup

To connect your existing Clearbit subscription to Unify, simply navigate to
[Settings -> Integrations -> Clearbit](https://app.unifygtm.com/dashboard/settings/integrations/clearbit)
and enter your API key. Unify will start using your Clearbit account to identify
website visitors.


# Demandbase Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/demandbase

Identify website visitors with Demandbase and other providers.

# Overview

Unify provides out-of-the-box website visitor identification Demandbase and
other providers. To get started, simply enable [Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
in your settings.

Once connected, Unify will automatically begin identifying website visitors
using Demandbase and other data sources for maximum coverage. Be sure to set up
the Unify Intent client on your website to start receiving visitors to identify.


# G2 Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/g2

Revealing anonymous visitors on your G2 profile.

# Overview

You can connect your G2 account to Unify to reveal anonymous visitors on your G2
profile, comparison pages, and more. These visitors can then be used to create
Audiences and Plays.

# Setup

To connect your existing G2 subscription to Unify, simply navigate to
[Settings -> Integrations -> G2](https://app.unifygtm.com/dashboard/settings/integrations/g2)
and enter your API token. Your API token can be found [here](https://my.g2.com/)
in the G2 dashboard. Once this is done, Unify will start using your G2 account
to identify visitors.


# Gmail Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/gmail

This guide outlines how start sending and receiving emails via Gmail in Unify.

# Overview

Unify integrates with Gmail in order to send and receive emails in sequences. Once your mailbox is connected, you can start enrolling people in sequences and sending outbound emails.

# Connecting to Gmail

1. Go to [Settings -> Mailboxes](https://app.unifygtm.com/dashboard/settings/deliverability/mailboxes)
   in Unify and select **New Mailbox**

2. After being redirected to Gmail's authorization page, select the mailbox you
   want to connect and choose **Allow** to proceed

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=278eb3ad49eec8f33f35ce81d65636bd" alt="gmail-integration-step-2" data-og-width="1394" width="1394" data-og-height="1740" height="1740" data-path="images/gmail-integration-step-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f760295f9925609fac24dd14d49fe574 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0fd33cfe3fe29b8912dc761cba34cc75 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d4150551b332254712aa9b054cd40c7c 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=be36aaa4ab33afd48b2c0477c8f62aea 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1b1457c43c646a28a9f6d1fafd7ea81c 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/gmail-integration-step-2.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=592be38eb9f0ab9e924b504d1b973eb5 2500w" /></Frame>

3. You will be redirected back to the mailbox settings page, where you can see
   the status of your newly connected mailbox


# Google Tag Manager Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/google-tag-manager

This guide outlines how to install the Unify website tag using Google Tag Manager.

# Overview

Unify provides several different ways to start collecting intent data from your
website. The quickest way to get started is by installing the Unify website tag
directly on your website.

If you're using Google Tag Manager, you can add the website tag as a custom HTML
tag. This allows you to manage all of your scripts in one place and easily
control when and where they are loaded.

# Installation

For instructions, see the [Website Tag](/developers/intent-client/website-tag)
installation guide.


# Configure Default Values
Source: https://docs.unifygtm.com/reference/integrations/hubspot/default-values

Learn how to set default values writing to HubSpot.

# Overview

When Unify creates or updates records in HubSpot, it will populate each HubSpot
property using the value in the corresponding Unify field. However, you can also
specify *default values* to be used as a fallback. This can useful in a few
different scenarios:

1. You may have custom fields in HubSpot that require a value
2. You may want to write a custom value to a field that is not available in the
   field mappings
3. You may want to dynamically set a value in different Plays or Play actions

You can set global default values from [Settings -> Integrations -> HubSpot](https://app.unifygtm.com/dashboard/settings/integrations/hubspot).
These will be used for all writes to HubSpot unless overridden in a Play or by a
field mapping.

<Frame caption="Set global default values on a per-field basis.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aaa689bbc60b7a8d96ef4294044b814a" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/default-values.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f8595b78abe9cec841b9b341cad7b7bc 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=156578b3d0b21623cfccebff86a0c185 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8d2e877576e45a7d3f668f1ab42bab0c 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=533989b50347e9e6cd3dbcf537090c70 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=40e26b62cec9048074a62941e9b91a8c 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b1a95246e5eb7557efde6323b13cfaf8 2500w" />
</Frame>

To learn how to set default values at the Play level instead, see the [Sync to HubSpot](/reference/plays/actions#sync-to-hubspot)
action reference.


# Field Mappings
Source: https://docs.unifygtm.com/reference/integrations/hubspot/field-mappings

Understand how to configure and use HubSpot field mappings in Unify.

# Overview

Unify can sync data between HubSpot objects and Unify objects. However, the
exact fields in HubSpot differ from Unify, so Unify needs to understand how to
sync data between the two systems. This is done using *field mappings*.

# Setup

### Change field mappings

When you first connect your HubSpot instance, Unify will automatically prepare
the field mappings for you. If you use any custom properties in place of
default HubSpot properties, you may want to update the mappings before Unify
starts syncing data.

In the [HubSpot integration settings](https://app.unifygtm.com/dashboard/settings/integrations/hubspot),
look for the **Company**, **Person**, and **Email Message** field mappings at
the bottom of the page. Select one to view and edit the field configuration.

<Frame caption="Customize which fields are synced to and from HubSpot.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ac67ac0a544b106dc1dc157b1c65f21e" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/company-field-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e0e5a21f398d430674ff089354662e25 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1dd74350c864f98fa2eecbb025a130bd 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2564067d541a2e16a8af2b797d3ebb4 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=95da33ae2b2935818aaa2e745bf8b7a4 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ba22a3e6a3cdba653fe401c8dd386aea 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=692ab57c15caa7b4dc11082a3c919650 2500w" />
</Frame>

You can return to update these mappings any time in the future, so you don't
need to worry about getting them perfect right off the bat!

### (Optional) Create custom properties

You can write values to default properties and custom properties. In order to
write to custom properties, they must already exist in HubSpot.

While some of the fields Unify can write exist as standard properties in
HubSpot, many of them do not. In particular, Unify-specific fields (like the
name of the Sequence a person was enrolled in) do not exist in HubSpot by
default. In order to write these values to HubSpot, you will need to create
custom properties before mapping them.

<Note>
  Here's what the process looks like for adding **Contact** properties. First, in
  HubSpot, navigate to **CRM -> Contacts**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bcc0b056e9ca14a99f444d9de2ae07f7" alt="HubSpot Home" data-og-width="3626" width="3626" data-og-height="1690" height="1690" data-path="images/hubspot-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=82a9120918278b8e6350bf7da19f3475 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e657714152d25702d61d971c63e492c1 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=edb8c0622a7233009af44f28f6b1e04f 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=52f7714574c3cf485621d2f2864a4e83 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d177efe241afc4b91b6cf6494c0c0989 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-7.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=936f43f82639054fcab46b88ed2e89eb 2500w" /></Frame>

  Select **Actions -> Edit properties**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ce62a906f1697fa03aa461fbf8352de9" alt="HubSpot Contacts" data-og-width="3634" width="3634" data-og-height="1688" height="1688" data-path="images/hubspot-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=16f5d32d0827f6fb0bedede76ccd262c 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=74c1d1cf0af3adedbb62fba8a60fa843 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=67a3420481cf392ed34e6190e73873c0 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d3912c8a76ec048296af86c08d2b3f7f 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=42af62484900fb5da5b08b73670ce5eb 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-8.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fde74d0f80dfccc586c127374148936c 2500w" /></Frame>

  Navigate to **Groups -> Create group**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b219405e8e5bc293f4e443a9387628bd" alt="HubSpot Contact Property Groups" data-og-width="3628" width="3628" data-og-height="1686" height="1686" data-path="images/hubspot-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=98e87d67d6a782471fb0e2ea9863c334 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5285e69071a189046008b3cd1898b084 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d2fffbed30b7f26fe22b2a6e95a7458a 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=29e326dd7fca3f1dbbadb64a3a3d07eb 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=620a28ca8b6c4079a0a1ee78d047a038 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-9.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5fbc70114fdcf74ae29bce180d0ae375 2500w" /></Frame>

  Type in the name of the group (recommended title "Unify information") and click
  **Create**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=df07eed5693cf547cebc6a00c84d45e0" alt="HubSpot Contact Create Property Group" data-og-width="3626" width="3626" data-og-height="1678" height="1678" data-path="images/hubspot-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2b055d160606f353ba121c583faf56ff 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=098fd2f6be5d78c49a1f24be4374b635 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2008ceeb0d75c6ad2428e3761a51b39b 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9bda2be9897274817bf910a2a9dda4da 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0837ff32041c5c06543a023520fc3624 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-10.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2c7d01028d50244fb4cfd43c90f91401 2500w" /></Frame>

  Navigate to **Properties -> Create property**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=829423a8d2b2402434a2db732ac9118f" alt="HubSpot Contact Properties" data-og-width="3628" width="3628" data-og-height="1686" height="1686" data-path="images/hubspot-11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=00564d38f28cd6a719d1e7ff4600f7ee 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1d30aa1d153d152c5b23d56adb27894c 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e64fdba91fe6bc3a8b4644e47492a496 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=864dfbde6ac3cdc2bff508d9c6cc1500 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c0b8a3309db92d23b7987a12e374675b 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-11.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e55593cb76d3c4480e77d3e96fa7f26f 2500w" /></Frame>

  When editing the property details, make sure the **Object type** is set properly
  (in this case, to **Contact**) and the **Group** is set to the group you
  created earlier. You can fill in the **Label** and **Description** as desired.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=176a486a4bc99e29f4b12f1b864418e7" alt="HubSpot Contact Create Property" data-og-width="3630" width="3630" data-og-height="1764" height="1764" data-path="images/hubspot-12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5406599c54ae95bc1f0183c6cd7cc63b 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bff618afc94938ace22c020cd86ac483 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8b240ce98e6293570259a67d461334bc 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=70a13b2233b5fd7568d8d5b7e4cdf28e 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9281935ca33a61c437c6149e66a4b65e 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-12.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=65169ae5b6fb350ea4c400003d922606 2500w" /></Frame>

  Lastly, select the **Field type** and click **Create**.

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=48ac7a78694a745bbfbe0d04cdc75077" alt="HubSpot Contact Select Property Type" data-og-width="3628" width="3628" data-og-height="1766" height="1766" data-path="images/hubspot-13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0eb6e01b65c82d53b71a5c98d1551ef7 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=3d78ee498385afd451dcb0184caabf76 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aaf15f9d8f6c7c9d0e2479792a757747 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=17179480eb1fbcb2c7efc868d5545433 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6aac265a632464b4152e4349a49a91dc 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-13.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aa129f35c0d782c0dea63dce3d53663c 2500w" /></Frame>

  This is what your **Contact** properties filtered to your new group might look
  like after you've added them:

  <Frame>  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ab7f38574fd82ed1a8015ebedfba3c72" alt="HubSpot Contact New Properties" data-og-width="3626" width="3626" data-og-height="1762" height="1762" data-path="images/hubspot-14.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a0263c59aeee4984f01a6f1f24d38c39 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=95124d0a0b28d9d27df5d17004f50bb7 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4b7436649d97bca731c47709d46ee06a 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=010a11b95995e0d3a23ca840889adafc 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7e848f087f2e6ac2838881ca4d3b3b05 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-14.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=93fa187b24b20474165bfe69ee68b495 2500w" /></Frame>

  You can then repeat this process for **Company** properties as well.
</Note>

# Available fields

Below is a full list of the values that can be configured in the field mappings
for each object type. Some of these are standard properties, while others
provide Unify-specific information, such as the name of the Sequence that a
person was enrolled in.

<AccordionGroup>
  <Accordion title="Companies">
    | Field                                  | Description                                                                                                                                                       |
    | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Company Name**<br />*Text*           | Name of the company.                                                                                                                                              |
    | **Domain**<br />*Text*                 | Web domain of the company.                                                                                                                                        |
    | **Address**<br />*Text*                | Physical address of the company.                                                                                                                                  |
    | **State or Province**<br />*Text*      | State, province, region, or territory the company is located in.                                                                                                  |
    | **Country**<br />*Country*             | Country the address is located in.                                                                                                                                |
    | **City**<br />*Text*                   | City, town, or village the company is located in.                                                                                                                 |
    | **Postal Code**<br />*Text*            | Postal code for the company.                                                                                                                                      |
    | **Time Zone**<br />*Text*              | Time zone the company is located in.                                                                                                                              |
    | **Corporate Phone**<br />*Text*        | Corporate phone number for the company.                                                                                                                           |
    | **Status**<br />*Text*                 | Status of the company in the sales lifecycle.                                                                                                                     |
    | **LinkedIn URL**<br />*Text*           | URL to the company's LinkedIn page.                                                                                                                               |
    | **Description**<br />*Text*            | Description of the company.                                                                                                                                       |
    | **Do Not Contact**<br />*Boolean*      | Flag indicating that the company should not be contacted.                                                                                                         |
    | **Founded**<br />*Date*                | Date the company was founded.                                                                                                                                     |
    | **Industry**<br />*Text*               | Industry the company is in.                                                                                                                                       |
    | **Employee Count**<br />*Number*       | Approximate number of employees at the company.                                                                                                                   |
    | **Revenue**<br />*Number*              | Estimated annual revenue of the company.                                                                                                                          |
    | **Revenue Currency**<br />*Text*       | Three-letter ISO 4217 code indicating the revenue value currency type.                                                                                            |
    | **Account Source**<br />*Text*         | Channel this Company record was sourced from.                                                                                                                     |
    | **Unify Metadata**<br />*Text*         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date* | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text* | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Intent Level**<br />*Text*     | Intent level of the company (either **High**, **Medium**, **Low**, or **None**).                                                                                  |
  </Accordion>

  <Accordion title="People">
    | Field                                                  | Description                                                                                                                                                       |
    | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Email**<br />*Text*                                  | Contact email address.                                                                                                                                            |
    | **Address**<br />*Text*                                | Physical address of the person.                                                                                                                                   |
    | **Country**<br />*Country*                             | Country the address is located in.                                                                                                                                |
    | **Postal Code**<br />*Text*                            | Postal code for the person.                                                                                                                                       |
    | **Email Opt Out**<br />*Boolean*                       | Indicates whether the person has opted out of receiving emails.                                                                                                   |
    | **Status**<br />*Text*                                 | Status of the person in the sales lifecycle.                                                                                                                      |
    | **First Name**<br />*Text*                             | First name of the contact.                                                                                                                                        |
    | **First Name Suffix**<br />*Text*                      | Suffix of the first name of the contact.                                                                                                                          |
    | **Last Name**<br />*Text*                              | Last name of the contact.                                                                                                                                         |
    | **Title**<br />*Text*                                  | Job title or position of the contact.                                                                                                                             |
    | **Mobile Phone**<br />*Text*                           | Mobile phone number of the contact.                                                                                                                               |
    | **Work Phone**<br />*Text*                             | Work phone number of the contact.                                                                                                                                 |
    | **Corporate Phone**<br />*Text*                        | Corporate phone number of the contact.                                                                                                                            |
    | **LinkedIn URL**<br />*Text*                           | LinkedIn profile URL of the contact.                                                                                                                              |
    | **Do Not Call**<br />*Boolean*                         | Indicates whether the contact should receive phone calls or not.                                                                                                  |
    | **Do Not Email**<br />*Boolean*                        | Indicates whether the contact should receive emails or not.                                                                                                       |
    | **EU Resident**<br />*Boolean*                         | Indicates whether the contact is a resident of the European Union.                                                                                                |
    | **Lead Source**<br />*Text*                            | Channel this Person record was sourced from.                                                                                                                      |
    | **Last Activity Date**<br />*Date*                     | Date of the last activity or engagement with the contact.                                                                                                         |
    | **Unify Metadata**<br />*Text*                         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*                       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*                       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date*                 | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*                     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*                  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text*                 | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Most Recent Play At**<br />*Date*              | Date and time the most recent Unify Play ran on this record.                                                                                                      |
    | **Unify Initial Sequence**<br />*Text*                 | Name of the first Unify Sequence this person was enrolled in.                                                                                                     |
    | **Unify Initial Sequence At**<br />*Date*              | Date and time this person was first enrolled in a Unify Sequence.                                                                                                 |
    | **Unify Initial Sequence Step At**<br />*Date*         | Date and time this person first completed a step in a Unify Sequence.                                                                                             |
    | **Unify Most Recent Sequence**<br />*Text*             | Name of the most recent Unify Sequence this person was enrolled in.                                                                                               |
    | **Unify Most Recent Sequence At**<br />*Date*          | Date and time this person was most recently enrolled in a Unify Sequence.                                                                                         |
    | **Unify Most Recent Sequence Step At**<br />*Date*     | Date and time this person most recently completed a step in a Unify Sequence.                                                                                     |
    | **Unify Most Recent Sequence Status**<br />*Text*      | Status of the most recent enrollment for this person. The statuses shown on enrollments in Unify are the same values that will be written to HubSpot.             |
    | **Unify Initial Reply Classification**<br />*Text*     | High-level classification of the initial reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".          |
    | **Unify Most Recent Reply Classification**<br />*Text* | High-level classification of the most recent reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".      |
    | **Unify Initial Reply Tags**<br />*Text*               | Comma-separated list of classification tags of the initial reply received from a person. For example, "Ready to meet, Needs more information".                    |
    | **Unify Most Recent Reply Tags**<br />*Text*           | Comma-separated list of classification tags of the most recent reply received from a person. For example, "Ready to meet, Needs more information".                |
  </Accordion>

  <Accordion title="Email Messages">
    | Field                                | Description                                                    |
    | ------------------------------------ | -------------------------------------------------------------- |
    | **Universal Message ID**<br />*Text* | Globally unique identifier that exists for all email messages. |
    | **Subject**<br />*Text*              | Subject of the email.                                          |
    | **HTML Content**<br />*Text*         | Body of the email.                                             |
    | **Sent At**<br />*Date*              | Date and time the email was sent.                              |
  </Accordion>
</AccordionGroup>


# HubSpot Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/hubspot/overview

This guide outlines how to connect your HubSpot CRM to Unify.

## Overview

In just a few steps, you can connect your HubSpot CRM to Unify and start syncing
data bidirectionally. This unlocks a few key benefits when using Unify:

1. HubSpot records can be used to [construct exclusions](/tutorials/how-to-create-an-exclusion)
   that prevent Unify from engaging with specific people or companies. For
   example, you can create an exclusion for all current customers or deals in
   progress.
2. You can create Plays that are triggered by HubSpot records. This allows you
   to run a Play based on a specific event or criteria captured within HubSpot.
3. Unify can write data back to HubSpot so that you can maintain a source of
   truth in your CRM and respect rules of engagement in other tools or business
   processes.

Unify's integration with HubSpot is designed from the ground up to prevent many
common pitfalls, including overwriting existing data or creating duplicate
records.

# Setup

<Steps titleSize="h3">
  <Step title="Connect HubSpot instance">
    Navigate to [Settings -> HubSpot](https://app.unifygtm.com/dashboard/settings/integrations/hubspot)
    and select **Connect**. You will be redirected to the HubSpot authentication
    page where you can sign in and authorize Unify to access HubSpot data.

    <Frame caption="This screen will appear before you have connected a HubSpot instance.">
      <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fab08b9de9f6effa1feec3ac5d37c20c" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/hubspot/connect-hubspot-instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=74fe56d64c356735f006d74f02341e5d 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=759c9c6aa691e3ff5e18d9ba2715ff64 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=73c7dd504208c616607554527b0cfb46 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cfa8c4bbba9b44189bdb1ff3dcdaabff 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=da44d2a19b3f5997ab56aebd1145b6e6 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connect-hubspot-instance.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f5b0b87b604717062cddf81ee62794ab 2500w" />
    </Frame>

    <Frame caption="Once a connected, you will see the settings available for your HubSpot connection.">
      <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a665a6aa999f0b914962729618cda869" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/hubspot/connected-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=07148bcacff0730a99c94f61033a5ea1 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=79cb3047c219a73c171dce3f5aca6de4 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f130d31c3505f2924cb772e46721a5dc 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=dff2ac3dd5b573eed0b2e20b310c67a4 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d5beed7eb9b8180d96dfbe6f06d76eb3 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/connected-settings.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ed6b4df0f298da9a2d42247742c002f3 2500w" />
    </Frame>
  </Step>

  <Step title="Create field mappings">
    Unify provides granular control over which HubSpot properties map to which
    Unify fields. For each object, select **Create Mapping** and update any
    fields you wish to customize.

    In most cases, the default options will be a good starting point. You can
    always return to change these mappings in the future.

    <Frame caption="The field mappings page lets you customize which fields Unify can read and write.">
      <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ac67ac0a544b106dc1dc157b1c65f21e" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/company-field-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e0e5a21f398d430674ff089354662e25 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1dd74350c864f98fa2eecbb025a130bd 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2564067d541a2e16a8af2b797d3ebb4 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=95da33ae2b2935818aaa2e745bf8b7a4 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ba22a3e6a3cdba653fe401c8dd386aea 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/company-field-mapping.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=692ab57c15caa7b4dc11082a3c919650 2500w" />
    </Frame>

    See [Field Mappings](/reference/integrations/hubspot/field-mappings) for details on
    how field mappings work and the available options.
  </Step>

  <Step title="Enable syncs">
    Once you're satisfied with your integration settings and field mappings, you
    can begin syncing data into Unify by selecting **Resume**. If at any point
    you want to pause syncs again, you can return to this page and select
    **Pause**.

    To enable Unify to write data back to HubSpot, activate the toggle next to
    **Enable writing to HubSpot**. This will allow Unify to sync records back to
    HubSpot.

    <Frame caption="The HubSpot integration settings page after setup is complete.">
      <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=151ad31a63ce64dbd923ecb70cbac758" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/hubspot-integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cf404f015aeb132df53c8021652eb947 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8a9ffa92b2cf8f32f87e54a9c9151d67 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=3a4e428ba2be268866670b5be3d8b77a 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2feb9de8cec04a95bb48c0966f1af72f 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=134746ef819f0f259ae76404a2ce32a6 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/hubspot-integration-settings.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ebb7e953caec8d9034be01ee10193ccb 2500w" />
    </Frame>
  </Step>
</Steps>

## Additional HubSpot resources

<CardGroup cols={2}>
  <Card icon="arrow-right-arrow-left" title="Field Mappings" href="/reference/integrations/hubspot/field-mappings">
    Configure mappings between Unify fields and HubSpot properties.
  </Card>

  <Card icon="pen-to-square" title="Configure Default Values" href="/reference/integrations/hubspot/default-values">
    Specify default values that should be used when writing to HubSpot.
  </Card>
</CardGroup>


# Property Options
Source: https://docs.unifygtm.com/reference/integrations/hubspot/property-options

Find the options for a property in HubSpot.

# Explanation

Properties in HubSpot have a different name displayed in the UI than the value
used at the API level. For most properties, the dropdown options you see in the
UI will be the same as the values you see in Unify.

However, certain properties in HubSpot have options which Unify cannot access.
At the moment, this is a known HubSpot limitation. The steps outlined here can
help to work around the issue.

## Workaround

In order to support using these options for filtering in audiences and
exclusions, you can perform the following steps. This article uses the
**Lifecycle Stage** property on **Company** as an example, but the same steps
should work for other properties and objects.

In HubSpot, navigate to **CRM -> Companies** and select **Actions -> Edit properties**.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1921ca6a6c8d55cbe9d43acfda23c093" alt="Properties" data-og-width="3298" width="3298" data-og-height="1714" height="1714" data-path="images/hubspot-15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cb84e181083f2a5aa6e1d050b061f50c 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=34fd18fd3ff5007da248bb9a7917f662 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b7af8a6eaa29372d0bc23cc0357af5eb 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=55d3b96a59c51c3589af704058b58996 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e037c750bd4283be6e54094508de2015 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=55f96b586d13b40ba54922318ac7b127 2500w" /></Frame>

Search for the property by its name (in this case, **Lifecycle Stage**) and
select the property.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=519d64e0d1ec74d5a7d96e410ba61329" alt="Properties" data-og-width="3302" width="3302" data-og-height="1714" height="1714" data-path="images/hubspot-16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=136d46eea58da98c324d552bebfe8696 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e17ad0bb1f63e7b81e927f77d51f80fb 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b9b5a6678ff7d622bc2c46b6604e4543 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1aa4aedb46d2347fdfb91a45c702c9bb 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=272408e3a45c8334a94692c47a1b5d71 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5b33588249be5ece6a58f94f036cce7b 2500w" /></Frame>

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0d963831c638fb28c9225523fb8c5152" alt="Lifecycle Stage" data-og-width="3298" width="3298" data-og-height="1792" height="1792" data-path="images/hubspot-17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1b9529099ee842f5a418e94457890137 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=97a854999d38b97118510c700404474b 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b2608ac2ef23901d301d3346f471dbc2 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4f464626c9348d5455a68d895317ddbe 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cea16da7f9e709328f9bbf75596b6f2b 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=908021c15ba68f3bdd212fa05aee1974 2500w" /></Frame>

Navigate to **Field type**. You will see a list of options, with **LABEL** and
**INTERNAL NAME** values alongside the number of records that have that value.
You may want to copy these values to a secure separate location for easy future
reference. If you wish to filter records in Unify to a specific **LABEL** value,
you can do so by using the corresponding **INTERNAL NAME** value.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7528480a7063625b527e922cc47e7cdc" alt="Property Options" data-og-width="3298" width="3298" data-og-height="1786" height="1786" data-path="images/hubspot-18.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=071d437228946b1005d30fba272c56df 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ee6268904afc051100a16e51e37ddb7d 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fa926371f1a86f89e5a62da4f679a314 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b9befe41a4c33178cd771f1fdaae0faa 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ae5eb877ea8b9fbd522428c47700fcda 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=935e6d8848a6824f39a35b887b79c9ad 2500w" /></Frame>

Here's what that looks like in Unify for the **LABEL** value "Lead" and
therefore **INTERNAL NAME** value "lead":

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d215e8246b62ba7121cd5b390cb3634b" alt="Filtering in Unify" data-og-width="2162" width="2162" data-og-height="1344" height="1344" data-path="images/hubspot-19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fc07816aded5d8d2282800d8df4afbbd 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e6e3fd5ca0ea1a83bbb3aee4c69a12af 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=813d146fbd8b2f32a2e0eb79299246a1 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=82a9f4aab37b80ebc14935910b3084d5 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=68951146227379c3d98fe99bc6e29ac4 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a4c07b50efe8e6f61b5591c7d433bdfe 2500w" /></Frame>


# Running Call Campaigns with Nooks
Source: https://docs.unifygtm.com/reference/integrations/nooks/call-campaigns

Launch and manage effective call campaigns using Nooks with your CRM integration.

## Prerequisites

Before starting your call campaign, ensure you have:

* Completed your CRM setup ([HubSpot](/reference/integrations/nooks/hubspot-setup) or [Salesforce](/reference/integrations/nooks/salesforce-setup))

## Setting Up Your Call Campaign

### 1. Create Your Sequence

Create a Unify Sequence that includes manual phone call steps. This will generate the call tasks that sync to your CRM and feed into Nooks. Learn more in our [Sequences guide](/reference/sequences/manual-steps#phone-call-steps).

### 2. Monitor the Sync

Sequence enrollments will appear in your CRM within 30 minutes of being created in Unify. These tasks will automatically be available in Nooks when you reset your call list.

### 3. Set Up Your Call Session

In Nooks, follow these steps to prepare your calling session:

1. Login to Nooks

2. Select your call sequence

### 4. Start Calling

Begin your call campaign! As you complete calls, results will automatically sync back to both your CRM and Unify, keeping all your systems up to date.

<Note>
  Need additional help? Contact our support team or visit the [Nooks documentation](https://support.devrev.ai/nooks/directories) for more detailed troubleshooting guides.
</Note>

***

That's it! By following these steps, your team will run faster, more productive call campaigns with seamless integration between your CRM, Unify, and Nooks.


# Nooks HubSpot Setup
Source: https://docs.unifygtm.com/reference/integrations/nooks/hubspot-setup

Configure Nooks integration with HubSpot for seamless call task management.

# HubSpot Setup for Nooks Integration

This guide walks you through how to set up the Nooks integration with HubSpot to synchronize call tasks.

## Prerequisites

Before you begin, make sure you have:

* Admin access to your HubSpot account
* An active Nooks subscription

## Setup Steps

1. **Admin**: Map users to their Hubspot profiles. Make sure your team has the proper permissions in your Hubspot to be able to create sequences, tasks or lists for themselves (If managers/admins are creating sequences and lists, this can be disregarded)
2. Create or Edit your Call Outcomes
3. Set up automation rules and/or filters to ensure proper hygiene and activities against your contacts.

For detailed step-by-step instructions, see [setup guide](https://support.devrev.ai/nooks/article/ART-120-getting-started-with-hubspot).

## Next Steps

With your HubSpot integration configured and Nooks connected, you're ready to [launch your first call campaign](/reference/integrations/nooks/call-campaigns)!


# Nooks Integration Overview
Source: https://docs.unifygtm.com/reference/integrations/nooks/overview

Learn how to integrate Nooks with your CRM for seamless call campaign management.

## What You'll Need

Before setting up the Nooks integration, ensure you have:

* Admin access to your CRM (HubSpot or Salesforce)
* An active Nooks account

## Integration Options

Choose your CRM to get started:

<Card title="HubSpot Setup" icon="hubspot" href="/reference/integrations/nooks/hubspot-setup">
  Configure Nooks with HubSpot for call task synchronization
</Card>

<Card title="Salesforce Setup" icon="salesforce" href="/reference/integrations/nooks/salesforce-setup">
  Set up call reports and connect Nooks with Salesforce
</Card>

## Getting Started

1. **Choose your CRM**: Follow the setup guide for either HubSpot or Salesforce
2. **Configure Integration**: Setup call tasks to sync to CRM
3. **Launch Campaigns**: Start running organized, efficient call campaigns

Ready to get started? Select your CRM platform above to begin the setup process.


# Nooks Salesforce Setup
Source: https://docs.unifygtm.com/reference/integrations/nooks/salesforce-setup

Configure Nooks integration with Salesforce for call task synchronization.

# Salesforce Setup for Nooks Integration

This guide walks you through the steps required to set up call tasks in Salesforce and configure the Nooks integration for seamless call campaign management.

## Overview

You can bidirectionally sync your call tasks between Unify and Nooks using a Salesforce report. The instructions below will help you build a report to successfully set up the sync.

## Salesforce Report Setup

### Call Report Setup in Salesforce

To create call tasks in Salesforce, set up a new report with the following criteria:

1. Navigate to your Salesforce Reports tab
2. Click **New Report**
3. Configure the report with these settings:
   * **Category**: Activities (Activities with Contacts)
   * **Show Me**: All activities
   * **Date**: All Time
   * **Show**: Open Activities
   * **Show**: Tasks
   * **Assigned**: equals \$USER
   * **Task Subtype**: equals Call

<Note>
  These report filters ensure that each user in Nooks only sees their own open call tasks
</Note>

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5b1e59e21b44231d0bda66e623728092" alt="salesforce-report-filters.png" data-og-width="387" width="387" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-report-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=21a820992314f94b9d74c0f6ac644164 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=edb8a19385ebee1cdaa12b8590126159 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8a237b0702b5356918800df34dbbded2 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8f09aa5bea90a81b3b990c46b143b36b 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5506bbd4c5f3b855c9895e78d56f8e3e 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=26b160ab0db565c745904cd78a7e94e1 2500w" /></Frame>

### Best Practices for Report Columns

We recommend including the following columns in your report for better visibility and alignment with Unify sequences:

1. Click **Customize** on your report
2. Add the following columns:
   * Subject
   * First Name
   * Last Name
   * Unify Sequence

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=b44857af3ebb733b9880615ed3e9176c" alt="salesforce-column-setup.png" data-og-width="418" width="418" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-column-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=d983866fa604a227ce99edafe347acb7 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=cd802fb66106d991db90fc22d74b73d4 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=a9c0f33d842106aa5a84fbb1a78c79c7 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=40d31b55a1d796d926fc7d9e73feecde 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=4ed0c5852f172a55ee57baa895724135 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=0e662e08fd1cd4955ecc3e269252d51a 2500w" /></Frame>

## Nooks Integration Setup

<Info>
  **Sep 2025 Update: Installing Nooks as a Trusted App in Salesforce**

  In September 2025, Salesforce made security changes regarding which apps can be connected to Salesforce (via OAuth) by individual reps. This can impact Nooks users who are connecting to Salesforce for the first time, or reconnecting Salesforce. They might see an "OAuth Error" like this:

  <Frame>  <img src="https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=a1ebaeb24ed30aab2ed88e3efea4bc2c" alt="salesforce-oauth-error.png" data-og-width="764" width="764" data-og-height="788" height="788" data-path="images/reference/integrations/nooks/salesforce-oauth-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=280&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=9bb77abc9abdd32edc2f4c1c62c02581 280w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=560&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=1c47d6180098971aae3ac41f91c06965 560w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=840&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=8009ee2a2b0e524f9c5b25397a5049c9 840w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=1100&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=17ba9540bcebc4f639da37da353da2b7 1100w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=1650&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=d26fd5af55f5e88685cf9c11d85dc3f7 1650w, https://mintcdn.com/unify-19/SMh_isreZvLK6DBw/images/reference/integrations/nooks/salesforce-oauth-error.png?w=2500&fit=max&auto=format&n=SMh_isreZvLK6DBw&q=85&s=0e9207211e926bf376293590b3e69931 2500w" /></Frame>

  Your Salesforce administrator will need to install Nooks as a trusted app in your Salesforce org. For more information, see: [Installing Nooks as a Trusted App in SFDC](https://support.devrev.ai/nooks/article/ART-115-getting-started-with-salesforce-sfdc#Sep%202025%20Update%3A%20Installing%20Nooks%20as%20a%20Trusted%20App%20in%20SFDC).
</Info>

Once your Salesforce report is ready, connect Nooks to Salesforce:

1. Navigate to **Settings** in Nooks
2. Select **Integrations**
3. Select **Connect Salesforce** and authorize the connection
4. Install Nooks as an OAuth app. Nooks should appear as an app in the Salesforce Setup settings in the "Connected Apps OAuth Usage" section. Click "Install".
5. \[Recommended] Configure field mappings to optimize your call tasks:
   * Navigate to **Settings** > **Salesforce** > **Field Mappings**
   * Add your specific SFDC fields such as:
     * Current Unify Sequence
     * Current Unify Play
     * Relevant prospect information for call tasks

<Note>
  You will need admin access to Salesforce to authorize this connection. For more information, see: [Nooks admin setup](https://support.devrev.ai/nooks/article/ART-115-getting-started-with-salesforce-sfdc) or reach our to your CSM.
</Note>

## Next Steps

With your Salesforce integration configured and Nooks connected, you're ready to [launch your first call campaign](/reference/integrations/orum/call-campaigns)!


# Running Call Campaigns with Orum
Source: https://docs.unifygtm.com/reference/integrations/orum/call-campaigns

Launch and manage effective call campaigns using Orum with your CRM integration.

## Prerequisites

Before starting your call campaign, ensure you have:

* Completed your CRM setup ([HubSpot](/reference/integrations/orum/hubspot-setup) or [Salesforce](/reference/integrations/orum/salesforce-setup))

## Setting Up Your Call Campaign

### 1. Create Your Sequence

Create a Unify Sequence that includes manual phone call steps. This will generate the call tasks that sync to your CRM and feed into Orum. Learn more in our [Sequences guide](/reference/sequences/manual-steps#phone-call-steps).

### 2. Monitor the Sync

Sequence enrollments will appear in your CRM within 30 minutes of being created in Unify. These tasks will automatically be available in Orum when you reset your call list.

### 3. Set Up Your Call Session

In Orum, follow these steps to prepare your calling session:

1. **Login with your CRM** to ensure Orum can access your phone call tasks

2. **Select your call list** from the available CRM reports:

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=6537804a69925cfdfb8297a24f12652f" alt="list-selection.png" data-og-width="275" width="275" data-og-height="255" height="255" data-path="images/reference/integrations/orum/list-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5a4951181364f64dce7160ade7754d6b 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=58c0f46ac0f497a2fae80da6101e2072 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=52c5b704a459cff57af4c5560e80edd9 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=de8913e7b986fd3364adf0227319f6d2 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=dcf78d389df1acd5d5d8a00e9f4fe619 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/list-selection.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=75e9d6b90edf22cb1555ca1873c94998 2500w" /></Frame>

3. **Reset your tasks** by clicking the reset button to pull the latest call tasks:

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=4185c92b7d061595370e189f9b9c099a" alt="reset-button.png" data-og-width="504" width="504" data-og-height="103" height="103" data-path="images/reference/integrations/orum/reset-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=b32ef115b0eb20f54dfd793999aa3b0f 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=bd72aee29380ccc1ef7db582ee6ee387 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5cba5ea0684fca710f828ff87d8eb0a4 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=48202f518c7a01aacb500cb7a6f0013f 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=e60e02c25c0b0fe5ac616980330b8dae 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/reset-button.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=35fa74d55ed941f2526cdc2d15bb0a90 2500w" /></Frame>

4. **Configure filters** (optional): If you have multiple call tasks for the same person, uncheck the "Skip duplicate numbers" filter to include all tasks:

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=ff0e271080eb1ef94f0c3bba78b3a05f" alt="skip-duplicate-numbers.png" data-og-width="580" width="580" data-og-height="570" height="570" data-path="images/reference/integrations/orum/skip-duplicate-numbers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=0e261ca72cb3f1c00e57c10a9e5b6563 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5cd48181af5a5353468961b44cb3bdc6 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=6b2160e45f8aad953a5d2a48a5947a07 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=cc698eaa36fa16c4895755b37d58c86e 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=3bfd1ac94e053bb6bf687bca08573237 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/skip-duplicate-numbers.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=ea8f1ba5e23dbfd271b882e97eacdbb9 2500w" /></Frame>

### 4. Start Calling

Begin your call campaign! As you complete calls, results will automatically sync back to both your CRM and Unify, keeping all your systems up to date.

<Note>
  Need additional help? Contact our support team or visit the [Orum documentation](https://support.orum.com) for more detailed troubleshooting guides.
</Note>

***

That's it! By following these steps, your team will run faster, more productive call campaigns with seamless integration between your CRM, Unify, and Orum.


# Orum HubSpot Setup
Source: https://docs.unifygtm.com/reference/integrations/orum/hubspot-setup

Configure Orum integration with HubSpot for seamless call task management.

# HubSpot Setup for Orum Integration

This guide walks you through how to set up the Orum integration with HubSpot to synchronize call tasks.

## Prerequisites

Before you begin, make sure you have:

* Admin access to your HubSpot account
* An active Orum subscription

## Setup Steps

1. **Admin Authorization**: Have a HubSpot admin authorize the Orum connection in your HubSpot account
2. **Login**: Login with your HubSpot credentials in Orum to complete the integration

For detailed step-by-step instructions, follow our [interactive setup guide](https://app.tango.us/app/workflow/Connecting-Orum-to-HubSpot-899a4dfbc33b40a9bf6faef1fdb60761).

## Next Steps

With your HubSpot integration configured and Orum connected, you're ready to [launch your first call campaign](/reference/integrations/orum/call-campaigns)!

<Note>
  Need help with the setup? Contact our support team or refer to [Orum's HubSpot documentation](https://support.orum.com/orum/article/ART-449-getting-started-with-hubspot) for additional assistance.
</Note>


# Orum Integration Overview
Source: https://docs.unifygtm.com/reference/integrations/orum/overview

Learn how to integrate Orum with your CRM for seamless call campaign management.

## What You'll Need

Before setting up the Orum integration, ensure you have:

* Admin access to your CRM (HubSpot or Salesforce)
* An active Orum account

## Integration Options

Choose your CRM to get started:

<Card title="HubSpot Setup" icon="hubspot" href="/reference/integrations/orum/hubspot-setup">
  Configure Orum with HubSpot for call task synchronization
</Card>

<Card title="Salesforce Setup" icon="salesforce" href="/reference/integrations/orum/salesforce-setup">
  Set up call reports and connect Orum with Salesforce
</Card>

## Getting Started

1. **Choose your CRM**: Follow the setup guide for either HubSpot or Salesforce
2. **Configure Integration**: Setup call tasks to sync to CRM
3. **Launch Campaigns**: Start running organized, efficient call campaigns

Ready to get started? Select your CRM platform above to begin the setup process.


# Orum Salesforce Setup
Source: https://docs.unifygtm.com/reference/integrations/orum/salesforce-setup

Configure Orum integration with Salesforce for call task synchronization.

# Salesforce Setup for Orum Integration

This guide walks you through the steps required to set up call tasks in Salesforce and configure the Orum integration for seamless call campaign management.

## Overview

You can bidirectionally sync your call tasks between Unify and Orum using a Salesforce report. The instructions below will help you build a report to successfully set up the sync.

## Salesforce Report Setup

### Call Report Setup in Salesforce

To create call tasks in Salesforce, set up a new report with the following criteria:

1. Navigate to your Salesforce Reports tab
2. Click **New Report**
3. Configure the report with these settings:
   * **Category**: Activities (Activities with Contacts)
   * **Show Me**: All activities
   * **Date**: All Time
   * **Show**: Open Activities
   * **Show**: Tasks
   * **Assigned**: equals \$USER
   * **Task Subtype**: equals Call

<Note>
  These report filters ensure that each user in Orum only sees their own open call tasks
</Note>

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5b1e59e21b44231d0bda66e623728092" alt="salesforce-report-filters.png" data-og-width="387" width="387" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-report-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=21a820992314f94b9d74c0f6ac644164 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=edb8a19385ebee1cdaa12b8590126159 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8a237b0702b5356918800df34dbbded2 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=8f09aa5bea90a81b3b990c46b143b36b 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=5506bbd4c5f3b855c9895e78d56f8e3e 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-report-filters.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=26b160ab0db565c745904cd78a7e94e1 2500w" /></Frame>

### Best Practices for Report Columns

We recommend including the following columns in your report for better visibility and alignment with Unify sequences:

1. Click **Customize** on your report
2. Add the following columns:
   * Subject
   * First Name
   * Last Name
   * Unify Sequence

<Frame><img src="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=b44857af3ebb733b9880615ed3e9176c" alt="salesforce-column-setup.png" data-og-width="418" width="418" data-og-height="640" height="640" data-path="images/reference/integrations/orum/salesforce-column-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=280&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=d983866fa604a227ce99edafe347acb7 280w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=560&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=cd802fb66106d991db90fc22d74b73d4 560w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=840&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=a9c0f33d842106aa5a84fbb1a78c79c7 840w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1100&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=40d31b55a1d796d926fc7d9e73feecde 1100w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=1650&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=4ed0c5852f172a55ee57baa895724135 1650w, https://mintcdn.com/unify-19/4OacOKaQcpDLCYcA/images/reference/integrations/orum/salesforce-column-setup.png?w=2500&fit=max&auto=format&n=4OacOKaQcpDLCYcA&q=85&s=0e662e08fd1cd4955ecc3e269252d51a 2500w" /></Frame>

## Orum Integration Setup

Once your Salesforce report is ready, connect Orum to Salesforce:

1. Navigate to **Settings** in Orum
2. Select **Integrations**
3. Choose **Salesforce** and authorize the connection

<Note>
  You will need admin access to Salesforce to authorize this connection. For more information, see: [Orum admin setup](https://support.orum.com/orum/article/ART-441).
</Note>

## Next Steps

With your Salesforce integration configured and Orum connected, you're ready to [launch your first call campaign](/reference/integrations/orum/call-campaigns)!

<Note>
  Need help with the setup? Contact our support team or refer to [Orum's Salesforce documentation](https://support.orum.com/orum/article/ART-410-getting-started-with-salesforce) for additional assistance.
</Note>


# Integration Guides
Source: https://docs.unifygtm.com/reference/integrations/overview

Explore the external tools and systems Unify integrates natively with.

export const SnitcherLogo = () => <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 31.620859 32.325714285714284" width="25" height="25">
    <path fill="#4133F5" d="M12.1913 32C11.541 32 11.1919 31.6171 11.1344 31.2376C11.0729 30.8311 11.3172 30.2585 12.2082 29.9822C14.3467 29.3204 21.5315 26.4956 24.2033 17.933C24.9018 15.6955 24.7286 13.3316 23.7157 11.2766C22.7021 9.22022 20.9706 7.72154 18.84 7.05672C18.0671 6.81565 17.2686 6.69338 16.4667 6.69338C12.7751 6.69338 9.39348 9.2674 8.24327 12.9529C8.04864 13.5764 7.53647 14.0466 7.05195 14.0466C6.77129 14.0466 6.59283 13.8841 6.49247 13.7477C6.24067 13.4053 6.17427 12.8456 6.32735 12.355C7.73631 7.83968 11.9072 4.68599 16.4699 4.68599C17.4721 4.68599 18.4706 4.83907 19.4379 5.141C24.8943 6.84342 27.8916 12.8502 26.1194 18.5309C23.1565 28.0267 15.1779 31.164 12.8031 31.8994C12.5886 31.9661 12.3828 32 12.1913 32ZM22.5611 31.4169C22.1839 31.4169 21.8703 31.2139 21.743 30.8872C21.5733 30.4521 21.7655 29.9223 22.2573 29.4699C25.2407 26.7233 27.459 23.216 28.6725 19.3275C29.7393 15.9091 29.4543 12.2854 27.87 9.12387C26.279 5.94902 23.5674 3.62789 20.2346 2.5878C19.0288 2.21166 17.7725 2.02095 16.5006 2.02095C10.6703 2.02095 5.55598 5.85367 3.77448 11.5583C3.36254 12.8771 3.57258 14.2845 4.33634 15.3231C4.98999 16.2119 5.98018 16.7217 7.05314 16.7217C8.71075 16.7217 10.2501 15.4995 10.7966 13.7496C11.6014 11.1698 13.9307 9.36797 16.4615 9.36797C16.9965 9.36797 17.5289 9.44944 18.0435 9.61001C19.497 10.0633 20.6717 11.0992 21.3511 12.527C22.0279 13.9493 22.1342 15.5862 21.6504 17.1364C19.6378 23.5867 13.6289 28.0918 7.03785 28.0918C6.20725 28.0918 5.37036 28.0198 4.55029 27.8778C3.6483 27.722 3.28486 27.182 3.32489 26.7159C3.36113 26.2924 3.73922 25.8649 4.5019 25.8649C4.62569 25.8649 4.75674 25.8767 4.89149 25.8999C5.59873 26.0223 6.32127 26.0844 7.03893 26.0844C12.7605 26.0839 17.9808 22.1584 19.7347 16.5384C20.4083 14.3785 19.3814 12.1298 17.4455 11.5256C17.1233 11.4253 16.7896 11.3743 16.4536 11.3743C14.797 11.3743 13.2585 12.597 12.7122 14.3474C11.9077 16.9269 9.57846 18.7283 7.04794 18.7283C5.3363 18.7283 3.76092 17.9211 2.72571 16.5137C1.58256 14.9593 1.25839 12.8834 1.85844 10.9605C3.87223 4.50709 9.87854 0 16.4648 0C17.9346 0 19.404 0.226091 20.8325 0.671875C24.6491 1.86266 27.7698 4.51447 29.62 8.13878C31.4797 11.782 31.8237 15.9679 30.5885 19.9254C29.2713 24.1463 26.8669 27.9499 23.6356 30.9248C23.1938 31.3315 22.8075 31.4169 22.5611 31.4169ZM7.01441 23.4158C4.69241 23.4155 2.48638 22.6011 0.634679 21.0605C0.106768 20.6194 -0.110428 20.0859 0.0537171 19.6335C0.17631 19.2956 0.493644 19.0858 0.882037 19.0858C1.21651 19.0858 1.57496 19.2376 1.91877 19.5246C3.39054 20.7525 5.1523 21.4016 7.01355 21.4016C10.7224 21.4016 14.1158 18.8285 15.2657 15.1442C15.514 14.3476 16.0155 14.0638 16.4019 14.0638C16.4845 14.0638 16.5654 14.076 16.6424 14.1001C17.1035 14.2439 17.469 14.8191 17.1816 15.7419C15.7714 20.2601 11.5909 23.4158 7.0155 23.4158H7.01441Z" />
    <path fill="#4133F5" d="M152.363 26.9306V11.3743H156.433V15.4141C157.488 11.3743 159.961 10.5905 162.252 11.314V15.1729C158.966 14.0273 156.433 15.5347 156.433 18.2179V26.9306H152.363Z" />
    <path fill="#4133F5" d="M133.359 19.1526C133.359 14.5701 136.887 11.073 141.529 11.073C146.745 11.073 150.393 15.4143 149.549 20.5997H137.55C138.093 22.4387 139.66 23.7351 141.801 23.7351C143.489 23.7351 144.906 22.9211 145.66 21.5644L149.006 23.0718C147.649 25.5138 145.057 27.2322 141.68 27.2322C136.947 27.2322 133.359 23.7351 133.359 19.1526ZM137.61 17.4945H145.479C144.936 15.7459 143.459 14.5701 141.529 14.5701C139.69 14.5701 138.183 15.7459 137.61 17.4945Z" />
    <path fill="#4133F5" d="M115.621 26.9305V4.62109H119.691V15.3537C120.505 12.7309 122.495 11.0727 125.088 11.0727C128.555 11.0727 130.816 13.786 130.816 17.4942V26.9305H126.746V18.2178C126.746 16.1979 125.299 14.7809 123.369 14.7809C121.198 14.7809 119.691 16.1979 119.691 18.2178V26.9305H115.621Z" />
    <path fill="#4133F5" d="M97.4121 19.1526C97.4121 14.5701 101 11.073 105.733 11.073C109.049 11.073 111.883 12.8517 113.21 16.0172L109.471 17.3136C108.778 15.7158 107.391 14.8113 105.733 14.8113C103.412 14.8113 101.633 16.6805 101.633 19.1526C101.633 21.6549 103.412 23.4939 105.733 23.4939C107.391 23.4939 108.778 22.5895 109.471 20.9916L113.21 22.288C111.883 25.4535 109.049 27.2322 105.733 27.2322C101 27.2322 97.4121 23.7351 97.4121 19.1526Z" />
    <path fill="#4133F5" d="M84.7676 14.9619V11.3743H87.903V6.79184L91.9729 5.52563V11.3743H96.0127V14.9619H91.9729V21.1422C91.9729 22.6496 92.6663 23.343 94.1737 23.343H96.0127V26.9306H94.1737C89.8927 26.9306 87.903 24.9408 87.903 20.901V14.9619H84.7676Z" />
    <path fill="#4133F5" d="M78.6428 26.9305V11.3742H82.7127V26.9305H78.6428ZM78.2207 7.06307C78.2207 5.70641 79.3362 4.62109 80.6928 4.62109C82.0193 4.62109 83.1348 5.70641 83.1348 7.06307C83.1348 8.38957 82.0193 9.50504 80.6928 9.50504C79.3362 9.50504 78.2207 8.38957 78.2207 7.06307Z" />
    <path fill="#4133F5" d="M60.3008 26.9308V11.3745H64.3707V15.354C65.1847 12.7311 67.1745 11.073 69.7672 11.073C73.2342 11.073 75.4953 13.7863 75.4953 17.4945V26.9308H71.4253V18.218C71.4253 16.1981 69.9782 14.7812 68.0488 14.7812C65.8781 14.7812 64.3707 16.1981 64.3707 18.218V26.9308H60.3008Z" />
    <path fill="#4133F5" d="M45.3802 20.479C45.7119 22.3481 47.0685 23.4937 49.42 23.4937C51.5304 23.4937 52.9172 22.4084 52.9172 21.0518C52.9172 16.9818 41.4912 19.5745 41.4912 11.7662C41.4912 8.20879 44.8979 5.52563 49.2391 5.52563C53.701 5.52563 56.6857 7.96761 57.1982 11.4045L52.8267 12.2787C52.4951 10.4699 51.1686 9.23382 49.0884 9.23382C47.2192 9.23382 45.953 10.1985 45.953 11.5251C45.953 15.4141 57.3791 12.8214 57.3791 20.9312C57.3791 24.5489 53.8216 27.2321 49.2994 27.2321C44.717 27.2321 41.5515 24.9107 41.0088 21.3532L45.3802 20.479Z" />
  </svg>;

export const SlackLogo = () => <svg width="25" height="25" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid">
    <path d="M27.2 80c0 7.3-5.9 13.2-13.2 13.2C6.7 93.2.8 87.3.8 80c0-7.3 5.9-13.2 13.2-13.2h13.2V80zm6.6 0c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2v33c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V80z" fill="#E01E5A" />
    <path d="M47 27c-7.3 0-13.2-5.9-13.2-13.2C33.8 6.5 39.7.6 47 .6c7.3 0 13.2 5.9 13.2 13.2V27H47zm0 6.7c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H13.9C6.6 60.1.7 54.2.7 46.9c0-7.3 5.9-13.2 13.2-13.2H47z" fill="#36C5F0" />
    <path d="M99.9 46.9c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H99.9V46.9zm-6.6 0c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V13.8C66.9 6.5 72.8.6 80.1.6c7.3 0 13.2 5.9 13.2 13.2v33.1z" fill="#2EB67D" />
    <path d="M80.1 99.8c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V99.8h13.2zm0-6.6c-7.3 0-13.2-5.9-13.2-13.2 0-7.3 5.9-13.2 13.2-13.2h33.1c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H80.1z" fill="#ECB22E" />
  </svg>;

export const SixsenseLogoLight = () => <svg className="block dark:hidden" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.603 8.31196C14.5316 8.50714 15.4351 8.87062 16.2661 9.40665L13.5118 12.6791C12.0197 11.9955 10.1959 12.3568 9.08921 13.6715C7.98258 14.9851 7.94215 16.8377 8.87688 18.1833L6.1215 21.4558C3.42843 18.5695 3.25322 14.0681 5.86045 10.971L15.0982 0L18.3271 2.7004L13.603 8.31196Z" fill="#13BBB2" />
    <path d="M18.0446 21.1689C15.4365 24.2659 10.959 24.8762 7.63892 22.7335L10.3942 19.4609C11.8864 20.1445 13.7101 19.7841 14.8157 18.4695C15.9225 17.1548 15.9628 15.3024 15.0282 13.9567L17.7834 10.6841C20.4766 13.5704 20.6528 18.0718 18.0446 21.1689Z" fill="#192232" />
  </svg>;

export const SixsenseLogoDark = () => <svg className="hidden dark:block" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.603 8.31196C14.5316 8.50714 15.4351 8.87062 16.2661 9.40665L13.5118 12.6791C12.0197 11.9955 10.1959 12.3568 9.08921 13.6715C7.98258 14.9851 7.94215 16.8377 8.87688 18.1833L6.1215 21.4558C3.42843 18.5695 3.25322 14.0681 5.86045 10.971L15.0982 0L18.3271 2.7004L13.603 8.31196Z" fill="#13BBB2" />
    <path d="M18.0446 21.1689C15.4365 24.2659 10.959 24.8762 7.63892 22.7335L10.3942 19.4609C11.8864 20.1445 13.7101 19.7841 14.8157 18.4695C15.9225 17.1548 15.9628 15.3024 15.0282 13.9567L17.7834 10.6841C20.4766 13.5704 20.6528 18.0718 18.0446 21.1689Z" fill="white" />
  </svg>;

export const SegmentIcon = () => <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
      <g transform="matrix(.768307 0 0 .768307 0 2.304922)">
        <path d="M51.9 52.8H4c-2.2 0-4-1.8-4-4s1.8-4 4-4h47.9c2.2 0 4 1.8 4 4s-1.8 4-4 4z" fill="#99cfac" />
        <path d="M41.7 77.3c-3.9 0-7.8-.6-11.5-1.7-2.1-.7-3.3-2.9-2.6-5s2.9-3.3 5-2.6c2.9.9 6 1.4 9.1 1.4 13.6 0 25.4-8.7 29.3-21.7.6-2.1 2.9-3.3 5-2.7s3.3 2.9 2.7 5c-5.1 16.3-19.9 27.3-37 27.3z" fill="#49b881" />
        <path d="M79.3 32.5H31.4c-2.2 0-4-1.8-4-4s1.8-4 4-4h47.9c2.2 0 4 1.8 4 4s-1.8 4-4 4z" fill="#99cfac" />
        <path d="M8.5 32.5c-.4 0-.8-.1-1.2-.2-2.1-.6-3.3-2.9-2.7-5C9.7 11 24.5 0 41.7 0c3.9 0 7.8.6 11.5 1.7 2.1.7 3.3 2.9 2.6 5s-2.9 3.3-5 2.6c-2.9-.9-6-1.4-9.1-1.4-13.6 0-25.4 8.7-29.3 21.7-.6 1.8-2.2 2.9-3.9 2.9z" fill="#49b881" />
        <g fill="#99cfac">
          <circle r="4" cy="13.3" cx="65.4" />
          <circle r="4" cy="64.1" cx="17.9" />
        </g>
      </g>
    </svg>;

export const SalesforceLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M9.98736 5.83214C10.7614 5.02566 11.839 4.52545 13.0308 4.52545C14.6151 4.52545 15.9973 5.40886 16.7334 6.72031C17.373 6.43452 18.0811 6.27553 18.826 6.27553C21.6834 6.27553 24 8.6123 24 11.4947C24 14.3774 21.6834 16.7142 18.826 16.7142C18.4837 16.7144 18.1423 16.6803 17.8068 16.6126C17.1587 17.7688 15.9234 18.5501 14.5057 18.5501C13.9121 18.5501 13.3508 18.413 12.851 18.1692C12.1939 19.7148 10.6629 20.7986 8.87863 20.7986C7.02052 20.7986 5.43692 19.6229 4.82907 17.974C4.56344 18.0304 4.28822 18.0598 4.00581 18.0598C1.79351 18.0598 0 16.2479 0 14.0123C0 12.5142 0.805814 11.2061 2.00308 10.5063C1.75659 9.93915 1.61948 9.31315 1.61948 8.65502C1.61948 6.08408 3.70667 4 6.28103 4C7.79248 4 9.13574 4.71863 9.98736 5.83214Z" fill="#00A1E0" />
  </svg>;

export const NooksLogo = () => <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 200 200">
  <path fill="#230043" opacity="1.000000" stroke="none" d="
  M119.000000,201.000000 
    C79.357826,201.000000 40.215649,201.000000 1.036737,201.000000 
    C1.036737,134.399536 1.036737,67.799034 1.036737,1.099268 
    C67.558670,1.099268 134.117538,1.099268 200.838196,1.099268 
    C200.838196,67.666351 200.838196,134.333145 200.838196,201.000000 
    C173.799316,201.000000 146.649658,201.000000 119.000000,201.000000 
  M117.402946,131.074799 
    C117.402946,131.074799 117.368576,131.114456 117.171303,131.878006 
    C117.233192,132.133499 117.295082,132.388977 116.794640,132.923996 
    C117.524574,135.285172 118.254509,137.646332 119.109833,140.693161 
    C122.630615,144.002182 125.623695,148.380356 129.768097,150.425919 
    C143.941711,157.421646 161.413132,147.001297 161.826416,131.058090 
    C161.517914,128.386688 161.209412,125.715279 160.888306,122.396355 
    C160.816833,121.971794 160.745361,121.547241 160.696289,120.569565 
    C160.414612,120.112282 160.132935,119.654991 159.575928,118.568634 
    C157.246841,116.031120 154.917740,113.493614 152.224594,110.360306 
    C151.053970,109.674019 149.883331,108.987732 148.243439,107.801765 
    C144.195679,105.070541 142.673996,101.173119 142.658783,96.399162 
    C142.642593,91.322090 142.345291,86.245911 142.521454,80.471642 
    C142.581055,79.956490 142.640671,79.441338 143.178589,78.424683 
    C145.867081,75.618240 148.222549,72.357765 151.309021,70.093933 
    C159.272583,64.252914 163.173325,56.874401 161.692825,46.276360 
    C161.153000,45.177895 160.613174,44.079430 159.991623,42.247223 
    C158.666672,39.839832 157.341721,37.432438 155.694244,34.333748 
    C155.208603,33.746727 154.722977,33.159706 154.150162,32.718189 
    C154.150162,32.718189 154.397202,32.735134 153.618408,32.332333 
    C153.340530,32.241802 153.062637,32.151272 152.481506,31.467390 
    C147.844543,28.026756 142.723007,26.380198 136.289032,27.193102 
    C135.897720,27.332186 135.506409,27.471270 134.386642,27.562538 
    C127.190384,29.125095 121.697433,32.857269 118.848953,39.880856 
    C118.848953,39.880856 118.890305,39.783588 118.360428,40.180073 
    C118.201492,40.806564 118.042557,41.433056 117.609276,42.083569 
    C117.609276,42.083569 117.553223,42.353195 117.206917,42.655434 
    C117.206917,42.655434 117.022713,43.076977 116.702599,43.570484 
    C116.649361,44.139359 116.596130,44.708233 116.367493,45.843288 
    C116.305962,46.233009 116.244431,46.622730 115.769272,47.597370 
    C114.960197,56.792149 118.671906,63.921101 125.790611,69.481300 
    C128.617783,71.689499 131.469528,73.866226 134.434402,76.665985 
    C134.550827,77.063438 134.667252,77.460884 134.625656,78.147202 
    C134.577728,78.499908 134.679138,78.796150 134.964600,79.937508 
    C135.080856,82.644852 135.197098,85.352196 135.176483,88.970795 
    C135.128906,93.013496 135.081345,97.056198 134.722336,101.356323 
    C134.530029,101.557854 134.411545,101.796104 134.019547,102.726768 
    C132.905304,107.666924 128.653061,108.627609 124.072868,109.833397 
    C120.348953,108.317902 116.625038,106.802406 112.634995,104.981895 
    C112.634995,104.981895 112.246994,104.866493 111.963188,104.263824 
    C109.956551,102.880707 107.949913,101.497589 105.944572,100.045898 
    C105.944572,100.045898 105.879280,100.066917 105.642876,99.482033 
    C104.414650,98.701881 103.186424,97.921730 101.741562,96.859840 
    C101.741562,96.859840 101.401520,96.756493 101.109169,96.181671 
    C100.045120,95.504997 98.981064,94.828316 97.903435,94.081161 
    C97.903435,94.081161 97.833923,94.099014 97.565155,93.500557 
    C95.362381,92.036285 93.159615,90.572006 90.911095,89.037682 
    C90.911095,89.037682 90.841759,89.084503 90.456726,88.671234 
    C89.980850,88.127373 89.504974,87.583511 88.741211,86.469208 
    C88.116745,85.659126 87.492287,84.849037 86.879776,83.248955 
    C86.756653,80.838165 86.685135,78.423340 86.497391,76.017593 
    C86.260704,72.984627 85.929153,69.959076 85.590286,66.299171 
    C85.433327,65.909241 85.276375,65.519310 85.263451,64.896996 
    C85.279411,64.584854 85.147278,64.376114 84.752304,63.715252 
    C84.347870,63.091015 83.943428,62.466774 83.295242,61.186539 
    C82.298279,59.910656 81.301323,58.634773 80.149780,57.088146 
    C80.149780,57.088146 79.841751,57.037807 79.692574,56.470448 
    C79.212151,56.168922 78.731728,55.867397 78.027046,55.220951 
    C77.823006,55.016632 77.576790,54.907394 77.013245,54.277802 
    C75.653831,53.588547 74.294426,52.899292 72.537148,51.879364 
    C72.209251,51.785549 71.881363,51.691730 71.141777,51.176254 
    C70.758720,51.139988 70.375656,51.103725 69.402168,50.761986 
    C68.972610,50.664165 68.543060,50.566345 67.526222,50.116928 
    C64.521820,50.303875 61.517422,50.490822 58.217030,50.614349 
    C58.217030,50.614349 58.005230,50.830616 57.230679,50.769482 
    C51.861492,52.071629 47.726509,55.105419 44.105682,60.012886 
    C43.233921,62.088749 42.362160,64.164612 41.320072,66.816582 
    C41.257984,67.211861 41.195892,67.607140 40.649155,68.654129 
    C38.693535,77.950264 42.736500,87.428093 50.771049,92.653412 
    C53.385910,94.354004 55.849258,96.287552 58.577328,98.993286 
    C58.984524,102.679764 59.391720,106.366241 59.637421,110.952721 
    C59.636517,114.606415 59.635609,118.260109 59.308216,122.200485 
    C59.165024,122.480568 59.163528,122.761406 59.101990,123.683083 
    C58.894932,124.552650 58.687874,125.422211 58.004536,126.730652 
    C57.292507,127.798080 56.580479,128.865524 55.470181,130.100403 
    C55.470181,130.100403 55.166119,130.407318 54.524738,130.653534 
    C51.728916,132.789658 48.933094,134.925781 45.713295,137.267990 
    C45.439571,137.475708 45.311337,137.751160 44.723133,138.439301 
    C42.167591,142.247849 39.653011,146.068146 40.997334,151.763611 
    C41.082321,152.498810 41.167305,153.234009 40.754997,154.293304 
    C41.102726,155.849152 41.450455,157.405014 41.626148,158.800018 
    C41.626148,158.800018 41.461735,158.968643 41.337486,159.370193 
    C41.588215,159.843475 41.838943,160.316757 42.326839,161.399231 
    C43.140118,162.673630 43.953400,163.948044 44.963867,165.867126 
    C47.540440,169.876984 50.969147,172.646759 56.298027,173.914413 
    C68.718102,178.491943 84.257690,169.711105 85.886284,157.095978 
    C85.900024,153.736160 85.913773,150.376328 85.875824,146.245773 
    C84.919815,144.161362 83.963814,142.076965 82.882080,139.426773 
    C80.044670,136.742599 77.543434,133.514725 74.290161,131.503128 
    C69.543098,128.567856 67.308975,124.616432 67.239426,119.315216 
    C67.155128,112.889870 67.320831,106.461250 67.941154,99.772301 
    C71.469711,94.103271 76.744133,92.176811 83.715454,93.019890 
    C84.878555,93.533356 86.041656,94.046822 87.549652,94.835114 
    C87.549652,94.835114 87.951370,95.017075 88.125496,95.665161 
    C97.024139,102.526329 105.922775,109.387505 115.084503,116.555908 
    C115.084503,116.555908 115.477020,116.654602 115.542862,117.246819 
    C115.878716,118.174599 116.214577,119.102379 116.271988,120.724419 
    C116.340332,122.501274 116.408676,124.278137 116.408844,126.821350 
    C116.446480,127.845695 116.484116,128.870041 116.439430,130.325775 
    C116.769691,130.559998 117.099960,130.794205 117.402946,131.074799 
  z" />
  <path fill="#BB3BEE" opacity="1.000000" stroke="none" d="
  M44.702873,59.698479 
    C47.726509,55.105419 51.861492,52.071629 57.449570,51.043808 
    C57.116058,51.882748 56.563656,52.447365 56.005733,53.006042 
    C56.000214,53.000107 56.012901,53.013134 55.689079,53.158539 
    C49.111294,56.793011 48.129742,62.992222 52.843033,68.380768 
    C56.638596,72.720116 61.499714,73.285187 66.845932,73.077835 
    C75.237869,72.752357 80.043480,68.088913 80.072693,59.832466 
    C80.075615,59.007679 80.223671,58.183403 80.304367,57.358891 
    C81.301323,58.634773 82.298279,59.910656 83.172653,61.717991 
    C83.043068,63.496494 83.036072,64.743546 82.824112,66.269646 
    C81.741867,68.690643 80.864594,70.832588 79.683731,73.077858 
    C78.260780,73.794456 77.141411,74.407730 75.595039,75.025162 
    C70.577339,75.215775 65.977318,75.279716 61.398983,75.628479 
    C57.904903,75.894646 54.438313,76.521652 50.770664,76.723587 
    C49.741463,75.297234 48.901093,74.135422 47.912491,72.766998 
    C47.535614,72.310585 47.306961,72.060799 46.957855,71.549179 
    C45.889259,71.280563 44.941120,71.273781 43.736748,71.243385 
    C43.316856,71.168320 43.153206,71.116867 42.769718,70.857300 
    C42.077854,69.766922 41.605831,68.884674 41.133804,68.002419 
    C41.195892,67.607140 41.257984,67.211861 41.706558,66.396889 
    C42.962986,63.884289 43.832928,61.791386 44.702873,59.698479 
  z" />
  <path fill="#822ABB" opacity="1.000000" stroke="none" d="
  M44.766678,165.222443 
    C43.953400,163.948044 43.140118,162.673630 42.169197,160.772171 
    C41.828278,159.752960 41.645008,159.360794 41.461735,158.968643 
    C41.461735,158.968643 41.626148,158.800018 42.190018,158.761688 
    C43.065533,158.622925 43.377178,158.522491 43.941238,158.543671 
    C44.801579,159.097137 45.409496,159.529007 46.105396,160.246185 
    C50.892612,162.108398 52.784393,157.638199 56.403019,155.989868 
    C58.216991,155.984207 59.612339,155.974518 61.330742,155.958374 
    C62.439323,155.649475 63.224854,155.347015 64.340652,155.048630 
    C65.111267,155.047256 65.551605,155.041824 66.323608,155.236313 
    C72.699760,156.554947 78.716064,153.631912 81.951233,147.626862 
    C81.940559,146.470398 81.913795,145.699554 81.900314,144.550140 
    C81.884323,143.164413 81.855049,142.157257 81.950409,140.981720 
    C82.385971,140.539749 82.696892,140.266159 83.007812,139.992554 
    C83.963814,142.076965 84.919815,144.161362 85.711685,146.932068 
    C83.406837,150.810562 81.895500,154.840179 78.994339,157.020538 
    C72.960251,161.555450 66.028389,164.159424 58.057297,162.397095 
    C56.127769,161.970490 53.873577,162.746170 51.822117,163.206909 
    C49.439594,163.742020 47.115902,164.539078 44.766678,165.222443 
  z" />
  <path fill="#C93CF8" opacity="1.000000" stroke="none" d="
  M154.237350,32.572685 
    C154.722977,33.159706 155.208603,33.746727 155.788574,35.044037 
    C155.894150,36.495552 155.905396,37.236778 155.717499,38.260147 
    C152.425461,47.379707 146.510757,53.130180 137.123184,54.611008 
    C133.929688,55.114761 130.356903,53.894909 127.359367,54.797516 
    C123.078537,56.086548 121.735153,53.928799 121.119164,50.797295 
    C120.422066,47.253483 120.349144,43.586891 120.177383,39.704700 
    C121.539650,38.617138 122.729347,37.798561 123.918785,37.326874 
    C123.617569,38.779926 123.316612,39.886093 123.034180,41.356773 
    C125.896111,49.726406 134.436172,53.434261 140.407898,49.083916 
    C142.178589,48.383106 143.596863,47.701790 145.340683,46.903854 
    C151.135956,42.447968 150.270782,36.807632 149.211945,31.178783 
    C150.613632,31.550232 151.699203,31.805487 152.784760,32.060741 
    C153.062637,32.151272 153.340530,32.241802 153.961182,32.532501 
    C154.303955,32.732666 154.237350,32.572681 154.237350,32.572685 
  z" />
  <path fill="#3C0E7E" opacity="1.000000" stroke="none" d="
  M161.723511,131.912369 
    C161.413132,147.001297 143.941711,157.421646 129.768097,150.425919 
    C125.623695,148.380356 122.630615,144.002182 119.389702,140.419754 
    C130.852798,149.517761 142.166565,148.305954 153.280014,140.210190 
    C156.435120,137.911804 158.927307,134.703430 161.723511,131.912369 
  z" />
  <path fill="#5E1B99" opacity="1.000000" stroke="none" d="
  M44.865273,165.544785 
    C47.115902,164.539078 49.439594,163.742020 51.822117,163.206909 
    C53.873577,162.746170 56.127769,161.970490 58.057297,162.397095 
    C66.028389,164.159424 72.960251,161.555450 78.994339,157.020538 
    C81.895500,154.840179 83.406837,150.810562 85.737534,147.317444 
    C85.913773,150.376328 85.900024,153.736160 85.478775,157.590942 
    C79.440567,160.710464 74.003952,163.972733 68.119522,165.763626 
    C63.158112,167.273575 58.853680,169.046143 55.829300,173.333405 
    C50.969147,172.646759 47.540440,169.876984 44.865273,165.544785 
  z" />
  <path fill="#D446FA" opacity="1.000000" stroke="none" d="
  M55.166119,130.407318 
    C55.166119,130.407318 55.470181,130.100403 55.998940,129.996399 
    C57.351768,129.596146 58.175842,129.299881 59.280098,128.819855 
    C61.376488,126.752556 63.192688,124.869034 65.163025,123.301071 
    C68.549721,127.394257 71.782272,131.171890 75.002289,135.389069 
    C74.644707,138.859604 74.299652,141.890594 73.603065,145.018982 
    C72.093056,145.763733 70.969109,146.485077 69.769798,147.044968 
    C65.726120,148.932693 59.228966,148.248474 56.795105,144.887009 
    C54.316647,141.463959 52.936123,137.336182 54.993225,132.641602 
    C55.084061,131.685623 55.125088,131.046478 55.166119,130.407318 
  M59.166622,137.796555 
    C57.238651,143.872665 60.554127,147.438934 66.954620,145.759933 
    C68.491180,145.356873 70.517868,143.368683 70.651184,141.952454 
    C70.814278,140.219940 69.703651,137.538239 68.283844,136.664719 
    C65.618294,135.024796 62.330544,134.332031 59.166622,137.796555 
  z" />
  <path fill="#581797" opacity="1.000000" stroke="none" d="
  M161.774963,131.485229 
    C158.927307,134.703430 156.435120,137.911804 153.280014,140.210190 
    C142.166565,148.305954 130.852798,149.517761 119.327011,140.076935 
    C118.254509,137.646332 117.524574,135.285172 117.276520,133.129211 
    C119.658554,135.079727 121.266434,137.620819 123.505554,138.443176 
    C139.947937,144.482040 154.275650,140.743134 160.900909,123.043869 
    C161.209412,125.715279 161.517914,128.386688 161.774963,131.485229 
  z" />
  <path fill="#EF53FE" opacity="1.000000" stroke="none" d="
  M71.553467,51.597916 
    C71.881363,51.691730 72.209251,51.785549 72.776978,52.406235 
    C74.440666,53.586483 75.864532,54.239861 77.288391,54.893238 
    C77.576790,54.907394 77.823006,55.016632 77.985023,55.737309 
    C77.858528,56.490112 77.774048,56.726562 77.387932,56.990467 
    C76.743484,57.879498 75.924530,58.884182 76.133629,59.579865 
    C77.718140,64.851479 74.550362,68.735504 70.762901,69.891075 
    C66.831055,71.090698 61.362442,70.703964 57.816013,68.746315 
    C54.266441,66.786934 51.715694,62.222656 55.021252,57.265789 
    C55.777332,56.132008 55.704327,54.445343 56.012901,53.013134 
    C56.012901,53.013134 56.000214,53.000107 56.381176,53.009567 
    C58.202141,52.419704 59.642139,51.820381 61.397522,51.261467 
    C63.808361,51.530056 65.903816,51.758236 68.169067,52.144585 
    C68.895287,52.236588 69.451714,52.170429 70.402069,52.000893 
    C71.048492,51.797649 71.300980,51.697781 71.553467,51.597916 
  M59.131992,67.296608 
    C61.127747,67.858650 63.092590,68.694717 65.125870,68.924049 
    C69.012184,69.362381 70.781357,67.146538 71.383400,63.480083 
    C72.008842,59.671177 69.445686,58.454754 66.732155,57.538837 
    C60.069546,55.289955 57.018555,58.779259 59.131992,67.296608 
  z" />
  <path fill="#8627BF" opacity="1.000000" stroke="none" d="
  M152.588654,110.956100 
    C154.917740,113.493614 157.246841,116.031120 159.672882,119.182434 
    C159.718521,120.197006 159.667221,120.597771 159.332199,121.165405 
    C156.362152,128.297333 152.629013,134.273300 144.797592,136.352203 
    C137.729263,138.228531 130.694016,139.411880 124.312408,135.145111 
    C127.058052,134.612747 129.491180,134.341522 131.813934,133.681717 
    C136.855804,132.249466 142.300674,131.425354 146.749023,128.892090 
    C154.692215,124.368591 158.393677,116.890129 151.979431,110.981812 
    C152.181107,110.952560 152.588654,110.956100 152.588654,110.956100 
  z" />
  <path fill="#411084" opacity="1.000000" stroke="none" d="
  M56.063663,173.623901 
    C58.853680,169.046143 63.158112,167.273575 68.119522,165.763626 
    C74.003952,163.972733 79.440567,160.710464 85.386650,157.984070 
    C84.257690,169.711105 68.718102,178.491943 56.063663,173.623901 
  z" />
  <path fill="#B135EC" opacity="1.000000" stroke="none" d="
  M120.004822,39.973686 
    C120.349144,43.586891 120.422066,47.253483 121.119164,50.797295 
    C121.735153,53.928799 123.078537,56.086548 127.359367,54.797516 
    C130.356903,53.894909 133.929688,55.114761 137.123184,54.611008 
    C146.510757,53.130180 152.425461,47.379707 155.943436,38.574371 
    C157.760147,45.784027 152.189835,55.311237 144.543289,56.919846 
    C137.486984,58.404285 130.122696,58.424751 122.661392,58.912811 
    C121.657188,57.668087 120.885643,56.600578 120.067184,55.115822 
    C119.089607,52.770611 118.158943,50.842640 117.147812,48.649055 
    C116.772522,47.926441 116.477707,47.469444 116.182892,47.012447 
    C116.244431,46.622730 116.305962,46.233009 116.648827,45.521179 
    C116.930161,45.199070 117.249413,44.965485 117.384872,44.657940 
    C117.531288,43.684662 117.542259,43.018929 117.553223,42.353195 
    C117.553223,42.353195 117.609276,42.083569 117.929031,41.815063 
    C118.462631,40.958904 118.676468,40.371246 118.890305,39.783588 
    C118.890305,39.783588 118.848953,39.880856 119.114120,39.893364 
    C119.587799,39.928478 119.796310,39.951084 120.004822,39.973686 
  z" />
  <path fill="#581599" opacity="1.000000" stroke="none" d="
  M161.649994,46.931911 
    C163.173325,56.874401 159.272583,64.252914 151.309021,70.093933 
    C148.222549,72.357765 145.867081,75.618240 142.678650,78.430405 
    C141.825485,75.322983 141.472244,72.209846 141.436584,68.993599 
    C148.980896,62.109882 157.808807,56.780033 161.649994,46.931911 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M75.014816,134.949524 
    C71.782272,131.171890 68.549721,127.394257 65.166977,122.892700 
    C63.277489,118.130089 61.538204,114.091400 59.798916,110.052719 
    C59.391720,106.366241 58.984524,102.679764 58.892731,98.526917 
    C59.482452,98.032570 59.756767,98.004601 60.261467,98.220863 
    C61.993977,100.307686 63.557194,101.914398 66.384995,99.959282 
    C66.935051,100.019539 67.156700,100.026787 67.378357,100.034042 
    C67.320831,106.461250 67.155128,112.889870 67.239426,119.315216 
    C67.308975,124.616432 69.543098,128.567856 74.290161,131.503128 
    C77.543434,133.514725 80.044670,136.742599 82.944946,139.709656 
    C82.696892,140.266159 82.385971,140.539749 81.655380,140.839188 
    C79.162079,138.893204 77.088448,136.921356 75.014816,134.949524 
  z" />
  <path fill="#B63FE8" opacity="1.000000" stroke="none" d="
  M54.943413,132.958405 
    C52.936123,137.336182 54.316647,141.463959 56.795105,144.887009 
    C59.228966,148.248474 65.726120,148.932693 69.769798,147.044968 
    C70.969109,146.485077 72.093056,145.763733 73.623169,145.317505 
    C74.007523,145.717102 74.020248,145.915573 73.931732,146.450729 
    C72.258286,147.829697 70.724609,149.678162 69.106316,149.755478 
    C65.068565,149.948395 60.992363,149.336288 56.710815,148.813385 
    C53.051800,146.240417 51.860378,148.245834 51.084927,151.299301 
    C50.589451,153.250320 49.899910,155.152039 49.224670,156.621704 
    C49.073326,154.074051 48.853680,151.974274 48.946915,149.888458 
    C49.114285,146.144287 47.439274,144.906494 43.962528,145.483200 
    C44.442558,142.788513 44.885578,140.441422 45.328598,138.094345 
    C45.311337,137.751160 45.439571,137.475708 46.278152,137.144196 
    C49.543140,135.666397 52.243279,134.312408 54.943413,132.958405 
  z" />
  <path fill="#962BD2" opacity="1.000000" stroke="none" d="
  M122.894058,59.090027 
    C130.122696,58.424751 137.486984,58.404285 144.543289,56.919846 
    C152.189835,55.311237 157.760147,45.784027 156.142548,38.292221 
    C155.905396,37.236778 155.894150,36.495552 155.949829,35.389687 
    C157.341721,37.432438 158.666672,39.839832 159.816727,42.895180 
    C156.324478,52.801731 151.032639,60.169003 140.544250,62.995022 
    C135.373016,63.334919 130.662292,63.679485 125.674500,63.833050 
    C124.562981,62.124710 123.728523,60.607368 122.894058,59.090027 
  z" />
  <path fill="#D341FA" opacity="1.000000" stroke="none" d="
  M55.689079,53.158539 
    C55.704327,54.445343 55.777332,56.132008 55.021252,57.265789 
    C51.715694,62.222656 54.266441,66.786934 57.816013,68.746315 
    C61.362442,70.703964 66.831055,71.090698 70.762901,69.891075 
    C74.550362,68.735504 77.718140,64.851479 76.133629,59.579865 
    C75.924530,58.884182 76.743484,57.879498 77.750000,57.016632 
    C78.889717,57.022827 79.365730,57.030319 79.841751,57.037807 
    C79.841751,57.037807 80.149780,57.088146 80.227074,57.223518 
    C80.223671,58.183403 80.075615,59.007679 80.072693,59.832466 
    C80.043480,68.088913 75.237869,72.752357 66.845932,73.077835 
    C61.499714,73.285187 56.638596,72.720116 52.843033,68.380768 
    C48.129742,62.992222 49.111294,56.793011 55.689079,53.158539 
  z" />
  <path fill="#BA3CF0" opacity="1.000000" stroke="none" d="
  M116.550430,120.030159 
    C116.214577,119.102379 115.878716,118.174599 115.778366,116.688599 
    C116.646591,115.752457 117.279320,115.374535 118.168259,115.217850 
    C121.567268,118.493652 123.409721,123.362747 129.316162,123.027786 
    C130.071442,123.051880 130.503113,123.060631 131.121277,123.217613 
    C131.542648,123.581207 131.755569,123.816444 132.100052,124.381592 
    C134.167831,125.449089 136.082092,126.206566 137.668091,127.179581 
    C134.939117,127.448120 132.510986,127.303131 130.148193,127.630089 
    C128.781082,127.819267 127.188446,128.465027 126.286766,129.446732 
    C124.905167,130.950958 124.032097,132.922272 122.659409,134.619659 
    C121.625961,133.925537 120.876282,133.307068 120.095444,132.358429 
    C119.332062,131.044373 118.599831,130.060455 117.494461,129.220642 
    C116.921463,129.541290 116.721603,129.717834 116.521744,129.894379 
    C116.484116,128.870041 116.446480,127.845695 116.702591,126.202316 
    C116.847702,123.732239 116.699066,121.881203 116.550430,120.030159 
  z" />
  <path fill="#A435DB" opacity="1.000000" stroke="none" d="
  M135.313339,88.059540 
    C135.197098,85.352196 135.080856,82.644852 134.964188,79.185829 
    C134.903732,78.242210 134.843704,78.050270 134.783676,77.858330 
    C134.667252,77.460884 134.550827,77.063438 134.580414,76.389618 
    C134.726425,76.113258 135.138565,76.034576 135.492065,76.062775 
    C137.953949,77.783760 140.062347,79.476547 142.170746,81.169342 
    C142.345291,86.245911 142.642593,91.322090 142.658783,96.399162 
    C142.673996,101.173119 144.195679,105.070541 148.288025,108.238594 
    C148.208664,108.802803 148.084702,108.930191 147.637054,108.965607 
    C145.592300,107.868996 143.871246,106.864357 142.059540,105.531136 
    C141.341354,103.748428 140.713821,102.294296 140.028473,100.505280 
    C138.711075,96.020821 140.870712,90.556366 135.313339,88.059540 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M85.638519,66.930321 
    C85.929153,69.959076 86.260704,72.984627 86.497391,76.017593 
    C86.685135,78.423340 86.756653,80.838165 86.518311,83.647026 
    C84.732788,84.690773 83.308716,85.336449 81.491821,85.897354 
    C73.461891,85.962570 65.819550,86.005737 58.193539,86.380882 
    C57.085365,86.435387 56.055328,88.078224 54.656364,88.916840 
    C52.352501,87.561157 50.381405,86.274727 48.320946,84.800415 
    C48.231579,84.612534 48.079762,84.230301 48.350990,84.081467 
    C49.178623,83.652657 49.735031,83.372696 50.663139,83.118408 
    C52.027020,83.100693 53.019203,83.057312 54.413757,83.105927 
    C59.210915,83.142174 63.605705,83.086426 68.332161,83.026001 
    C69.105804,83.005630 69.547783,82.989929 70.439255,82.986427 
    C74.723244,82.280914 80.508507,85.493713 80.986359,77.996170 
    C80.996689,78.000214 80.992462,77.978935 81.284248,77.806076 
    C82.391396,76.090134 83.206757,74.547050 84.151596,72.719116 
    C84.240723,71.264771 84.200371,70.095284 84.158585,68.628113 
    C84.164551,67.933929 84.171944,67.537415 84.543350,67.082840 
    C85.151085,66.993301 85.394798,66.961807 85.638519,66.930321 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M120.126602,132.688599 
    C120.876282,133.307068 121.625961,133.925537 122.905830,134.764771 
    C123.607292,135.067047 123.778572,135.148529 123.949844,135.230026 
    C130.694016,139.411880 137.729263,138.228531 144.797592,136.352203 
    C152.629013,134.273300 156.362152,128.297333 159.597244,121.204819 
    C160.321976,121.092476 160.497940,121.107582 160.673889,121.122681 
    C160.745361,121.547241 160.816833,121.971794 160.894608,122.720108 
    C154.275650,140.743134 139.947937,144.482040 123.505554,138.443176 
    C121.266434,137.620819 119.658554,135.079727 117.557686,132.989441 
    C117.295082,132.388977 117.233192,132.133499 117.574554,131.702179 
    C118.183784,131.654465 118.389763,131.782608 118.850525,132.044418 
    C119.445732,132.348267 119.786171,132.518433 120.126602,132.688599 
  z" />
  <path fill="#6519A6" opacity="1.000000" stroke="none" d="
  M122.661392,58.912811 
    C123.728523,60.607368 124.562981,62.124710 125.860054,64.125214 
    C127.646461,65.506241 128.855347,66.741501 130.315567,67.238838 
    C134.725601,68.740852 136.881287,71.261070 135.138565,76.034576 
    C135.138565,76.034576 134.726425,76.113258 134.518250,76.085274 
    C131.469528,73.866226 128.617783,71.689499 125.790611,69.481300 
    C118.671906,63.921101 114.960197,56.792149 115.976082,47.304909 
    C116.477707,47.469444 116.772522,47.926441 117.098328,49.024940 
    C117.744011,51.788624 118.358704,53.910797 119.079712,56.142712 
    C119.186020,56.252453 119.604782,56.367851 119.604782,56.367851 
    C119.604782,56.367851 119.999855,56.182224 120.053345,56.024323 
    C120.106827,55.866417 120.114098,55.533066 120.114098,55.533066 
    C120.885643,56.600578 121.657188,57.668087 122.661392,58.912811 
  z" />
  <path fill="#7325AB" opacity="1.000000" stroke="none" d="
  M48.410309,84.988289 
    C50.381405,86.274727 52.352501,87.561157 54.737282,89.248291 
    C56.771130,91.768982 58.391300,93.888962 60.012711,96.337013 
    C60.019665,97.102257 60.025375,97.539444 60.031086,97.976624 
    C59.756767,98.004601 59.482452,98.032570 58.795021,98.087555 
    C55.849258,96.287552 53.385910,94.354004 50.771049,92.653412 
    C42.736500,87.428093 38.693535,77.950264 40.891479,68.328278 
    C41.605831,68.884674 42.077854,69.766922 42.686665,71.254227 
    C41.625519,76.798447 43.396835,80.718208 47.171368,84.245834 
    C47.701733,84.650085 48.056019,84.819191 48.410309,84.988289 
  z" />
  <path fill="#C93EF9" opacity="1.000000" stroke="none" d="
  M128.992538,123.012451 
    C123.409721,123.362747 121.567268,118.493652 118.162079,114.894310 
    C117.860100,113.920418 117.820511,113.491302 118.045670,112.935104 
    C120.457779,111.883446 122.605141,110.958862 124.752502,110.034279 
    C128.653061,108.627609 132.905304,107.666924 134.423645,102.413666 
    C134.827728,102.100563 135.286041,102.041382 135.418335,102.190750 
    C135.720474,102.545929 135.870071,102.765541 135.996216,103.403702 
    C134.799393,106.108711 134.163651,109.122368 132.306763,110.574554 
    C126.892166,114.809059 126.094017,116.747681 128.992538,123.012451 
  z" />
  <path fill="#7E1DC8" opacity="1.000000" stroke="none" d="
  M135.492065,76.062775 
    C136.881287,71.261070 134.725601,68.740852 130.315567,67.238838 
    C128.855347,66.741501 127.646461,65.506241 126.137115,64.316208 
    C130.662292,63.679485 135.373016,63.334919 140.544907,63.428566 
    C141.043716,65.610085 141.081360,67.353394 141.118988,69.096703 
    C141.472244,72.209846 141.825485,75.322983 142.439514,78.681152 
    C142.640671,79.441338 142.581055,79.956490 142.346100,80.820496 
    C140.062347,79.476547 137.953949,77.783760 135.492065,76.062775 
  z" />
  <path fill="#531094" opacity="1.000000" stroke="none" d="
  M67.659760,99.903168 
    C67.156700,100.026787 66.935051,100.019539 66.348526,99.640472 
    C65.699852,98.231606 65.416054,97.194550 65.427368,95.991638 
    C72.637436,85.672821 73.000481,85.520363 82.240517,89.111343 
    C82.661667,89.466072 82.865540,89.703575 83.017235,90.307999 
    C83.047752,91.324486 83.099213,92.000862 83.150673,92.677246 
    C76.744133,92.176811 71.469711,94.103271 67.659760,99.903168 
  z" />
  <path fill="#F14AFE" opacity="1.000000" stroke="none" d="
  M123.015656,40.992264 
    C123.316612,39.886093 123.617569,38.779926 124.084915,37.029755 
    C126.207855,34.479412 128.061737,32.449574 130.155746,30.708576 
    C131.640900,29.473808 133.450378,28.629145 135.115097,27.610355 
    C135.506409,27.471270 135.897720,27.332186 136.597839,27.454552 
    C136.906662,27.716000 136.968994,28.164061 137.075958,28.401690 
    C138.120926,28.761702 139.058960,28.884085 140.239761,29.044865 
    C140.482544,29.083263 140.969452,29.150974 141.084625,29.405609 
    C142.131653,29.785444 143.063492,29.910643 144.271408,30.099964 
    C145.026962,30.449812 145.506454,30.735540 146.055038,31.359610 
    C146.401443,32.820145 146.678726,33.942333 146.598923,34.978645 
    C145.193130,34.399662 144.127701,33.939003 143.098419,33.408257 
    C135.747650,29.617796 128.525742,33.722034 127.582031,41.955681 
    C125.827766,41.579136 124.421707,41.285698 123.015656,40.992264 
  z" />
  <path fill="#7B20B8" opacity="1.000000" stroke="none" d="
  M141.436584,68.993599 
    C141.081360,67.353394 141.043716,65.610085 141.005402,63.433235 
    C151.032639,60.169003 156.324478,52.801731 159.857605,43.262047 
    C160.613174,44.079430 161.153000,45.177895 161.671417,46.604134 
    C157.808807,56.780033 148.980896,62.109882 141.436584,68.993599 
  z" />
  <path fill="#AB34E2" opacity="1.000000" stroke="none" d="
  M83.038170,89.967896 
    C82.865540,89.703575 82.661667,89.466072 82.259712,88.737823 
    C82.023476,87.474220 81.954063,86.728165 81.884651,85.982117 
    C83.308716,85.336449 84.732788,84.690773 86.512337,84.042023 
    C87.492287,84.849037 88.116745,85.659126 88.877129,87.021362 
    C88.992134,87.925514 88.971222,88.277519 88.764915,88.900337 
    C89.713005,90.789871 90.577759,92.720718 92.029099,93.970268 
    C96.872833,98.140526 101.926727,102.066689 106.542435,106.078674 
    C104.217392,104.956001 102.216484,103.895744 100.289536,102.714806 
    C96.156570,100.181915 92.061790,97.586746 87.951370,95.017075 
    C87.951370,95.017075 87.549652,94.835114 87.342911,94.368378 
    C85.770172,92.590393 84.404175,91.279144 83.038170,89.967896 
  z" />
  <path fill="#EF78FE" opacity="1.000000" stroke="none" d="
  M43.925522,145.830811 
    C47.439274,144.906494 49.114285,146.144287 48.946915,149.888458 
    C48.853680,151.974274 49.073326,154.074051 49.005432,156.855408 
    C47.911732,158.349136 46.964569,159.154999 46.017414,159.960876 
    C45.409496,159.529007 44.801579,159.097137 43.896523,158.224167 
    C42.817020,156.511765 42.034653,155.240494 41.252289,153.969208 
    C41.167305,153.234009 41.082321,152.498810 41.382576,151.319397 
    C42.487053,149.193710 43.206287,147.512268 43.925522,145.830811 
  z" />
  <path fill="#E65AFB" opacity="1.000000" stroke="none" d="
  M106.900101,106.086380 
    C101.926727,102.066689 96.872833,98.140526 92.029099,93.970268 
    C90.577759,92.720718 89.713005,90.789871 89.065384,89.042648 
    C89.981415,88.970924 90.411591,89.027718 90.841759,89.084503 
    C90.841759,89.084503 90.911095,89.037682 91.028748,89.391945 
    C93.375572,91.197144 95.604752,92.648079 97.833923,94.099014 
    C97.833923,94.099014 97.903435,94.081161 97.992691,94.448425 
    C99.188477,95.462616 100.294998,96.109558 101.401520,96.756500 
    C101.401520,96.756493 101.741562,96.859840 101.921646,97.324905 
    C103.360916,98.548950 104.620094,99.307938 105.879280,100.066917 
    C105.879280,100.066917 105.944572,100.045898 106.033005,100.402466 
    C108.163284,102.128189 110.205139,103.497337 112.246994,104.866493 
    C112.246994,104.866493 112.634995,104.981895 112.821594,105.455147 
    C113.346489,106.951515 113.684792,107.974625 113.658981,108.981979 
    C111.174988,108.004173 109.055107,107.042122 106.931198,106.073242 
    C106.927177,106.066414 106.900101,106.086380 106.900101,106.086380 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M88.038437,95.341118 
    C92.061790,97.586746 96.156570,100.181915 100.289536,102.714806 
    C102.216484,103.895744 104.217392,104.956001 106.542435,106.078674 
    C106.900101,106.086380 106.927177,106.066414 106.996460,106.406372 
    C108.305237,107.991806 109.663345,109.142319 110.755135,110.506042 
    C112.218468,112.333870 113.475700,114.326691 114.821419,116.248672 
    C105.922775,109.387505 97.024139,102.526329 88.038437,95.341118 
  z" />
  <path fill="#B63FE8" opacity="1.000000" stroke="none" d="
  M59.718170,110.502716 
    C61.538204,114.091400 63.277489,118.130089 65.012833,122.577133 
    C63.192688,124.869034 61.376488,126.752556 59.221786,128.363052 
    C58.749126,127.490608 58.614971,126.891197 58.480816,126.291779 
    C58.687874,125.422211 58.894932,124.552650 59.386559,123.322876 
    C59.789783,122.858841 60.025928,122.717354 60.006809,122.657707 
    C59.923164,122.396790 59.765503,122.159599 59.634705,121.913803 
    C59.635609,118.260109 59.636517,114.606415 59.718170,110.502716 
  M62.523151,120.495300 
    C62.523151,120.495300 62.486084,120.508423 62.523151,120.495300 
  z" />
  <path fill="#C13BF2" opacity="1.000000" stroke="none" d="
  M135.999390,102.998955 
    C135.870071,102.765541 135.720474,102.545929 135.365250,101.952072 
    C135.179871,101.564026 135.033768,101.098900 135.033768,101.098900 
    C135.081345,97.056198 135.128906,93.013496 135.244904,88.515167 
    C140.870712,90.556366 138.711075,96.020821 139.750977,100.702431 
    C138.353989,101.822624 137.176697,102.410789 135.999390,102.998955 
  z" />
  <path fill="#C744EA" opacity="1.000000" stroke="none" d="
  M134.750870,27.586445 
    C133.450378,28.629145 131.640900,29.473808 130.155746,30.708576 
    C128.061737,32.449574 126.207855,34.479412 124.085175,36.682873 
    C122.729347,37.798561 121.539650,38.617138 120.177383,39.704700 
    C119.796310,39.951084 119.587799,39.928478 119.066269,39.870918 
    C121.697433,32.857269 127.190384,29.125095 134.750870,27.586445 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M114.023094,108.997742 
    C113.684792,107.974625 113.346489,106.951515 112.954659,105.607651 
    C116.625038,106.802406 120.348953,108.317902 124.412689,109.933838 
    C122.605141,110.958862 120.457779,111.883446 117.749329,112.835739 
    C116.133194,111.574883 115.078140,110.286308 114.023094,108.997742 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M43.962532,145.483200 
    C43.206287,147.512268 42.487053,149.193710 41.441132,150.951691 
    C39.653011,146.068146 42.167591,142.247849 45.025864,138.266815 
    C44.885578,140.441422 44.442558,142.788513 43.962532,145.483200 
  z" />
  <path fill="#AB34E2" opacity="1.000000" stroke="none" d="
  M113.658981,108.981979 
    C115.078140,110.286308 116.133194,111.574883 117.484589,112.962814 
    C117.820511,113.491302 117.860100,113.920418 117.905869,114.673080 
    C117.279320,115.374535 116.646591,115.752457 115.745445,116.392487 
    C115.477020,116.654602 115.084503,116.555908 114.952957,116.402290 
    C113.475700,114.326691 112.218468,112.333870 110.755135,110.506042 
    C109.663345,109.142319 108.305237,107.991806 107.000481,106.413200 
    C109.055107,107.042122 111.174988,108.004173 113.658981,108.981979 
  z" />
  <path fill="#C744EA" opacity="1.000000" stroke="none" d="
  M140.969452,29.150974 
    C140.969452,29.150974 140.482544,29.083263 139.984009,28.844193 
    C138.646652,28.458101 137.807816,28.311081 136.968994,28.164061 
    C136.968994,28.164061 136.906662,27.716000 136.912384,27.489910 
    C142.723007,26.380198 147.844543,28.026756 152.633133,31.764065 
    C151.699203,31.805487 150.613632,31.550232 148.850525,31.163826 
    C147.443954,31.028872 146.714935,31.025068 145.985931,31.021267 
    C145.506454,30.735540 145.026962,30.449812 144.018463,29.893719 
    C142.649429,29.465891 141.809448,29.308434 140.969452,29.150974 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M54.993225,132.641602 
    C52.243279,134.312408 49.543140,135.666397 46.490139,137.041153 
    C48.933094,134.925781 51.728916,132.789658 54.845428,130.530426 
    C55.125088,131.046478 55.084061,131.685623 54.993225,132.641602 
  z" />
  <path fill="#BB3BEE" opacity="1.000000" stroke="none" d="
  M67.999268,51.986420 
    C65.903816,51.758236 63.808361,51.530056 60.967896,51.173904 
    C59.652931,50.923218 59.082977,50.800495 58.513023,50.677773 
    C61.517422,50.490822 64.521820,50.303875 67.798264,50.672737 
    C68.046623,51.481171 68.022942,51.733795 67.999268,51.986420 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M97.699539,93.799789 
    C95.604752,92.648079 93.375572,91.197144 91.051620,89.426971 
    C93.159615,90.572006 95.362381,92.036285 97.699539,93.799789 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M112.105087,104.565155 
    C110.205139,103.497337 108.163284,102.128189 106.032356,100.436752 
    C107.949913,101.497589 109.956551,102.880707 112.105087,104.565155 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M83.017235,90.307999 
    C84.404175,91.279144 85.770172,92.590393 87.170471,94.230972 
    C86.041656,94.046822 84.878555,93.533356 83.433060,92.848572 
    C83.099213,92.000862 83.047752,91.324486 83.017235,90.307999 
  z" />
  <path fill="#7325AB" opacity="1.000000" stroke="none" d="
  M44.404278,59.855682 
    C43.832928,61.791386 42.962986,63.884289 41.791718,66.108833 
    C42.362160,64.164612 43.233921,62.088749 44.404278,59.855682 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M116.411209,120.377289 
    C116.699066,121.881203 116.847702,123.732239 116.736679,125.819138 
    C116.408676,124.278137 116.340332,122.501274 116.411209,120.377289 
  z" />
  <path fill="#A030D9" opacity="1.000000" stroke="none" d="
  M85.614403,66.614746 
    C85.394798,66.961807 85.151085,66.993301 84.362190,66.877655 
    C83.554375,66.483879 83.291725,66.237236 83.029083,65.990593 
    C83.036072,64.743546 83.043068,63.496494 83.294525,62.045990 
    C83.943428,62.466774 84.347870,63.091015 84.835564,64.218468 
    C84.918823,64.721687 85.119415,65.129379 85.119415,65.129379 
    C85.276375,65.519310 85.433327,65.909241 85.614403,66.614746 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M41.003639,154.131256 
    C42.034653,155.240494 42.817020,156.511765 43.644104,158.102554 
    C43.377178,158.522491 43.065533,158.622925 42.276035,158.842117 
    C41.450455,157.405014 41.102726,155.849152 41.003639,154.131256 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M105.761078,99.774475 
    C104.620094,99.307938 103.360916,98.548950 102.029968,97.465775 
    C103.186424,97.921730 104.414650,98.701881 105.761078,99.774475 
  z" />
  <path fill="#BB3BEE" opacity="1.000000" stroke="none" d="
  M77.150818,54.585518 
    C75.864532,54.239861 74.440666,53.586483 72.975906,52.571571 
    C74.294426,52.899292 75.653831,53.588547 77.150818,54.585518 
  z" />
  <path fill="#D341FA" opacity="1.000000" stroke="none" d="
  M58.365028,50.646061 
    C59.082977,50.800495 59.652931,50.923218 60.652512,51.133495 
    C59.642139,51.820381 58.202141,52.419704 56.386696,53.015503 
    C56.563656,52.447365 57.116058,51.882748 57.836845,51.074375 
    C58.005230,50.830616 58.217030,50.614349 58.365028,50.646061 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M101.255341,96.469086 
    C100.294998,96.109558 99.188477,95.462616 97.999481,94.483658 
    C98.981064,94.828316 100.045120,95.504997 101.255341,96.469086 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M58.242676,126.511215 
    C58.614971,126.891197 58.749126,127.490608 58.941597,128.546829 
    C58.175842,129.299881 57.351768,129.596146 56.198071,129.912689 
    C56.580479,128.865524 57.292507,127.798080 58.242676,126.511215 
  z" />
  <path fill="#A435DB" opacity="1.000000" stroke="none" d="
  M148.522644,108.488434 
    C149.883331,108.987732 151.053970,109.674019 152.406616,110.658203 
    C152.588654,110.956100 152.181107,110.952560 151.761078,110.995422 
    C151.341034,111.038284 150.900330,111.061768 150.641708,110.916336 
    C149.575638,110.199791 148.768204,109.628685 147.960754,109.057587 
    C148.084702,108.930191 148.208664,108.802803 148.522644,108.488434 
  z" />
  <path fill="#D341FA" opacity="1.000000" stroke="none" d="
  M68.169067,52.144585 
    C68.022942,51.733795 68.046623,51.481171 68.091904,50.848534 
    C68.543060,50.566345 68.972610,50.664165 69.698929,51.173954 
    C69.999832,51.758701 70.003983,51.931484 70.008133,52.104267 
    C69.451714,52.170429 68.895287,52.236588 68.169067,52.144585 
  z" />
  <path fill="#BB46DB" opacity="1.000000" stroke="none" d="
  M90.649246,88.877869 
    C90.411591,89.027718 89.981415,88.970924 89.250778,88.771835 
    C88.971222,88.277519 88.992134,87.925514 89.021072,87.306580 
    C89.504974,87.583511 89.980850,88.127373 90.649246,88.877869 
  z" />
  <path fill="#BB3BEE" opacity="1.000000" stroke="none" d="
  M79.767166,56.754128 
    C79.365730,57.030319 78.889717,57.022827 78.051628,56.989174 
    C77.774048,56.726562 77.858528,56.490112 78.097153,55.909767 
    C78.731728,55.867397 79.212151,56.168922 79.767166,56.754128 
  z" />
  <path fill="#5E1B99" opacity="1.000000" stroke="none" d="
  M41.399612,159.169418 
    C41.645008,159.360794 41.828278,159.752960 42.050613,160.467575 
    C41.838943,160.316757 41.588215,159.843475 41.399612,159.169418 
  z" />
  <path fill="#6519A6" opacity="1.000000" stroke="none" d="
  M117.249413,44.965485 
    C117.249413,44.965485 116.930161,45.199070 116.736526,45.238091 
    C116.596130,44.708233 116.649361,44.139359 116.912468,43.637177 
    C117.164696,44.124409 117.207054,44.544949 117.249413,44.965485 
  z" />
  <path fill="#581797" opacity="1.000000" stroke="none" d="
  M116.480591,130.110077 
    C116.721603,129.717834 116.921463,129.541290 117.465790,129.544159 
    C117.866241,130.152802 117.922218,130.582031 117.841827,131.035645 
    C117.705467,131.060028 117.430222,131.028427 117.430222,131.028427 
    C117.099960,130.794205 116.769691,130.559998 116.480591,130.110077 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M59.471458,122.057144 
    C59.765503,122.159599 59.923164,122.396790 60.006809,122.657707 
    C60.025928,122.717354 59.789783,122.858841 59.487427,123.002838 
    C59.163528,122.761406 59.165024,122.480568 59.471458,122.057144 
  z" />
  <path fill="#C744EA" opacity="1.000000" stroke="none" d="
  M118.625366,39.981831 
    C118.676468,40.371246 118.462631,40.958904 118.066208,41.803055 
    C118.042557,41.433056 118.201492,40.806564 118.625366,39.981831 
  z" />
  <path fill="#581797" opacity="1.000000" stroke="none" d="
  M160.685089,120.846123 
    C160.497940,121.107582 160.321976,121.092476 159.880966,121.037956 
    C159.667221,120.597771 159.718521,120.197006 159.810532,119.496964 
    C160.132935,119.654991 160.414612,120.112282 160.685089,120.846123 
  z" />
  <path fill="#962BD2" opacity="1.000000" stroke="none" d="
  M117.384872,44.657940 
    C117.207054,44.544949 117.164696,44.124409 117.072525,43.390427 
    C117.022713,43.076977 117.206917,42.655434 117.380066,42.504314 
    C117.542259,43.018929 117.531288,43.684662 117.384872,44.657940 
  z" />
  <path fill="#C744EA" opacity="1.000000" stroke="none" d="
  M154.193756,32.645435 
    C154.237350,32.572681 154.303955,32.732666 154.350586,32.733902 
    C154.397202,32.735134 154.150162,32.718189 154.193756,32.645435 
  z" />
  <path fill="#6519A6" opacity="1.000000" stroke="none" d="
  M134.704666,78.002762 
    C134.843704,78.050270 134.903732,78.242210 134.946838,78.735039 
    C134.679138,78.796150 134.577728,78.499908 134.704666,78.002762 
  z" />
  <path fill="#581797" opacity="1.000000" stroke="none" d="
  M118.595749,131.910736 
    C118.389763,131.782608 118.183784,131.654465 117.673187,131.320404 
    C117.368576,131.114456 117.402946,131.074799 117.416580,131.051605 
    C117.430222,131.028427 117.705467,131.060028 117.961227,131.175385 
    C118.386986,131.470688 118.513245,131.677353 118.595749,131.910736 
  z" />
  <path fill="#BB3BEE" opacity="1.000000" stroke="none" d="
  M70.402069,52.000893 
    C70.003983,51.931484 69.999832,51.758701 69.994141,51.326691 
    C70.375656,51.103725 70.758720,51.139988 71.347626,51.387085 
    C71.300980,51.697781 71.048492,51.797649 70.402069,52.000893 
  z" />
  <path fill="#7B22B8" opacity="1.000000" stroke="none" d="
  M85.191437,65.013184 
    C85.119415,65.129379 84.918823,64.721687 84.892944,64.496231 
    C85.147278,64.376114 85.279411,64.584854 85.191437,65.013184 
  z" />
  <path fill="#A435DB" opacity="1.000000" stroke="none" d="
  M134.878052,101.227615 
    C135.033768,101.098900 135.179871,101.564026 135.232956,101.802704 
    C135.286041,102.041382 134.827728,102.100563 134.597290,102.085815 
    C134.411545,101.796104 134.530029,101.557854 134.878052,101.227615 
  z" />
  <path fill="#A030D9" opacity="1.000000" stroke="none" d="
  M84.160011,68.925789 
    C84.200371,70.095284 84.240723,71.264771 83.863144,72.899963 
    C82.627625,74.903427 81.810043,76.441177 80.992462,77.978935 
    C80.992462,77.978935 80.996689,78.000214 80.617645,78.025368 
    C76.822319,79.691757 73.406036,81.332993 69.989761,82.974228 
    C69.547783,82.989929 69.105804,83.005630 68.199043,82.729553 
    C63.146244,81.963264 58.558224,81.488739 53.900978,81.110046 
    C53.721733,81.428841 53.743530,81.640816 53.923782,82.135025 
    C53.970734,82.623466 53.991058,82.818695 54.011387,83.013931 
    C53.019203,83.057312 52.027020,83.100693 50.530640,82.855240 
    C49.982155,82.375778 49.937866,82.185150 50.139069,81.772552 
    C50.658764,80.721848 50.932972,79.893105 51.604744,79.019325 
    C55.397156,78.903458 58.793182,78.740334 62.186577,78.783615 
    C67.176613,78.847267 72.441505,80.081734 76.022041,75.021004 
    C77.141411,74.407730 78.260780,73.794456 80.010948,73.004311 
    C81.814499,71.526886 82.987259,70.226341 84.160011,68.925789 
  z" />
  <path fill="#AD36E8" opacity="1.000000" stroke="none" d="
  M75.595039,75.025162 
    C72.441505,80.081734 67.176613,78.847267 62.186577,78.783615 
    C58.793182,78.740334 55.397156,78.903458 51.541294,78.675514 
    C51.040020,77.913879 50.999756,77.451004 50.959492,76.988136 
    C54.438313,76.521652 57.904903,75.894646 61.398983,75.628479 
    C65.977318,75.279716 70.577339,75.215775 75.595039,75.025162 
  z" />
  <path fill="#F079FE" opacity="1.000000" stroke="none" d="
  M49.893581,81.994530 
    C49.937866,82.185150 49.982155,82.375778 50.158943,82.829567 
    C49.735031,83.372696 49.178623,83.652657 48.088833,83.979668 
    C47.368732,84.021362 47.182011,84.016022 46.995293,84.010674 
    C43.396835,80.718208 41.625519,76.798447 42.906502,71.462341 
    C43.153206,71.116867 43.316856,71.168320 44.020744,71.382683 
    C45.400089,71.634064 46.239201,71.722534 47.078312,71.811005 
    C47.306961,72.060799 47.535614,72.310585 47.918236,73.164703 
    C48.679333,76.510857 49.286457,79.252693 49.893581,81.994530 
  z" />
  <path fill="#CC56F6" opacity="1.000000" stroke="none" d="
  M50.139069,81.772552 
    C49.286457,79.252693 48.679333,76.510857 48.066467,73.371323 
    C48.901093,74.135422 49.741463,75.297234 50.770664,76.723587 
    C50.999756,77.451004 51.040020,77.913879 51.143730,78.720558 
    C50.932972,79.893105 50.658764,80.721848 50.139069,81.772552 
  z" />
  <path fill="#AD36E8" opacity="1.000000" stroke="none" d="
  M84.158585,68.628113 
    C82.987259,70.226341 81.814499,71.526886 80.314529,72.900986 
    C80.864594,70.832588 81.741867,68.690643 82.824112,66.269646 
    C83.291725,66.237236 83.554375,66.483879 83.998169,66.935715 
    C84.171944,67.537415 84.164551,67.933929 84.158585,68.628113 
  z" />
  <path fill="#CC56F6" opacity="1.000000" stroke="none" d="
  M46.957855,71.549171 
    C46.239201,71.722534 45.400089,71.634064 44.276981,71.406296 
    C44.941120,71.273781 45.889259,71.280563 46.957855,71.549171 
  z" />
  <path fill="#9F2FD9" opacity="1.000000" stroke="none" d="
  M56.931591,149.047302 
    C60.992363,149.336288 65.068565,149.948395 69.106316,149.755478 
    C70.724609,149.678162 72.258286,147.829697 74.339645,146.427338 
    C77.194893,145.687759 79.540962,145.308243 81.887032,144.928741 
    C81.913795,145.699554 81.940559,146.470398 81.609009,147.699585 
    C76.164452,150.450760 71.078201,152.743576 65.991951,155.036377 
    C65.551605,155.041824 65.111267,155.047256 64.110184,154.872650 
    C62.702202,155.116669 61.854950,155.540756 61.007694,155.964828 
    C59.612339,155.974518 58.216991,155.984207 56.144638,155.779266 
    C50.513874,152.169861 54.435375,150.768646 56.931591,149.047302 
  z" />
  <path fill="#B734F4" opacity="1.000000" stroke="none" d="
  M81.900314,144.550140 
    C79.540962,145.308243 77.194893,145.687759 74.440903,146.090668 
    C74.020248,145.915573 74.007523,145.717102 73.974701,145.220123 
    C74.299652,141.890594 74.644707,138.859604 75.002289,135.389069 
    C77.088448,136.921356 79.162079,138.893204 81.530746,141.007568 
    C81.855049,142.157257 81.884323,143.164413 81.900314,144.550140 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M56.710815,148.813370 
    C54.435375,150.768646 50.513874,152.169861 55.726021,155.775253 
    C52.784393,157.638199 50.892612,162.108398 46.105392,160.246185 
    C46.964569,159.154999 47.911732,158.349136 49.078133,157.309570 
    C49.899910,155.152039 50.589451,153.250320 51.084927,151.299301 
    C51.860378,148.245834 53.051800,146.240417 56.710815,148.813370 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M66.323608,155.236313 
    C71.078201,152.743576 76.164452,150.450760 81.592918,148.085220 
    C78.716064,153.631912 72.699760,156.554947 66.323608,155.236313 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M61.330746,155.958389 
    C61.854950,155.540756 62.702202,155.116669 63.779919,154.868561 
    C63.224854,155.347015 62.439323,155.649475 61.330746,155.958389 
  z" />
  <path fill="#FB61FE" opacity="1.000000" stroke="none" d="
  M127.930237,42.038792 
    C128.525742,33.722034 135.747650,29.617796 143.098419,33.408257 
    C144.127701,33.939003 145.193130,34.399662 146.605560,35.396095 
    C146.317902,39.606438 145.666504,43.313457 145.015121,47.020477 
    C143.596863,47.701790 142.178589,48.383106 139.966400,49.052185 
    C130.384872,48.893105 129.395096,48.276711 127.930237,42.038792 
  M142.292679,36.065334 
    C140.873306,35.711113 139.349884,34.849773 138.057617,35.114948 
    C135.807938,35.576580 132.584015,36.180756 131.814377,37.736977 
    C130.834488,39.718342 131.053726,43.310089 132.327225,45.071884 
    C133.376907,46.524014 136.778961,46.951813 139.024536,46.721607 
    C143.592606,46.253319 144.946396,42.257790 142.292679,36.065334 
  z" />
  <path fill="#E346FE" opacity="1.000000" stroke="none" d="
  M127.582031,41.955681 
    C129.395096,48.276711 130.384872,48.893105 139.613953,49.071678 
    C134.436172,53.434261 125.896111,49.726406 123.034180,41.356773 
    C124.421707,41.285698 125.827766,41.579136 127.582031,41.955681 
  z" />
  <path fill="#E346FE" opacity="1.000000" stroke="none" d="
  M145.340683,46.903854 
    C145.666504,43.313457 146.317902,39.606438 146.962646,35.481972 
    C146.678726,33.942333 146.401443,32.820145 146.055038,31.359608 
    C146.714935,31.025068 147.443954,31.028872 148.534378,31.047632 
    C150.270782,36.807632 151.135956,42.447968 145.340683,46.903854 
  z" />
  <path fill="#FC7DFF" opacity="1.000000" stroke="none" d="
  M59.390804,137.494507 
    C62.330544,134.332031 65.618294,135.024796 68.283844,136.664719 
    C69.703651,137.538239 70.814278,140.219940 70.651184,141.952454 
    C70.517868,143.368683 68.491180,145.356873 66.954620,145.759933 
    C60.554127,147.438934 57.238651,143.872665 59.390804,137.494507 
  z" />
  <path fill="#FE8FFE" opacity="1.000000" stroke="none" d="
  M58.898018,66.957420 
    C57.018555,58.779259 60.069546,55.289955 66.732155,57.538837 
    C69.445686,58.454754 72.008842,59.671177 71.383400,63.480083 
    C70.781357,67.146538 69.012184,69.362381 65.125870,68.924049 
    C63.092590,68.694717 61.127747,67.858650 58.898018,66.957420 
  z" />
  <path fill="#A933E1" opacity="1.000000" stroke="none" d="
  M150.900330,111.061768 
    C150.900330,111.061768 151.341034,111.038284 151.559402,111.024673 
    C158.393677,116.890129 154.692215,124.368591 146.749023,128.892090 
    C142.300674,131.425354 136.855804,132.249466 131.813934,133.681717 
    C129.491180,134.341522 127.058052,134.612747 124.312408,135.145111 
    C123.778572,135.148529 123.607292,135.067047 123.189606,134.840454 
    C124.032097,132.922272 124.905167,130.950958 126.286766,129.446732 
    C127.188446,128.465027 128.781082,127.819267 130.148193,127.630089 
    C132.510986,127.303131 134.939117,127.448120 138.026886,127.107986 
    C140.450974,126.086548 142.188019,125.352226 144.125793,124.467125 
    C144.792786,123.832169 145.259018,123.348000 146.085861,122.800125 
    C151.532410,120.218765 150.980881,115.550430 150.900330,111.061768 
  z" />
  <path fill="#962BD2" opacity="1.000000" stroke="none" d="
  M120.067184,55.115822 
    C120.114098,55.533066 120.106827,55.866417 119.798737,55.976757 
    C119.318245,56.069057 119.145828,56.051014 118.973404,56.032970 
    C118.358704,53.910797 117.744011,51.788624 117.178802,49.290558 
    C118.158943,50.842640 119.089607,52.770611 120.067184,55.115822 
  z" />
  <path fill="#7A1CC4" opacity="1.000000" stroke="none" d="
  M65.132248,96.157501 
    C65.416054,97.194550 65.699852,98.231606 66.020126,99.587463 
    C63.557194,101.914398 61.993977,100.307686 60.261467,98.220863 
    C60.025375,97.539444 60.019665,97.102257 60.188507,96.076416 
    C60.359043,94.699432 60.328995,93.910202 60.356850,93.123016 
    C60.403660,91.799988 60.197655,90.349739 60.699116,89.219765 
    C60.897491,88.772736 63.166180,88.576050 63.675053,89.084007 
    C64.547745,89.955132 64.960022,91.432655 65.222633,92.725266 
    C65.444664,93.818115 65.180969,95.009644 65.132248,96.157501 
  z" />
  <path fill="#DA47FC" opacity="1.000000" stroke="none" d="
  M135.996216,103.403702 
    C137.176697,102.410789 138.353989,101.822624 139.808792,101.037323 
    C140.713821,102.294296 141.341354,103.748428 142.051971,105.902626 
    C142.952530,107.972168 143.864380,109.295021 144.568588,110.720459 
    C146.205597,114.034019 148.621399,117.307671 145.498596,120.768883 
    C144.873230,116.576363 144.513641,112.695267 139.425018,112.055046 
    C132.786514,111.219826 129.399139,115.573669 130.934784,123.069382 
    C130.503113,123.060631 130.071442,123.051880 129.316162,123.027786 
    C126.094017,116.747681 126.892166,114.809059 132.306763,110.574554 
    C134.163651,109.122368 134.799393,106.108711 135.996216,103.403702 
  z" />
  <path fill="#F76AFE" opacity="1.000000" stroke="none" d="
  M131.121277,123.217606 
    C129.399139,115.573669 132.786514,111.219826 139.425018,112.055046 
    C144.513641,112.695267 144.873230,116.576363 145.523438,121.059738 
    C145.705170,122.084892 145.715210,122.474358 145.725250,122.863831 
    C145.259018,123.348000 144.792786,123.832169 143.768295,124.315735 
    C139.455551,124.233940 135.701035,124.152748 131.946533,124.071564 
    C131.755569,123.816444 131.542648,123.581207 131.121277,123.217606 
  M141.661270,116.110741 
    C139.437897,112.689125 136.631241,114.256035 134.498093,115.817993 
    C133.574539,116.494240 133.278458,120.014992 133.828430,120.342133 
    C135.456543,121.310555 137.871979,122.024452 139.542099,121.484642 
    C140.693329,121.112549 141.117783,118.491837 141.661270,116.110741 
  z" />
  <path fill="#DA47FC" opacity="1.000000" stroke="none" d="
  M132.100052,124.381592 
    C135.701035,124.152748 139.455551,124.233940 143.567551,124.466515 
    C142.188019,125.352226 140.450974,126.086548 138.355148,126.892456 
    C136.082092,126.206566 134.167831,125.449089 132.100052,124.381592 
  z" />
  <path fill="#A933E1" opacity="1.000000" stroke="none" d="
  M118.850525,132.044418 
    C118.513245,131.677353 118.386986,131.470688 118.097588,131.151016 
    C117.922218,130.582031 117.866241,130.152802 117.838928,129.400055 
    C118.599831,130.060455 119.332062,131.044373 120.095444,132.358429 
    C119.786171,132.518433 119.445732,132.348267 118.850525,132.044418 
  z" />
  <path fill="#C13BF2" opacity="1.000000" stroke="none" d="
  M146.085876,122.800125 
    C145.715210,122.474358 145.705170,122.084892 145.670258,121.404556 
    C148.621399,117.307671 146.205597,114.034019 144.568588,110.720459 
    C143.864380,109.295021 142.952530,107.972168 142.142609,106.231209 
    C143.871246,106.864357 145.592300,107.868996 147.637054,108.965607 
    C148.768204,109.628685 149.575638,110.199791 150.641708,110.916336 
    C150.980881,115.550430 151.532410,120.218765 146.085876,122.800125 
  z" />
  <path fill="#731CB7" opacity="1.000000" stroke="none" d="
  M65.427368,95.991638 
    C65.180969,95.009644 65.444664,93.818115 65.222633,92.725266 
    C64.960022,91.432655 64.547745,89.955132 63.675053,89.084007 
    C63.166180,88.576050 60.897491,88.772736 60.699116,89.219765 
    C60.197655,90.349739 60.403660,91.799988 60.356850,93.123016 
    C60.328995,93.910202 60.359043,94.699432 60.187267,95.748352 
    C58.391300,93.888962 56.771130,91.768982 55.070045,89.317535 
    C56.055328,88.078224 57.085365,86.435387 58.193539,86.380882 
    C65.819550,86.005737 73.461891,85.962570 81.491821,85.897354 
    C81.954063,86.728165 82.023476,87.474220 82.073685,88.593788 
    C73.000481,85.520363 72.637436,85.672821 65.427368,95.991638 
  z" />
  <path fill="#932BD0" opacity="1.000000" stroke="none" d="
  M54.413757,83.105927 
    C53.991058,82.818695 53.970734,82.623466 53.943775,81.929413 
    C53.937141,81.430573 53.970207,81.014221 53.970207,81.014221 
    C58.558224,81.488739 63.146244,81.963264 67.867378,82.734230 
    C63.605705,83.086426 59.210915,83.142174 54.413757,83.105927 
  z" />
  <path fill="#932BD0" opacity="1.000000" stroke="none" d="
  M70.439255,82.986420 
    C73.406036,81.332993 76.822319,79.691757 80.607315,78.021317 
    C80.508507,85.493713 74.723244,82.280914 70.439255,82.986420 
  z" />
  <path fill="#932BD0" opacity="1.000000" stroke="none" d="
  M81.284248,77.806076 
    C81.810043,76.441177 82.627625,74.903427 83.733665,73.184814 
    C83.206757,74.547050 82.391396,76.090134 81.284248,77.806076 
  z" />
  <path fill="#932BD0" opacity="1.000000" stroke="none" d="
  M47.171368,84.245834 
    C47.182011,84.016022 47.368732,84.021362 47.817604,84.128510 
    C48.079762,84.230301 48.231579,84.612534 48.320946,84.800415 
    C48.056019,84.819191 47.701733,84.650085 47.171368,84.245834 
  z" />
  <path fill="#7E1DC8" opacity="1.000000" stroke="none" d="
  M119.079712,56.142712 
    C119.145828,56.051014 119.318245,56.069057 119.745255,56.134659 
    C119.999855,56.182224 119.604782,56.367851 119.604782,56.367851 
    C119.604782,56.367851 119.186020,56.252453 119.079712,56.142712 
  z" />
  <path fill="#E346FE" opacity="1.000000" stroke="none" d="
  M141.084625,29.405609 
    C141.809448,29.308434 142.649429,29.465891 143.742371,29.829596 
    C143.063492,29.910643 142.131653,29.785444 141.084625,29.405609 
  z" />
  <path fill="#E346FE" opacity="1.000000" stroke="none" d="
  M137.075958,28.401690 
    C137.807816,28.311081 138.646652,28.458101 139.741226,28.805794 
    C139.058960,28.884085 138.120926,28.761702 137.075958,28.401690 
  z" />
  <path fill="#9D34CF" opacity="1.000000" stroke="none" d="
  M62.504616,120.501862 
    C62.486084,120.508423 62.523151,120.495300 62.504616,120.501862 
  z" />
  <path fill="#AD36E8" opacity="1.000000" stroke="none" d="
  M53.900978,81.110046 
    C53.970207,81.014221 53.937141,81.430573 53.917145,81.636192 
    C53.743530,81.640816 53.721733,81.428841 53.900978,81.110046 
  z" />
  <path fill="#FE89FF" opacity="1.000000" stroke="none" d="
  M142.584991,36.352379 
    C144.946396,42.257790 143.592606,46.253319 139.024536,46.721607 
    C136.778961,46.951813 133.376907,46.524014 132.327225,45.071884 
    C131.053726,43.310089 130.834488,39.718342 131.814377,37.736977 
    C132.584015,36.180756 135.807938,35.576580 138.057617,35.114948 
    C139.349884,34.849773 140.873306,35.711113 142.584991,36.352379 
  M133.394180,39.005192 
    C133.954269,40.872196 134.027267,43.798290 135.198303,44.336876 
    C136.646851,45.003094 139.302475,44.117641 140.852158,43.052414 
    C141.664490,42.494034 141.744156,38.982006 141.264709,38.764362 
    C139.358444,37.899002 137.108063,37.757847 134.968460,37.474327 
    C134.620483,37.428215 134.188293,38.017612 133.394180,39.005192 
  z" />
  <path fill="#FF92FF" opacity="1.000000" stroke="none" d="
  M141.764160,116.493408 
    C141.117783,118.491837 140.693329,121.112549 139.542099,121.484642 
    C137.871979,122.024452 135.456543,121.310555 133.828430,120.342133 
    C133.278458,120.014992 133.574539,116.494240 134.498093,115.817993 
    C136.631241,114.256035 139.437897,112.689125 141.764160,116.493408 
  z" />
  <path fill="#FFA5FF" opacity="1.000000" stroke="none" d="
  M133.594604,38.659229 
    C134.188293,38.017612 134.620483,37.428215 134.968460,37.474327 
    C137.108063,37.757847 139.358444,37.899002 141.264709,38.764362 
    C141.744156,38.982006 141.664490,42.494034 140.852158,43.052414 
    C139.302475,44.117641 136.646851,45.003094 135.198303,44.336876 
    C134.027267,43.798290 133.954269,40.872196 133.594604,38.659229 
  z" />
  </svg>;

export const OrumLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M22.7819 6.8553C21.7787 7.85886 20.7966 8.83673 19.8208 9.82077C19.6587 9.98421 19.535 10.0861 19.2747 9.95795C16.5689 8.62614 13.7043 7.94733 10.6877 7.91247C10.6585 7.91213 10.6294 7.90053 10.5361 7.88022C10.6342 7.76154 10.7066 7.65812 10.7944 7.57019C12.8728 5.48925 14.9545 3.41162 17.0297 1.32757C17.2107 1.14581 17.3447 1.06323 17.6142 1.20662C19.8832 2.414 21.6165 4.14789 22.7987 6.42823C22.8541 6.53511 22.8054 6.69596 22.7819 6.8553Z" fill="#FAFE70" />
  <path d="M8.19869 0.505913C8.85903 0.339915 9.48678 0.193188 10.1088 0.0252183C10.3434 -0.0381412 10.4654 0.0125958 10.5779 0.237928C11.2021 1.48841 11.8485 2.72784 12.4698 3.9797C12.5269 4.09465 12.5216 4.32895 12.4437 4.40961C10.3052 6.6219 8.76037 9.19331 7.74179 12.1969C7.37663 11.4924 7.04816 10.868 6.72797 10.2393C5.66144 8.14526 4.6031 6.04702 3.52704 3.95791C3.38158 3.67549 3.41241 3.50739 3.64097 3.28785C4.94792 2.03249 6.45176 1.10683 8.19869 0.505913Z" fill="#FBFE70" />
  <path d="M12.8194 23.9837C10.6593 24.089 8.64776 23.6825 6.73345 22.7695C6.42971 22.6246 6.35027 22.4593 6.40633 22.1338C6.62814 20.8458 6.8243 19.5533 7.02687 18.262C7.06568 18.0147 7.08957 17.8208 7.43027 17.7622C10.3706 17.2568 13.0527 16.1166 15.4986 14.4135C15.5471 14.3798 15.6023 14.3556 15.7237 14.2888C15.218 17.4845 14.7222 20.6183 14.2165 23.8142C13.7681 23.8693 13.3156 23.925 12.8194 23.9837Z" fill="#FBFE70" />
  <path d="M23.632 15.3749C23.0417 17.2938 22.0726 18.9453 20.7032 20.3661C20.4846 20.593 20.3198 20.6281 20.0359 20.4774C18.8561 19.8509 17.6645 19.2463 16.4709 18.6462C16.2546 18.5375 16.1352 18.4329 16.1738 18.1628C16.6043 15.1487 16.3466 12.1886 15.415 9.21204C15.5818 9.28012 15.7006 9.31907 15.8108 9.37497C18.4402 10.7091 21.0668 12.0486 23.7 13.3752C23.9693 13.5109 24.0519 13.6559 23.9685 13.9501C23.8389 14.4072 23.7499 14.8759 23.632 15.3749Z" fill="#FBFE70" />
  <path d="M7.15693 16.7412C5.34191 17.0326 3.56721 17.3209 1.78896 17.5853C1.64035 17.6074 1.38698 17.5154 1.31837 17.3973C0.171743 15.4238 -0.311718 12.0863 0.208712 9.78506C1.56721 9.56782 2.94964 9.37508 4.3187 9.11266C4.80614 9.01923 5.00791 9.17146 5.22743 9.57704C6.55596 12.0316 8.3514 14.0945 10.5574 15.802C10.6653 15.8855 10.7708 15.9722 10.9751 16.1356C9.65299 16.3442 8.42465 16.538 7.15693 16.7412Z" fill="#FBFE70" />
</svg>;

export const HubspotLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M17.2421 17.2947C15.4495 17.2947 13.9963 15.8566 13.9963 14.0829C13.9963 12.3088 15.4495 10.8707 17.2421 10.8707C19.0348 10.8707 20.488 12.3088 20.488 14.0829C20.488 15.8566 19.0348 17.2947 17.2421 17.2947ZM18.2138 7.89901V5.04163C18.9675 4.68936 19.4954 3.93487 19.4954 3.05925V2.9933C19.4954 1.78482 18.4963 0.796098 17.2751 0.796098H17.2088C15.9876 0.796098 14.9885 1.78482 14.9885 2.9933V3.05925C14.9885 3.93487 15.5164 4.68966 16.2701 5.04194V7.89901C15.148 8.07068 14.1227 8.52868 13.2772 9.20272L5.34945 3.09994C5.40177 2.90114 5.43852 2.6965 5.43884 2.48137C5.44008 1.11293 4.32076 0.00185084 2.93734 1.60552e-06C1.55455 -0.00153942 0.43149 1.10646 0.429933 2.4752C0.428376 3.84395 1.54769 4.95503 2.93111 4.95657C3.38177 4.95719 3.7991 4.83051 4.16473 4.62463L11.9629 10.6282C11.2998 11.6188 10.9112 12.8053 10.9112 14.0829C10.9112 15.4202 11.3381 16.6573 12.0594 17.6747L9.68813 20.0217C9.50065 19.9659 9.30631 19.9271 9.10013 19.9271C7.96369 19.9271 7.04213 20.8387 7.04213 21.9634C7.04213 23.0883 7.96369 24 9.10013 24C10.2369 24 11.1581 23.0883 11.1581 21.9634C11.1581 21.76 11.1189 21.5673 11.0625 21.3818L13.4083 19.0604C14.4731 19.8645 15.7992 20.3478 17.2421 20.3478C20.7387 20.3478 23.5728 17.5428 23.5728 14.0829C23.5728 10.9506 21.2476 8.36286 18.2138 7.89901Z" fill="#FF7A59" />
  </svg>;

export const GoogleWorkspaceLogo = () => <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
    <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
    <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
    <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
    <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
    <path d="M1 1h22v22H1z" fill="none" />
  </svg>;

export const GoogleTagManagerLogo = () => <svg width="24" height="24" viewBox="0 0 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
    <g>
      <polygon fill="#8AB4F8" points="150.261818 245.516364 105.825455 202.185455 201.258182 104.730909 247.265455 149.821818"></polygon>
      <path d="M150.450909,53.9381818 L106.174545,8.73090909 L9.36,104.629091 C-3.12,117.109091 -3.12,137.341818 9.36,149.836364 L104.72,245.821818 L149.810909,203.64 L77.1563636,127.232727 L150.450909,53.9381818 Z" fill="#4285F4"></path>
      <path d="M246.625455,105.370909 L150.625455,9.37090909 C138.130909,-3.12363636 117.869091,-3.12363636 105.374545,9.37090909 C92.88,21.8654545 92.88,42.1272727 105.374545,54.6218182 L201.374545,150.621818 C213.869091,163.116364 234.130909,163.116364 246.625455,150.621818 C259.12,138.127273 259.12,117.865455 246.625455,105.370909 Z" fill="#8AB4F8"></path>
      <circle fill="#246FDB" cx="127.265455" cy="224.730909" r="31.2727273"></circle>
    </g>
  </svg>;

export const G2Logo = () => <svg width="25" height="25" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g clip-path="url(#clip0_1_13)">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M50 25C50 38.807 38.807 50 25 50C11.193 50 0 38.807 0 25C0 11.193 11.193 0 25 0C38.807 0 50 11.193 50 25Z" fill="#FF492C" />
      <path fill-rule="evenodd" clip-rule="evenodd" d="M35.8349 19.1462H31.5624C31.6784 18.4766 32.0914 18.1031 32.9307 17.6781L33.718 17.2788C35.125 16.5579 35.8736 15.7465 35.8736 14.4199C35.8736 13.5828 35.551 12.9258 34.9055 12.4496C34.2731 11.973 33.4985 11.741 32.6078 11.741C31.8979 11.741 31.2524 11.9214 30.6587 12.2948C30.0779 12.6556 29.6389 13.1192 29.368 13.6986L30.6073 14.9351C31.0847 13.9692 31.7818 13.4926 32.6982 13.4926C33.4728 13.4926 33.9505 13.892 33.9505 14.4455C33.9505 14.9094 33.718 15.2955 32.8273 15.7465L32.3239 15.9911C31.2268 16.5449 30.4652 17.1759 30.0262 17.8971C29.5875 18.6054 29.368 19.5196 29.368 20.6146V20.9108H35.8349V19.1462Z" fill="white" />
      <path fill-rule="evenodd" clip-rule="evenodd" d="M35.2541 22.9554H28.1907L24.6592 29.0736H31.7226L35.2541 35.1921L38.7856 29.0736L35.2541 22.9554Z" fill="white" />
      <path fill-rule="evenodd" clip-rule="evenodd" d="M25.2576 33.1608C20.7546 33.1608 17.0912 29.5 17.0912 25C17.0912 20.5004 20.7546 16.8395 25.2576 16.8395L28.0533 10.9926C27.1493 10.8133 26.2146 10.7187 25.2576 10.7187C17.3649 10.7187 10.9665 17.1128 10.9665 25C10.9665 32.8876 17.3649 39.2813 25.2576 39.2813C28.4044 39.2813 31.3132 38.2643 33.6741 36.5421L30.5779 31.1834C29.1477 32.4141 27.2887 33.1608 25.2576 33.1608Z" fill="white" />
    </g>
    <defs>
      <clipPath id="clip0_1_13">
        <rect width="50" height="50" fill="white" />
      </clipPath>
    </defs>
  </svg>;

export const DemandbaseLogo = () => <svg fill="none" viewBox="0 0 59 70" xmlns="http://www.w3.org/2000/svg" width="25" height="25">
    <path clip-rule="evenodd" d="m.5.0838406h24.3291c18.3824 0 33.3338 12.2211594 33.3338 34.4971594 0 22.2759-14.9514 34.4971-33.3338 34.4971h-24.3291v-35.3464c0-7.9459 6.06871-14.3876 13.5546-14.3876v37.0162h10.2117c10.4015 0 19.7792-7.0966 19.7792-21.7793s-9.3777-21.7794-19.7792-21.7794h-11.7916c-6.61118 0-11.9747-5.6931-11.9747-12.7177594z" fill="#4ca3ff" fill-rule="evenodd" />
  </svg>;

export const ClearbitLogo = () => <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M17.5703 23.9994H6.43997H5.97931C4.10691 23.9697 3.34903 23.7467 2.60602 23.3307C1.7887 22.8997 1.16457 22.2607 0.718762 21.4434L0.6296 21.2651C0.272953 20.5369 0.0649091 19.7196 0.0500488 17.8175V6.40478C0.0500488 4.17574 0.287813 3.37329 0.718762 2.55597C1.14971 1.73865 1.7887 1.09966 2.60602 0.668713L2.78434 0.579553C3.5125 0.222906 4.31495 0.0148603 6.21707 0H17.5703C19.7845 0 20.587 0.237765 21.4043 0.668713C22.2216 1.09966 22.8457 1.73865 23.2915 2.55597L23.3807 2.7343C23.7374 3.46245 23.9454 4.27976 23.9603 6.18188V17.5946V18.0553C23.9305 19.9425 23.7076 20.6855 23.3064 21.4434C22.8755 22.2607 22.2365 22.8997 21.4191 23.3307L21.2408 23.4198C20.4681 23.8062 19.6359 23.9994 17.5703 23.9994Z" fill="#C4D3E0" fill-opacity="0.2" />
    <path d="M23.9452 12.0078V17.5953C23.9452 19.8243 23.7075 20.6268 23.2765 21.4441C22.8456 22.2614 22.2066 22.9004 21.3893 23.3314C20.5719 23.7623 19.7695 24.0001 17.5553 24.0001H11.9976V12.0078H23.9452Z" fill="url(#paint0_linear_239_59)" />
    <path d="M11.9976 0.0146484H17.5553C19.7695 0.0146484 20.5719 0.252413 21.3893 0.683362C22.2066 1.11431 22.8307 1.7533 23.2765 2.57062C23.7075 3.38793 23.9452 4.19039 23.9452 6.41943V12.0069H11.9976V0.0146484Z" fill="url(#paint1_linear_239_59)" />
    <path d="M6.43997 0.0146484H11.9977V23.9992H6.43997C4.22579 23.9992 3.42333 23.7614 2.60602 23.3304C1.7887 22.8995 1.16457 22.2605 0.718762 21.4432C0.287813 20.6259 0.0500488 19.8234 0.0500488 17.5944V6.41943C0.0500488 4.19039 0.287813 3.38793 0.718762 2.57062C1.14971 1.7533 1.7887 1.11431 2.60602 0.683362C3.42333 0.252413 4.22579 0.0146484 6.43997 0.0146484Z" fill="url(#paint2_linear_239_59)" />
    <defs>
      <linearGradient id="paint0_linear_239_59" x1="15.5715" y1="13.2151" x2="21.5827" y2="25.188" gradientUnits="userSpaceOnUse">
        <stop stop-color="#DEF2FE" />
        <stop offset="1" stop-color="#DBF1FE" />
      </linearGradient>
      <linearGradient id="paint1_linear_239_59" x1="13.5922" y1="-0.783111" x2="19.6034" y2="11.1898" gradientUnits="userSpaceOnUse">
        <stop stop-color="#57BCFD" />
        <stop offset="1" stop-color="#51B5FD" />
      </linearGradient>
      <linearGradient id="paint2_linear_239_59" x1="1.70069" y1="1.43981" x2="11.9197" y2="21.7937" gradientUnits="userSpaceOnUse">
        <stop stop-color="#1CA7FD" />
        <stop offset="1" stop-color="#148CFC" />
      </linearGradient>
    </defs>
  </svg>;

<CardGroup cols={2}>
  <Card title="Salesforce" href="/reference/integrations/salesforce/overview" icon={<SalesforceLogo />} cta="Most Popular">
    Connect your Salesforce instance to seamlessly keep your CRM in sync.
  </Card>

  <Card title="HubSpot" href="/reference/integrations/hubspot/overview" icon={<HubspotLogo />} cta="Most Popular">
    Connect your HubSpot instance to seamlessly keep your CRM in sync.
  </Card>

  <Card
    title="6sense"
    href="/reference/integrations/6sense"
    icon={
    <>
      <SixsenseLogoDark />
      <SixsenseLogoLight />
    </>
  }
    horizontal
  >
    Use your existing 6sense subscription to identify visitors.
  </Card>

  <Card title="Clearbit" href="/reference/integrations/clearbit" icon={<ClearbitLogo />} horizontal>
    Connect your existing Clearbit subscription to identify visitors.
  </Card>

  <Card title="Demandbase" href="/reference/integrations/demandbase" icon={<DemandbaseLogo />} horizontal>
    Identify website visitors with Unify's native Demandbase integration.
  </Card>

  <Card title="G2" href="/reference/integrations/g2" icon={<G2Logo />} horizontal>
    Identify anonymous visitors on G2 and use them as an intent source.
  </Card>

  <Card title="Gmail" href="/reference/integrations/gmail" icon={<GoogleWorkspaceLogo />} horizontal>
    Send emails from your existing Google Workspace mailbox.
  </Card>

  <Card title="Google Tag Manager" href="/reference/integrations/google-tag-manager" icon={<GoogleTagManagerLogo />} horizontal>
    Install the Unify website tag using Google Tag Manager.
  </Card>

  <Card title="Nooks" href="/reference/integrations/nooks/overview" icon={<NooksLogo />} horizontal>
    Connect your Nooks dialer to streamline call workflows and sync call tasks.
  </Card>

  <Card title="Orum" href="/reference/integrations/orum/overview" icon={<OrumLogo />} horizontal>
    Connect your Orum dialer to streamline call workflows and sync call tasks.
  </Card>

  <Card title="Segment" href="/reference/integrations/segment" icon={<SegmentIcon />} horizontal>
    Use Segment website analytics to power Plays, Audiences, and more.
  </Card>

  <Card title="Slack" href="/reference/integrations/slack" icon={<SlackLogo />} horizontal>
    Send Slack notifications and messages from Unify Plays.
  </Card>

  <Card title="Snitcher" href="/reference/integrations/snitcher" icon={<SnitcherLogo />} horizontal>
    Identify website visitors with Unify's native Snitcher integration.
  </Card>
</CardGroup>


# How Bidirectional Syncs Work
Source: https://docs.unifygtm.com/reference/integrations/salesforce/bidirectional-syncs

An in-depth explanation of how syncs work between Salesforce and Unify.

# Overview

Unify can create and update Salesforce records in response to Play runs and
sequence enrollments. This page summarizes the rules used to determine when and
how to create or update records in Salesforce.

# Overwriting data

Unify takes a very conservative approach to overwriting existing Salesforce
data in order to make data loss impossible. This approach is based around only
a few simple rules:

* **Creating new records:** When Unify is creating a new Salesforce record, it
  will fill in all fields that are enabled for writing in the field mapping or
  default values.

* **Updating existing records:** Unify will inspect whether the field is empty
  or not. If the field is empty, it will be updated with the new value. If the
  field already has a value, it will only be updated if it is a Unify-specific
  field. These fields are prefixed with "Unify" and can be found [here](/reference/integrations/salesforce/field-mappings#available-fields).

These rules apply regardless of how the record was originally created (e.g., by
Unify or externally). If you're looking for more fine-grained control, you can
also limit the permissions granted to the Unify integration user in Salesforce.

# Duplicate prevention

Duplicates are strictly prevented within Unify. When creating new Salesforce
records, Unify will only ever create one record. If there is already an existing
Salesforce record of the same type, Unify will always update it rather than
creating a new one.

However, duplicates are a common problem in Salesforce and may already exist in
your Salesforce instance. In addition, users or other integrations may
accidentally create new duplicates over time.

In order to accommodate this reality, Unify follows specific rules to ensure
predictable behavior when updating duplicated Salesforce records. While Unify
cannot de-duplicate your Salesforce, it will *never* make the problem worse, and
in some situations may be able to help clarify the “source of truth” record.

### Contacts

Salesforce contacts are written by Unify if **Create new records as Contacts & Accounts**
is selected. In addition, contacts are sometimes created in place of leads if
the person being written to Salesforce *already exists* as a contact. Unify
cannot create a lead in this situation due to Salesforce’s
[contact duplicate rules](https://help.salesforce.com/s/articleView?language=en_US\&id=sf.duplicate_rules_standard_contact_rule.htm\&type=5).

In both situations, if there is an existing contact that matches the Unify
person being written, it will be updated. Matches are determined based on email
address. If there are no matches, a new contact will be created.

If there are multiple contacts that match the Unify person, only one will be
updated. Specifically, the contact that was most recently modified within
Salesforce is the one that will be updated.

### Accounts

Salesforce accounts are written by Unify whenever a contact is created or
updated. They are also written if a Salesforce sync action runs within a Play
that is running on companies.

If there is an existing account that matches the Unify company being written, it
will be updated. Matches are determined based on the domain of the company
website. Domains are normalized, so URLs that redirect to different domains will
not result in duplicates. If there are no matches, a new account will be
created.

If there are multiple accounts that match the Unify company, only one will be
updated. Specifically:

* If one account has more associated contacts than the other(s), that one will
  be updated
* Otherwise, the account that was most recently modified within Salesforce will
  be updated

### Leads

Salesforce leads are written by Unify when **Create new records as Leads** is
selected.

If there is an existing lead that matches the Unify company being written, it
will be updated. Matches are determined based on email address. If there are no
matches, a new lead will be created.

If there are multiple leads that match the Unify person, only one will be
updated. Specifically, the lead that was most recently modified within
Salesforce is the one that will be updated.

### Email Messages

Unify writes to the email message object in Salesforce, which is the recommended
approach for syncing email data to Salesforce. In order to write records of this
object type, the *Enhanced Email* feature must be enabled in Salesforce. This is
typically enabled by default.

Unify does not update existing email messages in Salesforce; only emails sent
through Unify or received in response to those emails will be written to
Salesforce. Unify uses the standard **Universal Message ID** to deduplicate
email messages if they are simultaneously being written by another integration.

Email messages are written to Salesforce for all emails sent as a part of Unify
sequences if the corresponding person already exists in Salesforce. This means
that in order to write email messages for sequence enrollments, you should
ensure that the person already exists in Salesforce or that you include a Play
action to sync them to Salesforce.


# Bulk Update Records
Source: https://docs.unifygtm.com/reference/integrations/salesforce/bulk-update-records

Use Salesforce reports to quickly update a large number of records in Salesforce.

## Explanation

If you need to update a large number of records in Salesforce, you can use Salesforce reports to simplify the process. A common use case is updating the value of a field across all records created by a Play. However, these steps are generally applicable to any set of Salesforce records.

## Steps

### Export the Records

1. Navigate to the **Reports** page.

<Tip>
  In the top-right corner of the screen, if you click the menu icon and search for “reports”, you should see a link to get there.

  <Frame>  <img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=afef402ff19f40bf04f6837b7df2c779" alt="export-the-records-step-1" data-og-width="668" width="668" data-og-height="482" height="482" data-path="images/export-the-records-step-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f2e0c8cd44d0216df28734f565b6ca73 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=807071f0ed3fa433bd0b688318de3565 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d897fc95fbc863a9bce025cd84a55792 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=15ac6dfa5bc377f383e5c7ec19f196fd 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9b660f88fa8c7fc15b7a0d3a53365617 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/export-the-records-step-1.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1fdcf1823721a752d0825dd883fb98fb 2500w" /></Frame>
</Tip>

2. In the top-right corner of the screen, select **New Report**
3. Choose a report type based on which type of records you need to update, and then click **Start Report** on the right

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9f9db7eec6f1d5845e8b2efecd7484a2" alt="export-the-records-step-3" data-og-width="2622" width="2622" data-og-height="1258" height="1258" data-path="images/export-the-records-step-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a0244fdcfb46ccb126c3db20b85b693f 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=be79b54c40f26a86c0525825d355e20e 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ed932fa117ce613c8604eaa52e86217c 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1e5f4e85ab353195921786cb9f7381f5 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b334e0c3f21c18cff2d91b2baca851d1 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-3.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8e74d1e2f183eda6912bb1491a8b2f03 2500w" /></Frame>

4. Be sure to add the `Id` column to your report in the sidebar, which is typically named after the record type you are selecting (e.g., `Account ID`, `Contact ID`, etc.)

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=707665a70b65177b856771e1e5a9ebdd" alt="export-the-records-step-4" data-og-width="594" width="594" data-og-height="716" height="716" data-path="images/export-the-records-step-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f394f459d4c62b5187fde3fad2d61b2b 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b24b78c57d27ea529239dcc5013533eb 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=87581e0cdba1bb02d648eaf1e8cf7270 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c91c78cb3d4c4cf86bb45ef823d545a9 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fc3d7ed62af84deb14fb79c0bf92741b 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-4.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e231a784fe38a2de93c6d2d84b209e5e 2500w" /></Frame>

5. Also add any additional columns that you wish to edit on the records
6. Add any filters or sorting options needed to narrow down the records you want to update

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b47175c0f6adf7f944d2063838e820fa" alt="export-the-records-step-6" data-og-width="2964" width="2964" data-og-height="1394" height="1394" data-path="images/export-the-records-step-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=43e34eab03585487f7c50ab21e371bea 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4aec818dc4c2e73f5a972e5976023657 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fbc778a74599e900fad8098958a62a5b 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=12859826be5cded83bffe3e6601af53e 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4a0e7d08e48b5f0189bbe0220ddca42c 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-6.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aa950de625fb110dc0b1ab6089561864 2500w" /></Frame>

7. When ready, click **Save** in the top-right corner, enter a name, and then click **Save** again

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4a2b828199bff9fad92ab18436226f98" alt="export-the-records-step-7" data-og-width="2108" width="2108" data-og-height="1086" height="1086" data-path="images/export-the-records-step-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a79c0955277aedf78c2899be7a0c74d3 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e544efca2458dd2420597e4b53b89f5c 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=243917aabc7a88d97f96c390ba1acd4e 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ee5d13e4571adc680e8091febc9a7655 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f3712d613e852f111e16c103e621c28f 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-7.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f7c14f37b058337b72e7a06ae8d43e77 2500w" /></Frame>

8. Click **Run** in the top-right corner and verify these are the records you want to update
9. Click the dropdown arrow next to **Edit** in the top-right corner and select **Export**
10. Choose **Details Only** and **Comma Delimited .csv** as the format and then click **Export**

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=18860ea151699b3c55d3a024596d9222" alt="export-the-records-step-10" data-og-width="1322" width="1322" data-og-height="1010" height="1010" data-path="images/export-the-records-step-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=da0bb52f2da3c4808a0eb0a7baea65c9 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=2f590ef7babb8591c6f5947792f6ce16 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b28e893ac6baa11911a288d1a665a1ca 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0d183ae6747d8d428fa05308632a7f5d 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=052bd74eb5b7b1f58e923ab9bf10fd4e 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/export-the-records-step-10.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d7f8cbbb915851fbbf92ac1b015321b1 2500w" /></Frame>

### Make Changes

1. Open the downloaded file and make any desired updates to the values
2. Save the changes as a new file so that the original is available as a backup

### Upload the Changed Records

1. Navigate to the **Setup** page in Salesforce

2. In the sidebar on the left, search for "data import wizard" and select the **Data Import Wizard** integration

3. Follow the on-screen instructions to update existing records and be sure to choose the option to match records by `Salesforce.com ID`

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=748aa079e1209ae40917e693b3ac6fd0" alt="upload-the-changed-records-step-3" data-og-width="2960" width="2960" data-og-height="1464" height="1464" data-path="images/upload-the-changed-records-step-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6a18032e5cabdd1f9e9c262888d4195a 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=189a7133a31db2cf51a47e0ae90e56e1 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a843727cc49f06e5c7387656c9dbcaec 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=98031d55197cb388e7f3841627a7e849 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=bac9e81f6145abfbb58e16bfe3be9f28 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-3.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=80464bf4573415373ad4ce25a6f023ea 2500w" /></Frame>

4. Ensure the mapping looks correct and that the ID column is mapped to `Salesforce.com ID`

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=804c196b99314f990ca59dc55c3093e9" alt="upload-the-changed-records-step-4" data-og-width="2962" width="2962" data-og-height="1468" height="1468" data-path="images/upload-the-changed-records-step-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6ba26340e6c3a7a61663e7ed0e9036d1 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=727e3682837a1f6f0ff6504ce3e9e7d3 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3f200589b67495ffb1ad055929359bd4 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=afae305c76f91909ee70365fb31ab153 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=55af268f3ef02e0453ea23460234baf5 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-4.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=543dadd6fe6f9a97222435c2d90464ae 2500w" /></Frame>

5. Verify the details on the last page and then click **Start Import**

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=664b6da549b8ca2996c3e210cff98d10" alt="upload-the-changed-records-step-5" data-og-width="2960" width="2960" data-og-height="1460" height="1460" data-path="images/upload-the-changed-records-step-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3752a97278de399e328d204d02af70d9 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=62e7a6aa78f69d79b3b30f9e9cd33f05 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=77eadb9166a822a08faf31ac8af1513e 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=62c584fcfd36b05f877f448b43aa8ff5 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=73f639bc4e61d278b0d79761967bf2a9 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/upload-the-changed-records-step-5.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d8502ce81b7797b903c20014df6f93db 2500w" /></Frame>

6. Once this bulk import is complete you’re all finished!


# Configure Default Values
Source: https://docs.unifygtm.com/reference/integrations/salesforce/default-values

Learn how to set default values writing to Salesforce.

# Overview

When Unify creates or updates records in Salesforce, it will populate each
Salesforce field using the value in the corresponding Unify field. However, you
can also specify *default values* to be used as a fallback. This can useful in a
few different scenarios:

1. You may have custom fields in Salesforce that require a value
2. You may want to write a custom value to a field that is not available in the
   field mappings
3. You may want to dynamically set a value in different Plays or Play actions

You can set global default values from [Settings -> Integrations -> Salesforce](https://app.unifygtm.com/dashboard/settings/integrations/salesforce).
These will be used for all writes to Salesforce unless overridden in a Play or
by a field mapping.

<Frame caption="Set global default values on a per-field basis.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=43177ec636b782750a3284b853e6099f" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/integrations/salesforce/default-values.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f755832415eb0a14bb6956c057566f88 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=894f326560b2a71c3e7f231bf5509f82 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=edc156ee1008a3c3badf0974a105661b 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=801510e6a7e29480f3bac77db8b97195 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a7aaa4d608673cf341278f971f16cd27 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/default-values.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d9ca9ba5782c1809cba932ec4f7bcf6e 2500w" />
</Frame>

To learn how to set default values at the Play level instead, see the [Sync to Salesforce](/reference/plays/actions#sync-to-salesforce)
action reference.


# Field Mappings
Source: https://docs.unifygtm.com/reference/integrations/salesforce/field-mappings

Understand how to configure and use Salesforce field mappings in Unify.

# Overview

Unify can sync data between Salesforce objects and Unify objects. However, the
exact objects and fields in Salesforce differ from Unify, so Unify needs to
understand how to sync data between the two systems. This is done using *field
mappings*.

# Setup

### Change field mappings

When you first connect your Salesforce instance, Unify will automatically
prepare the field mappings for you. If you use any custom fields in place of
standard Salesforce fields, you may want to update the mappings before Unify
starts syncing data.

In the [Salesforce integration settings](https://app.unifygtm.com/dashboard/settings/integrations/salesforce),
look for the **Company**, **Person**, and **Email Message** field mappings at
the bottom of the page. Select one to view and edit the field configuration.

<Frame caption="Customize which fields are synced to and from Salesforce.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c5cc752682aff7d93f6fc97d10951710" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/integrations/salesforce/company-field-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9b3a21f1df08e05ec7a37b07b25805ff 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2811bc9f6a2bef265fd367395ab91c1c 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=53e66578b010ede7789f3b5ba319f45f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be0a19235dfb59e8c6cc858618224d9c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=fe00c650efbbb818544437108076c921 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c83d165ff45d19caa0c201d05fe38b55 2500w" />
</Frame>

You can return to update these mappings any time in the future, so you don't
need to worry about getting them perfect right off the bat!

### (Optional) Create custom fields

You can write values to standard fields and custom fields. In order to write to
custom fields, they must already exist in Salesforce. See [this guide](https://help.salesforce.com/s/articleView?id=platform.adding_fields.htm\&type=5)
for instructions on creating custom fields in Salesforce.

While some of the fields Unify can write exist as standard fields in Salesforce,
many of them do not. In particular, Unify-specific fields (like the name of the
Sequence a person was enrolled in) do not exist in Salesforce by default. In
order to write these values to Salesforce, you will need to create custom fields
before mapping them.

# Available fields

Below is a full list of the values that can be configured in the field mappings
for each object type. Some of these are standard fields, while others provide
Unify-specific information, such as the name of the Sequence that a person was
enrolled in.

<AccordionGroup>
  <Accordion title="Companies">
    | Field                                  | Description                                                                                                                                                       |
    | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Company Name**<br />*Text*           | Name of the company.                                                                                                                                              |
    | **Domain**<br />*Text*                 | Web domain of the company.                                                                                                                                        |
    | **Address**<br />*Text*                | Physical address of the company.                                                                                                                                  |
    | **State or Province**<br />*Text*      | State, province, region, or territory the company is located in.                                                                                                  |
    | **Country**<br />*Country*             | Country the address is located in.                                                                                                                                |
    | **City**<br />*Text*                   | City, town, or village the company is located in.                                                                                                                 |
    | **Postal Code**<br />*Text*            | Postal code for the company.                                                                                                                                      |
    | **Time Zone**<br />*Text*              | Time zone the company is located in.                                                                                                                              |
    | **Corporate Phone**<br />*Text*        | Corporate phone number for the company.                                                                                                                           |
    | **Status**<br />*Text*                 | Status of the company in the sales lifecycle.                                                                                                                     |
    | **LinkedIn URL**<br />*Text*           | URL to the company's LinkedIn page.                                                                                                                               |
    | **Description**<br />*Text*            | Description of the company.                                                                                                                                       |
    | **Do Not Contact**<br />*Boolean*      | Flag indicating that the company should not be contacted.                                                                                                         |
    | **Founded**<br />*Date*                | Date the company was founded.                                                                                                                                     |
    | **Industry**<br />*Text*               | Industry the company is in.                                                                                                                                       |
    | **Employee Count**<br />*Number*       | Approximate number of employees at the company.                                                                                                                   |
    | **Revenue**<br />*Number*              | Estimated annual revenue of the company.                                                                                                                          |
    | **Revenue Currency**<br />*Text*       | Three-letter ISO 4217 code indicating the revenue value currency type.                                                                                            |
    | **Account Source**<br />*Text*         | Channel this Company record was sourced from.                                                                                                                     |
    | **Unify Metadata**<br />*Text*         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date* | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text* | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Intent Level**<br />*Text*     | Intent level of the company (either **High**, **Medium**, **Low**, or **None**).                                                                                  |
  </Accordion>

  <Accordion title="People">
    | Field                                                  | Description                                                                                                                                                       |
    | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Email**<br />*Text*                                  | Contact email address.                                                                                                                                            |
    | **Address**<br />*Text*                                | Physical address of the person.                                                                                                                                   |
    | **Country**<br />*Country*                             | Country the address is located in.                                                                                                                                |
    | **Postal Code**<br />*Text*                            | Postal code for the person.                                                                                                                                       |
    | **Email Opt Out**<br />*Boolean*                       | Indicates whether the person has opted out of receiving emails.                                                                                                   |
    | **Status**<br />*Text*                                 | Status of the person in the sales lifecycle.                                                                                                                      |
    | **First Name**<br />*Text*                             | First name of the contact.                                                                                                                                        |
    | **First Name Suffix**<br />*Text*                      | Suffix of the first name of the contact.                                                                                                                          |
    | **Last Name**<br />*Text*                              | Last name of the contact.                                                                                                                                         |
    | **Title**<br />*Text*                                  | Job title or position of the contact.                                                                                                                             |
    | **Mobile Phone**<br />*Text*                           | Mobile phone number of the contact.                                                                                                                               |
    | **Work Phone**<br />*Text*                             | Work phone number of the contact.                                                                                                                                 |
    | **Corporate Phone**<br />*Text*                        | Corporate phone number of the contact.                                                                                                                            |
    | **LinkedIn URL**<br />*Text*                           | LinkedIn profile URL of the contact.                                                                                                                              |
    | **Do Not Call**<br />*Boolean*                         | Indicates whether the contact should receive phone calls or not.                                                                                                  |
    | **Do Not Email**<br />*Boolean*                        | Indicates whether the contact should receive emails or not.                                                                                                       |
    | **EU Resident**<br />*Boolean*                         | Indicates whether the contact is a resident of the European Union.                                                                                                |
    | **Lead Source**<br />*Text*                            | Channel this Person record was sourced from.                                                                                                                      |
    | **Last Activity Date**<br />*Date*                     | Date of the last activity or engagement with the contact.                                                                                                         |
    | **Unify Metadata**<br />*Text*                         | A unique identifier useful for tracking records that Unify writes to.                                                                                             |
    | **Unify Created At**<br />*Date*                       | Date and time the record was created by Unify. This will only be populated if Unify created the record; otherwise, it will remain empty.                          |
    | **Unify Updated At**<br />*Date*                       | Date and time the record was last updated by Unify.                                                                                                               |
    | **Unify First Written At**<br />*Date*                 | Date and time the record was first written to by Unify. This will be populated when Unify first creates or updates the record, and it will not change after that. |
    | **Unify Initial Play**<br />*Text*                     | Name of the first Unify Play that ran on this record.                                                                                                             |
    | **Unify Initial Play At**<br />*Date*                  | Date and time the first Unify Play ran on this record.                                                                                                            |
    | **Unify Most Recent Play**<br />*Text*                 | Name of the most recent Unify Play that ran on this record.                                                                                                       |
    | **Unify Most Recent Play At**<br />*Date*              | Date and time the most recent Unify Play ran on this record.                                                                                                      |
    | **Unify Initial Sequence**<br />*Text*                 | Name of the first Unify Sequence this person was enrolled in.                                                                                                     |
    | **Unify Initial Sequence At**<br />*Date*              | Date and time this person was first enrolled in a Unify Sequence.                                                                                                 |
    | **Unify Initial Sequence Step At**<br />*Date*         | Date and time this person first completed a step in a Unify Sequence.                                                                                             |
    | **Unify Most Recent Sequence**<br />*Text*             | Name of the most recent Unify Sequence this person was enrolled in.                                                                                               |
    | **Unify Most Recent Sequence At**<br />*Date*          | Date and time this person was most recently enrolled in a Unify Sequence.                                                                                         |
    | **Unify Most Recent Sequence Step At**<br />*Date*     | Date and time this person most recently completed a step in a Unify Sequence.                                                                                     |
    | **Unify Most Recent Sequence Status**<br />*Text*      | Status of the most recent enrollment for this person. The statuses shown on enrollments in Unify are the same values that will be written to Salesforce.          |
    | **Unify Initial Reply Classification**<br />*Text*     | High-level classification of the initial reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".          |
    | **Unify Most Recent Reply Classification**<br />*Text* | High-level classification of the most recent reply received from a person. It will be either "Positive", "Objection", "Neutral", "Automated", or "Negative".      |
    | **Unify Initial Reply Tags**<br />*Text*               | Comma-separated list of classification tags of the initial reply received from a person. For example, "Ready to meet, Needs more information".                    |
    | **Unify Most Recent Reply Tags**<br />*Text*           | Comma-separated list of classification tags of the most recent reply received from a person. For example, "Ready to meet, Needs more information".                |
  </Accordion>

  <Accordion title="Email Messages">
    | Field                                | Description                                                                                                    |
    | ------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
    | **Universal Message ID**<br />*Text* | Globally unique identifier that exists for all email messages.                                                 |
    | **Sender**<br />*Text*               | Reference to the user, contact, or lead who sent the email.                                                    |
    | **Recipients**<br />*Text\[]*        | List of users, contacts, or leads who received the email.                                                      |
    | **Subject**<br />*Text*              | Subject of the email.                                                                                          |
    | **Content**<br />*Text*              | Body of the email.                                                                                             |
    | **Sent At**<br />*Date*              | Date and time the email was sent.                                                                              |
    | **Is Bounced**<br />*Boolean*        | Indicates whether the email bounced.                                                                           |
    | **Bounced At**<br />*Date*           | Date and time the email bounced.                                                                               |
    | **Click Count**<br />*Number*        | Number of times a link in the email was clicked. Only links to sites with the Unify intent client are tracked. |
    | **Clicked At**<br />*Date*           | Date and time a link in the email was first clicked.                                                           |
    | **Is Marked as Spam**<br />*Boolean* | Indicates whether the email was marked as spam by a recipient.                                                 |
    | **Marked As Spam At**<br />*Date*    | Date and time the email was marked as spam by a recipient.                                                     |
    | **Is Opened**<br />*Boolean*         | Indicates whether the email was opened by a recipient.                                                         |
    | **First Opened At**<br />*Date*      | Date and time the email was first opened by a recipient.                                                       |
    | **Last Opened At**<br />*Date*       | Date and time the email was last opened by a recipient.                                                        |
    | **Track Opens**<br />*Boolean*       | Indicates whether open tracking was enabled for the email.                                                     |
    | **Is Opted Out**<br />*Boolean*      | Indicates whether the recipient opted out of receiving emails.                                                 |
    | **Opted Out At**<br />*Date*         | Date and time the recipient opted out of receiving emails.                                                     |
    | **Enrolled By Play**<br />*Text*     | Name of the Play that enrolled the recipient in the sequence.                                                  |
    | **Sequence Name**<br />*Text*        | Name of the sequence linked to the email.                                                                      |
  </Accordion>
</AccordionGroup>


# Toggle Lead Assignment Rules in Salesforce
Source: https://docs.unifygtm.com/reference/integrations/salesforce/lead-assignment-rules

Troubleshoot a common bug in Salesforce related to lead assignment rules.

## Explanation

Salesforce allows you to create "lead assignment rules" that automatically assign different owners to leads depending on custom criteria. However, sometimes these rules don’t work right off the bat due to a specific bug in Salesforce. The steps outlined here should resolve the issue.

## Steps

### Ensure you have an active lead assignment rule

Navigate to the **Setup** page in Salesforce by clicking the settings icon in the top-right corner of any Salesforce page.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=225c290fe4ff35d75b032c2708a8fa19" alt="active-lead-assignment-rule-step-1" data-og-width="362" width="362" data-og-height="402" height="402" data-path="images/active-lead-assignment-rule-step-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=184d7b7e426ae232f68970899cb6293f 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=00f4179c5b6623b1b7f03d9301319f29 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=aa30939addb0d1ab9e1b7cadaffebc78 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=cc09fc24f119cded80f0f78a349a0b4e 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0a00de7f6b4f79570690a94b026ca3f6 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-1.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=6976bbed56c8fbcd0c245b7b345ee51e 2500w" /></Frame>

Search for **Lead Assignment Rules** in the sidebar.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=df1192fdef7dbe47181e75614280823c" alt="active-lead-assignment-rule-step-2" data-og-width="500" width="500" data-og-height="500" height="500" data-path="images/active-lead-assignment-rule-step-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=213b145a065c299739a8812ddbd4b91f 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4f2c2fe19c92729a99e0728d8037f3d2 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=19835957d052f59bb1d4117600dc695a 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=6c042ee9a0fe71f63c274c1b06439c27 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=14dcc758fb424281569b2d93d867e05d 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-2.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=16cd30e960bccfedffe7f0363de20f0f 2500w" /> </Frame>

You should see at least one rule with a checkmark under the **Active** column.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c4ecd26c8b2c77122f1b5650d37b8046" alt="active-lead-assignment-rule-step-3" data-og-width="2388" width="2388" data-og-height="620" height="620" data-path="images/active-lead-assignment-rule-step-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=95b6ed3868e31e096d8a15dbadb0114f 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c5fddcc136790d2e4b6330134f8bac14 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=52708fbb18f1d514ad56e7e7bda132ec 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=95a79c352cf107be1d2220c4ee0ab929 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2ec062fb468dfadd769e0a76c26a6d38 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/active-lead-assignment-rule-step-3.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=03de90833a114a45e74d86c1d3b836f8 2500w" /> </Frame>

### Toggle the rule off and on

In the **Lead Assignment Rules** page from the previous step, click on the name of your rule and then select **Edit**. Uncheck the checkbox next to **Active** to temporarily deactivate the rule.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2ffa4ba0241fb40208789e10f54051c6" alt="toggle-rule-off-on-step-2" data-og-width="1012" width="1012" data-og-height="558" height="558" data-path="images/toggle-rule-off-on-step-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=67c7c8085ed9a51af38eb62dd497cdae 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=4df5e094e2bdd229fa679ed58c592c68 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c14403847c82acd1687dd60f9cdaa74e 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9d89930bcfee5233786579fc922c1ba6 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6a270381b55d2145f6013e4c3993728a 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/toggle-rule-off-on-step-2.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=8e82479a0a60eaa87b845cbfe1df8e79 2500w" /> </Frame>

Click **Save**. Then click **Edit** again, re-check the checkbox next to **Active**, and then choose **Save**.

### Test that leads are assigned correctly in the UI

Navigate to the **Leads** page in Salesforce. You can get there via the app launcher.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=44d52b741ccb9a6009cabc35e9bef711" alt="test-leads-correctly-assigned-step-1" data-og-width="648" width="648" data-og-height="482" height="482" data-path="images/test-leads-correctly-assigned-step-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=97c769dc6529eb6a9a59968482b69a70 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ec33620fa1c94207eda0b654b131b106 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e20812e634d4b61bf3522cb61191ca7d 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ee5ed898d955c6923c161c93ff591fd2 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=54b0e936c8a82b4f49f8ccb5978045b9 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-1.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=67f6b605cc525a40e2bec780677a2441 2500w" /> </Frame>

In the top-right corner of the screen, select **New** to create a new lead.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a82b6a990a7ce6fed11bae2b771725a5" alt="test-leads-correctly-assigned-step-2" data-og-width="1126" width="1126" data-og-height="82" height="82" data-path="images/test-leads-correctly-assigned-step-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=52df0afc42719245fd61c9ea2cf40322 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7da4c8e8e7ec8cfe4c0f2649b12fe533 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=21d4bdc2b8e4a393b524900936683138 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=26a8c9a2eae8de3818d25dd9b8aa1fb5 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1e9e8afad0002fc4b79758ee41bc6da6 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-2.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f564a8560f90962ced5a19ec5e4eae64 2500w" /> </Frame>

Check the **Assign using active assignment rule** checkbox in the lower-left corner.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ca073da311624856c0b44932b7f81538" alt="test-leads-correctly-assigned-step-3" data-og-width="1994" width="1994" data-og-height="1206" height="1206" data-path="images/test-leads-correctly-assigned-step-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ffffd30dcf0394ffd53dca7d208ad7b0 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c11bdc9e77b28a5e944068c94f31e989 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=31ace94fe3f4cace937bb2b85570b480 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=217b4bce8079654faefbc02dc070070c 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ee85d339a6346d1fad7d0511c841a88c 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/test-leads-correctly-assigned-step-3.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9c4dd7318441e762f4b869964ddd6299 2500w" /> </Frame>

Fill out the required lead fields with values that should trigger the lead assignment rule you created and then click **Save** in the bottom-right corner.

Lastly, verify that the lead was assigned to the correct owner.


# Salesforce Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/salesforce/overview

This guide outlines how to connect your Salesforce instance to Unify.

# Overview

In just a few steps, you can connect your Salesforce instance to Unify and start
syncing data bidirectionally. This unlocks a few key benefits when using Unify:

1. Salesforce records can be used to [construct exclusions](/tutorials/how-to-create-an-exclusion)
   that prevent Unify from engaging with specific people or companies. For
   example, you can create an exclusion for all current customers or deals in
   progress.
2. You can create Plays that are triggered by Salesforce records. This allows
   you to run a Play based on a specific event or criteria captured within
   Salesforce.
3. Unify can write data back to Salesforce so that you can maintain a source of
   truth in your CRM and respect rules of engagement in other tools or business
   processes.

Unify's integration with Salesforce is designed from the ground up to prevent
many common pitfalls, including overwriting existing data or creating duplicate
records. For an in-depth description of how Unify does this, see [How Bidirectional Syncs Work](/reference/integrations/salesforce/bidirectional-syncs).

# Prerequisites

* **Salesforce Subscription:** Unify requires API access to your Salesforce
  instance. This is typically included with most Salesforce plans, but some
  plans may require an upgrade.

  * If you're unsure, follow [these instructions](https://help.salesforce.com/s/articleView?id=000386929\&type=1)
    to determine your plan and then check [here](https://help.salesforce.com/s/articleView?id=000385436\&language=en_US\&type=1)
    to see if API access is included.

* **Administrative Access:** In order to assign the correct permissions to the
  integration user, a Salesforce admin may be needed to complete these steps.

# Setup

<Note>
  If you are using a Salesforce sandbox instance, let our support team know in
  advance and we will create a dedicated testing login for you.
</Note>

<Steps titleSize="h3">
  <Step title="Choose an integration user strategy">
    Decide which integration user Unify should use to connect to Salesforce.
    Unify supports multiple approaches:

    | Setup                                                      | Pros                                                                                                                                                                         | Cons                                                                                                                                                                 |
    | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Dedicated integration user**                             | This is best practice and our recommended option. The user is granted specific limited permissions and all updates made within Salesforce are clearly attributable to Unify. | This requires the purchase or use of a dedicated Salesforce user license, which may require time to set up at your company.                                          |
    | **Shared integration user with other connected apps**      | This might be a better choice, because you may already use an integration user with other connected apps. You don't need to provision a new user.                            | Unify must share the permissions and limits of the shared integration user. If this user's access is shut down, all connected apps will be impacted.                 |
    | **Existing individual user with system admin permissions** | This is typically the fastest and most affordable option because you use an individual user that already exists in your Salesforce. There's no need to create anything new.  | Unify is given full system access and edits made within Salesforce are attributed to the individual user. If the user leaves the company, the connection will break. |

    If you choose to create a dedicated integration user, you can follow [this guide](https://help.salesforce.com/s/articleView?id=ind.sf_contracts_create_users_and_assign_permission_sets.htm\&type=5)
    for step-by-step instructions.
  </Step>

  <Step title="Connect Salesforce instance">
    Navigate to [Settings -> Salesforce](https://app.unifygtm.com/dashboard/settings/integrations/salesforce)
    and select **Connect**. You will be redirected to the Salesforce authentication
    page where you can sign in using the desired Salesforce integration user that
    Unify will use.

    <Frame caption="This screen will appear before you have connected a Salesforce organization.">
      <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6a1c510a608f9a7930ee41fe8abc29ab" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/connect-salesforce-instance.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d2b032ce103659db0e676ffbf607cf05 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=88d72edd4f08490d99d748f51ffe544a 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=02dab166a2e40e506a44d5cfcf4f6487 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a9660f16de8139d0043ce43797dca04a 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=66a3aeb90be91f6e1c3feaecaeee5270 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connect-salesforce-instance.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7ba00f8b8ec7bb0f4951e9e509965ae4 2500w" />
    </Frame>

    <Frame caption="Once a connected, you will see the settings available for your Salesforce connection.">
      <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=966bc13bfbab95e05d10f6a946774c9b" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/connected-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c4864502f249c37dd8135f6fdbd5d78e 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=033c8c211afab2b973169872e6276559 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7c421975681f69a51980519d869f8473 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7673805386c44f41d3be7804663887b6 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=15dcba15bd6106137b0531cb6d4e8d10 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/connected-settings.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b726209553826ee15c400e8a13e81ff8 2500w" />
    </Frame>
  </Step>

  <Step title="Assign required permissions">
    Unify requires specific permissions in order to access the Salesforce API and
    read and write data. If any permissions are missing, they will be shown on
    the settings page.

    <Frame caption="The permissions widget will indicate if permissions are missing.">
      <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c1b2160778cc25bdc9df55963c4aaf2d" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/missing-permissions-settings-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9631cd5ef28ffff5689c1085891693c6 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4a84c5360df3a158222835feabe72bef 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dd4cf8a57312a23e4e1c74b267d25a7b 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=87345249c0860e92219f92f29b00e37c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=19dd4a89adeb4e369843aa7eebedbcbd 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a520595c950078a6de3e237f2ca33928 2500w" />
    </Frame>

    See [Required Permissions and Settings](/reference/integrations/salesforce/required-permissions)
    for details on fixing any issues.
  </Step>

  <Step title="Choose which objects to create">
    Salesforce has two different ways of representing companies and people:

    1. **Contacts and Accounts**: Every person has a Contact record, and Contacts are associated with Accounts.
    2. **Leads**: Every person has a Lead record which contains information about both the person and their company.

    Unify supports both options, and you can choose which approach you want to
    use on the integration settings page. This can be changed at any time.

    <Tip>
      Pick the option that best aligns with how your team uses Salesforce today.
      If you're unsure, Unify recommends **Contacts and Accounts** as a best
      practice.
    </Tip>
  </Step>

  <Step title="Create field mappings">
    Unify provides granular control over which Salesforce fields map to which
    Unify fields. For each object, select **Create Mapping** and update any
    fields you wish to customize.

    In most cases, the default options will be a good starting point. You can
    always return to change these mappings in the future.

    <Frame caption="The field mappings page lets you customize which fields Unify can read and write.">
      <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c5cc752682aff7d93f6fc97d10951710" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/integrations/salesforce/company-field-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9b3a21f1df08e05ec7a37b07b25805ff 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2811bc9f6a2bef265fd367395ab91c1c 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=53e66578b010ede7789f3b5ba319f45f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be0a19235dfb59e8c6cc858618224d9c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=fe00c650efbbb818544437108076c921 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/company-field-mapping.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c83d165ff45d19caa0c201d05fe38b55 2500w" />
    </Frame>

    See [Field Mappings](/reference/integrations/salesforce/field-mappings) for details on
    how field mappings work and the available options.
  </Step>

  <Step title="Enable syncs">
    Once you're satisfied with your integration settings and field mappings, you
    can begin syncing data into Unify by selecting **Resume**. If at any point
    you want to pause syncs again, you can return to this page and select
    **Pause**.

    To enable Unify to write data back to Salesforce, activate the toggle next to
    **Enable writing to Salesforce**. This will allow Unify to sync records back
    to Salesforce.

    <Frame caption="The Salesforce integration settings page after setup is complete.">
      <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ad94068dd0e453ea13f91477f5fa13a6" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/salesforce-integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e8a31188824121df237082438c613772 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e0bf911aaa5d1860488e6c71394e2beb 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ad9b326344799156b6f1821f53364a48 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=336025ee4486816b12247ed6b6350dd6 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c0fa1ce75d97c8f3923f0a72fc0285f7 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/salesforce-integration-settings.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9225486ea0e49156abd5a967762eda85 2500w" />
    </Frame>
  </Step>
</Steps>

## Additional Salesforce resources

<CardGroup cols={2}>
  <Card icon="shield-check" title="Required Permissions" href="/reference/integrations/salesforce/required-permissions">
    Ensure your Salesforce user has the correct permissions and settings enabled
    for Unify.
  </Card>

  <Card icon="arrow-right-arrow-left" title="Field Mappings" href="/reference/integrations/salesforce/field-mappings">
    Configure mappings between Unify fields and Salesforce fields.
  </Card>

  <Card icon="pen-to-square" title="Configure Default Values" href="/reference/integrations/salesforce/default-values">
    Specify default values that should be used when writing to Salesforce.
  </Card>

  <Card icon="arrows-rotate" title="How Bidirectional Syncs Work" href="/reference/integrations/salesforce/bidirectional-syncs">
    Learn how Unify's bidirectional syncs work and how to avoid common pitfalls.
  </Card>
</CardGroup>


# Required Permissions and Settings
Source: https://docs.unifygtm.com/reference/integrations/salesforce/required-permissions

Ensure your Salesforce user has the required permissions for Unify.

# Overview

The permissions that Unify requires fall into two categories:

1. **System Permissions**: These are permissions that apply to the entire
   Salesforce instance and are required for Unify to function properly.
2. **Object Permissions**: These are permissions that apply to specific objects
   (e.g., Account, Contact, etc.) and are required for Unify to read and write
   data.

The exact permissions that Unify needs are detailed below along with
instructions on assigning these permissions to your integration user.

# Required Permissions

<Info>
  Access can be restricted as desired for sensitive records or fields that you
  do not want Unify to access. However, Unify needs access to any records or
  fields that you want to use for exclusions.

  For example, to prevent Unify from engaging with current customers, Unify will
  require access to the records that indicate current customers to evaluate the
  exclusion rule.
</Info>

<Tabs>
  <Tab title="System Permissions">
    | Permission                       | Reason                                                      |
    | -------------------------------- | ----------------------------------------------------------- |
    | **API Enabled**                  | Allows Unify to communicate with Salesforce via the API     |
    | **View All Users**               | Enables Unify to link Salesforce users to Unify users       |
    | **View Setup and Configuration** | Enables Unify to provide details about missing permissions  |
    | **Edit Tasks**                   | Enables Unify to create and update tasks and email messages |
  </Tab>

  <Tab title="Object Permissions">
    | Object            | Permissions          | Reason                                                     |
    | ----------------- | -------------------- | ---------------------------------------------------------- |
    | **Account**       | *Read, Create, Edit* | Enables Unify to sync companies bidirectionally            |
    | **Contact**       | *Read, Create, Edit* | Enables Unify to sync people bidirectionally               |
    | **Lead**          | *Read, Create, Edit* | Enables Unify to sync companies and people bidirectionally |
    | **Opportunity**   | *Read*               | Enables Unify to use and filter based on opportunities     |
    | **Email Message** | *Read, Create, Edit* | Enables Unify to write outbound emails and replies         |
  </Tab>
</Tabs>

# Setup

### Assign required permissions

Depending on whether you are using profiles or permission sets, the steps to
assign the required permissions will differ slightly. Follow the instructions
below based on your setup.

<Tabs>
  <Tab title="Profiles">
    If you're using a **Profile** to manage permissions, follow these steps:

    1. Navigate to the **Setup** page in Salesforce by clicking the gear icon in
       the top-right corner.

    2. Go to **Users > Profiles**.

    3. Choose the Profile assigned to your integration user.

    4. Click **Edit**.

    5. In the **Administrative Permissions** section, enable the following
       options:

       * **API Enabled**
       * **View All Users**
       * **View Setup and Configuration**

    6. In the **General User Permissions** section, enable the following
       options:

       * **Access Activities**

    7. In the **Standard Object Permissions** section, enable the following
       options for each object:

       * **Account**: Read, Create, Edit
       * **Contact**: Read, Create, Edit
       * **Lead**: Read, Create, Edit
       * **Opportunity**: Read
       * **Email Message**: Read, Create, Edit

    8. Click **Save**.
  </Tab>

  <Tab title="Permission Sets">
    If you're using a **Permission Set** to manage permissions, follow these steps:

    1. Navigate to **Setup > Permission Sets**.

    2. Create a new permission set (or modify an existing one).

    3. Assign the permission set to your integration user.

    4. Under **System Permissions**, enable the following options:

       * **API Enabled**
       * **View All Users**
       * **View Setup and Configuration**

    5. Under **App Permissions**, enable the following options:

       * **Access Activities**

    6. Under **Object Settings**, select each object and enable the following
       options:

       * **Account**: Read, Create, Edit
       * **Contact**: Read, Create, Edit
       * **Lead**: Read, Create, Edit
       * **Opportunity**: Read
       * **Email Message**: Read, Create, Edit

    7. Click **Save**.

    8. If you created a new permission set, assign it to your integration user.
  </Tab>
</Tabs>

Once you've assigned these permissions, you can verify they are correctly set up
by checking the **Permissions** widget in Unify. Navigate to
[Settings -> Integrations -> Salesforce](https://app.unifygtm.com/dashboard/settings/integrations/salesforce)
and look for the **Permissions** widget.

<Frame caption="The permissions widget will indicate if permissions are missing.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c1b2160778cc25bdc9df55963c4aaf2d" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/integrations/salesforce/missing-permissions-settings-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9631cd5ef28ffff5689c1085891693c6 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4a84c5360df3a158222835feabe72bef 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dd4cf8a57312a23e4e1c74b267d25a7b 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=87345249c0860e92219f92f29b00e37c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=19dd4a89adeb4e369843aa7eebedbcbd 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/missing-permissions-settings-page.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a520595c950078a6de3e237f2ca33928 2500w" />
</Frame>

<Frame caption="The specific missing permissions are displayed in the details view.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bf9161fd9b568ae58178b8258f884f10" data-og-width="2880" width="2880" data-og-height="2050" height="2050" data-path="images/reference/integrations/salesforce/view-missing-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4f4df5d4bc9a4a0b1c5e0a00b774020a 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e40f8e2272fdabac8e63e17658c6481a 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8666941f6b10bf8e23621922468672e8 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=307bd20f36c0b0ab360bec5246d9df37 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bf678cbcc71d2d27747cfe2685968b80 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/integrations/salesforce/view-missing-permissions.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=60477b55b55c7dcc593fd96ac8f1e508 2500w" />
</Frame>

### Enable Enhanced Emails

To ensure Unify can write emails to Salesforce, the **Enhanced Email** feature
must be enabled. This allows Unify to write sent emails using the **Email Message**
object.

In most orgs, Enhanced Email is enabled by default. If you don’t see the
**Email Message** object, review the following guide to enable it.

<Card icon="envelope" title="Set Up Enhanced Email" href="https://help.salesforce.com/s/articleView?id=sf.enable_enhanced_email.htm&type=5">
  Salesforce support article explaining how to enable Enhanced Email.
</Card>

For more information:

* [Use Enhanced Email for More Email Functionality](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_overview.htm\&type=5)
* [Considerations for Using Enhanced Email](https://help.salesforce.com/s/articleView?id=sf.emailadmin_enhanced_email_considerations.htm\&type=5)


# Segment Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/segment

This guide outlines how to connect your Segment workspace to Unify.

# Overview

If you use Segment to collect website analytics, Unify can be connected to your
Segment workspace as a destination in order to reveal web traffic data. This
will also let you build audiences and Plays using Segment analytics data.

# Steps

<Note>
  If you’re also using the Unify Tag, ensure it isn’t running on the same
  pages as Segment. Otherwise, events may be double counted.
</Note>

### Generate a key in Unify

1. Log in to Unify

2. Navigate to [Settings -> Integrations -> Segment](https://app.unifygtm.com/dashboard/settings/integrations/segment) and click **Setup**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f629a09a07d5de67bc7cbfa456108893" alt="Setup.png" data-og-width="2000" width="2000" data-og-height="1329" height="1329" data-path="images/53.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=df996a278fe7bd9ae993f35780797dc5 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=460fdebb6b407f278bffa52ef1aa5624 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=55881c3b33f35f9ec8be5e8293fa13c3 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7ad5962d63f510fbca3e80ca216dc15b 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=721faed7d996038e4515e7886fd6de9c 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/53.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ed1cc879e75b33b65a3b4eebb2007c1 2500w" /></Frame>

3. Click the **Copy** button to copy the write key to your clipboard

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b6ebe5630f7cd5731f7ffa0c68fcc759" alt="Write Key.png" data-og-width="2000" width="2000" data-og-height="1329" height="1329" data-path="images/54.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=051960a213222d78a1bbc24adb42ae39 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7af6a399973b52c9d015e21e9e244aba 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=88994a08664d2f936bdc8274d3b37014 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=d5ea57830aaa2426ad56c68b39df57d4 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4f206ace2ab585e04dbf7807ed103f68 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/54.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=2061f372489e7fd25cab0b4294728822 2500w" /></Frame>

### Add Segment destination

1. Log in to Segment and click on the **Destinations** tab in the sidebar

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=24da26163177fb33eb7f27f3048593c5" alt="Screenshot 2023-08-23 at 8.02.29 PM.png" data-og-width="480" width="480" data-og-height="552" height="552" data-path="images/55.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=903d9a4ca167b7dfdf1846c14e462506 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=87e929c2527e6479b59e82217559f811 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=0fc3fef80ce1d2a65b73e338a7b1a9b5 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=1e68cb077b4e6aec0db132411dfacb15 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=2796809dccaf120c041a7d55c3f8cccd 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/55.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=36352931288f3de9495d6a7174d938eb 2500w" /></Frame>

2. Click **Add destination** in the top right corner

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=379089fb5a0816300977290b6eecabc1" alt="Screenshot 2023-08-23 at 7.02.47 PM.png" data-og-width="580" width="580" data-og-height="182" height="182" data-path="images/56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=9f51ea710e307ecede0eb15d5beef26f 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=92612ad8420c65a3ccde3ebe6b4683e3 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ae695279918da1d3473cfe6aaf25ae6 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=29185cd2a81369f8e9cdaa3342f877fc 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4c0e3ba3db82d2dbdcfbca2fe5a4c1f7 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/56.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8485091e69083893699e4e23f26d56d5 2500w" /></Frame>

3. Search for “webhook” and select the **Webhook (actions)** destination

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f8ba7a4e1baf18efd52cbf086b547005" alt="Screenshot 2023-08-23 at 7.03.49 PM.png" data-og-width="580" width="580" data-og-height="249" height="249" data-path="images/57.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=68f29c8e08f364eef17c56b44b5cf576 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=816b8af70354f3441a0cf05d68e22044 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=63dff82e4b70f8678c7620e5412f4d26 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=39e4535796122ff4299829f543900608 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=3f761fd4eed74e78047039e38d848b28 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/57.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=77a1ad489eb49239bf848f5c264e36ed 2500w" /></Frame>

4. Click **Add destination** again in the top right corner

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=0fce45f6e023787737ffed8968e51334" alt="Screenshot 2023-08-23 at 7.05.58 PM.png" data-og-width="2000" width="2000" data-og-height="1312" height="1312" data-path="images/58.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c3d22724ff84a83d37a4077b046084f1 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=39e0963f822234738226b961b55d876a 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=86e55370218185b24b4269595a6796a6 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b9c41bcea18b3d377a12aa51971fb56e 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=33f49d17295bf03dd94f360e7a2a4d1e 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/58.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=044acf50e506e11435a28d93733ca14f 2500w" /></Frame>

5. Select website source whose data you want to send to Unify and then click **Next**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=badeaf966f78d2bb57e6452001d0a48d" alt="Screenshot 2023-08-23 at 7.08.02 PM.png" data-og-width="2000" width="2000" data-og-height="1120" height="1120" data-path="images/59.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7344ef79d7bac6547c260dede4a1322d 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f274de83c1bfca90d590578e6f0efd7a 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=445ca7982a838f1163e5d1ca1c6e2802 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=bc64cb5cb7a7cca808b646ae06037c7a 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8db1a2de1c86f509985172609516fa95 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/59.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=f50d6224f19d759cbbc4a8896906a4b0 2500w" /></Frame>

6. Give this destination a name, make sure **Fill in settings manually** is selected, and click **Create destination**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=1f16e50997242eb3c75af440f8b96feb" alt="Screenshot 2023-08-23 at 7.13.50 PM.png" data-og-width="2000" width="2000" data-og-height="1120" height="1120" data-path="images/60.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=eb06f0bbd5228f79397104352c41f7ed 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=e82434032dc43ee20b0117d7eb911ed0 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c4728f13d0048aa42303e5f3144513bf 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=54ee9da16309fc3f112a3e05fb67fef5 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c9f8649fefda99a749c62ea883b1fa6a 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/60.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=86c8c1eaadd34156c989f25dd33d6d7e 2500w" /></Frame>

7. Click on the **Mappings** tab on the top and then select **New Mapping**

   <Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=34ea46b0bb84ce018cf2bd321eaa3288" alt="Screenshot 2023-08-23 at 7.18.04 PM.png" data-og-width="2000" width="2000" data-og-height="1310" height="1310" data-path="images/61.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4dde078bba98b1d36f3ff77b76466926 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b0bbe6d0ac6cce785cd3bc79e8ef2ace 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4b06672b3614d60b8467d73d22db348d 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=afab0babd9b0b89eab4de08cffac14ed 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=a4994b3f9951d31561a34bbafd2af4a7 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/61.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=7babc6451378736091e701bd763580c2 2500w" /></Frame>

8. Choose the **Send** option

   <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=aede00c7fb3b01a961e528900005836d" alt="Screenshot 2023-08-23 at 7.21.39 PM.png" data-og-width="2000" width="2000" data-og-height="1088" height="1088" data-path="images/62.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0137248863ca94ea854f665e31e09b8e 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e41b2a8f493610ac760ca4811ba4ee21 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a715159b20ff9ac79a518fc990820919 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=95969236fcd55764bbb1d1e3deb7ebcc 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=69f7095e1194c2436e7495cebed5a79b 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/62.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b392ba5bd79571ae6537163d759c260 2500w" /></Frame>

9. Fill in the following mapping values…
   1. Under **Section 1**:

      1. Unify currently supports Page and Identify event types. Track events will be supported soon. You should select **any** and then list these types.
      2. If there are specific event types that you know you do not want to forward to Unify, you can safely omit them.

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=73ac92bbf6a4be152a5e8cc90c8e29fd" alt="Screenshot 2023-08-23 at 7.24.38 PM.png" data-og-width="2000" width="2000" data-og-height="770" height="770" data-path="images/63.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1fd08bb01166d9d00ececb25f203fd2d 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b6f5d3acb29214a1de41160c87a091c6 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b1f099a33604e4199cf4825315660b01 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2f9b6cc35a9495c7e36c29f13dab3e4d 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f873ee61649448e7e32df139d6508537 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/63.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=11f13b569280066e1f497bffe5c8051b 2500w" /></Frame>

   2. Under **Section 2**:

      1. Click **Load Sample Event** to populate the box with an example Segment event

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=97aeeeb9d9239342b59fa624be477b28" alt="Screenshot 2023-08-23 at 7.29.31 PM.png" data-og-width="2000" width="2000" data-og-height="1229" height="1229" data-path="images/64.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=81d78da8d0865250989de7e96a3c1448 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9d0e8040457c36e729f9252a06ea325e 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=98aca53d6acb54c5625b28ba9d1fd869 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=22493118e21a01cca5ec65d9764c57c4 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=8b1fb6dd06fb22965c4a3605751af2c0 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/64.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=912abd28e8120e3b5a7457495e12ebc8 2500w" /></Frame>

   3. Under **Section 3**:

      1. Next to **URL**, fill in the following value:

         ```
         https://analytics.unifygtm.com/api/v1/webhooks/segment
         ```

      2. List two values under **Headers** (click **Add Mapping Field** to add more boxes):
         1. `<YOUR WRITE KEY` → `X-Write-Key`
         2. `application-json` → `Content-Type`

      3. Be sure to replace `<YOUR WRITE KEY>` with the key you copied earlier

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=de35b4f8dea4d7a97e2bfbb61a1ca79c" alt="Screenshot 2023-08-23 at 7.42.22 PM.png" data-og-width="2000" width="2000" data-og-height="2301" height="2301" data-path="images/65.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=49a6ec26e80401583ae06bcc5422358c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=25efd4b9f56dfad01aad5b17aa86b8db 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1537dd8e39a5ba93a76cc8f87fbff6f3 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=138fb67fbb5d8b4ec17df2f1729fe309 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2970d25e9d0e022efc297418af84039f 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/65.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4a328474d5343b557237d99e68ebde65 2500w" /></Frame>

   4. Under **Section 4**:

      1. Send a test event to verify that it’s working

      <Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c089096e1eec784eaa551bdbdf25295d" alt="Screenshot 2023-08-23 at 7.44.09 PM.png" data-og-width="2000" width="2000" data-og-height="1031" height="1031" data-path="images/66.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2adc82442b01ead8e7b964be5532ed1a 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ca4b43b72136f15dc0a077dfc5f85150 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5f6203f0d8e24933f07dff91086c7097 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3983840d43a682d8efe0b0687f18e400 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5b9735e08fb4047af8d4ce3e94d0936e 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/66.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b2406d656da98b8fd4192db87f03bb0b 2500w" /></Frame>

That’s it! If you see **Test succeeded**, you’re all set. Traffic should now be flowing into Unify.


# Slack Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/slack

This guide details the process of integrating Unify with your Slack workspace.

<Note>
  To add an app to your Slack workspace, you need the necessary permissions as
  per your organization's policy. Refer to [Slack's roles and
  permissions](https://slack.com/help/articles/201314026-Permissions-by-role-in-Slack)
  or consult with a workspace owner or admin.
</Note>

# Connect to Slack

Go to [Settings -> Integrations -> Slack](https://app.unifygtm.com/dashboard/settings/integrations/slack) in Unify and press the **Connect** button.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=282e3387bb0e2479fb1626f1bc7c94a0" alt="" data-og-width="3456" width="3456" data-og-height="1556" height="1556" data-path="images/68.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1a956c23248cd5bb48b1b229533883b7 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=647eaf79720782a9901885648f81c816 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=fcb12daaef67cf663ee3107ef8c42629 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b20b2082412187fbb7923ac55ac23944 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e6dc27575eab8ec4e121bfc52500617d 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/68.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=126966009ddcb30d43b9318962570ac2 2500w" /></Frame>

You will be redirected to Slack's authorization page. Click **Allow** to proceed.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7b88f15eaf11e9d8a4798baa45f7f9a9" alt="" data-og-width="1334" width="1334" data-og-height="748" height="748" data-path="images/69.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d9ecf2be34c0cb918a7b1d6e9a93f07d 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=933cc349fdb65b1ad372764565a02a5f 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=fbd13e292511cb21589897af9e49ab00 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e370e85d563b6fcea35b862dc0c97d29 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4ed101add1c3d1d17e712c9236337453 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/69.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9279fdd68626cbb9f7ae9ee10a99b306 2500w" /></Frame>

You will be redirected back to the Slack settings page, where you can view the status of your connection.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9ac19f4cc05130533ba2f8ca982a7d6b" alt="" data-og-width="3436" width="3436" data-og-height="1526" height="1526" data-path="images/70.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=21229a4fc5c7afc47d41d963c2aee443 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c0311557a085284117bb55e3c96a3e9c 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=be15e5f7eb0b54371ffe09be337e619c 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=072c178a878e6c65b1bb33bec71800be 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9d1775cf08379f2517dfde77836c9c9f 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/70.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=36cb1958ff0450353b7cb4499215e363 2500w" /></Frame>


# Snitcher Integration Guide
Source: https://docs.unifygtm.com/reference/integrations/snitcher

Identify website visitors with Snitcher and other providers.

# Overview

Unify provides out-of-the-box website visitor identification Snitcher and other
providers. To get started, simply enable [Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
in your settings.

Once connected, Unify will automatically begin identifying website visitors
using Snitcher and other data sources for maximum coverage. Be sure to set up
the Unify Intent client on your website to start receiving visitors to identify.


# Authentication Options
Source: https://docs.unifygtm.com/reference/management/authentication

Learn about the login methods available for your organization in Unify.

## Overview

Unify supports the following forms of authentication:

1. **Username and Password**: Users can log in with an email address and password managed by Unify.

2. **Google Workspace**: Users can log in using a Google account associated with your organization's Google Workspace.

3. **Single Sign-On (SSO) via SAML 2.0**: For enterprise customers, Unify supports SSO through the SAML 2.0 protocol. This allows your organization to use your existing identity provider (IdP), such as Okta or Azure AD, to authenticate your users.

All methods are powered by Auth0, the leading industry standard for secure authentication.

### Single Sign-On (SSO)

Our team will work directly with you to integrate Unify with your identify provider. Below are the steps and information we'll cover during this process.

#### Supported Identity Providers (IdPs)

* Okta
* Azure Active Directory (AD)
* Any SAML 2.0 compliant IdP

#### Information required for SSO setup

* **Sign In URL**: The URL where SAML authentication requests are sent. This is also called the single sign-on (SSO) endpoint.
* **Sign Out URL**: The URL where SAML logout requests are sent. This is also called the single logout (SLO) endpoint.
* **X.509 Certificate**: A certificate used to verify the SAML response.


# Unify Credit System
Source: https://docs.unifygtm.com/reference/management/credit-system

Learn how credits work in Unify.

## Overview

Unify operates on a flexible, usage-based credit system that scales with your
needs. Credits are consumed by various activities such as prospecting,
enrichment, AI Agent runs, and certain intent signals.

## How credits work

Here are the key points to know about the credit system:

* **Credit Value**: Each Unify Credit represents a unit of platform usage.

* **Consumption**: Credits are deducted in real-time as features are used.

* **Replenishment**: Credits reset monthly or annually based on your plan. Add
  credits at anytime on the [Usage](https://app.unifygtm.com/dashboard/settings/organization/usage)
  page or upgrade your plan on the [Plans & Billing](https://app.unifygtm.com/dashboard/settings/billing)
  page.

You can monitor your credit consumption on the [Usage](https://app.unifygtm.com/dashboard/settings/organization/usage)
page.

## Credit consumption

Different features consume credits at different rates. Here's a breakdown of the
credit consumption of each feature:

| Feature                        | Unify Credits | Unit                              | Description                                                                                                                  |
| ------------------------------ | ------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Website Reveals                | 0.1           | Per website visitor revealed      | Website reveals are triggered by adding our website tag and turning on Unify Intent.                                         |
| Person Enriched (B2B Email)    | 2             | Per person enriched               | People that are uploaded via CSV without emails or prospected via the prospecting step are enriched when run through a Play. |
| Person Enriched (Phone Number) | 4             | Per person enriched               | Phone number enrichment can be turned on in the prospecting node in Unify.                                                   |
| New Hire Tracking              | 5             | Per new hire found                | A new hire is returned when someone within the customer defined specifications that has moved jobs in the last 90 days.      |
| Champion Tracking              | 1             | Per champion track attempt        | Champions are set up by users and are tracked on a monthly basis.                                                            |
| AI Agent                       | 1             | Per question answered per company | Agents can be configured to answer various per each company or person they are run on.                                       |

## Best practices

* **Use Prospecting Limits**: Set limits on the number of people you want to prospect for at each company, especially when targeting only a couple personas.

* **Create Specific Personas**: Be as specific as possible when listing titles to include or exclude in your buyer persona to make sure you aren't prospecting for unqualified contacts.

* **Set Global Exclusions**: Exclusions are a helpful way to make sure that you are not prospecting, enriching, or tracking people who don't fit your ICP.

## Need Help?

* Contact [billing@unifygtm.com](mailto:billing@unifygtm.com) for credit-related questions

* Visit our [Reference Center](/reference/overview) for detailed guides on each feature


# Organization Settings
Source: https://docs.unifygtm.com/reference/management/organization-settings

Configure your organization within Unify.

Users with suffient permission can configure their organization settings within Unify. There are a variety of available configuration options, including:

* **Company name**: The name of your organization.
* **Managed signature**: A standardized email signature to be included in all outbound emails sent by Unify users. This is a template that will dynamically construct each signature based on the user's profile information.
* **Custom user fields**: Additional fields that can be set for each user profile. These values can then be used with other Unify features, such as email signatures and snippets.

You will find these options within [Settings](https://app.unifygtm.com/dashboard/settings/organization/general).

<Frame caption="This is what the organization settings page looks like.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=77094c3afb41f9da578680f8b193abfa" data-og-width="2880" width="2880" data-og-height="3154" height="3154" data-path="images/reference/management/organization-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a98a43f236bd4147035ef11adf78031f 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a85fbf120a9abb18ed75aefbde1695b9 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=eccabec634dade93782d201ac1223f3b 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=317955cfbe234e3e0779edc1f9653500 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=5295e393ffae37e7bea7302955709d6b 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/organization-settings.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f054c96ce5ee3cadfd2486c669165e8f 2500w" />
</Frame>


# User Management
Source: https://docs.unifygtm.com/reference/management/user-management

Invite users and set their roles directly in Unify.

Your teammates can be assigned two different roles in Unify:

* **Admin** — Designed for users who need access to all core Unify capabilities and settings in the organization.

* **Rep** — Designed for users who are primarily focused on creating and managing Sequences in Unify, and who don’t need access to edit Plays or manage organization settings.

<Frame>
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=34a6f6f898173896464d2a0d724b0925" data-og-width="1526" width="1526" data-og-height="612" height="612" data-path="images/reference/management/user-management.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=086e4ede74cc7012c5e90fe388e838f6 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=262a9386ff56c7a1c261cfc7d29ca9b4 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=92be1d3db476bcf7543993581d62912a 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2f57e265a4c5554259e6703a553c4aee 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4338ec5127c0c2dd8208fb48e92e936b 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/user-management.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dc9084f6ecf2cef0db00b468126a9ae5 2500w" />
</Frame>

## Role detail

Each role has a granular set of permissions available to them:

| Permission                                    |    Admin    |           Rep          |
| --------------------------------------------- | :---------: | :--------------------: |
| Invite users and set roles                    |      ✅      |            ❌           |
| Edit Organization settings, including Billing |      ✅      |            ❌           |
| Edit Exclusion settings                       |      ✅      |            ❌           |
| Create and edit Plays                         |      ✅      |            ❌           |
| View Plays                                    |      ✅      |            ✅           |
| Create and edit Sequences                     |      ✅      |            ✅           |
| Create and edit Audiences                     |      ✅      |            ✅           |
| Viewable tasks on Tasks dashboard             | *All tasks* | *Tasks assigned to me* |
| Edit settings to make task skippable          |      ✅      |            ❌           |

## Inviting a new user

To invite a new user, click the **+ Invite** button, and set their role. You can invite multiple users at one time.

You can always change this role after they accept the invite.

<Frame>
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=932db75f5051ffa55d4e7a2ff1c957b7" data-og-width="1520" width="1520" data-og-height="864" height="864" data-path="images/reference/management/invite-team-member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b34e7fe9344442134f2262c522de636d 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9676da32114de711e93fd3032e41086f 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e51420d34de80cc9bc82b2f42e57e4f0 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=63d270739a6aee5cada1c93e8c6cfc96 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dba72e9893816eb07174bdb10fdf465c 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/management/invite-team-member.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c12ccb589e26a0a3167aa37aad7628a5 2500w" />
</Frame>


# Unify Notifications
Source: https://docs.unifygtm.com/reference/notifications/overview

Stay on top of important updates with multi-channel notifications.

export const ReplyIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M9 14l-4 -4l4 -4" />
    <path d="M5 10h11a4 4 0 1 1 0 8h-1" />
  </svg>;

export const TasksIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M9 11l3 3l8 -8"></path>
    <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
  </svg>;

## Overview

Notifications help you stay on top of important updates — from positive replies to Sequences to ensuring no tasks slip through the cracks.

Notifications are available both in-app and through Slack, giving teams visibility wherever they work.

## Notification Types

<CardGroup cols={2}>
  <Card title="Replies to Sequences" icon={<ReplyIcon />}>
    Receive a notification when prospects reply to your Sequences. Admins can customize which reply classifications trigger notifications. Slack notifications can be sent to shared channels to increase team visibility.
  </Card>

  <Card title="New Tasks" icon={<TasksIcon />}>
    Get notified when new tasks are assigned to you. Reps receive task notifications as soon as they are assigned. Admins can choose to be notified of all new tasks or only those assigned to them.
  </Card>
</CardGroup>

## Notification Channels

Unify supports notifications across multiple channels so you can stay informed wherever you work.

### In-App Notifications

Access all your notifications directly within Unify through the notification feed in the left sidebar. The notification icon displays a badge with your unread count, making it easy to see when new updates arrive.

<Frame caption="In-app notification feed">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=3da8d5fd86d0ed6c1e55da7a1d6e82e6" data-og-width="1570" width="1570" data-og-height="1722" height="1722" data-path="images/reference/notifications/in-app-notifications.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=3c7dfc0c3c1bac1c423eb3482e4ee088 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=5fdeeded90851adabb90bccd661e886c 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=7084115ed30c1c372884792944eed24f 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=b87f057ddb501c9968753281d267ff86 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=fe767cf01447a77f02bb6fa444dd115d 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/in-app-notifications.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=7bb22632606e4a4f8f6661a9f8738f4f 2500w" />
</Frame>

In-app notifications provide quick access to relevant context and allow you to take immediate action — like viewing a reply or opening a task — with a single click.

### Slack Notifications

Connect your Slack workspace to receive notifications directly in Slack. Admins can configure notifications to be sent to shared channels for team-wide visibility, or individuals can receive personal notifications through the Unify Slack app.

<Frame caption="Slack notification example">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=3fefa346adc5b880ca0f81eeb2ee6468" data-og-width="1788" width="1788" data-og-height="682" height="682" data-path="images/reference/notifications/slack-notifications.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=ce2ca247f4c3bf5cf56b6a44ddfc5108 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=1c2ab983f1c61c69137f81a1f8014d3d 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=20135d03e4f2224733b0c76bccf835aa 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=24057fd4fe4af6a9bce435da4547b966 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=faccfb7af0af1caa64d8b24b9131de99 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/slack-notifications.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=94e1e42e622e1263d50c9785e8051d69 2500w" />
</Frame>

Slack notifications include all the essential details and provide a direct link back to Unify to take action.

### Email Notifications

<Info>
  Email notifications are coming soon.
</Info>

## Learn More

<Tip>
  Watch [this Loom](https://www.loom.com/share/473d5ba223a94a049fba94312bc3e442?sid=53c24cbf-a1ee-4b57-99a2-b0cb283bc6b9) for a quick overview of how notifications appear in Unify and Slack, and how to update your preferences.
</Tip>


# Notification Preferences
Source: https://docs.unifygtm.com/reference/notifications/preferences

Set how you want to be notified for updates and activities on Unify.

export const WillingToMeetIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" />
      <path d="M15 7a2 2 0 0 1 2 2" />
      <path d="M15 3a6 6 0 0 1 6 6" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" />
      <path d="M15 7a2 2 0 0 1 2 2" />
      <path d="M15 3a6 6 0 0 1 6 6" />
    </svg>
  </span>;

export const PositiveToneIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3" />
    </svg>
  </span>;

export const OutOfOfficeIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M17.553 16.75a7.5 7.5 0 0 0 -10.606 0" />
    <path d="M18 3.804a6 6 0 0 0 -8.196 2.196l10.392 6a6 6 0 0 0 -2.196 -8.196z" />
    <path d="M16.732 10c1.658 -2.87 2.225 -5.644 1.268 -6.196c-.957 -.552 -3.075 1.326 -4.732 4.196" />
    <path d="M15 9l-3 5.196" />
    <path d="M3 19.25a2.4 2.4 0 0 1 1 -.25a2.4 2.4 0 0 1 2 1a2.4 2.4 0 0 0 2 1a2.4 2.4 0 0 0 2 -1a2.4 2.4 0 0 1 2 -1a2.4 2.4 0 0 1 2 1a2.4 2.4 0 0 0 2 1a2.4 2.4 0 0 0 2 -1a2.4 2.4 0 0 1 2 -1a2.4 2.4 0 0 1 1 .25" />
  </svg>;

export const NeedsMoreInfoIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M8 9h8" />
      <path d="M8 13h6" />
      <path d="M14 18h-1l-5 3v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v4.5" />
      <path d="M19 22v.01" />
      <path d="M19 19a2.003 2.003 0 0 0 .914 -3.782a1.98 1.98 0 0 0 -2.414 .483" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M8 9h8" />
      <path d="M8 13h6" />
      <path d="M14 18h-1l-5 3v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v4.5" />
      <path d="M19 22v.01" />
      <path d="M19 19a2.003 2.003 0 0 0 .914 -3.782a1.98 1.98 0 0 0 -2.414 .483" />
    </svg>
  </span>;

export const NeutralToneIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-teal-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 10l.01 0" />
      <path d="M15 10l.01 0" />
      <path d="M9 15l6 0" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-teal-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 10l.01 0" />
      <path d="M15 10l.01 0" />
      <path d="M9 15l6 0" />
    </svg>
  </span>;

export const AutomatedIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M13.256 20.473c-.855 .907 -2.583 .643 -2.931 -.79a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.07 .26 1.488 1.29 1.254 2.15" />
    <path d="M19 16l-2 3h4l-2 3" />
    <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />
  </svg>;

Notification preferences allow you to control how and when you receive alerts for replies, tasks, and updates.
Preferences are divided into two categories: **Workspace notifications** (team-level notifications available for admins) and
**my notifications** (personal notifications available for all users).

## Workspace Notifications

<Note>
  Workspace notifications are only available to users with the **Admin** role.
</Note>

Workspace notifications allow admins to have visibility into any notification for any team member, ensuring admins stay informed about important updates
across the team.

### Workspace Replies

Receive notifications when prospects reply to any Sequence. Admins can customize which reply classifications trigger notifications and choose where to receive them.

<Frame caption="Workspace replies preferences">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=ef4b1271b9fd97c4c35c3b5bf422e114" data-og-width="1840" width="1840" data-og-height="1186" height="1186" data-path="images/reference/notifications/workspace-replies-preferences.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=3a5d1d651e0e0e834a2fd98958cec5dc 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=f2027ad7d03a2024e884885db8953e97 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=62270c8f53adbf92f7c3829b2db513bd 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=8998ef632fee299fe118536f84ec0d0e 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=fdb5a4dd765d8645ca3a16463c672a06 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-preferences.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=6d63133d2a1d39171ff718f0f2d5dc27 2500w" />
</Frame>

#### Reply Classifications

By default, the following reply classifications can be configured.

* <PositiveToneIcon size={20} inline />**Positive** — The email response shows enthusiasm, agreement, or active engagement with the sender's offer, indicating a genuine interest in moving forward
* <WillingToMeetIcon size={20} inline />**Willing to meet** — The recipient's email indicates their openness to schedule a meeting, specifically about the offer mentioned in the initial outreach
* <NeedsMoreInfoIcon size={20} inline />**Needs more info** — The recipient requests additional details or expresses uncertainty about the offer
* <NeutralToneIcon size={20} inline />**Neutral** — The email is objective, factual, respectful, unemotional, and polite yet concise

You can add additional classifications if you want to receive notifications for other types of replies. For example, if you want to be notified
about <OutOfOfficeIcon size={20} inline />**Out of Office** replies, you can add that classification in your settings.

<Tip>
  See [Reply Classifications](/reference/sequences/replies#reply-classifications) for detailed definitions of all classification types.
</Tip>

<Frame caption="Adding new reply classifications">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=28d2637b529f890b19c1a98ad20299e3" data-og-width="1776" width="1776" data-og-height="640" height="640" data-path="images/reference/notifications/workspace-replies-new-classification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=0a13b71397e240a467e739f20c17d9f6 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=910c9ad1327bf32fac1cff39dbf73992 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=e42af72b145d85d2f1929a029213e6a4 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=83aa1cfe96c9d9d5aece6d382d88e1bd 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=16ff019eda3507928186f640548cf26d 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-new-classification.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=658d096f1aa04f2f3819cb5d543297e6 2500w" />
</Frame>

#### Excluding Classifications

Some replies can have multiple classifications. You can exclude specific classifications from triggering notifications. **If a reply has any excluded classification, no notification will be sent**, even if it also has other classifications that would normally trigger an alert.

Common exclusions include:

* <OutOfOfficeIcon size={20} inline />**OOO** (Out of Office) — Automated away messages
* <AutomatedIcon size={20} inline />**Automated** — Auto-responders and system-generated replies

<Frame caption="Workspace replies exclusions">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=a51cd5c5c47100efce99c03187fa101e" width="700" data-og-width="1829" data-og-height="965" data-path="images/reference/notifications/workspace-replies-exclusions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=23cbef5864c16546c924473fcd9d9879 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=d489db482f67b4b6890e6c46a16d9671 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=8c9ed59d5fbf57609e8237a632b98f52 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=4115c55ddd7ad7b41e8166b33786c106 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=309193aafef7110ebd63f0f62010d0a3 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-replies-exclusions.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=eebe543ff8667958f39d8a565d8693d7 2500w" />
</Frame>

### Workspace Tasks and Updates

Receive notifications for all tasks and updates created for anyone on your team. This allows admins to stay informed about task assignments and progress across the organization.

<Frame caption="Workspace tasks preferences">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=15bb5e17173984b8f5a619b0f75e8598" width="700" data-og-width="1840" data-og-height="328" data-path="images/reference/notifications/workspace-tasks-preferences.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=b54fcda78410641dcc218488edebf35a 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=bb8392699dfcfdb6b2a35698577b0c87 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=50c754ee2fbe1ab716abb15b91059932 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=e8cb7c5ccba058ba98a07387da6a0569 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=671d6a0aa9c5d57b789317685fb5d2a5 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/workspace-tasks-preferences.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=d823681399ad94eb15575ebacd796b5d 2500w" />
</Frame>

## My Notifications

Personal notifications are available to all users (both Admins and Reps) and allow you to manage alerts specific to you.

<Frame caption="Personal notification preferences">
  <img src="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=bc0d31c9ea8ff267e3521d380fef0834" width="700" data-og-width="2058" data-og-height="846" data-path="images/reference/notifications/personal-preferences.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=280&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=dd0830fec6b902a9ce25cb223186f7e1 280w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=560&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=bb0d56602af436fc07ac40d6d99beebe 560w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=840&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=9f3cb55de63ea342ac9020bdf3ecdc11 840w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=1100&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=1950c8b2cb0bc3aaadd624beaddccc4c 1100w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=1650&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=bee37d74a8c6a6b98806fb8fa8d6da32 1650w, https://mintcdn.com/unify-19/5THlZ59mmYYtD-bs/images/reference/notifications/personal-preferences.png?w=2500&fit=max&auto=format&n=5THlZ59mmYYtD-bs&q=85&s=801cab79272b6a7a2c0cd00870d6f87a 2500w" />
</Frame>

### Connecting Your Slack Account

To receive Slack notifications, you need to connect your personal Slack profile to Unify.

<Steps>
  <Step title="Connect to your Slack Organization">
    Admins must configure their tenant's connection to Slack before users can select their profiles.
  </Step>

  <Step title="Select your Slack profile">
    Click on the Slack profile selector to connect your account. Slack notifications will be sent directly to your Unify Slack app.
  </Step>
</Steps>

<Tip>
  If you don't see your Slack profile in the dropdown, or if the options are disabled,
  make sure the Unify Slack app is installed in your workspace and you've been added to it.
</Tip>

### My Tasks and Updates

Receive notifications for tasks assigned to you and updates on those tasks.

**Notification channels:**

* **Slack** — Direct messages in Slack (requires Slack profile connection)
* **In app** — Notifications in the Unify notification feed

## Notification Channels

Unify supports two notification channels:

| Channel    | Description                                       | Requirements                                         |
| ---------- | ------------------------------------------------- | ---------------------------------------------------- |
| **Slack**  | Receive notifications as direct messages in Slack | Must connect your Slack Organization / Slack profile |
| **In app** | View notifications in the Unify notification feed | No setup required                                    |

You can enable either or both channels for each notification type.

## Default Settings

All new users are configured with default notification preferences upon onboarding.
You can customize these settings at any time from the notification preferences page.


# Reference Guide
Source: https://docs.unifygtm.com/reference/overview

Bring your most creative go-to-market ideas to life with Unify.

export const UserIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M8 7a4 4 0 1 0 8 0a4 4 0 0 0 -8 0"></path>
    <path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"></path>
  </svg>;

export const SignalsIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M12 10.941c2.333 -3.308 .167 -7.823 -1 -8.941c0 3.395 -2.235 5.299 -3.667 6.706c-1.43 1.408 -2.333 3.621 -2.333 5.588c0 3.704 3.134 6.706 7 6.706s7 -3.002 7 -6.706c0 -1.712 -1.232 -4.403 -2.333 -5.588c-2.084 3.353 -3.257 3.353 -4.667 2.235"></path>
  </svg>;

export const SettingsIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"></path>
    <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"></path>
  </svg>;

export const SequencesIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M10 14l11 -11"></path>
    <path d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5"></path>
  </svg>;

export const PlaysIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"></path>
    <path d="M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"></path>
    <path d="M11 19h5.5a3.5 3.5 0 0 0 0 -7h-8a3.5 3.5 0 0 1 0 -7h4.5"></path>
  </svg>;

export const MailboxesIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M10 21v-6.5a3.5 3.5 0 0 0 -7 0v6.5h18v-6a4 4 0 0 0 -4 -4h-10.5"></path>
    <path d="M12 11v-8h4l2 2l-2 2h-4"></path>
    <path d="M6 15h1"></path>
  </svg>;

<CardGroup cols={2}>
  <Card title="Plays" icon={<PlaysIcon />} href="/reference/plays/overview">
    Automate your go-to-market motion with repeatable strategies and campaigns.
  </Card>

  <Card title="Signals" icon={<SignalsIcon />} href="/reference/signals/overview">
    Identify and engage your target accounts with real-time buying signals.
  </Card>

  <Card title="Sequences" icon={<SequencesIcon />} href="/reference/sequences/overview">
    Personalize your outreach at scale with dynamic multi-channel outbound.
  </Card>

  <Card title="Deliverability" icon={<MailboxesIcon />} href="/reference/deliverability/overview">
    Safeguard your deliverability and domain reputation as you scale your
    outbound.
  </Card>

  <Card title="Integrations" icon={<SettingsIcon />} href="/reference/integrations/overview">
    Connect and orchestrate your full stack end-to-end in minutes, not months.
  </Card>

  <Card title="Management" icon={<UserIcon />} href="/reference/management/user-management">
    Add or remove users, control organization settings, and set up
    authentication.
  </Card>

  <Card title="Chrome extension" icon="chrome" href="/reference/browser-extension/installation">
    Access Companies and People in Unify on your CRM or the larger world wide web.
  </Card>
</CardGroup>


# Play Actions
Source: https://docs.unifygtm.com/reference/plays/actions

Actions are the building blocks of Unify Plays.

## Overview

Plays chain together actions to perform anything from simple automations to
complex and dynamic outbound campaigns. Below are the actions you can choose
from when creating a Play.

## Core actions

### AI qualification

AI agents are powerful tools for researching companies or people and answering
questions about them. In Plays, the answers provided by an agent can be used to
determine whether a company or person is qualified or not.

When you select the agent qualification action, you will be able to choose an
existing agent or create a new one. Every agent has a set of questions that it
will answer about the given record. In the action configuration panel, you can
select which answers are required for the record to be considered qualified.

<Frame caption="The configuration for an agent action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ae13f5e001b11b7500a6fcb0e3563515" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/ai-agent-qualification-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6c6e75de0cac43f95ec2480944e6d6e5 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a5d665f93a5d6dcbf87f010876f05002 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2b480c2af9001e5b99ca790c054599d0 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6bb7120518b6389e859b2bf535a63d62 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a33ab414ab9352d5d25aa0b434fb3814 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/ai-agent-qualification-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6ccc3b038d6111f94c6a3f1baf4df75a 2500w" />
</Frame>

### Assign owner

The owner assignment action allows you to assign a record to a specific owner in
Unify. Every company and person record in Unify has an owner, and this action
allows you to set or change the owner of a record.

<Frame caption="The configuration for an assign owner action.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=241efecb2718679e70d2d3bc25a601ae" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/assign-owner-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=f7e6187ed7b447c70ddb52356f6d446a 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=20fe9b79869563cb7d4f926e78a2b9a2 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=31a10c55b9163de8a869d1527a3f90e8 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=91615bfcb17d2961810c73f28494336d 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=cda13b27155238d5d2d00d8adcff8497 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/assign-owner-action.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=3e754e5f4ec7257534101836a685b671 2500w" />
</Frame>

When you connect a CRM to Unify, the owner of the corresponding records in the
CRM will be synced into Unify. For records that don't yet have an owner or don't
yet exist in the CRM, you can use this action to assign an owner. You can also
choose to update the owner if desired.

### Prospect

One of the most common use cases for Plays is to find new people to reach out
to. The prospecting action takes a company record as input and finds new people
at the company matching specific personas and criteria.

When you select the prospecting action, you can specify one or more personas to
search for. The personas are considered in order, so the first persona will be
preferred over the second, and so on.

<Frame caption="The configuration for a prospecting action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=cdf115e4f29086a6afd0f0987d3dcdc5" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/prospect-for-people-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8ed8122b0527b0c3f6ab8f4115405d01 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=89c7177cf547bca510be40851d41ac60 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=85602b0d1ab14f2d61e835f00c0aa8e5 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1022f088bda1a428784cade350923ddb 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=80ea4f009983525ff923898c150e104a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/prospect-for-people-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be09c0c6438ceb3184d7a64b4678ffe1 2500w" />
</Frame>

You can also specify a limit on the number of people to find per company. If the
**Include existing people** option is enabled, existing people at the company
already in Unify will count towards this limit. This can be useful if you want
to save prospecting credits on companies you already have relevant contacts for.

### Sequence

The sequence enrollment action makes building automated outbound campaigns
easier than ever. You can choose which sequences to send people to based on
which personas they match.

<Frame caption="The configuration for an sequence enrollment action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1b5d3852b0b12dc65e30b9cd7ed6ad51" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sequence-enrollment-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c7b2d1bfcb3c6e146d0155d5b220c96c 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=aae9877c386d1ed79c333a0f35cab8f1 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a06e8690ce9e30895d90844bcbb222ce 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=30cae8d0624e827b01121be4808794a9 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dc475a4e95775b2b303e9c764cd80e8c 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sequence-enrollment-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=71f1ad0f8ab6917c243068da63acc00a 2500w" />
</Frame>

The routing configuration provides a way to specify which mailboxes and
sequences should be used for people this action runs on. You can specify a
set of mailboxes to use or choose to use a mailbox associated with the [company
or person record owner](/reference/plays/actions#assign-owner-action).

<Frame caption="The routing configuration for a sequence enrollment action.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=90333760d59b78640f562e1cd5701d24" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/sequence-enrollment-action-routing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=eea09adac7e723f93374c8169504d327 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=c716166a7e7b6dbd62faeee62898deae 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=3e5a27e0c59ce240e9001fa0a3acf6a1 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=4848b55de15584a80757e3eb784f0e64 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=d7702690348026a55eaeef086d7f8d07 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/sequence-enrollment-action-routing.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=183776511118dc8ff3e92ca95feaece8 2500w" />
</Frame>

You also have the option to set a limit on how many people to enroll per
company, which is generally recommended to avoid overtargeting a single company.
This limit applies globally across play runs, so if multiple Plays run on the
same company, this limit will be shared across all of them.

### Slack alert

The Slack alert action allows you to send a customized Slack message at any
point in a Play. You can send messages to any public channels or DM any users in
your workspace.

<Frame caption="The configuration for a Slack alert action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=14bf74a7d4b2f7c74e3f0e08a911591b" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/plays/slack-alert-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=505cbd1557634e7e5ec57c60136930de 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2263b06235fe83b4638abd810a6253bf 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c79abd0edb48f14903b552709e629308 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=75e0956f1a36707faab6d7a938c525d0 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1c5daf22f8547f8d01cd253cf520f6f6 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/slack-alert-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7eba5f36bc4016b3263cd0bba4f74881 2500w" />
</Frame>

The contents of the messages can be customized with template variables, so you
can include information about the record that triggered the action.

<Note>
  If the value for a template variable is missing, the message will still be sent,
  but the variable will be replaced with `Unknown`.
</Note>

You may optionally tag the owner of the account (e.g. `@John Doe`), so they can
be easily notified of the alert. You can also include intent signal information
containing recent website visitors, G2 page views, and more.

This action is available when Slack connected to Unify. See the [Slack Integration Guide](/reference/integrations/slack)
for information on integrating Slack with Unify.

### Sync to HubSpot

The HubSpot sync action allows you to create or update a record in HubSpot based
on a company or person record in Unify. This action will use the settings you've
configured for HubSpot in the Unify settings.

You also have the option to specify additional default field values. These will
be written to HubSpot unless a different Unify field is already mapped to the
HubSpot field.

<Frame caption="The configuration for a HubSpot sync action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f621f35815f62e850ca80e55f4443364" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sync-to-hubspot-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9825e826601053748d87d9de59d7e0f5 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=20d0bc07a5b05a115441faa323c1082b 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=041ec6ccbdaa35058aad35e148b6cf34 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f54849a5b3d7de68afef3fe32e296913 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=012298f9c0a85c1a517159a3ed35e6eb 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-hubspot-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=80594bc4970af042e2e2ec74b440d803 2500w" />
</Frame>

### Sync to Salesforce

The Salesforce sync action allows you to create or update a record in Salesforce
based on a company or person record in Unify. This action will use the settings
you've configured for Salesforce in the Unify settings.

You also have the option to specify additional default field values. These will
be written to Salesforce unless a different Unify field is already mapped to the
Salesforce field.

<Frame caption="The configuration for a Salesforce sync action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8f10439466d6f16b8241a250fefca8a4" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/sync-to-salesforce-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=720643418a4794f35560eb724531eaaa 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b7d432d3c2077e0739f4a061694529bb 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=35a75ba86229884c8afe9098e89a7460 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=480e4d11717e82ab6b7217365a0ba9d4 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3e55ede04afce22bdab8baa3005f9b0b 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/sync-to-salesforce-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=77eb4e5d5e2e48fe891d1a78e41e334a 2500w" />
</Frame>

## Utility actions

### Loop

<Note>
  In order to fully understand the purpose of loops and how to use them
  effectively, it's recommended that you read about action [inputs and outputs](/reference/plays/building-a-play#inputs-and-outputs) first.
</Note>

Most actions run on one record at a time. Loops are a simple way to run one or
more actions on every record in a list.

For example, a **Prospect for new People** action will return a list of people.
You can connect a loop action to the prospecting action and then add actions
within the loop. The first action in the loop will receive one person at a time.

### If / Else

The if-else action creates a branch in a Play, evaluates some conditions for
records, and sends them down a specific path based on the result. This allows
you to perform different actions on different records based on criteria that you
specify.

<Frame caption="The branch created by an if-else action in a Play.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6e5ecbd41ecd17ae34dc1b98665cc3a2" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/if-else-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c93964321c4134bddc9da21447ea2377 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=83db77977ed3077ca874d2b0adda6ae0 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=650061bb55f4b6a7126f337dfc1828e8 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9a784963a3528229f4a442a41a9a4383 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=dd573137658adf0eae57e5c03e79726a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/if-else-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1adf6d638fe085769bb1404a69043bbf 2500w" />
</Frame>

This action enables you to solve a wide variety of more complex use cases using
Plays. For example, you can enroll people into different sequences based on
their company firmographics, exact job title, or custom CRM field values.

### A/B Test

The A/B test action allows you to route records down a specific path based on a set probability.
This is useful for testing different sequences or actions.

<Frame caption="The branch created by an A/B test action in a Play.">
  <img src="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=f63444050b67c693f47c36a5b78f3ccd" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/actions/ab-test-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=280&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=4c8625d2c4dfa8c249adcafbb9c0cad4 280w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=560&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=ccc851d8662083b1efaeb74c2a0d4216 560w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=840&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=2cdf8c1d984cd05ef9f5137ad431cd90 840w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=1100&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=907017a18c2426add57f331952413d66 1100w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=1650&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=ecb4be051168d36ad0246488c6c93fb2 1650w, https://mintcdn.com/unify-19/MyP9qE51P6xDuum4/images/reference/plays/actions/ab-test-action.png?w=2500&fit=max&auto=format&n=MyP9qE51P6xDuum4&q=85&s=69cd2bba618fa4243432729f08e57f41 2500w" />
</Frame>

### Delay

The Delay action waits for a specified amount of time before continuing to the
next action in a Play. This can be useful for spacing out actions in a Play and
ensuring that actions are performed at the right time.

<Frame caption="You can customize the amount of time to wait before the next action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b7884bf007fb2519a3308b3291e13961" data-og-width="2304" width="2304" data-og-height="1639" height="1639" data-path="images/reference/plays/delay-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4a5018ca59f685324dcefbe2eb2ee997 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ded13504affdc8118dca88fd75ddb606 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=96469084c423ebf4ed3f222c20a70db0 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=900d4337940335212f29b7a9fa41884e 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=71cdca69756ac257d742dc1679834000 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delay-action.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7557c2a42ddf75c799a79fc005636890 2500w" />
</Frame>

This action is particularly useful when combined with if-else actions. For
example, when a person visitors your website, it can be useful to wait a few
minutes before taking action to see which pages they end up visitor or whether
they fill out a form.

### Get Company

If you have a person record, you can use this action to fetch the company that
the person works at. If the person does not have a company associated with them,
this action will not return any result.

### Get People

If you have a company record, you can use this action to fetch people that work
at the company. Unlike the **Prospect for new People** action, this action only
looks for people that already exist in Unify rather than prspect for new people.

## Coming soon

There are lots of additional actions in the works including more powerful AI
features and deep integrations with third-party tools. If you're interested in
an action that isn't available yet, [let us know](mailto:support@unifygtm.com)!
We'll get you in the beta as soon as it's ready.


# Building a Play
Source: https://docs.unifygtm.com/reference/plays/building-a-play

Learn the fundamentals of creating Plays in Unify.

export const PlayBuilderCompanyHandleDark = () => <svg className="hidden dark:block" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#403C2A" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#404040" />
    <g clip-path="url(#clip0_2769_1689)">
      <path d="M5.75 16.25H16.25" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 8.66663H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 11H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 13.3334H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 8.66663H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 11H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 13.3334H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M6.91699 16.25V6.91667C6.91699 6.60725 7.03991 6.3105 7.2587 6.09171C7.47749 5.87292 7.77424 5.75 8.08366 5.75H13.917C14.2264 5.75 14.5232 5.87292 14.7419 6.09171C14.9607 6.3105 15.0837 6.60725 15.0837 6.91667V16.25" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1689">
        <rect width="14" height="14" fill="white" transform="translate(4 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderCompanyHandleLight = () => <svg className="block dark:hidden" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#FFFAE6" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#E2E2E2" />
    <g clip-path="url(#clip0_2769_1689)">
      <path d="M5.75 16.25H16.25" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 8.66663H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 11H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 13.3334H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 8.66663H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 11H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 13.3334H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M6.91699 16.25V6.91667C6.91699 6.60725 7.03991 6.3105 7.2587 6.09171C7.47749 5.87292 7.77424 5.75 8.08366 5.75H13.917C14.2264 5.75 14.5232 5.87292 14.7419 6.09171C14.9607 6.3105 15.0837 6.60725 15.0837 6.91667V16.25" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1689">
        <rect width="14" height="14" fill="white" transform="translate(4 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonListHandleDark = () => <svg className="hidden dark:block" width="23" height="22" viewBox="0 0 23 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" fill="#323F3E" />
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" stroke="#404040" />
    <g clip-path="url(#clip0_2769_1947)">
      <path d="M12.083 12.1667C12.083 10.5558 13.3889 9.25 14.9997 9.25C16.6105 9.25 17.9163 10.5558 17.9163 12.1667V12.4583" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M15 9.25C15.9665 9.25 16.75 8.4665 16.75 7.5C16.75 6.5335 15.9665 5.75 15 5.75C14.0335 5.75 13.25 6.5335 13.25 7.5C13.25 8.4665 14.0335 9.25 15 9.25Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M5.08301 15.6667V15.0833C5.08301 12.8282 6.91118 11 9.16634 11C11.4215 11 13.2497 12.8282 13.2497 15.0833V15.6667" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.16634 11C10.455 11 11.4997 9.95529 11.4997 8.66665C11.4997 7.37798 10.455 6.33331 9.16634 6.33331C7.87768 6.33331 6.83301 7.37798 6.83301 8.66665C6.83301 9.95529 7.87768 11 9.16634 11Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1947">
        <rect width="14" height="14" fill="white" transform="translate(4.5 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonListHandleLight = () => <svg className="block dark:hidden" width="23" height="22" viewBox="0 0 23 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" fill="#F0FBFA" />
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" stroke="#E2E2E2" />
    <g clip-path="url(#clip0_2769_1947)">
      <path d="M12.083 12.1667C12.083 10.5558 13.3889 9.25 14.9997 9.25C16.6105 9.25 17.9163 10.5558 17.9163 12.1667V12.4583" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M15 9.25C15.9665 9.25 16.75 8.4665 16.75 7.5C16.75 6.5335 15.9665 5.75 15 5.75C14.0335 5.75 13.25 6.5335 13.25 7.5C13.25 8.4665 14.0335 9.25 15 9.25Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M5.08301 15.6667V15.0833C5.08301 12.8282 6.91118 11 9.16634 11C11.4215 11 13.2497 12.8282 13.2497 15.0833V15.6667" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.16634 11C10.455 11 11.4997 9.95529 11.4997 8.66665C11.4997 7.37798 10.455 6.33331 9.16634 6.33331C7.87768 6.33331 6.83301 7.37798 6.83301 8.66665C6.83301 9.95529 7.87768 11 9.16634 11Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1947">
        <rect width="14" height="14" fill="white" transform="translate(4.5 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonHandleDark = () => <svg className="hidden dark:block" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#323F3E" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#404040" />
    <path d="M6.91699 15.6667V15.0833C6.91699 12.8282 8.74516 11 11.0003 11C13.2555 11 15.0837 12.8282 15.0837 15.0833V15.6667" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M11.0003 11.0002C12.289 11.0002 13.3337 9.95547 13.3337 8.66683C13.3337 7.37816 12.289 6.3335 11.0003 6.3335C9.71166 6.3335 8.66699 7.37816 8.66699 8.66683C8.66699 9.95547 9.71166 11.0002 11.0003 11.0002Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
  </svg>;

export const PlayBuilderPersonHandleLight = () => <svg className="block dark:hidden" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#F0FBFA" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#E2E2E2" />
    <path d="M6.91699 15.6667V15.0833C6.91699 12.8282 8.74516 11 11.0003 11C13.2555 11 15.0837 12.8282 15.0837 15.0833V15.6667" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M11.0003 11.0002C12.289 11.0002 13.3337 9.95547 13.3337 8.66683C13.3337 7.37816 12.289 6.3335 11.0003 6.3335C9.71166 6.3335 8.66699 7.37816 8.66699 8.66683C8.66699 9.95547 9.71166 11.0002 11.0003 11.0002Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
  </svg>;

## Actions and triggers

The building blocks of Plays are called *actions*. Each action is a different
step of a Play, each representing a different task that can be automated in
Unify.

Every Play stars with a special type of action called a *trigger*. A trigger is
the starting point of your Play which defines when the Play should be executed
and what data should be provided to it.

<Frame caption="An empty Play showing the trigger selection panel.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b84850735993e7c46cc25f2a9bd67217" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c0192afc78305e086c2bf33dd880935a 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=cb846df40e17ec27f51d55135771a420 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3b46b920b8dbfde7da9c7ce8e28a7004 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=402ccd79c0ca86d18d0bd415b5a54a43 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bfcf5eb74be446cc7f5ad0e0b6ec5bb1 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9643af5c2539b32b75aa9cdbe39598df 2500w" />
</Frame>

Here are a few of the triggers you can choose from:

* **Record enters an Audience**: Run a Play once on every company or person that
  "enters" an Audience. Audiences can be reused across multiple Plays.
* **Record matches criteria**: Run a Play once on every company or person that
  matches a set of filters. This trigger is similar to the audience trigger, but
  it doesn't require you to create a separate audience. Useful when you don't
  need to create a reusable audience.
* **Manual**: Only run a Play when it is manually triggered. For example, you
  can send individual companies or people to a Play, or you can send an entire
  audience.

Once the trigger is selected, you can start adding additional actions to the
Play. Each action performs a different task. Actions can be chained together or
perform branching logic based on the results of the previous action.

Here are some of the most commonly used actions:

* **AI Agent Qualification**: Perform AI-powered research to answer qualifying
  questions about a company or person.
* **Prospect for new People**: Find new people at a company matching specific
  personas. You can specify a limit on the number of people to find.
* **Sequence Enrollment**: Enroll a person in a sequence. You can route people
  to different mailboxes and sequences based on their persona.
* **Write to Salesforce or HubSpot**: Sync a company or person to Salesforce or
  HubSpot. This will create or update a record in your CRM.

You can find details about the full set of available triggers and actions in the
reference sections below:

<Card title="Triggers" icon="link" iconType="sharp-regular" href="/reference/plays/triggers" horizontal>
  See the full list of triggers available in Unify and how to use them.
</Card>

<Card title="Actions" icon="link" iconType="sharp-regular" href="/reference/plays/actions" horizontal>
  See the full list of actions available in Unify and how to use them.
</Card>

## Inputs and outputs

Each action receives an input and produces an output. Actions in the Play
Builder have small colored symbols that represent what type of input and output
they expect.

Here's what each symbol represents:

|                                    Symbol                                   |   | Value                                 |
| :-------------------------------------------------------------------------: | - | :------------------------------------ |
|     {<PlayBuilderPersonHandleLight />}{<PlayBuilderPersonHandleDark />}     |   | A single person record.               |
| {<PlayBuilderPersonListHandleLight />}{<PlayBuilderPersonListHandleDark />} |   | A list of one or more person records. |
|    {<PlayBuilderCompanyHandleLight />}{<PlayBuilderCompanyHandleDark />}    |   | A single company record.              |

Plays work by connecting each action's output to a matching input on another
action. This is how data flows through the Play and how each action knows what
to do.

## Connecting actions

To connect two actions, click on the output symbol of the first action and drag
the connection to the input symbol of the second action.

<Frame caption="Connect two actions by dragging a connection line between them.">
  <video autoPlay muted loop playsInline className="w-full aspect-video dark:hidden" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/draw-connection-light.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=37e6d321718e6ca91064c2797a06e42c" data-path="images/reference/plays/draw-connection-light.mp4" />

  <video autoPlay muted loop playsInline className="hidden w-full aspect-video dark:block" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/draw-connection-dark.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=0da77a575ba6dbdb667e2656764d8e12" data-path="images/reference/plays/draw-connection-dark.mp4" />
</Frame>

When adding a new action to the Play Builder, you can drag and drop it on top of
another action to automatically connect them.

<Frame caption="Drag a new action onto another action to quickly connect them.">
  <video autoPlay muted loop playsInline className="w-full aspect-video dark:hidden" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/drag-and-drop-light.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a68834a16044eb4f63b7c3951bf03b34" data-path="images/reference/plays/drag-and-drop-light.mp4" />

  <video autoPlay muted loop playsInline className="hidden w-full aspect-video dark:block" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/drag-and-drop-dark.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=82b46126a9a4cbe00d40f989af75e92b" data-path="images/reference/plays/drag-and-drop-dark.mp4" />
</Frame>

Another shortcut for connecting actions is to move any action near to another
action. Once the input and output symbols are close enough, they will
automatically be connected.

<Frame caption="Move an action near another action to automatically connect them.">
  <video autoPlay muted loop playsInline className="w-full aspect-video dark:hidden" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/drag-to-connect-light.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=021fdffb3cf7318941b9724f792ccace" data-path="images/reference/plays/drag-to-connect-light.mp4" />

  <video autoPlay muted loop playsInline className="hidden w-full aspect-video dark:block" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/drag-to-connect-dark.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=15ebad7cca464ed3f0fb08056e6ed037" data-path="images/reference/plays/drag-to-connect-dark.mp4" />
</Frame>

To delete a connection, click on the connection line and press the **Backspace**
or **Delete** key.

<Frame caption="Delete a connection by clicking on it and pressing the backspace key.">
  <video autoPlay muted loop playsInline className="w-full aspect-video dark:hidden" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delete-connection-light.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d652e69c963a2c55ae5b25688d33f503" data-path="images/reference/plays/delete-connection-light.mp4" />

  <video autoPlay muted loop playsInline className="hidden w-full aspect-video dark:block" src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/delete-connection-dark.mp4?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=eb58839cb879f849219a7c98d7174b5c" data-path="images/reference/plays/delete-connection-dark.mp4" />
</Frame>

## Save and publish

When you first create a Play, it is automatically saved as a draft. You can
leave and return later to finish building the Play without losing your progress.

Once you're ready to start running the Play, you can publish it. Published Plays
will run automatically based on the trigger you've selected. To publish a Play,
click the **Publish** button in the top right corner of the Play Builder.

<Frame caption="The confirmation shown when publishing a Play.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8c606c3f5d7fcd5c88275e1599200800" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-publish-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=185d74c8a4d36d1079d4189e2a255879 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4c8ba9d3a1d35cdbeb2c226b0d93a250 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=8a783349aa36cd6058909c221c41d71a 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d8c62b1176471a12c0e34ce83dd78a67 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=76c5d7c419ac4212e36d293770639fd4 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-publish-modal.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4fe97f07574ff842a940d34ef2831623 2500w" />
</Frame>

After publishing a Play, you can still make changes to it. Any changes you make
will be saved as a new draft. You can publish the new draft at any time by
clicking the **Publish** button again. You can also discard the draft and revert
to the last published version.

If you want to temporarily stop a Play from running, you can pause it by
toggling the pause button to the left of the **Publish** button. Pausing a Play
will prevent it from running until you resume it.

## View logs

Once a Play starts running, you can view the logs to see which companies and
people the Play has run on. In the top left corner of the Play Builder, click
on **Logs** to see the full history of Play executions.

<Frame caption="The logs view showing the history of Play executions.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=64399fad0d6eeb815b02dc18bf6da612" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-logs-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9160e79ea6ebd75eb0632b23ef22b522 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=195ff1bbfffdcda2f490831cd524375e 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=0678dae4300d19c76bc1b1795d16807f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a5f78d1560a02d21f9e1e0d67fd19d04 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ed330341f861acf8bd1bc085dd8c8cc8 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-table.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=018927052d1219ee2b89cc3f0bc86069 2500w" />
</Frame>

Within the logs view, you can see the status of each Play execution, including
in-progress, completed, and failed executions. You can click on any row of the
logs table to see more details about that specific execution.

<Frame caption="The details view showing the results of a single Play run.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1d8180d94a2444af4a65c469c5772882" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-logs-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9d0242c5c215c2c2574a9c8e8587938c 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=48ca69ce39c74bf8baacb048f1ab9af6 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e93d2b88f8ffb6d88345135ba10f51e9 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6c926e84a438d1c43904345c666d0315 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ec8a8c90b532be9321b2c661ded2849a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-logs-details.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d9e582f381056659e158654c9275e9b2 2500w" />
</Frame>

The exact path this record took through the Play is highlighted on the right
side of the details view. You can see exactly which actions ran and what the
results were at each step.

## View metrics

In addition to logs, you can view metrics for each Play to see how it's
performing over time. In the top left corner of the Play Builder, click on
**Metrics** to see overview metrics and charts for the Play and each of its
actions.

<Frame caption="Overview metrics for the play.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=09e325d3f07b6ad29e379e4a2a4f9540" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-metrics-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9691df16076e0dc18c17c60c1a37af88 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=36dff2ba80862bba820f18e30d5f085d 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=70674feb6cbafe6bf53e58694a23a4c8 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d4f27f91941fa6ee77cea2001ebeacd1 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=35fa3a0666604c3812321ab2897c50f9 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-overview.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3a4941030244e79b92cbd6004207cea1 2500w" />
</Frame>

You can click on any action to see detailed information about how it's
performing. For example, clicking  on an agent qualification action will let
you measure how many records are being qualified over time and why.

<Frame caption="Detailed metrics about an AI Agent Qualification action.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2af9777c1e699157ee41ca0f565a8976" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-metrics-agent-qualification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=eacaff82a1d5b060f8f8817c0fc9761a 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ad34f5062f875d12e55b7406a7116d69 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=482b9f334dac3f203b957900dcc5d727 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=cee8ec8893cd33e19cf4dd8c79b59754 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ba59cd3f5a3c290c3f5f5eda5400ee70 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-metrics-agent-qualification.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=031375912055b130385e8a1a2bdd55a3 2500w" />
</Frame>

The action-specific metrics pages will also show you the records that have
passed through that action and their results.


# Unify Plays
Source: https://docs.unifygtm.com/reference/plays/overview

Learn what Unify Plays are and how to use them.

## What are Plays?

Plays are automated workflows that let you build and execute repeatable
strategies. Unify manages the logistics of coordinating and scaling all of the
details.

<Frame>
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e45cb527afea9b440f781b3c362b3757" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-log-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d9e5f99522af7614de7ef074d6928298 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6f4be0c0bad7697962c18e3fc54ebdc9 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=85e0fc5e0858129ea8c2f63a746aee2d 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=872421533031903076a3c6ff363748e1 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=06269568e3c70cdd9c67768ba0c419b3 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=509373770b388b3dafa75a316e133068 2500w" />
</Frame>

Building scalable and effective sales, marketing, and GTM strategies requires
successfully coordinating two key components:

* **Data**: Countless data sources go into building scalable automations. This
  data is traditionally scattered across tools and databases, but Unify
  centralizes it in one place.
* **Actions**: Researching companies, identifying decision-makers, executing
  multi-channel outreach, and more. Taking the right action at the right time
  is crucial to success.

Unify is a purpose-built system of action that solves this problem. Plays let
you define a series of actions that will be taken on companies or people at
exactly the right moment.

## Use cases

Plays are a versatile tool that can be used to build out anything from standard,
reliable outbound strategies to complex and innovative growth campaigns. Here
are some of the most popular use cases for Plays:

* **Warm Outbound**: Find prospects at companies matching intent signals and
  reach out to them with personalized messaging at just the right time.
* **Champion tracking**: Keep tabs on champions of your business and reach out
  to them when they take a role at a new company.
* **List building**: Take a list of companies and turn it into high-quality
  leads by enriching the data and finding new contacts in relevant roles.

These are just a few of the most common ways Plays are used. Plays provide the
flexibility to build arbitrarily complex automations tailored to your goals.

<Tip>Check out the tutorial [How to Create a Play](/tutorials/how-to-create-a-play) for a hands-on introduction to Plays!</Tip>


# Play Triggers
Source: https://docs.unifygtm.com/reference/plays/triggers

Triggers represent the events and data sources that a Play runs on.

## Overview

Plays run on invidiual records, such as companies or people. Triggers define
when a Play should run and what data should be provided to it. Below are the
triggers you can choose from when creating a Play.

## Available triggers

### Champions

This trigger is a shortcut for running a Play on champions that Unify has
tracked for your business. Once selected, you can customize the matching
criteria similar to the record match trigger. This trigger always returns
People.

<Frame caption="The configuration panel for a champions trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a26582da988298dbdedc223863e17682" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/champions-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=74b7e908d46c5baea5e5dffb763b6cf1 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9c6d99afe8db8e34f4b7a81675e64217 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f2c7222c77b79c3f039256474a9b7f2f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=00737c09734267cecf660579ade055a8 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=0677416141bc204f1fc82384078465d3 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c6dec9c784c790daaf0bec4584f1ff47 2500w" />
</Frame>

In order to use this trigger, you must have enabled and configured champion
tracking in your settings. For more information, see [Champion Tracking](/reference/signals/champions).

### Find lookalike companies

This trigger runs a Play on companies that are similar to a set of companies
you specify. This is useful for finding new companies that are similar to your
existing customers or ideal customer profile.

<Frame caption="The criteria panel for a lookalike companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1b6b19abcb96637ada83885fc3594c7" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-criteria-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=24108a56f46defdb2a7cd8532d7f35c3 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e082600be56e2e8e51f92f5b6c2b53d1 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ad6e60a9ab61f9bb56dc6b85c4f0fa9d 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=533504120e70cc6efedf3c40f4d4b114 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e05e930b767632122fda43bbd544dade 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21eddece4a8dbbd255acce80fe6116e9 2500w" />
</Frame>

Once you've defined the criteria that specifies which companies to find
lookalikes for, you can define some additional options for the trigger, such as
additional filters to apply or exclusions to enable and disable.

<Frame caption="The configuration panel for a lookalike companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=11e4dd11db05b12b7586fa07031668d5" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-configuration-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d476fac45cafa4a90b0276e2e3feb54b 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3a5c06738c881929fe9461124612b10b 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=56b0970bee1a35256829f2464863ef41 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=be8f6bd13d7d47c35c2844624973b733 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ceb8d2545cdc7e918eee00f519f9bf26 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f03b70c53fc8620d588f8a20adcc783e 2500w" />
</Frame>

This trigger is powered by [Ocean.io](https://www.ocean.io/). The integration is
fully managed by Unify and included in your plan, so no additional subscription
or setup is required.

### Record enters an Audience

This trigger runs a Play once on every company or person that "enters" an
audience. A record enters an audience when it meets the criteria of the audience
for the first time.

<Frame caption="The configuration panel for an audience trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=751a2369977272fb19ea23245f51627d" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/audience-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=696ff812de2dd2e958f18a432d4d9733 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f3667b137cee2ee8e20b8bbc0cc3bcba 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ea8bdf9df29a73328232ab8c96633e37 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e8a891b067cd78ced213640b6137ecd1 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=630398b748be76d9b13369040b87c8b7 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a99a0f1035dbc85e96dc181fbddcdb6e 2500w" />
</Frame>

When you select an audience trigger, you will be prompted to select an audience
from the list of audiences you have created. Audiences are reusable in Unify,
which means you can use the same audience in multiple Plays.

You also have the choice to run the Play on either companies that enter the
audience or people that enter the audience. If you select companies, the output
of this trigger will be a company record. Otherwise, the output will be a person
record.

### Record matches criteria

This trigger runs a Play once on every company or person that matches a set of
filters. This trigger behaves the same as the audience trigger, but it doesn't
require that you already have an audience created. Instead, you can define the
filters directly in the Play.

<Frame caption="The configuration panel for a record match trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=312374b3bbe33c6dc447a5c092c2848c" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/record-match-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=830f88561e84a75d244c865a6feb4695 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f4a6c485e1a6cbc9fc67c310660c3905 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6c29cd5cb1a665b5f907af66e4c7165c 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=af479b57aa8bb8b801887a7d1745a498 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=28ad0475f6a61dd6964ac38fee319983 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e3e27d7441ed8496629ec00e16a66f3d 2500w" />
</Frame>

When you select a criteria trigger, you will be prompted to add filters to
select the companies or people that the Play should run on. Just like building
audiences, you can add as many filters as you like and preview the records that
match the filters before saving the trigger.

As with audience triggers, you can choose to run the Play on either companies or
people. This will determine what type of record the trigger outputs.

### Website visitors

This trigger is a shortcut for running a Play on companies that visit your
website. Once selected, you can customize the matching criteria similar to the
record match trigger. This trigger always returns Companies.

<Frame caption="The configuration panel for a website visitors trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ed575ee55f0e23aa0b40f0323a29284e" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/website-visitors-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=74244388cb6e6e8349178f6781a52943 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=62819080d980f172d63aff91609849f5 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c5fe15a653f9235c6ec507b2a1dc8c94 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1bbd3ecd4840405ba738dea02c7801f8 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e07e0c78d6b1a11b4134396eedcf525a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a9205bc4897ed64a8b0ddf44932129bb 2500w" />
</Frame>

## Coming soon

There are lots of additional triggers in the works including webhooks, third-party
events, schedules, and more. If you're interested in one that isn't available
yet, [let us know](mailto:support@unifygtm.com)! We'll get you in the beta as
soon as it's ready.

## FAQ

<AccordionGroup>
  <Accordion title="Should I use an Audience trigger or a record match trigger?">
    Audience triggers and record match triggers can both be used to accomplish
    the same goal. The main difference is that audience triggers require you to
    create an audience ahead of time, while record match triggers allow you to
    define the filters directly in the Play.

    Audiences can be reused in multiple Plays, which is useful if you have a set
    of filters that you use frequently. Audiences can also be viewed, edited,
    and exported from the **Audiences** tab.

    Record match triggers are a great option for quickly iterating on a Play or
    if you don't want to create an audience for a one-off Play. You can always
    come back later, convert the filters into an audience, and then swap the
    trigger out for an audience trigger.
  </Accordion>

  <Accordion title="Is an Audience trigger the same as sending an Audience to a manual trigger?">
    Audiences are dynamic lists of companies and people that can change over
    time according to the filters you specify. For example, an audience might
    capture all companies that have visited your website in the last 30 days.

    When you send an audience to a manual trigger, you are sending the current
    list of companies or people that are in the audience at that moment. This
    is useful if you want to run a Play on a snapshot of the audience but not on
    a recurring basis.

    By contrast, an audience trigger will run a Play on every company or person
    that enters the audience in the future. This is useful if you want to run a
    Play on every company or person that meets the audience criteria now and in
    the future.
  </Accordion>
</AccordionGroup>


# Manual Sequence Steps
Source: https://docs.unifygtm.com/reference/sequences/manual-steps

Bring human-in-the-loop actions to your Unify Sequences.

export const PhoneCallIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-pink-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-pink-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2"></path>
    </svg>
  </>;

export const ManualEmailIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-blue-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"></path>
      <path d="M3 7l9 6l9 -6"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-blue-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v10a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-10z"></path>
      <path d="M3 7l9 6l9 -6"></path>
    </svg>
  </>;

export const LinkedInLogo = () => <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
    <path fill="#0A66C2" fillRule="evenodd" d="M2.667 24h18.666A2.667 2.667 0 0 0 24 21.333V2.667A2.667 2.667 0 0 0 21.333 0H2.667A2.667 2.667 0 0 0 0 2.667v18.666A2.667 2.667 0 0 0 2.667 24" clipRule="evenodd" />
    <path fill="#fff" fillRule="evenodd" d="M20.667 20.666h-3.562V14.6c0-1.663-.632-2.592-1.948-2.592-1.432 0-2.18.967-2.18 2.592v6.066H9.544V9.111h3.433v1.556s1.032-1.91 3.484-1.91c2.45 0 4.206 1.498 4.206 4.593zM5.45 7.598a2.124 2.124 0 0 1-2.117-2.133c0-1.177.948-2.132 2.117-2.132s2.116.955 2.116 2.132A2.124 2.124 0 0 1 5.45 7.598M3.677 20.666h3.58V9.111h-3.58z" clipRule="evenodd" />
  </svg>;

export const ActionItemIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-purple-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M9 11l3 3l8 -8"></path>
      <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-purple-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M9 11l3 3l8 -8"></path>
      <path d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"></path>
    </svg>
  </>;

Manual steps allow you to layer manual emails, phone calls, action items, and LinkedIn touches into your Unify Sequences.

## Adding Manual steps to Sequences

In the Sequence Builder, click the `+` button to add a step and choose from the following options:

<CardGroup cols={2}>
  <Card title="Manual email" icon={<ManualEmailIcon />} href="#manual-email-steps">
    Create an email that must be manually queued to send from Unify
  </Card>

  <Card title="Phone call" icon={<PhoneCallIcon />} href="#phone-call-steps">
    Create a task to call the prospect.
  </Card>

  <Card title="LinkedIn" icon={<LinkedInLogo />} href="#linkedin-steps">
    Create a task to view the prospect's LinkedIn profile, send them a
    connection request, or send them a LinkedIn message.
  </Card>

  <Card title="Action item" icon={<ActionItemIcon />} href="#action-item-steps">
    This will create a task to perform some generic action.
  </Card>
</CardGroup>

Each time a prospect runs through the Sequence, a corresponding task will be created in your Task Dashboard for each manual step.

<Frame caption="Adding a manual step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=bc20d14be82a7ab9cce68ec39d6a296a" data-og-width="3046" width="3046" data-og-height="1586" height="1586" data-path="images/reference/sequences/add-manual-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c91e98e3998fc07bc0dd96ca3c3e80f7 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f306f19922af4d4711b834d2fe000e1d 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f98534b4ce24ee605903443ae7625285 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=fa364223e514204d5d583ec7fab0de2e 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e935ac9eed7958354f1da20f6cfd196a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/add-manual-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=56f6e7bb6500f265b10d8f9dcb41f8a4 2500w" />
</Frame>

## Manual email steps

Just like automated emails, manual email steps can be composed using
[template variables](/reference/sequences/template-variables)
or [snippets](/reference/sequences/smart-snippets). You can set the priority of
the task that will be created for the step and who to assign the task to.

<Frame caption="Adding a manual email step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=89cb51506015c59d8903a921b10df145" data-og-width="3014" width="3014" data-og-height="1862" height="1862" data-path="images/reference/sequences/manual-email-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=672b3a2457da807c8d61f734172d4ba7 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=37f4b0b65f5a7c11202f5cdf02d804eb 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2b163a30c425732d0e9657e21ea61556 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f89177f359e779bc435688a7d1982e75 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=31b3280b9560fe729c023f876814490e 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/manual-email-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=33a52e9f8f9e10c4052e67bc48d08783 2500w" />
</Frame>

## Phone call steps

Phone call steps can include notes that will appear on the call task once created.
[Template variables](/reference/sequences/template-variables) and
[snippets](/reference/sequences/smart-snippets) can be used to customize the notes.

<Frame caption="Adding a phone call step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a15d26ded98ac73c08678c5e9f863afb" data-og-width="2996" width="2996" data-og-height="1084" height="1084" data-path="images/reference/sequences/phone-call-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=4f06cabda9b5b8a2b779e2dfa518da85 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=eb18748781f262406cadf33e953c9d45 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c847993e95d3675b0f12975dd8d39138 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7bd5de861a77fd159b119c7dd86dde4f 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=99a6f5d537184c1708a65cbb87cbc369 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/phone-call-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=36ece6039276d6cb77e52eb7aa4c0936 2500w" />
</Frame>

## LinkedIn steps

LinkedIn steps can include notes that will appear on the task once created. These notes
can be copied and pasted into the connection request or DM that you send to the prospect on LinkedIn.
[Template variables](/reference/sequences/template-variables) and
[snippets](/reference/sequences/smart-snippets) can be used to customize the notes.

<Frame caption="Adding a LinkedIn step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=58b347241ed12ce29805610776d3d192" data-og-width="3034" width="3034" data-og-height="816" height="816" data-path="images/reference/sequences/linkedin-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3160ef2c1c13e0c650538a8779ba31c4 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ddd38f6ed0187f49d511f3c3173054ae 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d3d2586cf44b6cd279d38d8d51d83028 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c4b3e880ab29425b56bf9b16c3046a01 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=21c9009b0b60ab2c0076a553d1ba25af 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/linkedin-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=12a5470c36a8987837296601c484f540 2500w" />
</Frame>

## Action item steps

Action item steps can include notes that will appear on the task once created. These notes
can be used to generate instructions for the user to complete the task or simply contain information
about the prospect. [Template variables](/reference/sequences/template-variables) and
[snippets](/reference/sequences/smart-snippets) can be used to customize the notes.

<Frame caption="Adding an action item step in a Sequence.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=be13af243166e535c23dff387e13d777" data-og-width="3004" width="3004" data-og-height="1048" height="1048" data-path="images/reference/sequences/action-item-step.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=69fcf93feddb2d235b4ccbb03e0e900f 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=26aa7d8581a8de6a56d943514d9ee86f 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3cbcc9cc0ff876a78b26dee956a73689 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=7cfce655f1b2884a1f33cd0d7e59e32f 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f0370cc7512fbec38a8d65389d462d97 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/action-item-step.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=99cfd00d658cb25cf46183ba7a3a70fa 2500w" />
</Frame>


# Unify Sequences
Source: https://docs.unifygtm.com/reference/sequences/overview

Learn what Unify sequences are and how to use them.

## What are Sequences?

A sequence is a series of automated outreach steps that let you scale your
outbound and measure its effectiveness. Sequences are purpose-built for modern
outbound sales with native AI capabilities and deep integration with the Unify
platform.

Once you've created a sequence, you can enroll people in it to automate your
outreach. Sequence enrollments can be performed automatically from Plays, but
you can also enroll people manually. Enrollments can then be monitored from the
sequence details page to track their progress.

<Frame caption="Manage and monitor sequence enrollments within Unify.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=3d4e3b62357fb53ec32e0342a6869106" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/sequences/sequence-enrollments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=89d3fdda9ac0ea5c73e2bf37d815f663 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=32e6e5185358ef90b97121df34616c16 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=10558a9250d694db5cb3dfe6dbc1bc9f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=576fad4f599a54e285df151c9bf8b39c 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=617f2d17f49423cb2385c0bf2ae9c16d 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/sequence-enrollments.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=b31bd536c47e6516e63b33b842416c07 2500w" />
</Frame>

Unify sequences come equipped with comprehensive analytics that let you measure
their effectiveness and compare performance across different sequences with
ease. Unify also provides an unparalleled suite of features for maintaining high
deliverability and ensuring your domain reputation is being handled with care.


# Sequence Replies
Source: https://docs.unifygtm.com/reference/sequences/replies

View and manage replies from prospects in your Sequences.

export const WillingToMeetIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" />
      <path d="M15 7a2 2 0 0 1 2 2" />
      <path d="M15 3a6 6 0 0 1 6 6" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M5 4h4l2 5l-2.5 1.5a11 11 0 0 0 5 5l1.5 -2.5l5 2v4a2 2 0 0 1 -2 2a16 16 0 0 1 -15 -15a2 2 0 0 1 2 -2" />
      <path d="M15 7a2 2 0 0 1 2 2" />
      <path d="M15 3a6 6 0 0 1 6 6" />
    </svg>
  </span>;

export const UpdatedContactInfoIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-teal-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M20 6v12a2 2 0 0 1 -2 2h-10a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h10a2 2 0 0 1 2 2z" />
      <path d="M10 16h6" />
      <path d="M13 11m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
      <path d="M4 8h3" />
      <path d="M4 12h3" />
      <path d="M4 16h3" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-teal-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M20 6v12a2 2 0 0 1 -2 2h-10a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h10a2 2 0 0 1 2 2z" />
      <path d="M10 16h6" />
      <path d="M13 11m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
      <path d="M4 8h3" />
      <path d="M4 12h3" />
      <path d="M4 16h3" />
    </svg>
  </span>;

export const SoftBounceIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M10 18h4" />
    <path d="M3 8a9 9 0 0 1 9 9v1l1.428 -4.285a12 12 0 0 1 6.018 -6.938l.554 -.277" />
    <path d="M15 6h5v5" />
  </svg>;

export const ReferralIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-teal-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M11 12h10" />
      <path d="M18 9l3 3l-3 3" />
      <path d="M7 12a2 2 0 1 1 -4 0a2 2 0 0 1 4 0z" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-teal-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M11 12h10" />
      <path d="M18 9l3 3l-3 3" />
      <path d="M7 12a2 2 0 1 1 -4 0a2 2 0 0 1 4 0z" />
    </svg>
  </span>;

export const PositiveToneIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3" />
    </svg>
  </span>;

export const OutOfOfficeIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M17.553 16.75a7.5 7.5 0 0 0 -10.606 0" />
    <path d="M18 3.804a6 6 0 0 0 -8.196 2.196l10.392 6a6 6 0 0 0 -2.196 -8.196z" />
    <path d="M16.732 10c1.658 -2.87 2.225 -5.644 1.268 -6.196c-.957 -.552 -3.075 1.326 -4.732 4.196" />
    <path d="M15 9l-3 5.196" />
    <path d="M3 19.25a2.4 2.4 0 0 1 1 -.25a2.4 2.4 0 0 1 2 1a2.4 2.4 0 0 0 2 1a2.4 2.4 0 0 0 2 -1a2.4 2.4 0 0 1 2 -1a2.4 2.4 0 0 1 2 1a2.4 2.4 0 0 0 2 1a2.4 2.4 0 0 0 2 -1a2.4 2.4 0 0 1 2 -1a2.4 2.4 0 0 1 1 .25" />
  </svg>;

export const OptOutIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-red-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 12l6 0" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-red-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 12l6 0" />
    </svg>
  </span>;

export const NsfwIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-red-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M10 10l4 4m0 -4l-4 4" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-red-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M10 10l4 4m0 -4l-4 4" />
    </svg>
  </span>;

export const NeutralToneIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-teal-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 10l.01 0" />
      <path d="M15 10l.01 0" />
      <path d="M9 15l6 0" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-teal-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
      <path d="M9 10l.01 0" />
      <path d="M15 10l.01 0" />
      <path d="M9 15l6 0" />
    </svg>
  </span>;

export const NegativeToneIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-red-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 13v-8a1 1 0 0 0 -1 -1h-2a1 1 0 0 0 -1 1v7a1 1 0 0 0 1 1h3a4 4 0 0 1 4 4v1a2 2 0 0 0 4 0v-5h3a2 2 0 0 0 2 -2l-1 -5a2 3 0 0 0 -2 -2h-7a3 3 0 0 0 -3 3" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-red-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M7 13v-8a1 1 0 0 0 -1 -1h-2a1 1 0 0 0 -1 1v7a1 1 0 0 0 1 1h3a4 4 0 0 1 4 4v1a2 2 0 0 0 4 0v-5h3a2 2 0 0 0 2 -2l-1 -5a2 3 0 0 0 -2 -2h-7a3 3 0 0 0 -3 3" />
    </svg>
  </span>;

export const NeedsMoreInfoIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-success-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M8 9h8" />
      <path d="M8 13h6" />
      <path d="M14 18h-1l-5 3v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v4.5" />
      <path d="M19 22v.01" />
      <path d="M19 19a2.003 2.003 0 0 0 .914 -3.782a1.98 1.98 0 0 0 -2.414 .483" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-success-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M8 9h8" />
      <path d="M8 13h6" />
      <path d="M14 18h-1l-5 3v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v4.5" />
      <path d="M19 22v.01" />
      <path d="M19 19a2.003 2.003 0 0 0 .914 -3.782a1.98 1.98 0 0 0 -2.414 .483" />
    </svg>
  </span>;

export const LeftJobIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-teal-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M4 19v2h16v-14l-8 -4l-8 4v2" />
      <path d="M13 14h-9" />
      <path d="M7 11l-3 3l3 3" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-teal-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M4 19v2h16v-14l-8 -4l-8 4v2" />
      <path d="M13 14h-9" />
      <path d="M7 11l-3 3l3 3" />
    </svg>
  </span>;

export const HasSolutionIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-purple-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M3 21h4l13 -13a1.5 1.5 0 0 0 -4 -4l-13 13v4" />
      <path d="M14.5 5.5l4 4" />
      <path d="M12 8l-5 -5l-4 4l5 5" />
      <path d="M7 8l-1.5 1.5" />
      <path d="M16 12l5 5l-4 4l-5 -5" />
      <path d="M16 17l-1.5 1.5" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-purple-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M3 21h4l13 -13a1.5 1.5 0 0 0 -4 -4l-13 13v4" />
      <path d="M14.5 5.5l4 4" />
      <path d="M12 8l-5 -5l-4 4l5 5" />
      <path d="M7 8l-1.5 1.5" />
      <path d="M16 12l5 5l-4 4l-5 -5" />
      <path d="M16 17l-1.5 1.5" />
    </svg>
  </span>;

export const HardBounceIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M10 18h4" />
    <path d="M3 8a9 9 0 0 1 9 9v1l1.428 -4.285a12 12 0 0 1 6.018 -6.938l.554 -.277" />
    <path d="M15 6h5v5" />
  </svg>;

export const BadTimingIcon = ({size = 24, inline}) => <span style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <svg class="block dark:hidden" stroke="var(--icon-purple-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M20.997 12.25a9 9 0 1 0 -8.718 8.745" />
      <path d="M19 19m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0" />
      <path d="M17 21l4 -4" />
      <path d="M12 7v5l2 2" />
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-purple-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path stroke="none" d="M0 0h24v24H0z" fill="none" />
      <path d="M20.997 12.25a9 9 0 1 0 -8.718 8.745" />
      <path d="M19 19m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0" />
      <path d="M17 21l4 -4" />
      <path d="M12 7v5l2 2" />
    </svg>
  </span>;

export const AutomatedIcon = ({size = 24, inline}) => <svg className="stroke-gray-600 dark:stroke-gray-400" fill="none" strokeWidth="2" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg" style={{
  ...inline && ({
    display: 'inline-block'
  }),
  verticalAlign: 'text-bottom',
  marginRight: '4px'
}}>
    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
    <path d="M13.256 20.473c-.855 .907 -2.583 .643 -2.931 -.79a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.07 .26 1.488 1.29 1.254 2.15" />
    <path d="M19 16l-2 3h4l-2 3" />
    <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />
  </svg>;

## Overview

When prospects reply to your Sequence emails, Unify automatically captures and classifies those replies. All replies are accessible directly within the Unify app.

<Frame caption="Replies in a sequence">
  <img src="https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=9da490ff48d50bc410c193e519d2589c" width="500" data-og-width="1648" data-og-height="2048" data-path="images/reference/sequences/sequence-replies.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=280&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=a64181e9597e9d7c870036b5ee37912e 280w, https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=560&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=9b95511ce36482fae28687fa76409cc8 560w, https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=840&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=fab9a6b4a91b0830dd366fc620d5d8fc 840w, https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=1100&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=229953c0f0d228f10962de3ecbd04013 1100w, https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=1650&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=54cf4ab2607880ab1fbca611ff08a5da 1650w, https://mintcdn.com/unify-19/992x7Ng1_thQsMnR/images/reference/sequences/sequence-replies.png?w=2500&fit=max&auto=format&n=992x7Ng1_thQsMnR&q=85&s=75d6341232c2f8d2296742fe0ade92c4 2500w" />
</Frame>

## Out-of-Thread Replies

In addition to direct replies to Sequence emails, Unify also captures **out-of-thread replies** from your prospects.

An out-of-thread reply is an email from a sequence enrollee that doesn't directly reply to a sequence email. This includes new email threads initiated by the prospect or separate conversations sent to your mailbox while they're engaged with your sequence.

## Reply Classifications

Unify automatically classifies replies using AI to help you prioritize your responses. Each reply receives one or more classification tags that indicate the prospect's intent or sentiment.

* <PositiveToneIcon size={20} inline />**Positive** — The email response shows enthusiasm, agreement, or active engagement with the sender's offer, indicating a genuine interest in moving forward. This is not an automated reply.
* <WillingToMeetIcon size={20} inline />**Willing to meet** — The recipient's email indicates their openness to schedule a meeting, specifically about the offer mentioned in the initial outreach.
* <NeedsMoreInfoIcon size={20} inline />**Needs more info** — The recipient requests additional details or expresses uncertainty about the offer. Providing clarification may result in a positive outcome.
* <BadTimingIcon size={20} inline />**Bad Timing** — The email conveys interest but explains that current budget constraints or timing prevent immediate action. Future actions may be possible if a timeframe is mentioned.
* <HasSolutionIcon size={20} inline />**Has solution** — The recipient mentions that they are already using a different product or service to meet their needs.
* <NeutralToneIcon size={20} inline />**Neutral** — The email is objective, factual, respectful, unemotional, and polite yet concise.
* <LeftJobIcon size={20} inline />**Left Job** — The email indicates the sender is no longer employed at their previous role or company.
* <UpdatedContactInfoIcon size={20} inline />**Updated contact info** — The email notifies the sender of a new or updated email address for further communication.
* <ReferralIcon size={20} inline />**Referral** — The email includes a suggestion to contact another person, and provides the referral's contact information.
* <NegativeToneIcon size={20} inline />**Negative** — The email contains hostile, emotional, or adversarial language, such as anger or frustration.
* <NsfwIcon size={20} inline />**NSFW** — The email includes content that is offensive or inappropriate.
* <OptOutIcon size={20} inline />**Opt out** — The recipient explicitly requests to unsubscribe, threatens to block communication, or mentions reporting the sender.
* <OutOfOfficeIcon size={20} inline />**OOO** — The recipient's email indicates they are out of office or currently unable to provide a complete response.
* <SoftBounceIcon size={20} inline />**Soft Bounce** — The email indicates a temporary delivery failure, meaning the message might eventually be delivered.
* <HardBounceIcon size={20} inline />**Hard Bounce** — The email indicates a permanent delivery failure, suggesting the recipient's email address is invalid or no longer in use.
* <AutomatedIcon size={20} inline />**Automated** — The email appears to have been generated by an automated system, rather than sent by a person.

<Note>
  Reply classifications can be configured to trigger [notifications](/reference/notifications/preferences) so you're alerted when important replies come in.
</Note>


# Creating a Custom Send Schedule
Source: https://docs.unifygtm.com/reference/sequences/send-schedules/creating-send-schedules

Learn how to configure Custom Send Schedules for Sequences.

## Navigation

You can access the Custom Send Schedules page by navigating to:
**Settings → Organization → Sequences → Send Schedules**.

Once you are on this page, click the **+ New Schedule** button to create a new Custom Send Schedule.

<Frame caption="Navigating to Custom Send Schedules">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b86217923cbd34020b7b7528e63032d5" data-og-width="1856" width="1856" data-og-height="1708" height="1708" data-path="images/reference/sequences/send-schedules/send-schedules-list-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=77dfe772a2e0ca24369197f503f23427 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=fc58b3cee33815d2fce8225e629af04c 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=dd49fbf59ba309ed75551cb56908d433 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=2a796afd5dc0969a728b8d13eb50d75d 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=72ab3dda4e123f880bca447b5fe1d141 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list-2.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=1329f0f7dfd180abe2b4ccb77f6d1522 2500w" />
</Frame>

## Configuring a new Custom Send Schedule

After clicking the **+ New Schedule** button, a configuration drawer will open, allowing you to define the parameters of your new Custom Send Schedule.

### General

Under the **General** section, you can configure the basic information for your Custom Send Schedule.

* **Name** — Provide a clear, descriptive name for your Custom Send Schedule (e.g., *North America Weekdays* or *APAC Morning Outreach*).
* **Time Zone** — Select the time zone in which the schedule will operate. This ensures that all send windows and skip dates align to the correct local time. (e.g., America/Los Angeles, Europe/London, Asia/Singapore)

<Frame caption="General settings">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=965f902c9b61894ff04c70408d73c73c" data-og-width="1614" width="1614" data-og-height="532" height="532" data-path="images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b33293b9e764d5c2102210e900960ba7 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=02d61e6ad1ce9b63041de4590bccabc5 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=aa13eb48f8b855bbb10814a8d458fa66 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=74b2859ae4f2b6b4b3afd380d839816d 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=dc870c09109b5a49449d6c5d0cfd82c7 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-general.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=a3528bce8a27cd11b03608ed75f527bd 2500w" />
</Frame>

> 💡 **Tip:** If your team operates globally, create separate Custom Send Schedules for each region to ensure messages are sent during local business hours.

***

### Windows

The **Windows** section defines when Unify is allowed to send automated messages through Sequences during the week.

For each day of the week, you can:

* Enable or disable sending (for example, enable Monday–Friday and disable Saturday–Sunday).
* Specify one or more **time windows** when messages can be sent (e.g., 9 AM–12 PM, 1 PM–5 PM).

<Frame caption="Configuring send windows">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=3b9c82cbc83301da17b65e0cb23dce26" data-og-width="1608" width="1608" data-og-height="1270" height="1270" data-path="images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=6d8727242c6a18e205984dacef67b512 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=c6459400ba0b0e2a31505686eec32490 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=7a7dce98c59b9e07354e8018d4aa214d 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=e36c20c54d124c65ee28de0f17ef5b1c 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=d4a88460e79861819327443676a074d1 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-windows.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=cf5a05c4fe66a48d39f4e7da4de50a30 2500w" />
</Frame>

**Example:**
If you want outreach to happen only during typical working hours, you might configure:

* Monday–Friday: 9:00 AM–4:30 PM
* Saturday & Sunday: Disabled

> **Note:** Messages queued outside of active windows will automatically be held until the next available send window.

***

### Skip Dates

Skip Dates allow you to automatically **pause sending on holidays or custom dates**.
This helps maintain deliverability and professionalism by avoiding sends on non-working days.

There are two ways to configure Skip Dates:

1. **U.S. Holidays** — Toggle this option to automatically skip sending on major U.S. federal holidays (e.g., New Year’s Day, Independence Day, Thanksgiving).
2. **Custom Dates** — Add specific dates or recurring dates (such as company offsites, local holidays, or yearly breaks).

You can specify whether custom dates repeat **annually** or occur **once**.

<Frame caption="Configuring skip dates">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=84787ccecedbb9157822e8d9277aa4be" data-og-width="1588" width="1588" data-og-height="972" height="972" data-path="images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=72d6589cbb931f2b50447829d95b3972 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=4efeeda9e5e5af416e3a9d5528b9fea0 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=8ec1c2c795d921e49a4fe93f604cd7c7 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=6cdd9b2adfe0c4ea93c028cd7adc1242 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=6494775bd255a42c65c2d0b44e03f1c9 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-create-drawer-skip-dates.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=ac33729027f0dce30373ea5e5a9ecc78 2500w" />
</Frame>

> 💡 **Tip:** Use Skip Dates to prevent outreach from occurring during out-of-office periods or industry-wide holidays that may impact engagement.

***

### Saving the Custom Send Schedule

Once you’ve configured the General settings, Windows, and Skip Dates, click **Create** to save your Custom Send Schedule.
It will now appear in the **Custom Send Schedules** list view, where you can edit, duplicate, or delete it at any time.

Your new Custom Send Schedule is now ready to use!


# Custom Send Schedules Overview
Source: https://docs.unifygtm.com/reference/sequences/send-schedules/overview

Learn what Custom Send Schedules are and how they control automated email sending within Sequences in Unify.

Custom Send Schedules help teams coordinate outreach across time zones, avoid weekends or holidays, and ensure emails are delivered during ideal business hours for recipients.

## What are Custom Send Schedules?

Custom Send Schedules define the specific days and time windows when Unify is allowed to send automated email messages through Sequences.

Each schedule can be customized with:

* **Time zones** — Align delivery windows with your target audience or team region (e.g., America/Los Angeles, Europe/London, Asia/Singapore).

* **Active days** — Choose which weekdays are enabled for sending (e.g., Monday–Friday).

* **Time windows** — Define the daily sending hours to control when messages are delivered within each active day (e.g., 9 AM–2 PM, 3 PM–6 PM).

* **Skip dates** — Exclude U.S. holidays or add custom recurring dates to pause sending automatically.

<Frame caption="Custom Send Schedules">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=6665049c018ae1186c332df57362905f" data-og-width="713" width="713" data-og-height="817" height="817" data-path="images/reference/sequences/send-schedules/send-schedules-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=aa76a07668f49233424e3fba5436585f 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=82ec1e7854d767f6edc317e9816b78c3 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=53887f3eb645a85911596c4424c76bf3 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=0f308770988ad61558492ffa4e3671e5 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=e00992982d38a65997108336dda50570 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/send-schedules-list.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=9f9a2a1c590e2dae4b382c36ca42908a 2500w" />
</Frame>


# Using a Custom Send Schedule
Source: https://docs.unifygtm.com/reference/sequences/send-schedules/using-send-schedules

Learn how to view and apply Custom Send Schedules for Sequences.

Custom Send Schedules define when automated emails in a Sequence are allowed to send. Once you’ve configured your Custom Send Schedule, you can assign them to individual Sequences.

***

## Accessing Sequence Settings

To view or edit the Custom Send Schedule assigned to a Sequence:

1. Open any Sequence from your **Sequences** list.
2. Click the **⚙️ cog icon** in the top-right corner to open **Sequence Settings**.
3. In the settings drawer, you’ll see a section labeled **Send schedule**, displaying the currently linked schedule and its details.

<Frame caption="Viewing the Custom Send Schedule assigned to a Sequence">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=0c30a36eb5743a13db3f5ec7b4c4c534" data-og-width="3244" width="3244" data-og-height="1596" height="1596" data-path="images/reference/sequences/send-schedules/sequences-settings-drawer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=9e10928567fffe479c95aefd55ce7f08 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=741953681084074239e9c61b738b476b 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=705aec18869b5660e24f772109b1a94c 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=223dead02da49e3a9b29e21100d2a4ac 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=58cbb5d6acdbe55c238c57e5c2ca5185 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-drawer.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b29217addbc60ddcbb89e0474649d6d7 2500w" />
</Frame>

***

## Selecting a Custom Send Schedule

To change which Custom Send Schedule a Sequence uses:

1. Click **Edit** in the top-right corner of the Sequence Settings drawer.
2. Open the **Send schedule** dropdown.
3. Choose the desired schedule from the list. You’ll see details including:
   * Schedule name
   * Timezone
   * Days enabled for sending
   * Sending windows per day
   * Skip dates

<Frame caption="Selecting a Custom Send Schedule for a Sequence">
  <img src="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=c61f6d584db97b89080526066fc95bdb" data-og-width="2284" width="2284" data-og-height="1612" height="1612" data-path="images/reference/sequences/send-schedules/sequences-settings-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=280&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=d1e5dd6ef49283994e156f0484190436 280w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=560&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b82b702f769a52cbe3765d535a2e63e2 560w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=840&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=9e56b629e3b17ec3ab1ef2ccbc914827 840w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=1100&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=b57805a426feb48ab58e57f926b7f244 1100w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=1650&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=979a284875616b8c2e3099641ec57fae 1650w, https://mintcdn.com/unify-19/o9cPk0MfoGZNAFAu/images/reference/sequences/send-schedules/sequences-settings-edit.png?w=2500&fit=max&auto=format&n=o9cPk0MfoGZNAFAu&q=85&s=5575ea4dc41066a8ad2e9e7876997e2f 2500w" />
</Frame>

After you’ve selected a schedule, click **Save** to apply it.

***

## Important Notes

<Note>
  When linking a new Custom Send Schedule to an active Sequence, **Unify will
  immediately reschedule all pending emails for that Sequence** according to the
  new Custom Send Schedule configurations.
</Note>

> 💡 **Tip:** If you’re running outreach across multiple regions, use different Custom Send Schedules for each region’s Sequences to optimize timing and engagement.

***


# Smart Snippets
Source: https://docs.unifygtm.com/reference/sequences/smart-snippets

Personalize your outreach with AI-powered email copy generation.

## Overview

Smart snippets allow you to personalize messages with AI-generated copy that's
unique to each recipient. You can use smart snippets to enhance your messaging,
improve deliverability, and increase engagement.

Smart snippets are concise, self-contained pieces of text that serve a clear
communicative purpose. Each snippet should be laser-focused on the parts of your
outbound message that change the most to fit each recipient differently.

## Creating a smart snippet

Navigate to the [Snippets](https://app.unifygtm.com/dashboard/snippets) tab in
the sidebar, select **New Snippet** in the top right corner, and choose
**Smart Snippet**. You will see the smart snippet creation screen.

<Frame caption="This is where you enter the prompt for your smart snippet.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=95c886816ee1ef78ea46bc17216f5ae4" data-og-width="2864" width="2864" data-og-height="2048" height="2048" data-path="images/reference/sequences/smart-snippet-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a3a6d195abb412416a3bc1388f3fc045 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=68faebcf57e2e15ee576f4d638c839c0 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9de1184c52edb5b38cf00a53b89d2e52 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=2977cac1cb67953f5edd0ed667ecf924 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=258075fcf7ec5f96946d75f417cf73cb 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/sequences/smart-snippet-create.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=baa72f675a2928b50bdd4b0277615972 2500w" />
</Frame>

To define a smart snippet, you provide a prompt that describes the content you
want to generate. The prompt should include template variables for any data you
want the model to use when writing the snippet. You can click on the quick
prompts to see example prompts for inspiration.

After you've entered your prompt, click **Generate examples** to see what the
smart snippet will generate for a sample of real people from your data. You can
edit the prompt and regenerate examples to iteratively refine your snippet.

<Frame caption="Example snippet generations appear on the left.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=82661918e2a2402dba1597add9a60c13" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/sequences/smart-snippet-previews.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=1a639f51d52fa02accdd149ccd267357 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=33e8219401a70e5926bc450811baaec6 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f7694a795e29b2784f352b6e16ae89ad 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a1562993bd6d44a3cff43a4488852ee0 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=58a2b3b5cc317895828edceef0889c77 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/smart-snippet-previews.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=b46c2396a9101681f2cd0f0f7d400369 2500w" />
</Frame>

Just like regular snippets, you should also define a fallback value for the case
where some of the template variables in the prompt are missing data. This will
prevent enrollments from being blocked by the missing data.

When you're satisfied with your prompt, click **Create** to save it. You will
now be able to use the snippet in your sequences.

## Recommendations

Here are a few practices we recommend to get the most out of smart snippets:

1. Always include at least one template variable for the model to use to
   personalize the snippet. For example, include some details about the sender,
   the recipient, or their company. This helps the model write more precise and
   personalized copy.
2. Include 2-3 example outputs to guide the model. Examples help the model
   understand the tone and structure you're trying to achieve. The model will
   often pick up on vocabulary and stylistic choices from your examples.
3. Start small. Pick a specific part of the email—such as the salutation or
   hook—and focus on personalizing that part. Smart snippets are most effective
   when they're used to personalize small sections of your email. Remember that
   you can use as many snippets in an email as you want!


# Template Variables
Source: https://docs.unifygtm.com/reference/sequences/template-variables

Use template variables to personalize your emails.

## Overview

Template variables are key to personalizing messages sent through Unify. You can
use template variables to insert dynamic values into your emails, such as a
person's name, company, or job title.

## Inserting variables

You can insert template variables into emails you write when creating sequences in Unify. To open the template variable dropdown, click on the template variable button in the sequence builder.

<Frame><img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=bac2c0e11a9a8e13f353fe75d1824a7e" alt="template-var-1" data-og-width="960" width="960" data-og-height="719" height="719" data-path="images/template-var-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=b0c057a483326216164f31dbff43e04f 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=990979614ea3b237a14df2be6de35502 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=7ff229d96eeb8da3a66befac1416f7ef 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ee6181db63dee7f70c0813cfca25184d 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=7fb572bf7c4bdd3824a8e176dccfaba5 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/template-var-1.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=6e69df735e04adfb1c752756c06ba98c 2500w" /></Frame>

You can also press **`{`** on your keyboard to open the template variable dropdown. Once open, you can select a variable and insert it into your email.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3d8c4031b5bf67fb9b37c7f22e1b3863" alt="template-var-2" data-og-width="960" width="960" data-og-height="720" height="720" data-path="images/template-var-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9c36198a3c828914997616e3bfacfd6a 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=51544e3c819655b301578115a989a297 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=adcd570cabd34d8eac23bee52197a632 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a8d77013e6df25af2d383be327f01c3c 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=05939758a7b69700024d630d79de04ab 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-2.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=60e86f12d0d15d21e878d6e95b005942 2500w" /></Frame>

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=95f1cebb93806f8705e73f574fccda10" alt="template-var-3" data-og-width="960" width="960" data-og-height="721" height="721" data-path="images/template-var-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5a187e233c373be54819847284f8acca 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=480a7343fa246378b98698b6006aa3a2 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2ca266ec16f278e4f030090de5d2068d 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e1c8f7871dc366d0d80f3b55ef8b5f28 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7a997c7f6f518886f2731218f7842b25 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-3.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cfe8c015dec3fed72bbbda6e7bb764d8 2500w" /></Frame>

When a person is enrolled in this sequence, this value will be filled in dynamically.

## Handling missing data

### Enrollment blocking

Sometimes, Unify won’t have data to populate variables used in a sequence email. In these cases, Unify will never send an email with a placeholder or missing value. Instead, Unify will *block* the sequence enrollment.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b5db662068de02ec8dce6bbba21d1475" alt="template-var-4" data-og-width="1420" width="1420" data-og-height="1010" height="1010" data-path="images/template-var-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a62fb385ff4d529ceef771c30bd24c21 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f0ed2fdb946083f031d709095e961936 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0485eeea28cafaf21503e2a7cc3fa964 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7506630cf62501d7bb510f253795f737 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1923d23c72e4559d02fe86eaed6aa7cf 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-4.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c55832e3ad25bae8a3cbb18836d5fcef 2500w" /></Frame>

Blocked enrollments can be seen on the sequence details page. You can click on a blocked enrollment to edit the message and manually fill in any missing values.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=056909dd0c5dc7653de2d3d92c1b32ec" alt="template-var-5" data-og-width="1420" width="1420" data-og-height="1010" height="1010" data-path="images/template-var-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2813396aa42590e12f12ab2097d10731 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5475ca6ecd95bcef25b0c708d3c52401 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c4524779caa7cf0e731cc59d470b6263 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=451cf3409d53324425f77ed90e800d98 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=66f6b4c3d70d1ce5a90ebbc5664fdc10 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-5.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2d6ecb4d736994359594f068525e640d 2500w" /></Frame>

The template variables with missing values will appear highlighted in orange. Once you’ve replaced the missing values, click **Save** and the blocked status will disappear.

<Frame><img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e85da34feb1caf0ee17b162b597934d7" alt="template-var-6" data-og-width="1420" width="1420" data-og-height="1010" height="1010" data-path="images/template-var-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a04c57b2b03d9ae9a2817b71cfba3752 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=fd03f41a0c69add20a6121362615035e 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d741375a98928586c915a4a9ea7514d9 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=815a2a29a616359a030f3d7251857ee0 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=250cd2cca1f37e52fa54d80870703659 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/template-var-6.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c9ab78515606c4f9911d9e332721e74d 2500w" /></Frame>

The step will then be rescheduled and sent automatically as part of the sequence.

### Snippets

To avoid having to manually unblock enrollments that are missing a value, it's
highly recommended that you take advantage of *snippets*.

Snippets are reusable blocks of copy that can be inserted into messages the same
as template variables. However, snippets also allow you to define fallback text
which is used if any template variables are missing values.

<Frame caption="A basic snippet with a single template variable.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=5d7c66e3f5407991b2f16106f6907343" data-og-width="2881" width="2881" data-og-height="2048" height="2048" data-path="images/reference/sequences/snippets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c5f5b69bc4593ae5da52a7a46e62c4e9 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=b7d1477eb7fc289fa8322ebf961ddea3 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=907af6dd79b67fe207010c15a0dbdc31 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=518dc1dc227ca3853ad0bad0467d33d4 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=95fdda1a77af468d32d1eee8ad80bb9e 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=6f13df0dd54f702cbd11727cefddfeb6 2500w" />
</Frame>

You can access snippets by navigating to the [Snippets](https://app.unifygtm.com/dashboard/snippets)
tab in the sidebar. When defining a snippet, you can use template variables or
even other snippets in the copy. Underneath the snippet text area, there is a
second text area where you can define a fallback.

<Frame caption="A snippet with fallback text in case the variable value is missing.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=5df038763d31df655c128638a25402ea" data-og-width="2881" width="2881" data-og-height="2048" height="2048" data-path="images/reference/sequences/snippets-fallback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=86474464c9a765a99e7a354202d67223 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=51d349e22ab75a519d76520df9b7e041 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=71a4ccc354418a768618e762d1a09b5e 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3e93b2a62842e8adfef71dff9ab5a2d0 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=b711460ec606b52c7a1e0845a6730268 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/sequences/snippets-fallback.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=6a991e9c2139f7c3fc34277a80599a08 2500w" />
</Frame>

The fallback will be used in the event that any of the variables used in the
copy are missing. If you use snippets within snippets (which is called
*snippet-ception*), the fallback for the nested snippet will be used in the
top-level snippet.


# Champion Tracking
Source: https://docs.unifygtm.com/reference/signals/champions

Automatically track your champions and take action on them.

## What is a Champion?

Your companies' champions are customers who have used and advocated for the adoption of your product or services.

## What is Champion Tracking?

With Champion Tracking, you can define filters to select your company's champions and automatically follow when they change jobs.
A champion who has changed jobs is indicative of an opportunity with an outsized probability of success.

When enabled, the job statuses of each of your champions will be checked once per month
and their new contact information will be found when they change jobs. This information is extremely
valuable for breaking into new accounts and performing retargeting campaigns.

Unify will automatically create an exclusion for the old contact records of your champions who have changed jobs.
This means that the old records won't appear in audiences nor be sequenced.

You will be charged one credit per champion tracked per month regardless of whether a job change was detected.
You can view the `Tracking` tab in the Champion Tracking Settings page to see who is being tracked.

### Set Up Champion Tracking

Define who your champions are.

#### Enabling

1. In the Unify app, go to [Settings -> Track -> Champions](https://app.unifygtm.com/dashboard/settings/champion-tracking).

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=cf025ee1e994c81f6bfd4b9d2c6433de" alt="" data-og-width="3216" width="3216" data-og-height="2024" height="2024" data-path="images/enable-champ-tracking-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=8a6e673f5889bb7bc928c7361051acd0 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d449ee88a9473b969eddb1248266cdee 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7e75802fe61ef767a533819c155506e6 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c049ccecd5fe16a39bdfbf8072b9e3c0 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7d6275b600c2b4fa1b358e56cbdcd9f5 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-1.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=68c8b39d03069e53fe43a4a89e3ef5d9 2500w" /></Frame>

2. Click the toggle at the top of the page to open the Champion Tracking Settings modal.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4f3831f9ba8e62b4254232733c461eda" alt="" data-og-width="2968" width="2968" data-og-height="388" height="388" data-path="images/enable-champ-tracking-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=373e8332bf0f50a12fbafb2a8b2e723e 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1789ad7e1cf4a4a26fc99575704dfbd8 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=05e7b40484d1e5a34ed14248182601a1 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c0af60eceb375d9866b0183247765c8e 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=42466f807a24d2b97e16eba708cf4325 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-2.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=bf21cb534680dc720040e26bba135b99 2500w" /></Frame>

3. Define filters to identify your champions to track. For example, users commonly filter down to companies with Closed Won opportunities.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7c1ab0df2a0f680ee8ef12a03074dbb2" alt="" data-og-width="3245" width="3245" data-og-height="2003" height="2003" data-path="images/enable-champ-tracking-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3c1ee3b430dfb8de21e33e892255032c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3c27f86e62c3ff5d663567db3a8494b0 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=669e2eb94d18dc41b9f1ca6d19e8ce5c 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7540e51c45dfac34464f65e0ec128c7e 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=aef36ec49e267977024c6b77bb464239 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/enable-champ-tracking-3.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7ac87901c53b773dfb1e4a3a85e14c3a 2500w" /></Frame>

4. Click `Enable Champion Tracking`.  Unify will track your champions once per month starting from the moment you enable Champion Tracking.

#### Disabling

1. In the Unify app, go to [Settings -> Track -> Champions](https://app.unifygtm.com/dashboard/settings/champion-tracking).

2. Click the toggle and click `Disable` to disable Champion Tracking. You will still be able to view job changes Unify has already detected throughout the app, but people will stop being tracked monthly.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=44f909f05e8de9cd3459900b4f8d44ef" alt="" data-og-width="3190" width="3190" data-og-height="2006" height="2006" data-path="images/disable-champ-tracking-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=37840ca83b10acac8200e7b71af94b54 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=3ca0c5786a6be5549a4eb9b9360d8a60 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=02ef09b410b119d0f38a23ac19bffb6e 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=699c345a32a591369d79abeccd711ada 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0caef2bbf46fae9958ec8cf8474df7fd 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/disable-champ-tracking-2.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d1812ee51780aae9b99e56e91e108506 2500w" /></Frame>

### Take Action on Champion Job Changes

Take action when Unify detects a champion job change.

#### Champion Tracking Audience Filters

In the audience builder, you can add filters for champion job changes.
Connect these audiences to Plays, sequences, and Slack alerts to automate workflows triggered by these changes.

Here is an example of audience filters that includes all champions for whom Unify has ever detected a job change:

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=69aa43da46a441052de6cd5672c37350" alt="" data-og-width="1765" width="1765" data-og-height="1491" height="1491" data-path="images/audience-champ-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=17bd9ea96d75b641f52fc34fff1d2eac 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=8e5fff1f1d53c86cf49c9060416bcba2 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f684e26635560738a6f5543ce86d1dd8 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=49dfbfdae52be7e72d137294c6ef8a4a 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7219bcef0073b832564fcc3271ec750e 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/audience-champ-tracking.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=7316adfbfd2c24cf383b145c20e36c36 2500w" /></Frame>

### Frequently Asked Questions

#### How can I be notified in Slack whenever a champion changes jobs?

Create an audience containing champions who have changed jobs and enable Slack alerts on the audience.


# Lookalike Companies
Source: https://docs.unifygtm.com/reference/signals/lookalike-companies

Find companies similar to your most successful customers.

## Overview

We’ve partnered with [Ocean.io](https://www.ocean.io/) — a leading Lookalike data provider — so you can run automated Plays that target lookalikes of your most successful customers.

The integration is fully managed by Unify and included in your plan, so no additional subscription or setup is required.

## Setup

### Build a new Play

Start by setting up a new Play using the Find Lookalike Companies trigger. You can also get started with our [pre-built template](https://app.unifygtm.com/dashboard/plays?templateType=SEQUENCE_LOOKALIKE_COMPANIES).

<Frame caption="The Find Lookalike Companies trigger node in the Play Builder.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1679fdcaa507618368fab7d31ca6aaf" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-build-play.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ca34496b03f727a920900fbead8159c2 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=296543a58626202548c52f8e1fa95654 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=7d0c1fdfaa6a0d7a41ec6b6b844b67e6 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=2078f42941b75a1a39fe2d250349ad7f 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=0023ad84e93d6ebd3eaf39a2635a6d23 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-build-play.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=1ea4d2cc40d30de8911fb92486569896 2500w" />
</Frame>

### Configure the Trigger

First, configure the seed companies you want to find lookalike companies for. You can do this by adding filters to select companies that meet your criteria,
just like building audiences.

<Frame caption="The criteria panel for a Find Lookalike Companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1b6b19abcb96637ada83885fc3594c7" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-criteria-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=24108a56f46defdb2a7cd8532d7f35c3 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e082600be56e2e8e51f92f5b6c2b53d1 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ad6e60a9ab61f9bb56dc6b85c4f0fa9d 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=533504120e70cc6efedf3c40f4d4b114 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e05e930b767632122fda43bbd544dade 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21eddece4a8dbbd255acce80fe6116e9 2500w" />
</Frame>

Next, configure the lookalike companies you want to find for each seed company.
You can set the number of lookalike companies per seed company, minimum relevance score, and more.

The previews on the right will show you a sample of the lookalike companies that will be found based on your configuration.

<Frame caption="The configuration panel for a Find Lookalike Companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=11e4dd11db05b12b7586fa07031668d5" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-configuration-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d476fac45cafa4a90b0276e2e3feb54b 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3a5c06738c881929fe9461124612b10b 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=56b0970bee1a35256829f2464863ef41 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=be8f6bd13d7d47c35c2844624973b733 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ceb8d2545cdc7e918eee00f519f9bf26 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f03b70c53fc8620d588f8a20adcc783e 2500w" />
</Frame>

Build the rest of your Play as you need, then click Publish to begin finding lookalike companies and running them through your Play.
Learn more about building Plays [here](/reference/plays/overview).

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="How do I see what seed company a lookalike company was based on?">
    Find your lookalike company in the Play Logs.

    <Frame caption="A list of Play Logs.">
      <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c53e3ff3bd3fe6640fc29b09ebd38559" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-play-logs-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d3eb8800359c2472569bb638d5cc207d 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f2c50dd46075512e21ae0aaee0d231c8 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=eac3992bab5e864fbb6340d79c25f943 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a9a1df18ad96711041cc87c582918392 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=87b61c8cec907d3d07024d3dc69ee4f5 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-logs-list.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=07a3f36c7ae49d8be1ab91e46fdb4bc7 2500w" />
    </Frame>

    Click the Trigger node to see details like the seed company and the relevance score.

    <Frame caption="A log of the Play trigger.">
      <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=30d6035deef5fb8f3f86f3f223ae1e2d" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-play-log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=0ccd3dec36f42830fa4b81fc75f8557c 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3f2791becfdc4bdd1bdcea2ed0cbeec6 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3399dfce5fdb3a29fff6e41b0e4222b8 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=296923899e2d7127d1478c585e685c8a 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21d1f9209a0d5c4172b0078a15d18a11 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-play-log.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a88e2073261bc2306d1d40f6386e5a13 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="How long does it take for Play Logs to appear for my lookalike companies?">
    Depending on the number of seed companies the Play is running on, it can take up to several hours for Play Logs to appear.
  </Accordion>

  <Accordion title="Do I get charged credits if a lookalike company falls under my exclusion rules?">
    Nope! Lookalike companies that fall under your exclusion rules will not run through the Play, and you will not be charged for them.
  </Accordion>
</AccordionGroup>


# New Hire Tracking
Source: https://docs.unifygtm.com/reference/signals/new-hires

Automatically track new hires at companies and take action.

## What is New Hire Tracking?

A new hire is someone who has recently started a job at a new company within the past 90 days.

New Hire Tracking helps you identify and monitor individuals who have recently joined companies that align with your target profile. These new hires often play pivotal roles in shaping change within their organizations, making them valuable opportunities for outreach.

These are not people in your current Unify instance, they are net new prospects, meaning that they have not already been sourced through CRM integration, website intent, or uploaded manually.

By using New Hire Tracking, you can apply specific filters to define your target companies and personas, automatically keeping track of new hires at these organizations.

### Why is this a valuable signal?

New hires signify organizational shifts and often catalyze new purchasing decisions, presenting valuable opportunities for strategic outreach.

### How does New Hire Tracking work?

Once activated, Unify scans for new hires that match your selected personas at your target companies, delivering their contact details to you daily. Your target personas and companies can be customized to include or exclude specific job titles, industries, company size, and location. This enables you to build a dynamic, up-to-date list of key contacts for your team to engage through Audiences.

New hires will not track existing contacts synced over from your CRM today. If enabled, Champion Tracking will be tracking when contacts from existing customers change jobs. For more information, see the [Champion Tracking section](/reference/signals/champions).

Each tracked new hire costs two credits, regardless of whether the lead has been routed or engaged.

To view tracked new hires, navigate to the “New Hires” tab in the New Hire Tracking Settings.

### Setting Up New Hire Tracking

Define the personas and companies you want to track, then follow the steps below to get started.

#### How to Enable

1. In the Unify app, go to [Settings -> Track -> New Hires](https://app.unifygtm.com/dashboard/settings/new-hire-tracking).

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b67aa92af66e2711b70822816667ec0a" alt="" data-og-width="3058" width="3058" data-og-height="1562" height="1562" data-path="images/new-hire-tracking-1-blank.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c32c6925dec08462f75012c81b1068d7 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d2d4aef887d7345503d8098c1329bdbc 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4cb6c8c1fc539c621e85341f0a43202f 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5dfb1dd36ca1d6d6cbb2fc234d87742b 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=de4f6a686832074ae8889b7ab3a1657a 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-1-blank.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d9e3f17a24d34663c7bbe4e67613031e 2500w" /></Frame>

2. Click the toggle at the top of the page to open the New Hire Tracking Settings.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7518af29aec71921d10a1d8c2a71056d" alt="" data-og-width="3058" width="3058" data-og-height="1562" height="1562" data-path="images/new-hire-tracking-2-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=50f5156c37ab39329fc17ddab70ac5ad 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=91411240e5f40292b60edd45fb366547 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=bc448659cfa521a9bfa8cc7dbba4f5c2 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=dca607b9a4ce983b5c372eec0a97f4d3 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=231d0010194c3cdb112ab235d197f842 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-2-settings.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=86cbd2c4108e9bf19c427c51b45ffbbe 2500w" /></Frame>

3. Apply filters to fine-tune your new hire tracking. For best results, use all available filters to narrow down the most relevant target companies and personas.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cdb6de2baaf21b988ebeb1c2cfa8db98" alt="" data-og-width="3066" width="3066" data-og-height="1838" height="1838" data-path="images/new-hire-tracking-3-enable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=76bb687a719be26f80da5a03a587e3e4 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6b67495d1452d217ddfcefca7a72c0c1 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8094dfc19c6744cff995b5450e10d410 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=68364aa03c46cb08df9e04eab2ee3db5 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aecf3ba69cd5bb7fb3ca2da73a55c66f 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-3-enable.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=016ee8d8eb96f7034412250497f1ba1f 2500w" /></Frame>

4. Click `Enable New Hire Tracking`. Unify will begin tracking new hires daily from this point forward.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=96598c671ca95baa8c6a49fbe2d70e4c" alt="" data-og-width="3050" width="3050" data-og-height="1831" height="1831" data-path="images/new-hire-tracking-4-enabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f854debe04d0827da5e500dfdda3698f 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fe818fecacd51b983271be1de0f1f02b 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7d46ca8d4e7db4e4a56c4aba95853755 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=dc5c240286ee33b94437cc36a69fd6d4 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=175bad98b34830da7e78b4614fefb210 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-4-enabled.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c76630a86225ead222be77fbb050fe8b 2500w" /></Frame>

#### How to Disable

1. In the Unify app, go to [Settings -> Track -> New Hires](https://app.unifygtm.com/dashboard/settings/new-hire-tracking).

2. Click the toggle and select `Disable` to stop tracking new hires. Previously detected job changes will remain visible, but new hires will no longer be tracked.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d62e300b870d0bb5b817136af5840198" alt="" data-og-width="3242" width="3242" data-og-height="1830" height="1830" data-path="images/new-hire-tracking-5-disable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=c2a8ec3c5e6282f7c6c975468108ba14 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8350c40e23f6f0e16ec8c57235902580 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=6f08fe4be8cf2f6be8e54a5955f271e4 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=10139448ad3a3834c265d15e25e97148 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a411e9e0c48e04099c6d153e13c7b52f 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-5-disable.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=190a84d6d4a9ed1ca3f316d55cfc2dad 2500w" /></Frame>

### Acting on New Hires

When Unify identifies a new hire, you can immediately add these contacts to audiences and run Plays on them. Similar to setting up Plays to capture website intent or retarget CRM opportunities as they’re added, you can create Plays that consistently capture and engage with new hires added by Unify!

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4b9ce04edbf1c29710a5913bb3ab99d7" alt="" data-og-width="3058" width="3058" data-og-height="1798" height="1798" data-path="images/new-hire-tracking-6-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=74f99cb787473c85278277c2d30c1f09 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f2a92f31976cfe1ba7d7109bb8d01a2b 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ada09f9dbaefbd0db4c0dfb6d2b20965 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a4da97c04b8550c0e17b37db74279e32 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=545865f6d4c30a64c36c8d5cee973d39 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-6-results.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=9e008220b251719e95a5b8e5a96fb297 2500w" /></Frame>

#### New Hire Tracking in Audience Filters

In the Audience Builder, you can add filters to focus on new hires.

These audiences can be linked to Plays, sequences, or Slack alerts, allowing you to automate workflows based on new hire data.

Here’s an example of filters used to track all new hires:

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=158f560af7348a37a4f3c9b895f8ea7f" alt="" data-og-width="3246" width="3246" data-og-height="2182" height="2182" data-path="images/new-hire-tracking-7-audiences.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=78d82d08ca383a6ac7771f05add55788 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4b0096e3622b296cc8b1b8384cd32ff1 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=faf382ac1d6388584a3a940246802309 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8425c6478a119ee1ab2e86f1b50aa49d 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d2bbd9ac007f2abe5c8e372e6ac70418 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/new-hire-tracking-7-audiences.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=45c04dedf5a814918f898ed24fdc2903 2500w" /></Frame>

### Frequently Asked Questions

#### How can I get Slack notifications for new hires?

Create an audience for new hires, then enable Slack alerts for that audience to receive real-time notifications.

#### How do I stop tracking new hires?

Click the toggle to disable new hire tracking. Previously detected job changes will remain visible, but new hires will no longer be tracked.

#### Can I track new hires in a specific industry?

Yes, you can filter new hires by industry.

#### Can I track new hires by country?

At the moment, you can track new hires based on the location of their company. We’re actively working on expanding this feature to allow tracking new hires based on their individual country of residence.

#### How are you selecting the new contacts added to Unify?

We identify ideal new hire prospects who have changed roles within the last 90 days, using a combination of job title, company size, and industry. These prospects are then selected through a randomized process.


# Unify Signals
Source: https://docs.unifygtm.com/reference/signals/overview

Learn what data signals are and how to use them.

export const WebsiteIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0"></path>
    <path d="M3.6 9h16.8"></path>
    <path d="M3.6 15h16.8"></path>
    <path d="M11.5 3a17 17 0 0 0 0 18"></path>
    <path d="M12.5 3a17 17 0 0 1 0 18"></path>
  </svg>;

export const OceanioLogo = () => <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 225 225" width="24" height="24">
    <rect width={42.12} height={14.56} x={89.93} y={13.71} fill="#3b56f4" rx={7.02} />
    <path fill="#3b56f4" d="m127.42 60.72.01.19a4.99 4.98-1.6 0 0 4.98 4.71q51.86-.03 60.91-.03 5.61 0 7.76.86c5.26 2.12 7.38 6.84 9.82 11.91 1.51 3.14 3.26 6.2 2.15 9.28-1.7 4.77-5.15 5.31-10.15 5.25q-4.29-.05-27.66-.01a3.64 3.43 34.2 0 0-1.12.18c-4.15 1.43-6.09 6.24-3.21 9.75 1.49 1.83 3.52 2.45 6.06 2.46q22.54.11 29.96-.05 6.34-.14 8.96 1.28 5.97 3.23 4.79 11.49-1.05 7.26-3.66 16.28-1.89 6.5-8.47 8.1a1.28 1.17-47.6 0 1-.22.02q-11.5.01-89.33 0c-8.22 0-11.09 9.73-3.86 13.99q1.58.93 5.46.83 2.55-.06 74.65-.02c2.77 0 5.18.1 6.53 2.3 1.4 2.27.81 4.46-.87 6.66q-27.99 36.74-72.11 44.06c-41.31 6.86-83.17-10.4-107.83-44.42-3.38-4.66-.7-8.69 5.03-8.63q10.12.1 17.64-.03a3.3 3.18 32.6 0 0 1.15-.23c6.16-2.47 7-9.89 1.26-13.55q-1.78-1.13-6.27-.98-2.3.08-24.52.02c-6.26-.02-9.05-3.86-10.77-9.92q-1.8-6.33-2.83-12.11c-1.19-6.67-.61-11.17 4.98-14.19q1.74-.93 6.41-.93 25.46.04 100.2.02c8.42-.01 8.74-11.96-.11-12.41q-.41-.02-93.94.02-5.9 0-7.62-1.39C8.5 89 7.86 85.26 9.66 81.39c2.51-5.37 5.01-12.01 10.46-14.62q2.51-1.2 7.94-1.18 13.19.04 61.58.04a4.93 4.92-88.7 0 0 4.92-4.71l.02-.33a4.63 4.62-88.4 0 0-4.57-4.83q-6.96-.09-21.24-.05c-9.26.02-12.32-12.1-3.94-16.3q1.98-.99 6.06-.99 42.27.01 82.61.01c7.38 0 11.61 9.19 6.03 14.51q-2.94 2.8-6.01 2.78-13.17-.11-21.48.03a4.71 4.7 87.9 0 0-4.62 4.97" />
  </svg>;

export const NewHiresIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-yellow-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7m0 2a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2z"></path>
      <path d="M8 7v-2a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v2"></path>
      <path d="M12 12l0 .01"></path>
      <path d="M3 13a20 20 0 0 0 18 0"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-yellow-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7m0 2a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2z"></path>
      <path d="M8 7v-2a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v2"></path>
      <path d="M12 12l0 .01"></path>
      <path d="M3 13a20 20 0 0 0 18 0"></path>
    </svg>
  </>;

export const ChampionsIcon = ({size = 24}) => <>
    <svg class="block dark:hidden" stroke="var(--icon-pink-light)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M12 6l4 6l5 -4l-2 10h-14l-2 -10l5 4z"></path>
    </svg>
    <svg class="hidden dark:block" stroke="var(--icon-pink-dark)" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
      <path d="M12 6l4 6l5 -4l-2 10h-14l-2 -10l5 4z"></path>
    </svg>
  </>;

## What are signals?

Signals are data sources that provide insights into companies and people that
are demonstrating buying intent. Unify brings a multitude of real-time signals
together to help you identify and engage with warm prospects at exactly the
right time.

<Frame caption="An audience showing high-intent website visitors.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=aecec098bb0f6c71ef44e8b95796d010" data-og-width="2880" width="2880" data-og-height="2118" height="2118" data-path="images/reference/signals/audience-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=45cd1c34a79637a137909ba9b6665f4c 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=07ff339b13324b68332f43c19a485de1 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=a49aab1d67c9dc90ff4da84b92c17355 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=5863c87e9a563641853fea9858956620 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=36714379328a6ae84fd70260edef7bf6 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/audience-page.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=900e18eab4d9477530c2f59cc352f0d0 2500w" />
</Frame>

Unify doesn't just bring the data. Unify is a system of action that provides the
framework and the tools to act on that data in the most effective way possible.

## What signals are available?

Unify provides a wide range of signals, from real-time website visits to
continuous champion tracking. Here are some of the most popular signals
available in Unify:

<CardGroup cols={2}>
  <Card title="Website Visitors" icon={<WebsiteIcon />} href="/reference/signals/website-visitors">
    Identify the companies and people visiting your website in real-time.
  </Card>

  <Card title="Champions" icon={<ChampionsIcon />} href="/reference/signals/champions">
    Keep track of champions for your business moving to new companies.
  </Card>

  <Card title="New Hires" icon={<NewHiresIcon />} href="/reference/signals/new-hires">
    Find out when key decision-makers join a company you're targeting.
  </Card>

  <Card title="Lookalikes" icon={<OceanioLogo />} href="/reference/signals/lookalike-companies">
    Find companies similar to your most successful customers.
  </Card>
</CardGroup>


# Website Visitor Intent
Source: https://docs.unifygtm.com/reference/signals/website-visitors

Start revealing the companies and people visiting your website.

## Overview

By integrating with your website, Unify can reveal the companies and people
visiting your website in real-time. Beyond idenifying these visitors, Unify
enables you to take action based on which pages they're clicking on, where
they're visiting from, and how many sessions they've had.

## How to get started

### Step 1: Integrate Unify with your website

The first step is to integrate Unify with your website using either the official
Unify plugin for your website or a third-party analytics provider like Segment.

If you're not already using Segment, we recommend starting with the official
Unify plugin. You can find the installation instructions [here](/developers/intent-client/overview).
For customers already using Segment, you can find the instructions for setting
up the official Segment integration [here](/reference/integrations/segment).

### Step 2: Turn on website intent data

Once that's done, the only thing left to do is to enable the feature in Unify
and start revealing the companies and people visiting your website. Navigate to
[Settings -> Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
to turn on this feature.

If you already have a subscription to 6sense or Clearbit Reveal, you can also
bring your own API key. See the [6sense](https://app.unifygtm.com/dashboard/settings/integrations/6sense)
and [Clearbit](https://app.unifygtm.com/dashboard/settings/integrations/clearbit)
integration settings pages to get started.


# How to Create a Play
Source: https://docs.unifygtm.com/tutorials/how-to-create-a-play

Learn the fundamentals and build a Unify Play from start to finish.

export const PlayBuilderCompanyHandleDark = () => <svg className="hidden dark:block" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#403C2A" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#404040" />
    <g clip-path="url(#clip0_2769_1689)">
      <path d="M5.75 16.25H16.25" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 8.66663H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 11H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 13.3334H9.83333" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 8.66663H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 11H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 13.3334H12.7503" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M6.91699 16.25V6.91667C6.91699 6.60725 7.03991 6.3105 7.2587 6.09171C7.47749 5.87292 7.77424 5.75 8.08366 5.75H13.917C14.2264 5.75 14.5232 5.87292 14.7419 6.09171C14.9607 6.3105 15.0837 6.60725 15.0837 6.91667V16.25" stroke="#FFEE9A" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1689">
        <rect width="14" height="14" fill="white" transform="translate(4 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderCompanyHandleLight = () => <svg className="block dark:hidden" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#FFFAE6" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#E2E2E2" />
    <g clip-path="url(#clip0_2769_1689)">
      <path d="M5.75 16.25H16.25" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 8.66663H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 11H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.25 13.3334H9.83333" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 8.66663H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 11H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M12.167 13.3334H12.7503" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M6.91699 16.25V6.91667C6.91699 6.60725 7.03991 6.3105 7.2587 6.09171C7.47749 5.87292 7.77424 5.75 8.08366 5.75H13.917C14.2264 5.75 14.5232 5.87292 14.7419 6.09171C14.9607 6.3105 15.0837 6.60725 15.0837 6.91667V16.25" stroke="#887115" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1689">
        <rect width="14" height="14" fill="white" transform="translate(4 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonListHandleDark = () => <svg className="hidden dark:block" width="23" height="22" viewBox="0 0 23 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" fill="#323F3E" />
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" stroke="#404040" />
    <g clip-path="url(#clip0_2769_1947)">
      <path d="M12.083 12.1667C12.083 10.5558 13.3889 9.25 14.9997 9.25C16.6105 9.25 17.9163 10.5558 17.9163 12.1667V12.4583" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M15 9.25C15.9665 9.25 16.75 8.4665 16.75 7.5C16.75 6.5335 15.9665 5.75 15 5.75C14.0335 5.75 13.25 6.5335 13.25 7.5C13.25 8.4665 14.0335 9.25 15 9.25Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M5.08301 15.6667V15.0833C5.08301 12.8282 6.91118 11 9.16634 11C11.4215 11 13.2497 12.8282 13.2497 15.0833V15.6667" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.16634 11C10.455 11 11.4997 9.95529 11.4997 8.66665C11.4997 7.37798 10.455 6.33331 9.16634 6.33331C7.87768 6.33331 6.83301 7.37798 6.83301 8.66665C6.83301 9.95529 7.87768 11 9.16634 11Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1947">
        <rect width="14" height="14" fill="white" transform="translate(4.5 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonListHandleLight = () => <svg className="block dark:hidden" width="23" height="22" viewBox="0 0 23 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" fill="#F0FBFA" />
    <path d="M1 11C1 5.20101 5.70101 0.5 11.5 0.5C17.299 0.5 22 5.20101 22 11C22 16.799 17.299 21.5 11.5 21.5C5.70101 21.5 1 16.799 1 11Z" stroke="#E2E2E2" />
    <g clip-path="url(#clip0_2769_1947)">
      <path d="M12.083 12.1667C12.083 10.5558 13.3889 9.25 14.9997 9.25C16.6105 9.25 17.9163 10.5558 17.9163 12.1667V12.4583" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M15 9.25C15.9665 9.25 16.75 8.4665 16.75 7.5C16.75 6.5335 15.9665 5.75 15 5.75C14.0335 5.75 13.25 6.5335 13.25 7.5C13.25 8.4665 14.0335 9.25 15 9.25Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M5.08301 15.6667V15.0833C5.08301 12.8282 6.91118 11 9.16634 11C11.4215 11 13.2497 12.8282 13.2497 15.0833V15.6667" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M9.16634 11C10.455 11 11.4997 9.95529 11.4997 8.66665C11.4997 7.37798 10.455 6.33331 9.16634 6.33331C7.87768 6.33331 6.83301 7.37798 6.83301 8.66665C6.83301 9.95529 7.87768 11 9.16634 11Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    </g>
    <defs>
      <clipPath id="clip0_2769_1947">
        <rect width="14" height="14" fill="white" transform="translate(4.5 4)" />
      </clipPath>
    </defs>
  </svg>;

export const PlayBuilderPersonHandleDark = () => <svg className="hidden dark:block" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#323F3E" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#404040" />
    <path d="M6.91699 15.6667V15.0833C6.91699 12.8282 8.74516 11 11.0003 11C13.2555 11 15.0837 12.8282 15.0837 15.0833V15.6667" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M11.0003 11.0002C12.289 11.0002 13.3337 9.95547 13.3337 8.66683C13.3337 7.37816 12.289 6.3335 11.0003 6.3335C9.71166 6.3335 8.66699 7.37816 8.66699 8.66683C8.66699 9.95547 9.71166 11.0002 11.0003 11.0002Z" stroke="#9DE6E2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
  </svg>;

export const PlayBuilderPersonHandleLight = () => <svg className="block dark:hidden" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" fill="#F0FBFA" />
    <path d="M0.5 11C0.5 5.20101 5.20101 0.5 11 0.5C16.799 0.5 21.5 5.20101 21.5 11C21.5 16.799 16.799 21.5 11 21.5C5.20101 21.5 0.5 16.799 0.5 11Z" stroke="#E2E2E2" />
    <path d="M6.91699 15.6667V15.0833C6.91699 12.8282 8.74516 11 11.0003 11C13.2555 11 15.0837 12.8282 15.0837 15.0833V15.6667" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
    <path d="M11.0003 11.0002C12.289 11.0002 13.3337 9.95547 13.3337 8.66683C13.3337 7.37816 12.289 6.3335 11.0003 6.3335C9.71166 6.3335 8.66699 7.37816 8.66699 8.66683C8.66699 9.95547 9.71166 11.0002 11.0003 11.0002Z" stroke="#0F837B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
  </svg>;

## Overview

Plays are automated workflows that let you build and execute repeatable
strategies. In this guide, you'll learn the basics of how Plays work and create
one from scratch.

### What are Plays?

Building scalable and effective sales, marketing, and GTM strategies requires
successfully coordinating two key components:

* **Data**: Countless data sources go into building scalable automations. This
  data is traditionally scattered across tools and databases, but Unify
  centralizes it in one place.
* **Actions**: Researching companies, identifying decision-makers, executing
  multi-channel outreach, and more. Taking the right action at the right time
  is crucial to success.

Unify is a purpose-built system of action that solves this problem. Plays let
you define a series of actions that will be taken on companies or people at
exactly the right moment.

<Frame caption="An example of a complex Play that performs account research and prospecting.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e45cb527afea9b440f781b3c362b3757" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/play-log-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=d9e5f99522af7614de7ef074d6928298 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6f4be0c0bad7697962c18e3fc54ebdc9 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=85e0fc5e0858129ea8c2f63a746aee2d 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=872421533031903076a3c6ff363748e1 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=06269568e3c70cdd9c67768ba0c419b3 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/play-log-details.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=509373770b388b3dafa75a316e133068 2500w" />
</Frame>

### Tutorial preview

One of the most popular use cases for Plays is to find prospects at companies
that are visiting your website and enroll them in outbound sequences. This is a
great example of a *warm outbound* campaign that targets key decision-makers
at companies showing buying intent.

In this guide, you'll create a Unify Play that runs on companies visiting your
website and performs the following actions:

1. **Prospect**: Find new people at the company that match your buyer personas.
2. **Sequence**: Enroll the new prospects in a sequence to send them emails.
3. **Sync to CRM**: Sync newly found people to Salesforce or HubSpot.

This standard Play is a great starting point to understand how Plays work and
kickstart your outbound strategy.

## Walkthrough

### Step 1: Create a new Play

Look for the [Plays](https://app.unifygtm.com/dashboard/plays) tab in the
sidebar and click on it. This is where you will create and manage all your
team's Plays. To create a new Play, click the **New Play** button.

<Frame caption="This is what the Plays tab will look like before creating any Plays.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cff29c75d17bdbf3027f07ab3436d35b" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/tutorials/how-to-create-a-play/plays-tab-empty.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f24f14011a6df499e276aabf94fd55c5 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=816bb08b805d034e63231d0eed2ffc98 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2d3a5c4c3323abccb208dd8d2601a99c 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=898dba9594055fc824c96de04dfc2847 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e34e0748574e33986fd11789cbb3361f 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-empty.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3d8912c20c3abbf5416cdbe54a557630 2500w" />
</Frame>

<Frame caption="When you create a Play, you will be prompted to give it a name.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e58d97141cac834403326072d465b2d7" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/tutorials/how-to-create-a-play/plays-tab-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=37c9864b4c1e8d173e8b2bef3f481f26 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=61c532a1612ab4b637cb1755b6d0834f 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=a34215c07a4a8e705786bdcaaa10093d 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3a4e4b737146a93fbb64422d9e2e0e98 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6cc52bf882eca2fc2f366e090d34d767 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/plays-tab-new.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1c6b677af82caa9c7690cf9d1949c19e 2500w" />
</Frame>

<Frame caption="Once the Play is created, you will see the Play Builder.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6ba2735b3691266d12815fe96566a4ed" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0891b72049adeb7070cfd68d41d2171a 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=72f405c5d0e774468b00a4af59c462bf 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=afc072a3e34478f33d8619d0c89dde1a 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c8afbcf519c6ab7a578877304ed5dd60 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2f39b83d570b88e269f87de9b584f2ef 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-new.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c5595cc96e9a459b7be4de149ef43143 2500w" />
</Frame>

### Step 2: Choose a trigger

Once you've created a new Play, you will see the Play Builder. The first step
when building any Play is to choose a *trigger*. The trigger lets you specify
exactly when the Play should run and which companies or people it should run on.

In the center of the builder, you will see an action that says **Select a trigger**.
Click on it to show the trigger configuration panel. For this Play, choose the
**Website visitors** template.

<Frame caption="Select a trigger type or a template from the configuration panel.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=626c8d9051dcc830b29cec3b3ef5186c" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ce8c90539ce568ddb539cfa4e52fa9eb 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=74e2152f271b8dc7a32467995aefe384 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b3c548305e34f19b6cd4878eb72d5d60 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=4d8287474d6663d666c2df02f7b64bbc 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f4c43b9618b4a93bc04e0dcc6736d149 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-selection.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f206e8a23e3c1cf814f40976c0a82c9a 2500w" />
</Frame>

<Frame caption="This is where you define the criteria for companies that this Play will run on.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2b206749d5a5ce26f820f6ae9292a32e" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f3d703f6291bf0425ac18cb15828e7f0 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=06481788f75c234ce51d486adec5d6cf 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7ccdef6dcc552d63fc952488a88a4100 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=73b2a89cd15926f512401d1891d1a304 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=927c6a6c13b1336b347ff6166f68e64d 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-trigger-configuration.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d91059e426b79c6ff173c76fcb0d4a1a 2500w" />
</Frame>

Here you have the option to further filter and refine the companies that this
Play will run on. For example, if you only want to run this Play on companies
with more than 100 employees, you can add a filter on **Employee Count**.

You can learn more about the available filters and how to use them in the tutorial
[How to Create an Audience](/tutorials/how-to-create-an-audience). You can always
return later to add or modify filters. Click **Done** to finish configuring the
trigger.

### Step 3: Add actions

Now that the trigger has been selected, it's time to start adding actions. There
are many actions to choose from, and you can configure them in countless ways.
For this Play, we're going to start simple and add three actions.

#### Prospect for people

Start by adding a prospecting action. This action will take the company coming
from the trigger and search for relevant prospects. Drag the **Prospect for People**
action from the action list and drop it into the builder.

<Tip>
  If you drag and drop a new action on top of an existing action, it will
  automatically be connected to it.
</Tip>

<Frame caption="Drag and drop actions from the action list into the Play Builder.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=8a70d73cc70fdda3719cfee1e81ac4bd" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-prospect-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=73a92e0bbdadf0cb6a7527e6197486c9 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7da05e242f3c740e55fce67fed06f905 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=4b040a6bbdb107a0beac1f3c4a2db17b 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d75e2053cfcac6d50736be18ec625ae0 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c7299fe4cdeafc445ff6369cdb1b28f0 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-prospect-action.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=71b2298a4d5c8a3238c0bb1682a1ef10 2500w" />
</Frame>

Once added, you will see the prospecting options shown in the configuration
panel on the left. Here are the most important selections to make:

* **Max. prospects per company**: This is how many prospects you want to find at
  each company. We recommend starting with 2-4 prospects per company.
* **Personas**: These are the personas to search for. You can select from
  existing personas or create new ones. Unify will find people matching these
  personas in order, so list them in order of preference.

If you haven't defined any personas yet, you can learn how to do so in the
tutorial [How to Create Personas](/tutorials/how-to-use-personas).

#### Loop

Next, add a **Loop** action. The prospecting action will return a list of people
found at the company, and the loop will run subsequent actions once for each
person in the list.

<Frame caption="Add a loop and connect it to the prospecting action.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0b1d2ae66f5b9cac90f2458dc80e1b3b" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-loop-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d3510758ce73fe74916637f89b8568cd 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=833c9ec122b854164f8784b4cb5cd1e1 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f6650b8a7933bd89b8e4622afa2846fe 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=4e56fbdd51cd9449f9c5c117b3b4c703 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6090c819665d7aff0bd100385f1efd53 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-loop-action.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ec0221041894ff6ff6331cf03b5847ee 2500w" />
</Frame>

Each action receives an input and produces an output. Actions in the Play
Builder have small colored symbols that represent what type of input and output
they expect.

Here's what each symbol represents:

|                                    Symbol                                   |   | Value                                 |
| :-------------------------------------------------------------------------: | - | :------------------------------------ |
|     {<PlayBuilderPersonHandleLight />}{<PlayBuilderPersonHandleDark />}     |   | A single person record.               |
| {<PlayBuilderPersonListHandleLight />}{<PlayBuilderPersonListHandleDark />} |   | A list of one or more person records. |
|    {<PlayBuilderCompanyHandleLight />}{<PlayBuilderCompanyHandleDark />}    |   | A single company record.              |

Plays work by connecting each action's output to a matching input on another
action. This is how data flows through the Play and how each action knows what
to do.

Most actions run on one record at a time. The **Loop** action is how you take a
list of records and run actions on them one by one.

#### Sequence enrollment

Now place a **Sequence** action inside the loop. This will enroll each person
into a Unify Sequence.

<Tip>
  Once you've dropped the action into the loop, you can drag it near the loop
  action to automatically connect them. You can also manually draw connections
  between the colored icons that represent action inputs and outputs.
</Tip>

Once added, you can configure the sequence enrollment action by routing personas
to the desired sequences and mailboxes. To speed up the process, click the
**Add prospect personas** button to automatically reuse all of the personas you
selected in the prospecting action.

<Frame caption="Configure sequence enrollment by routing specific personas to mailboxes and sequences.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=12626a58af7c353fc968c1ad2e2b6e4a" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b9950fc0584acbf53cbe1f6319a97ee8 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5ad72db6d860d8faa7216d42d0c2bf41 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=7a1fcda9a6fbc4f2e243fb464b4a97cb 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e6033d9fa5bdbf5e7c56013cd22fd01a 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f34a72f9e263b3380706fe3e9d2e60c8 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment-configuration.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f199f7e53f83b8a79cdb13582cb5c68c 2500w" />
</Frame>

<Frame caption="Add a sequence enrollment action and connect it to the loop.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1bf672635996ae091822fdf1b0c88c29" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d55ab3b1e9f78369161b58d8c3073e07 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c9bdf76f56a5eda314adf4102496ef72 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e9bd2aee17ea281d69e59682ab9d8d4f 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=29a5ec8dd9be10d4ba514a6e39950b9a 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1480d0ce088c709d0770e532ef60364f 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-sequence-enrollment.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9dafb02e15482fae113494729dd267eb 2500w" />
</Frame>

#### Sync to CRM

Finally, add an action to sync each new person to your CRM. Depending on which
CRM you've connected in Unify, you will see either a **Sync to Salesforce** or
**Sync to HubSpot** action.

<Frame caption="You can specify default field values or limit the number of people synced per company.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d42ba7dda013eb2ba49eceb901d9b779" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-hubspot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2688e7e74bfbb47659467000ebc35d18 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=88641b55a7624f2ddd10bf9525564fe6 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=84fba174325df17d3f7c692e07f806de 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b467159ad3f4060a838048545c1c41eb 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0aad1f6cd58e155394c1d3acdd0f0d16 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-hubspot.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=068d0989fb11294b1d51aaa0d81d6810 2500w" />
</Frame>

### Step 4: Publish and view logs

Once your Play is ready, click the **Publish** button in the top right corner of
the Play Builder. This will activate the Play and start running it on companies
that match the trigger criteria you defined earlier.

<Frame caption="By publishing the Play, it will immediately start running on companies.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f9b85788f676e11eb97609bbe85b2c7d" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-builder-publish.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f0f04fce1620c21a2e6350d65d16470c 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5564eef36d0069da0bf97b638bb4b227 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c9abadaf695b28e967b1b95a1f8bb3a6 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0b359e99d811faf9f07404978d612b54 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ee24b3fbd4545040aebf951b3f684e58 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-builder-publish.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1dda6efbac70c9e0a0c6799346539ab4 2500w" />
</Frame>

As the Play starts to run on companies, you will see them appear in the logs.
Click on the **Logs** tab at the top of the Play Builder to view the logs.

<Frame caption="Logs show a detailed view of every company or person a Play has run on.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0000cbd964af7144fda4bf0a96f48718" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=23fdb6522358b19ffb37a178e79aac84 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=eeb1ac0fb9d8ab088c0e0e3e01343410 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=bf85420b36887d59a1207b0c518d494e 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3c3280eed3bd13dbb7170d9e7e7b6d67 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c5887529a031e946c6cd4f584d19c0d2 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f00e17ef39123fb018e94d88bf156a0b 2500w" />
</Frame>

Click on any company to view the details of its run, including the exact actions
that were taken and the results of each action. Click on any action to view the
precise inputs, outputs, and result of that action.

<Frame caption="Click on any company to view exactly what the Play did.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9020f1aad71fc48334b3846d4830c5c8" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-logs-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=36196ec7a1ed6b8a4e9fcc2752fc672f 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=757a33102e253f4401cb385fe3e4a719 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b6b541cbd9a635d4ae64ee972d0a95e9 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=928ff09d17d8c2bac9a98aa1e391af18 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=629a60eb18d117e39654f830619e8269 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=252b0f00705b41e4312ec50113d77756 2500w" />
</Frame>

<Frame caption="Click on any action within the log details to see its results.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=91ad526c9c77c88ecf003a903a945f92" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=70ef0f514c54fa918fcb2e04f3d29e82 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5e83673deddbc7529eba855322870b1c 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=513127eced38c67acdaafdd0fd55eb57 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=375eb2c7fb4301b6321ae935e08b0ed9 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=886573471ccd805baa5327f6640eb4e6 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-prospect-action.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=092b46ce42146327ff657e1a9cb0dfe5 2500w" />
</Frame>

<Frame caption="You can use the action logs to inspect exactly how a Play is working.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=765455e619d03172f32b7d50ae4fea94" data-og-width="2592" width="2592" data-og-height="1842" height="1842" data-path="images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1e0d62057264b07bec5848b029ff1481 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=0aaf98efda41aacb73872dc7e1bea93a 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6b62e4b378e15242454eafdf8f7fa404 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=2bf712f0d9bf32d421ebd077c43a02a6 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3876ccb4712d2bf6573f728d944d8ece 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-a-play/play-logs-details-sequence-action.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e2f11ac09c6e4333d2a967373cc5a924 2500w" />
</Frame>

## Conclusion

Congratulations on creating a Play! Combining website intent, prospecting, and
sequences into a single automated flow is a popular Play and an excellent
starting point.

For a comprehensive overview of Unify Plays, check out the reference guide:

<Card title="Plays Reference" icon="arrow-progress" href="/reference/plays/overview">
  Detailed reference guide that covers the fundamentals of plays, the actions
  and triggers available to use, and more.
</Card>


# How to Create an Audience
Source: https://docs.unifygtm.com/tutorials/how-to-create-an-audience

Create dynamic lists of companies and people to view and act on.

## What are Audiences?

In Unify, audiences are dynamic lists of companies and people that are generated
based on powerful filter criteria that you specify. Once defined, you can view and take
action on these companies and people in Unify.

<Frame caption="An audience showing high intent website visitors.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d637fe288df8a1957e0bfdd68aebf76b" data-og-width="2880" width="2880" data-og-height="2118" height="2118" data-path="images/tutorials/how-to-create-an-audience/audience-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=bb884edfa189ec1596fd9cae344948f4 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=35d2bedf2379514d4b985cdfb3d6428e 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=bea140b8e36d2f9892890b9836c9dd32 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=eab565b433b35612b39599a736c5c972 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=04be98818c7cbe37b77b7dc1c4425bd9 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=c842b0a62a970f1bcf0940ebe39ae9a9 2500w" />
</Frame>

Here are just a few examples of the
types of audiences you can define:

* Companies that have clicked on your pricing page in the past week
* People who have opened an email you sent them in the past month at least twice
  without replying yet
* Champions for your business that have joined a new company matching your ICP

Typically, either sales leaders, revenue operations, or sales operations will
create the audiences to be used by sellers for building plays and taking action.

## Build a new audience

Access audiences by clicking on [Audiences](https://app.unifygtm.com/dashboard/audiences)
in the sidebar. You can view and edit existing audiences or create a new one by
selecting **New audience**.

Audience support a wide variety of filters. One of the most commonly used
options is to filter by fields in your CRM. To get started, click **Add condition**
and search for the field you want to filter by.

<Frame caption="Add CRM filters by searching for fields in your CRM and entering the desired condition.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=00681c89de08f917590bbba8513edc71" data-og-width="2290" width="2290" data-og-height="2390" height="2390" data-path="images/tutorials/how-to-create-an-audience/audience-select-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3da586842c9a73f0b4ddb88bf8e7cd00 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=44b499e45bbeb25bac96939fa240d1ff 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=11404f0487139132a7cb66d838e6ba99 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5d21e43809aff41aaafcec61583fc433 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b051ba1b4a487d5b6186638ffca2f7f9 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-select-fields.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6ade1376810a595f6d28e86a882cfed9 2500w" />
</Frame>

Another popular filter is website activity. You can filter by page views,
sessions, and visitors to your website. This is a great way to identify which
companies are showing interest in your business.

<Frame caption="Add website activity filters and define the required criteria.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=4632d4a25ef1e68b0e88a19ee46ed03d" data-og-width="2192" width="2192" data-og-height="1639" height="1639" data-path="images/tutorials/how-to-create-an-audience/audience-page-views.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=86b9b0c30c76d131e5611618e3192071 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9a85bec68c629d944a0fb72b5e85ffe1 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6bfce108428ef5b827541ab03098918a 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cde165408c07a319f3437fe7925cd26d 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=f519303a2f55fddcf22e148cf1dfe255 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-page-views.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=bf0e2d99f3e7ad82e89fcd8789afd11b 2500w" />
</Frame>

You can combine multiple filter criteria with **And** and **Or** groups to
build more complex audiences. For example, you might want to capture companies
that have visited your pricing page or that have filled out an inbound form.

<Frame caption="Combine filters to capture exactly the right companies and people.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=1492b435b0d270ebd1e233582fd52389" data-og-width="2192" width="2192" data-og-height="1639" height="1639" data-path="images/tutorials/how-to-create-an-audience/audience-and-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=d6a0416fc80c735c46eaff6f71aad584 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=05e392f3c282ab2c0eba322a69259ec2 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cad99b3870812aa6bc6d7ea1b26490a0 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=88daf043ce88aa2d19e817cfef48d10d 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=22c485e7078eaed75875f1387c094d70 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-and-filters.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=78bd30b84d4cb3929303d431fe7a5cb9 2500w" />
</Frame>

The best way to to learn about the available filter options is to explore! As
you add and remove filters, the audience preview will update in real-time to
show the companies and people that match your criteria.

## Exclusions

Exclusions are a mechanism to prevent Unify from taking action on specific
companies or people. Common use cases for exclusions include preventing current
customers or competitors from appearing in your audiences or Plays.

Once you've defined exclusions, they will be automatically applied to all
audiences by default. Sometimes, you may want to disable an exclusion for a
specific audience. This can be done from the audience configuration page under
the **Advanced** section.

<Frame caption="Enable or disable exclusions on a per-audience basis.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5a82cd0643498367eed2616ebb4e7c0c" data-og-width="2192" width="2192" data-og-height="1639" height="1639" data-path="images/tutorials/how-to-create-an-audience/audience-exclusions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=fdea55bbd697eaadad6c33571f310420 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5b530fff83180115d2feb519650551f9 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=15d3a34dd0a2b3a3c7f653605896bc7d 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=40c5ade7efff47704e614c20a0a2a14f 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6bd15a880d2697eed93a88388b1d94da 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-create-an-audience/audience-exclusions.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=eb686613b5c15364e42ddfa8e6a4facf 2500w" />
</Frame>

For more information on creating exclusions, see [How to Create an Exclusion](/tutorials/how-to-create-an-exclusion).

## What's next?

Audiences can be used for a variety of purposes, including building plays and
subscribing to Slack alerts. For more information, check out these tutorials:

<Card icon="link" title="How to Create a Play" href="/tutorials/how-to-create-a-play">
  Create a Play that runs on companies or people in an audience.
</Card>

<Card icon="link" title="How to Receive Slack Alerts" href="/tutorials/how-to-receive-slack-alerts">
  Receive Slack alerts when a new company or person enters an audience.
</Card>


# How to Create an Exclusion
Source: https://docs.unifygtm.com/tutorials/how-to-create-an-exclusion

Prevent Unify from actioning on specific companies or people.

1. Excluding current customers
2. Exclude people who have unsubscribed from outbound campaigns

## How to create an exclusion

Let’s walk through how to exclude all Active Salesforce accounts.

### 1. Go to Exclusions in Settings

Navigate to [Settings > Exclusions](https://app.unifygtm.com/dashboard/settings/organization/exclusions) and click `New exclusion`

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=845a080c7721d5f7fe40346ef6d7d8d2" alt="Exclusions 1.png" data-og-width="2000" width="2000" data-og-height="1072" height="1072" data-path="images/49.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=532d5fff3ddfd64d71af29056b9e74d6 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=6ba8f95fe6ce78961e25a7f462b0e0d2 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=d07511e3e0f012ef76f938243473ed02 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b3ef267b0e0e5944f16af9507b561d8d 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=cf502fd2dcc3cb1bcab63c3f64429b93 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=e1c0d7b3c5cec3456d1a7d0fa44b0335 2500w" /></Frame>

## 2. Select Companies or People

Select `Companies` in this case

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=282fa34dd20b99f5612b70c9971544d4" alt="Untitled" data-og-width="2000" width="2000" data-og-height="1070" height="1070" data-path="images/50.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b5bea2b48c375b79ed49e633676b8c8d 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=5a527600534a520896c7738ee94fa565 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b2e5c59fce112c8499ca782247eae15d 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c335a8af79e893bd973123c5344e4cdd 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=ee3b230678279ab16606abfe6f7b197c 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=27d74d1b0670c039ab1b36b3947858af 2500w" /></Frame>

## 3. Define criterion to filter

In this example, we’re creating an exclusion called `Current Customers` that excludes companies with Salesforce `Account Status` equal to `Active`

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=49da7ff94d49ccb761f25da55bc2f558" alt="Exclusions 2.png" data-og-width="2000" width="2000" data-og-height="2069" height="2069" data-path="images/51.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=28a2bca511b10431aa57c7cbe1b262cd 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4c15a9192bc040d2da38884fa35b7bbf 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=772befa106f43f8e046e7377a64a3af3 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=03e674cfae3ed4535033439b149067cf 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ec850505735d3537b1992b85ed485a1 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=6c6a5e3ecf999d335279f0185071147d 2500w" /></Frame>

## 4. Hit Save

Here you’ll see an overview of your new exclusion. These lists will automatically be excluded from targeting.

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=5f8049145d8c1e9fe72e6d09a4e6064a" alt="Exclusions 2.png" data-og-width="2000" width="2000" data-og-height="1077" height="1077" data-path="images/52.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8fa09380d3ef8860d43e26ae7243aab6 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=23dce421576b5f6fc29ceb3e638f45c7 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b4b10bedc60fa86a8a2c55d8ea0144ff 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=115b0c00106f2002216890bd2b5206ad 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=cc939bf1aeef4ec04c0b4813694d79c3 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=47f55c8d43e176f9f2d169e62668ed1d 2500w" /></Frame>

## Upload exclusions from a CSV

Let's walk through how to set up an exclusion using a CSV of companies or people.

### 1. Create a column in your CSV called "Status"

Populate the "Status" column with the same value across all the rows in your CSV. This value usually indicates the type of contact you are excluding. Examples can include "Active Customer", "Competitor", etc.

### 2. Upload these contacts in the companies or people tab

If you're uploading companies, you'll need to include both the company name and domain. If you're uploading people, you'll need to include one of the following set of fields:

* Email
* First Name, Last Name, and Company Domain
* LinkedIn URL

### 3. Map the CSV fields to the Unify fields

You'll select the fields you want to map into Unify. Make sure to select "Status" field from Unify when mapping that same column from your CSV. The Unify "Status" field should then populate with the values you populated in the CSV under the column. Once these are mapped, you can finish the upload.

### 4. Create a new exclusion and add the "Status" field in the conditions

You'll then switch over into the "Exclusions" tab in your settings and create a new exclusion. Under either the people or companies filters, you will select the Unify status column and add the value from your CSV (i.e. "Active Customer"). Once you save this exclusion, this list should be excluded from future audiences and Plays moving forward!

***

Note that if you would like to add more companies or contacts to this exclusion list in the feature, you'll need to follow the same process as above and make sure the "Status" field is correctly mapped. This should automatically pull in the new exclusion after uploaded if the "Status" value is the same value in the filter.


# How to Receive Slack Alerts
Source: https://docs.unifygtm.com/tutorials/how-to-receive-slack-alerts

Receive real-time Slack alerts when companies or people enter an audience.

## Audience Entry Alerts

When a new entry is added to the audience, a notification will be sent to the selected Slack channel.

### Enabling

1. Go to the audience page and click on `Enable alert`.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e3a108547d3f950e7a804c7251cfbb5e" alt="" data-og-width="3434" width="3434" data-og-height="1770" height="1770" data-path="images/71.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=81009de9654f0b8bba62089c3c647473 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=71f90e62850667e98e8325e87ffcd514 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=49d87ae0da90244df5e880a305d9e04b 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a7931090791cc6f5287bbd3064669069 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0f3210331b0b5fddfa7437f8c83f1aa5 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/71.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=eb3da34176214ef728d705567539dcca 2500w" /></Frame>

2. Choose a channel from the dropdown menu.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=568ce933ee511219be77972069a3b120" alt="" data-og-width="3424" width="3424" data-og-height="1764" height="1764" data-path="images/72.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0c165b3f0aec04c647792c46578ba6dd 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ca856522edcec52f6b49d2714e82bd4d 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e922021a3cd90936eeddd402d8470f46 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=626bf2941eaeb3de748c52420928ecdc 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a735e6683980b942a554c4b642885e7e 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/72.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=726e597155a5574e395d5f4ca12e7975 2500w" /></Frame>

<p />

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9b190da597da67ea0ef04d0ee6cdcc23" alt="" data-og-width="1860" width="1860" data-og-height="630" height="630" data-path="images/73.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=1733196db2a86cbed2b9a62e90bf49fb 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0b07d4cd7f99006131c7748063ec3299 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d53d35653359529b078cc33624d20a90 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=14fd00c401c6f2919623f4e706b5f7a4 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=669b229a1b6528e916298003fffd6173 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/73.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=354f5ce33907b8fb45e2f48ee1a44849 2500w" /></Frame>

3. After selecting a channel, click on `Enable`.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=6137386872a8e577cc0c885d56198a73" alt="" data-og-width="1856" width="1856" data-og-height="1762" height="1762" data-path="images/74.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=150dab34a24d2680be09e4d32051e669 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=8cb54c28899cbc6e91ede457406ade5b 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ecba20d54d1396b3f844b51e31458514 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=9bece39121a54933ed0675c5fce081bc 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=50d2be7210a0dd934a15b3ada050304c 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/74.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=08d54f5e5e6cabf56393aaee783e0eaa 2500w" /></Frame>

### Disabling

1. Go to the audience page and click on `Enabled`.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ba69c9c40cdf9c7fceab7e45164c0c06" alt="" data-og-width="3430" width="3430" data-og-height="1768" height="1768" data-path="images/75.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=147d80ee58d4d8c9ce8342972548ac36 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=cfcb9545f11d2a2d53cf1c1862f8b024 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=25a1cf68cc7f5211fe18d41d6a97e73d 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=0a11cc74d23caab50dcc89d2cd9f6f92 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2c4e6491ef1691afd0a23383338bb2af 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/75.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=367bcb7be2f400e1018c9e6b2d82f310 2500w" /></Frame>

2. Click on `Disconnect`.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=29c36473f8d5beccc922bb5ca82fc24d" alt="" data-og-width="3430" width="3430" data-og-height="1774" height="1774" data-path="images/76.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ac0e7127b27ad1af040eb01c6e806509 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a37e1184ef9df2261e0ccb209816a998 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e9262cd548118c47138b0ce52127d7ce 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=f9c8b01a1b3264d7cb209857b61e041d 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=60042dd40f4e362c479ac729cf7a47a2 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/76.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=2c6a8d9aca668c3466cba96ac7d60a1f 2500w" /></Frame>


# How to Define Personas
Source: https://docs.unifygtm.com/tutorials/how-to-use-personas

Create personas to prospect and reach out to your ideal buyers.

## Overview

Personas are collections of job titles that you want to target. Each persona
consists of a list of titles that you want to include and exclude. Personas can
be used throughout Unify, such as when prospecting or routing people to
different sequences.

## Create a persona

Navigate to the [Personas](https://app.unifygtm.com/dashboard/settings/personas) tab in
the sidebar and select **New persona**. Here you can add job titles that you
wish to include or exclude when matching people against this persona.

<Frame caption="Add titles to be included or excluded.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=9661c87c764e1b33e5bc31d6eb306ce1" data-og-width="2920" width="2920" data-og-height="2128" height="2128" data-path="images/tutorials/how-to-use-personas/create-persona.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cd484fc4df2c2608b6d53950480dc682 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e373b2fa7fb42f34c94464d3b398a81f 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=cff4d35ffc40d5e6835676b9b6883e67 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=b79b803f58a0b86ff810d2dab0f02d0a 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=ba5ab5b5301115aaf506adb1f8ac401f 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/create-persona.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e6e0c7fdfbdf4ad44f0b885a45600fa2 2500w" />
</Frame>

You can also take advantage of AI-powered persona generation to automatically
find and add similar job titles to your persona. This lets you quickly define
comprehensive personas that match different variations of a job title.

<Frame caption="You can add suggested titles individually or all at once.">
  <img src="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=e4bde852dfce8189950f43d91dbe4240" data-og-width="2920" width="2920" data-og-height="2128" height="2128" data-path="images/tutorials/how-to-use-personas/persona-suggestions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=280&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=6fff371937921dc0895b1eb6686f0bc0 280w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=560&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=3f354d7b62d395825bfe20f771005e00 560w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=840&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=59d6ddcd947de208ef143ccc147b85ee 840w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=1100&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=78f259354a572baba6a322cefcb23439 1100w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=1650&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=5c71ab6613ec975204529aa5cf7b446e 1650w, https://mintcdn.com/unify-19/QTxNj2fcd-br9FnE/images/tutorials/how-to-use-personas/persona-suggestions.png?w=2500&fit=max&auto=format&n=QTxNj2fcd-br9FnE&q=85&s=75f89df8d9f486860e50a572f4feecd9 2500w" />
</Frame>

Once you've added all the titles you want to include or exclude, click **Create
persona** to save your changes. This persona will now be available for use
throughout Unify.

## Title matching behavior

When evaluating whether a person's job title matches a persona, Unify adheres to
the following rules and heuristics:

* **Ignore capitalization**: For example, "RevOps Lead" and "Revops lead" are
  considered equivalent.
* **Ignore punctuation**: For example, "Enterprise Sales, Lead" and "Enterprise
  Sales Lead" are considered equivalent.
* **Ignore word order**: For example, "Lead Sales Engineer" and "Sales Engineer,
  Lead" are considered equivalent.
* **Ignore extraneous words**: For example, "CEO" and "CEO and Founder" are
  considered equivalent.

That means that you don't need to exhaustively list every possible variation of
a job title in your persona. Instead, you can focus on the most common keywords
and let Unify handle the details.


# Unify Tutorials
Source: https://docs.unifygtm.com/tutorials/welcome

Quickly learn the basics and become a Unify expert.

export const PlaysIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"></path>
    <path d="M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"></path>
    <path d="M11 19h5.5a3.5 3.5 0 0 0 0 -7h-8a3.5 3.5 0 0 1 0 -7h4.5"></path>
  </svg>;

export const PersonasIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M4 4m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v1a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M4 13m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v3a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M14 4m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v3a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
    <path d="M14 15m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v1a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
  </svg>;

export const ExclusionsIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
    <path d="M5.7 5.7l12.6 12.6"></path>
  </svg>;

export const AudiencesIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M4 4h16v2.172a2 2 0 0 1 -.586 1.414l-4.414 4.414v7l-6 2v-8.5l-4.48 -4.928a2 2 0 0 1 -.52 -1.345v-2.227z"></path>
  </svg>;

<CardGroup cols={2}>
  <Card title="How to Create a Play" icon={<PlaysIcon />} href="/tutorials/how-to-create-a-play">
    Learn the fundamentals and build a Unify Play from start to finish.
  </Card>

  <Card title="How to Create an Audience" icon={<AudiencesIcon />} href="/tutorials/how-to-create-an-audience">
    Create dynamic lists of companies and people to view and act on.
  </Card>

  <Card title="How to Define Personas" icon={<PersonasIcon />} href="/tutorials/how-to-use-personas">
    Create personas to prospect and reach out to your ideal buyers.
  </Card>

  <Card title="How to Create an Exclusion" icon={<ExclusionsIcon />} href="/tutorials/how-to-create-an-exclusion">
    Prevent Unify from actioning on specific companies or people.
  </Card>

  <Card title="How to Receive Slack Alerts" icon="slack" href="/tutorials/how-to-receive-slack-alerts">
    Receive real-time Slack alerts when companies or people enter an audience.
  </Card>
</CardGroup>


