# Source: https://hexo.io/docs/permalinks

Title: Permalinks

URL Source: https://hexo.io/docs/permalinks

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
You can specify the permalinks for your site in `_config.yml` or in the front-matter for each post.

### [](https://hexo.io/docs/permalinks#Variables "Variables")Variables

Besides the following variables, you can use any attributes in the permalink except `:path` and `:permalink`.

| Variable | Description |
| --- | --- |
| `:year` | Published year of posts (4-digit) |
| `:month` | Published month of posts (2-digit) |
| `:i_month` | Published month of posts (Without leading zeros) |
| `:day` | Published day of posts (2-digit) |
| `:i_day` | Published day of posts (Without leading zeros) |
| `:hour` | Published hour of posts (2-digit) |
| `:minute` | Published minute of posts (2-digit) |
| `:second` | Published second of posts (2-digit) |
| `:timestamp` | Timestamp of post’s published [date](https://hexo.io/docs/front-matter#Settings-Their-Default-Values) |
| `:title` | Filename (relative to “source/_posts/“ folder) |
| `:name` | Filename |
| `:post_title` | Post title |
| `:id` | Post ID (_not persistent across [cache reset](https://hexo.io/docs/commands#clean)_) |
| `:category` | Categories. If the post is uncategorized, it will use the `default_category` value. |
| `:hash` | SHA1 hash of filename (same as `:title`) and date (12-hexadecimal) |

You can define the default value of each variable in the permalink through the `permalink_defaults` setting:

permalink_defaults:

 lang: en

### [](https://hexo.io/docs/permalinks#Examples "Examples")Examples

source/_posts/hello-world.md

title: Hello World

date: 2013-07-14 17:01:34

categories:

- foo

- bar

| Setting | Result |
| --- | --- |
| `:year/:month/:day/:title/` | 2013/07/14/hello-world/ |
| `:year-:month-:day-:title.html` | 2013-07-14-hello-world.html |
| `:category/:title/` | foo/bar/hello-world/ |
| `:title-:hash/` | hello-world-a2c8ac003b43/ |

source/_posts/lorem/hello-world.md

title: Hello World

date: 2013-07-14 17:01:34

categories:

- foo

- bar

| Setting | Result |
| --- | --- |
| `:year/:month/:day/:title/` | 2013/07/14/lorem/hello-world/ |
| `:year/:month/:day/:name/` | 2013/07/14/hello-world/ |

### [](https://hexo.io/docs/permalinks#Multi-language-Support "Multi-language Support")Multi-language Support

To create a multi-language site, you can modify the `new_post_name` and `permalink` settings like this:

new_post_name: :lang/:title.md

permalink: :lang/:title/

When you create a new post, the post will be saved to:

$ hexo new "Hello World" --lang tw

and the URL will be:

http://localhost:4000/tw/hello-world/
