# Source: https://symfony.com/doc/current/contributing/code/security.html

Title: Security Issues (Symfony Docs)

URL Source: https://symfony.com/doc/current/contributing/code/security.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/contributing/code/security.rst)

This document explains how Symfony security issues are handled by the Symfony core team (Symfony being the code hosted on the main `symfony/symfony`[Git repository](https://github.com/symfony/symfony)).

[Reporting a Security Issue](https://symfony.com/doc/current/contributing/code/security.html#reporting-a-security-issue "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------

If you think that you have found a security issue in Symfony, don't use the bug tracker and don't publish it publicly. Instead, all security issues must be sent to **security [at] symfony.com**. Emails sent to this address are forwarded to the Symfony core team private mailing-list.

The following issues are not considered security issues and should be handled as regular bug fixes (if you have any doubts, don't hesitate to send us an email for confirmation):

* Any security issues found in debug tools that must never be enabled in production (including the web profiler or anything enabled when `APP_DEBUG` is set to `true` or `APP_ENV` set to anything but `prod`);
* Any security issues found in classes provided to help for testing that should never be used in production (like for instance mock classes that contain `Mock` in their name or classes in the `Test` namespace);
* Any fix that can be classified as **security hardening** like route enumeration, login throttling bypasses, denial of service attacks, timing attacks, or lack of `SensitiveParameter` attributes.

In any case, the core team has the final decision on which issues are considered security vulnerabilities.

[Security Bug Bounties](https://symfony.com/doc/current/contributing/code/security.html#security-bug-bounties "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

Symfony is an Open-Source project where most of the work is done by volunteers. We appreciate that developers are trying to find security issues in Symfony and report them responsibly, but we are currently unable to pay bug bounties.

[Resolving Process](https://symfony.com/doc/current/contributing/code/security.html#resolving-process "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------

For each report, we first try to confirm the vulnerability. When it is confirmed, the core team works on a solution following these steps:

1. Send an acknowledgment to the reporter;
2. Work on a patch;
3. Get a CVE identifier from [mitre.org](https://cveform.mitre.org/);
4. Write a security announcement for the official Symfony [blog](https://symfony.com/blog/) about the vulnerability. This post should contain the following information:

    *   a title that always include the "Security release" string;
    *   a description of the vulnerability;
    *   the affected versions;
    *   the possible exploits;
    *   how to patch/upgrade/workaround affected applications;
    *   the CVE identifier;
    *   credits.

5.   Send the patch and the announcement to the reporter for review;
6.   Apply the patch to all maintained versions of Symfony;
7.   Package new versions for all affected versions;
8.   Publish the post on the official Symfony [blog](https://symfony.com/blog/) (it must also be added to the "`Security Advisories`_" category);
9.   Update the public [security advisories database](https://github.com/FriendsOfPHP/security-advisories) maintained by the FriendsOfPHP organization and which is used by [the check:security command](https://symfony.com/doc/current/setup.html#security-checker).

Note

Releases that include security issues should not be done on Saturday or Sunday, except if the vulnerability has been publicly posted.

Note

While we are working on a patch, please do not reveal the issue publicly.

Note

The resolution takes anywhere between a couple of days to a month depending on its complexity and the coordination with the downstream projects (see next paragraph).

[Collaborating with Downstream Open-Source Projects](https://symfony.com/doc/current/contributing/code/security.html#collaborating-with-downstream-open-source-projects "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As Symfony is used by many large Open-Source projects, we standardized the way the Symfony security team collaborates on security issues with downstream projects. The process works as follows:

1. After the Symfony security team has acknowledged a security issue, it immediately sends an email to the downstream project security teams to inform them of the issue;
2. The Symfony security team creates a private Git repository to ease the collaboration on the issue and access to this repository is given to the Symfony security team, to the Symfony contributors that are impacted by the issue, and to one representative of each downstream projects;
3. All people with access to the private repository work on a solution to solve the issue via pull requests, code reviews, and comments;
4. Once the fix is found, all involved projects collaborate to find the best date for a joint release (there is no guarantee that all releases will be at the same time but we will try hard to make them at about the same time). When the issue is not known to be exploited in the wild, a period of two weeks is considered a reasonable amount of time.

The list of downstream projects participating in this process is kept as small as possible in order to better manage the flow of confidential information prior to disclosure. As such, projects are included at the sole discretion of the Symfony security team.

As of today, the following projects have validated this process and are part of the downstream projects included in this process:

* Drupal (releases typically happen on Wednesdays)
* eZPublish

[Issue Severity](https://symfony.com/doc/current/contributing/code/security.html#issue-severity "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------

In order to determine the severity of a security issue we take into account the complexity of any potential attack, the impact of the vulnerability and also how many projects it is likely to affect. This score out of 15 is then converted into a level of: Low, Medium, High, Critical, or Exceptional.

### [Attack Complexity](https://symfony.com/doc/current/contributing/code/security.html#attack-complexity "Permalink to this headline")

_Score of between 1 and 5 depending on how complex it is to exploit the vulnerability_

* 4 - 5 Basic: attacker must follow a set of simple steps
* 2 - 3 Complex: attacker must follow non-intuitive steps with a high level of dependencies
* 1 - 2 High: A successful attack depends on conditions beyond the attacker's control. That is, a successful attack cannot be accomplished at will, but requires the attacker to invest in some measurable amount of effort in preparation or execution against the vulnerable component before a successful attack can be expected.

### [Impact](https://symfony.com/doc/current/contributing/code/security.html#impact "Permalink to this headline")

_Scores from the following areas are added together to produce a score. The score for Impact is capped at 6. Each area is scored between 0 and 4._

* Integrity: Does this vulnerability cause non-public data to be accessible? If so, does the attacker have control over the data disclosed? (0-4)
* Disclosure: Can this exploit allow system data (or data handled by the system) to be compromised? If so, does the attacker have control over modification? (0-4)
* Code Execution: Does the vulnerability allow arbitrary code to be executed on an end-users system, or the server that it runs on? (0-4)
* Availability: Is the availability of a service or application affected? Is it reduced availability or total loss of availability of a service / application? Availability includes networked services (e.g. databases) or resources such as consumption of network bandwidth, processor cycles, or disk space. (0-4)

### [Affected Projects](https://symfony.com/doc/current/contributing/code/security.html#affected-projects "Permalink to this headline")

_Scores from the following areas are added together to produce a score. The score for Affected Projects is capped at 4._

* Will it affect some or all using a component? (1-2)
* Is the usage of the component that would cause such a thing already considered bad practice? (0-1)
* How common/popular is the component (e.g. Console vs HttpFoundation vs Lock)? (0-2)
* Are a number of well-known open source projects using Symfony affected that requires coordinated releases? (0-1)

### [Score Totals](https://symfony.com/doc/current/contributing/code/security.html#score-totals "Permalink to this headline")

* Attack Complexity: 1 - 5
* Impact: 1 - 6
* Affected Projects: 1 - 4

### [Severity levels](https://symfony.com/doc/current/contributing/code/security.html#severity-levels "Permalink to this headline")

* Low: 1 - 5
* Medium: 6 - 10
* High: 11 - 12
* Critical: 13 - 14
* Exceptional: 15

[Security Advisories](https://symfony.com/doc/current/contributing/code/security.html#security-advisories "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------

Check the [Security Advisories](https://symfony.com/blog/category/security-advisories) blog category for a list of all security vulnerabilities that were fixed in Symfony releases, starting from Symfony 1.0.0.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
