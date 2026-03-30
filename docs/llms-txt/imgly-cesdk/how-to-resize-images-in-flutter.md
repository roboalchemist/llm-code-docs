# Source: https://img.ly/blog/how-to-resize-images-in-flutter/

<!DOCTYPE html>
<!--
    Design by:
    ——————————
        GODO FREDO
        ✉ https://godofredo.ninja
        ✎ @GodoFredoNinja
        ✈ Lima - Perú
-->
<html lang="en" data-theme="light">
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />

    <title>How To Resize Images in Flutter | IMG.LY</title>

    <meta name="HandheldFriendly" content="True" />
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" type="text/css" href="/blog/assets/styles/main.css?v=2feabc0f4f"/>
    <link rel="stylesheet" type="text/css" href="/blog/assets/styles/webflow.min.css?v=2feabc0f4f" />
    <link rel="stylesheet" type="text/css" href="/blog/assets/styles/website-components.css?v=2feabc0f4f" />

    <link
        rel="preload"
        href="https://img.ly/static/imgly-website-components/imgly-website-components.css"
        as="style"
        onload="this.onload=null;this.rel='stylesheet'"
    />


    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/4.11.1/tocbot.css">

    <link rel="sitemap" type="application/xml" href="https://img.ly/sitemap.xml" />

    <meta name="description" content="Learn how to resize your images in Flutter with our step-by-step guide.">
    <link rel="icon" href="https://blog.img.ly/2024/10/publication-icon.png" type="image/png">
    <link rel="canonical" href="https://img.ly/blog/how-to-resize-images-in-flutter/">
    <meta name="referrer" content="no-referrer-when-downgrade">
    <link rel="amphtml" href="https://img.ly/blog/how-to-resize-images-in-flutter/amp/">
    
    <meta property="og:site_name" content="IMG.LY: Blog">
    <meta property="og:type" content="article">
    <meta property="og:title" content="How To Resize Images in Flutter | IMG.LY">
    <meta property="og:description" content="Keep it light: resize your application images in Flutter.">
    <meta property="og:url" content="https://img.ly/blog/how-to-resize-images-in-flutter/">
    <meta property="og:image" content="https://blog.img.ly/2022/09/resize-images-in-flutter-1.png">
    <meta property="article:published_time" content="2022-09-27T15:03:53.000Z">
    <meta property="article:modified_time" content="2024-10-01T10:14:25.000Z">
    <meta property="article:tag" content="How-To">
    <meta property="article:tag" content="Flutter">
    <meta property="article:tag" content="Photo Editing">
    <meta property="article:tag" content="App Development">
    <meta property="article:tag" content="Framework">
    <meta property="article:tag" content="Tutorial">
    
    <meta property="article:publisher" content="https://www.facebook.com/imgly">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="How To Resize Images in Flutter | IMG.LY">
    <meta name="twitter:description" content="Keep it light: resize your application images in Flutter.">
    <meta name="twitter:url" content="https://img.ly/blog/how-to-resize-images-in-flutter/">
    <meta name="twitter:image" content="https://blog.img.ly/2022/09/resize-images-in-flutter-1.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Natalia Kuzminykh">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="How-To, Flutter, Photo Editing, App Development, Framework, Tutorial">
    <meta name="twitter:site" content="@imgly">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="675">
    
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "publisher": {
        "@type": "Organization",
        "name": "IMG.LY: Blog",
        "url": "https://img.ly/blog/",
        "logo": {
            "@type": "ImageObject",
            "url": "https://imgly-blog-prod.storage.googleapis.com/2021/03/logo@2x.png"
        }
    },
    "author": {
        "@type": "Person",
        "name": "Natalia Kuzminykh",
        "image": {
            "@type": "ImageObject",
            "url": "https://imgly-blog-prod.storage.googleapis.com/2022/08/illlustrations--Community-_page-0001.jpg",
            "width": 1200,
            "height": 1196
        },
        "url": "https://img.ly/blog/author/nataliakzm/",
        "sameAs": [
            "https://medium.com/@natalia.kzm"
        ]
    },
    "headline": "How To Resize Images in Flutter | IMG.LY",
    "url": "https://img.ly/blog/how-to-resize-images-in-flutter/",
    "datePublished": "2022-09-27T15:03:53.000Z",
    "dateModified": "2024-10-01T10:14:25.000Z",
    "image": {
        "@type": "ImageObject",
        "url": "https://blog.img.ly/2022/09/resize-images-in-flutter-1.png",
        "width": 1200,
        "height": 675
    },
    "keywords": "How-To, Flutter, Photo Editing, App Development, Framework, Tutorial",
    "description": "Keep it light: resize your application images in Flutter. ",
    "mainEntityOfPage": "https://img.ly/blog/how-to-resize-images-in-flutter/"
}
    </script>

    <meta name="generator" content="Ghost 5.99">
    <link rel="alternate" type="application/rss+xml" title="IMG.LY: Blog" href="https://img.ly/blog/rss/">
    
    <script defer src="https://cdn.jsdelivr.net/ghost/sodo-search@~1.5/umd/sodo-search.min.js" data-key="e0bac6a5a7a1214eb40c4878a5" data-styles="https://cdn.jsdelivr.net/ghost/sodo-search@~1.5/umd/main.css" data-sodo-search="https://img.ly/blog/" crossorigin="anonymous"></script>
    
    <link href="https://img.ly/blog/webmentions/receive/" rel="webmention">
    <script defer src="/blog/public/cards.min.js?v=2feabc0f4f"></script><style>:root {--ghost-accent-color: #15171A;}</style>
    <link rel="stylesheet" type="text/css" href="/blog/public/cards.min.css?v=2feabc0f4f">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/themes/prism-tomorrow.min.css" integrity="sha512-vswe+cgvic/XBoF1OcM/TeJ2FW0OofqAVdCZiEYkd6dwGXthvkSFWOoGGJgS2CW70VK5dQM5Oh+7ne47s74VTg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/plugins/toolbar/prism-toolbar.min.css" integrity="sha512-DSAA0ziYwggOJ3QyWFZhIaU8bSwQLyfnyIrmShRLBdJMtiYKT7Ju35ujBCZ6ApK3HURt34p2xNo+KX9ebQNEPQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<style>
    code[class*=language-], pre[class*=language-], pre {
        font-size: 14px;
        background: #282c34;
    }
    code{
        font-size: smaller !important;
        box-decoration-break: clone;
    }
    div.code-toolbar>.toolbar a, div.code-toolbar>.toolbar button, div.code-toolbar>.toolbar span {
        font-size: .6em;
        border-radius: 5em;
        padding: .5em 1.5em;
        margin: 1em .5em;
        background: rgba(63, 69, 82, .95);
	}
</style>
<script async custom-element="amp-iframe" src="https://cdn.ampproject.org/v0/amp-iframe-0.1.js"></script>
<script type="text/javascript"
      src="https://onsite.optimonk.com/script.js?account=261668"
      async></script>
<style>
  /* Add styles for the responsive table container */
  .v-table-container {
    /* Add any other styling as needed */
    width: 80vw;
    border-collapse: collapse;    /* Clean borders */
    table-layout: fixed; 
  }
  
  table th{
    width: calc(100% / var(--cols));
    word-wrap: break-word;
    white-space: normal;
    text-align: left;
  }
  
  table td{
    width: calc(100% / var(--cols));
    white-space: normal;          /* Allows text wrapping */
    word-wrap: break-word;        /* Legacy support */
    text-align: left;
  }
</style>
    
</head>
<body class="white-theme is-article">
    <div class="site-wrapper u-flexColumnTop">
        <header id="imgly-website-components-header"></header>
        <div id="imgly-website-components-cookies"></div>

        

        <main class="main u-relative ">



<article class="post u-marginBottom40 u-relative">
    <header class="post-header u-container u-maxWidth688 u-relative zindex3">
    <h1 class="post-title u-marginBottom24">How To Resize Images in Flutter</h1>
    <p class="post-excerpt u-textMuted subheadline read-font">Keep it light: resize your application images in Flutter. </p>

    <hr>

    <div class="u-flex post-share">
        <div class="hh u-flex u-flexCenter u-relative zindex4 u-flex1">
    <ul class="hh-author u-flex u-flexWrap u-flex0">
        <li class="hh-author-item u-realtive">
            <a href="/blog/author/nataliakzm/" title="Go to the profile of Natalia Kuzminykh" class="u-relative u-block avatar-image img-md">
                <img
                    class="u-absolute u-image u-block u-round"
                    src="https://imgly-blog-prod.storage.googleapis.com/2022/08/illlustrations--Community-_page-0001.jpg"
                    alt="Go to the profile of  Natalia Kuzminykh"
                />
            </a>
        </li>
    </ul>

    <div class="hh-right u-flex1 u-overflowHidden">
        <div class="hh-author-name u-fontSize15 u-noWrapWithEllipsis"><a href="/blog/author/nataliakzm/">Natalia Kuzminykh</a></div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2022-09-27">27 Sep 2022</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="3 min read">3 min read</span>
    
</div>    </div>
</div>
        <aside class="post-share u-flex0 u-flexCenter u-hide-before-md">
            <span class="share-label u-textMuted u-fontSizeSmaller">Share:</span>
            <a href="https://x.com/share?text=How%20To%20Resize%20Images%20in%20Flutter&amp;url=https://img.ly/blog/how-to-resize-images-in-flutter/"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Twitter"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-twitter"></use></svg>
            </a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://img.ly/blog/how-to-resize-images-in-flutter/&amp;title=How%20To%20Resize%20Images%20in%20Flutter"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Linkedin"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-linkedin"></use></svg>
            </a>
            <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/how-to-resize-images-in-flutter/"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Facebook"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-facebook"></use></svg>
            </a>
        </aside>
    </div>
</header>    <div class="read-area ">
          <figure class="post-image u-block u-marginAuto u-sizeFullHeight u-sizeFullWidth u-maxWidth1080">
              <img class="u-block u-marginAuto u-sizeFullWidth simply-zoom"
                  srcset="https://blog.img.ly/2022/09/resize-images-in-flutter-1.png 300w,
                          https://blog.img.ly/2022/09/resize-images-in-flutter-1.png 600w,
                          https://blog.img.ly/2022/09/resize-images-in-flutter-1.png 1000w,
                          https://blog.img.ly/2022/09/resize-images-in-flutter-1.png 2000w"
                  sizes="(max-width: 400px) 300px,(max-width: 730px) 600px, (max-width: 1600px) 100vw"
                  src="https://blog.img.ly/2022/09/resize-images-in-flutter-1.png"
                  alt="How To Resize Images in Flutter"
              />
          </figure>

      <div class="post-wrap u-maxWidth1080 u-relative u-marginAuto">
          <div id="post-body" class="u-container u-maxWidth688 u-relative">
            <section class="post-body gh-content gh-canvas">
                <aside class="gh-sidebar"><div class="gh-toc">
                    <h4 class="toc-heading">On this Page</h4>
                </div></aside>
                <p>Static images are a core part of mobile applications. Usually, you store them in the directory in their original sizes, which requires you to adjust the sizes now and then, depending on where they are displayed. This article discusses how to resize images in Flutter and adjust their width, height, and size with efficient lines of code.</p><!--kg-card-begin: html--><div class="video" data-src="https://storage.googleapis.com/imgly-static-assets/static/blog/videos/flutter-resize-images.mp4" data-autoplay="false" data-muted="true" data-loop="true" data-poster=""></div><!--kg-card-end: html--><h3 id="resizing-methods">Resizing Methods</h3><p>For image editing tools, Flutter offers an excellent and easy-in-use <code>Boxfit</code> property that works within the <code>fit</code> parameter, and you can easily integrate it into your application.</p><pre><code class="language-dart">child: Image.asset( 'images/pexels.jpg', fit: BoxFit.cover)
</code></pre><p>Depending on your needs, you can choose between multiple attributes. For example, <code>.cover</code> and <code>.fitHeight</code> properties are similar when called, and both result in maximum frame coverage. Yet, although the image is widened proportionally, these methods can significantly affect the quality of crop image borders if they overfill. On the contrary, with <code>.fitWidth</code> or <code>.scaledown</code>, the asset is resized to the container's width boundaries, which could be helpful when multiple images are needed to be displayed simultaneously.  If you are dealing with a static image of small size, you can also employ <code>.fill</code> attribute that helps stretch your assets without cropping any critical information.</p><p>Alternatively, by calling  .scale 0.5 the fit parameter will return you a graphical asset based on the scale you define. Note that any value less than 1 would reduce the image size.</p><h3 id="adjusting-image-size-with-flutter">Adjusting Image Size with Flutter</h3><p>Now, let’s look at how Flutter allows applying these image manipulation techniques. The crucial difference from the other frameworks is that in Flutter, images should be stored in a specific folder. In other words, once you upload graphic files, go to the <code>pubspec.yaml</code> file and add the path to the directory around under <code>assets</code>(<strong>Note:</strong> by default the dependencies corresponding to ****<code>assets</code>are usually placed around 45-46th lines in the code and need to be uncommented first by eliminating # and one space).</p><pre><code class="language-yaml"># Don't forget to define the assets folder in your directory 
# To do so, find lines 45 - 46 in the **pubspec.yaml** file
# and uncomment the assets section like this:
  assets:
   - images/ #Note that this should correspond to the name of your folder
</code></pre><p>Alternatively, you can specify the path to each image in the list:</p><pre><code class="language-yaml">    assets:
      - assets/images/your_image.jpg
      - assets/images/your_image2.jpg
</code></pre><p>When the image is uploaded to Flutter, it seeks to occupy as much size as possible. But let’s presume that we have a “frame” or container that differs in size from the visual asset. One way to see the differences in sizes of both canvases is to color one frame, like color: Colors.indigo. Then we provide Flutter with the size specification and render our image in a child node child: Image.asset('images/pexels.jpg'). Thus, now we can see the image is placed inside the frame, and we need only to assign one of the filling methods (for example, fit: BoxFit.cover) discussed above.</p><pre><code class="language-dart">import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const ImgApp());
}

