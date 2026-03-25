# Source: https://symfony.com/doc/current/validation/translations.html

Title: How to Translate Validation Constraint Messages (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation/translations.html

Markdown Content:
How to Translate Validation Constraint Messages (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/validation/translations.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/validation/translations.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/validation/translations.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) Learn Symfony today](https://symfony.com/book)[![Image 2](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)[![Image 3](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)

[](https://symfony.com/doc/current/validation/translations.html# "Search")

[](https://symfony.com/doc/current/validation/translations.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/validation/translations.html)

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

[SymfonyDay Montreal 2026](https://live.symfony.com/2026-montreal)

June 4, 2026

+20 talks and workshops

Register now

1.   [Home](https://symfony.com/)
2.   [Documentation](https://symfony.com/doc)
3.   [Validation](https://symfony.com/doc/current/validation.html)
4.    How to Translate Validation Constraint Messages 

 Search Symfony Docs 

Version:

*   [Custom Translation Domain](https://symfony.com/doc/current/validation/translations.html#custom-translation-domain)

How to Translate Validation Constraint Messages
===============================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation/translations.rst)

The validation constraints used in forms can translate their error messages by creating a translation resource for the `validators`[translation domain](https://symfony.com/doc/current/translation.html#translation-resource-locations).

First of all, install the Symfony translation component (if it's not already installed in your application) running the following command:

 Copy

1`$ composer require symfony/translation`

Suppose you've created a plain-old-PHP object that you need to use somewhere in your application:

1
2
3
4
5
6
7
```
// src/Entity/Author.php
namespace App\Entity;

class Author
{
    public string $name;
}
```

Add constraints through any of the supported methods. Set the message option to the translation source text. For example, to guarantee that the `$name` property is not empty, add the following:

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
// src/Entity/Author.php
namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class Author
{
    #[Assert\NotBlank(message: 'author.name.not_blank')]
    public string $name;
}
```

1
2
3
4
5
```
# config/validator/validation.yaml
App\Entity\Author:
    properties:
        name:
            - NotBlank: { message: 'author.name.not_blank' }
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
<!-- config/validator/validation.xml -->
<?xml version="1.0" encoding="UTF-8" ?>
<constraint-mapping xmlns="http://symfony.com/schema/dic/constraint-mapping"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/constraint-mapping
        https://symfony.com/schema/dic/constraint-mapping/constraint-mapping-1.0.xsd">

    <class name="App\Entity\Author">
        <property name="name">
            <constraint name="NotBlank">
                <option name="message">author.name.not_blank</option>
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
```
// src/Entity/Author.php
namespace App\Entity;

// ...
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Mapping\ClassMetadata;

class Author
{
    public string $name;

    public static function loadValidatorMetadata(ClassMetadata $metadata): void
    {
        $metadata->addPropertyConstraint('name', new Assert\NotBlank(
            message: 'author.name.not_blank',
        ));
    }
}
```

Now, create a `validators` catalog file in the `translations/` directory:

XML YAML PHP

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
<!-- translations/validators/validators.en.xlf -->
<?xml version="1.0" encoding="UTF-8" ?>
<xliff version="1.2" xmlns="urn:oasis:names:tc:xliff:document:1.2">
    <file source-language="en" datatype="plaintext" original="file.ext">
        <body>
            <trans-unit id="author.name.not_blank">
                <source>author.name.not_blank</source>
                <target>Please enter an author name.</target>
            </trans-unit>
        </body>
    </file>
</xliff>
```

1
2
```
# translations/validators/validators.en.yaml
author.name.not_blank: Please enter an author name.
```

1
2
3
4
```
// translations/validators/validators.en.php
return App::config([
    'author.name.not_blank' => 'Please enter an author name.',
]);
```

You may need to clear your cache (even in the dev environment) after creating this file for the first time.

Tip

Symfony will also create translation files for the built-in validation messages. You can optionally set the [enabled_locales](https://symfony.com/doc/current/reference/configuration/framework.html#reference-translator-enabled-locales) option to restrict the available locales in your application. This will improve performance a bit because Symfony will only generate the translation files for those locales instead of all of them.

You can also use [TranslatableMessage](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Translation/TranslatableMessage.php "Symfony\Component\Translation\TranslatableMessage") to build your violation message:

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
use Symfony\Component\Translation\TranslatableMessage;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Context\ExecutionContextInterface;

#[Assert\Callback]
public function validate(ExecutionContextInterface $context, mixed $payload): void
{
    // somehow you have an array of "fake names"
    $fakeNames = [/* ... */];

    // check if the name is actually a fake name
    if (in_array($this->getFirstName(), $fakeNames, true)) {
        $context->buildViolation(new TranslatableMessage('author.name.fake', [], 'validators'))
            ->atPath('firstName')
            ->addViolation()
        ;
    }
}
```

You can learn more about translatable messages in [the dedicated section](https://symfony.com/doc/current/translation.html#translatable-objects).

[Custom Translation Domain](https://symfony.com/doc/current/validation/translations.html#custom-translation-domain "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------

The default translation domain can be changed globally using the `FrameworkBundle` configuration:

YAML PHP

1
2
3
4
```
# config/packages/validator.yaml
framework:
    validation:
        translation_domain: validation_errors
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
```
// config/packages/validator.php
namespace Symfony\Component\DependencyInjection\Loader\Configurator;

return App::config([
    'framework' => [
        'validation' => [
            'translation_domain' => 'validation_errors',
        ],
    ],
]);
```

Or it can be customized for a specific violation from a constraint validator:

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
public function validate($value, Constraint $constraint): void
{
    // validation logic

    $this->context->buildViolation($constraint->message)
        ->setParameter('{{ string }}', $value)
        ->setTranslationDomain('validation_errors')
        ->addViolation();
}
```

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/14dd57f2b8ca28bc6e6b0d3c3db360539e38d88a)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEK3KCYYDE277CVAD653WF6SDP53IC6SD4K3KC6SI5K7WCESDVK3EHJNCLSIZ)[Review requests, book clients, and get paid with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEK3KCYYDE277CVAD653WF6SDP53IC6SD4K3KC6SI5K7WCESDVK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 8: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611894;dc_trk_aid=613858970;dc_trk_cid=235700574;ord=177344968;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 9: Online exam, become Sylius certified today](https://symfony.com/images/network/sy1certif_01.webp)](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertified)
[Online exam, become Sylius certified today](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliuscertified)

[![Image 10: Make sure your project is risk free](https://symfony.com/images/network/sfinsight_01.png)](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=riskfree)
[Make sure your project is risk free](https://insight.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=insight&utm_content=riskfree)

Symfony footer
--------------

![Image 11: Avatar of Benjamin Toussaint, a Symfony contributor](https://connect.symfony.com/api/images/22610e57-a63a-44d8-b941-c89df49692f7.png?format=48x48)

Thanks **[Benjamin Toussaint](https://connect.symfony.com/profile/bto)** (**@bto**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=benjamintoussaint) • **82** lines changed

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
