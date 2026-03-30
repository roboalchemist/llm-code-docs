# Source: https://symfony.com/doc/8.0/frontend.html

Title: Front-end Tools: Handling CSS & JavaScript (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/frontend.html

Markdown Content:
Front-end Tools: Handling CSS & JavaScript (Symfony Docs)
===============

[Skip to content](https://symfony.com/doc/8.0/frontend.html#main-content)

[Symfony Hub](https://symfony.com/doc/8.0/frontend.html# "Toggle Symfony menu")[SF H](https://symfony.com/doc/8.0/frontend.html# "Toggle Symfony menu")

[![Image 1](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight](https://insight.symfony.com/)[![Image 2](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight: The life jacket for your projects](https://insight.symfony.com/)[![Image 3](https://connect.symfony.com/uploads/sln/1991a94e-4351-4af1-88ab-4f17f6d20f45/8697a26e-20ac-429a-8da7-510bf022a7c8.png) SymfonyInsight helps you protect your projects against security issues and technical debt.](https://insight.symfony.com/)

[](https://symfony.com/doc/8.0/frontend.html# "Search")

[](https://symfony.com/doc/8.0/frontend.html# "Search")Search

[Connect](https://symfony.com/connect/login?target=https://symfony.com/doc/current/frontend.html)

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

[SymfonyDay Montreal 2026](https://live.symfony.com/2026-montreal)

June 4, 2026

+20 talks and workshops

Register now

1. [Home](https://symfony.com/)
2. [Documentation](https://symfony.com/doc)
3. Front-end Tools: Handling CSS & JavaScript

 Search Symfony Docs

Version:

Table of Contents

* [Using PHP & Twig](https://symfony.com/doc/8.0/frontend.html#using-php-twig)
  * [AssetMapper (Recommended)](https://symfony.com/doc/8.0/frontend.html#assetmapper-recommended)
  * [Webpack Encore](https://symfony.com/doc/8.0/frontend.html#webpack-encore)
  * [Stimulus & Symfony UX Components](https://symfony.com/doc/8.0/frontend.html#stimulus-symfony-ux-components)

* [Using a Front-end Framework (React, Vue, Svelte, etc)](https://symfony.com/doc/8.0/frontend.html#using-a-front-end-framework-react-vue-svelte-etc)
* [Other Front-End Articles](https://symfony.com/doc/8.0/frontend.html#other-front-end-articles)

Front-end Tools: Handling CSS & JavaScript
==========================================

[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/frontend.rst)

Symfony gives you the flexibility to choose any front-end tools you want. There are generally two approaches:

1. [building your HTML with PHP & Twig](https://symfony.com/doc/8.0/frontend.html#frontend-twig-php);
2. [building your frontend with a JavaScript framework](https://symfony.com/doc/8.0/frontend.html#frontend-js) like React, Vue, Svelte, etc.

Both work great - and are discussed below.

[Using PHP & Twig](https://symfony.com/doc/8.0/frontend.html#using-php-twig "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

Symfony comes with two powerful options to help you build a modern and fast frontend:

* [AssetMapper](https://symfony.com/doc/8.0/frontend.html#frontend-asset-mapper) (recommended for new projects) runs entirely in PHP, doesn't require any build step and leverages modern web standards.
* [Webpack Encore](https://symfony.com/doc/8.0/frontend.html#frontend-webpack-encore) is built with [Node.js](https://nodejs.org/) on top of [Webpack](https://webpack.js.org/).

|  | AssetMapper | Encore |
| --- | --- | --- |
| Production Ready? | yes | yes |
| Stable? | yes | yes |
| Requirements | none | Node.js |
| Requires a build step? | no | yes |
| Works in all browsers? | yes | yes |
| Supports [Stimulus/UX](https://symfony.com/bundles/StimulusBundle/current/index.html) | yes | yes |
| Supports Sass/Tailwind | [yes](https://symfony.com/doc/8.0/frontend/asset_mapper.html#asset-mapper-tailwind) | yes |
| Supports React, Vue, Svelte? | yes [[1]](https://symfony.com/doc/8.0/frontend.html#ux-note-1) | yes |
| Supports TypeScript | [yes](https://symfony.com/doc/8.0/frontend/asset_mapper.html#asset-mapper-ts) | yes |
| Removes comments from JavaScript | no [[2]](https://symfony.com/doc/8.0/frontend.html#ux-note-2) | yes |
| Removes comments from CSS | no [[2]](https://symfony.com/doc/8.0/frontend.html#ux-note-2) | yes [[4]](https://symfony.com/doc/8.0/frontend.html#ux-note-4) |
| Versioned assets | always | optional |
| Can update 3rd party packages | yes | no [[3]](https://symfony.com/doc/8.0/frontend.html#ux-note-3) |

**[1]** Using JSX (React), Vue, etc with AssetMapper is possible, but you'll need to use their native tools for pre-compilation. Also, some features (like Vue single-file components) cannot be compiled down to pure JavaScript that can be executed by a browser.

**[2]** You can install the [SensioLabs Minify Bundle](https://github.com/sensiolabs/minify-bundle) to minify CSS/JS code (and remove all comments) when compiling assets with AssetMapper.

**[3]** If you use `npm`, there are update checkers available (e.g. `npm-check`).

**[4]** CSS comments can be removed using [CssMinimizerPlugin](https://webpack.js.org/plugins/css-minimizer-webpack-plugin), which is included in Webpack Encore and configurable via `Encore.configureCssMinimizerPlugin()`.

### [AssetMapper (Recommended)](https://symfony.com/doc/8.0/frontend.html#assetmapper-recommended "Permalink to this headline")

Screencast

Do you prefer video tutorials? Check out the [AssetMapper screencast series](https://symfonycasts.com/screencast/asset-mapper).

AssetMapper is the recommended system for handling your assets. It runs entirely in PHP with no complex build step or dependencies. It does this by leveraging the `importmap` feature of your browser, which is available in all browsers thanks to a polyfill.

[Read the AssetMapper Documentation](https://symfony.com/doc/8.0/frontend/asset_mapper.html)

### [Webpack Encore](https://symfony.com/doc/8.0/frontend.html#webpack-encore "Permalink to this headline")

Screencast

Do you prefer video tutorials? Check out the [Webpack Encore screencast series](https://symfonycasts.com/screencast/webpack-encore).

[Webpack Encore](https://www.npmjs.com/package/@symfony/webpack-encore) is a simpler way to integrate [Webpack](https://webpack.js.org/) into your application. It wraps Webpack, giving you a clean & powerful API for bundling JavaScript modules, pre-processing CSS & JS and compiling and minifying assets.

[Read the Encore Documentation](https://symfony.com/doc/8.0/frontend/encore/index.html)

#### [Switch from AssetMapper](https://symfony.com/doc/8.0/frontend.html#switch-from-assetmapper "Permalink to this headline")

By default, new Symfony webapp projects (created with `symfony new --webapp myapp`) use AssetMapper. If you still need to use Webpack Encore, use the following steps to switch. This is best done on a new project and provides the same features (Turbo/Stimulus) as the default webapp.

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
# Remove AssetMapper & Turbo/Stimulus temporarily
$ composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundle

# Add Webpack Encore & Turbo/Stimulus back
$ composer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle

# Install & Build Assets
$ npm install
$ npm run dev
```

### [Stimulus & Symfony UX Components](https://symfony.com/doc/8.0/frontend.html#stimulus-symfony-ux-components "Permalink to this headline")

Once you've installed AssetMapper or Webpack Encore, it's time to start building your front-end. You can write your JavaScript however you want, but we recommend using [Stimulus](https://stimulus.hotwired.dev/), [Turbo](https://turbo.hotwired.dev/) and a set of tools called [Symfony UX](https://ux.symfony.com/).

To learn about Stimulus & the UX Components, see the [StimulusBundle Documentation](https://symfony.com/bundles/StimulusBundle/current/index.html)

[Using a Front-end Framework (React, Vue, Svelte, etc)](https://symfony.com/doc/8.0/frontend.html#using-a-front-end-framework-react-vue-svelte-etc "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Screencast

Do you prefer video tutorials? Check out the [API Platform screencast series](https://symfonycasts.com/screencast/api-platform).

If you want to use a front-end framework (Next.js, React, Vue, Svelte, etc), we recommend using their native tools and using Symfony as a pure API. A wonderful tool to do that is [API Platform](https://api-platform.com/). Their standard distribution comes with a Symfony-powered API backend, frontend scaffolding in Next.js (other frameworks are also supported) and a React admin interface. It comes fully Dockerized and even contains a web server.

[Other Front-End Articles](https://symfony.com/doc/8.0/frontend.html#other-front-end-articles "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

* [Create a UX bundle](https://symfony.com/doc/8.0/frontend/create_ux_bundle.html)
* [How to Use a Custom Version Strategy for Assets](https://symfony.com/doc/8.0/frontend/custom_version_strategy.html)
* [Passing Information from Twig to JavaScript](https://symfony.com/doc/8.0/frontend/server-data.html)

 This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

 TOC

 Search

 Version

**Symfony 8.0**[backers](https://symfony.com/backers)

[](https://sulu.io/)

[](https://jb.gg/fbsk8y)

[![Image 7: ads via Carbon](https://srv.carbonads.net/static/30242/70cc0e30a452d507609b098b06c11cd5d85af10b)](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I553ICWAITZ3JCASIC53UFT7DLKQKCW7DE277CVBIT2JYCYYIE23LCWAIV53KC6SI5K7JF6YDEK3EHJNCLSIZ)[High-Performance PDF SDK for Developers. Code Without Limits. Try for Free.](https://srv.carbonads.net/ads/click/x/GTND427UCKYILKQNF67LYKQUCA7I553ICWAITZ3JCASIC53UFT7DLKQKCW7DE277CVBIT2JYCYYIE23LCWAIV53KC6SI5K7JF6YDEK3EHJNCLSIZ)[ads via Carbon](http://carbonads.net/?utm_source=symfonycom&utm_medium=ad_via_link&utm_campaign=in_unit&utm_term=carbon)

[![Image 8: Check Code Performance in Dev, Test, Staging & Production](https://symfony.com/images/network/blackfire_03.png)](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)
[Check Code Performance in Dev, Test, Staging & Production](https://www.blackfire.io/profiler?utm_source=symfony&utm_medium=ad_black_logo&utm_campaign=profiler)

[![Image 9: Get your Sylius expertise recognized](https://symfony.com/images/network/sy1certif_01.webp)](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliusrecognized)
[Get your Sylius expertise recognized](https://certification.symfony.com/exams/sylius.html?utm_source=ad&utm_medium=banner&utm_campaign=certification&utm_content=syliusrecognized)

Symfony footer
--------------

![Image 10: Avatar of Peter van Dommelen, a Symfony contributor](https://www.gravatar.com/avatar/e0823e7189cc4c2970d1022cab747d10?size=48&rating=g&default=retro)

Thanks **Peter van Dommelen** for being a Symfony contributor

**1** commit • **30** lines changed

[View all contributors](https://symfony.com/contributors) that help us make Symfony

### Become a Symfony contributor

Be an active part of the community and contribute ideas, code and bug fixes. Both experts and newcomers are welcome.

[Learn how to contribute](https://symfony.com/doc/current/contributing/index.html)

![Image 11](https://symfony.com/assets/icons/logos/sf-20years-wordmark-dark--dFsFxh.webp)
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