class ImgApp extends StatelessWidget {
  const ImgApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const ResizePage(),
    );
  }
}

class ResizePage extends StatelessWidget {
  const ResizePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('How to Resize Images'),
          backgroundColor: Color(0xffe55586),
        ),

        body: Center(
            // Enabling the Image Frame
            child: Container(
                color: Colors.indigo, // To see the difference between the image's original size and the frame
                height: 550,
                width: 300,

                // Uploading the Image from Assets
                child: Image.asset(
                  'images/pexels.jpg',

                  // Resizing the Image to the Frame Size
                  fit: BoxFit.cover,
                ))));
  }
}
</code></pre><p>You can find the associated to this tutorial Git repository ― <a href="https://github.com/nataliakzm/Resizing_Images_with_Flutter?ref=img.ly">here</a>. Otherwise, run the following command to clone the complete code to your system:</p><pre><code class="language-bash">git clone &lt;https://github.com/nataliakzm/Resizing_Images_with_Flutter&gt;
</code></pre><h3 id="conclusion">Conclusion</h3><p>This article covered Flutter’s approach to the image resizing problem and saw how to use it in practice. However, despite the diversity of suggested methods that could fulfill basic users’ needs, Flutter fails to provide a comfortable integration. Just imagine you are building an app similar to Instagram in its functionality and you need not only upload various images from different assets but also resize them differently. If you want to avoid spending your time writing and maintaining a ton of code, then you may consider using <a href="https://img.ly/products/photo-sdk?utm_source=imgly&utm_medium=blog&utm_campaign=howtos">PhotoEditor SDK</a> in your next project.</p><!--kg-card-begin: html--><div class="video" data-src="https://storage.googleapis.com/imgly-static-assets/static/blog/videos/photoeditor-sdk-resize-image.mp4" data-autoplay="false" data-muted="true" data-loop="true" data-poster=""></div><!--kg-card-end: html--><p>PhotoEditor SDK is available for various frameworks: first, read <a href="https://img.ly/docs/pesdk/flutter/getting-started/integration/?utm_source=imgly&utm_medium=blog&utm_campaign=howtos">this article</a> from <a href="https://img.ly/docs/pesdk/guides/?utm_source=imgly&utm_medium=blog&utm_campaign=howtos">the official documentation</a> to set up dependencies for your Flutter-based project. You can also follow our guide on how to integrate <a href="https://img.ly/blog/a-modern-video-editor-sdk-for-your-flutter-app/">video editor for Flutter</a> into your app. </p><p>In case you encounter any difficulties with the installation process, don’t hesitate to contact our <a href="https://img.ly/support?utm_source=imgly&utm_medium=blog&utm_campaign=howtos">support</a> who will be happy to help you.  Then, as shown in the example below, you can efficiently resize, crop, rotate or flip your visual assets with the <a href="https://img.ly/docs/pesdk/web/features/transform/?utm_source=imgly&utm_medium=blog&utm_campaign=howtos">transform tool</a>.</p>
            </section>
        </div>
      </div>
    </div>

    <footer class="post-footer u-container u-maxWidth868">
            <div class="post-tags buttonSet u-marginTop30">
        <a href="https://img.ly/blog/tag/how-to/" title="How-To" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="How-To" data-event-non-interaction="true">How-To</a><a href="https://img.ly/blog/tag/flutter/" title="Flutter" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Flutter" data-event-non-interaction="true">Flutter</a><a href="https://img.ly/blog/tag/photo-editing/" title="Photo Editing" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Photo Editing" data-event-non-interaction="true">Photo Editing</a><a href="https://img.ly/blog/tag/app-development/" title="App Development" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="App Development" data-event-non-interaction="true">App Development</a><a href="https://img.ly/blog/tag/framework/" title="Framework" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Framework" data-event-non-interaction="true">Framework</a><a href="https://img.ly/blog/tag/tutorial/" title="Tutorial" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Tutorial" data-event-non-interaction="true">Tutorial</a>
    </div>

        <hr>
        <div class="prev-next">
                <div class="u-flex u-relative godo-tracking prev-article u-marginBottom30"
    data-event-category="Article"
    data-event-action="Previous article"
    data-event-label="https://img.ly/blog/the-top-5-open-source-javascript-image-manipulation-libraries/"
    data-event-non-interaction="true">

    <a href="/blog/the-top-5-open-source-javascript-image-manipulation-libraries/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="Comparing the Top 5 Open Source JavaScript Image Manipulation Libraries">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2022/09/image-manipulation-libraries-javascript-1.png" alt="Comparing the Top 5 Open Source JavaScript Image Manipulation Libraries"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Previous article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/the-top-5-open-source-javascript-image-manipulation-libraries/" class="u-relative zindex3">Comparing the Top 5 Open Source JavaScript Image Manipulation Libraries</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Learn the difference between five major image manipulation libraries and choose the right one for you!</p>
    </div>

    <a href="/blog/the-top-5-open-source-javascript-image-manipulation-libraries/" aria-label="Comparing the Top 5 Open Source JavaScript Image Manipulation Libraries" class="u-absolute0 zindex2"></a>
