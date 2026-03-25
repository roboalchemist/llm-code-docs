# Source: https://symfony.com/doc/current/reference/constraints/PasswordStrength.html

Title: PasswordStrength (Symfony Docs)

URL Source: https://symfony.com/doc/current/reference/constraints/PasswordStrength.html

Markdown Content:
PasswordStrength (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight](https://insight.symfony.com/)[![Image 2](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight: The life jacket for your projects](https://insight.symfony.com/)[![Image 3](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight helps you protect your projects against security issues and technical debt.](https://insight.symfony.com/)

[](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html# "Search")

[](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/reference/constraints/PasswordStrength.html)

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
5.    PasswordStrength 

 Search Symfony Docs 

Version:

Table of Contents

*   [Basic Usage](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#basic-usage)
*   [Available Options](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#available-options)
    *   [minScore](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#minscore)
    *   [message](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#message)

*   [Customizing the Password Strength Estimation](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#customizing-the-password-strength-estimation)

PasswordStrength
================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/reference/constraints/PasswordStrength.rst)

Validates that the given password has reached the minimum strength required by the constraint. The strength of the password is not evaluated with a set of predefined rules (include a number, use lowercase and uppercase characters, etc.) but by measuring the entropy of the password based on its length and the number of unique characters used.

Applies to[property or method](https://symfony.com/doc/current/validation.html#validation-property-target)
Class[PasswordStrength](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraints/PasswordStrength.php "Symfony\Component\Validator\Constraints\PasswordStrength")
Validator[PasswordStrengthValidator](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraints/PasswordStrengthValidator.php "Symfony\Component\Validator\Constraints\PasswordStrengthValidator")

[Basic Usage](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#basic-usage "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------

The following constraint ensures that the `rawPassword` property of the `User` class reaches the minimum strength required by the constraint. By default, the minimum required score is `2`.

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
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class User
{
    #[Assert\PasswordStrength]
    protected $rawPassword;
}
```

1
2
3
4
5
```
# config/validator/validation.yaml
App\Entity\User:
    properties:
        rawPassword:
            - PasswordStrength
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
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\User">
        <property name="rawPassword">
            <constraint name="PasswordStrength"/>
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
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class User
{
    public static function loadValidatorMetadata(ClassMetadata $metadata)
    {
        $metadata->addPropertyConstraint('rawPassword', new Assert\PasswordStrength());
    }
}
```

[Available Options](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#available-options "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------

### [`minScore`](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#minscore "Permalink to this headline")

**type**: `integer`**default**: `PasswordStrength::STRENGTH_MEDIUM` (`2`)

The minimum required strength of the password. Available constants are:

*   `PasswordStrength::STRENGTH_WEAK` = `1`
*   `PasswordStrength::STRENGTH_MEDIUM` = `2`
*   `PasswordStrength::STRENGTH_STRONG` = `3`
*   `PasswordStrength::STRENGTH_VERY_STRONG` = `4`

`PasswordStrength::STRENGTH_VERY_WEAK` is available but only used internally or by a custom password strength estimator.

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
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class User
{
    #[Assert\PasswordStrength(
        minScore: PasswordStrength::STRENGTH_VERY_STRONG, // Very strong password required
    )]
    protected $rawPassword;
}
```

### [`message`](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#message "Permalink to this headline")

**type**: `string`**default**: `The password strength is too low. Please use a stronger password.`

The default message supplied when the password does not reach the minimum required score.

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
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class User
{
    #[Assert\PasswordStrength(
        message: 'Your password is too easy to guess. Company\'s security policy requires using a stronger password.'
    )]
    protected $rawPassword;
}
```

[Customizing the Password Strength Estimation](https://symfony.com/doc/current/reference/constraints/PasswordStrength.html#customizing-the-password-strength-estimation "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, this constraint calculates the strength of a password based on its length and the number of unique characters used. You can get the calculated password strength (e.g. to display it in the user interface) using the following static function:

1
2
3
```
use Symfony\Component\Validator\Constraints\PasswordStrengthValidator;

$passwordEstimatedStrength = PasswordStrengthValidator::estimateStrength($password);
```

If you need to override the default password strength estimation algorithm, you can pass a `Closure` to the [PasswordStrengthValidator](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraints/PasswordStrengthValidator.php "Symfony\Component\Validator\Constraints\PasswordStrengthValidator") constructor (e.g. using the [service closures](https://symfony.com/doc/current/service_container/service_closures.html)).

First, create a custom password strength estimation algorithm within a dedicated callable class:

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
namespace App\Validator;

class CustomPasswordStrengthEstimator
{
    /**
     * @return PasswordStrength::STRENGTH_*
     */
    public function __invoke(string $password): int
    {
        // Your custom password strength estimation algorithm
    }
}
```

Then, configure the [PasswordStrengthValidator](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/Constraints/PasswordStrengthValidator.php "Symfony\Component\Validator\Constraints\PasswordStrengthValidator") service to use your own estimator:

YAML PHP

1
2
3
4
5
6
7
```
# config/services.yaml
services:
    custom_password_strength_estimator:
        class: App\Validator\CustomPasswordStrengthEstimator

    Symfony\Component\Validator\Constraints\PasswordStrengthValidator:
        arguments: [!closure '@custom_password_strength_estimator']
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
```
// config/services.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use App\Validator\CustomPasswordStrengthEstimator;
use Symfony\Component\Validator\Constraints\PasswordStrengthValidator;

return App::config([
    'services' => [
        'custom_password_strength_estimator' => CustomPasswordStrengthEstimator::class,
        PasswordStrengthValidator::class => [
            'arguments' => [closure(service('custom_password_strength_estimator'))],
        ],
    ],
]);
```

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/4a372bd18f2b81d116c3e412bf834e43a6aba110)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQICE7DE23KC6BIE23IF6BIK23EF67DV27ECASDLKQJHEYI527ICEBDK23ECTNCYBZ52K)[Create a website that turns your practice into profit. Start your free trial.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQICE7DE23KC6BIE23IF6BIK23EF67DV27ECASDLKQJHEYI527ICEBDK23ECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 8: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.401293666;dc_trk_aid=593420487;dc_trk_cid=207494836;ord=177344950;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 9: Check Code Performance in Dev, Test, Staging & Production](https://symfony.com/images/network/blackfire_03.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)
[Check Code Performance in Dev, Test, Staging & Production](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)

[![Image 10: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 11: Avatar of Mouad ZIANI, a Symfony contributor](https://connect.symfony.com/api/images/95443bd0-dcea-42a7-a456-94540038fb7b.png?format=48x48)

Thanks **[Mouad ZIANI](https://connect.symfony.com/profile/mouadziani)** (**@mouadziani**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=mouadziani) • **16** lines changed

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
