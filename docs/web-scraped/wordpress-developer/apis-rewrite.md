# Rewrite

**Source:** [https://developer.wordpress.org/apis/rewrite/](https://developer.wordpress.org/apis/rewrite/)



# Rewrite




## In this article


Table of Contents- Description
- API Reference



↑Back to top



## Description


WordPress allows theme and plugin developers to programmatically specify new, custom rewrite rules.


The following functions (which are mostly aliases forWP_Rewritemethods) can be used to achieve this.


Please note that these rules are usually called inside theinithook. Furthermore, permalinks will need to be refreshed (you can do this from WP-Admin under Settings -> Permalinks) before the rewrite changes will take effect. Requires one-time use offlush_rules()to take effect.


## API Reference


#### Articles


- Class:WP_Rewrite– An overview of WordPress’s built-in URL rewrite class.


#### Hooks


- Filter:root_rewrite_rules– Filters the rewrite rules generated for the root of your weblog.
- Filter:post_rewrite_rules– Filters the rewrite rules generated for permalink URLs.
- Filter:page_rewrite_rules– Filters the rewrite rules generated for your Pages.
- Filter:date_rewrite_rules– Filters the rewrite rules generated for dated archive URLs.
- Filter:search_rewrite_rules– Filters the rewrite rules generated for search URLs.
- Filter:comments_rewrite_rules– Filters the rewrite rules generated for the latest comment feed URLs.
- Filter:author_rewrite_rules– Filters the rewrite rules generated for author archive URLs.
- Filter:rewrite_rules_array– Filtersallthe rewrite rules at once.
- Filter:{$permastructname}_rewrite_rules– Can be used to create or modify rewrite rules for any custom permastructs, such as taxonomies or custom post types.
- Action:generate_rewrite_rules– Runsafterall the rules have been created.


#### Functions


- add_rewrite_tag()– Can be used to allow WordPress to recognize custom variables (particularly custom querystring variables).
- add_rewrite_rule()– Allows you to specify new, custom rewrite rules.
- add_rewrite_endpoint()– Add a new endpoint like /trackback/
- flush_rules()– Regenerate the rewrite rules and save them to the database.
- flush_rewrite_rules()– Remove rewrite rules and then recreate rewrite rules.
- generate_rewrite_rules()– Generates rewrite rules from a permalink structure
- add_permastruct()– Add a new permastruct
- add_feed()– Add a new feed type like/atom1/





First published


August 12, 2019


Last updated


November 21, 2022



[PreviousRESTPrevious: REST](https://developer.wordpress.org/apis/rest/)
[NextSecurityNext: Security](https://developer.wordpress.org/apis/security/)