</div>
                <div class="u-flex u-relative godo-tracking prev-article "
    data-event-category="Article"
    data-event-action="Next article"
    data-event-label="https://img.ly/blog/how-to-build-video-player-in-javascript/"
    data-event-non-interaction="true">

    <a href="/blog/how-to-build-video-player-in-javascript/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="How To Build a Video Player in JavaScript">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2022/09/video-player-javascript_tutorial.png" alt="How To Build a Video Player in JavaScript"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Next article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/how-to-build-video-player-in-javascript/" class="u-relative zindex3">How To Build a Video Player in JavaScript</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Create your own JavaScript video player using simple methods for neat results!</p>
    </div>

    <a href="/blog/how-to-build-video-player-in-javascript/" aria-label="How To Build a Video Player in JavaScript" class="u-absolute0 zindex2"></a>
</div>        </div>
        <hr>
    </footer>
</article>



<div class="post-related">
    <div class="u-container u-maxWidth1048">
        <div class="row">

            <div class="col s12 u-marginBottom40 u-textAlignCenter">
                <h3 class="u-contentTitle u-fontSizeLarger">Related Articles</h3>
            </div>

            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/open-source-photo-editing-sdks-vs-img-ly-ce-sdk-an-honest-comparison-for-developers/" data-event-non-interaction="true">
    <a href="/blog/open-source-photo-editing-sdks-vs-img-ly-ce-sdk-an-honest-comparison-for-developers/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/11/open-source-photo-editor-sdk-whitelabel-best-comparison.jpg"
            srcset="https://blog.img.ly/2025/11/open-source-photo-editor-sdk-whitelabel-best-comparison.jpg"
            data-srcset="https://blog.img.ly/2025/11/open-source-photo-editor-sdk-whitelabel-best-comparison.jpg 300w,https://blog.img.ly/2025/11/open-source-photo-editor-sdk-whitelabel-best-comparison.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="Open-Source Photo Editing SDKs vs IMG.LY CE.SDK: An Honest Comparison for Developers"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/open-source-photo-editing-sdks-vs-img-ly-ce-sdk-an-honest-comparison-for-developers/">Open-Source Photo Editing SDKs vs IMG.LY CE.SDK: An Honest Comparison for Developers</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-11-25">25 Nov 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="11 min read">11 min read</span>
    
