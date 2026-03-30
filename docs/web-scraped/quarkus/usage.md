# Source: https://quarkus.io/usage

Title: Quarkus Usage Analytics

URL Source: https://quarkus.io/usage

Markdown Content:
Quarkus Usage Analytics - Quarkus
===============

- [x] 

[![Image 2: Quarkus](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_600px_reverse.png)](https://quarkus.io/)

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
    *   [OFFICIAL (ENGLISH)](https://quarkus.io/usage/)
    *   [PORTUGUÊS (BR)](https://pt.quarkus.io/usage/)
    *   [ESPAÑOL](https://es.quarkus.io/usage/)
    *   [简体中文](https://cn.quarkus.io/usage/)
    *   [日本語](https://ja.quarkus.io/usage/)

Quarkus Usage Analytics
=======================

### Help us make Quarkus even better, anonymously.

Why does Quarkus want to gather usage analytics?
------------------------------------------------

Usage analytics (telemetry collection) is invaluable for the Quarkus team and contributors to gauge which operating systems, java version, build systems, extensions and more are used. This service is provided by Red Hat and the details can be found on [usage policy](https://quarkus.io/usage/policy) page.

How will this work?
-------------------

In order to get this information, beginning in Quarkus 3.2, when you run Quarkus the first time in dev mode (
```plaintext
quarkus dev
```
, 
```plaintext
mvn quarkus:dev
```
, etc.) you get asked if you agree to contribute anonymous build data to the Quarkus community.

![Image 3: /assets/images/usage-prompt-arrows.png](https://quarkus.io/assets/images/usage-prompt-arrows.png)

By answering **“Yes”**, when you perform a quarkus build, anonymized data is sent to gather usage statistics on how Quarkus is being used and adopted.

However if you answer **“No”**, then no usage data is sent and you will not be asked again.

We will share what is learned from these anonymous usage data and plan on integrate things like usage and adoption into sites like [extensions.quarkus.io](https://extensions.quarkus.io/) and [code.quarkus.io](https://code.quarkus.io/).

How can I enable and disable ?
------------------------------

Build time analytics is not active by default. If you have opted in and would like to disable build time analytics or would like to later enable collection, you can do so in two ways:

### Set globally

You can manually configure the global settings by editing the 
```plaintext
io.quarkus.analytics.localconfig
```
 file in the 
```plaintext
.redhat
```
 folder of your user’s home directory.

#### To enable analytics collection

```
{"disabled":false}
```

#### To disable analytics collection

```
{"disabled":true}
```

### Set per build

You can configure it for a given build by using the 
```plaintext
quarkus.analytics.disabled
```
 system property:

*   To disable analytics collection, set 
```plaintext
quarkus.analytics.disabled
```
 to 
```plaintext
true
```
.
*   To enable analytics collection, set 
```plaintext
quarkus.analytics.disabled
```
 to 
```plaintext
false
```
.

For instance, when using Maven, you can disable analytics collection for a single run with:

```
./mvnw clean install -Dquarkus.analytics.disabled=true
```

[![Image 4: Quarkus](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_reverse.svg)](https://quarkus.io/)

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

[![Image 5](https://raw.githubusercontent.com/commonhaus/artwork/main/foundation/brand/svg/CF_logo_horizontal_single_reverse.svg)](https://www.commonhaus.org/)

 Copyright © Quarkus. All rights reserved. For details on our trademarks, please visit our [Trademark Policy](https://www.commonhaus.org/policies/trademark-policy/) and [Trademark List](https://www.commonhaus.org/trademarks/). Trademarks of third parties are owned by their respective holders and their mention here does not suggest any endorsement or association.
