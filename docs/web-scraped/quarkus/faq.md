# Source: https://quarkus.io/faq/

Title: FAQ

URL Source: https://quarkus.io/faq/

Markdown Content:
### Get answers to some of your common Quarkus questions.

[](https://quarkus.io/faq/#where-can-i-get-it)Where can I get it?
-----------------------------------------------------------------

Quarkus is published in Maven Central. We recommend you start your Quarkus experience with our [Getting Started guides](https://quarkus.io/get-started) or by downloading a scaffolded application from [code.quarkus.io](https://code.quarkus.io/).

[](https://quarkus.io/faq/#quarkus-is-stable)Quarkus is stable?
---------------------------------------------------------------

Yes, we consider Quarkus stable. Quarkus is used in production by a wide range of organizations (see some [user stories](https://quarkus.io/faq/blog/tag/user-story/)). Remember 95% of the features Quarkus apps use are provided by the ecosystem like Hibernate ORM, Eclipse Vert.x, Netty, RESTEasy, etc. These libraries are rock solid :)

You can go to [quarkus.io/extensions](https://quarkus.io/extensions) to see if a particular extension is _stable_ (default) or _preview_.

[](https://quarkus.io/faq/#what-is-a-quarkus-extension)What is a Quarkus extension?
-----------------------------------------------------------------------------------

One of the main goals of Quarkus is ease of extensibility and to build a vibrant ecosystem.

Think of Quarkus extensions as your project dependencies. Extensions configure, boot and integrate a framework or technology into your Quarkus application. They also do all of the heavy lifting of providing the right information to GraalVM for your application to compile natively. This will allow 3rd party projects to easily take advantage of the work we have done to make it easier to target GraalVM.

[](https://quarkus.io/faq/#what-are-the-extension-statuses)What are the extension statuses?
-------------------------------------------------------------------------------------------

Extensions have a various degree of maturity when they enter the Quarkus ecosystem. A status offers the expectations you can rely on.

**Stable**: backward compatibility and presence in the ecosystem are taken very seriously. An application can safely rely on these extensions. Extensions not marked as preview or experimental (the majority) are stable.

**Preview**: backward compatibility and presence in the ecosystem is not guaranteed. Specific improvements might require to change configuration or APIs and plans to become _stable_ are under way. Such extensions are in the middle of their maturation process.

**Experimental**: early feedback is requested to mature the idea. There is no guarantee of stability nor long term presence in the platform until the solution matures. Such extensions are at the beginning of their maturation process.

**Deprecated**: backward compatibility and presence in the ecosystem is not guaranteed. Such extensions are likely to be replaced or removed in a future version of Quarkus.

[](https://quarkus.io/faq/#will-the-quarkus-team-accept-my-extension)Will the Quarkus team accept my extension?
---------------------------------------------------------------------------------------------------------------

Oh yeah! We had quite a few extensions written outside the Quarkus "initial" team.

Quarkus is an open ecosystem and we hope to see all the extensions people need to write their apps. We are working as we speak to allow an extension to be published in separate repos and separate GAVs and thus published in Maven repos independently of Quarkus core. This will greatly simplify the publication process. Expect news soon.

The one current restriction is that extensions should work in both OpenJDK and GraalVM native executables. That is the guarantee we give Quarkus users (a cross compilation for their app). We have a [maturity model](https://quarkus.io/guides/extension-maturity-matrix) to improve an extension to be fully "Quarked" and benefit from Quarkus, all done in incremental steps. Just hop on our [mailing list](https://quarkus.io/community/#discussions) to discuss your ideas and get help. And you can start reading our [Writing extensions guide](https://quarkus.io/guides/writing-extensions) as well or more simply get inspiration from the [existing ones](https://quarkus.io/extensions).

[](https://quarkus.io/faq/#what-is-graalvm)What is GraalVM?
-----------------------------------------------------------

[GraalVM](https://www.graalvm.org/) is a universal virtual machine for running applications written in various different languages, as well as providing the ability to compile JVM bytecode to a native executable (this native executable runs a special virtual machine called SubstrateVM). These native executables start much faster and can use a lot less memory than a traditional JVM, however not every JVM feature is supported, and some are more limited than normal.

For example by default reflection in GraalVM will not work, unless a class/member has been explicitly registered for reflection. This is normally achieved by listing every class, method, field and constructor in a JSON file, and passing this as a parameter into the native image build. This obviously gets quite cumbersome for all but the most trivial projects. Quarkus provides a framework that makes it easy to work around these annotations, and programmatically determine what should be registered.
