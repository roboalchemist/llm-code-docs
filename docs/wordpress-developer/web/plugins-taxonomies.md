# Taxonomies

**Source:** [https://developer.wordpress.org/plugins/taxonomies/](https://developer.wordpress.org/plugins/taxonomies/)

↑Back to top

ATaxonomyis a fancy word for the classification/grouping of things. Taxonomies can be hierarchical (with parents/children) or flat.

WordPress stores the Taxonomies in theterm_taxonomydatabase table allowing developers to register Custom Taxonomies along the ones that already exist.

Taxonomies haveTermswhich serve as the topic by which you classify/group things. They are stored inside thetermstable.

For example: a Taxonomy named “Art” can have multiple Terms, such as “Modern” and “18th Century”.

This chapter will show you how to register Custom Taxonomies, how to retrieve their content from the database, and how to render them to the public.

WordPress 3.4 and earlier had a Taxonomy named “Links” which was deprecated in WordPress 3.5.

First published

February 5, 2015

Last updated

December 14, 2023

[PreviousWorking with Custom Post TypesPrevious: Working with Custom Post Types](https://developer.wordpress.org/plugins/post-types/working-with-custom-post-types/)
[NextTerm Splitting (WordPress 4.2)Next: Term Splitting (WordPress 4.2)](https://developer.wordpress.org/plugins/taxonomies/split-terms-wp-4-2/)
