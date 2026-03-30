# Subscription Overview

::: {.toctree maxdepth="1" hidden="" titlesonly=""}
Self-Hosted \</product-overview/self-hosted-subscriptions\> Cloud
\</product-overview/cloud-subscriptions\> Non-Profit
\</product-overview/non-profit-subscriptions\>
:::

Mattermost offers the following types of paid subscriptions:

- `Self-hosted subscriptions </product-overview/self-hosted-subscriptions>`{.interpreted-text
  role="doc"} for secure enterprise collaboration with full control over
  your data.
- `Cloud subscriptions </product-overview/cloud-subscriptions>`{.interpreted-text
  role="doc"} for secure, cloud-based collaboration that\'s private,
  scaleable, and lower maintenance.
- `Non-profit subscriptions </product-overview/non-profit-subscriptions>`{.interpreted-text
  role="doc"} for nonprofit and open-source organizations who are unable
  to afford commercial licenses.

Learn more about Mattermost\'s commerial
`editions and offerings </product-overview/editions-and-offerings>`{.interpreted-text
role="doc"}.

## Mattermost Cloud

Enterprises can inquire about Mattermost Cloud \-- a secure, cloud-based
collaboration for fast moving enterprises that's private, scaleable, and
low maintenance offered on the same Kubernetes-based platform as the
self-hosted edition, and managed by Mattermost, Inc.

Enterprises can choose between
`dedicated </product-overview/cloud-dedicated>`{.interpreted-text
role="doc"} and
`shared </product-overview/cloud-shared>`{.interpreted-text role="doc"}
infrastructure based on your organizations' size, budget, technical
requirements, and level of control and customization needed.
`Private connectivity through VPC </product-overview/cloud-vpc-private-connectivity>`{.interpreted-text
role="doc"} is also available.

