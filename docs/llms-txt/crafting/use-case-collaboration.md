# Source: https://docs.sandboxes.cloud/docs/use-case-collaboration.md

## Team Collaboration, Local or Remote

In this section, we will describe the use cases of Crafting for facilitate collaboration in development teams, no matter that are working in the same office or remotely across the globe.

Collaboration is always a key factor to the overall performance of development teams. A collaborative engineering team is able to output much more in much higher quality than a team with everyone working in silos. In recent years, there is an increasing trend for distributed development teams, which adds barriers for effective collaboration.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/10e60a7-use-case-collaboration.png" />

With Crafting, the whole team can leverage the online dev environments to collaborate much better no matter where they are. In the rest of this section, we are going to talk about several examples related to team collaboration:

* [Pair programming](#pair-programming)
* [Frontend backend integration](#frontend-backend-integration)
* [Live troubleshooting in context](#live-troubleshooting-in-context)
* [QA testing and feedback to developers](#qa-testing-and-feedback-to-developers)
* [Demo to customers](#demo-to-customers)

## Pair programming

Multiple developers sometimes need to work on a single piece of code in order to leverage each other's knowledge, brainstorm solutions, or simply avoid making mistakes in critical points. Traditionally it requires the developers to sit together looking at the same monitor, which can not happen with they work from different geographical locations.

With Crafting, the codebase is in an online workspace where all the developers from the same team can access simply using their own IDEs or even in a browser window with Web IDE. This way on Crafting platform, one developer can see the code modification live from their view and even make modification one after another.

## Frontend backend integration

For build a feature end-to-end, it often involves both frontend engineers and backend engineers working on their corresponding parts of the code. To make sure the code works well together, a frontend engineer often needs to have a backend version with the new APIs to support the feature. That sometimes becomes a problem when the frontend engineer is not really familiar about how to make the backend run properly. So he usually needs to wait for the backend feature making its way to staging or even production before being able to try it, adding significant delay. Furthermore, if there is any issue with the backend, the frontend engineers can get blocked and again needs to wait for a long time for the fix to slowly make to staging or production before resuming his work.

With Crafting, the backend engineer can create a version of sandbox with his code change and pass that to the frontend engineer before it's even merged to main branch. The frontend engineer can point the API calls to the sandbox version and work against that. If there is any issues with the API implementation, the backend engineers can modify the code in the sandbox live and iterate together with the frontend engineers quickly.

## Live troubleshooting in context

When a new developer joins a new project, he is not familiar with the codebase and is often hit by some issues that requires troubleshooting from a more experienced developer. In a distributed team, it is usually very hard to describe precisely what went wrong over emails and messages. At the same time, troubleshooting over a zoom call is painful and time consuming. As a result, it's not uncommon to have some team members get blocked frequently without timely troubleshooting and lose productivity.

With Crafting, one experienced engineer can hop on another engineer's dev environment and diagnose what exactly went wrong in the code and settings. The experienced engineer can see all the code and is able to run the code in the other engineer's environment to reproduce the problem. This live context makes troubleshooting much easier to perform from remote.

## QA testing and feedback to developers

Pre-production QA testing by a QA team is an important step to ensure correctness but it can be challenging to run smoothly. Not only that it's difficult for the remote QA team to create an on-demand environment that reflect the exact version of the product need testing, when the QA team finds an issue, it's often difficult for the developers to reproduce it in their environment in order to fix it.

With Crafting, the QA team can test against a sandbox that has the exact version of the product. When they hit some error, the whole environment including testing data can be snapshotted and sent to developers right at the failure point for debugging. The developer can reproduce the issue right in the environment and apply a fix. Then the whole sandbox can be passed back to QA for verification of the fix. It greatly reduces the communication gaps between developers and the QA team.

## Demo to customers

To sell a product to customers, the business people usually need to demo a version of the product specially made with a certain data set and specific features. It is not ideal to demo with the production version because the features to demo may be experimental and not ready for production. To make the matter worse, with new information becoming available, it is often desirable to have last minute changes made to the demo in order to make the best pitch.

With Crafting, the business development team can have dedicated environments tailored to each customer's use case, with customized data set and settings. And engineers can easily hop on these environments and make live changes and make it reflect immediately in the demo. Collaboration between business functions and developer can be made much smoother.
