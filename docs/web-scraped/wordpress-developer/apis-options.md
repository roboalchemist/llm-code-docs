# Options

**Source:** [https://developer.wordpress.org/apis/options/](https://developer.wordpress.org/apis/options/)



# Options




## In this article


Table of Contents- Overview
- Function Reference
- Examples
- Available options by categoryDiscussionGeneralLinksMediaMiscellaneousPermalinksPrivacyReadingThemesWritingUncategorized
- All Settings Screen



↑Back to top



## Overview


TheOptions APIis a simple and standardized way of storing data in the database. The API makes it easy to create, access, update, and delete options. All the data is stored in thewp_options tableunder a given custom name.


This page contains the technical documentation needed to use the Options API. A list of default options can be found in theOption Reference(link to Codex version, waiting for content migration to HelpHub).


Note that the_site_functions are essentially the same as their counterparts. The only differences occur for WP Multisite, when the options apply network-wide and the data is stored in thewp_sitemetatable under the given custom name.


## Function Reference


Add/Delete Option:


- add_option()
- delete_option()
- add_site_option()
- delete_site_option()


Get/Update Option:


- get_option()
- update_option()
- get_site_option()
- update_site_option()


## Examples


```
// Create an option to the database
add_option( $option, $value = , $deprecated = , $autoload = 'yes' );

// Removes option by name.
delete_option( $option );

// Fetch a saved option
get_option( $option, $default = false );

// Update the value of an option that was already added.
update_option( $option, $newvalue );
```


## Available options by category


### Discussion


- blacklist_keys: When a comment contains any of these words in its content, name, URL, e-mail, or IP, it will be marked as spam. One word or IP per line. It will match inside words, so “press” will match “WordPress.”Default: NULLData type:String (possibly multi-line)
- comment_max_links: Hold a comment in the queue if it contains the value of this option or more.Default: 2Data type:Integer
- comment_moderation: Before a comment appears, an administrator must always approve the comment.1:Yes0:False(default)Data type:Integer
- comments_notify: E-mail me when anyone posts a comment.1:Yes(default)0:NoData type:Integer
- default_comment_status: Allow comments (can be overridden with individual posts)open:Allow comments(default)closed:Disallow commentsData type:String
- default_ping_status: Allow link notifications from other blogs (pingbacks and trackbacks).open:Allow pingbacks and trackbacks from other blogs(default)closed:Disallow pingbacks and trackbacks from other blogsData type:String
- default_pingback_flag: Attempt to notify any blogs linked to from the article (slows down posting).1:Yes(default)0:NoData type:Integer
- moderation_keys: When a comment contains any of these words in its content, name, URL, e-mail, or IP, it will be held in the moderation queue. One word or IP per line. It will match inside words, so “press” will match “WordPress.”Default: NULLData type:String (possibly multi-line)
- moderation_notify: E-mail me when a comment is held for moderation.1:Yes(default)0:NoData type:Integer
- require_name_email: Before a comment appears, the comment author must fill out his/her name and email.1:Yes(default)0:NoData type:Integer
- thread_comments: Enable WP-native threaded (nested) comments.1:Yes0:No(default)Data type:Integer
- thread_comments_depth: Set the number of threading levels for comments.1thru10: levelsDefault: 5Data type:Integer
- show_avatars: Avatar Display1: (default)Show Avatars0:Do not show AvatarsData type:Integer
- avatar_rating: Maximum RatingG: (default)Suitable for all audiencesPG:Possibly offensive, usually for audiences 13 and aboveR:Intended for adult audiences above 17X:Even more mature than aboveData type:String
- avatar_default: Default Avatarmystery: (default)Mystery Manblank:Blankgravatar_default:Gravatar Logoidenticon:Identicon (Generated)wavatar:Wavatar (Generated)monsterid:MonsterID (Generated)retro:Retro (Generated)Data type:String
- close_comments_for_old_posts: Automatically close comments on old articles1:Yes0:No(default)Data type:Integer
- close_comments_days_old: Automatically close comments on articles older than x daysDefault: 14Data type:Integer
- show_comments_cookies_opt_in: Show the cookies opt-in checkbox on the comment form and enable comment cookies1:Yes(default as of 4.9.8)0:NoData type:Integer
- page_comments: Break comments into pages1:Yes(default)0:NoData type:Integer
- comments_per_page:Default: 50Data type:Integer
- default_comments_page:Default: ‘newest’Data type:String
- comment_order:asc: (default)desc:Data type:String
- comment_whitelist: Comment author must have a previously approved comment1:Yes(default)0:NoData type:


### General


- admin_email: Administrator emailDefault: ‘you@example.com’Data type:String
- blogdescription: Blog taglineDefault: ‘__(‘Just another WordPress weblog’)’Data type:String
- blogname: Blog titleDefault: ‘__(‘My Blog’)’Data type:String
- comment_registration: Users must be registered and logged in to comment1:Yes0:No(default)Data type:Integer
- date_format: Default date formatDefault: ‘__(‘F j, Y’)’Data type:String
- default_role: The default role of users who register at the blog.subscriber(default)administratoreditorauthorcontributorData type:String
- gmt_offset: Times in the blog should differ by this value.-6:GMT -6 (aka Central Time, USA)0:GMT (aka Greenwich Mean Time)Default:date(‘Z’) / 3600Data type:Integer
- home: Blog address (URL)Default:wp_guess_url()Data type:String (URI)
- siteurl: WordPress address (URL)Defaultwp_guess_url()Data type:String (URI)
- start_of_week: The starting day of the week.0:Sunday1:Monday(default)2:Tuesday3:Wednesday4:Thursday5:Friday6:SaturdayData type:Integer
- time_format: Default time formatDefault: ‘__(‘g:i a’)’Data type:String
- timezone_string: TimezoneDefault: NULLData type:String
- users_can_register: Anyone can register1:Yes0:No(default)Data type:Integer


### Links


- links_updated_date_format:Default__('F j, Y g:i a')Data type:String
- links_recently_updated_prepend:Default emptyData type:String
- links_recently_updated_appendDefaultemptyData type:String
- links_recently_updated_timeDefault: 120Data type:Integer


### Media


- thumbnail_size_w:Default: 150Data type:Integer
- thumbnail_size_h:Default: 150Data type:Integer
- thumbnail_crop: Crop thumbnail to exact dimensions (normally thumbnails are proportional)1:Yes(default)0:NoData type:Integer
- medium_size_w:Default: 300Data type:Integer
- medium_size_hDefault: 300Data type:Integer
- large_size_wDefault: 1024Data type:Integer
- large_size_hDefault: 1024Data type:Integer
- embed_autourls: Attempt to automatically embed all plain text URLsDefault: 1Data type:Integer
- embed_size_wDefault: NULLData type:Integer
- embed_size_hDefault: 600Data type:Integer


### Miscellaneous


- hack_file: Use legacymy-hacks.phpfile support1:Yes0:No(default)Data type:Integer
- html_type: Default MIME type for blog pages (text/html, text/xml+html, etc.)Default: ‘text/html’Data type:String (MIME type)
- secret: Secret value created during installation used with salting, etc.Default: wp_generate_password(64)Data type:String (MD5)
- upload_path: Store uploads in this folder (relative to the WordPress root)Default: NULLData type:String (relative path)
- upload_url_path: URL path to upload folder (will be blank by default – Editable in “All Settings” Screen.Data type:String (URL path)
- uploads_use_yearmonth_folders: Organize my uploads into month- and year-based folders1:Yes(default)0:No(default for safe mode)Data type:Integer
- use_linksupdate: Track links’ update times1:Yes0:No(default)Data type:Integer


### Permalinks


- permalink_structure: The desired structure of your blog’s permalinks. Some examples:/%year%/%monthnum%/%day%/%postname%/: Date and name based/archives/%post_id%/: Numeric/%postname%/: Post name-basedDefault: NULLData type:String
- category_base: The default category base of your blog categories permalink.Default: NULLData type:String
- tag_base: The default tag base for your blog tags permalink.Default: NULLData type:String


### Privacy


- blog_public:1:I would like my blog to be visible to everyone, including search engines (like Google, Sphere, Technorati) and archivers.(default)0:I would like to block search engines, but allow normal visitors.Data type:Integer


### Reading


- blog_charset: Encoding for pages and feeds. The character encoding you write your blog in (UTF-8 is recommended).Default:UTF-8Data type:String
- gzipcompression: WordPress should compress articles (with gzip) if browsers ask for them.1:Yes0:No(default)Data type:Integer
- page_on_front: The ID of the page that should be displayed on the front page. Requiresshow_on_front‘s value to bepage.Data type:Integer
- page_for_posts: The ID of the page that displays posts. Useful whenshow_on_front‘s value ispage.Data type:Integer
- posts_per_page: Show at mostxmany posts on blog pages.Default: 10Data type:Integer
- posts_per_rss: Show at mostxmany posts in RSS feeds.Default: 10Data type:Integer
- rss_language: Language for RSS feeds (metadata purposes only)Default:enData type:String (ISO two-letter language code)
- rss_use_excerpt: Show an excerpt instead of the full text of a post in RSS feeds1:Yes0:No(default)Data type:Integer
- show_on_front: What to show on the front pageposts:Your latest posts(default)page:A static page (see page_on_front)Data type:String


### Themes


- template: The slug of the currently activated theme (how it is accessed by path, ex./wp-content/themes/my-theme(my-themewould be the value of this option).Default: ‘default’Data type:String
- stylesheet: The slug of the currently activated stylesheet (style.css) (how it is accessed by path, ex./wp-content/themes/my-style(my-style would be the value of this option)Default: ‘default’Data type:String


### Writing


- default_category: ID of the category that posts will be put in by defaultDefault: 1Data type:Integer
- default_email_category: ID of the category that posts will be put in by default when written via e-mailDefault: 1Data type:Integer
- default_link_category: ID of the category that links will be put in by defaultDefault: 2Data type:Integer
- default_post_edit_rows: Size of the post box (in lines)Default: 10Data type:Integer
- mailserver_login: Mail server username for posting to WordPress by e-mailDefault: ‘login@example.com’Data type:String
- mailserver_pass: Mail server password for posting to WordPress by e-mailDefault: ‘password’Data type:String
- mailserver_port: Mail server port for posting to WordPress by e-mailDefault: 110Data type:Integer
- mailserver_url: Mail server for posting to WordPress by e-mailDefault: ‘mail.example.com’Data type:String
- ping_sites: When you publish a new post, WordPress automatically notifies the following site update services. For more about this, seeUpdate Services. Separate multiple service URLs with line breaks. Requiresblog_publicto have a value of1.Default: ‘http://rpc.pingomatic.com/’Data type:String (possibly multi-line)
- use_balanceTags: Correct invalidly-nested XHTML automatically1:Yes0:No(default)Data type:Integer
- use_smilies: Convert emoticons like:-)and:Pto graphics when displayed1:Yes(default)0:NoData type:Integer
- use_trackback: Enable sending and receiving of trackbacks1:Yes0:No(default)
- enable_app: Enable the Atom Publishing Protocol1:Yes0:No(default)Data type:Integer
- enable_xmlrpc: Enable the WordPress, Movable Type, MetaWeblog and Blogger XML-RPC publishing protocols1:Yes0:No(default)Data type:Integer


### Uncategorized


- active_plugins: Returns an array of strings containing the path of themainphp file of the plugin. The path is relative to thepluginsfolder. An example of path in the array :/mainpage.php.Default: array()Data type:Array
- advanced_edit:Default: 0Data type:Integer
- recently_edited:Default: NULLData type:
- image_default_link_type:Default: ‘file’Data type:‘file’, ‘none’
- image_default_size:Default: NULLData type:‘thumbnail’, ‘medium’, ‘large’ or Custom size
- image_default_align:Default: NULLData type:‘left’, ‘right’, ‘center’, ‘none’
- sidebars_widgets: Returns array of sidebar states (list of active and inactive widgets).Default:Data type:Array
- sticky_posts:Default: array()Data type:
- widget_categories:Default: array()Data type:
- widget_text:Default: array()Data type:
- widget_rss:Default: array()Data type:


## All Settings Screen


WordPress 3.0removed Settings > Miscellaneous screen and some of the options cannot be reached (e.g.upload_url_path). You may use the All Settings Screen to view and change almost all options listed above. It is accessible by visiting/wp-admin/options.php






First published


August 12, 2019


Last updated


June 14, 2023



[PreviousMetadataPrevious: Metadata](https://developer.wordpress.org/apis/metadata/)
[NextPluginsNext: Plugins](https://developer.wordpress.org/apis/plugins/)


