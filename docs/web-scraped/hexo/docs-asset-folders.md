# Source: https://hexo.io/docs/asset-folders

Title: Asset Folders

URL Source: https://hexo.io/docs/asset-folders

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Asset Folders | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/asset-folders)

Asset Folders
=============

[](https://github.com/hexojs/site/edit/master/source/docs/asset-folders.md "Improve this doc")

[](https://hexo.io/docs/asset-folders#Global-Asset-Folder "Global Asset Folder")Global Asset Folder[](https://hexo.io/docs/asset-folders#Global-Asset-Folder)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Assets are non-post files in the `source` folder, such as images, CSS or JavaScript files. For instance, If you are only going to have a few images in the Hexo project, then the easiest way is to keep them in a `source/images` directory. Then, you can access them using something like `![](/images/image.jpg)`.

[](https://hexo.io/docs/asset-folders#Post-Asset-Folder "Post Asset Folder")Post Asset Folder[](https://hexo.io/docs/asset-folders#Post-Asset-Folder)
-----------------------------------------------------------------------------------------------------------------------------------------------------

For users who expect to regularly serve images and/or other assets, and for those who prefer to separate their assets on a post-per-post basis, Hexo also provides a more organized way to manage assets. This slightly more involved, but very convenient approach to asset management can be turned on by setting the `post_asset_folder` setting in `_config.yml` to true.

_config.yml

post_asset_folder: true

With asset folder management enabled, Hexo will create a folder every time you make a new post with the `hexo new [layout] <title>` command. This asset folder will have the same name as the markdown file associated with the post. Place all assets related to your post into the associated folder, and you will be able to reference them using a relative path, making for an easier and more convenient workflow.

[](https://hexo.io/docs/asset-folders#Tag-Plugins-For-Relative-Path-Referencing "Tag Plugins For Relative Path Referencing")Tag Plugins For Relative Path Referencing[](https://hexo.io/docs/asset-folders#Tag-Plugins-For-Relative-Path-Referencing)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Referencing images or other assets using normal markdown syntax and relative paths may lead to incorrect display on archive or index pages. Plugins have been created by the community to address this issue in Hexo 2. However, with the release of Hexo 3, several new [tag plugins](https://hexo.io/docs/tag-plugins#Include-Assets) were added to core. These enable you to reference your assets more easily in posts:

{% asset_path slug %}

{% asset_img slug [title] %}

{% asset_link slug [title] %}

For example, with post asset folders enabled, if you place an image `example.jpg` into your asset folder, it will _not_ appear on the index page if you reference it using a relative path with regular `![](example.jpg)` markdown syntax (however, it will work as expected in the post itself).

The correct way to reference the image will thus be using tag plugin syntax rather than markdown:

{% asset_img example.jpg This is an example image %}

{% asset_img "spaced asset.jpg" "spaced title" %}

This way, the image will appear both inside the post and on index and archive pages.

[](https://hexo.io/docs/asset-folders#Embedding-an-image-using-markdown "Embedding an image using markdown")Embedding an image using markdown[](https://hexo.io/docs/asset-folders#Embedding-an-image-using-markdown)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[hexo-renderer-marked](https://github.com/hexojs/hexo-renderer-marked) 3.1.0 introduced a new option that allows you to embed an image in markdown without using `asset_img` tag plugin.

To enable:

_config.yml

post_asset_folder: true

marked:

 prependRoot: true

 postAsset: true

Once enabled, an asset image will be automatically resolved to its corresponding post’s path. For example, “image.jpg” is located at “/2020/01/02/foo/image.jpg”, meaning it is an asset image of “/2020/01/02/foo/“ post, `![](image.jpg)` will be rendered as `<img src="/2020/01/02/foo/image.jpg">`.

Last updated: 2026-03-12[Prev](https://hexo.io/docs/tag-plugins "Tag Plugins")[Next](https://hexo.io/docs/data-files "Data Files")

**Contents**

1. [Global Asset Folder](https://hexo.io/docs/asset-folders#Global-Asset-Folder)
2. [Post Asset Folder](https://hexo.io/docs/asset-folders#Post-Asset-Folder)
3. [Tag Plugins For Relative Path Referencing](https://hexo.io/docs/asset-folders#Tag-Plugins-For-Relative-Path-Referencing)
4. [Embedding an image using markdown](https://hexo.io/docs/asset-folders#Embedding-an-image-using-markdown)

[Back to Top](https://hexo.io/docs/asset-folders#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
