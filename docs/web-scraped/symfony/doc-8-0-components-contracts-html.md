# Source: https://symfony.com/doc/8.0/components/contracts.html

Title: The Contracts Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/contracts.html

Markdown Content:
The Contracts Component (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/components/contracts.html#main-content)

[Symfony Hub](https://symfony.com/doc/8.0/components/contracts.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/8.0/components/contracts.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight](https://insight.symfony.com/)[![Image 2](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight: The life jacket for your projects](https://insight.symfony.com/)[![Image 3](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight helps you protect your projects against security issues and technical debt.](https://insight.symfony.com/)

[](https://symfony.com/doc/8.0/components/contracts.html# "Search")

[](https://symfony.com/doc/8.0/components/contracts.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/components/contracts.html)

![Image 4: SensioLabs](https://connect.symfony.com/assets/images/sln-v2/sensiolabs-9Agct9D.png)
SensioLabs is the creator of Symfony and plays a pivotal role in supporting its growth. With a passionate team pushing the boundaries of PHP, SensioLabs helps organizations get the most out of Symfony through quality, high-performance, software vendor-level training and consulting services.

* [International](https://sensiolabs.com/en)
* [France](https://sensiolabs.com/fr)

In the Spotlight
----------------

[![Image 5: SymfonyInsight](https://connect.symfony.com/assets/images/sln-v2/symfonyinsight-HwpmiQ3.png)](https://insight.symfony.com/)

[![Image 6: Blackfire](https://connect.symfony.com/assets/images/sln-v2/blackfire-ca6NfRp.png)](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

Open Source
-----------

* [Symfony - Web framework](https://symfony.com/)
* [Twig - Templating](https://twig.symfony.com/)
* [PHP Polyfills](https://github.com/symfony/polyfill)

Products
--------

* [Insight: PHP Quality](https://insight.symfony.com/)
* [Blackfire: Web App performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)
* [SymfonyCloud powered by Upsun](https://symfony.com/cloud)

Solutions & Services
--------------------

* [Training](https://training.sensiolabs.com/)
* [Certification](https://certification.symfony.com/)
* [Technical Solutions](https://sensiolabs.com/solutions)
* [SensioLabs University](https://university.sensiolabs.com/)
* [Experts](https://expert.sensiolabs.com/)

Community
---------

* [Community](https://connect.symfony.com/)
* [Conferences](https://live.symfony.com/)
* [Videos](https://www.youtube.com/symfonytv)
* [Partners](https://network.sensiolabs.com/en/partenaires)

Blogs
-----

[Symfony](https://symfony.com/blog/), [SensioLabs](https://blog.sensiolabs.com/), [Insight](https://blog.insight.symfony.com/), and [Blackfire](https://blog.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler).

[](https://symfony.com/)

Close

* About

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Community](https://symfony.com/community)
  * [News](https://symfony.com/blog/)
  * [Contributing](https://symfony.com/doc/current/contributing/index.html)
  * [Support](https://symfony.com/support)

* Documentation

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Screencasts](https://symfonycasts.com/)
  * [Symfony Bundles](https://symfony.com/bundles)
  * [Symfony Cloud](https://symfony.com/doc/cloud/)
  * [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

* Services

  * [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
  * [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
  * [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
  * [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
  * [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

* Other
* [Blog](https://symfony.com/blog/)
* [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

[SymfonyCon Warsaw 2026](https://live.symfony.com/2026-warsaw-con)

November 26 – 27, 2026

Worldwide event in English

+35 talks and workshops

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. [Components](https://symfony.com/doc/current/components/index.html)
4. The Contracts Component

 Search Symfony Docs

Version:

Table of Contents

* [Installation](https://symfony.com/doc/8.0/components/contracts.html#installation)
* [Usage](https://symfony.com/doc/8.0/components/contracts.html#usage)
* [Design Principles](https://symfony.com/doc/8.0/components/contracts.html#design-principles)
* [Frequently Asked Questions](https://symfony.com/doc/8.0/components/contracts.html#frequently-asked-questions)
  * [How Is this Different From PHP-FIG's PSRs?](https://symfony.com/doc/8.0/components/contracts.html#how-is-this-different-from-php-fig-s-psrs)

The Contracts Component
=======================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/contracts.rst)

> The Contracts component provides a set of abstractions extracted out of the Symfony components. They can be used to build on semantics that the Symfony components proved useful - and that already have battle-tested implementations.

[Installation](https://symfony.com/doc/8.0/components/contracts.html#installation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

Contracts are provided as separate packages, so you can install only the ones your projects really need:

1
2
3
4
5
6

```
composer require symfony/cache-contracts
composer require symfony/event-dispatcher-contracts
composer require symfony/deprecation-contracts
composer require symfony/http-client-contracts
composer require symfony/service-contracts
composer require symfony/translation-contracts
```

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/8.0/components/using_components.html) for more details.

[Usage](https://symfony.com/doc/8.0/components/contracts.html#usage "Permalink to this headline")
-------------------------------------------------------------------------------------------------

The abstractions in this package are useful to achieve loose coupling and interoperability. By using the provided interfaces as type hints, you are able to reuse any implementations that match their contracts. It could be a Symfony component, or another package provided by the PHP community at large.

Depending on their semantics, some interfaces can be combined with [autowiring](https://symfony.com/doc/8.0/service_container/autowiring.html) to seamlessly inject a service in your classes.

Others might be useful as labeling interfaces, to hint about a specific behavior that can be enabled when using [autoconfiguration](https://symfony.com/doc/8.0/service_container.html#services-autoconfigure) or manual [service tagging](https://symfony.com/doc/8.0/service_container/tags.html) (or any other means provided by your framework.)

[Design Principles](https://symfony.com/doc/8.0/components/contracts.html#design-principles "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

* Contracts are split by domain, each into their own sub-namespaces;
* Contracts are small and consistent sets of PHP interfaces, traits, normative docblocks and reference test suites when applicable, ...;
* Contracts must have a proven implementation to enter this repository;
* Contracts must be backward compatible with existing Symfony components.

Packages that implement specific contracts should list them in the `provide` section of their `composer.json` file, using the `symfony/*-implementation` convention. For example:

1
2
3
4
5
6

```
{
    "...": "...",
    "provide": {
        "symfony/cache-implementation": "3.0"
    }
}
```

[Frequently Asked Questions](https://symfony.com/doc/8.0/components/contracts.html#frequently-asked-questions "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

### [How Is this Different From PHP-FIG's PSRs?](https://symfony.com/doc/8.0/components/contracts.html#how-is-this-different-from-php-fig-s-psrs "Permalink to this headline")

When applicable, the provided contracts are built on top of [PHP-FIG](https://www.php-fig.org/)'s PSRs. However, PHP-FIG has different goals and different processes. Symfony Contracts focuses on providing abstractions that are useful on their own while still compatible with implementations provided by Symfony.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: Online exam, become Symfony certified today](https://symfony.com/images/network/sf7certif_02.webp)](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=symfonycertified)
[Online exam, become Symfony certified today](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=symfonycertified)

[![Image 8: Save your teams and projects before they sink](https://symfony.com/images/network/sfinsight_02.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=sink)
[Save your teams and projects before they sink](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=sink)

Symfony footer
--------------

![Image 9: Avatar of Tim Jabs, a Symfony contributor](https://www.gravatar.com/avatar/1913f930c92023712407b9dc07c37dbe?size=48&rating=g&default=retro)

Thanks **Tim Jabs** for being a Symfony contributor

**3** commits • **49** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 10](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

* [What is Symfony?](https://symfony.com/what-is-symfony)

  * [What is Symfony?](https://symfony.com/what-is-symfony)
  * [Symfony at a Glance](https://symfony.com/at-a-glance)
  * [Symfony Packages](https://symfony.com/packages)
  * [Symfony Releases](https://symfony.com/releases)
  * [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
  * [Logo & Screenshots](https://symfony.com/logo)
  * [Trademark & Licenses](https://symfony.com/license)
  * [symfony1 Legacy](https://symfony.com/legacy)

* [Learn Symfony](https://symfony.com/doc)

  * [Symfony Docs](https://symfony.com/doc)
  * [Symfony Book](https://symfony.com/book)
  * [Reference](https://symfony.com/doc/current/reference/index.html)
  * [Bundles](https://symfony.com/bundles)
  * [Best Practices](https://symfony.com/doc/current/best_practices.html)
  * [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Certification](https://certification.symfony.com/)

* [Screencasts](https://symfonycasts.com/)

  * [Learn Symfony](https://symfonycasts.com/tracks/symfony)
  * [Learn PHP](https://symfonycasts.com/tracks/php)
  * [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
  * [Learn Drupal](https://symfonycasts.com/tracks/drupal)
  * [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

* [Community](https://symfony.com/community)

  * [Symfony Community](https://symfony.com/community)
  * [SymfonyConnect](https://connect.symfony.com/)
  * [Events & Meetups](https://symfony.com/events/)
  * [Projects using Symfony](https://symfony.com/projects)
  * [Contributors](https://symfony.com/contributors)
  * [Symfony Jobs](https://symfony.com/jobs)
  * [Backers](https://symfony.com/backers)
  * [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
  * [Downloads Stats](https://symfony.com/stats/downloads)
  * [Support](https://symfony.com/support)

* [Blog](https://symfony.com/blog/)

  * [All Blog Posts](https://symfony.com/blog/)
  * [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
  * [Case Studies](https://symfony.com/blog/category/case-studies)
  * [Cloud](https://symfony.com/blog/category/cloud)
  * [Community](https://symfony.com/blog/category/community)
  * [Conferences](https://symfony.com/blog/category/conferences)
  * [Diversity](https://symfony.com/blog/category/diversity)
  * [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
  * [Releases](https://symfony.com/blog/category/releases)
  * [Security Advisories](https://symfony.com/blog/category/security-advisories)
  * [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
  * [Twig](https://symfony.com/blog/category/twig)
  * [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

* [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

  * [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
  * [Manage your project quality](https://insight.symfony.com/)
  * [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
  * [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance:

CLOSE

Search Symfony Docs

Search