</div>    </div>

    <a href="/blog/open-source-photo-editing-sdks-vs-img-ly-ce-sdk-an-honest-comparison-for-developers/" class="u-absolute0 zindex3" aria-label="Open-Source Photo Editing SDKs vs IMG.LY CE.SDK: An Honest Comparison for Developers"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/how-to-build-a-short-video-generator-using-ce-sdk-2/" data-event-non-interaction="true">
    <a href="/blog/how-to-build-a-short-video-generator-using-ce-sdk-2/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/03/AI-video-generator-tutorial-1.jpg"
            srcset="https://blog.img.ly/2025/03/AI-video-generator-tutorial-1.jpg"
            data-srcset="https://blog.img.ly/2025/03/AI-video-generator-tutorial-1.jpg 300w,https://blog.img.ly/2025/03/AI-video-generator-tutorial-1.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="How to Build a Short Video Generator Using CE.SDK"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/how-to-build-a-short-video-generator-using-ce-sdk-2/">How to Build a Short Video Generator Using CE.SDK</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-03-04">4 Mar 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="7 min read">7 min read</span>
    
</div>    </div>

    <a href="/blog/how-to-build-a-short-video-generator-using-ce-sdk-2/" class="u-absolute0 zindex3" aria-label="How to Build a Short Video Generator Using CE.SDK"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/creative-editor-sdk-v-1-44-0-release-notes/" data-event-non-interaction="true">
    <a href="/blog/creative-editor-sdk-v-1-44-0-release-notes/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/02/creative-editor-sdk-1-44.jpg"
            srcset="https://blog.img.ly/2025/02/creative-editor-sdk-1-44.jpg"
            data-srcset="https://blog.img.ly/2025/02/creative-editor-sdk-1-44.jpg 300w,https://blog.img.ly/2025/02/creative-editor-sdk-1-44.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="CE.SDK v1.44 Release Notes"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/creative-editor-sdk-v-1-44-0-release-notes/">CE.SDK v1.44 Release Notes</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-02-06">6 Feb 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="2 min read">2 min read</span>
    
</div>    </div>

    <a href="/blog/creative-editor-sdk-v-1-44-0-release-notes/" class="u-absolute0 zindex3" aria-label="CE.SDK v1.44 Release Notes"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/how-to-build-short-video-generator-ai-creative-sdk/" data-event-non-interaction="true">
    <a href="/blog/how-to-build-short-video-generator-ai-creative-sdk/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/01/build-ai-video-generator-1.jpg"
            srcset="https://blog.img.ly/2025/01/build-ai-video-generator-1.jpg"
            data-srcset="https://blog.img.ly/2025/01/build-ai-video-generator-1.jpg 300w,https://blog.img.ly/2025/01/build-ai-video-generator-1.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="How I Built a Short Video Generator with AI &amp; CE.SDK in One Day"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/how-to-build-short-video-generator-ai-creative-sdk/">How I Built a Short Video Generator with AI &amp; CE.SDK in One Day</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-01-09">9 Jan 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="6 min read">6 min read</span>
    
</div>    </div>

    <a href="/blog/how-to-build-short-video-generator-ai-creative-sdk/" class="u-absolute0 zindex3" aria-label="How I Built a Short Video Generator with AI &amp; CE.SDK in One Day"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/a-modern-vue-js-video-editor/" data-event-non-interaction="true">
    <a href="/blog/a-modern-vue-js-video-editor/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/01/video-editor-vue_js.jpg"
            srcset="https://blog.img.ly/2025/01/video-editor-vue_js.jpg"
            data-srcset="https://blog.img.ly/2025/01/video-editor-vue_js.jpg 300w,https://blog.img.ly/2025/01/video-editor-vue_js.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="A Modern Vue.js Video Editor: Setup Guide"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/a-modern-vue-js-video-editor/">A Modern Vue.js Video Editor: Setup Guide</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-01-08">8 Jan 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="8 min read">8 min read</span>
    
</div>    </div>

    <a href="/blog/a-modern-vue-js-video-editor/" class="u-absolute0 zindex3" aria-label="A Modern Vue.js Video Editor: Setup Guide"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/a-modern-react-video-editor/" data-event-non-interaction="true">
    <a href="/blog/a-modern-react-video-editor/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/01/video-editor-react.jpg"
            srcset="https://blog.img.ly/2025/01/video-editor-react.jpg"
            data-srcset="https://blog.img.ly/2025/01/video-editor-react.jpg 300w,https://blog.img.ly/2025/01/video-editor-react.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="A Modern React Video Editor: Integration Guide"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/a-modern-react-video-editor/">A Modern React Video Editor: Integration Guide</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-01-08">8 Jan 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="7 min read">7 min read</span>
    
</div>    </div>

    <a href="/blog/a-modern-react-video-editor/" class="u-absolute0 zindex3" aria-label="A Modern React Video Editor: Integration Guide"></a>
</div>
            </div>
        </div>
    </div>
</div>


    <div id="post-comments" class="post-comments js-comments u-hide u-bgColorGrayLight u-paddingTop30 u-paddingBottom30 u-contentTitle">
    <div class="u-container u-maxWidth1080 u-card">
        <div id="disqus_thread"></div>
    </div>
</div>


    <div class="share-sticky u-textAlignRight is-visible">
    <div class="share-sticky-wrap buttonSet u-container u-maxWidth1048">
        <span class="u-textMuted u-fontSize15 u-paddingRight10 u-hide-before-md">Share this article:</span>
        <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/how-to-resize-images-in-flutter/"
            target="_blank"
            rel="noopener noreferrer"
            title="Share on Facebook"
            class="godo-tracking button button--s bg-facebook u-textColorWhite js-share"
            data-event-category="Article"
            data-event-action="Share"
            data-event-label="Facebook - Sticky Footer"
            data-event-non-interaction="true">
            <svg class="icon"><use xlink:href="#icon-facebook"></use></svg>
            Share
        </a>
        <a href="https://x.com/share?text=How%20To%20Resize%20Images%20in%20Flutter&amp;url=https://img.ly/blog/how-to-resize-images-in-flutter/"
            target="_blank"
            rel="noopener noreferrer"
            title="Share on Twitter"
            class="godo-tracking button button--s bg-twitter u-textColorWhite js-share"
            data-event-category="Article"
            data-event-action="Share"
            data-event-label="Twitter - Sticky Footer"
            data-event-non-interaction="true">
            <svg class="icon"><use xlink:href="#icon-twitter"></use></svg>
            Tweet
        </a>
        <a href="whatsapp://send?text=https://img.ly/blog/how-to-resize-images-in-flutter/"
            target="_blank"
            rel="noopener noreferrer"
            class="godo-tracking button button--s u-textColorWhite bg-whatsapp u-hide-after-lg"
            data-event-category="Article"
            data-event-action="Share"
            data-event-label="Whatsapp - Sticky Footer"
            data-event-non-interaction="true">
            <svg class="icon"><use xlink:href="#icon-whatsapp"></use></svg>
            Send
        </a>
    </div>
