# Source: https://symfony.com/doc/current/reference/constraints/UserPassword.html

Title: UserPassword (Symfony Docs)

URL Source: https://symfony.com/doc/current/reference/constraints/UserPassword.html

Markdown Content:
UserPassword (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/reference/constraints/UserPassword.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/reference/constraints/UserPassword.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/reference/constraints/UserPassword.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight](https://insight.symfony.com/)[![Image 2](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight: The life jacket for your projects](https://insight.symfony.com/)[![Image 3](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight helps you protect your projects against security issues and technical debt.](https://insight.symfony.com/)

[](https://symfony.com/doc/current/reference/constraints/UserPassword.html# "Search")

[](https://symfony.com/doc/current/reference/constraints/UserPassword.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/reference/constraints/UserPassword.html)

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

[SymfonyCon Warsaw 2026](https://live.symfony.com/2026-warsaw-con)

November 26 – 27, 2026

Worldwide event in English

+35 talks and workshops

1.   [Home](https://symfony.com/)
2.   [Documentation](https://symfony.com/doc)
3.   [Reference](https://symfony.com/doc/current/reference/index.html)
4.   [Constraints](https://symfony.com/doc/current/reference/constraints.html)
5.    UserPassword 

 Search Symfony Docs 

Version:

Table of Contents

*   [Basic Usage](https://symfony.com/doc/current/reference/constraints/UserPassword.html#basic-usage)
*   [Options](https://symfony.com/doc/current/reference/constraints/UserPassword.html#options)
    *   [groups](https://symfony.com/doc/current/reference/constraints/UserPassword.html#groups)
    *   [message](https://symfony.com/doc/current/reference/constraints/UserPassword.html#message)
    *   [payload](https://symfony.com/doc/current/reference/constraints/UserPassword.html#payload)

UserPassword
============

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/reference/constraints/UserPassword.rst)

This validates that an input value is equal to the current authenticated user's password. This is useful in a form where a user can change their password, but needs to enter their old password for security.

Note

This should **not** be used to validate a login form, since this is done automatically by the security system.

Note

In order to use this constraint, you should have installed the symfony/security-core component with Composer.

Applies to[property or method](https://symfony.com/doc/current/validation.html#validation-property-target)
Class[UserPassword](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Security/Core/Validator/Constraints/UserPassword.php "Symfony\Component\Security\Core\Validator\Constraints\UserPassword")
Validator[UserPasswordValidator](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Security/Core/Validator/Constraints/UserPasswordValidator.php "Symfony\Component\Security\Core\Validator\Constraints\UserPasswordValidator")

[Basic Usage](https://symfony.com/doc/current/reference/constraints/UserPassword.html#basic-usage "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------

Suppose you have a `ChangePassword` class, that's used in a form where the user can change their password by entering their old password and a new password. This constraint will validate that the old password matches the user's current password:

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
```
// src/Form/Model/ChangePassword.php
namespace App\Form\Model;

use Symfony\Component\Security\Core\Validator\Constraints as SecurityAssert;

class ChangePassword
{
    #[SecurityAssert\UserPassword(
        message: 'Wrong value for your current password',
    )]
    protected string $oldPassword;
}
```

1
2
3
4
5
6
```
# config/validator/validation.yaml
App\Form\Model\ChangePassword:
    properties:
        oldPassword:
            - Symfony\Component\Security\Core\Validator\Constraints\UserPassword:
                message: 'Wrong value for your current password'
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
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Form\Model\ChangePassword">
        <property name="oldPassword">
            <constraint
                name="Symfony\Component\Security\Core\Validator\Constraints\UserPassword"
            >
                <option name="message">Wrong value for your current password</option>
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
```
// src/Form/Model/ChangePassword.php
namespace App\Form\Model;

use Symfony\Component\Security\Core\Validator\Constraints as SecurityAssert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class ChangePassword
{
    // ...

    public static function loadValidatorData(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint(
            'oldPassword',
            new SecurityAssert\UserPassword([
                'message' => 'Wrong value for your current password',
            ])
        );
    }
}
```

[Options](https://symfony.com/doc/current/reference/constraints/UserPassword.html#options "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

### [`groups`](https://symfony.com/doc/current/reference/constraints/UserPassword.html#groups "Permalink to this headline")

**type**: `array` | `string`**default**: `null`

It defines the validation group or groups of this constraint. Read more about [validation groups](https://symfony.com/doc/current/validation/groups.html).

### [`message`](https://symfony.com/doc/current/reference/constraints/UserPassword.html#message "Permalink to this headline")

**type**: `message`**default**: `This value should be the user current password.`

This is the message that's displayed when the underlying string does _not_ match the current user's password.

This message has no parameters.

### [`payload`](https://symfony.com/doc/current/reference/constraints/UserPassword.html#payload "Permalink to this headline")

**type**: `mixed`**default**: `null`

This option can be used to attach arbitrary domain-specific data to a constraint. The configured payload is not used by the Validator component, but its processing is completely up to you.

For example, you may want to use [several error levels](https://symfony.com/doc/current/validation/severity.html) to present failed constraints differently in the front-end depending on the severity of the error.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/84dc127dd611279d2e1851401dca56a0f28ebfa8)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKC6YIE2QYCE7IK53LCVADP23YCK7IT27MHEYI527ICEBDK23ECTNCYBZ52K)[Start an annual website plan, and get a free domain name with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKC6YIE2QYCE7IK53LCVADP23YCK7IT27MHEYI527ICEBDK23ECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 8: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B34445489.438308384;dc_trk_aid=631459208;dc_trk_cid=248949291;ord=177344955;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 9: Take the exam at home](https://symfony.com/images/network/sy1certif_02.webp)](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliusexamhome)
[Take the exam at home](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliusexamhome)

[![Image 10: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 11: Avatar of Ian Kevin Irlen, a Symfony contributor](https://connect.symfony.com/api/images/150a7a92-475d-497a-84dd-24b471e30a41.png?format=48x48)

Thanks **[Ian Kevin Irlen](https://connect.symfony.com/profile/kevinirlen)** (**@kevinirlen**) for being a Symfony contributor

[**1** commit](https://github.com/symfony/symfony/commits?author=kevinirlen) • **8** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 12](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
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
