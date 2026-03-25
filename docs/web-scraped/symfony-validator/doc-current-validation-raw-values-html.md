# Source: https://symfony.com/doc/current/validation/raw_values.html

Title: How to Validate Raw Values (Scalar Values and Arrays) (Symfony Docs)

URL Source: https://symfony.com/doc/current/validation/raw_values.html

Markdown Content:
How to Validate Raw Values (Scalar Values and Arrays) (Symfony Docs)
===============
[Skip to content](https://symfony.com/doc/current/validation/raw_values.html#main-content)

[Symfony Hub](https://symfony.com/doc/current/validation/raw_values.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/current/validation/raw_values.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) Learn Symfony today](https://symfony.com/book)[![Image 2](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)[![Image 3](https://connect.symfony.com/uploads/sln/9dcfe3b7-4ac7-4fd7-bdaa-d690f48b40da/48b70252-5e84-4200-ab44-fed8cd091b60.png) "Symfony: The Fast Track", a new book to learn Symfony](https://symfony.com/book)

[](https://symfony.com/doc/current/validation/raw_values.html# "Search")

[](https://symfony.com/doc/current/validation/raw_values.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/validation/raw_values.html)

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

[SymfonyOnline June 2026](https://live.symfony.com/2026-online-june)

June 11 – 12, 2026

100% Online

+20 talks and workshops

1.   [Home](https://symfony.com/)
2.   [Documentation](https://symfony.com/doc)
3.   [Validation](https://symfony.com/doc/current/validation.html)
4.    How to Validate Raw Values (Scalar Values and Arrays) 

 Search Symfony Docs 

Version:

How to Validate Raw Values (Scalar Values and Arrays)
=====================================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/validation/raw_values.rst)

Usually you will be validating entire objects. But sometimes, you want to validate a simple value - like to verify that a string is a valid email address. From inside a controller, it looks like this:

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
```
// ...
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Validator\ValidatorInterface;

// ...
public function addEmail(string $email, ValidatorInterface $validator): void
{
    $emailConstraint = new Assert\Email();
    // all constraint "options" can be set this way
    $emailConstraint->message = 'Invalid email address';

    // use the validator to validate the value
    $errors = $validator->validate(
        $email,
        $emailConstraint
    );

    if (!$errors->count()) {
        // ... this IS a valid email address, do something
    } else {
        // this is *not* a valid email address
        $errorMessage = $errors[0]->getMessage();

        // ... do something with the error
    }

    // ...
}
```

By calling `validate()` on the validator, you can pass in a raw value and the constraint object that you want to validate that value against. A full list of the available constraints - as well as the full class name for each constraint - is available in the [constraints reference](https://symfony.com/doc/current/reference/constraints.html) section.

Validation of arrays is possible using the `Collection` constraint:

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
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
```
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Validation;

$validator = Validation::createValidator();

$input = [
    'name' => [
        'first_name' => 'Fabien',
        'last_name' => 'Potencier',
    ],
    'email' => 'test@email.tld',
    'simple' => 'hello',
    'eye_color' => 3,
    'file' => null,
    'password' => 'test',
    'tags' => [
        [
            'slug' => 'symfony_doc',
            'label' => 'symfony doc',
        ],
    ],
];

$groups = new Assert\GroupSequence(groups: ['Default', 'custom']);

$constraint = new Assert\Collection(fields: [
    // the keys correspond to the keys in the input array
    'name' => new Assert\Collection(fields: [
        'first_name' => new Assert\Length(min: 101),
        'last_name' => new Assert\Length(min: 1),
    ]),
    'email' => new Assert\Email(),
    'simple' => new Assert\Length(min: 102),
    'eye_color' => new Assert\Choice(choices: [3, 4]),
    'file' => new Assert\File(),
    'password' => new Assert\Length(min: 60),
    'tags' => new Assert\Optional(constraints: [
        new Assert\Type(type: 'array'),
        new Assert\Count(min: 1),
        new Assert\All(constraints: [
            new Assert\Collection(fields: [
                'slug' => [
                    new Assert\NotBlank(),
                    new Assert\Type(type: 'string'),
                ],
                'label' => [
                    new Assert\NotBlank(),
                ],
            ]),
            new CustomUniqueTagValidator(groups: ['custom']),
        ]),
    ]),
]);

$violations = $validator->validate($input, $constraint, $groups);
```

The `validate()` method returns a [ConstraintViolationList](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolationList.php "Symfony\Component\Validator\ConstraintViolationList") object, which acts like an array of errors. Each error in the collection is a [ConstraintViolation](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Validator/ConstraintViolation.php "Symfony\Component\Validator\ConstraintViolation") object, which holds the error message on its `getMessage()` method.

Note

When using groups with the [Collection](https://symfony.com/doc/current/reference/constraints/Collection.html) constraint, be sure to use the `Optional` constraint when appropriate as explained in its reference documentation.

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license. 

 TOC 

 Search 

 Version 

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/84dc127dd611279d2e1851401dca56a0f28ebfa8)](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKCASI523NCKAIL53LCTYIP53YC6YDP27KC6SI5K7WCESDVK3EHJNCLSIZ)[Start an annual website plan, and get a free domain name with Squarespace.](https://srv.carbonads.net/ads/click/x/GTND427UCKBDP5QYCYALYKQUCABDT23UCEYIPZ3JCASIVKQYCTYDEKQKCASI523NCKAIL53LCTYIP53YC6YDP27KC6SI5K7WCESDVK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

![Image 8: ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B34445489.438308384;dc_trk_aid=631459208;dc_trk_cid=248949291;ord=177344965;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1?)

[![Image 9: Become certified from home](https://symfony.com/images/network/sf7certif_02.webp)](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=certifiedathome)
[Become certified from home](https://certification.symfony.com/?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=certifiedathome)

[![Image 10: Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://symfony.com/images/network/sltraining_01.webp)](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)
[Be trained by SensioLabs experts (2 to 6 day sessions -- French or English).](https://sensiolabs.com/training/courses?utm_source=symfony&utm_medium=symfony_ads&utm_campaign=permanent_referral)

Symfony footer
--------------

![Image 11: Avatar of Gerhard Seidel, a Symfony contributor](https://connect.symfony.com/api/images/5ea96469-ed3d-44d2-8327-54964c0c3905.png?format=48x48)

Thanks **[Gerhard Seidel](https://connect.symfony.com/profile/gseidel)** (**@gseidel**) for being a Symfony contributor

[**2** commits](https://github.com/symfony/symfony/commits?author=gseidel) • **25** lines changed

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
