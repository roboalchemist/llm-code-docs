# Source: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/llms.txt

# Amazon CodeGuru Profiler User Guide

> Provides a conceptual overview of Amazon CodeGuru Profiler, instructions for creating profile groups, using graphs and filters, reviewing recommendations, and exploring code.

- [What is Amazon CodeGuru Profiler?](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
- [Working with Amazon EventBridge](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-eventbridge.html)
- [Working with unsupported AWS Regions](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-unsupported-regions.html)
- [Working with anomalies and recommendation reports](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-recommendation-reports.html)
- [Troubleshooting](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/troubleshooting.html)
- [Quotas](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/quotas.html)
- [Document history](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/glossary.html)

## [Setting up](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up.html)

- [Set up in the Lambda console](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-short.html): You can use the following method to create a profiling group with your Lambda function.
- [Set up in the CodeGuru Profiler console](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-long.html)


## [Getting Started](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/getting-started.html)

- [Python sample application](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/tutorial-python.html): In this tutorial, youâll walk through the complete set up necessary to run Amazon CodeGuru Profiler within a sample application.
- [Java sample application](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/tutorial-java.html): This tutorial walks through the complete setup necessary to run Amazon CodeGuru Profiler within two sample applications: one that features issues to generate CodeGuru Profiler recommendations and one that does not.


## [Integrating with JVM](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/integrating-with-java.html)

### [Profiling your applications that run on AWS Lambda](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html)

To start CodeGuru Profiler in your application running on AWS Lambda, you can either update your Lambda function configuration or modify your application code.

- [All Java runtimes](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/lambda-custom.html): If you're profiling applications that run on AWS Lambda, add the following environment variables to your Lambda function.
- [Easier option for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto) runtimes](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/lambda-simple.html): You can enable CodeGuru Profiler from the AWS console by setting environment variables and updating configuration for your AWS Lambda function.
- [Enabling the agent from the command line](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/enabling-the-agent-with-command-line.html): The command line option for integrating the CodeGuru Profiler agent is the easiest way to start profiling your application, because it doesn't require recompiling and redeploying your application.

### [Enabling the agent with code](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/enabling-the-agent-with-code.html)

You can enable the Amazon CodeGuru Profiler agent in your application by adding code inside the startup routine of your application.

- [Java](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/java-language-support.html): You can add support for the CodeGuru Profiler agent into your Java application by adding the following lines into your startup or main function.
- [Scala](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/scala-language-support.html): You can add support for the CodeGuru Profiler agent into your Scala application by adding the following lines into your startup or main function.
- [Kotlin](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/kotlin-language-support.html): You can add support for the CodeGuru Profiler agent into your Kotlin application by adding the following lines into your startup or main function.
- [Groovy](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/groovy-language-support.html): You can add support for the CodeGuru Profiler agent into your Groovy application by adding the following lines into your startup or main function.
- [Jython](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/jython-language-support.html): You can add support for the CodeGuru Profiler agent into your Jython application by adding the following lines into your startup or main function.
- [JRuby](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/jruby-language-support.html): You can add support for the CodeGuru Profiler agent into your JRuby application by adding the following lines into your startup or main function.
- [Clojure](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/clojure-language-support.html): You can add support for the CodeGuru Profiler agent into your Clojure application by adding the following lines into your startup or main function.


## [Integrating with Python](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/integrating-with-python.html)

### [Profiling your applications that run on AWS Lambda](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda.html)

CodeGuru Profiler integration for AWS Lambda is currently available for applications that run on Python 3.7 up to Python 3.9.

- [Apply the CodeGuru Profiler function decorator to your handler function](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda-command-line.html): Pull your codeguru_profiler_agent dependency to your local environment through pip and include it in the .zip file for Lambda.
- [Use AWS Lambda layers](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda-layers.html): There are two ways you can use layers to enable CodeGuru in Lambda functions using Python.

### [Enabling the agent with code](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-code-change.html)

If your application runs on a platform other than Lambda, install codeguru_profiler_agent through pip.

- [Django](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-django.html): Start the profiler in your settings file.
- [Flask](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-flask.html): Start the profiler based on the configuration for your web server.
- [WSGI servers](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-wsgi.html): Start the profiler based on the configuration for your web server.
- [Enabling the agent from the command line](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-command-line.html): If your application runs on a platform other than Lambda, install codeguru_profiler_agent through pip.
- [Profiling Distributed systems](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-distributed-systems.html): Amazon CodeGuru Profiler offers limited support when implemented on distributed systems like Spark on EMR or Glue jobs running across clusters.
- [Enabling logs](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-enabling-logs.html): The Amazon CodeGuru Profiler agent uses the logging library.


## [Working with profiling groups](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups.html)

- [Creating a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups-create.html): Follow the steps in to create a profiling group, set permissions, and add CodeGuru Profiler profiling agent dependencies and startup code to your application.
- [Deleting a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups-delete.html): When you delete a profiling group, the profiling group and recommendations reports are deleted.


## [Working with visualizations](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations.html)

