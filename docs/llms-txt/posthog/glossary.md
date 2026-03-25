# Source: https://posthog.com/docs/glossary.md

# Glossary - Docs

PostHog is an incredibly broad platform, with many distinct features and tools. As a result, it's hugely powerful -- but can be overwhelming if you're new to product analytics. So, we've created a glossary to explain many of the most common terms and acronyms. If a term is specific to PostHog then it's marked with a [hedgehog](/manual/glossary.md#hedgehog) 🦔 to help reduce confusion.

[A](/manual/glossary.md#a) • [B](/manual/glossary.md#b) • [C](/manual/glossary.md#c) • [D](/manual/glossary.md#d) • [E](/manual/glossary.md#e) • [F](/manual/glossary.md#f) • [G](/manual/glossary.md#g) • [H](/manual/glossary.md#h) • [I](/manual/glossary.md#i) • [J](/manual/glossary.md#j) • [K](/manual/glossary.md#k) • [L](/manual/glossary.md#l) • [M](/manual/glossary.md#m) • [N](/manual/glossary.md#n) • [O](/manual/glossary.md#o) • [P](/manual/glossary.md#p) • [Q](/manual/glossary.md#q) • [R](/manual/glossary.md#r) • [S](/manual/glossary.md#s) • [T](/manual/glossary.md#t) • [U](/manual/glossary.md#u) • [V](/manual/glossary.md#v) • [W](/manual/glossary.md#w) • [X](/manual/glossary.md#x) • [Y](/manual/glossary.md#y) • [Z](/manual/glossary.md#z)

## A

#### Action 🦔

Actions in PostHog are a way to organize [events](/manual/glossary.md#event) into a different format. In their simplest form actions consist of one or more events which have been given a new name - usually a descriptive title, such as 'Viewed Glossary Page\`. [Find out more about actions in PostHog](/docs/data/actions.md).

#### Active user

Active users are the people who currently use your product. A user who becomes inactive may have [churned](/manual/glossary.md#churn).

#### Alias 🦔

A related user account. In PostHog, aliases can be used to connect two user accounts (and their data). For example, combining the data of an anonymous user with their signed up account. See more in [identifying users](/docs/integrate/identifying-users.md).

#### Annotation 🦔

Annotations are short text notes you can apply to your data to help you understand context at a later point, or to signal important context to others. A common use for annotations it to add them shared charts and mark important events, such as feature releases or new marketing activiity. [Find out more about annotations in PostHog](/manual/annotations.md).

#### App 🦔

Apps are additional features or functionality built on top of PostHog. They are commonly used to integrate PostHog with other platforms, modify events or enhance PostHog's functionality. Apps may be built by the PostHog team, or by the community. You can [browse the app library](/apps.md) to see what's available, or [find out more in the docs](/docs/apps.md). Formerly known as plugins.

#### App chain 🦔

In PostHog, the output of one app can impact the actions of the next app to create a chain. This makes it crucial to understand the order in which apps run. [Find out more about app chains in the docs](/docs/apps/build.md).

#### ARR

Annual recurring revenue - basically how much revenue you expect to make each year.

#### Autocapture

The ability to capture user behavior (events, pageviews) automatically, without having to implement dedicated instrumentation. PostHog enables you to [autocapture](/docs/data/autocapture.md) data by using our [JavaScript web library or snippet](/docs/libraries/js/features.md#capturing-events).

#### A/B test

A/B tests are when you test two versions of an idea by serving each version to portion of your userbase, so you can monitor which performs best. If you're using more than two versions, it's a [multivariate test](/manual/glossary.md#multivariate-test). PostHog can do both, via [Experiments](/manual/experimentation.md).

## B

#### B2B

Business to business. It's when you make money by selling things or services to other businesses, rather than to individual users. Tools such as [Group Analytics](/manual/group-analytics.md) are especially important for B2B users in PostHog.

#### B2C

Business to customer. It's when you make money by selling things or services to individual customers, rather than to other businesses. Tools such as [experiments](/manual/experimentation.md) are especially important for B2C users in PostHog.

#### BAA

Business Associate Agreement, or also known as a Business Associate Contract. It's a legal document signed by contractors who may have to handle [personal health information](/manual/glossary.md#PHI) in order to agree to and satisfy the requirements of [HIPAA](/manual/glossary.md#HIPAA). [Find out more about PostHog and HIPAA](/docs/privacy/hipaa-compliance.md).

#### Bounce rate

A bounce is a session where the user only had one pageview, no autocaptures, and spent less than 10 seconds on the page. Your bounce rate is the percentage of sessions that resulted in a bounce. Used on the [web analytics dashboard](/docs/web-analytics/dashboard.md).

## C

#### CAC

Cost of acquisition. The amount spent on marketing, promotion, or advertising to acquire a customer. You can calculate CAC using the formula `Amount of money spent on customer acquisition / number of customers acquired`.

#### Chart

A graph or visual representation of data such as trend, bar, pie. In PostHog, charts often appear in [insights](/manual/glossary.md#insight). [Trend](/manual/glossary.md#trend) insights can have multiple [chart types](/manual/trends.md#chart-types).

#### Churn

When a user stops using your product and is no longer considered to be an [active user](/manual/glossary.md#active-user). The speed at which users churn is known as your *churn rate* and, if it is greater than the rate at which you acquire new customers then your product is in decline.

#### ClickHouse

ClickHouse is an [open source](/manual/glossary.md#open-source), column-oriented database. [We like it a lot and use it to power PostHog](/docs/how-posthog-works/clickhouse.md).

#### Cloud

Computing infrastructure, power, services, or storage hosted for on-demand usage with less required user setup and maintenance. You can choose to host your instance of PostHog in the cloud by choosing PostHog Cloud, instead of [self-hosting](/manual/glossary.md#self-host).

#### Cohort

Cohorts are groups of users in PostHog, created using the Cohorts tool. Cohorts can be created as either a static list, or a dynamic list which continues to update. Cohorts and [groups](/manual/glossary.md#groups) are similar, but [not the same](/manual/group-analytics.md#groups-vs-cohorts).

#### Contributor 🦔

As an [open source](/manual/glossary.md#open-source) company, PostHog enables anyone to add to our codebase or to submit ideas, either as [issues](/manual/glossary.md#issue) or [PRs](/manual/glossary.md#pull-request). When someone does this, they become a contributor and can earn rewards such as [merch](https://merch.posthog.com), invitations and public thank yous. Sometimes, they even [get hired](/careers.md). We love our contributors - [check them out](/contributors.md)!

#### Conversion

Conversion is when a user of your product changes into a new, usually more desirable, state. For example, converting from a lead into an [active user](/manual/glossary.md#active-user). You can use tools such as [funnels](/manual/funnels.md) to track users who convert between states.

#### Compliance

The act of complying with laws or regulations such as [HIPAA](/manual/glossary.md#HIPAA) or \[GDPR\](\](/manual/glossary#GDPR). [Find out more about how to use PostHog in compliance with common regulations](/docs/privacy.md).

#### CPA

Cost per Acquisition. How much it costs you to acquire users through an advertising campaign using the formula `Cost of the campaign / number of successful conversions`. \\

#### CTA

Call to Action. A message intended to elicit an action in your users, like this one: [Star PostHog on GitHub!](https://github.com/PostHog/posthog)

#### CTR

Click-through Rate, or what proportion of users which saw a CTA actually clicked it. CTR is usually a good measure of [engagement](/manual/glossary.md#engagement).

## D

#### Dashboard

Dashboards in PostHog enable you to save multiple useful pieces of information, such as [insights](/manual/glossary.md#insights), into one place. This makes it easier to collaborate, as you can share dashboards with others in many different ways. [Find out more about Dashboards in the docs](/manual/dashboards.md).

#### Data lake

A data lake is a system for storing raw data. The data stored in a data lake is usually for an ambiguous or unknown purpose, but the style of storage means all data is easily accessible to seasoned professionals and can be quickly updated.

#### Data warehouse

A data warehouse is a system for storing processed data. The data that's stored in a data warehouse is usually for a specific, known purpose and is in constant use. As a result, the data is highly accessible but it can be slow and costly to make infrastructure changes.

#### DAU

Daily Active Users. Basically, how many [active users](/manual/glossary.md#active-users) you have each day. [You can track this in PostHog using a simple trends chart.](/manual/trends.md)

#### Dormant user

In PostHog's [lifecycle insight](/manual/lifecycle.md) a dormant user is one who did not complete the specified action within the currently viewed period, but had completed it in the previous period.

## E

#### Engagement

In product and marketing terms, engagement is how involved or active someone is with your product. A regular user would be said to have *high* engagement, or to be highly engaged.

#### Event 🦔

Events are the core building block of PostHog. Any activity a user does, such as clicking a button or viewing a page, is an event. Events are [ingested](/manual/glossary.md#ingestion) into PostHog, and sometimes organized as [actions](/manual/glossary.md#actions).

## F

#### Feature flag

Feature flags are used to divide users into two groups - those for whom the flag is enabled, and those for whom the flag is disabled. Based on this flag status, users are served a version of the product where a specific feature is, or isn't, available. [Find out more about feature flags in the docs](/manual/feature-flags.md).

#### First-party cookies

Every time you visit a website or view content from a website, you are served a `cookie` - a data packet which contains information on your visit. First-party cookies are those which are served by the website operator and are typically used to store only user preferences. Users who self-host PostHog are able to collect additional information through their first-party cookie because PostHog is also deployed onto their servers. See also: [third-party cookies](/manual/glossary.md#third-party-cookies)

#### Formula 🦔

An equation or calculation that modifies data from one or more series.

#### FOSS

Free Open Source Software. FOSS products are exactly as they are described: free, and open source. [PostHog has a FOSS version too!](https://github.com/PostHog/posthog-foss)

#### Funnel

A funnel is a concept used to track users through a series of actions, such as from pageview to registration and login. In PostHog, you can use [the funnel insight](/manual/funnels.md) to track how many users move through each stage, and where drop-offs occur.

## G

#### GDPR

General Data Protection Regulation. GDPR is a regulation within the EU which governs how data must be processed, protected and kept private - notably by keeping it on servers within EU jurisdiction. [Find out more about complying with GDPR while using PostHog](/docs/privacy/gdpr-compliance.md).

#### Groups

Groups in PostHog enable you to aggregate events by anything other than an individual user, such as a company, team, device, project or pricing tier. [Groups are different to cohorts](/manual/group-analytics.md#groups-vs-cohorts) and can be used for [group analytics](/manual/group-analytics.md).

#### GTM

Go-to Market. In short, it's the plan you have for how you will bring a new product or feature to market, often building in intelligence on your users gained from product analytics.

## H

#### Heatmap 🦔

Heatmaps enable you to visualize user activity as an overlay on top of the page, with warmer colours used to represent where the most activity takes place. In PostHog, heatmaps are used to track where users click. Find out more about [PostHog heatmaps](/manual/toolbar.md), which are enabled via the [toolbar](/manual/glossary.md#toolbar).

#### Hedgehog

Incredibly cute creatures which are sadly becoming increasingly rare around the world. Hedgehogs are recognisable for their prickly backs, dislike of badgers and [ever-changing fashion habits](/blog/drawing-hedgehogs.md). PostHog's mascot is [a hedgehog called Max](/max.md), who was designed by [our Graphic Designer, Lottie](/blog/posthog-first-five.md#4-lottie-coxon).

#### HIPAA

Health Insurance Portability and Accountability Act. It's a piece of legislation in the US which covers, among other things, how [personal health information](/manual/glossary.md#PHI) must be handled. [Find out more about how to use PostHog in a which complies with HIPAA regulations](/docs/privacy/hipaa-compliance.md).

## I

#### Identify

The process of collecting, connecting, and combining data to a user. Also the process of de-anonymizing a user with [properties](/manual/glossary.md#property).

#### Ingestion

The process of getting the [events](/manual/glossary.md#events) users trigger into PostHog, regardless of whether the data is [current](/docs/integrate/ingest-live-data.md) or [historic](/docs/integrate/ingest-historic-data.md).

#### Insights 🦔

Insights are a core feature of PostHog which enable you to query analytics and derive visualized results. [Funnels](/manual/funnels.md), [trends](/manual/trends.md), [path analysis](/manual/paths.md) and more are all examples of PostHog insights.

#### Internal users

Users within your team. Often you'll want to remove internal users from your analysis to avoid swaying results with biased data. [Find out how to filter internal users from your PostHog insights](/tutorials/filter-internal-users.md).

#### Issues

What we use to log bugs, discuss ideas and make decisions on Github. Issues are better than a [community question](/posts.md), but worse than a [pull request](/manual/glossary.md#pull-request).

## J

> We couldn't think of anything which begins with a J. If you can think of something which should go here, let us know by [making a GitHub issue](https://github.com/PostHog) or join [our community page](/posts.md).

## K

#### K Factor

A metric for understanding the virality of your product. You can calculate your K factor by figuring out the number of invitations or recommendations about your product which users make, then multiplying it by the success rate of those invitations or recommendations. Any result greater than 1 indicates viral growth, as every user you acquire will, on average, successfully invite another.

#### KPI

Key Performance Indicator. A measurable metric which enables you to judge the success (or failure) of a person, team or product. Typically, teams may have multiple KPIs they are accountable for.

## L

#### LTV

Lifetime Value. The total amount of revenue you get from the average user before they [churn](/manual/glossary.md#churn), calculated using the formula `number of users / total revenue`.

## M

#### MAU

Monthly [Active Users](/manual/glossary.md#active-users). Essentially, how many users you have using your product each month.

#### MOM

Month-on-month or month-over-month. Normally this is used to track your performance from one month to the next, e.g. "We grew revenue 10% month-on-month".

#### MQL

Marketing Qualified Lead. A person who has indicated interest in a product based on activities taken by the marketing department, such as adverts or downloading marketing content. See also: [PQL](/manual/glossary.md#pql)

#### MRR

Monthly Recurring Revenue - basically how much revenue you expect to make each month.

#### Multivariate test

An [A/B test](/manual/glossary.md#a/b-test) which runs with more than two possible variants. You can run multivariate tests in PostHog using the [experimentation suite](/manual/experimentation.md).

#### MVP

Minimum Viable Product. In other words, the simplest (and usually cheapest and fastest) version of something which you can build to test an idea. We build a *lot* of MVPs.

## N

#### New user 🦔

In PostHog's [lifecycle insight](/manual/lifecycle.md) a New User is someone who was first identified within the specified period, and who did the investigated event in that same period.

#### North star

A single metric or objective which guides your decision making. Find out more about [how to set north stars and why they matter](/blog/north-star-metrics.md).

#### NPS

Net Promoter Score. A metric for understanding customer satisfaction and loyalty, based on asking users how likely they are to recommend your product, on a scale of 0 (not likely) to 10 (certainly likely). Users are then grouped into buckets based on their score - those who score 9-10 are labelled as Promoters, while those who score 0 to 6 are labelled as Detractors. Everyone else is labelled as Passive. By subtracting the percentage of Detractors from the percentage of Promoters, you determine an NPS score between -100 (very poor) and +100 (excellent).

## O

#### OKR

Objectives and Key Results. OKRs are, like [KPIs](/manual/glossary.md#kpi), a system for organizing team goals and measuring performance. Unlike KPIs, OKRs involve setting ambitious goals and judging performance in hitting them.

#### Open source

A model of distribution which involves giving others the ability to inspect, modify, and share what you create. PostHog is an example of both an open-source product, because [we distribute our software under an open source MIT license](https://github.com/PostHog/posthog), and [an open source company, because we work with transparency](/handbook/company/culture.md).

## P

#### Path 🦔

In PostHog, a path is a visualization of a users' activity achieved using the [path analysis insight](/manual/paths.md). Paths enable you to see, for example, all the pages which users who visited a particular page viewed afterwards.

#### Persons 🦔

In PostHog, persons are used to aggregate the behavior of an individual user, whether or not that user has been identified. [Find out more about Persons on PostHog](/manual/persons.md).

#### PHI

Personal Health Information. Regulations such as [HIPAA](/manual/glossary.md#hipaa) require that any information about an individual's health must be processed and store in accordance with law.

#### PII

Personal Identifying Information. Under some regulations, such as [HIPAA](/manual/glossary.md#HIPAA), any information which can be used to identify a user - such as their birthday, ethnicity, or address - must be processed in accordance with law.

#### Pipeline

A managed stream of data connecting data creation, modification, storage, and access.

#### Pivot

A rapid change in company direction. [One of our favourite hobbies](/blog/story-about-pivots.md).

#### Plugin

A way of adding extra functionality to PostHog, or integrating with other systems. We don't call them plugins anymore, though. We call them apps.

#### PQL

Product Qualified Lead. A PQL is a user who has expressed interest in your product based on actions which can be attributed to the product, such as completing a free trial or having experienced the direct value of the product.

#### Product analytics

Analytics services which focus on tracking identified *and* anonymous users and how they interact with your product. Product analytics services, such as PostHog, typically involve more detailed analysis tools than [web analytics](/manual/glossary.md#web-analytics) tools as a result of being able to focus on idenfitied users.

#### PR

Sometimes this means Public Relations and refers to working with journalists and members of the media. But when *we* say PR, we usually mean a [pull request](/manual/glossary.md#pull-request), because [we don't really do the other sort of PR outside of major announcements](/handbook/marketing.md).

#### Property

In PostHog, [events](/manual/glossary.md#events) and [persons](/manual/glossary.md#persons) contain additional information, called Properties. A property can be any information stored on the object, such as which device they are using or their geographic location. [Find out more about using properties in PostHog](/docs/how-posthog-works/queries.md).

#### Pull request

An event when someone makes a change to a piece of software. The best thing that anyone on PostHog's team can ever be doing.

## Q

#### Query

The process of asking a question using your data. Whenever you create an [insight](/manual/glossary.md#insight) you're running a query against your data. Find out more about [how querying works in PostHog](/docs/how-posthog-works/queries.md).

## R

#### Release Conditions

The users a [feature flag](/manual/glossary.md#feature-flag) is active for. For example, the internal team, or 50% of all users.

#### Retention 🦔

In PostHog, a retention insight is used to visualize how many users return to your product after first visiting it on a particular day. [Find out more about measuring retention on PostHog](/manual/retention.md).

#### Returning user 🦔

In PostHog's [lifecycle insight](/manual/lifecycle.md) a returning user is one who did the specified action within the current period *and* within the previous period.

#### Resurrecting user 🦔

In PostHog's [lifecycle insight](/manual/lifecycle.md) a resurrecting user is one who did the specified action within the current period *but not* within the previous period.

## S

#### SAML

Security Assertion Markup Language is a system which enables users to login to multiple systems with one set of credentials. [Find out more about SAML on PostHog](/manual/sso.md).

#### SDK

Software development kit. Tools for building and using a software platform. [PostHog has many SDKs available](/docs/integrate.md).

#### Segment

Segmentation is a way of dividing users into groups based on either demographic, geographic, behavioral or technographic properties.

#### Self-host

The ability to host and manage software yourself (on your own servers). PostHog provides the ability to [self-host](/docs/self-host.md).

#### Session

A period of time when users are [engaged](/manual/glossary.md#engagement) and interacting with your product. PostHog enables you to [capture sessions directly, as recordings](/manual/recordings.md).

#### SQL

Structured Query Language (pronounced "sequel"). A programming language for designing, building, and querying relational database management systems.

#### SSO

Single Sign-on is a system which enables users to login to a system (such as PostHog) using their access to another system (such as Google Workspace) as their credentials. [Find out more about SAML on PostHog](/manual/sso.md).

#### Stickiness 🦔

In PostHog, a stickiness insight enables you to see how many times users perform an action within a set period of time. [Find out more about measuring stickiness with PostHog](/manual/stickiness.md).

## T

#### Third-party cookies

Every time you visit a website or view content from a website, you are served a `cookie` - a data packet which contains information on your visit. Third-party cookies are those which are *not* served by the website operator and are instead served by third-parties, typically advertising companies. Users who self-host PostHog are able to collect additional information through [first-party cookies](/manual/glossary.md#first-party-cookies) because PostHog is also deployed onto their servers.

#### Toolbar 🦔

In PostHog, the toolbar is a widget in your browser that contains easy access to useful actions or information. PostHog's toolbar lets you easily inspect elements, view page \[heatmaps\]((/manual/glossary#heatmap), create [actions](/manual/glossary.md#actions), and toggle [feature flags](/manual/glossary.md#feature-flag). [Find out more about using the toolbar](/manual/toolbar.md).

#### Trend 🦔

In PostHog, a trend [insight](/manual/glossary.md#insight) is the default insight type and enables you to plot data from PostHog onto a [chart](/manual/glossary.md#chart). There are many different [chart types](/manual/trends.md#chart-types) and options which can be used when creating trend insights, including [formula](/manual/glossary.md#formula). Find out more about trend insights in PostHog.

## U

#### UGC

User Generated Content refers to any content which users create within, or using your product for the purpose of sharing with others. Posts on Instagram are a typical example of user-generated content.

#### UTM

Urchin Tracking Module. Essentially, a UTM are modifiers appended to an existing URL in order to aid attribution in marketing campaigns.

## V

#### Variants

Different versions of an experiment. In PostHog, variants are linked to [feature flags](/manual/glossary.md#feature-flag), which activate them.

#### VM

Virtual machine. An emulated and often isolated computing process. We use VMs to run [apps](/manual/glossary.md#app).

## W

#### Web analytics

Analytics services which focus on tracking anonymous users and how they interact with your content. Web analytics services, such as [Google Analytics](http://isgoogleanalyticsillegal.com), typically involve less detailed analysis tools than [product analytics](/manual/glossary.md#product-analytics) tools and cannot track user identities.

## X

> We couldn't think of anything which begins with an X. If you can think of something which should go here, let us know by [making a GitHub issue](https://github.com/PostHog) or join [our community page](/posts.md).

## Y

#### YOY

Year-on-Year. Normally this is used to track your performance from one year to the next, e.g. "We grew revenue 10% year-on-year".

## Z

> We couldn't think of anything which begins with a Z. If you can think of something which should go here, let us know by [making a GitHub issue](https://github.com/PostHog) or join [our community page](/posts.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better