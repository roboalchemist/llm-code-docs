# Source: https://docs.startree.ai/concepts/what-is-real-time-analytics.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Real-Time Analytics?

> Real-time analytics enable users to make better and more timely decisions. Real-time analytics products pull data in as soon as it happens, pull data out as soon as it gets pulled in, and do so at scale.

Many modern software or web applications offer analytics capabilities to their users. But what does it mean for those analytics to be real-time?

<iframe width="560" height="315" src="https://www.youtube.com/embed/1pZmafdvsmk" title="YouTube video player" allow="fullscreen; accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" />

*Tim Berglund explains Real-Time Analytics*

## Types of analytics

There are, broadly speaking, three types of analytics:

#### Dashboards and BI Tools

Normally used for internal purposes. BI Analysts are often the ones that are assessing this data.

#### User-Facing Analytics

Analytics that you provide to the end users of your software or web applications.

#### Machine Learning

Also referred to as machine-powered, or machine-fed analytics. These are when you feed analytics or events directly into your systems and then have your systems do the processing, automatically. Anomaly detection and fraud detection fit into this category, or any time a machine is generating insights without human interaction.

## Why is fresh data important?

When you're working with very large data sets that are constantly changing, you need to make sure the analytics that you have are based on the most recent data. Data gets outdated quickly and not having the freshest data can set you back in each of the type of analytics defined above.

* Dashboards need to be able to monitor the constant changes.
* You can build more interactive applications on top of this fresh data with actionable triggers for your end users. Organizations like LinkedIn provide their end users with real-time data through features like \_Who viewed my profile \_where a user can message other users upon seeing that they viewed their profile. Another example is in LinkedIn's news feed where a user can react, comment, or like a post as soon as they see it.
* For machine learning analytics you want your systems to know right away when something is happening, when there are changes in patterns or trends, so that you or your systems can take action.

## Building a real-time analytics system

What does it take to build a real-time analytics system? There are three requirements that these systems must satisfy:

### Speed of ingestion

Your application has data coming from a bunch of different sources, including batch and streaming sources. Streaming sources are built to pull new data as soon as it comes in. The data ingestion process needs to be really really fast. As soon as any changes happen, you should see this reflected in the real-time analytics system.

### Speed of queries

After you pull this data in, you need to make sure that the data can be queried as quickly as possible. If you're building dashboards, providing your end users with their own analytics, or feeding your data into some kind of machine learning algorithm, you need to make sure that all the freshly ingested data can be pulled out as quickly as it was pulled in.

### Scalability

Your system need to be able to handle a large number of queries run at the same time. It's not uncommon for real-time analytics systems to process 100s of thousands of queries per second.

Built with [Mintlify](https://mintlify.com).
