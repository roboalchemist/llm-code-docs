# Source: https://hexo.io/docs/helpers

Title: Helpers

URL Source: https://hexo.io/docs/helpers

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Helpers are used in templates to help you insert snippets quickly. Helpers cannot be used in source files.

You could easily [write your own custom helper](https://hexo.io/api/helper) or use our ready-made helpers.

[](https://hexo.io/docs/helpers#URL "URL")URL
---------------------------------------------

### [](https://hexo.io/docs/helpers#url-for "url_for")url_for

Returns a URL with the root path prefixed. Output is encoded automatically.

<%- url_for(path, [option]) %>

| Option | Description | Default |
| --- | --- | --- |
| `relative` | Output relative link | Value of `config.relative_link` |

**Examples:**

_config.yml

root: /blog/

<%- url_for('/a/path') %>

Relative link, follows `relative_link` option by default

e.g. post/page path is ‘/foo/bar/index.html’

_config.yml

relative_link: true

<%- url_for('/css/style.css') %>

<%- url_for('/css/style.css', {relative: false}) %>

### [](https://hexo.io/docs/helpers#relative-url "relative_url")relative_url

Returns the relative URL from `from` to `to`.

<%- relative_url(from, to) %>

**Examples:**

<%- relative_url('foo/bar/', 'css/style.css') %>

### [](https://hexo.io/docs/helpers#full-url-for "full_url_for")full_url_for

Returns a URL with the `config.url` prefixed. Output is encoded automatically.

<%- full_url_for(path) %>

**Examples:**

_config.yml

url: https://example.com/blog

<%- full_url_for('/a/path') %>

### [](https://hexo.io/docs/helpers#gravatar "gravatar")gravatar

Returns the gravatar image URL from an email.

If you don’t specify the [options] parameter, the default options will apply. Otherwise, you can set it to a number which will then be passed on as the size parameter to Gravatar. Finally, if you set it to an object, it will be converted into a query string of parameters for Gravatar.

<%- gravatar(email, [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `s` | Output image size | 80 |
| `d` | Default image |  |
| `f` | Force default |  |
| `r` | Rating |  |

More info: [Gravatar](https://en.gravatar.com/site/implement/images/)

**Examples:**

<%- gravatar('a@abc.com') %>

<%- gravatar('a@abc.com', 40) %>

<%- gravatar('a@abc.com' {s: 40, d: 'https://via.placeholder.com/150'}) %>

[](https://hexo.io/docs/helpers#HTML-Tags "HTML Tags")HTML Tags
---------------------------------------------------------------

### [](https://hexo.io/docs/helpers#css "css")css

Loads CSS files. `path` can be a string, an array, an object or an array of objects. [`/<root>/`](https://hexo.io/docs/configuration#URL) value is prepended while `.css` extension is appended to the `path` automatically. Use object type for custom attributes.

<%- css(path, ...) %>

**Examples:**

<%- css('style.css') %>

<%- css(['style.css', 'screen.css']) %>

<%- css({ href: 'style.css', integrity: 'foo' }) %>

<%- css([{ href: 'style.css', integrity: 'foo' }, { href: 'screen.css', integrity: 'bar' }]) %>

### [](https://hexo.io/docs/helpers#js "js")js

Loads JavaScript files. `path` can be a string, an array, an object or an array of objects. [`/<root>/`](https://hexo.io/docs/configuration#URL) value is prepended while `.js` extension is appended to the `path` automatically. Use object type for custom attributes.

<%- js(path, ...) %>

**Examples:**

<%- js('script.js') %>

<%- js(['script.js', 'gallery.js']) %>

<%- js({ src: 'script.js', integrity: 'foo', async: true }) %>

<%- js([{ src: 'script.js', integrity: 'foo' }, { src: 'gallery.js', integrity: 'bar' }]) %>

### [](https://hexo.io/docs/helpers#link-to "link_to")link_to

Inserts a link.

<%- link_to(path, [text], [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `external` | Opens the link in a new tab | false |
| `class` | Class name |  |
| `id` | ID |  |

**Examples:**

<%- link_to('http://www.google.com') %>

<%- link_to('http://www.google.com', 'Google') %>

<%- link_to('http://www.google.com', 'Google', {external: true}) %>

### [](https://hexo.io/docs/helpers#mail-to "mail_to")mail_to

Inserts a mail link.

<%- mail_to(path, [text], [options]) %>

| Option | Description |
| --- | --- |
| `class` | Class name |
| `id` | ID |
| `subject` | Mail subject |
| `cc` | CC |
| `bcc` | BCC |
| `body` | Mail content |

**Examples:**

<%- mail_to('a@abc.com') %>

<%- mail_to('a@abc.com', 'Email') %>

### [](https://hexo.io/docs/helpers#image-tag "image_tag")image_tag

Inserts an image.

<%- image_tag(path, [options]) %>

| Option | Description |
| --- | --- |
| `alt` | Alternative text of the image |
| `class` | Class name |
| `id` | ID |
| `width` | Image width |
| `height` | Image height |

### [](https://hexo.io/docs/helpers#favicon-tag "favicon_tag")favicon_tag

Inserts a favicon.

<%- favicon_tag(path) %>

### [](https://hexo.io/docs/helpers#feed-tag "feed_tag")feed_tag

Inserts a feed link.

<%- feed_tag(path, [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `title` | Feed title | `config.title` |
| `type` | Feed type |  |

**Examples:**

<%- feed_tag('atom.xml') %>

<%- feed_tag('rss.xml', { title: 'RSS Feed', type: 'rss' }) %>

<%- feed_tag() %>

[](https://hexo.io/docs/helpers#Conditional-Tags "Conditional Tags")Conditional Tags
------------------------------------------------------------------------------------

### [](https://hexo.io/docs/helpers#is-current "is_current")is_current

Check whether `path` matches the URL of the current page. Use `strict` options to enable strict matching.

<%- is_current(path, [strict]) %>

### [](https://hexo.io/docs/helpers#is-home "is_home")is_home

Check whether the current page is home page.

<%- is_home() %>

### [](https://hexo.io/docs/helpers#is-home-first-page-6-3-0 "is_home_first_page (+6.3.0)")is_home_first_page (+6.3.0)

Check whether the current page is the first of home page.

<%- is_home_first_page() %>

### [](https://hexo.io/docs/helpers#is-post "is_post")is_post

Check whether the current page is a post.

<%- is_post() %>

### [](https://hexo.io/docs/helpers#is-page "is_page")is_page

Check whether the current page is a page.

<%- is_page() %>

### [](https://hexo.io/docs/helpers#is-archive "is_archive")is_archive

Check whether the current page is an archive page.

<%- is_archive() %>

### [](https://hexo.io/docs/helpers#is-year "is_year")is_year

Check whether the current page is a yearly archive page.

<%- is_year() %>

### [](https://hexo.io/docs/helpers#is-month "is_month")is_month

Check whether the current page is a monthly archive page.

<%- is_month() %>

### [](https://hexo.io/docs/helpers#is-category "is_category")is_category

Check whether the current page is a category page.

If a string is given as parameter, check whether the current page match the given category.

<%- is_category() %>

<%- is_category('hobby') %>

### [](https://hexo.io/docs/helpers#is-tag "is_tag")is_tag

Check whether the current page is a tag page.

If a string is given as parameter, check whether the current page match the given tag.

<%- is_tag() %>

<%- is_tag('hobby') %>

[](https://hexo.io/docs/helpers#String-Manipulation "String Manipulation")String Manipulation
---------------------------------------------------------------------------------------------

### [](https://hexo.io/docs/helpers#trim "trim")trim

Removes prefixing and trailing spaces of a string.

<%- trim(string) %>

### [](https://hexo.io/docs/helpers#strip-html "strip_html")strip_html

Sanitizes all HTML tags in a string.

<%- strip_html(string) %>

**Examples:**

<%- strip_html('It\'s not <b>important</b> anymore!') %>

### [](https://hexo.io/docs/helpers#titlecase "titlecase")titlecase

Transforms a string into proper title caps.

<%- titlecase(string) %>

**Examples:**

<%- titlecase('this is an apple') %>

# This is an Apple

### [](https://hexo.io/docs/helpers#markdown "markdown")markdown

Renders a string with Markdown.

<%- markdown(str) %>

**Examples:**

<%- markdown('make me **strong**') %>

### [](https://hexo.io/docs/helpers#render "render")render

Renders a string.

<%- render(str, engine, [options]) %>

**Examples:**

<%- render('p(class="example") Test', 'pug'); %>

See [Rendering](https://hexo.io/api/rendering) for more details.

### [](https://hexo.io/docs/helpers#word-wrap "word_wrap")word_wrap

Wraps text into lines no longer than `length`. `length` is 80 by default.

<%- word_wrap(str, [length]) %>

**Examples:**

<%- word_wrap('Once upon a time', 8) %>

### [](https://hexo.io/docs/helpers#truncate "truncate")truncate

Truncates text after certain `length`. Default is 30 characters.

<%- truncate(text, [options]) %>

**Examples:**

<%- truncate('Once upon a time in a world far far away', {length: 17}) %>

<%- truncate('Once upon a time in a world far far away', {length: 17, separator: ' '}) %>

<%- truncate('And they found that many people were sleeping better.', {length: 25, omission: '... (continued)'}) %>

### [](https://hexo.io/docs/helpers#escape-html "escape_html")escape_html

Escapes HTML entities in a string.

<%- escape_html(str) %>

**Examples:**

<%- escape_html('<p>Hello "world".</p>') %>

[](https://hexo.io/docs/helpers#Templates "Templates")Templates
---------------------------------------------------------------

### [](https://hexo.io/docs/helpers#partial "partial")partial

Loads other template files. You can define local variables in `locals`.

<%- partial(layout, [locals], [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `cache` | Cache contents (Use fragment cache) | `false` |
| `only` | Strict local variables. Only use variables set in `locals` in templates. | `false` |

### [](https://hexo.io/docs/helpers#fragment-cache "fragment_cache")fragment_cache

Caches the contents in a fragment. It saves the contents within a fragment and serves the cache when the next request comes in.

<%- fragment_cache(id, fn);

**Examples:**

<%- fragment_cache('header', function(){

 return '<header></header>';

}) %>

[](https://hexo.io/docs/helpers#Date-Time "Date & Time")Date & Time
-------------------------------------------------------------------

### [](https://hexo.io/docs/helpers#date "date")date

Inserts formatted date. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object. `format` is `date_format` setting by default.

<%- date(date, [format]) %>

**Examples:**

<%- date(Date.now()) %>

<%- date(Date.now(), 'YYYY/M/D') %>

### [](https://hexo.io/docs/helpers#date-xml "date_xml")date_xml

Inserts date in XML format. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object.

<%- date_xml(date) %>

**Examples:**

<%- date_xml(Date.now()) %>

### [](https://hexo.io/docs/helpers#time "time")time

Inserts formatted time. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object. `format` is `time_format` setting by default.

<%- time(date, [format]) %>

**Examples:**

<%- time(Date.now()) %>

<%- time(Date.now(), 'h:mm:ss a') %>

### [](https://hexo.io/docs/helpers#full-date "full_date")full_date

Inserts formatted date and time. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object. `format` is `date_format + time_format` setting by default.

<%- full_date(date, [format]) %>

**Examples:**

<%- full_date(new Date()) %>

<%- full_date(new Date(), 'dddd, MMMM Do YYYY, h:mm:ss a') %>

### [](https://hexo.io/docs/helpers#relative-date "relative_date")relative_date

Inserts relative time from now. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object.

<%- relative_date(date) %>

**Examples:**

<%- relative_date(new Date()) %>

<%- relative_date(new Date(1000000000000)) %>

### [](https://hexo.io/docs/helpers#time-tag "time_tag")time_tag

Inserts time tag. `date` can be unix time, ISO string, date object, or [Moment.js](http://momentjs.com/) object. `format` is `date_format` setting by default.

<%- time_tag(date, [format]) %>

**Examples:**

<%- time_tag(new Date()) %>

<%- time_tag(new Date(), 'MMM-D-YYYY') %>

### [](https://hexo.io/docs/helpers#moment "moment")moment

[Moment.js](http://momentjs.com/) library.

[](https://hexo.io/docs/helpers#List "List")List
------------------------------------------------

### [](https://hexo.io/docs/helpers#list-categories "list_categories")list_categories

Inserts a list of all categories.

<%- list_categories([options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `orderby` | Order of categories | name |
| `order` | Sort of order. `1`, `asc` for ascending; `-1`, `desc` for descending | 1 |
| `show_count` | Display the number of posts for each category | true |
| `style` | Style to display the category list. `list` displays categories in an unordered list. Use `false` or any other value to disable it. | list |
| `separator` | Separator between categories. (Only works if `style` is not `list`) | , |
| `depth` | Levels of categories to be displayed. `0` displays all categories and child categories; `-1` is similar to `0` but displayed in flat; `1` displays only top level categories. | 0 |
| `class` | Class name of category list. | category |
| `transform` | The function that changes the display of category name. |  |
| `suffix` | Add a suffix to link. | None |

**Examples:**

<%- list_categories(post.categories, {

 class: 'post-category',

 transform(str) {

 return titlecase(str);

 }

}) %>

<%- list_categories(post.categories, {

 class: 'post-category',

 transform(str) {

 return str.toUpperCase();

 }

}) %>

### [](https://hexo.io/docs/helpers#list-tags "list_tags")list_tags

Inserts a list of all tags.

<%- list_tags([options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `orderby` | Order of tags | name |
| `order` | Sort of order. `1`, `asc` for ascending; `-1`, `desc` for descending | 1 |
| `show_count` | Display the number of posts for each tag | true |
| `style` | Style to display the tag list. `list` displays tags in an unordered list. Use `false` or any other value to disable it. | list |
| `separator` | Separator between categories. (Only works if `style` is not `list`) | , |
| `class` | Class name of tag list (string) or customize each tag’s class (object, see below). | tag |
| `transform` | The function that changes the display of tag name. See examples in [list_categories](https://hexo.io/docs/helpers#list-categories). |  |
| `amount` | The number of tags to display (0 = unlimited) | 0 |
| `suffix` | Add a suffix to link. | None |

Class advanced customization:

| Option | Description | Default |
| --- | --- | --- |
| `class.ul` | `<ul>` class name (only for style `list`) | `tag-list` (list style) |
| `class.li` | `<li>` class name (only for style `list`) | `tag-list-item` (list style) |
| `class.a` | `<a>` class name | `tag-list-link` (list style) `tag-link` (normal style) |
| `class.label` | `<span>` class name where the tag label is stored (only for normal style, when `class.label` is set the label is put in a `<span>`) | `tag-label` (normal style) |
| `class.count` | `<span>` class name where the tag counter is stored (only when `show_count` is `true`) | `tag-list-count` (list style) `tag-count` (normal style) |

Examples:

<%- list_tags(site.tags, {class: 'classtest', style: false, separator: ' | '}) %>

<%- list_tags(site.tags, {class: 'classtest', style: 'list'}) %>

<%- list_tags(site.tags, {class: {ul: 'ululul', li: 'lilili', a: 'aaa', count: 'ccc'}, style: false, separator: ' | '}) %>

<%- list_tags(site.tags, {class: {ul: 'ululul', li: 'lilili', a: 'aaa', count: 'ccc'}, style: 'list'}) %>

### [](https://hexo.io/docs/helpers#list-archives "list_archives")list_archives

Inserts a list of archives.

<%- list_archives([options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `type` | Type. This value can be `yearly` or `monthly`. | monthly |
| `order` | Sort of order. `1`, `asc` for ascending; `-1`, `desc` for descending | 1 |
| `show_count` | Display the number of posts for each archive | true |
| `format` | Date format | MMMM YYYY |
| `style` | Style to display the archive list. `list` displays archives in an unordered list. Use `false` or any other value to disable it. | list |
| `separator` | Separator between archives. (Only works if `style` is not `list`) | , |
| `class` | Class name of archive list. | archive |
| `transform` | The function that changes the display of archive name. See examples in [list_categories](https://hexo.io/docs/helpers#list-categories). |  |

### [](https://hexo.io/docs/helpers#list-posts "list_posts")list_posts

Inserts a list of posts.

<%- list_posts([options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `orderby` | Order of posts | date |
| `order` | Sort of order. `1`, `asc` for ascending; `-1`, `desc` for descending | 1 |
| `style` | Style to display the post list. `list` displays posts in an unordered list. Use `false` or any other value to disable it. | list |
| `separator` | Separator between posts. (Only works if `style` is not `list`) | , |
| `class` | Class name of post list. | post |
| `amount` | The number of posts to display (0 = unlimited) | 6 |
| `transform` | The function that changes the display of post name. See examples in [list_categories](https://hexo.io/docs/helpers#list-categories). |  |

### [](https://hexo.io/docs/helpers#tagcloud "tagcloud")tagcloud

Inserts a tag cloud.

<%- tagcloud([tags], [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `min_font` | Minimum font size | 10 |
| `max_font` | Maximum font size | 20 |
| `unit` | Unit of font size | px |
| `amount` | Total amount of tags | unlimited |
| `orderby` | Order of tags | name |
| `order` | Sort order. `1`, `asc` as ascending; `-1`, `desc` as descending | 1 |
| `color` | Colorizes the tag cloud | false |
| `start_color` | Start color. You can use hex (`#b700ff`), rgba (`rgba(183, 0, 255, 1)`), hsla (`hsla(283, 100%, 50%, 1)`) or [color keywords](http://www.w3.org/TR/css3-color/#svg-color). This option only works when `color` is true. |  |
| `end_color` | End color. You can use hex (`#b700ff`), rgba (`rgba(183, 0, 255, 1)`), hsla (`hsla(283, 100%, 50%, 1)`) or [color keywords](http://www.w3.org/TR/css3-color/#svg-color). This option only works when `color` is true. |  |
| `class` | Class name prefix of tags |  |
| `level` | The number of different class names. This option only works when `class` is set. | 10 |
| `show_count` (+6.3.0) | Display the number of posts for each tag | false |
| `count_class` (+6.3.0) | Class name of tag count | count |

**Examples:**

<%- tagcloud() %>

<%- tagcloud({amount: 30}) %>

[](https://hexo.io/docs/helpers#Miscellaneous "Miscellaneous")Miscellaneous
---------------------------------------------------------------------------

### [](https://hexo.io/docs/helpers#paginator "paginator")paginator

Inserts a paginator.

<%- paginator(options) %>

| Option | Description | Default |
| --- | --- | --- |
| `base` | Base URL | / |
| `format` | URL format | page/%d/ |
| `total` | The number of pages | 1 |
| `current` | Current page number | 0 |
| `prev_text` | The link text of previous page. Works only if `prev_next` is set to true. | Prev |
| `next_text` | The link text of next page. Works only if `prev_next` is set to true. | Next |
| `space` | The space text | &hellp; |
| `prev_next` | Display previous and next links | true |
| `end_size` | The number of pages displayed on the start and the end side | 1 |
| `mid_size` | The number of pages displayed between current page, but not including current page | 2 |
| `show_all` | Display all pages. If this is set to true, `end_size` and `mid_size` will not work | false |
| `escape` | Escape HTML tags | true |
| `page_class` (+6.3.0) | Page class name | `page-number` |
| `current_class` (+6.3.0) | Current page class name | `current` |
| `space_class` (+6.3.0) | Space class name | `space` |
| `prev_class` (+6.3.0) | Previous page class name | `extend prev` |
| `next_class` (+6.3.0) | Next page class name | `extend next` |
| `force_prev_next` (+6.3.0) | Force display previous and next links | false |

**Examples:**

<%- paginator({

 prev_text: '<',

 next_text: '>'

}) %>

<a href="/1/">&lt;</a>

<a href="/1/">1</a>

2

<a href="/3/">3</a>

<a href="/3/">&gt;</a>

<%- paginator({

 prev_text: '<i class="fa fa-angle-left"></i>',

 next_text: '<i class="fa fa-angle-right"></i>',

 escape: false

}) %>

<a href="/1/"><i class="fa fa-angle-left"></i></a>

<a href="/1/">1</a>

2

<a href="/3/">3</a>

<a href="/3/"><i class="fa fa-angle-right"></i></a>

### [](https://hexo.io/docs/helpers#search-form "search_form")search_form

Inserts a Google search form.

<%- search_form(options) %>

| Option | Description | Default |
| --- | --- | --- |
| `class` | The class name of form | search-form |
| `text` | Search hint word | Search |
| `button` | Display search button. The value can be a boolean or a string. If the value is a string, it’ll be the text of the button. | false |

### [](https://hexo.io/docs/helpers#number-format "number_format")number_format

Formats a number.

<%- number_format(number, [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `precision` | The precision of number. The value can be `false` or a nonnegative integer. | false |
| `delimiter` | The thousands delimiter | , |
| `separator` | The separator between the fractional and integer digits. | . |

**Examples:**

<%- number_format(12345.67, {precision: 1}) %>

<%- number_format(12345.67, {precision: 4}) %>

<%- number_format(12345.67, {precision: 0}) %>

<%- number_format(12345.67, {delimiter: ''}) %>

<%- number_format(12345.67, {separator: '/'}) %>

### [](https://hexo.io/docs/helpers#meta-generator "meta_generator")meta_generator

Inserts [generator tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta).

<%- meta_generator() %>

**Examples:**

<%- meta_generator() %>

### [](https://hexo.io/docs/helpers#open-graph "open_graph")open_graph

Inserts [Open Graph](http://ogp.me/) data.

<%- open_graph([options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `title` | Page title (`og:title`) | `page.title` |
| `type` | Page type (`og:type`) | article(post page) website(non-post page) |
| `url` | Page URL (`og:url`) | `url` |
| `image` | Page images (`og:image`) | All images in the content |
| `author` | Article author (`og:article:author`) | `config.author` |
| `date` | Article published time (`og:article:published_time`) | Page published time |
| `updated` | Article modified time (`og:article:modified_time`) | Page modified time |
| `language` | Article language (`og:locale`) | `page.lang || page.language || config.language` |
| `site_name` | Site name (`og:site_name`) | `config.title` |
| `description` | Page description (`og:description`) | Page excerpt or first 200 characters of the content |
| `twitter_card` | Twitter card type (`twitter:card`) | summary |
| `twitter_id` | Twitter ID (`twitter:creator`) |  |
| `twitter_site` | Twitter Site (`twitter:site`) |  |
| `twitter_image` | Twitter Image (`twitter:image`) |  |
| `google_plus` | Google+ profile link |  |
| `fb_admins` | Facebook admin ID |  |
| `fb_app_id` | Facebook App ID |  |

### [](https://hexo.io/docs/helpers#toc "toc")toc

Parses all heading tags (h1~h6) in the content and inserts a table of contents.

<%- toc(str, [options]) %>

| Option | Description | Default |
| --- | --- | --- |
| `class` | Class name | `toc` |
| `class_item` (+6.3.0) | Class name of item | `${class}-item` |
| `class_link` (+6.3.0) | Class name of link | `${class}-link` |
| `class_text` (+6.3.0) | Class name of text | `${class}-text` |
| `class_child` (+6.3.0) | Class name of child | `${class}-child` |
| `class_number` (+6.3.0) | Class name of number | `${class}-number` |
| `class_level` (+6.3.0) | Class name prefix of level | `${class}-level` |
| `list_number` | Displays list number | true |
| `max_depth` | Maximum heading depth of generated toc | 6 |
| `min_depth` | Minimum heading depth of generated toc | 1 |
| `max_items` (+7.3.0) | Maximum number of items in generated toc | `Infinity` |

**Examples:**

<%- toc(page.content) %>

#### [](https://hexo.io/docs/helpers#data-toc-unnumbered-6-1-0 "data-toc-unnumbered (+6.1.0)")data-toc-unnumbered (+6.1.0)

Headings with attribute `data-toc-unnumbered="true"` will be marked as unnumbered (list number will not be displayed).

> **Warning!**
> For using `data-toc-unnumbered="true"`, the renderer must have the option to add CSS classes.
>
>
> Please see the below PRs.
>
>
> * [https://github.com/hexojs/hexo/pull/4871](https://github.com/hexojs/hexo/pull/4871)
> * [https://github.com/hexojs/hexo-util/pull/269](https://github.com/hexojs/hexo-util/pull/269)
> * [https://github.com/hexojs/hexo-renderer-markdown-it/pull/174](https://github.com/hexojs/hexo-renderer-markdown-it/pull/174)
