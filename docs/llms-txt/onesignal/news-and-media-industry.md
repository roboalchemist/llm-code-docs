# Source: https://documentation.onesignal.com/docs/en/news-and-media-industry.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# News and media industry

> An overview of messaging and strategic best practices specific to the news and media industry.

## Prompting best practices

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/R56m4ynqMtA?si=RWIQ8m9MZBrR77yK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Provide clear context for messaging they will receive

With so much content and information available at your fingertips these days, it’s important to let your users know exactly what type of messaging they will receive.

It’s best to explain the benefits of the news updates users will receive *before* asking permission, which can help to maximize the push subscription rate. Don’t be afraid to tell users exactly what kind of updates they will be receiving.

### Allow users to choose what they’d like to receive notifications about

A best practice for news sites and apps is to allow users to choose which categories of news they'd like to receive notifications about. Providing specific opt-ins to specific news categories allows your users to be in control of the information they receive and can lead to greater engagement.

News category examples include:

* Breaking news
* World news
* Local news
* Politics
* Technology
* Sports

Apps that use segments and target users effectively generally see **50% higher click rates** than apps that do not.

### Prompts

<Tabs>
  <Tab title="Category Prompt">
    For web push, OneSignal’s [Category Prompt feature](./permission-requests) allows you to easily add and create categories for users to opt-in to as well as clearly explain the benefits of why they should opt-in. A 2-in-1 feature that aligns perfectly with the needs of news/media websites.

    <Tip>
      * Be direct with the types of content updates users will receive. Don’t risk being vague and potentially over messaging
      * Provide users with control - allow them to choose exactly what types of content they’d like to receive.
      * Effective message segmentation leads to increased engagement and click through rates
    </Tip>
  </Tab>

  <Tab title="Custom Link Prompt">
    OneSignal actually has a web push feature that can be set-up to automatically group users based on the page visits.

    The [Custom Link Prompt](./permission-requests) provides prompting for push notification permissions through a link or button you can place anywhere on your site. Simply add the "onesignal-customlink-container" CSS class to any div HTML tag on your site to use and enable the prompting option on the OneSignal dashboard or through OneSignal.init if you are using a custom setup. This provides more customization and a less intrusive user experience to other prompting options.

    The Custom Link Prompt allows for the following customizations:

    * Size
    * Explanation text (optional)
    * Subscribe text (defaults to "Subscribe to push notifications")
    * Flag to show/not to show unsubscribe button (defaults to show)
    * Unsubscribe text (defaults to "Unsubscribe from push notifications")
    * Colors
    * Button color (button mode only)
    * Text color

    Be sure to tap into your users interests based on their own self-selection or the pages they visit to effectively target them with appropriate content. This will lead to increased audience growth and retention.
  </Tab>
</Tabs>

## Send news updates based on visitor/user interests to grow and retain audience

Growing your audience is typically a major focus of news and media companies. Moreover, retaining that audience is right up there as well. By providing users information on exactly the topics that they’re interested in, you can actually achieve both: growth and retention.

In addition to the recommendations outlined in [Prompting Best Practices](./permission-requests#what-are-some-best-practices-around-web-push-prompting), another effective way to segment your users based on their interests, is to group them by the pages they visit within your app or website. They’re already showing interest by visiting that specific page, so additional content or updates pertaining to that category page will most likely be relevant.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/r6GeyiYxiN4?si=5Tl4DgUxWxE3LM2c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Tag page visits

Data tags are a great way to segment or group your users based on the pages of your site or app they visit. Depending on which pages of your site or app a user visits, you can automatically add a category or page specific tag to their user or device profile. You can even set additional criteria for when you’d like the page visit tags to be applied, for example - the number of page visits.

For web push, we’ve even outlined the specific code you can add to your site to have the appropriate page visit tag added automatically: [Tag Page Visits](./auto-segment-users-by-page-visit)

### Tag with subscription page

Within OneSignal, you can also tag web users based on where they subscribed to notifications from, which can help with further leveraging known interests to help retain your audience: [Tag with Subscription Page](./auto-segment-users-by-subscription-page)

### Tag with notification data

OneSignal also allows you to track and segment mobile and web push users by clicked notification data.

Three common things you will want to know about your notifications:

1. The last time a user clicked a notification
2. What notification topics users click
3. How many times they are clicking that topic notification

With OneSignal, you can track this behavior using data tags, adding some code to your site or app, and sending notifications with a topic We’ve outlined the steps to achieve this in our [Tag with Notification Data documentation](./segment-based-on-notification-clicks).

Tagging with Notification allows you to segment and re-engage your users with content you already know they want.

## Leveraging push and in-app for effective re-engagement

The more a customer visits your site or app, the more likely they will be to engage with and share your news, thereby increasing traffic to your site. Additionally, the more people feel appreciated by and engaged with your site or app, the more they are likely to remain loyal and recommend you to others, which helps your site traffic grow. Customer or user re-engagement is key to any sound news/media strategy.

Luckily, push messaging and in-app messaging are perfect to leverage for re-engaging users who have previously engaged with your app or website.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/uh66akjYclI?si=XjmTa69ZGScwwZA7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Re-engage users effectively in 2 steps

<Steps>
  <Step title="Establish timeframes for inactivity">
    We first recommend establishing some set timeframes for inactivity (the amount of days that the user hasn’t visited your site or app) that you can use to schedule messaging around. For example, timeframes we typically recommend include:

    * Inactive for 7 Days
    * Inactive for 14 Days
    * Inactive for 30 Days
  </Step>

  <Step title="Set up a Journey to message users based on inactivity">
    Leveraging the OneSignal [Journeys feature](./journeys-overview) makes automating re-engagement campaigns simple and easy - it will automatically message users according to your desired re-engagement inactivity, with your preferred messaging.

    We recommend setting up a Journey with an audience for one of the inactivity segments to encourage your users to come back to your site/app. Effective re-engagement messaging that can entice your users to come back includes:

    <Columns cols={2}>
      <Card icon="newspaper">
        Recent breaking news
      </Card>

      <Card icon="list">
        * Recent content from one of their categories of interest
      </Card>

      <Card icon="gift">
        * Limited time offers to access any paywalled content
      </Card>

      <Card icon="tags">
        * Discounts to paid memberships
      </Card>
    </Columns>

    Creating a tailored re-engagement strategy for when and how to engage users can increase **traffic and improve retention by as much as 20%**.
  </Step>
</Steps>

***

Built with [Mintlify](https://mintlify.com).