</div></main>

        <div class="instagram js-instagram u-hide u-relative u-bgColorGrayLight"></div>

        <footer id="imgly-website-components-footer"></footer>
    </div>

    <div class="search u-fixed u-flexColumnTop u-flexCenter u-fixed u-absolute0">
    <div class="js-search-close search-shader u-absolute0 zindex1"></div>
    <div class="js-search-close button button--circle button--dark search-close zindex3 u-hide-after-lg">
        <svg class="icon icon--close icon--md"><use xlink:href="#icon-close"></use></svg>
    </div>

    <div class="search-inner u-relative u-marginAuto zindex2">
        <div class="search-wrap">
            <form class="search-form u-sizeFullWidth u-flex u-flexCenter u-fontSizeBase">
                <svg class="icon icon--search icon--md icon--gray"><use xlink:href="#icon-search"></use></svg>
                <input id="search-field" class="u-sizeFullWidth input--md" type="text" placeholder="Search..." aria-label="Search box"/>
            </form>
            <span class="js-search-message search-message u-block u-hide">No results found</span>
            <div id="search-results" class="search-results u-marginAuto u-sizeFullWidth"></div>
        </div>
        <div class="search-nav-hints u-flex u-flexEnd u-hide-before-lg">
            <div class="search-nav-hint"><span>↑</span> <span>↓</span> Navigate up/down</div>
            <div class="search-nav-hint"><span>Enter</span> Go to article</div>
            <div class="search-nav-hint"><span>/</span> Search new term</div>
            <div class="search-nav-hint"><span>Esc</span> Close search</div>
        </div>
    </div>
