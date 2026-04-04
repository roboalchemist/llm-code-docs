# Source: https://www.jenkins.io/doc/book/blueocean/

Title: Blue Ocean

URL Source: https://www.jenkins.io/doc/book/blueocean/

Published Time: Sat, 14 Mar 2026 05:15:53 GMT

Markdown Content:
Blue Ocean
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
    *   [Getting started with Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/)
    *   [Creating a Pipeline](https://www.jenkins.io/doc/book/blueocean/creating-pipelines/)
    *   [Dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard/)
    *   [Activity View](https://www.jenkins.io/doc/book/blueocean/activity/)
    *   [Pipeline Run Details View](https://www.jenkins.io/doc/book/blueocean/pipeline-run-details/)
    *   [Pipeline Editor](https://www.jenkins.io/doc/book/blueocean/pipeline-editor/)

*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

[⇐ Pipeline](https://www.jenkins.io/doc/book/pipeline)

[Index](https://www.jenkins.io/doc/book/)

[Getting started with Blue Ocean ⇒](https://www.jenkins.io/doc/book/blueocean/getting-started)

Blue Ocean
==========

 Chapter Sub-Sections 

*   [Getting started with Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started)
*   [Creating a Pipeline](https://www.jenkins.io/doc/book/blueocean/creating-pipelines)
*   [Dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard)
*   [Activity View](https://www.jenkins.io/doc/book/blueocean/activity)
*   [Pipeline Run Details View](https://www.jenkins.io/doc/book/blueocean/pipeline-run-details)
*   [Pipeline Editor](https://www.jenkins.io/doc/book/blueocean/pipeline-editor)

Table of Contents

*   [What is Blue Ocean?](https://www.jenkins.io/doc/book/blueocean/#blue-ocean-overview)
*   [Frequently asked questions](https://www.jenkins.io/doc/book/blueocean/#frequently-asked-questions)
    *   [Why does Blue Ocean exist?](https://www.jenkins.io/doc/book/blueocean/#why-does-blue-ocean-exist)
    *   [Where is the name from?](https://www.jenkins.io/doc/book/blueocean/#where-is-the-name-from)
    *   [What does this mean for my plugins?](https://www.jenkins.io/doc/book/blueocean/#what-does-this-mean-for-my-plugins)
    *   [What technologies are currently in use?](https://www.jenkins.io/doc/book/blueocean/#what-technologies-are-currently-in-use)
    *   [Where can I find the source code?](https://www.jenkins.io/doc/book/blueocean/#where-can-i-find-the-source-code)

*   [Join the Blue Ocean community](https://www.jenkins.io/doc/book/blueocean/#join-the-blue-ocean-community)

This chapter covers all aspects of Blue Ocean’s functionality, including how to:

*   [get started with Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started), which covers how to set up Blue Ocean in Jenkins and access the Blue Ocean interface.

*   [create a new Pipeline](https://www.jenkins.io/doc/book/blueocean/creating-pipelines) project in Blue Ocean.

*   use Blue Ocean’s [dashboard](https://www.jenkins.io/doc/book/blueocean/dashboard).

*   use the [Activity view](https://www.jenkins.io/doc/book/blueocean/activity), where you can access [your current and historic run data](https://www.jenkins.io/doc/book/blueocean/activity#activity), your Pipeline’s [branches](https://www.jenkins.io/doc/book/blueocean/activity#branches), and any open [pull requests](https://www.jenkins.io/doc/book/blueocean/activity#pull-requests).

*   use the [Pipeline run details view](https://www.jenkins.io/doc/book/blueocean/pipeline-run-details) to access details such as console output, for a particular Pipeline or item run.

*   use the [Pipeline editor](https://www.jenkins.io/doc/book/blueocean/pipeline-editor) to modify Pipelines as code, which you can then commit to source control.

This chapter is intended for Jenkins users of all skill levels, but beginners may need to refer to the [Pipeline](https://www.jenkins.io/doc/book/pipeline/) chapter to understand some topics covered here.

For an overview of content in the Jenkins User Handbook, refer to [user handbook overview](https://www.jenkins.io/doc/book/getting-started/).

Blue Ocean status

Blue Ocean will not receive further functionality updates. Blue Ocean will continue to provide easy-to-use Pipeline visualization, but it will not be enhanced further. It will only receive selective updates for significant security issues or functional defects.

Alternative options for Pipeline visualization, such as the [Pipeline: Stage View](https://plugins.jenkins.io/pipeline-stage-view/) and [Pipeline Graph View](https://plugins.jenkins.io/pipeline-graph-view/) plugins, are available and offer some of the same functionality. While not complete replacements for Blue Ocean, contributions are encouraged from the community for continued development of these plugins.

The [Pipeline syntax snippet generator](https://www.jenkins.io/doc/book/pipeline/getting-started/#snippet-generator) assists users as they define Pipeline steps with their arguments. It is the preferred tool for Jenkins Pipeline creation, as it provides online help for the Pipeline steps available in your Jenkins controller. It uses the plugins installed on your Jenkins controller to generate the Pipeline syntax. Refer to the [Pipeline steps reference](https://www.jenkins.io/doc/pipeline/steps/) page for information on all available Pipeline steps.

[](https://www.jenkins.io/doc/book/blueocean/#blue-ocean-overview)What is Blue Ocean?
-------------------------------------------------------------------------------------

Blue Ocean as it stands provides easy-to-use Pipeline visualization. It was intended to be a rethink of the Jenkins user experience, designed from the ground up for [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/). Blue Ocean was intended to reduce clutter and increases clarity for all users.

However, Blue Ocean will not receive further functionality or enhancement updates. It will only receive selective updates for significant security issues or functional defects. If you are just starting out, you can still use Blue Ocean, or you may want to consider alternative options such as the [Pipeline: Stage View](https://plugins.jenkins.io/pipeline-stage-view/) and [Pipeline Graph View](https://plugins.jenkins.io/pipeline-graph-view/) plugins. These offer some of the same functionality.

To sum up, Blue Ocean’s main features include:

*   **Sophisticated visualization** of continuous delivery (CD) Pipelines, allowing for fast and intuitive comprehension of your Pipeline’s status.

*   **Pipeline editor** makes the creation of Pipelines more approachable, by guiding the user through a visual process to create a Pipeline.

*   **Personalization** to suit the role-based needs of each member of the team.

*   **Pinpoint precision** when intervention is needed or issues arise. Blue Ocean shows where attention is needed, facilitating exception handling and increasing productivity.

*   **Native integration for branches and pull requests**, which enables maximum developer productivity when collaborating on code in GitHub and Bitbucket.

If you would like to start using Blue Ocean, please refer to [getting started with Blue Ocean](https://www.jenkins.io/doc/book/blueocean/getting-started/).

[](https://www.jenkins.io/doc/book/blueocean/#frequently-asked-questions)Frequently asked questions
---------------------------------------------------------------------------------------------------

### [](https://www.jenkins.io/doc/book/blueocean/#why-does-blue-ocean-exist)Why does Blue Ocean exist?

The DevOps world has transitioned from developer tools that are purely functional, to developer tools being part of a "developer experience." It was no longer about a single tool, but the many tools developers use throughout the day, and how they work together to achieve a better workflow for the developer.

Developer tool companies like Heroku, Atlassian, and GitHub have raised the bar for what is considered a good developer experience. Gradually, developers have become more attracted to tools that are not only functional, but are designed to fit into their existing workflow seamlessly. This shift represents a higher standard for design and function, where developers are expecting an exceptional user experience. Jenkins needed to rise to meet this higher standard.

Creating and visualising continuous delivery Pipelines has always been something valuable for many Jenkins users. This has been demonstrated in the plugins that the Jenkins community has created to meet their needs. This also indicates a need to revisit how Jenkins currently expresses these concepts, and consider delivery pipelines as a central theme to the Jenkins user experience.

It is not just continuous delivery concepts, but the tools that developers use every day such as GitHub, Bitbucket, Slack, Puppet, or Docker. It is about more than Jenkins, as it includes the developer workflow surrounding Jenkins, which comprised multiple tools.

New teams can encounter challenges when learning how to assemble their own Jenkins experience. However, the goal to improve their time to market by shipping better software more consistently is the same. Assembling the ideal Jenkins experience is something we, as a community of Jenkins users and contributors, can work together to define. As time progresses, developers' expectations of a good user experience change, and the Jenkins project needs to be receptive to these expectations.

The Jenkins community has worked constantly to build the most technically capable and extensible software automation tool in existence. Not revolutionizing the Jenkins developer experience today could mean that a closed source option attempts to capitalize on this in the future.

Blue Ocean was created to meet such demands of its time. However, as time passed, more modern tools have cropped up to replace it. Now, the time has come for the rise of other plugins of similar functionality. Therefore, any new development or enhancement of Blue Ocean has ceased. If you are interested in contributing to a plugin which serves a similar purpose, you should consider the alternative options as suggested in **[What is Blue Ocean?](https://www.jenkins.io/doc/book/blueocean/#blue-ocean-overview)** section on above.

### [](https://www.jenkins.io/doc/book/blueocean/#where-is-the-name-from)Where is the name from?

The name Blue Ocean comes from the book [Blue Ocean Strategy](https://en.wikipedia.org/wiki/Blue_Ocean_Strategy). This strategy involves looking at problems in the larger uncontested space, instead of strategic problems within a contested space. To put this more simply, consider this quote from ice hockey legend Wayne Gretzky: "Skate to where the puck is going to be, not where it has been."

#### [](https://www.jenkins.io/doc/book/blueocean/#does-blue-ocean-support-freestyle-jobs)Does Blue Ocean support freestyle jobs?

Blue Ocean aims to deliver a great experience around Pipeline and compatibility with any freestyle jobs you already have configured in your Jenkins controller. However, you will not benefit from the features built for Pipelines, for example Pipeline visualization.

Blue Ocean was designed to be extensible, so that the Jenkins community could extend Blue Ocean functionality. While there will not be any further functionalities added to Blue Ocean, it still provides Pipeline visualization and other features that users find valuable.

### [](https://www.jenkins.io/doc/book/blueocean/#what-does-this-mean-for-my-plugins)What does this mean for my plugins?

Extensibility is a core feature of Jenkins and being able to extend the Blue Ocean UI is equally important. The `<ExtensionPoint name=..>` can be used in the markup of Blue Ocean, leaving places for plugins to contribute to the UI. This means plugins can have their own Blue Ocean extension points. Blue Ocean itself is implemented using these extension points.

Extensions are delivered by plugins as usual. Plugins must include some additional JavaScript to connect to Blue Ocean’s extension points. Developers that have contributed to the Blue Ocean user experience will have added this JavaScript accordingly.

### [](https://www.jenkins.io/doc/book/blueocean/#what-technologies-are-currently-in-use)What technologies are currently in use?

Blue Ocean is built as a collection of Jenkins plugins. The key difference is that Blue Ocean provides both its own endpoint for HTTP requests, and it delivers HTML/JavaScript via a different path, without using the existing Jenkins UI markup or scripts. React.js and ES6 are used to deliver the JavaScript components of Blue Ocean. Inspired by this excellent open-source project, which you can refer to in the [building plugins for React apps](https://nylas.com/blog/react-plugins) blog post, an `<ExtensionPoint>` pattern was established that allows extensions to come from any Jenkins plugin with JavaScript. If the extensions fail to load, their failures are isolated.

### [](https://www.jenkins.io/doc/book/blueocean/#where-can-i-find-the-source-code)Where can I find the source code?

The source code can be found on Github:

*   [Blue Ocean](https://github.com/jenkinsci/blueocean-plugin)

*   [Jenkins Design Language](https://github.com/jenkinsci/jenkins-design-language)

[](https://www.jenkins.io/doc/book/blueocean/#join-the-blue-ocean-community)Join the Blue Ocean community
---------------------------------------------------------------------------------------------------------

As the development of Blue Ocean has frozen, we do not anticipate or expect any new contributions made to its codebase for new features. However, there are still a few ways you can join the community:

1.   Chat with the community and development team on Gitter [![Image 1: blueocean plugin](https://badges.gitter.im/jenkinsci/blueocean-plugin.svg)](https://app.gitter.im/#/room/#jenkinsci_blueocean-plugin:gitter.im)

2.   Request features or report bugs against the [`blueocean-plugin` component in JIRA](https://issues.jenkins.io/).

3.   Subscribe and ask questions on the [Jenkins Users mailing list](https://groups.google.com/g/jenkinsci-users).

4.   Developer? We’ve [labeled a few issues](https://issues.jenkins.io/issues/?filter=16142) that are great for anyone wanting to get started developing Blue Ocean. Don’t forget to drop by the Gitter chat and introduce yourself!

* * *

[⇐ Pipeline](https://www.jenkins.io/doc/book/pipeline)

[Index](https://www.jenkins.io/doc/book/)

[Getting started with Blue Ocean ⇒](https://www.jenkins.io/doc/book/blueocean/getting-started)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/blueocean/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
