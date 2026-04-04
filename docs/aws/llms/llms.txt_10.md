# Source: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/llms.txt

# Amazon Mechanical Turk Developer Guide

> Provides developers with an overview of Amazon Mechanical Turk and describes how to programmatically interact with the Mechanical Turk web service.

- [Set up Mechanical Turk](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/SetUpMturk.html)
- [Access Mechanical Turk](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/AccessMturk.html)
- [Get Started with Mechanical Turk](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/GetStartedMturk.html)
- [Retrieving results](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/RetrievingResults.html)
- [Retrieving HIT status](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/RetrievingHitStatus.html)
- [Use Mechanical Turk notifications](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_NotificationsArticle.html)
- [Use request tokens](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/RequestTokens.html)
- [CORS configuration requirement](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/MturkCorsConfig.html)

## [What is Amazon Mechanical Turk?](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/WhatIs.html)

- [Mechanical Turk marketplace](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/IntroMarketplace.html): Learn what the Mechanical Turk marketplace is and how workers use it to find your tasks.
- [Tasks that work well on Mechanical Turk](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/IntroTaskWorkWellMturk.html): Tasks that work well on Mechanical Turk have certain characteristics.
- [Core concepts](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/IntroCoreConcepts.html): Learn the core concepts that are used in the Amazon Mechanical Turk ecosystem.
- [Best practices](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/IntroBestPractices.html): Explore best practices for getting the most out of Amazon Mechanical Turk
- [Frequently asked questions](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/IntroFAQ.html): Use the following sections to get answers to frequently asked questions.


## [Creating and managing tasks (HITs)](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_HITsArticle.html)

### [Define questions](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions.html)

The central component of a task in Amazon Mechanical Turk (Mechanical Turk) is the interface you provide for workers to give you the data you need.

### [Use HTML to define questions](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html.html)

Because workers access tasks (HITs) on Amazon Mechanical Turk (Mechanical Turk) using a web browser, the most common approach for creating a task interface for Mechanical Turk is to use HTML, CSS, and JavaScript.

- [How Mechanical Turk tasks are rendered](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html-rendered.html): When a worker accepts a task in the Mechanical Turk marketplace, they are directed to a page for the assignment they've accepted.
- [Defining an HTML form](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html-define.html): The example below describes a simple HTML form that prompts workers to answer a single question.
- [Crowd HTML Elements](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html-crowd-html-elements.html): Crowd HTML Elements are web components, a web standard that abstracts HTML markup, CSS, and JavaScript functionality into an HTML tag or set of tags.
- [Templating](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html-templating.html): When using Mechanical Turk tasks it's common to use a template approach to reuse the same question definition on multiple tasks.
- [Submitting from JavaScript](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-html-javascript.html): In some cases, it's necessary to collect data using mechanisms other than form fields.
- [Question definitions](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-definitions.html): Mechanical Turk provides three XML schemas that you can use to define your questions:
- [Requester website layouts](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-web-layout.html): If you have an existing task you created using the Mechanical Turk requester website, you can create HITs by referencing the LayoutId for that task and avoiding the need to provide a question value.
- [HIT attributes](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-attributes.html): When you create a task (HIT) with Amazon Mechanical Turk (Mechanical Turk), you provide a number of attributes about the task that tell Mechanical Turk how to display it in the marketplace.
- [Creating HITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-creating-hits.html): A human intelligence task, or HIT, is a question your application asks and a worker answers.
- [Modifying HITs](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-modifying-hits.html): Once a HIT has been created in the Amazon Mechanical Turk (Mechanical Turk) marketplace, it's possible to modify it; however, there is an important caveat.
- [Using the sandbox](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-use-sandbox.html): Many requesters choose to test their Amazon Mechanical Turk (Mechanical Turk) tasks in the sandbox environment.
- [HIT references using RequesterAnnotation](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/HITReferences.html): When building processes that leverage Amazon Mechanical Turk (Mechanical Turk), it's often valuable to keep track of identifiers associated with the data in each HIT, particularly when handling HIT responses via notifications.


## [Managing workers](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/ManagingWorkers.html)

- [Approving and rejecting work](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/ApproveRejectWork.html): Before workers can receive payment for tasks you post to Amazon Mechanical Turk (Mechanical Turk), the work must be approved.
- [Awarding a bonus](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/AwardingBonus.html): You can send bonus payments to workers who have completed an assignment for you in Amazon Mechanical Turk (Mechanical Turk) in the past six months.
- [Blocking workers](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/BlockingWorkers.html): When you identify workers that are not putting in the requested effort on your tasks on Amazon Mechanical Turk (Mechanical Turk), you have the option to block them.
- [Selecting eligible workers](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/SelectingEligibleWorkers.html): By default, all tasks (HITs) posted to Amazon Mechanical Turk (Mechanical Turk) are available to all active workers in the Mechanical Turk marketplace.

### [Working with custom qualification types](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/WorkWithCustomQualType.html)

When using Amazon Mechanical Turk (Mechanical Turk), you can create qualification types that you can then assign to workers as qualifications.

- [Tutorial: Require workers to be in a group](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/CustomQualTutorialGroup.html): In the following example, we create a qualification type that describes a group of workers that have demonstrated expertise at a task and add it to our qualification requirements.
- [Tutorial: Require workers to meet accuracy level](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/CustomQualTutorialAccuracy.html): In the following example, we create a qualification type that we can use to record how well workers did on a previous set of tasks and then build a qualification requirement that requires them to have achieved at least 80% accuracy.
- [Tutorial: Exclude workers from selecting tasks](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/CustomQualTutorialExclude.html)
- [Communicate with workers](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/CommunicateWithWorkers.html): You can send messages to workers in Amazon Mechanical Turk (Mechanical Turk) if you've previously accepted or rejected an assignment from that worker using the NotifyWorkers operation.