</div>

    
    <div class="loadingBar"></div>

    <div class="back-to-top js-back-to-top u-hide-before-lg u-pointer u-fixed">
        <svg class="back-to-top-icon" width="24px" height="69px" viewBox="0 0 24 69"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(2.000000, 2.000000)"><rect fill="currentColor" x="9" y="7" width="2" height="60"></rect><polygon stroke="currentColor" stroke-width="2" points="10 0 20 13 0 13"></polygon></g></g></svg>        <p class="back-to-top-text u-fontSizeBase u-fontWeightMedium">GO TOP</p>
    </div>


    <svg aria-hidden="true" style="position:absolute;width:0;height:0" version="1.1" xmlns="http://www.w3.org/2000/svg" overflow="hidden"><defs><symbol id="icon-sunny" viewBox="0 0 24 24"><title>sunny</title><path d="M12 18.141a.722.722 0 0 0-.722.722v2.166a.722.722 0 0 0 1.444 0v-2.166a.722.722 0 0 0-.722-.722zM12 2.25a.722.722 0 0 0-.722.722v2.166a.722.722 0 0 0 1.444 0V2.972A.722.722 0 0 0 12 2.25zM5.859 12a.722.722 0 0 0-.722-.722H2.971a.722.722 0 0 0 0 1.444h2.166A.722.722 0 0 0 5.859 12zm15.169-.722h-2.166a.722.722 0 0 0 0 1.444h2.166a.722.722 0 0 0 0-1.444zM7.148 16.13a.72.72 0 0 0-.511.211l-1.533 1.533a.72.72 0 0 0 0 1.022.72.72 0 0 0 1.022 0l1.533-1.533a.72.72 0 1 0-.511-1.233zm9.704-8.26a.72.72 0 0 0 .511-.211l1.533-1.533a.72.72 0 0 0 0-1.022.72.72 0 0 0-1.022 0l-1.533 1.533a.72.72 0 0 0 0 1.022.72.72 0 0 0 .511.211zM6.127 5.105a.72.72 0 0 0-1.022 0 .72.72 0 0 0 0 1.022L6.638 7.66a.72.72 0 0 0 1.022 0 .72.72 0 0 0 0-1.022L6.127 5.105zm11.235 11.236a.72.72 0 0 0-1.022 0 .725.725 0 0 0 0 1.022l1.533 1.533a.72.72 0 0 0 1.022 0 .72.72 0 0 0 0-1.022l-1.533-1.533zM12 7.5c-2.48 0-4.5 2.02-4.5 4.5s2.02 4.5 4.5 4.5 4.5-2.02 4.5-4.5-2.02-4.5-4.5-4.5z"/></symbol><symbol id="icon-moon" viewBox="0 0 32 32"><title>moon</title><path d="M25.087 22.137c-.181.006-.363.012-.544.012a11.018 11.018 0 0 1-7.925-3.337c-2.119-2.15-3.281-5.006-3.281-8.05 0-1.731.381-3.406 1.094-4.919.194-.412.581-1.038.85-1.462.119-.181-.031-.419-.244-.381-.375.056-.95.181-1.731.425C8.443 5.969 5 10.544 5 15.937 5 22.6 10.319 28 16.881 28c3.625 0 6.875-1.65 9.056-4.256.375-.45.719-.863 1.025-1.363.113-.188-.044-.419-.256-.381-.531.106-1.069.113-1.619.137z"/></symbol><symbol id="icon-arrow" viewBox="0 0 24 24"><title>arrow</title><path d="M3.984 13.002h12.174l-5.611 5.611L12 20.016 20.016 12 12 3.984l-1.403 1.403 5.561 5.611H3.984v2.004z"/></symbol><symbol id="icon-close" viewBox="0 0 24 24"><title>close</title><path d="M18.984 6.412l-1.397-1.397-5.588 5.588-5.588-5.588-1.397 1.397L10.602 12l-5.588 5.588 1.397 1.397 5.588-5.588 5.588 5.588 1.397-1.397L13.396 12z"/></symbol><symbol id="icon-comments" viewBox="0 0 24 24"><title>comments</title><path d="M20.203 15.028c0-.206.056-.403.155-.572.028-.052.066-.098.098-.145a7.594 7.594 0 0 0 1.294-4.233c.014-4.322-3.633-7.828-8.142-7.828-3.933 0-7.214 2.677-7.983 6.23a7.563 7.563 0 0 0-.173 1.603c0 4.327 3.506 7.927 8.016 7.927.717 0 1.683-.216 2.213-.361s1.055-.338 1.191-.389a1.23 1.23 0 0 1 .909.014l2.658.942s.112.047.183.047a.373.373 0 0 0 .375-.375c0-.047-.023-.127-.023-.127l-.769-2.733z"/><path d="M14.93 18.398c-.169.047-.384.098-.619.15-.492.103-1.12.211-1.594.211-4.509 0-8.016-3.6-8.016-7.927 0-.309.033-.703.07-1.003a6.33 6.33 0 0 1 .108-.6c.047-.211.103-.422.164-.628l-.375.333c-1.537 1.341-2.419 3.253-2.419 5.245 0 1.373.398 2.695 1.163 3.844.108.164.169.291.15.375s-.558 2.906-.558 2.906a.375.375 0 0 0 .127.361c.07.056.155.084.239.084a.331.331 0 0 0 .136-.028l2.63-1.036a.725.725 0 0 1 .267-.052s.113-.009.295.061c.886.347 1.866.563 2.845.563a7.363 7.363 0 0 0 5.63-2.583s.15-.206.323-.45c-.173.061-.37.122-.567.173z"/></symbol><symbol id="icon-star" viewBox="0 0 24 24"><title>star</title><path d="M21.703 9h-6.895l-2.095-6.253c-.103-.305-.389-.497-.712-.497s-.609.192-.712.497L9.194 9H2.252a.752.752 0 0 0-.75.75c0 .042.005.089.014.127.009.164.084.347.314.53l5.667 3.994-2.175 6.323a.752.752 0 0 0 .258.844c.136.098.262.183.422.183.155 0 .337-.08.469-.169l5.531-3.942 5.531 3.942a.876.876 0 0 0 .469.169c.159 0 .286-.08.417-.183a.742.742 0 0 0 .258-.844l-2.175-6.323 5.62-4.031.136-.117c.122-.131.244-.309.244-.502 0-.413-.384-.75-.797-.75z"/></symbol><symbol id="icon-link" viewBox="0 0 24 24"><title>link</title><path d="M13.125 15.989l-.056.005a.778.778 0 0 0-.45.211l-3.028 3.028c-.642.642-1.5.994-2.414.994s-1.772-.352-2.414-.994c-.642-.642-.994-1.5-.994-2.414s.352-1.772.994-2.414l3.216-3.216a3.425 3.425 0 0 1 1.228-.788c.225-.084.464-.141.703-.173a3.38 3.38 0 0 1 .478-.033c.066 0 .131.005.216.009.83.052 1.613.403 2.194.984.361.361.638.802.802 1.28a.737.737 0 0 0 .905.473c.005 0 .009-.005.014-.005s.009 0 .009-.005c.38-.117.6-.516.492-.895-.206-.731-.572-1.345-1.153-1.922a4.935 4.935 0 0 0-2.7-1.373 4.768 4.768 0 0 0-1.148-.052 4.744 4.744 0 0 0-.759.117c-.052.009-.098.023-.15.037a4.882 4.882 0 0 0-2.212 1.275l-3.216 3.216c-.919.933-1.43 2.17-1.43 3.492s.511 2.559 1.439 3.487a4.91 4.91 0 0 0 3.483 1.434 4.898 4.898 0 0 0 3.488-1.439l3.061-3.061c.487-.492.094-1.327-.595-1.261z"/><path d="M20.311 3.689c-.928-.928-2.166-1.439-3.483-1.439s-2.559.511-3.487 1.439l-2.986 2.986a.753.753 0 0 0 .473 1.284.759.759 0 0 0 .595-.216l2.991-2.981c.642-.642 1.5-.994 2.414-.994s1.772.352 2.414.994c.642.642.994 1.5.994 2.414s-.352 1.772-.994 2.414l-3.216 3.216a3.425 3.425 0 0 1-1.228.788 3.255 3.255 0 0 1-.703.173 3.38 3.38 0 0 1-.478.033c-.066 0-.136-.005-.216-.009a3.406 3.406 0 0 1-2.194-.984c-.342-.342-.6-.75-.769-1.195a.748.748 0 0 0-.895-.459.758.758 0 0 0-.53.961c.211.656.567 1.214 1.111 1.758l.009.009a4.935 4.935 0 0 0 3.853 1.425 4.882 4.882 0 0 0 3.117-1.425l3.216-3.216c.928-.928 1.439-2.166 1.439-3.487s-.52-2.559-1.448-3.488z"/></symbol><symbol id="icon-search" viewBox="0 0 24 24"><title>search</title><path d="M20.789 19.697l-5.006-5.053a7.173 7.173 0 0 0-5.607-11.649c-3.966 0-7.177 3.216-7.177 7.177s3.211 7.172 7.177 7.172c1.716 0 3.286-.6 4.523-1.603l4.973 5.02a.768.768 0 0 0 1.088.028.775.775 0 0 0 .028-1.092zm-10.612-3.895c-1.505 0-2.92-.586-3.984-1.65s-1.65-2.48-1.65-3.98c0-1.505.586-2.92 1.65-3.98 1.064-1.064 2.48-1.65 3.984-1.65s2.92.586 3.984 1.65a5.597 5.597 0 0 1 1.65 3.98c0 1.505-.586 2.92-1.65 3.98a5.6 5.6 0 0 1-3.984 1.65z"/></symbol><symbol id="icon-send" viewBox="0 0 24 24"><title>send</title><path d="M20.433 3.042l-17.208 7.5a.394.394 0 0 0 .014.717l4.655 2.63a.75.75 0 0 0 .858-.084l9.178-7.913c.061-.052.206-.15.263-.094.061.061-.033.202-.084.263l-7.941 8.944a.748.748 0 0 0-.075.895l3.042 4.88c.15.295.577.291.712-.009l7.116-17.208a.394.394 0 0 0-.53-.52z"/></symbol><symbol id="icon-heart" viewBox="0 0 24 24"><title>heart</title><path d="M16.5 2.625h-.047c-1.861 0-3.506.984-4.453 2.438-.947-1.453-2.592-2.438-4.453-2.438H7.5a5.3 5.3 0 0 0-5.25 5.297c0 1.734.759 4.195 2.241 6.22C7.313 18 12 21.375 12 21.375s4.688-3.375 7.509-7.233c1.481-2.025 2.241-4.486 2.241-6.22a5.3 5.3 0 0 0-5.25-5.297z"/></symbol><symbol id="icon-rss" viewBox="0 0 24 24"><title>rss</title><path d="M5.62 15.755A2.624 2.624 0 0 0 3 18.371a2.613 2.613 0 0 0 2.62 2.606c1.448 0 2.62-1.167 2.62-2.606s-1.172-2.616-2.62-2.616z"/><path d="M3 9v3.745c2.25 0 4.411.666 6 2.255s2.25 3.745 2.25 6H15C15 14.442 9.562 9 3 9z"/><path d="M3 3v3.745c8.016 0 14.245 6.234 14.245 14.255H21c0-9.923-8.063-18-18-18z"/></symbol><symbol id="icon-arrow-forward" viewBox="0 0 24 24"><title>arrow-forward</title><path d="M13.786 12L7.828 6.047c-.441-.441-.441-1.153 0-1.589s1.153-.436 1.594 0l6.75 6.745c.427.427.436 1.111.033 1.552l-6.778 6.792c-.22.22-.511.328-.797.328s-.577-.108-.797-.328a1.12 1.12 0 0 1 0-1.589L13.786 12z"/></symbol><symbol id="icon-twitter" viewBox="0 0 24 24"><title>twitter</title><path d="M11.0343 10.6221L4.33141 2.99841H5.91922L11.7418 9.61659L16.3889 2.99841H21.75L14.7212 13.0072L21.75 21.0008H20.1622L14.0173 14.0103L9.10866 21.0008H3.74753M19.5891 4.16999H17.1498L5.92042 19.8868H8.36036"/></symbol><symbol id="icon-linkedin" viewBox="0 0 24 24"><title>linkedin</title><path d="M19.556 3H4.537C3.717 3 3 3.591 3 4.402v15.052c0 .816.717 1.542 1.537 1.542h15.014c.825 0 1.444-.731 1.444-1.542V4.402C21 3.591 20.376 3 19.556 3zM8.578 18H6V9.984h2.578V18zm-1.2-9.234h-.019C6.534 8.766 6 8.152 6 7.383 6 6.6 6.548 6 7.392 6s1.359.595 1.378 1.383c0 .769-.534 1.383-1.392 1.383zM18 18h-2.578v-4.383c0-1.05-.375-1.767-1.308-1.767-.713 0-1.134.483-1.322.952-.07.169-.089.398-.089.633v4.566h-2.578V9.985h2.578v1.116c.375-.534.961-1.303 2.325-1.303 1.692 0 2.972 1.116 2.972 3.52v4.683z"/></symbol><symbol id="icon-facebook" viewBox="0 0 24 24"><title>facebook</title><path d="M20.006 3H3.993a.995.995 0 0 0-.994.994v16.013c0 .548.445.994.994.994h8.006v-7.125H9.847v-2.625h2.152V9.31c0-2.325 1.612-3.591 3.689-3.591.994 0 2.063.075 2.311.108v2.428h-1.655c-1.13 0-1.345.534-1.345 1.322v1.673h2.691l-.352 2.625h-2.339V21h5.006a.995.995 0 0 0 .994-.994V3.993a.995.995 0 0 0-.994-.994z"/></symbol><symbol id="icon-github" viewBox="0 0 24 24"><title>github</title><path d="M12 1.5C6.202 1.5 1.5 6.323 1.5 12.267c0 4.758 3.009 8.789 7.181 10.214a.831.831 0 0 0 .178.019c.389 0 .539-.286.539-.534 0-.258-.009-.933-.014-1.833a4.805 4.805 0 0 1-1.059.127c-2.02 0-2.48-1.57-2.48-1.57-.478-1.242-1.167-1.575-1.167-1.575-.914-.642-.005-.661.066-.661h.005c1.055.094 1.608 1.116 1.608 1.116.525.919 1.228 1.177 1.856 1.177.492 0 .938-.159 1.2-.281.094-.694.366-1.167.666-1.439-2.33-.272-4.781-1.195-4.781-5.32 0-1.177.408-2.137 1.078-2.887-.108-.272-.469-1.369.103-2.85 0 0 .075-.023.234-.023.38 0 1.238.145 2.653 1.13a9.85 9.85 0 0 1 2.63-.361 9.877 9.877 0 0 1 2.63.361c1.416-.984 2.273-1.13 2.653-1.13.159 0 .234.023.234.023.572 1.481.211 2.578.103 2.85.67.755 1.078 1.716 1.078 2.887 0 4.134-2.456 5.044-4.795 5.311.375.333.713.989.713 1.992 0 1.439-.014 2.602-.014 2.953 0 .253.145.539.534.539a.921.921 0 0 0 .188-.019c4.177-1.425 7.181-5.461 7.181-10.214 0-5.944-4.702-10.767-10.5-10.767z"/></symbol><symbol id="icon-instagram" viewBox="0 0 24 24"><title>instagram</title><path d="M15.75 4.5c.994 0 1.936.394 2.648 1.102S19.5 7.257 19.5 8.25v7.5c0 .994-.394 1.936-1.102 2.648S16.743 19.5 15.75 19.5h-7.5c-.994 0-1.936-.394-2.648-1.102S4.5 16.743 4.5 15.75v-7.5c0-.994.394-1.936 1.102-2.648S7.257 4.5 8.25 4.5h7.5zm0-1.5h-7.5C5.363 3 3 5.363 3 8.25v7.5C3 18.638 5.363 21 8.25 21h7.5c2.888 0 5.25-2.362 5.25-5.25v-7.5C21 5.363 18.638 3 15.75 3z"/><path d="M16.875 8.25c-.623 0-1.125-.502-1.125-1.125S16.252 6 16.875 6a1.125 1.125 0 0 1 0 2.25zM12 9c1.655 0 3 1.345 3 3s-1.345 3-3 3-3-1.345-3-3 1.345-3 3-3zm0-1.5c-2.484 0-4.5 2.016-4.5 4.5s2.016 4.5 4.5 4.5 4.5-2.016 4.5-4.5-2.016-4.5-4.5-4.5z"/></symbol><symbol id="icon-youtube" viewBox="0 0 24 24"><title>youtube</title><path d="M23.841 6.975c0-2.109-1.552-3.806-3.469-3.806A169.616 169.616 0 0 0 12.422 3h-.844c-2.7 0-5.353.047-7.95.169-1.912 0-3.464 1.706-3.464 3.816A68.603 68.603 0 0 0 0 11.991a71.766 71.766 0 0 0 .159 5.011c0 2.109 1.552 3.82 3.464 3.82 2.728.127 5.527.183 8.372.178 2.85.009 5.639-.047 8.372-.178 1.917 0 3.469-1.711 3.469-3.82.112-1.673.164-3.342.159-5.016a68.815 68.815 0 0 0-.155-5.011zM9.703 16.589V7.378l6.797 4.603-6.797 4.608z"/></symbol><symbol id="icon-whatsapp" viewBox="0 0 24 24"><title>whatsapp</title><path d="M12.19 1.5C6.497 1.5 1.881 6.08 1.881 11.73c0 1.933.541 3.74 1.479 5.282L1.499 22.5l5.708-1.813a10.334 10.334 0 0 0 4.983 1.272c5.694 0 10.31-4.58 10.31-10.23s-4.616-10.23-10.31-10.23zm5.127 14.115c-.243.601-1.339 1.15-1.823 1.175s-.497.375-3.133-.77-4.221-3.93-4.346-4.11-1.021-1.455-.973-2.74c.049-1.285.752-1.891 1.003-2.143s.538-.298.714-.301c.208-.003.342-.006.496-.001s.384-.032.584.499c.2.531.677 1.835.738 1.968s.099.287.005.458c-.094.171-.143.278-.279.426s-.289.33-.412.443c-.137.125-.28.261-.136.528s.64 1.142 1.396 1.863c.971.927 1.809 1.234 2.067 1.374s.413.125.573-.044c.16-.169.686-.738.872-.992s.359-.205.597-.109c.238.096 1.507.776 1.766.916s.431.212.493.323c.062.112.042.634-.2 1.236z"/></symbol><symbol id="icon-map" viewBox="0 0 24 24"><title>map</title><path stroke-linejoin="round" stroke-linecap="round" stroke-miterlimit="4" stroke-width="2" fill="none" d="M21 10c0 7-9 13-9 13s-9-6-9-13c0-4.971 4.029-9 9-9s9 4.029 9 9z"/><path stroke-linejoin="round" stroke-linecap="round" stroke-miterlimit="4" stroke-width="2" fill="none" d="M15 10a3 3 0 1 1-6 0 3 3 0 1 1 6 0z"/></symbol><symbol id="icon-reddit" viewBox="0 0 28 28"><title>reddit</title><path d="M28 13.219A3.105 3.105 0 0 1 26.297 16c.125.484.187.984.187 1.5 0 4.937-5.578 8.937-12.453 8.937-6.859 0-12.437-4-12.437-8.937 0-.5.063-1 .172-1.469A3.135 3.135 0 0 1 0 13.219a3.107 3.107 0 0 1 5.375-2.125c2.109-1.469 4.922-2.422 8.047-2.531L15.235.422a.547.547 0 0 1 .641-.406l5.766 1.266a2.337 2.337 0 0 1 4.422 1.047 2.34 2.34 0 0 1-2.344 2.344 2.334 2.334 0 0 1-2.328-2.328l-5.219-1.156-1.625 7.375c3.141.094 5.984 1.031 8.109 2.5a3.063 3.063 0 0 1 2.234-.953A3.107 3.107 0 0 1 28 13.22zM6.531 16.328a2.338 2.338 0 0 0 2.328 2.344 2.34 2.34 0 0 0 2.344-2.344A2.338 2.338 0 0 0 8.859 14a2.334 2.334 0 0 0-2.328 2.328zm12.656 5.547a.557.557 0 0 0 0-.812.566.566 0 0 0-.797 0c-.938.953-2.953 1.281-4.391 1.281s-3.453-.328-4.391-1.281a.566.566 0 0 0-.797 0 .557.557 0 0 0 0 .812c1.484 1.484 4.344 1.594 5.187 1.594s3.703-.109 5.187-1.594zm-.046-3.203a2.338 2.338 0 0 0 2.328-2.344A2.334 2.334 0 0 0 19.141 14a2.338 2.338 0 0 0-2.344 2.328 2.34 2.34 0 0 0 2.344 2.344z"/></symbol></defs></svg>
    <script>
        var siteUrl = 'https://img.ly/blog';
        var siteSearch = '/blog/assets/scripts/search.js?v=2feabc0f4f';
    </script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/tocbot/4.12.3/tocbot.min.js"></script>

    <script>
        tocbot.init({
            // Where to render the table of contents.
            tocSelector: '.gh-toc',
            // Where to grab the headings to build the table of contents.
            contentSelector: '.gh-content',
            // Which headings to grab inside of the contentSelector element.
            headingSelector: 'h1, h2, h3, h4',
            headingsOffset: -1000,
        });
        var ghToc = document.querySelector('.gh-toc')
        if (ghToc) {
            ghToc.innerHTML = '<h4 class="toc-heading">On this Page</h4>' + ghToc.innerHTML;
        }
    </script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/components/prism-core.min.js" integrity="sha512-xR+IAyN+t9EBIOOJw5m83FTVMDsPd63IhJ3ElP4gmfUFnQlX9+eWGLp3P4t3gIjpo2Z1JzqtW/5cjgn+oru3yQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/plugins/autoloader/prism-autoloader.min.js" integrity="sha512-zc7WDnCM3aom2EziyDIRAtQg1mVXLdILE09Bo+aE1xk0AM2c2cVLfSW9NrxE5tKTX44WBY0Z2HClZ05ur9vB6A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/plugins/toolbar/prism-toolbar.min.js" integrity="sha512-cu2C9EssrOrVXT4thyL4gz/qWyh3Lq9XbICUXYyh3zJRCSKk1J08tBKPXnsSpdpZXOliaK/OJBygw/l0twAmwA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js" integrity="sha512-bWzyGaP/f19RLeYGN6ZhDgvkS7GM0Fq23lOI1/PB3lV6I775RIDzXLxCGR4iiDGzeMsQ3lncuXUQMFP7qO9lIQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
  function responsiveTables() {
    const tables = document.getElementsByTagName('table');
    for (let i = 0; i < tables.length; i++) {
      const table = tables[i];
      // Create the responsive container div
      const container = document.createElement('div');
      container.classList.add('v-table-container');
      table.parentNode.insertBefore(container, table);
      container.appendChild(table);
    }
  }

  // Call the function to make tables responsive
  responsiveTables();
