# Source: https://quarkus.io/blog/adoptium-customer-story/

Title: Eclipse Adoptium Uses Quarkus for high volume Java SE distribution API

URL Source: https://quarkus.io/blog/adoptium-customer-story/

Markdown Content:
Eclipse Adoptium Uses Quarkus for high volume Java SE distribution API - Quarkus
===============

- [x] 

[![Image 1: Quarkus](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_600px_reverse.png)](https://quarkus.io/)

*   Why
    *   [WHAT IS QUARKUS?](https://quarkus.io/about)
    *   [DEVELOPER JOY](https://quarkus.io/developer-joy)
    *   [PERFORMANCE](https://quarkus.io/performance)
    *   [KUBERNETES NATIVE](https://quarkus.io/kubernetes-native)
    *   [STANDARDS](https://quarkus.io/standards)
    *   [VERSATILITY](https://quarkus.io/versatility)
    *   [CONTAINER FIRST](https://quarkus.io/container-first)
    *   [USING SPRING?](https://quarkus.io/spring)
    *   AI
        *   [AI OVERVIEW](https://quarkus.io/ai)
        *   [JAVA FOR AI](https://quarkus.io/java-for-ai)
        *   [WHY QUARKUS FOR AI](https://quarkus.io/quarkus-for-ai)
        *   [AI BLUEPRINTS](https://quarkus.io/ai-blueprints)

*   Learn
    *   [GET STARTED](https://quarkus.io/get-started)
    *   [DOCUMENTATION](https://quarkus.io/guides)
    *   [USER STORIES](https://quarkus.io/userstories/)
    *   ["Q" TIP VIDEOS](https://quarkus.io/qtips)
    *   [BOOKS](https://quarkus.io/books)

*   Extensions
    *   [BROWSE EXTENSIONS](https://quarkus.io/extensions/)
    *   [USE EXTENSIONS](https://quarkus.io/faq/#what-is-a-quarkus-extension)
    *   [CREATE EXTENSIONS](https://quarkus.io/guides/writing-extensions)
    *   [SHARE EXTENSIONS](https://hub.quarkiverse.io/)

*   Community
    *   [SUPPORT](https://quarkus.io/support/)
    *   [BLOG](https://quarkus.io/blog)
    *   [DISCUSSION](https://quarkus.io/discussion)
    *   [WORKING GROUPS](https://quarkus.io/working-groups)
    *   [PODCAST](https://quarkus.io/insights)
    *   [EVENTS](https://quarkus.io/events)
    *   [NEWSLETTER](https://quarkus.io/newsletter)
    *   [ROADMAP](https://github.com/orgs/quarkusio/projects/13/views/1)
    *   [BENEFACTORS](https://quarkus.io/benefactors)

*   [START CODING](https://code.quarkus.io/)
*    
    *   [OFFICIAL (ENGLISH)](https://quarkus.io/blog/adoptium-customer-story/)
    *   [PORTUGUÊS (BR)](https://pt.quarkus.io/blog/adoptium-customer-story/)
    *   [ESPAÑOL](https://es.quarkus.io/blog/adoptium-customer-story/)
    *   [简体中文](https://cn.quarkus.io/blog/adoptium-customer-story/)
    *   [日本語](https://ja.quarkus.io/blog/adoptium-customer-story/)

[Blog](https://quarkus.io/blog) Eclipse Adoptium Uses Quarkus for high volume Java SE distribution API

 September 15, 2021 [#user-story](https://quarkus.io/blog/tag/user-story)

Eclipse Adoptium Uses Quarkus for high volume Java SE distribution API
======================================================================

By ![Image 2](https://www.gravatar.com/avatar/0295b91cac6981b8bb87bf0d73dc0621)[James Falkner](https://quarkus.io/author/jfalkner)

![Image 3: Adoptium logo](https://quarkus.io/assets/images/posts/quarkus-user-stories/adoptium/adoptium-logo.png)

Java is used by [millions](https://www.daxx.com/blog/development-trends/number-software-developers-world) of developers worldwide and according to Redmonk, [recently moved](https://redmonk.com/sogrady/2021/08/05/language-rankings-6-21/) back to the #2 most used programming language. There are many distributions of the Java runtime and development kit, but the Eclipse Temurin (formerly known as AdoptOpenJDK) distribution has proven to be the [most popular](https://snyk.io/jvm-ecosystem-report-2021/). Recently, the AdoptOpenJDK project was moved into the Eclipse Foundation as [Eclipse Adoptium](https://adoptium.net/). The goal of Adoptium is to promote and support high-quality, TCK certified runtimes and associated technology for use across the Java ecosystem. It does this by performing regular builds, tests, certifications, and of course serving binaries to those millions of developers that need to evaluate, prototype, and run production workloads with Java. Like other open source Eclipse projects, the team behind the distribution API are mostly volunteers, so they are constantly looking for optimizations of their time and resources and technology used to deliver on their mission.

[](https://quarkus.io/blog/adoptium-customer-story/#the-challenge)The Challenge
-------------------------------------------------------------------------------

While developers can download distributions directly from the [Adoptium website](https://adoptium.net/) with a single click, it becomes more of a challenge to automate this process, for example in a CI/CD pipeline. This is especially true due to the number of variants of Java versions, release types, operating systems, architectures, JVM implementations, etc. To that end, Adoptium needed to offer a way to programmatically discover and access pre-built binaries based on these variables, and produced [an end-user API](https://api.adoptium.net/q/swagger-ui/).

The sheer volume of AdoptOpenJDK downloads, [about 500,000 per day](https://dash.adoptopenjdk.net/trends), meant that performance would become a key consideration for the API. In addition, Adoptium does not have a traditional datacenter, so all of this runs in the cloud on Microsoft Azure, where costs can increase when you have continuously running workloads that take up unnecessary space.

![Image 4: Download trends](https://quarkus.io/assets/images/posts/quarkus-user-stories/adoptium/download-trends.png)

Figure 1. Recent download statistics for Adoptium distributions, from [dash.adoptopenjdk.net](https://dash.adoptopenjdk.net/trends)

In 2017, the technical team’s first attempt at exposing an API was using Node.js + Express. As the request volume and number of distribution variants rose, the team found that the response times were getting slower, not only due to the volume, but also due to architectural choices made early on. In particular, the application’s monolithic architecture, where the frontend and backend were in the same app, would cause apparent slowness in the frontend, while the backend processed concurrent requests. In addition, lack of pagination in the API meant that requests could return huge results, even when only the first few elements of the result were needed.

The lead developer on the Technical Steering Committee responsible for the upkeep of the API explains:

> The existing API had design flaws that wouldn’t have been easy to fix, so we were considering replacing it with a new implementation. Our small team had more experience in JVM languages than JavaScript, and since this was an API serving Java data, we thought eating our own dogfood would be a good thing!
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

[](https://quarkus.io/blog/adoptium-customer-story/#enter-quarkus)Enter Quarkus
-------------------------------------------------------------------------------

In July 2019 the team discovered Quarkus through its related work with other frameworks in the Java ecosystem. They were especially interested in Quarkus’ promise of stellar performance and smaller footprint, which is comparable to Node.js and even Golang. Even better, Quarkus’ [first class support for Kotlin](https://quarkus.io/guides/kotlin) meant the team could re-use both their Java and Kotlin experience with Quarkus.

The team found Quarkus extremely easy to develop, especially the [Live Coding capability](https://quarkus.io/developer-joy#live-coding). The familiar JAX-RS APIs in Quarkus made it easy to create the necessary endpoints. The lead engineer explains further:

> We really liked the fact that Quarkus uses JAX-RS, which we were already familiar with. Having out-of-the-box integration with [RESTEasy reactive](https://quarkus.io/guides/resteasy-reactive) was a nice performance bonus, and the [OpenAPI extension](https://quarkus.io/guides/openapi-swaggerui) available in Quarkus made it pretty simple to expose the API as a Swagger API browser with no additional work needed.
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

Live Coding with Quarkus also proved extremely useful when developing the application:

> The live coding fast feedback loop was very useful when developing with Quarkus. Although fast startup was nice, it wasn’t critical since our apps are long-running, but during development, as we tweaked our APIs, being able to immediately re-test saved us a ton of development time.
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

The out-of-the-box performance of Quarkus on JVM exceeded their expectations quite easily:

> We initially wanted sub-second response times for most of the API, and be able to handle around 10 thousand requests per second. With zero optimizations, our app was responding within 1ms for most APIs, and easily surpassed our throughput requirements. This is way more than we will need for the foreseeable future. The Quarkus app also uses less than half the CPU time [compared to Node.js], despite handling more traffic and providing more functionality.
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

Overall, the move to Quarkus has been a very positive experience, with real benefits in terms of developer productivity and operational efficiency. The team has been using Quarkus in production for the Adoptium API since November 2019 and has proved to be extremely stable.

[](https://quarkus.io/blog/adoptium-customer-story/#an-active-community)An Active Community
-------------------------------------------------------------------------------------------

Communities are a critical aspect to any open source project’s success, including Quarkus. It is no surprise that the health of a community is a major consideration when an adoption decision must be made. For Adoptium, this is made clear by example:

> Earlier this year we discovered a memory leak in the RESTEasy Reactive component in Quarkus. Within a few days, working with the Quarkus community, we were able to identify and fix the issue. This gave us the confidence that longer term, we’ll be able to resolve issues quickly.
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

[](https://quarkus.io/blog/adoptium-customer-story/#whats-next-for-adoptium)What’s Next for Adoptium
----------------------------------------------------------------------------------------------------

Adoptium has been very happy with their decision to adopt Quarkus, and are looking forward to trying out new capabilities in Quarkus like continuous testing and dev services support for MongoDB (their database of choice).

> Overall, we have been very impressed with the capabilities of Quarkus, and our experience with the Quarkus community has been fantastic. We look forward to seeing how it evolves, and improving how we serve the Java community’s Java distribution needs for years to come!
> 
> 
> 
> **-Lead Developer on the Adoptium Technical Steering Committee**

[](https://quarkus.io/blog/adoptium-customer-story/#more-information)More Information
-------------------------------------------------------------------------------------

*   [Adoptium API](https://api.adoptium.net/q/swagger-ui/)

*   [Adoptium API Source code](https://github.com/adoptium/api.adoptium.net)

*   [Adoptium FAQ](https://adoptium.net/faq.html)

### [](https://quarkus.io/blog/adoptium-customer-story/#about-eclipse-adoptium)About Eclipse Adoptium

The mission of the Eclipse Adoptium Top-Level Project is to produce high-quality runtimes and associated technology for use within the Java ecosystem. Eclipse Adoptium also provides artifacts including open-source infrastructure as code, a comprehensive continuous integration build and test farm, and extensive quality assurance tests. These artifacts may be used by Eclipse Adoptium projects and other runtime technology builders to ensure the provision of secure, Java SE TCK-tested and compliant, production-ready runtimes.

[](https://www.linkedin.com/shareArticle?mini=true&url=https://quarkus.io/blog/adoptium-customer-story/&title=Eclipse%20Adoptium%20Uses%20Quarkus%20for%20high%20volume%20Java%20SE%20distribution%20API "Share on LinkedIn")[](https://x.com/intent/tweet?text=Eclipse%20Adoptium%20Uses%20Quarkus%20for%20high%20volume%20Java%20SE%20distribution%20API&url=https://quarkus.io/blog/adoptium-customer-story/&via=quarkusio&related=quarkusio "Share on X")[](https://facebook.com/sharer.php?u=https://quarkus.io/blog/adoptium-customer-story/ "Share on Facebook")[](http://www.reddit.com/submit?url=https://quarkus.io/blog/adoptium-customer-story/ "Share on Reddit")[](mailto:?subject=Eclipse%20Adoptium%20Uses%20Quarkus%20for%20high%20volume%20Java%20SE%20distribution%20API&body=Eclipse%20Adoptium%20Uses%20Quarkus%20for%20high%20volume%20Java%20SE%20distribution%20API%20https://quarkus.io/blog/adoptium-customer-story/ "Share via Email")

[![Image 5: Quarkus](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_reverse.svg)](https://quarkus.io/)

Quarkus is open. All dependencies of this project are available under the [Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0) or compatible license. [CC by 3.0](https://creativecommons.org/licenses/by/3.0/)

This website was built with [Jekyll](https://jekyllrb.com/), is hosted on [GitHub Pages](https://pages.github.com/) and is completely open source. If you want to make it better, [fork the website](https://github.com/quarkusio/quarkusio.github.io) and show us what you’ve got.

Navigation
*   [Home](https://quarkus.io/)
*   [About](https://quarkus.io/about)
*   [Blog](https://quarkus.io/blog)
*   [Podcast](https://quarkus.io/insights)
*   [Events](https://quarkus.io/events)
*   [Newsletter](https://quarkus.io/newsletter)
*   [User Stories](https://quarkus.io/userstories)
*   [Roadmap](https://github.com/orgs/quarkusio/projects/13/views/1)
*   [Security policy](https://quarkus.io/security)
*   [Usage](https://quarkus.io/usage)
*   [Brand](https://github.com/commonhaus/artwork/tree/main/projects/quarkus)
*   [Wallpapers](https://quarkus.io/desktopwallpapers)
*   [Privacy Policy](https://www.redhat.com/en/about/privacy-policy)

Follow Us
*   [X](https://x.com/quarkusio)
*   [Bluesky](https://bsky.app/profile/quarkus.io)
*   [Mastodon](https://fosstodon.org/@quarkusio)
*   [Threads](https://www.threads.com/@quarkusio)
*   [Facebook](https://www.facebook.com/quarkusio)
*   [Linkedin](https://www.linkedin.com/company/quarkusio/)
*   [Youtube](https://www.youtube.com/channel/UCaW8QG_QoIk_FnjLgr5eOqg)
*   [GitHub](https://github.com/quarkusio)

Get Help
*   [Support](https://quarkus.io/support)
*   [Guides](https://quarkus.io/guides)
*   [FAQ](https://quarkus.io/faq)
*   [Get Started](https://quarkus.io/get-started)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/quarkus)
*   [Discussions](https://github.com/quarkusio/quarkus/discussions)
*   [Development mailing list](https://groups.google.com/forum/#!forum/quarkus-dev)
*   [Quarkus Service Status](https://stats.uptimerobot.com/ze1PfweT2p)

Languages
*   [English](https://quarkus.io/)
*   [Português(Brasileiro)](https://pt.quarkus.io/)
*   [Español](https://es.quarkus.io/)
*   [简体中文](https://cn.quarkus.io/)
*   [日本語](https://ja.quarkus.io/)

Quarkus is made of community projects
*   [Eclipse Vert.x](https://vertx.io/)
*   [SmallRye](https://smallrye.io/)
*   [Hibernate](https://hibernate.org/)
*   [Netty](https://netty.io/)
*   [RESTEasy](https://resteasy.github.io/)
*   [Apache Camel](https://camel.apache.org/)
*   [Eclipse MicroProfile](https://microprofile.io/)
*   [And many more...](https://code.quarkus.io/)

[![Image 6](https://raw.githubusercontent.com/commonhaus/artwork/main/foundation/brand/svg/CF_logo_horizontal_single_reverse.svg)](https://www.commonhaus.org/)

 Copyright © Quarkus. All rights reserved. For details on our trademarks, please visit our [Trademark Policy](https://www.commonhaus.org/policies/trademark-policy/) and [Trademark List](https://www.commonhaus.org/trademarks/). Trademarks of third parties are owned by their respective holders and their mention here does not suggest any endorsement or association.
