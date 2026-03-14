# Source: https://symfony.com/doc/current/validation/groups.html

Title: How to Apply only a Subset of all Your Validation Constraints (Validation Groups) (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation/groups.html

Markdown Content:
How to Apply only a Subset of all Your Validation Constraints (Validation Groups) (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/validation/groups.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/validation/groups.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/validation/groups.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)[![Image 2](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io: Fire up your PHP apps performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)[![Image 3](https://connect.symfony.com/uploads/sln/1c5498dd-0649-4d42-af4b-1de957825f62/8a08e0e0-cc2d-490f-9a2f-882979624a7f.png) Blackfire.io: Fire up your PHP apps performance](https://www.blackfire.io/?utm_source=symfony&utm_medium=banner&utm_campaign=profiler)

[](https://symfony.com/doc/current/validation/groups.html# "Search")

[](https://symfony.com/doc/current/validation/groups.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/validation/groups.html)

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
3.   [Validation](https://symfony.com/doc/current/validation.html)
4.    How to Apply only a Subset of all Your Validation Constraints (Validation Groups) 

 Search Symfony Docs 

Version:

How to Apply only a Subset of all Your Validation Constraints (Validation Groups)
=================================================================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation/groups.rst)

By default, when validating an object all constraints of this class will be checked whether or not they actually pass. In some cases, however, you will need to validate an object against only _some_ constraints on that class. To do this, you can organize each constraint into one or more "validation groups" and then apply validation against one group of constraints.

For example, suppose you have a `User` class, which is used both when a user registers and when a user updates their contact information later:

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
17
18
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Security\Core\User\UserInterface;
use Symfony\Component\Validator\Constraints as Assert;

class User implements UserInterface
{
    #[Assert\Email(groups: ['registration'])]
    private string $email;

    #[Assert\NotBlank(groups: ['registration'])]
    #[Assert\Length(min: 7, groups: ['registration'])]
    private string $password;

    #[Assert\Length(min: 2)]
    private string $city;
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
```
# config/validator/validation.yaml
App\Entity\User:
    properties:
        email:
            - Email: { groups: [registration] }
        password:
            - NotBlank: { groups: [registration] }
            - Length: { min: 7, groups: [registration] }
        city:
            - Length:
                min: 2
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
31
32
33
34
35
36
37
38
39
```
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="
        http://symfony.com/schema/dic/constraint-mapping
        https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd
    ">

    <class name="App\Entity\User">
        <property name="email">
            <constraint name="Email">
                <option name="groups">
                    <value>registration</value>
                </option>
            </constraint>
        </property>

        <property name="password">
            <constraint name="NotBlank">
                <option name="groups">
                    <value>registration</value>
                </option>
            </constraint>
            <constraint name="Length">
                <option name="min">7</option>
                <option name="groups">
                    <value>registration</value>
                </option>
            </constraint>
        </property>

        <property name="city">
            <constraint name="Length">
                <option name="min">2</option>
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
24
25
26
27
```
// src/Entity/User.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class User
{
    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint('email', new Assert\Email(
            groups: ['registration'],
        ));

        $metadata->addPropertyConstraint('password', new Assert\NotBlank(
            groups: ['registration'],
        ));
        $metadata->addPropertyConstraint('password', new Assert\Length(
            min: 7,
            groups: ['registration'],
        ));

        $metadata->addPropertyConstraint('city', new Assert\Length(
            min: 2,
        ));
    }
}
```

With this configuration, there are three validation groups:

`Default` Contains the constraints in the current class and all referenced classes that belong to no other group. In this example, it only contains the `city` field. `User` Equivalent to all constraints of the `User` object in the `Default` group. This is always the name of the class. The difference between this and `Default` is explained in [How to Sequentially Apply Validation Groups](https://symfony.com/doc/current/validation/sequence_provider.html). `registration` This is a custom validation group, so it only contains the constraints that are explicitly associated with it. In this example, only the `email` and `password` fields. 
Constraints in the `Default` group of a class are the constraints that have either no explicit group configured or that are configured to a group equal to the class name or the string `Default`.

Warning

When validating _just_ the User object, there is no difference between the `Default` group and the `User` group. But, there is a difference if `User` has embedded objects. For example, imagine `User` has an `address` property that contains some `Address` object and that you've added the [Valid](https://symfony.com/doc/current/reference/constraints/Valid.html) constraint to this property so that it's validated when you validate the `User` object.

If you validate `User` using the `Default` group, then any constraints on the `Address` class that are in the `Default` group _will_ be used. But, if you validate `User` using the `User` validation group, then only constraints on the `Address` class with the `User` group will be validated.

In other words, the `Default` group and the class name group (e.g. `User`) are identical, except when the class is embedded in another object that's actually the one being validated.

If you have inheritance (e.g. `User extends BaseUser`) and you validate with the class name of the subclass (i.e. `User`), then all constraints in the `User` and `BaseUser` will be validated. However, if you validate using the base class (i.e. `BaseUser`), then only the default constraints in the `BaseUser` class will be validated.

To tell the validator to use a specific group, pass one or more group names as the third argument to the `validate()` method:

1`$errors = $validator->validate($author, null, ['registration']);`

If no groups are specified, all constraints that belong to the group `Default` will be applied.

In a full stack Symfony project, you'll usually work with validation indirectly through the form library. For information on how to use validation groups inside forms, see [Configuring Validation Groups in Forms](https://symfony.com/doc/current/form/validation_groups.html).

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/84dc127dd611279d2e1851401dca56a0f28ebfa8)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKC67D4KQJCYBICKJICY7DCKJLCVBI523IHEYI527ICEBDK23ECTNCYBZ52K)[Start an annual website plan, and get a free domain name with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKC67D4KQJCYBICKJICY7DCKJLCVBI523IHEYI527ICEBDK23ECTNCYBZ52K)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 8: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B34445489.438308384;dc_trk_aid=631459208;dc_trk_cid=248949291;ord=177344962;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 9: Become certified from home](https://symfony.com/images/network/sy1certif_01.webp)](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertifiedathome)
[Become certified from home](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertifiedathome)

[![Image 10: Make sure your project is risk free](https://symfony.com/images/network/sfinsight_01.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=riskfree)
[Make sure your project is risk free](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=riskfree)

Symfony footer
--------------

![Image 11: Avatar of Jeremy Benoist, a Symfony contributor](https://www.gravatar.com/avatar/5bbb490b6d742d393756aa089d6fff02?size=48&rating=g&default=retro)

Thanks **Jeremy Benoist** for being a Symfony contributor

**1** commit • **4** lines changed

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