</script>

    <script src="/blog/assets/scripts/main.min.js?v=2feabc0f4f"></script>

    <script src="/blog/assets/scripts/videoplayer.min.js?v=2feabc0f4f"></script>

<script type="module">
      import {
        React,
        createRoot,
        Header,
        Footer,
        Cookies,
      } from "https://img.ly/static/imgly-website-components/imgly-website-components.js";

      const initComponents = () => {
        if (document) {
          const FooterDomNode = document.getElementById("imgly-website-components-footer");
          if (FooterDomNode) {
            createRoot(FooterDomNode).render(
                React.createElement(Footer, {})
            );
          }
          const HeaderDomNode = document.getElementById("imgly-website-components-header");
          if (HeaderDomNode) {
            createRoot(HeaderDomNode).render(
                React.createElement(Header, {})
            );
          }
          const CookieDomNode = document.getElementById("imgly-website-components-cookies");
          if (CookieDomNode) {
            createRoot(CookieDomNode).render(
                React.createElement(Cookies, {})
            );
          }
        }
      };

      window.addEventListener("DOMContentLoaded", () => {
        initComponents();
      });
    </script>

    

    <script>
(function(d, s, id) {
    if (typeof disqusShortName === 'undefined') return;

    var disqus_config = function () {
        this.page.url = 'https://img.ly/blog/how-to-resize-images-in-flutter/';
        this.page.identifier = 'ghost-63330230768fba00013b93a6';
    };

    d.querySelector('.js-comments').classList.remove('u-hide')
    /*var disqusComments = d.querySelectorAll('.js-comments');
    disqusComments.forEach(function(item){item.classList.remove('u-hide')});*/

    function loadDisqus() {
        var currentScroll = d.scrollingElement.scrollTop;
        var disqusTarget = d.getElementById('disqus_thread');

        if (d.getElementById(id)) return;

        if( disqusTarget && (currentScroll > disqusTarget.getBoundingClientRect().top - 150) ) {
            var js = d.createElement(s);
            js.id = id;
            js.src = 'https://'+disqusShortName+'.disqus.com/embed.js';
            js.async = true;
            js.defer = true;
            js.setAttribute('data-timestamp', +new Date());
            d.body.appendChild(js);

            window.removeEventListener('scroll', loadDisqus);
        }
    }

    window.addEventListener('scroll', loadDisqus);

    document.querySelector('.js-dark-mode').addEventListener('click', function() {
        if (window.DISQUS) {
            DISQUS.reset({
                reload: true,
                config: disqus_config
            });
        }
    });
}(document, 'script', 'disqus-js'));
</script>

</body>
</html>
