# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.4.x/release-notes-5.4.0.md

# Release notes v5.4.0

The Avaamo Conversational AI Platform v5.4.0 minor release includes 2 enhancements and 1 change distributed as follows:

* **Enhancements**:
  * [Ability to export upto 6 months of data from Query insights](#1-ability-to-export-upto-6-months-of-data-from-query-insights)
  * [Ability to allow parallel development of Dynamic Q\&A, Q\&A, and Smalltalk skills ](#2-ability-to-allow-parallel-development-of-dynamic-q-and-a-q-and-a-and-smalltalk-skills)
* **Change**: This release also includes changes related to language packs in Q\&A and Smalltalk skills. See [Changes](#changes), for more information.

## Enhancements

### 1. Ability to export upto 6 months of data from Query insights

In this release, the export functionality in the **Query insights** page has been enhanced with the ability to export upto 6 months of data at a time based on your search criteria.&#x20;

* When you click **Export** from the **Query Insights** page, an export job is created based on the search criteria. An email notification is sent to you upon completion. Note that it may take a while to export the data based on your search results.&#x20;
* You can view the last 10 export jobs from **Query insights -> View export jobs** pop-up. You can also download the exported data or delete the jobs that are no longer required.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MJ2AP7aR2V11tSRCKiQ%2F-MJ2C5rjrM48lbESY-XB%2F5.4-export-jobs.png?alt=media\&token=63e8288e-6dd6-430e-9539-d4707aaff189)

See [Export query insights data](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights#export-query-insights-data), for more information.&#x20;

In the previous release, you could export only upto 50000 records from query insights at a time. If you had to export more than 50000 records, then you had to send a request to Avaamo Support for further assistance.&#x20;

Additionally, in the previous release, when you clicked the Export option, you could select user properties such as first\_name, last\_name that were required in the exported file. With the 5.3.0 release, you can now set the **User properties** in the **Agent -> Configuration**. Hence, by default, all the configured user properties in the agent are also exported in the CSV file. See [User properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

### 2. Ability to allow parallel development of Dynamic Q\&A, Q\&A, and Smalltalk skills&#x20;

In this release, Q\&A and Smalltalk skill development has been enhanced to allow multiple developers to work parallelly in the same skill. They can add or edit questions and answers simultaneously in the same skill. This feature helps in:

* Rapid agent development
* Better collaboration
* Faster delivery by reducing the turn around time to build a skill
* Seamless multiple developers engagement to build a single agent

As a part of this enhancement, on a high-level, the following changes have been implemented in this release:

* There is no **Save** at the skill level for Dynamic Q\&A, Smalltalk, and Q\&A.
* **Save** is now available for each intent, intro message, and outro message. This allows developers to obtain lock at each of these levels independently, hence promoting parallel development.

The illustration here, depicts a user "John Miller" editing an intent and another user parallelly editing another intent in the same Q\&A skill:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MJBkAAouVLY97Nf1eKK%2F-MJBs8y-AF0cNmgMdDzz%2F5.4-parallel-dev.png?alt=media\&token=f800a0f6-e25f-4997-ba76-cc5f0206930f)

Refer to the following topics for more in-depth understanding:

* [Dynamic Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/dynamic-q-and-a/build-and-manage-dynamic-q-and-a-skill)
* [Smalltalk](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-smalltalk/build-and-manage-smalltalk-skill)
* [Q\&A](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-q-and-a-designer/build-and-manage-q-and-a-skill)
* [Parallel development (QA & Smalltalk) FAQs](https://docs.avaamo.com/user-guide/ref/parallel-development-qa-and-smalltalk-faqs)

In the previous release, only one developer could work on Q\&A or Smalltalk skills at a time, as the lock was at the agent level. This resulted in slower development and subsequently affected the agent development and delivery time.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MJlKezCOgStySJVBaLO%2F-MJlpiZmXGdnXG44btAV%2Fold-qa-skill.png?alt=media\&token=9eae4658-79e5-4079-98ec-c43a1a9d92c7)

## Changes

In this release, **Make default** option in the **Configuration -> Language** page for language packs in Dynamic Q\&A, Q\&A, and Smalltalk skills has been removed, as it is no longer required. Since the conversation is always at the agent level, **Make default** option in the **Configuration -> Language** page at the agent level can be used instead.
