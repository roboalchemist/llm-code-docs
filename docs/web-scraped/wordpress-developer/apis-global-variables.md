# Global Variables

**Source:** [https://developer.wordpress.org/apis/global-variables/](https://developer.wordpress.org/apis/global-variables/)



# Global Variables




## In this article


Table of Contents- IntroductionInside the Loop variablesBrowser Detection BooleansWeb Server Detection BooleansVersion VariablesMiscAdmin Globals


↑Back to top



## Introduction


WordPress-specific global variables are used throughout WordPress code for various reasons. Almost all data that WordPress generates can be found in a global variable.


Note that it’s best to use the appropriate API functions when available, instead of modifying globals directly.


To access a global variable in your code, you first need to globalize the variable withglobal $variable;.


Accessing other globals besides the ones listed below is not recommended.


### Inside the Loop variables


While inside the loop, these globals are set, containing information about the current post being processed.


- $post(WP_Post): The post object for the current post. Object described inWP_Post Class Reference.
- $posts: Used by some core functions, not to be mistaken for$query->$posts.
- $authordata(WP_User): The author object for the current post. Object described inWP_User Class Reference.
- $currentday(string): Day that the current post was published.
- $currentmonth(string): Month that the curent post was published.
- $page(int): The page of the current post being viewed. Specified by the query var page.
- $pages(array): The content of the pages of the current post. Each page elements contains part of the content separated by the<!--nextpage-->tag.
- $multipage(boolean): Flag to know if the current post has multiple pages or not. Returnstrueif the post has multiple pages, related to$pages.
- $more(boolean): Flag to know if WordPress should enforce the<!--more-->tag for the current post. WordPress will not enforce the more tag iftrue.
- $numpages(int): Returns the number of pages in the post, related to$pages.


### Browser Detection Booleans


These globals store data about which browser the user is on.


- $is_iphone(boolean): iPhone Safari
- $is_chrome(boolean): Google Chrome
- $is_safari(boolean): Safari
- $is_NS4(boolean): Netscape 4
- $is_opera(boolean): Opera
- $is_macIE(boolean): Mac Internet Explorer
- $is_winIE(boolean): Windows Internet Explorer
- $is_gecko(boolean): FireFox
- $is_lynx(boolean): Lynx
- $is_IE(boolean): Internet Explorer
- $is_edge(boolean): Microsoft Edge


### Web Server Detection Booleans


These globals store data about which web server WordPress is running on.


- $is_apache(boolean): Apache HTTP Server
- $is_IIS(boolean): Microsoft Internet Information Services (IIS)
- $is_iis7(boolean): Microsoft Internet Information Services (IIS) v7.x
- $is_nginx(boolean): Nginx web server


### Version Variables


- $wp_version(string): The installed version of WordPress
- $wp_db_version(int): The version number of the database
- $tinymce_version(string): The installed version of TinyMCE
- $manifest_version(string): The cache manifest version
- $required_php_version(string): The version of PHP this install of WordPress requires
- $required_mysql_version(string): The version of MySQL this install of WordPress requires


### Misc


- $super_admins(array): An array of user IDs that should be granted super admin privileges (multisite). This global is only set by the site owner (e.g., inwp-config.php), and contains an array of IDs of users who should have super admin privileges. If set it will override the list of super admins in the database.
- $wp_query(object): The global instance of theWP_Queryclass.
- $wp_rewrite(object): The global instance of theWP_Rewriteclass.
- $wp(object): The global instance of theWPenvironment setup class.
- $wpdb(object): The global instance of thewpdbclass.
- $wp_locale(object): The global instance of theWP_Localeclass.
- $wp_admin_bar(object): The global instance of theWP_Admin_Barclass.
- $wp_roles(object): The global instance of theWP_Rolesclass.
- $wp_meta_boxes(array): Object containing all registered metaboxes, including their id’s, args, callback functions and title for all post types including custom.
- $wp_registered_sidebars(array)
- $wp_registered_widgets(array)
- $wp_registered_widget_controls(array)
- $wp_registered_widget_updates(array)


### Admin Globals


- $pagenow(string): Used in wp-admin.See alsoget_current_screen()for the WordPress Admin Screen API.
- $post_type(string): Used in wp-admin
- $allowedposttags(array)
- $allowedtags(array)
- $menu(array)





First published


August 12, 2019


Last updated


November 21, 2022



[PreviousFilesystemPrevious: Filesystem](https://developer.wordpress.org/apis/filesystem/)
[NextMetadataNext: Metadata](https://developer.wordpress.org/apis/metadata/)


