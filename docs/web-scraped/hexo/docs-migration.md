# Source: https://hexo.io/docs/migration

Title: Migration

URL Source: https://hexo.io/docs/migration

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
[](https://hexo.io/docs/migration#RSS "RSS")RSS
-----------------------------------------------

First, install the `hexo-migrator-rss` plugin.

$ npm install hexo-migrator-rss --save

Once the plugin is installed, run the following command to migrate all posts from RSS. `source` can be a file path or URL.

$ hexo migrate rss <source>

[](https://hexo.io/docs/migration#Jekyll "Jekyll")Jekyll
--------------------------------------------------------

Move all files in the Jekyll `_posts` folder to the `source/_posts` folder.

Modify the `new_post_name` setting in `_config.yml`:

new_post_name: :year-:month-:day-:title.md

[](https://hexo.io/docs/migration#Octopress "Octopress")Octopress
-----------------------------------------------------------------

Move all files in the Octopress `source/_posts` folder to `source/_posts`

Modify the `new_post_name` setting in `_config.yml`:

new_post_name: :year-:month-:day-:title.md

[](https://hexo.io/docs/migration#WordPress "WordPress")WordPress
-----------------------------------------------------------------

First, install the `hexo-migrator-wordpress` plugin.

$ npm install hexo-migrator-wordpress --save

Export your WordPress site by going to “Tools” → “Export” → “WordPress” in the WordPress dashboard (see the [WordPress support page](http://en.support.wordpress.com/export/) for more details).

Now run:

$ hexo migrate wordpress <source>

Where `source` is the file path or URL to the WordPress export file.

[](https://hexo.io/docs/migration#Joomla "Joomla")Joomla
--------------------------------------------------------

First, install the `hexo-migrator-joomla` plugin.

$ npm install hexo-migrator-joomla --save

Export your Joomla articles using the [J2XML](http://extensions.joomla.org/extensions/migration-a-conversion/data-import-a-export/12816?qh=YToxOntpOjA7czo1OiJqMnhtbCI7fQ==) component.

Now run:

$ hexo migrate joomla <source>

Where `source` is the file path or URL to the Joomla export file.
