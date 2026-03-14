# Source: https://quarkus.io/blog/leyden-2/

Title: How we integrated Project Leyden into Quarkus

URL Source: https://quarkus.io/blog/leyden-2/

Published Time: Wed, 11 Mar 2026 22:38:08 GMT

Markdown Content:
How we integrated Project Leyden into Quarkus - Quarkus
===============

- [x] 

[![Image 1](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_600px_reverse.png)](https://quarkus.io/)

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
    *   [OFFICIAL (ENGLISH)](https://quarkus.io/blog/leyden-2/)
    *   [PORTUGUÊS (BR)](https://pt.quarkus.io/blog/leyden-2/)
    *   [ESPAÑOL](https://es.quarkus.io/blog/leyden-2/)
    *   [简体中文](https://cn.quarkus.io/blog/leyden-2/)
    *   [日本語](https://ja.quarkus.io/blog/leyden-2/)

[Blog](https://quarkus.io/blog) How we integrated Project Leyden into Quarkus

 March 05, 2026 [#performance](https://quarkus.io/blog/tag/performance)[#leyden](https://quarkus.io/blog/tag/leyden)

How we integrated Project Leyden into Quarkus
=============================================

By ![Image 2](https://www.gravatar.com/avatar/ec96387a1a8295b6fd6dffb68f80c352)[Guillaume Smet](https://quarkus.io/author/gsmet) , ![Image 3](https://www.gravatar.com/avatar/dd57c2732aea5fe7eb686d17cfe14b44)[Georgios Andrianakis](https://quarkus.io/author/geoand)

Quarkus has long supported both JVM and native image modes, each optimized for different trade-offs. Native image delivers unmatched startup and footprint. JVM mode offers peak throughput, dynamic capabilities, and a mature tooling ecosystem.

Quarkus continues to improve and work well with native-image, and lately Project Leyden enabled us to strengthen the JVM side of that equation.

We shared our excitement about Project Leyden and how it gave us a new perspective on Java application startup performance in a previous [blog post](https://quarkus.io/blog/leyden-1/).

In this post, we want to share our journey integrating Project Leyden into Quarkus, and how we made this integration both efficient and easy to use for our users.

[](https://quarkus.io/blog/leyden-2/#acknowledgements)Acknowledgements
----------------------------------------------------------------------

First, we would like to thank the OpenJDK team at IBM for their work on Project Leyden and for the many discussions we had with them, which were instrumental in helping us understand Leyden and determine how best to integrate it into Quarkus, namely (in alphabetical order), Maria Arias de Reyna Dominguez, Andrew Dinn, and Ashutosh Mehra.

More broadly, we would like to thank everyone contributing to Project Leyden.

Project Leyden is still evolving, and we look forward to seeing what they are preparing for Java 27 and beyond.

Finally, special thanks to Sanne Grinovero for introducing us to the Leyden team at just the right time, and for his insights and valuable feedback on our work.

[](https://quarkus.io/blog/leyden-2/#what-is-project-leyden)What is Project Leyden?
-----------------------------------------------------------------------------------

### [](https://quarkus.io/blog/leyden-2/#graalvm)GraalVM and the popularization of AOT in Java

In the Java world, Ahead-of-Time (AOT) compilation rose to prominence with the introduction of GraalVM native image, which compiles Java applications into native executables.

It made a huge impact on the Java ecosystem and was a game changer for Java application startup performance:

*   Startup time and memory footprint are significantly reduced.

*   There is no warmup phase, as the code is already compiled to native code. Performance is effectively at its peak from the start.

*   The resulting executable is small, leading to much smaller container images.

*   The Resident Set Size (RSS) memory usage is much smaller compared to a regular JVM application.

But this comes with some drawbacks:

*   Not all Java features and libraries are supported out of the box as they are on OpenJDK.

*   It relies on a closed-world assumption and removes most runtime dynamism (at least in its current form - work on the GraalVM side could change this in the future). Note: This was not and is not an issue for Quarkus as it makes the same assumption; it can be problematic for third-party libraries.

*   It introduces specific constraints, the most common being the need to provide explicit reflection configuration. These requirements add effort during development and testing, although they are minimized for Quarkus supported extensions.

*   Native image builds are significantly slower. This typically does not affect the inner development loop (except when debugging native-specific issues), but it can have a noticeable impact on CI resources.

*   Debugging native executables is hard. It has improved, but it is still a lot harder than debugging in the JVM as it requires the use of GDB and the presence of debug symbols in the build.

*   And since everything is AOT-compiled, there is no JIT compiler to optimize code at runtime, which can lead to suboptimal peak performance in some cases.

All in all, native image is an excellent option when startup time and footprint are the primary goals.

However, not all applications optimize for those dimensions. Some prioritize peak throughput, development velocity, debuggability, and compatibility with existing tooling. This is where Leyden becomes interesting, aiming to improve startup and footprint while staying closer to the traditional JVM model.

### [](https://quarkus.io/blog/leyden-2/#project-leydens-approach-to-aot)Project Leyden’s approach to AOT

Project Leyden addresses the same fundamental problem as GraalVM native image, but takes a different approach:

*   It is still "pure" Java, it is part of OpenJDK: your application runs on the JVM, with full access to Java features and libraries, without special configuration.

*   During a training phase, it records application behavior and gathers information such as loaded and linked classes, and in more recent versions also starts recording some JIT output - increasing scope and optimization potentials in each JVM version.

*   This information is stored in an AOT cache file.

*   At startup, you configure the JVM with this AOT cache file.

*   Because the application still runs on the JVM, you continue to benefit from the JIT compiler, your preferred garbage collector, and all other JVM optimizations, preserving the high throughput typically associated with the JVM.

The AOT cache is exactly that: a cache. If a class is not present in the cache, it is loaded and linked as usual.

Project Leyden reduces startup time by optimizing class loading and linking. It reduces warmup time by providing the JVM with profiling information, and will reduce it even further once compiled code itself is stored in the cache.

![Image 4: How Leyden works](https://quarkus.io/assets/images/posts/leyden-2/leyden.png)

Figure 1. How Leyden works

That said, Project Leyden is not magic either. In its current form:

*   Startup and warmup time improvements are significant, but not as substantial as with GraalVM/Mandrel native image.

*   You must train your application and generate the AOT cache. In practice, this is not difficult, and in Quarkus, we have made it as seamless as possible.

*   You still need to ship a JVM with your application.

*   You also need to ship the AOT cache, which means container images will be significantly larger than with native executables.

*   You don’t get any memory footprint benefit yet: in most cases, it’s comparable to a regular JVM.

Our take is that Project Leyden offers a compelling balance between performance and compatibility, at a very reasonable cost, and could become part of the default deployment workflow for many Java applications running on the JVM.

### [](https://quarkus.io/blog/leyden-2/#project-leyden-status)Project Leyden status

In OpenJDK 25, the following Project Leyden-related JEPs are available:

*   [JEP 483 - Ahead-of-Time Class Loading & Linking](https://openjdk.org/jeps/483)

*   [JEP 514 - Ahead-of-Time Command-Line Ergonomics](https://openjdk.org/jeps/514)

*   [JEP 515 - Ahead-of-Time Method Profiling](https://openjdk.org/jeps/515)

Together, these JEPs make Project Leyden fully usable starting with OpenJDK 25.

Additional JEPs are planned for OpenJDK 26 and beyond.

[](https://quarkus.io/blog/leyden-2/#project-leyden-in-quarkus)Project Leyden in Quarkus
----------------------------------------------------------------------------------------

Quarkus is a highly specialized framework, with extensive build-time processing and optimizations. Project Leyden is a specialized technology as well, with its own constraints and requirements.

Our goal was to integrate Project Leyden into Quarkus in a way that preserves what Quarkus does best, while also maximizing the benefits of Leyden.

Quarkus 3.32 includes the first version of our end-to-end Leyden integration. Let’s take a closer look at how it works.

### [](https://quarkus.io/blog/leyden-2/#aot-jar-packaging)AOT JAR packaging

You may be used to seeing your Quarkus application packaged in a `target/quarkus-app/` directory, but that wasn’t always the case. In the early days of Quarkus, we built a traditional runner JAR in `target/`, with dependencies placed in a `lib/` directory, much like most other Java frameworks.

The current default packaging in Quarkus is called `fast-jar`. One of its primary goals is to optimize class loading.

We achieved this by introducing our own class loader, which, for example, keeps a `package name` → `jar file` mapping in memory. It also includes additional optimizations, such as maintaining a full directory index for specific locations like `META-INF/services`. These are just a few examples of what this packaging does, but they should give you some context.

This packaging performs very well in the traditional JVM world, but it doesn’t play nicely with Project Leyden.

Project Leyden takes a conservative approach: it only caches classes loaded by the standard JDK class loaders. In other words, no custom class loaders are allowed if you want to fully benefit from AOT caching.

We hope that, at some point, this limitation will be lifted by the Leyden team. If that happens, we will return to the `fast-jar` packaging, or an evolution of it.

To be precise: you cannot use custom class loaders to load **classes** if you want to fully benefit from AOT caching. However, you can still use a custom class loader for loading **resources** only.

This is why we developed a dedicated packaging for Project Leyden: `aot-jar`. It is automatically selected when AOT is enabled, making the transition completely transparent. It uses the same file layout as the `fast-jar` packaging.

In addition to delegating all **class** loading to the JDK class loader, this packaging has a few specific characteristics:

*   It collects service descriptors from `META-INF/services`, aggregates them, and keeps them in memory.

*   It applies the same approach to Quarkus configuration files (e.g., `application.properties`).

*   It maintains a full index of specific directories (e.g., the root directory, `META-INF`, and `META-INF/services`).

*   It introduces a pre-initialization phase, during which selected elements are preloaded in parallel (e.g., the time zone database).

As this packaging format is new, we hope to gather feedback from real-world usage.

Let’s be clear: `aot-jar` performs worse than `fast-jar` when Project Leyden is not used.

It does not include all the optimizations of `fast-jar` and is intended to be used only in conjunction with Project Leyden. So it should not be used outside of this specific use case.

### [](https://quarkus.io/blog/leyden-2/#training-and-aot-cache-generation)Training and AOT cache generation

The AOT cache is only as good as the training data used to generate it. During the training phase, the JVM records which classes are loaded and linked, and collects method profiling data. The more representative the training workload, the more effective the resulting cache.

We wanted training to be as seamless as possible for Quarkus users. The natural fit was to leverage the existing integration test infrastructure: if you already have `@QuarkusIntegrationTest` tests, they can serve as the training workload.

When AOT training is enabled, the flow is as follows:

1.   Quarkus builds the application with the `aot-jar` packaging.

2.   The application starts with AOT training enabled.

3.   Integration tests run against the application, exercising its endpoints and features.

4.   The JVM captures profiling data during the entire test execution.

5.   An optimized `app.aot` cache file is generated from the recorded data.

This is both practical and effective: you already write integration tests to validate your application, and they also happen to produce somewhat realistic training data for the AOT cache.

Integration tests that use `@QuarkusIntegrationTest` make it very easy to run the target application as they use Dev Services.

### [](https://quarkus.io/blog/leyden-2/#integration-with-the-build-system)Integration with the build system

We wanted enabling Leyden in Quarkus to be a one-flag operation.

Setting `quarkus.package.jar.aot.enabled=true` is all it takes. Quarkus automatically switches to the `aot-jar` packaging and sets up the entire AOT pipeline.

With Maven, the full flow is a single command:

```bash
./mvnw verify -Dquarkus.package.jar.aot.enabled=true -DskipITs=false
```

This builds the application, runs integration tests with AOT training, and generates the `app.aot` cache file in `target/quarkus-app/`.

If you are using a project generated by our tooling, integration tests are disabled by default. Adding `-DskipITs=false` makes sure they will be run.

Running the application with the AOT cache is just as straightforward:

```bash
cd target/quarkus-app
java -XX:AOTCache=app.aot -jar quarkus-run.jar
```

We also integrated AOT with the container image extensions (Jib, Docker, and Podman). When building a container image with AOT enabled, Quarkus:

1.   Builds the application with `aot-jar` packaging.

2.   Creates a base container image.

3.   Runs integration tests against the container to train the AOT cache.

4.   Produces a final container image (with an `-aot` suffix in its version) that includes the AOT cache and is pre-configured to use it at startup.

This end-to-end integration means going from source code to an AOT-optimized container image in a single command.

[](https://quarkus.io/blog/leyden-2/#some-numbers)Some numbers
--------------------------------------------------------------

We’ve described the benefits of Project Leyden in theory, but how does it perform in practice?

To find out, we collected some numbers for two different Quarkus applications:

*   A simple REST application, the one you get when you run `quarkus create app`

*   A very large REST CRUD application: 1,000 entities, 1,000 repositories, 1,000 services, 1,000 REST endpoints…​ `9,000` .java files in total. This is an extreme case, don’t try this at home!

The container image sizes were measured using our default images, which are based on Red Hat’s UBI 9 Minimal and use JDK 25.

### [](https://quarkus.io/blog/leyden-2/#raw-numbers)Raw numbers

These numbers were obtained using a full recording of all classes loaded during startup. They were measured on our laptops rather than in an isolated lab environment. We plan to run a more comprehensive set of benchmarks in our lab soon.

Your results may vary for several reasons:

*   Not all classes required at startup were recorded.

*   Your application performs actual work during startup, Leyden only optimizes class loading, not application logic.

In any case, if you see unexpected results, we’re very interested in your feedback. Please reach out to us, and we’ll guide you on how to gather useful profiling information.

RSS is for Resident Set Size memory usage.

#### [](https://quarkus.io/blog/leyden-2/#small-rest-application)Small REST application

|  | Startup time | Diff | Container image size | Diff | RSS | Diff |
| --- | --- | --- | --- | --- | --- | --- |
| **Default fast-jar** | `370 ms` | `Reference` | `456 MB` | `Reference` | `122 MB` | `Reference` |
| **Project Leyden and aot-jar** | `80 ms` | `-78%` | `495 MB` | `+9%` | `103 MB` | `-16%` |
| **Mandrel native executable** | `17 ms` | `-95%` | `155 MB` | `-66%` | `37 MB` | `-70%` |

The AOT cache file is `39 MB` in size, the minimum you can expect for a Quarkus REST application.

#### [](https://quarkus.io/blog/leyden-2/#large-rest-crud-application)Large REST CRUD application

|  | Startup time | Diff | Container image size | Diff | RSS | Diff |
| --- | --- | --- | --- | --- | --- | --- |
| **Default fast-jar** | `3,189 ms` | `Reference` | `517 MB` | `Reference` | `580 MB` | `Reference` |
| **Project Leyden and aot-jar** | `924 ms` | `-71%` | `715 MB` | `+38%` | `580 MB` | `0%` |
| **Mandrel native executable** | `242 ms` | `-92%` | `244 MB` | `-53%` | `210 MB` | `-64%` |

The AOT cache file is `198 MB`, not surprising, given that the application contains 9,000 `.java` files.

### [](https://quarkus.io/blog/leyden-2/#startup-time)Startup time

Startup time is greatly improved by Leyden, both for small and very large applications. While it doesn’t quite match the startup speed of a native executable, the results are still impressive.

Let’s pause for a moment. **We were able to start a Quarkus REST application in the JVM in just `80 ms`**.

![Image 5: Starting fast](https://quarkus.io/assets/images/posts/leyden-2/quarkus-startup.png)

Figure 2. Quarkus starting fast!

Granted, it’s a simple REST application with a single endpoint, but it still relies on a full-featured REST implementation. And it runs in the JVM.

For very large applications, the results are just as impressive: **we were able to reduce startup time by `71%`**.

### [](https://quarkus.io/blog/leyden-2/#container-image-size)Container image size

It won’t come as a surprise: you also need to include the AOT cache file in your container image, so Leyden increases the image size.

For a Quarkus REST application, the minimum is around `40 MB`. The cache size grows as your application becomes larger.

On the other hand, going native significantly reduces the container image size, since you no longer need to include the full JVM.

### [](https://quarkus.io/blog/leyden-2/#memory-footprint)Memory footprint

In terms of RSS, Project Leyden does not significantly change the picture, while native executables offer a substantially lower memory footprint.

Reducing memory usage has not been a primary goal of Project Leyden so far, though this may evolve in the future.

### [](https://quarkus.io/blog/leyden-2/#lets-take-a-step-back)Let’s take a step back

At this point, you might be thinking: "Why not just go native for everything?". For all the reasons [we’ve outlined](https://quarkus.io/blog/leyden-2/#graalvm), use native when it makes sense for you.

There’s also the question of throughput. We haven’t collected throughput numbers ourselves, as we didn’t have the proper setup, but some of our colleagues are running tests in an isolated environment, and recently published [new benchmark results](https://quarkus.io/blog/new-benchmarks/). Native executables usually result in lower throughput, at least with what is available as Open Source today in Mandrel and GraalVM CE.

This is where Project Leyden really shines: you get significantly faster startup times compared to a regular JVM, while still retaining all the benefits of running on the JVM.

[](https://quarkus.io/blog/leyden-2/#whats-next-for-leyden-in-quarkus)What’s next for Leyden in Quarkus?
--------------------------------------------------------------------------------------------------------

Project Leyden is actively evolving, and we are closely tracking its developments, in particular via the premain branch of the OpenJDK Leyden repository, where experimental features are developed before being integrated into mainline JDK releases.

There are several areas where we expect things to improve:

*   Storage of JIT-compiled code in the AOT cache, which would further reduce warmup time.

*   Potential support for custom class loaders, which would allow us to return to the more optimized `fast-jar` packaging.

On the Quarkus side, we are also working on:

*   Testing and validating on additional platforms, including Windows.

As Project Leyden matures, we will continue to integrate new features into Quarkus. We are looking forward to what Java 27 and beyond will bring.

[](https://quarkus.io/blog/leyden-2/#conclusion)Conclusion
----------------------------------------------------------

After a month of experimenting and working on the integration of Project Leyden into Quarkus, we are very excited about the results and the potential of this technology. And we are very happy we were able to integrate it into Quarkus 3.32 so that you can play with it already.

Project Leyden is being continuously improved and is likely to figure prominently in the future of the Java platform. As part of our quest in Quarkus to provide the best development platform, with the help of the OpenJDK team at IBM, we are actively monitoring the progress made upstream (in the `premain` branch of [`git@github.com:openjdk/leyden.git`](https://github.com/openjdk/leyden/tree/premain)) and plan to continue shaping the Quarkus + Leyden experience accordingly.

With AOT support, Quarkus expands its runtime flexibility: plain JVM, Leyden-optimized JVM, and native image.

Rather than replacing one another, these modes form a spectrum of trade-offs. Native image remains unmatched for startup and minimal footprint. Leyden strengthens the JVM startup story.

Which works best depends on your priorities, constraints, and application workload.

Our commitment is unchanged: give developers the best option for their workload and keep improving each path.

[](https://quarkus.io/blog/leyden-2/#come-join-us)Come Join Us
--------------------------------------------------------------

We value your feedback a lot so please report bugs, ask for improvements…​ Let’s build something great together!

If you are a Quarkus user or just curious, don’t be shy and join our welcoming community:

*   provide feedback on [GitHub](https://github.com/quarkusio/quarkus/issues);

*   craft some code and [push a PR](https://github.com/quarkusio/quarkus/pulls);

*   discuss with us on [Zulip](https://quarkusio.zulipchat.com/) and on the [mailing list](https://groups.google.com/d/forum/quarkus-dev);

*   ask your questions on [Stack Overflow](https://stackoverflow.com/questions/tagged/quarkus).

[](https://www.linkedin.com/shareArticle?mini=true&url=https://quarkus.io/blog/leyden-2/&title=How%20we%20integrated%20Project%20Leyden%20into%20Quarkus "Share on LinkedIn")[](https://x.com/intent/tweet?text=How%20we%20integrated%20Project%20Leyden%20into%20Quarkus&url=https://quarkus.io/blog/leyden-2/&via=quarkusio&related=quarkusio "Share on X")[](https://facebook.com/sharer.php?u=https://quarkus.io/blog/leyden-2/ "Share on Facebook")[](http://www.reddit.com/submit?url=https://quarkus.io/blog/leyden-2/ "Share on Reddit")[](mailto:?subject=How%20we%20integrated%20Project%20Leyden%20into%20Quarkus&body=How%20we%20integrated%20Project%20Leyden%20into%20Quarkus%20https://quarkus.io/blog/leyden-2/ "Share via Email")

[![Image 6](https://quarkus.io/assets/images/quarkus_logo_horizontal_rgb_reverse.svg)](https://quarkus.io/)

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

[![Image 7](https://raw.githubusercontent.com/commonhaus/artwork/main/foundation/brand/svg/CF_logo_horizontal_single_reverse.svg)](https://www.commonhaus.org/)

 Copyright © Quarkus. All rights reserved. For details on our trademarks, please visit our [Trademark Policy](https://www.commonhaus.org/policies/trademark-policy/) and [Trademark List](https://www.commonhaus.org/trademarks/). Trademarks of third parties are owned by their respective holders and their mention here does not suggest any endorsement or association.
