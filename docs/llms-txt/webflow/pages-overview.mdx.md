# Source: https://developers.webflow.com/designer/reference/pages-overview.mdx

***

title: Pages & Folders
slug: designer/reference/pages-overview
description: ''
hidden: false
'og:title': 'Webflow Designer API: Pages & Folders'
'og:description': >-
The Pages and Folders APIs provide access to the organizational structure of a
site, as well as the settings and metadata of individual pages.
---------------------------------------------------------------

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Pages%20Overview_v1_24fps.webm" type="video/webm" />

    Your browser does not support HTML video.
</video>

The Pages and Folders APIs provide access to the organizational structure of a site, as well as the settings and metadata of individual pages.

## Pages

The Pages APIs provide access to general page information, enabling Apps to update a page name, slug, and title. Additionally, Apps can programmatically manage SEO and Open Graph information through the Pages APIs, which is essential for improving search engine visibility and ranking, as well as controlling how content looks when shared on social media platforms.

Lastly, the Pages APIs also allow visibility into the current setting of a page, allowing Apps to determine whether a page is a draft, or if it's password protected and more.

## Folders

The Folders APIs allow Apps to [organize pages within folders, also known as directories.](https://university.webflow.com/lesson/page-folders?topics=site-settings) You can create and nest folders – subfolders, or subdirectories – for sites with deep hierarchy (i.e., sites with information organized into more sub-levels).

<Info title="Folders affect page URLs">
  Moving pages or folders to a new folder will result in a URL update. This will cause the old URLs to return a 404 page. If you want the old URLs to redirect to the new location, you’ll need to use 301 redirects.
</Info>
