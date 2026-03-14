# Source: https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/

Title: Jetpack Search

URL Source: https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/

Published Time: 2021-03-05T17:23:28Z

Markdown Content:
Jetpack Search · WordPress VIP Documentation
===============
[Skip to content](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#site-content)

Ready to get started with WordPress VIP? [Contact us](https://wpvip.com/contact/)

[Documentation](https://docs.wpvip.com/)

Search Search

 Menu

Search Search

[Home](https://docs.wpvip.com/)
### [WordPress on VIP](https://docs.wpvip.com/wordpress-on-vip/)

*   [Action Scheduler](https://docs.wpvip.com/wordpress-on-vip/action-scheduler/)
*   [Autoloaded options](https://docs.wpvip.com/wordpress-on-vip/autoloaded-options/)
*   [Block editor](https://docs.wpvip.com/wordpress-on-vip/block-editor/)
*   [Customize user roles](https://docs.wpvip.com/wordpress-on-vip/customize-user-roles/)
*   [Drop-ins](https://docs.wpvip.com/wordpress-on-vip/drop-ins/)
*   [Email](https://docs.wpvip.com/wordpress-on-vip/email/)
    *   [Send emails from a custom domain](https://docs.wpvip.com/wordpress-on-vip/email/send-from-custom-domain/)

*   [Jetpack](https://docs.wpvip.com/wordpress-on-vip/jetpack/)
    *   [Jetpack connections](https://docs.wpvip.com/wordpress-on-vip/jetpack/connections/)
    *   [Version updates for Jetpack](https://docs.wpvip.com/wordpress-on-vip/jetpack/version-updates/)
    *   [Control Jetpack content distribution](https://docs.wpvip.com/wordpress-on-vip/jetpack/content-distribution/)

*   [Obtaining a local time](https://docs.wpvip.com/wordpress-on-vip/local-time/)
*   [PHP](https://docs.wpvip.com/wordpress-on-vip/php/)
    *   [PHP error reporting](https://docs.wpvip.com/wordpress-on-vip/php/error-reporting/)
    *   [PHP sessions](https://docs.wpvip.com/wordpress-on-vip/php/php-sessions/)
    *   [Version updates for PHP](https://docs.wpvip.com/wordpress-on-vip/php/versions/)
        *   [Automated tests for PHP version compatibility](https://docs.wpvip.com/wordpress-on-vip/php/versions/automated-tests/)
        *   [PHP linting for PHP version compatibility](https://docs.wpvip.com/wordpress-on-vip/php/versions/php-linting-scans/)
        *   [PHPCS scans for PHP version compatibility](https://docs.wpvip.com/wordpress-on-vip/php/versions/phpcs-scans/)
        *   [Prepare application code for a PHP version update](https://docs.wpvip.com/wordpress-on-vip/php/versions/code-scanning-for-php-upgrade/)
        *   [Static analysis tools for PHP version compatibility](https://docs.wpvip.com/wordpress-on-vip/php/versions/static-analysis/)
        *   [Test a PHP update on a VIP Platform environment](https://docs.wpvip.com/wordpress-on-vip/php/versions/platform-environment-tests/)

*   [Post revisions](https://docs.wpvip.com/wordpress-on-vip/post-revisions/)
*   [Search options](https://docs.wpvip.com/wordpress-on-vip/search-options/)
    *   [Comparison of Elasticsearch options on WordPress VIP](https://docs.wpvip.com/wordpress-on-vip/search-options/comparing-search-options/)
    *   [Core WordPress search functionality](https://docs.wpvip.com/wordpress-on-vip/search-options/wordpress-search/)
    *   [Elasticsearch](https://docs.wpvip.com/wordpress-on-vip/search-options/elasticsearch/)
    *   [Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/)

*   [Version updates for WordPress](https://docs.wpvip.com/wordpress-on-vip/wordpress-upgrades/)
*   [WordPress multisite](https://docs.wpvip.com/wordpress-on-vip/multisites/)
    *   [Add a network site](https://docs.wpvip.com/wordpress-on-vip/multisites/create-new-sites/)
    *   [Database structure for multisites](https://docs.wpvip.com/wordpress-on-vip/multisites/database-structure/)
    *   [Network Sites](https://docs.wpvip.com/wordpress-on-vip/multisites/network-sites/)
    *   [Subdomain and subdirectory structures](https://docs.wpvip.com/wordpress-on-vip/multisites/subdomains-subdirectories/)
    *   [sunrise.php](https://docs.wpvip.com/wordpress-on-vip/multisites/sunrise-php/)
    *   [Update the Site Address (URL) of a network site](https://docs.wpvip.com/wordpress-on-vip/multisites/update-site-address-url/)

*   [WordPress REST API](https://docs.wpvip.com/wordpress-on-vip/wordpress-rest-api/)
*   [WordPress single site](https://docs.wpvip.com/wordpress-on-vip/wordpress-single-site/)
*   [WP-Cron](https://docs.wpvip.com/wordpress-on-vip/cron-control/)

Updates
-------

*   [Changelog](https://docs.wpvip.com/changelog/)
*   [WordPress VIP Status](https://wpvipstatus.com/)
*   [VIP Lobby](https://lobby.vip.wordpress.com/)

*   [Contact Support](https://wordpressvip.zendesk.com/)
*   [Trust Center](https://wpvip.com/trust/)
*   [Resource Library](https://wpvip.com/resources/)
*   [Parse.ly Help](https://docs.parse.ly/)
*   [Privacy Policy](https://wpvip.com/privacy/)
*   [Accessibility at WordPress VIP](https://wpvip.com/accessibility/)

1.   [WordPress on VIP](https://docs.wpvip.com/wordpress-on-vip/)
2.   [Search options](https://docs.wpvip.com/wordpress-on-vip/search-options/)
3.   Jetpack Search

Jetpack Search
==============

Table of contents
-----------------

*   [Enable Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-enable-jetpack-search "Enable Jetpack Search")
*   [Enable Jetpack Search on a non-production site](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#1-enable-jetpack-search-on-a-non-production-site "Enable Jetpack Search on a non-production site")
*   [Offload a front-end query to Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-offload-a-front-end-query-to-jetpack-search "Offload a front-end query to Jetpack Search")

[Jetpack Search](https://jetpack.com/support/search/) is a paid upgrade to the [Jetpack plugin](https://jetpack.com/) that improves the search experience for WordPress sites. Jetpack Search uses [Elasticsearch](https://www.elastic.co/what-is/elasticsearch) for indexing and searching, typically without any need for a site owner to add custom code.

When enabled on a VIP site, Jetpack Instant Search syncs content changes to a private cache site located within Automattic’s data centers, and uses that cached copy to perform indexing. When search queries are performed on the VIP site, the database query is sent to a public endpoint which only returns results for publicly available data.

*   The first 100,000 records of a VIP site’s Jetpack Search index are free; [additional records are billable by Jetpack](https://jetpack.com/support/search/jetpack-search-product-billing/).
*   Jetpack Search is enabled per-network site on WordPress multisite environments.

[Enable Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-enable-jetpack-search)
-----------------------------------------------------------------------------------------------------------------------

[Top ↑](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#a8c-docs-toc-content)
To enable Jetpack Search on a production WordPress site:

1.   [Create a VIP Support request](https://wordpressvip.zendesk.com/) and specify the site for which Jetpack Search should be enabled.
2.   VIP Support will communicate in the support ticket when this is complete and Jetpack Search is ready to use.

[Enable Jetpack Search on a non-production site](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#1-enable-jetpack-search-on-a-non-production-site)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Top ↑](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#a8c-docs-toc-content)
Enabling Jetpack Search on a non-production WordPress site requires a VIP Support request as well as code-enablement. After VIP Support has enabled Jetpack Search on a non-production site, it will not work as expected until Jetpack’s search module is force-enabled via code.

To enable Jetpack Search on a non-production WordPress site:

1.   [Create a VIP Support request](https://wordpressvip.zendesk.com/) and specify the site for which Jetpack Search should be enabled.
2.   VIP Support will communicate in the support ticket when this is complete and Jetpack Search is ready to use.
3.   Force-enable the Jetpack search module on a non-production site with the `jetpack_active_modules` filter. Add the following code snippet to a file in `/client-mu-plugins/` within the branch that deploys to the environment of the non-production site:

/client-mu-plugins/plugin-name.php

```php
/**
 * Force Jetpack 'search' module to be active.
 *
 * @param array $modules
 *
 * @return array
 */

function enable_jetpack_search( $modules ) {
    $modules[] = 'search';
    return array_unique( $modules );
}

add_filter( 'jetpack_active_modules', 'enable_jetpack_search', 9999 );
```
Copy Copied

When adding this code to a WordPress multisite, additional logic may be needed in order for the `jetpack_active_modules` filter to only be applied to a specific network site(s).

[Offload a front-end query to Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-offload-a-front-end-query-to-jetpack-search)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Top ↑](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#a8c-docs-toc-content)
Jetpack Search is only able to handle front-end search queries (whereas Enterprise Search is able to [offload front-end and non-standard queries](https://docs.wpvip.com/vip-search/es-enable-non-search-queries/)). To offload an existing front-end query to the Jetpack Search index, `'es' => 'true'` must be set for those `WP_Query` parameters. Supported queries that are sent to the Jetpack Search index will obtain a list of matching post IDs, and a MySQL query will then fetch the post data.

In this code example, the `pre_get_posts` filter is used to enable offloading queries for category pages, tag pages, and author pages to the Jetpack Search index:

```php
/**
* Enable Elastic search for category, tag and author pages.
*
* This is optional, and only necessary if you need Jetpack search
* for these queries
*
* @param $query
*/
function vip_s__maybe_enable_es_wp_query( $query ) {

        if ( is_admin() || ! $query->is_main_query() ) {
                return;
        }

        if ( $query->is_category() || $query->is_tag() || $query->is_author() ) {
                $query->set( 'es', 'true' );
        }
}

add_action( 'pre_get_posts', 'vip_s__maybe_enable_es_wp_query' );
```
Copy Copied

Last updated: July 16, 2024

* * *

Contact WordPress VIP
---------------------

Have a question, or ready to get started with WordPress VIP?

*   [Contact Support](https://wordpressvip.zendesk.com/)
*   [Contact Sales](https://wpvip.com/contact/)

* * *

Documentation is licensed under a

[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)

[An Automattic Creation](https://automattic.com/)

Relevant to
-----------

*   WordPress

Table of contents
-----------------

*   [Enable Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-enable-jetpack-search "Enable Jetpack Search")
*   [Enable Jetpack Search on a non-production site](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#1-enable-jetpack-search-on-a-non-production-site "Enable Jetpack Search on a non-production site")
*   [Offload a front-end query to Jetpack Search](https://docs.wpvip.com/wordpress-on-vip/search-options/jetpack-search/#h-offload-a-front-end-query-to-jetpack-search "Offload a front-end query to Jetpack Search")

As an open source company, we take your privacy seriously and want to be as transparent as possible. So: We use cookies to collect some personal data from you (like your browsing data, IP addresses, and other unique identifiers). Some of these cookies we absolutely need in order to make things work, and others you can choose in order to optimize your experience while using our site and services.

Customize Accept all

As an open source company, we take your privacy seriously and want to be as transparent as possible. So: We use cookies to collect some personal data from you (like your browsing data, IP addresses, and other unique identifiers). Some of these cookies we absolutely need in order to make things work, and others you can choose in order to optimize your experience while using our site and services.

- [x] 

**Required**
These cookies are essential for our websites and services to perform basic functions and are necessary for us to operate certain features, like allowing registered users to authenticate and perform account-related functions, storing preferences set by users (like account name, language, and location), and ensuring our services operate properly.

- [x] 

**Analytics**
These cookies allow us to optimize performance by collecting information on how users interact with our websites.

- [x] 

**Advertising**
We and our advertising partners set these cookies to provide you with relevant content and to understand that content’s effectiveness.

Accept selection

![Image 1](https://pixel.wp.com/g.gif?v=ext&blog=182304402&post=3184&tz=0&srv=docs.wpvip.com&hp=vip&ac=35&amp=0&j=1%3A15.5-beta&host=docs.wpvip.com&ref=&fcp=436&rand=0.9233530187342732)
