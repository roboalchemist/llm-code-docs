# Source: https://docs.tokens.studio/fundamentals/design-tokens.md

# Intro to Design Tokens

## What is a Design Token?

You might be wondering: *"What is a Design Token?"*

The answer depends on who you ask.

*Watch this 1min video clip of Sam from the Tokens Studio team explains what a Design Token is "like I'm 5" during an interview with Sil from the Into Design Systems conference.*&#x20;

{% embed url="<https://youtu.be/c8wcfXtmxvI?feature=shared>" %}

#### The original definition

The concept of Design Tokens originated at Salesforce, where [Jina](https://bsky.app/profile/jina.social) and [Jon](https://www.linkedin.com/in/jonnylevine) coined the term. A good explanation can be found on [Jina Anne's Youtube](https://www.youtube.com/watch?v=q5qIowMyVt8)

> "Design tokens are the visual design atoms of the design system — specifically, they are named entities that store visual design attributes. We use them in place of hard-coded values (such as hex values for color or pixel values for spacing) in order to maintain a scalable and consistent visual system for UI development." -  [Salesforce, Lightning Design System](https://www.lightningdesignsystem.com/design-tokens/)

#### Tokens Studio definition

The Tokens Studio team broadly agrees with the below definition:

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F1Yuri2ro8B6vd3XD21wL%2Fdesign-token-ts.png?alt=media&#x26;token=4f0d8529-66ed-4ff5-9b3b-203350596db6" alt=""><figcaption></figcaption></figure>

The specifications for this common language can be found on the [**W3C community**](https://www.w3.org/community/design-tokens/) and business groups pages, which are managed by the [**Design Tokens Community Group**](https://www.designtokens.org/) (also referred to as DTCG throughout our docs).

### Design Tokens Community Group

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FGRLvOwlyLiIC7dtcofeG%2Fdtcg.png?alt=media&#x26;token=8dc38670-ae5c-4a0b-97d8-6357f8c5cb69" alt=""><figcaption></figcaption></figure>

A Design Token, according to the [DTCG W3C specifications](https://tr.designtokens.org/format/#introduction), is:

* a method to express design decisions
* platform-agnostic
* shareable across disciplines, tools, and technologies
* composed from a common vocabulary

Tokens Studio is working with the DTCG as they shape Design Token specifications. Our docs will highlight where and why our tools deviate from these specifications.

***

### Anatomy of a Design Token

A Design Token holds all the key pieces of information needed to communicate a design decision.

According to the Design Tokens Community Group (DTCG), a Design Token is made up of:

* **Name**: acts as the unique identifier of the design decision
* **Value**: the data for what was decided
* **Type**: the design property the decision applies to
* **Description** *(optional)*: additional context about the decision

Design Tokens live in JSON files. The DTCG specifications define this common language or how to format Tokens within their JSON files so they can be a shared source of truth across different tools and technologies.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FjRyC8tpjbSIWPMBStXXl%2Fflow-chart-common-language.png?alt=media&#x26;token=3139b0ce-69fb-4c80-8fad-c8aa5faf946b" alt=""><figcaption><p>Each anatomic part of a Design Token and how they connect the Common Language as defined by the Design Tokens Community Group. </p></figcaption></figure>

### Design Tokens are design decisions

This means that if you are thoughtful with how you structure your Design Tokens, you should understand the who, what, where, when, why, and how of every design decision at a glance.

These Design Decisions should be easily understood by everyone on your team - including engineers, other designers, stakeholders, and your future self!

This is what we mean when we say Design Tokens are a *shared source of truth* for design decisions shared across cross-functional teams.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FeisfZNr9R0TpK2wph0rp%2Fdesign-decisions-ws.png?alt=media&#x26;token=b2d80d23-6b0e-411e-aa99-37df6300c1ff" alt=""><figcaption><p>An illustrated analogy of the information captured by a Design Token. </p></figcaption></figure>

### Shared source of truth

When you sync Design Tokens to an external code repository, engineers can see your design decisions in code as platform-agnostic Tokens. Using a tool like [Style Dictionary](https://styledictionary.com/), they can transform the Design Tokens into any programming language or tool-specific code they need.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FUBCJ9HPBk3WoLlZQU8mS%2Ftransform-sd.png?alt=media&#x26;token=1af16a36-fd24-4747-89cc-baad38d3a510" alt=""><figcaption><p>The gecko represents Style Dictionary in this infographic. </p></figcaption></figure>

When Design Tokens are applied to design elements in our design tool of choice, engineers can easily see the Token representing the designer's decision and then pull the details of the Token directly from the code.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FuNg9eIRpwtg3QRYkbepN%2Ftokens-button-figma-properties.png?alt=media&#x26;token=e12c9b17-23f4-4c63-aced-ad72d4a178c5" alt=""><figcaption><p>Design Tokens can be applied to components or attached to reusable styles or variables in design tools.</p></figcaption></figure>

This reduces the time it takes to communicate and understand design decisions, as Designers and Developers are essentially "speaking the same language" and working with a shared source of truth that lives in code.

When digital products are built with Design Tokens, it creates the foundation for a CICD pipeline between design and development, dramatically reducing the engineering effort to implement design changes.

***

### Tools to work with Design Tokens

Tokens Studio provides a suite of tools that allow designers to produce engineer-ready code so they can easily share design decisions with engineers and cross-functional team members.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZtgP0mBIBjrIVy43uHfe%2Finfographic-tokenSet-JSON%402x.png?alt=media&#x26;token=08f564a8-5490-4707-9701-6bd96e9007a5" alt=""><figcaption><p>In Tokens Studio, a Token Set is the no-code version of a JSON file.</p></figcaption></figure>

### <img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FtKuPwv8t7niZBgM3vQ0z%2Flogo-icon-figma.png?alt=media&#x26;token=2825ec2d-66b9-4557-9704-04ff62543e1a" alt="" data-size="line">Tokens Studio Plugin for Figma

In Figma, the Tokens Studio Plugin provides a no-code interface to create and manage Design Tokens, connect Tokens to styles and variables, and easily sync to external code repositories for version control and a shared source of truth with engineers.&#x20;

→ [Learn more about the Plugin for Figma](https://tokens.studio/plugin)

### <img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F3852nSu5VIFicqhTJscu%2Flogo-icon-studio-platform.png?alt=media&#x26;token=d819cfdd-1046-4c14-9e5f-01afeee997fd" alt="" data-size="line">Tokens Studio Platform

For large organizations, agencies and freelancers, the Tokens Studio standalone platform provides powerful workflows that support integrations with other tools commonly used by cross-functional team members, including Framer, In Design, Blender, and PowerPoint, to name a few.

→ [Learn more about the Studio Platform, currently in Beta!](https://tokens.studio/studio)

### <img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FlhmnkvBSgiG2AcwO0azl%2Flogo-icon-penpot.png?alt=media&#x26;token=b4ecda67-1ee4-42af-aaa2-a88cdd6b3008" alt="" data-size="line">Native Design Tokens in Penpot

The Tokens Studio Team is collaborating with [Penpot](https://penpot.app/), an open-source alternative to Figma, to build a native solution to work with Design Tokens in a design tool.&#x20;

→ [Learn more about the Penpot and Tokens Studio collaboration.](https://tokens.studio/blog/bringing-design-tokens-to-penpot-an-open-source-collaboration-for-the-design-systems-community)

### <img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FqjdrKi1k2ZhKwrMyLK5t%2Flogo-icon-style-dictionary.png?alt=media&#x26;token=eab1eeb9-d432-4ce4-b1a5-684fa9fd9078" alt="" data-size="line">**Style Dictionary**

Style Dictionary is most popular tool for transforming Design Tokens into development-ready code. While Style Dictionary was created by Danny Banks at Amazon, in August 2023 the Tokens Studio team, lead by Joren Broekema, officially joined the effort to grow the functionality of Style Dictionary. \
\
→ [Read the Tokens Studio x Style Dictionary collaboration announcement here.](https://styledictionary.com/version-4/statement/)

***

### Summary

Design Tokens capture design decisions used to scale a design system, and they include all the important information engineers need to bring big ideas to life quickly.&#x20;

You can use Tokens Studio in design tools or a standalone platform to work with Design Tokens in a no-code interface, then sync your Token JSON files to an external code repository to create a shared source of truth with Engineers.&#x20;

Those JSON files can be transformed by Engineers using Style Dictionary into whatever programming needs are required for the project.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fb1Cs3X9gbVk3FCjFAIXE%2FTS-git-SD-multi-tool.png?alt=media&#x26;token=b74844f5-87c3-4be3-92b8-9f4a70beda83" alt=""><figcaption><p>Tokens Studio can share code files of Design Tokens between Designers and Developers in their tool of choice. Style Dictionary is represented by the Geko, and it is used to transform the tech-agnostic JSON files into usable code. </p></figcaption></figure>

***

### Up next - Token Anatomy

Now that you've got the basics of what a Design Token is and what Tokens Studio does, let's take a closer look at each anatomic part of a Token, starting with the Types of Tokens available to work with.

Then you'll learn about Token Values as they are dependent on the Token Type, and how you can use the Description to add additional context about your design decision.&#x20;

We've saved the "best" for last, as Token Names are the most customizable part of working with Design Tokens.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FlUA6Jb3068Bh3dRxUWlu%2Fanatomy-token-all.png?alt=media&#x26;token=772928d6-d18a-4c5b-afd1-9fb8f379704b" alt=""><figcaption><p>The four anatomic parts of a Design Token are next to code examples. Each part will be reviewed next. </p></figcaption></figure>

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