Talk to a [Mattermost Expert](https://mattermost.com/contact-sales/) to
learn more.

## Purchase Mattermost Licenses

Mattermost offers self-hosted capabilities through **Mattermost
Enterprise** and **Mattermost Professional** subscription plans.

Mattermost self-hosted deployments require a license subscription key to
be applied to access features. Your plan subscription determines what
features you have access to. Talk to a [Mattermost
expert](https://mattermost.com/contact-sales/) to learn more.

`Mattermost Enterprise and Mattermost Professional licenses </product-overview/editions-and-offerings>`{.interpreted-text
role="doc"} are sold as prepaid annual subscriptions based on the number
of seat licenses purchased, or "seats". Each seat license purchased
entitles a customer to an "activated user", which is a user registered
on a specific Mattermost server and not deactivated.

System administrators can view user status in the System Console and
activate and deactivate registered users at any time. Deactivated users
have history and preferences saved.

Talk to a [Mattermost Expert](https://mattermost.com/contact-sales/) to
learn more.

## Mattermost educational license program

For academic licensing, please visit us online:
<https://mattermost.com/education/>

[Book a live demo](https://mattermost.com/request-demo/) or [talk to a
Mattermost expert](https://mattermost.com/contact-sales/) to explore
tailored solutions for your organization\'s secure collaboration needs.
Or try Mattermost yourself with a [1-hour
preview](https://mattermost.com/sign-up/) for instant access to a live
sandbox environment.

## Frequently asked questions

### Why do I need to provide my name and physical address when purchasing a subscription?

Mattermost is a U.S. corporation and, therefore, all business we do is
governed by the laws of the United States, in addition to the local laws
wherever we are doing business.

The United States has a number of export control regulations implemented
to protect national security interests and to promote its foreign policy
objectives. Based on these regulations, U.S. companies are prohibited
from doing business with specific countries which have been embargoed by
the U.S. government. They are also prohibited from exporting certain
items to certain countries that have been sanctioned by the U.S.
government. In addition, U.S. companies are prohibited from doing
business with specific people and/or companies that have been named and
listed by the U.S. government.

In order to comply with these requirements, Mattermost must collect the
name and physical address of all individuals and companies it does
business with so that it can comply with the U.S. export controls
regulations.

### What does Mattermost do with this information?

The information you provide is used for a screening process. There are
two different purposes for screening:

- One screening is to ensure against exports of certain restricted goods
  to countries that are embargoed. In our case, goods refer to our
  software that has encryption in it.
- The other screening is against people and companies. There are certain
  people and companies that the government has put on a list (the Denied
  Party List) that US companies are prohibited from doing any business
  with for various reasons. They could be terrorists, be on a terrorist
  watch list, could be helping finance terrorists, could be
  participating in human rights violations, etc. If they are on the
  Denied Party List, we are not able to do any business with them.

### Who are the sanctioned people, companies, and entities?

The Office of Foreign Assets Control (OFAC) maintains a list of
sanctioned entities. Some examples include:

- Terrorists
- Banks or other financial institutions that are involved in financing
  terrorism
- Companies or people that have been involved in human or drug
  trafficking
- Organizations that have been sanctioned for human rights violations

This will also include people in violation of government contracts
because of our business with the U.S. government. Individuals and
Companies do not end up on the Denied Party List based on the country
they live in but by their actions and conduct.

### What does "physical address" mean for software that will be used in many places?

In this case, the \"physical address\" is the location where the
individual, who will be receiving the license key, is physically located
and will be able to access the software for installation.

### How is a user defined for subscriptions?

For the purpose of billing, a "user" is any account created in
Mattermost that does not show as **Deactivated** in **System Console \>
User Management \> Users**. Guests are also defined as users.

Bots, deactivated users, and synthetic users in
`Microsoft Teams integrations </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>`{.interpreted-text
role="doc"} and
`connected workspace </administration-guide/onboard/connected-workspaces>`{.interpreted-text
role="doc"} users aren\'t counted towards the total number of activated
users.

You can review your user count, for billing purposes, by going to
**System Console \> Site Statistics**, under **Total Activated Users**.

### Do I need to pay for deactivated users?

No. If you deactivate a user, that user is not counted as an activated
user during your annual renewal process. You can deactivate users
manually via the System Console, and also via Active Directory/LDAP
synchronization, the mmctl tool, and the server APIs.

If you choose to pull SQL reports from the database to monitor
individual activity to make deactivation decisions, and you are running
under high user load, we recommend the reports are pulled from a read
replica of the database.

### Which features are affected when my subscription expires?

The affected features include, but are not limited to, the following:

+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Feature              | How it\'s affected   | What steps do I need to take?                                                                     |
+======================+======================+===================================================================================================+
| Elasticsearch        | Elasticsearch is     | None needed.                                                                                      |
|                      | automatically        |                                                                                                   |
|                      | disabled and will    |                                                                                                   |
|                      | start using the      |                                                                                                   |
|                      | default database for |                                                                                                   |
|                      | indexing posts.      |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| AD/LDAP, SAML SSO,   | Login options are no | Users must be migrated to email authentication via **System Console \> Users**. Select the        |
| Entra ID SSO, and    | longer provided on   | drop-down menu for the relevant member, choose **Switch to Email/Password**, enter a new          |
| Google SSO           | the sign-in page.    | password, and choose **Reset**.                                                                   |
|                      | Users who previously |                                                                                                   |
|                      | signed in with one   |                                                                                                   |
|                      | of these methods are |                                                                                                   |
|                      | no longer able to.   |                                                                                                   |
|                      |                      |                                                                                                   |
|                      | Users who were       |                                                                                                   |
|                      | already signed in    |                                                                                                   |
|                      | can continue to use  |                                                                                                   |
|                      | Mattermost until     |                                                                                                   |
|                      | their session        |                                                                                                   |
|                      | expires or until     |                                                                                                   |
|                      | they log out.        |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| AD/LDAP              | Groups in the        | Use `mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl group>`{.interpreted-text   |
|                      | database are         | role="ref"} to modify group sync settings for the team/channel.                                   |
|                      | retained but cannot  |                                                                                                   |
|                      | be used. Memberships |                                                                                                   |
|                      | are frozen in state  |                                                                                                   |
|                      | for group synced     |                                                                                                   |
|                      | teams/channels.      |                                                                                                   |
|                      |                      |                                                                                                   |
|                      | Mentions for AD/LDAP |                                                                                                   |
|                      | groups are not shown |                                                                                                   |
|                      | in the autocomplete  |                                                                                                   |
|                      | menu.                |                                                                                                   |
|                      |                      |                                                                                                   |
|                      | Group mentions are   |                                                                                                   |
|                      | no longer            |                                                                                                   |
|                      | highlighted in text  |                                                                                                   |
|                      | and do not trigger   |                                                                                                   |
|                      | new notifications.   |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| High availability    | High availability is | None needed.                                                                                      |
|                      | disabled. If all     |                                                                                                   |
|                      | nodes in a cluster   |                                                                                                   |
|                      | continue running,    |                                                                                                   |
|                      | the nodes will stop  |                                                                                                   |
|                      | communicating and    |                                                                                                   |
|                      | caches will get out  |                                                                                                   |
|                      | of sync. This is     |                                                                                                   |
|                      | likely to cause      |                                                                                                   |
|                      | delays in messages,  |                                                                                                   |
|                      | notifications, etc.  |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Performance          | Monitoring is        | None needed.                                                                                      |
| monitoring           | disabled and Grafana |                                                                                                   |
|                      | will no longer       |                                                                                                   |
|                      | update with new      |                                                                                                   |
|                      | data.                |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Compliance exports   | Jobs are no longer   | None needed.                                                                                      |
|                      | scheduled in the job |                                                                                                   |
|                      | server. Data is not  |                                                                                                   |
|                      | exported.            |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Data retention       | Jobs are no longer   | None needed.                                                                                      |
|                      | scheduled in the job |                                                                                                   |
|                      | server. Data is not  |                                                                                                   |
|                      | deleted.             |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Custom terms         | Custom terms no      | None needed.                                                                                      |
|                      | longer displayed to  |                                                                                                   |
|                      | end users on login.  |                                                                                                   |
|                      | Data is retained in  |                                                                                                   |
|                      | the Terms of Service |                                                                                                   |
|                      | database table.      |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Custom announcement  | No longer visible    | None needed.                                                                                      |
| banners              | and is replaced by   |                                                                                                   |
|                      | the default          |                                                                                                   |
|                      | announcement banner. |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Multi-factor         | MFA is no longer     | None needed.                                                                                      |
| authentication (MFA) | enforced/required    |                                                                                                   |
|                      | for new accounts but |                                                                                                   |
|                      | remains enabled for  |                                                                                                   |
|                      | those who configured |                                                                                                   |
|                      | it.                  |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Permissions          | Permissions are      | Use                                                                                               |
|                      | retained in the      | `mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl permissions>`{.interpreted-text |
|                      | database in a frozen | role="ref"} to reset permissions to default.                                                      |
|                      | state and cannot be  |                                                                                                   |
|                      | modified in the      |                                                                                                   |
|                      | System Console.      |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+
| Guest accounts       | Guests that are not  | None needed.                                                                                      |
|                      | actively logged in   |                                                                                                   |
|                      | are prevented from   |                                                                                                   |
|                      | logging in. Guests   |                                                                                                   |
|                      | who are actively     |                                                                                                   |
|                      | logged in are able   |                                                                                                   |
|                      | to use Mattermost    |                                                                                                   |
|                      | until their session  |                                                                                                   |
|                      | expires or they log  |                                                                                                   |
|                      | out.                 |                                                                                                   |
+----------------------+----------------------+---------------------------------------------------------------------------------------------------+

### Is there a maximum number of users per subscription?

No, there is no limit to the subscription value or number of users you
can purchase per plan.

### What happens if my department buys a Mattermost subscription and then central IT buys a high volume subscription that also covers my department?

Mattermost subscriptions and support benefits are per production
instance.

When the subscription for your department\'s production instance
expires, you can either discontinue your department\'s production
instance and move to the instance hosted by central IT (which can
optionally provision one or more teams for your department to control),
or you can renew your subscription to maintain control of your
department\'s instance (e.g., to configure or customize the system in a
manner highly specific to your line-of-business) in addition to using
the instance from central IT.
