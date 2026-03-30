# Source: https://docs.aws.amazon.com/macie/latest/user/llms.txt

# Amazon Macie User Guide

> Amazon Macie is a fully managed data security and data privacy service. Macie uses machine learning and pattern matching to help you discover, monitor, and protect your sensitive data in Amazon S3.

- [What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [Getting started](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)
- [Concepts and terminology](https://docs.aws.amazon.com/macie/latest/user/macie-terms.html)
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/macie/latest/user/macie-cloudtrail.html)
- [Creating resources with AWS CloudFormation](https://docs.aws.amazon.com/macie/latest/user/creating-resources-with-cloudformation.html)
- [Suspending Macie](https://docs.aws.amazon.com/macie/latest/user/suspend-macie.html)
- [Disabling Macie](https://docs.aws.amazon.com/macie/latest/user/disable-macie.html)
- [Quotas](https://docs.aws.amazon.com/macie/latest/user/macie-quotas.html)
- [Document history](https://docs.aws.amazon.com/macie/latest/user/doc-history.html)

## [Monitoring data security and privacy](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3.html)

- [How Macie monitors Amazon S3 data security](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html): Understand the features and techniques that Amazon Macie uses to monitor and evaluate S3 buckets for security and access control, and report potential issues.
- [Assessing your Amazon S3 security posture](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-dashboard.html): Understand the aggregated statistics and data that Amazon Macie provides to help you assess the security, privacy, and sensitivity of your Amazon S3 data.

### [Analyzing your Amazon S3 security posture](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory.html)

Learn about options for using Amazon Macie to examine and evaluate the security and privacy of your Amazon S3 data.

- [Reviewing your S3 bucket inventory](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory-review.html): Learn how to access and interpret statistics and other data that Amazon Macie provides to help you assess the security and privacy of your Amazon S3 data.
- [Filtering your S3 bucket inventory](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory-filter.html): Learn how to create and apply filter criteria in Amazon Macie to analyze data about your S3 buckets.
- [Allowing Macie to access S3 buckets and objects](https://docs.aws.amazon.com/macie/latest/user/monitoring-restrictive-s3-buckets.html): Learn about permitting Amazon Macie to evaluate and monitor your Amazon S3 data for security and access control, and inspect your S3 buckets for sensitive data.


## [Discovering sensitive data](https://docs.aws.amazon.com/macie/latest/user/data-classification.html)

### [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html)

Learn about the categories and types of sensitive data that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.

- [Keyword requirements](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers-keywords.html): Learn about Amazon Macie keyword requirements and proximity rules for detecting sensitive data in Amazon S3 objects by using built-in criteria and techniques.
- [Quick reference by sensitive data type](https://docs.aws.amazon.com/macie/latest/user/mdis-reference-quick.html): Learn about the types of sensitive data that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.

### [Detailed reference by sensitive data category](https://docs.aws.amazon.com/macie/latest/user/mdis-reference.html)

Find details about the categories and types of sensitive data that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.

- [Credentials](https://docs.aws.amazon.com/macie/latest/user/mdis-reference-credentials.html): Learn about the types of sensitive credentials data that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.
- [Financial information](https://docs.aws.amazon.com/macie/latest/user/mdis-reference-financial.html): Learn about the types of sensitive financial information that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.
- [Personal information: PHI](https://docs.aws.amazon.com/macie/latest/user/mdis-reference-phi.html): Learn about the types of sensitive, personal health information that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.
- [Personal information: PII](https://docs.aws.amazon.com/macie/latest/user/mdis-reference-pii.html): Learn about the types of personally identifiable information that Amazon Macie can detect in Amazon S3 objects by using built-in criteria and techniques.

### [Building custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html)

Learn how to define custom criteria that Amazon Macie can use to detect sensitive data in Amazon S3 objects.

- [Configuration options for custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/cdis-options.html): Learn about options for defining custom criteria that Amazon Macie can use to detect sensitive data in Amazon S3 objects.
- [Creating a custom data identifier](https://docs.aws.amazon.com/macie/latest/user/cdis-create.html): Learn how to create and configure custom criteria that Amazon Macie can use to detect sensitive data in Amazon S3 objects.
- [Deleting a custom data identifier](https://docs.aws.amazon.com/macie/latest/user/cdis-delete.html): Learn how to delete a custom data identifier that defines custom criteria for Amazon Macie to use when inspecting Amazon S3 objects for sensitive data.

### [Defining sensitive data exceptions with allow lists](https://docs.aws.amazon.com/macie/latest/user/allow-lists.html)

Learn about options for configuring Amazon Macie to ignore specific text and text patterns when it inspects Amazon S3 objects for sensitive data.

- [Configuration options for allow lists](https://docs.aws.amazon.com/macie/latest/user/allow-lists-options.html): Understand requirements for using Amazon Macie allow lists that define text and text patterns to ignore when inspecting Amazon S3 objects for sensitive data.
- [Creating an allow list](https://docs.aws.amazon.com/macie/latest/user/allow-lists-create.html): Learn how to create an allow list that defines text or a text pattern for Amazon Macie to ignore when inspecting Amazon S3 objects for sensitive data.
- [Checking the status of an allow list](https://docs.aws.amazon.com/macie/latest/user/allow-lists-status-check.html): Learn how to check an allow list that defines text or a text pattern for Amazon Macie to ignore when inspecting Amazon S3 objects for sensitive data.
- [Changing an allow list](https://docs.aws.amazon.com/macie/latest/user/allow-lists-change.html): Learn how to update an allow list that defines text or a text pattern for Amazon Macie to ignore when inspecting Amazon S3 objects for sensitive data.
- [Deleting an allow list](https://docs.aws.amazon.com/macie/latest/user/allow-lists-delete.html): Learn how to delete an allow list that defines text or a text pattern for Amazon Macie to ignore when inspecting Amazon S3 objects for sensitive data.

### [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html)

Learn about using Amazon Macie to automatically and continually select and analyze objects in S3 buckets to determine whether they contain sensitive data.

- [How automated discovery works](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-how-it-works.html): Understand the sampling, analysis, and reporting techniques that Amazon Macie when it performs automated sensitive data discovery for Amazon S3 data.

### [Configuring automated discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-manage.html)

Learn about configuring Amazon Macie to automatically and continually select and analyze objects in S3 buckets to determine whether they contain sensitive data.

- [Prerequisites](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-configure-prereqs.html): Learn which permissions and resources you need to enable and configure Amazon Macie to perform automated sensitive data discovery for your Amazon S3 data.
- [Enabling automated discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-enable.html): Learn how to activate automated sensitive data discovery and enable Amazon Macie to automatically select and inspect S3 objects for sensitive data.
- [Configuring automated discovery settings](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-configure.html): Learn how to customize the analysis settings that Amazon Macie uses when it performs automated sensitive data discovery for your Amazon S3 data.
- [Disabling automated discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-disable.html): Learn how to deactivate automated sensitive data discovery and stop Amazon Macie from automatically selecting and inspecting S3 objects for sensitive data.

### [Reviewing automated discovery statistics and results](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3.html)

Learn about options for reviewing the results of automated sensitive data discovery activities that Amazon Macie has performed for your Amazon S3 data.

- [Reviewing statistics on the Summary dashboard](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-dashboard.html): Understand the aggregated, automated sensitive data discovery statistics that Amazon Macie provides to help you assess the sensitivity of your Amazon S3 data.
- [Visualizing data sensitivity with the S3 buckets map](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-inventory-map.html): Learn how to assess the sensitivity of your Amazon S3 data by interacting with and interpreting data in the S3 buckets heat map on the Amazon Macie console.
- [Assessing data sensitivity with the S3 buckets table](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-inventory-table.html): Learn how to access statistics and other data that Amazon Macie provides to help you assess the sensitivity, security, and privacy of your Amazon S3 data.
- [Reviewing S3 bucket details](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-inventory-details.html): Learn how to interpret statistics and details that Amazon Macie provides to help you assess the sensitivity, security, and privacy of your Amazon S3 data.
- [Analyzing sensitive data findings](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-findings.html): Learn how to identify and access findings that Amazon Macie generates when it performs automated sensitive data discovery for your Amazon S3 data.
- [Accessing sensitive data discovery results](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-results-s3-sddrs.html): Learn about accessing sensitive data discovery results that Amazon Macie generates when it performs automated sensitive data discovery for your Amazon S3 data.

### [Assessing automated discovery coverage](https://docs.aws.amazon.com/macie/latest/user/discovery-coverage.html)

Understand how to identify and address issues and errors that prevent Amazon Macie from performing automated sensitive data discovery for your Amazon S3 data.

- [Reviewing coverage data](https://docs.aws.amazon.com/macie/latest/user/discovery-coverage-review.html): Learn how to identify issues and errors that prevent Amazon Macie from performing automated sensitive data discovery for your Amazon S3 data.
- [Remediating coverage issues](https://docs.aws.amazon.com/macie/latest/user/discovery-coverage-remediate.html): Learn about options for addressing issues and errors that prevent Amazon Macie from performing automated sensitive data discovery for your Amazon S3 data.
- [Adjusting sensitivity scores for S3 buckets](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-s3bucket-manage.html): Learn how to adjust the bucket-level settings that Amazon Macie uses when it performs automated sensitive data discovery for your Amazon S3 data.
- [Sensitivity scoring for S3 buckets](https://docs.aws.amazon.com/macie/latest/user/discovery-scoring-s3.html): Learn about the range of data sensitivity scores and labels that Amazon Macie defines for S3 buckets.
- [Default automated discovery settings](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-settings-defaults.html): Learn about the configuration settings that Amazon Macie uses by default when it performs automated sensitive data discovery for your Amazon S3 data.

### [Running sensitive data discovery jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs.html)

Learn about options for creating and configuring sensitive data discovery jobs in Amazon Macie to detect and report sensitive data.

- [Scope options for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-scope.html): Learn about options and settings that you can use to refine the scope of sensitive data discovery jobs in Amazon Macie.
- [Creating a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-create.html): Learn how to discover and report sensitive data by creating a sensitive data discovery job in Amazon Macie.
- [Reviewing job results](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-manage-results.html): Learn about the different types of results that sensitive data discovery jobs in Amazon Macie produce, and how to access those results.

### [Managing jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-manage.html)

Learn how to access an inventory of sensitive data discovery jobs in Amazon Macie and perform various management tasks for individual jobs in the inventory.

- [Reviewing your job inventory](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-manage-view.html): Learn how to access a list of sensitive data discovery jobs in Amazon Macie and how to review the configuration settings and status of individual jobs.
- [Reviewing configuration settings for a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-manage-settings.html): Learn how to access and review the configuration settings for a sensitive data discovery job in Amazon Macie.
- [Checking the status of a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-status-check.html): Learn about the different statuses that a sensitive data discovery job might have in Amazon Macie and how to check the current status of an existing job.
- [Changing the status of a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-status-change.html): Learn about options for pausing, resuming, or cancelling a sensitive data discovery job in Amazon Macie.
- [Copying a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-manage-copy.html): Learn how to quickly create and configure a sensitive data discovery job that is similar to an existing sensitive data discovery job in Amazon Macie.

### [Monitoring jobs with CloudWatch Logs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs.html)

Learn about the different types of events that Amazon Macie logs for sensitive data discovery jobs, and how to monitor the events with Amazon CloudWatch Logs.

- [How logging works for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs-configure.html): Learn about the resources and processes that Amazon Macie uses to publish logging data for sensitive data discovery jobs to Amazon CloudWatch Logs.
- [Reviewing logs for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs-review.html): Learn how to access, analyze, and monitor logging data that Amazon Macie publishes to Amazon CloudWatch Logs for sensitive data discovery jobs.
- [Understanding log events for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs-ref.html): Learn about the event schema and the different types of events that Amazon Macie logs in Amazon CloudWatch Logs for sensitive data discovery jobs.
- [Forecasting and monitoring job costs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-costs.html): Learn how to review estimated costs of running sensitive data discovery jobs in Amazon Macie.
- [Managed data identifiers recommended for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html): Learn which managed data identifiers we recommend for sensitive data discovery jobs in Amazon Macie.
- [Analyzing encrypted S3 objects](https://docs.aws.amazon.com/macie/latest/user/discovery-supported-encryption-types.html): Learn about the requirements for using Amazon Macie to inspect encrypted Amazon S3 objects for sensitive data.
- [Storing and retaining sensitive data discovery results](https://docs.aws.amazon.com/macie/latest/user/discovery-results-repository-s3.html): Learn how to configure Amazon Macie to store detailed records of the analysis that it performs when it inspects Amazon S3 objects for sensitive data.
- [Supported storage classes and formats](https://docs.aws.amazon.com/macie/latest/user/discovery-supported-storage.html): Learn which Amazon S3 objects and which types of content Amazon Macie can analyze to discover sensitive data.


## [Reviewing and analyzing findings](https://docs.aws.amazon.com/macie/latest/user/findings.html)

- [Types of findings](https://docs.aws.amazon.com/macie/latest/user/findings-types.html): Learn about the categories and types of findings that Amazon Macie provides to help you discover, monitor, and protect your sensitive data in Amazon S3.
- [Severity scoring for findings](https://docs.aws.amazon.com/macie/latest/user/findings-severity.html): Learn about the severity levels and scores that Amazon Macie assigns to policy findings and sensitive data findings.
- [Working with sample findings](https://docs.aws.amazon.com/macie/latest/user/findings-samples.html): Learn how to create sample findings that you can use to analyze and test the different types of findings that Amazon Macie can generate.
- [Reviewing findings](https://docs.aws.amazon.com/macie/latest/user/findings-view.html): Learn how to review and analyze Amazon Macie policy and sensitive data findings by using the Amazon Macie console.

### [Filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html)

Learn about using filter criteria to query and analyze findings in Amazon Macie.

- [Filter fundamentals](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html): Learn about the options and settings that you can use to filter findings in Amazon Macie.
- [Fields for filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-fields.html): Learn which fields and values you can use to filter findings in Amazon Macie.
- [Creating and applying filters](https://docs.aws.amazon.com/macie/latest/user/findings-filter-procedure.html): Learn how to create and use filter criteria to filter findings in Amazon Macie.

### [Defining filter rules](https://docs.aws.amazon.com/macie/latest/user/findings-filter-rule-procedures.html)

Learn how to create, apply, and manage rules for filtering views of findings on the Amazon Macie console.

- [Creating a filter rule](https://docs.aws.amazon.com/macie/latest/user/findings-filter-rule-create.html): Learn how to create a filter rule that uses saved filter criteria to include or exclude findings from views of findings on the Amazon Macie console.
- [Applying a filter rule](https://docs.aws.amazon.com/macie/latest/user/findings-filter-rule-apply.html): Learn how to apply a filter rule that uses saved filter criteria to include or exclude findings from views of findings on the Amazon Macie console.
- [Changing a filter rule](https://docs.aws.amazon.com/macie/latest/user/findings-filter-rule-change.html): Learn how to change a filter rule that specifies criteria for including or excluding findings from views of findings on the Amazon Macie console.
- [Deleting a filter rule](https://docs.aws.amazon.com/macie/latest/user/findings-filter-rule-delete.html): Learn how to delete a filter rule that uses saved filter criteria to include or exclude findings from views of findings on the Amazon Macie console.

### [Investigating sensitive data with findings](https://docs.aws.amazon.com/macie/latest/user/findings-investigate-sd.html)

Learn about locating and retrieving specific occurrences of sensitive data that Amazon Macie detects and reports in findings.

- [Locating sensitive data](https://docs.aws.amazon.com/macie/latest/user/findings-locate-sd.html): Learn how to determine where Amazon Macie found specific occurrences of sensitive data in an Amazon S3 object.

### [Retrieving sensitive data samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd.html)

Learn about using Amazon Macie to retrieve samples of sensitive data that Macie detects in Amazon S3 objects and reports in sensitive data findings.

- [Configuration options for retrieving samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd-options.html): Learn about options and requirements for configuring Amazon Macie to retrieve and reveal samples of sensitive data that it reports in sensitive data findings.
- [Configuring Macie to retrieve samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd-configure.html): Learn the tasks and requirements for configuring Amazon Macie to retrieve and reveal samples of sensitive data that it reports in sensitive data findings.
- [Retrieving samples](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd-proc.html): Learn how to determine whether samples are available for sensitive data that Amazon Macie reported in a sensitive data finding, and how to retrieve the samples.
- [Schema for sensitive data locations](https://docs.aws.amazon.com/macie/latest/user/findings-locate-sd-schema.html): Review details and examples of the JSON schema that Amazon Macie uses to indicate where it found occurrences of sensitive data in an Amazon S3 object.

### [Suppressing findings](https://docs.aws.amazon.com/macie/latest/user/findings-suppression.html)

Learn how to create, manage, and use suppression rules to automatically archive Amazon Macie findings based on specific attributes of findings.

- [Creating a suppression rule](https://docs.aws.amazon.com/macie/latest/user/findings-suppression-rule-create.html): Learn how to create a suppression rule that automatically archives Amazon Macie findings based on specific attributes of findings.
- [Reviewing suppressed findings](https://docs.aws.amazon.com/macie/latest/user/findings-suppression-view-findings.html): Learn how to access and review Amazon Macie findings that were archived automatically by suppression rules based on specific finding attributes.
- [Changing a suppression rule](https://docs.aws.amazon.com/macie/latest/user/findings-suppression-rule-change.html): Learn how to change a suppression rule that automatically archives Amazon Macie findings based on specific attributes of findings.
- [Deleting a suppression rule](https://docs.aws.amazon.com/macie/latest/user/findings-suppression-rule-delete.html): Learn how to delete a suppression rule that automatically archives Amazon Macie findings based on specific attributes of findings.


## [Monitoring and processing findings](https://docs.aws.amazon.com/macie/latest/user/findings-monitor.html)

- [Configuring publication settings for findings](https://docs.aws.amazon.com/macie/latest/user/findings-publish-frequency.html): Learn about the settings and schedule that Amazon Macie uses to publish findings to Amazon EventBridge and AWS Security Hub CSPM, and how to change the settings.
- [Processing findings with Amazon EventBridge](https://docs.aws.amazon.com/macie/latest/user/findings-monitor-events-eventbridge.html): Learn how to use Amazon EventBridge, formerly Amazon CloudWatch Events, to detect, monitor, and process Amazon Macie findings automatically.
- [Monitoring findings with AWS User Notifications](https://docs.aws.amazon.com/macie/latest/user/findings-monitor-events-uno.html): Learn how to configure AWS User Notifications to automatically send email, chat, and other types of notifications for Amazon Macie findings.
- [Evaluating findings with AWS Security Hub CSPM](https://docs.aws.amazon.com/macie/latest/user/securityhub-integration.html): Learn how to use AWS Security Hub CSPM to monitor, evaluate, and process Amazon Macie findings.
- [Amazon EventBridge event schema for findings](https://docs.aws.amazon.com/macie/latest/user/findings-publish-event-schemas.html): Learn about the structure of the finding events that Amazon Macie automatically publishes to Amazon EventBridge, formerly Amazon CloudWatch Events.


## [Forecasting and monitoring costs](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs.html)

- [Understanding estimated usage costs](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs-calculations.html): Learn about pricing dimensions and how estimated usage costs are calculated for Amazon Macie.
- [Reviewing estimated usage costs](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs-review.html): Learn how to access and review estimated costs for using Amazon Macie
- [Participating in the free trial](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-free-trial.html): Learn about features of the 30-day free trial for Amazon Macie, and how to enroll and check the status of your free trial.


## [Managing multiple accounts](https://docs.aws.amazon.com/macie/latest/user/macie-accounts.html)

- [Administrator and member account relationships](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-relationships.html): Learn what settings, data, and resources are available to Amazon Macie administrator and member accounts in an organization.

### [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao.html)

Learn about options for integrating Amazon Macie with AWS Organizations and centrally managing Macie for multiple accounts in the organization.

- [Considerations and recommendations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-notes.html): Consider these requirements and recommendations for configuring and managing Amazon Macie accounts for an organization in AWS Organizations.
- [Integrating and configuring an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-integrate.html): Learn how to integrate Amazon Macie with AWS Organizations, and configure Macie for accounts that are part of an organization in AWS Organizations.
- [Reviewing organization accounts](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-review.html): Learn how to access and review information about the Amazon Macie accounts for an organization in AWS Organizations.
- [Managing member accounts](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-administer.html): Learn how to add, remove, and manage the status of Amazon Macie accounts for an organization in AWS Organizations.
- [Changing the administrator account](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-admin-change.html): Learn how to designate a different account as the delegated Amazon Macie administrator account for an organization in AWS Organizations.
- [Disabling integration with AWS Organizations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-ao-disable.html): Learn how to disable Amazon Macie as a trusted service for an organization in AWS Organizations.

### [Managing accounts by invitation](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations.html)

Learn about options for centrally managing multiple Amazon Macie accounts by sending and responding to Macie membership invitations.

- [Considerations and recommendations](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-notes.html): Consider these requirements and recommendations for centrally managing multiple Amazon Macie accounts by using membership invitations.
- [Creating and managing an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-administer.html): Learn how to use membership invitations to centrally manage multiple Amazon Macie accounts and how to perform administrative tasks for the accounts.
- [Reviewing organization accounts](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-review.html): Learn how to review Amazon Macie accounts that you sent membership invitations to and are associated with your Macie administrator account.
- [Changing the administrator account](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-admin-change.html): Learn how to designate a different Amazon Macie administrator account for an organization that was created using Macie membership invitations.
- [Managing your membership in an organization](https://docs.aws.amazon.com/macie/latest/user/accounts-mgmt-invitations-membership-manage.html): Learn how to respond to membership invitations that you receive for Amazon Macie, and how to disassociate from a Macie administrator account and organization.


## [Tagging resources](https://docs.aws.amazon.com/macie/latest/user/tagging-resources.html)

- [Tagging fundamentals](https://docs.aws.amazon.com/macie/latest/user/tags-basics.html): Learn about options and requirements for defining and assigning tags to Amazon Macie resources such as allow lists and sensitive data discovery jobs.
- [Adding tags to resources](https://docs.aws.amazon.com/macie/latest/user/tags-add.html): Learn how to define and assign custom tags to Amazon Macie resources such as custom data identifiers and sensitive data discovery jobs.
- [Controlling access to resources using tags](https://docs.aws.amazon.com/macie/latest/user/tags-iam.html): Learn about using tags to define resource-level permissions in AWS Identity and Access Management policies that manage access to Amazon Macie resources.
- [Reviewing and editing tags for resources](https://docs.aws.amazon.com/macie/latest/user/tags-retrieve-update.html): Learn how to review and edit custom tags that are assigned to Amazon Macie resources such as custom data identifiers and sensitive data discovery jobs.
- [Removing tags from resources](https://docs.aws.amazon.com/macie/latest/user/tags-remove.html): Learn how to remove custom tags that are assigned to Amazon Macie resources such as custom data identifiers and sensitive data discovery jobs.


## [Security](https://docs.aws.amazon.com/macie/latest/user/security.html)

- [Data protection](https://docs.aws.amazon.com/macie/latest/user/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Macie.

### [Identity and access management](https://docs.aws.amazon.com/macie/latest/user/security-iam.html)

Learn about authenticating requests and managing access to Amazon Macie features, data, settings, and resources.

- [How Macie works with IAM](https://docs.aws.amazon.com/macie/latest/user/security_iam_service-with-iam.html): Learn about AWS Identity and Access Management features that you can use to manage access to Amazon Macie features, data, settings, and resources.
- [Identity-based policy examples](https://docs.aws.amazon.com/macie/latest/user/security_iam_id-based-policy-examples.html): Use these examples of AWS Identity and Access Management policies to build your own identity-based policies for Amazon Macie.
- [AWS managed policies](https://docs.aws.amazon.com/macie/latest/user/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Macie and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/macie/latest/user/service-linked-roles.html): Learn how to use service-linked roles to give Amazon Macie access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/macie/latest/user/security_iam_troubleshoot.html): Learn how to diagnose and address common access issues that you might encounter when working with AWS Identity and Access Management and Amazon Macie.
- [Compliance validation](https://docs.aws.amazon.com/macie/latest/user/compliance-validation.html): Learn how to determine which AWS services, including Amazon Macie, are in scope of specific compliance programs.
- [Resilience](https://docs.aws.amazon.com/macie/latest/user/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Macie features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/macie/latest/user/infrastructure-security.html): Learn about infrastructure protection and security for Amazon Macie.
- [AWS PrivateLink](https://docs.aws.amazon.com/macie/latest/user/vpc-interface-endpoints-macie.html): Learn about using an interface VPC endpoint, powered by AWS PrivateLink, to establish a private connection between your VPC and Amazon Macie.
