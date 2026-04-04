# Source: https://symfony.com/doc/current/validation/severity.html

Title: How to Handle Different Error Levels (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation/severity.html

Markdown Content:
How to Handle Different Error Levels (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/validation/severity.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/validation/severity.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/validation/severity.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) Learn Symfony today](https://symfony.com/book)[![Image 2](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)[![Image 3](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)

[](https://symfony.com/doc/current/validation/severity.html# "Search")

[](https://symfony.com/doc/current/validation/severity.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/validation/severity.html)

![Image 4: SensioLabs](https://connect.symfony.com/assets/images/sln-v2/sensiolabs-9Agct9D.png)
SensioLabs is the creator of Symfony and plays a pivotal role in supporting its growth. With a passionate team pushing the boundaries of PHP, SensioLabs helps organizations get the most out of Symfony through quality, high-performance, software vendor-level training and consulting services.

*   [International](https://sensiolabs.com/en)
*   [France](https://sensiolabs.com/fr)

In the Spotlight
----------------

[![Image 5: SymfonyInsight](https://connect.symfony.com/assets/images/sln-v2/symfonyinsight-HwpmiQ3.png)](https://insight.symfony.com/)

[![Image 6: Blackfire](https://connect.symfony.com/assets/images/sln-v2/blackfire-ca6NfRp.png)](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

Open Source
-----------

*   [Symfony - Web framework](https://symfony.com/)
*   [Twig - Templating](https://twig.symfony.com/)
*   [PHP Polyfills](https://github.com/symfony/polyfill)

Products
--------

*   [Insight: PHP Quality](https://insight.symfony.com/)
*   [Blackfire: Web App performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)
*   [SymfonyCloud powered by Upsun](https://symfony.com/cloud)

Solutions & Services
--------------------

*   [Training](https://training.sensiolabs.com/)
*   [Certification](https://certification.symfony.com/)
*   [Technical Solutions](https://sensiolabs.com/solutions)
*   [SensioLabs University](https://university.sensiolabs.com/)
*   [Experts](https://expert.sensiolabs.com/)

Community
---------

*   [Community](https://connect.symfony.com/)
*   [Conferences](https://live.symfony.com/)
*   [Videos](https://www.youtube.com/symfonytv)
*   [Partners](https://network.sensiolabs.com/en/partenaires)

Blogs
-----

[Symfony](https://symfony.com/blog/), [SensioLabs](https://blog.sensiolabs.com/), [Insight](https://blog.insight.symfony.com/), and [Blackfire](https://blog.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler). 

[](https://symfony.com/)

Close

*   About

    *   [What is Symfony?](https://symfony.com/what-is-symfony)
    *   [Community](https://symfony.com/community)
    *   [News](https://symfony.com/blog/)
    *   [Contributing](https://symfony.com/doc/current/contributing/index.html)
    *   [Support](https://symfony.com/support)

*   Documentation

    *   [Symfony Docs](https://symfony.com/doc)
    *   [Symfony Book](https://symfony.com/book)
    *   [Screencasts](https://symfonycasts.com/)
    *   [Symfony Bundles](https://symfony.com/bundles)
    *   [Symfony Cloud](https://symfony.com/doc/cloud/)
    *   [Training](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)

*   Services

    *   [Upsun for Symfony](https://symfony.com/cloud/)Best platform to deploy Symfony apps
    *   [SymfonyInsight](https://insight.symfony.com/)Automatic quality checks for your apps
    *   [Symfony Certification](https://certification.symfony.com/)Prove your knowledge and boost your career
    *   [SensioLabs](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_submenu&utm_campaign=permanent_referral)Professional services to help you with Symfony
    *   [Blackfire](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)Profile and monitor performance of your apps

*   Other
*   [Blog](https://symfony.com/blog/)
*   [Download](https://symfony.com/download)

sponsored by[](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_sponsoredby&utm_campaign=permanent_referral "SensioLabs, PHP services and software solutions for enterprise and community.")

[SymfonyLive Berlin 2026](https://live.symfony.com/2026-berlin)

April 23 – 24, 2026

+20 talks and workshops

Register now

1.   [Home](https://symfony.com/)
2.   [Documentation](https://symfony.com/doc)
3.   [Validation](https://symfony.com/doc/current/validation.html)
4.    How to Handle Different Error Levels 

 Search Symfony Docs 

Version:

Table of Contents

*   [1. Assigning the Error Level](https://symfony.com/doc/current/validation/severity.html#1-assigning-the-error-level)
*   [2. Customize the Error Message Template](https://symfony.com/doc/current/validation/severity.html#2-customize-the-error-message-template)

How to Handle Different Error Levels
====================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation/severity.rst)

Sometimes, you may want to display constraint validation error messages differently based on some rules. For example, you have a registration form for new users where they enter some personal information and choose their authentication credentials. They would have to choose a username and a secure password, but providing bank account information would be optional. However, you want to make sure that these optional fields, if entered, are still valid, but display their errors differently.

The process to achieve this behavior consists of two steps:

1.   Apply different error levels to the validation constraints;
2.   Customize your error messages depending on the configured error level.

[1. Assigning the Error Level](https://symfony.com/doc/current/validation/severity.html#1-assigning-the-error-level "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------

Use the `payload` option to configure the error level for each constraint:

Attributes YAML XML PHP

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class User
{
    #[Assert\NotBlank(payload: ['severity' => 'error'])]
    protected string $username;

    #[Assert\NotBlank(payload: ['severity' => 'error'])]
    protected string $password;

    #[Assert\Iban(payload: ['severity' => 'warning'])]
    protected string $bankAccountNumber;
}
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
```
# config/validator/validation.yaml
App\Entity\User:
    properties:
        username:
            - NotBlank:
                payload:
                    severity: error
        password:
            - NotBlank:
                payload:
                    severity: error
        bankAccountNumber:
            - Iban:
                payload:
                    severity: warning
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\User">
        <property name="username">
            <constraint name="NotBlank">
                <option name="payload">
                    <value key="severity">error</value>
                </option>
            </constraint>
        </property>
        <property name="password">
            <constraint name="NotBlank">
                <option name="payload">
                    <value key="severity">error</value>
                </option>
            </constraint>
        </property>
        <property name="bankAccountNumber">
            <constraint name="Iban">
                <option name="payload">
                    <value key="severity">warning</value>
                </option>
            </constraint>
        </property>
    </class>
</constraint-mapping>
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class User
{
    // ...

    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint('username', new Assert\NotBlank(
            payload: ['severity' => 'error'],
        ));
        $metadata->addPropertyConstraint('password', new Assert\NotBlank(
            payload: ['severity' => 'error'],
        ));
        $metadata->addPropertyConstraint('bankAccountNumber', new Assert\Iban(
            payload: ['severity' => 'warning'],
        ));
    }
}
```

[2. Customize the Error Message Template](https://symfony.com/doc/current/validation/severity.html#2-customize-the-error-message-template "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

When validation of the `User` object fails, you can retrieve the constraint that caused a particular failure using the [getConstraint()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolation.php#:~:text=function%20getConstraint "Symfony\Component\Validator\ConstraintViolation::getConstraint()") method. Each constraint exposes the attached payload as a public property:

1
2
3
4
5
```
// a constraint validation failure, instance of
// Symfony\Component\Validator\ConstraintViolation
$constraintViolation = ...;
$constraint = $constraintViolation->getConstraint();
$severity = $constraint->payload['severity'] ?? null;
```

For example, you can leverage this to customize the `form_errors` block so that the severity is added as an additional HTML class:

1
2
3
4
5
6
7
8
9
```
{%- block form_errors -%}
    {%- if errors|length > 0 -%}
    <ul>
        {%- for error in errors -%}
            <li class="{{ error.cause.constraint.payload.severity ?? '' }}">{{ error.message }}</li>
        {%- endfor -%}
    </ul>
    {%- endif -%}
{%- endblock form_errors -%}
```

See also

For more information on customizing form rendering, see [How to Customize Form Rendering](https://symfony.com/doc/current/form/form_customization.html).

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/a02f907a7f9ff11a4c0f59daa3918e1ce49db6e6)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDTK3ICKBDTZ3JCASIVKQICW7DTKJKCEYDVK37CWSIL23LCTSIC53WF6BDK2QKC6SI5K7WCESDVK3EHJNCLSIZ)[Improve collaboration and visibility with one DevSecOps platform. Learn more from our team.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDTK3ICKBDTZ3JCASIVKQICW7DTKJKCEYDVK37CWSIL23LCTSIC53WF6BDK2QKC6SI5K7WCESDVK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

[![Image 8: Symfony Code Performance Profiling](https://symfony.com/images/network/blackfire_02.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_red_logo&utm_campaign=profiler)
[Symfony Code Performance Profiling](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_red_logo&utm_campaign=profiler)

[![Image 9: Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://symfony.com/images/network/slsolutions_01.webp)](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)
[Peruse our complete Symfony & PHP solutions catalog for your web development needs.](https://sensiolabs.com/services?utm_source=symfony&utm_medium=ad_visual&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 10: Avatar of Rami Dridi, a Symfony contributor](https://www.gravatar.com/avatar/940767a93e519aa3e7713938626a4c2f?size=48&rating=g&default=retro)

Thanks **Rami Dridi** for being a Symfony contributor

**1** commit • **3** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 11](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
[Celebrating 20 years of Symfony](https://symfony.com/20years)

**Symfony**™ is a trademark of Symfony SAS. [All rights reserved](https://symfony.com/trademark).

*   [What is Symfony?](https://symfony.com/what-is-symfony)

    *   [What is Symfony?](https://symfony.com/what-is-symfony)
    *   [Symfony at a Glance](https://symfony.com/at-a-glance)
    *   [Symfony Packages](https://symfony.com/packages)
    *   [Symfony Releases](https://symfony.com/releases)
    *   [Security Policy](https://symfony.com/doc/current/contributing/code/security.html)
    *   [Logo & Screenshots](https://symfony.com/logo)
    *   [Trademark & Licenses](https://symfony.com/license)
    *   [symfony1 Legacy](https://symfony.com/legacy)

*   [Learn Symfony](https://symfony.com/doc)

    *   [Symfony Docs](https://symfony.com/doc)
    *   [Symfony Book](https://symfony.com/book)
    *   [Reference](https://symfony.com/doc/current/reference/index.html)
    *   [Bundles](https://symfony.com/bundles)
    *   [Best Practices](https://symfony.com/doc/current/best_practices.html)
    *   [Training](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [eLearning Platform](https://university.sensiolabs.com/e-learning-platform?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Certification](https://certification.symfony.com/)

*   [Screencasts](https://symfonycasts.com/)

    *   [Learn Symfony](https://symfonycasts.com/tracks/symfony)
    *   [Learn PHP](https://symfonycasts.com/tracks/php)
    *   [Learn JavaScript](https://symfonycasts.com/tracks/javascript)
    *   [Learn Drupal](https://symfonycasts.com/tracks/drupal)
    *   [Learn RESTful APIs](https://symfonycasts.com/tracks/rest)

*   [Community](https://symfony.com/community)

    *   [Symfony Community](https://symfony.com/community)
    *   [SymfonyConnect](https://connect.symfony.com/)
    *   [Events & Meetups](https://symfony.com/events/)
    *   [Projects using Symfony](https://symfony.com/projects)
    *   [Contributors](https://symfony.com/contributors)
    *   [Symfony Jobs](https://symfony.com/jobs)
    *   [Backers](https://symfony.com/backers)
    *   [Code of Conduct](https://symfony.com/doc/current/contributing/code_of_conduct/code_of_conduct.html)
    *   [Downloads Stats](https://symfony.com/stats/downloads)
    *   [Support](https://symfony.com/support)

*   [Blog](https://symfony.com/blog/)

    *   [All Blog Posts](https://symfony.com/blog/)
    *   [A Week of Symfony](https://symfony.com/blog/category/a-week-of-symfony)
    *   [Case Studies](https://symfony.com/blog/category/case-studies)
    *   [Cloud](https://symfony.com/blog/category/cloud)
    *   [Community](https://symfony.com/blog/category/community)
    *   [Conferences](https://symfony.com/blog/category/conferences)
    *   [Diversity](https://symfony.com/blog/category/diversity)
    *   [Living on the edge](https://symfony.com/blog/category/living-on-the-edge)
    *   [Releases](https://symfony.com/blog/category/releases)
    *   [Security Advisories](https://symfony.com/blog/category/security-advisories)
    *   [Symfony Insight](https://symfony.com/blog/category/symfony-insight)
    *   [Twig](https://symfony.com/blog/category/twig)
    *   [SensioLabs Blog](https://sensiolabs.com/blog?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

*   [Services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)

    *   [SensioLabs services](https://sensiolabs.com/?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Train developers](https://sensiolabs.com/training?utm_source=symfony&utm_medium=symfony_footer&utm_campaign=permanent_referral)
    *   [Manage your project quality](https://insight.symfony.com/)
    *   [Improve your project performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=symfonycom_footer&utm_campaign=profiler)
    *   [Host Symfony projects](https://symfony.com/cloud/)

[Powered by](https://symfony.com/cloud/)

[](https://symfony.com/cloud/ "Upsun, a Platform-as-a-Service optimized for Symfony developers")

### Follow Symfony

[](https://github.com/symfony "Symfony on GitHub")[](https://symfony.com/slack "Symfony on Slack")[](https://twitter.com/symfony "Symfony on Twitter")[](https://mastodon.social/@symfony "Symfony on Mastodon")[](https://www.linkedin.com/company/symfony-sas/ "Symfony on LinkedIn")[](https://www.facebook.com/SymfonyFramework "Symfony on Facebook")[](https://www.youtube.com/symfonytv "Symfony on YouTube")[](https://bsky.app/profile/symfony.com "Symfony on BlueSky")[](https://www.threads.net/@symfony "Symfony on Threads")[](https://symfonycasts.com/ "Symfony Screencasts")[](https://feeds.feedburner.com/symfony/blog "Symfony Blog RSS")

Site appearance: 

CLOSE

Search Symfony Docs 

Search