- [Accessing visualizations](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-accessing.html): The following instructions show you where to find the visualizations of your profiling group data in the CodeGuru Profiler console.
- [Types of visualizations](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-visualization-types.html): Amazon CodeGuru Profiler uses three types of visualizations to display profiling data collected from applications.

### [Exploring visualization data](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-exploring.html)

CodeGuru Profiler makes it easy to explore visualization data.

- [Choosing my code in visualizations](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-choosing-my-code.html): CodeGuru Profiler differentiates your code in the overview visualization, so you can quickly identify the methods you are working on.
- [Pausing over a frame](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-pause.html): One of the easiest ways to begin exploring visualization data is by pausing over the visualization.
- [Zooming in on a frame](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-zoom.html): Clicking a frame zooms in on the function.
- [Resetting zoom in a visualization](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-reset.html): You can zoom in to stack frames to view details.
- [Inspecting a frame](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-inspect.html): You can inspect frames that appear in many places in a visualization.
- [Understanding the dollar estimate of the CPU cost for frames](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-additional-info.html): Amazon CodeGuru Profiler provides an estimated dollar value for the active CPU cost of a frame.

### [Filtering visualization data](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-filtering.html)

This section contains information about how to filter profiling data.

- [Selecting and coloring thread states](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-thread-states.html): In a visualization view, you can filter profiling data by thread state.
- [Hiding a frame](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-hiding-frame.html): When you hide a frame, the visualization no longer shows that frame or its callee frames.
- [Selecting a custom time range](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-time-range.html): Information about how to select a time range for profiling data to visualize.
- [Understanding the summary page](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-summary-page.html): The Amazon CodeGuru Profiler summary page displays the status of your profiling group and relevant metrics gathered during profiling.
- [Understanding the heap summary](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-heap-summary.html): The Heap summary visualization shows your applicationâs heap usage over time.
- [Comparing two time ranges](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-visualizations-diff.html): The CodeGuru Profiler Compare option allows you to view differences between two different time ranges of the same profiling group.


## [Tagging profiling groups](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/tagging-profiling-groups.html)

- [Add a tag to a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/how-to-tag-profiling-group-add.html): Adding tags to a profiling group can help you identify and organize your profiling groups and manage access to them.
- [View tags for a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/how-to-tag-profiling-group-list.html): Tags can help you identify and organize your AWS resources and manage access to them.
- [Edit tags for a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/how-to-tag-profiling-group-update.html): You can change the value for a tag associated with a profiling group.
- [Remove a tag from a profiling group](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/how-to-tag-profiling-group-delete.html): You can remove one or more tags associated with a profiling group.


## [Security](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security.html)

- [Data protection](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/data-protection.html): Discusses data protection in Amazon CodeGuru Profiler.

### [Identity and access management](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control.html)

How to authenticate requests and manage access your CodeGuru Profiler resources.

- [Audience](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security_iam_audience.html): How you use AWS Identity and Access Management (IAM) differs based on your role:
- [Authenticating with identities](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security_iam_authentication.html): Authentication is how you sign in to AWS using your identity credentials.
- [Managing access using policies](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security_iam_access-manage.html): You control access in AWS by creating policies and attaching them to AWS identities or resources.
- [Overview of managing access](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security_iam_service-with-iam.html): Describes how account administrators can manage access to resources by attaching permissions policies to IAM identities.
- [Using identity-based policies](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control-iam-identity-based-access-control.html): Provides examples of IAM identity-based policies for controlling access to Amazon CodeGuru Profiler.
- [Resource-based policies](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html): Describes resource-based policies and how they work with CodeGuru Profiler profiling group resources.
- [CodeGuru Profiler permissions reference](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control-permissions-reference.html): Describes the Amazon CodeGuru Profiler API operations and the corresponding actions that you grant permissions to perform.
- [AWS managed policies](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security-iam-awsmanpol.html): Learn about AWS managed policies for CodeGuru Profiler and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon CodeGuru Profiler and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/using-service-linked-roles.html): How to use service-linked roles to give CodeGuru Profiler access to resources in your AWS account.
- [Using tags to control access to Amazon CodeGuru Profiler resources](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control-using-tags.html): Conditions in IAM policy statements are part of the syntax that you can use to specify permissions for CodeGuru Profiler profiling group-based actions.
- [Compliance Validation](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/codeguru-profilerE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Using CodeGuru Profiler with VPC Endpoints](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/private-link.html): If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and Amazon CodeGuru Profiler.
- [Infrastructure security](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/infrastructure-security.html): Learn how Amazon CodeGuru Profiler isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/monitoring-overview.html)

- [Logging CodeGuru Profiler API calls with CloudTrail](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/cloudtrail.html): Learn about logging CodeGuru Profiler with AWS CloudTrail.

### [Monitoring CodeGuru Profiler with CloudWatch](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/monitoring.html)

Learn about monitoring CodeGuru Profiler using CloudWatch metrics and alarms.

- [Monitoring profiling groups with CloudWatch metrics](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/cloudwatch-metric.html): Learn how to view CodeGuru Profiler profiling group metrics in the CloudWatch console.
- [Monitoring profiling groups with CloudWatch alarms](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/cloudwatch-alarm.html): Learn how to create CloudWatch alarms for CodeGuru Profiler recommendations metrics.
