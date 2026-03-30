# Source: https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/

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

    <title>A Modern JavaScript Video Editor: Integration Guide | IMG.LY Blog</title>

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

    <meta name="description" content="Learn how to integrate IMG.LY&#x27;s Javascript video editor into your web app and how to best leverage its capabilities.">
    <link rel="icon" href="https://blog.img.ly/2024/10/publication-icon.png" type="image/png">
    <link rel="canonical" href="https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/">
    <meta name="referrer" content="no-referrer-when-downgrade">
    <link rel="amphtml" href="https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/amp/">
    
    <meta property="og:site_name" content="IMG.LY: Blog">
    <meta property="og:type" content="article">
    <meta property="og:title" content="A Modern JavaScript Video Editor: Integration Guide | IMG.LY Blog">
    <meta property="og:description" content="Learn how to integrate IMG.LY&#x27;s Javascript video editor into your web app and how to best leverage its capabilities.">
    <meta property="og:url" content="https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/">
    <meta property="og:image" content="https://blog.img.ly/2025/01/video-editor-javascript.jpg">
    <meta property="article:published_time" content="2025-01-16T15:29:04.000Z">
    <meta property="article:modified_time" content="2025-05-28T10:30:58.000Z">
    <meta property="article:tag" content="JavaScript">
    <meta property="article:tag" content="Video Editor">
    <meta property="article:tag" content="CE.SDK">
    
    <meta property="article:publisher" content="https://www.facebook.com/imgly">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="A Modern JavaScript Video Editor: Integration Guide | IMG.LY Blog">
    <meta name="twitter:description" content="Learn how to integrate IMG.LY&#x27;s Javascript video editor into your web app and how to best leverage its capabilities.">
    <meta name="twitter:url" content="https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/">
    <meta name="twitter:image" content="https://blog.img.ly/2025/01/video-editor-javascript.jpg">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Antonello Zanini">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="JavaScript, Video Editor, CE.SDK">
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
        "name": "Antonello Zanini",
        "image": {
            "@type": "ImageObject",
            "url": "https://blog.img.ly/2025/01/500x500.jpeg",
            "width": 500,
            "height": 500
        },
        "url": "https://img.ly/blog/author/antozanini95/",
        "sameAs": [
            "https://antonellozanini.com"
        ]
    },
    "headline": "A Modern JavaScript Video Editor: Integration Guide | IMG.LY Blog",
    "url": "https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/",
    "datePublished": "2025-01-16T15:29:04.000Z",
    "dateModified": "2025-05-28T10:30:58.000Z",
    "image": {
        "@type": "ImageObject",
        "url": "https://blog.img.ly/2025/01/video-editor-javascript.jpg",
        "width": 1200,
        "height": 675
    },
    "keywords": "JavaScript, Video Editor, CE.SDK",
    "description": "Learn how to integrate IMG.LY&#x27;s Javascript video editor into your web app and how to best leverage its capabilities.",
    "mainEntityOfPage": "https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
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
    <h1 class="post-title u-marginBottom24">A Modern JavaScript Video Editor: Integration Guide</h1>
    <p class="post-excerpt u-textMuted subheadline read-font">Learn how to integrate IMG.LY&#x27;s Javascript video editor into your web app and how to best leverage its capabilities.</p>

    <hr>

    <div class="u-flex post-share">
        <div class="hh u-flex u-flexCenter u-relative zindex4 u-flex1">
    <ul class="hh-author u-flex u-flexWrap u-flex0">
        <li class="hh-author-item u-realtive">
            <a href="/blog/author/antozanini95/" title="Go to the profile of Antonello Zanini" class="u-relative u-block avatar-image img-md">
                <img
                    class="u-absolute u-image u-block u-round"
                    src="https://blog.img.ly/2025/01/500x500.jpeg"
                    alt="Go to the profile of  Antonello Zanini"
                />
            </a>
        </li>
    </ul>

    <div class="hh-right u-flex1 u-overflowHidden">
        <div class="hh-author-name u-fontSize15 u-noWrapWithEllipsis"><a href="/blog/author/antozanini95/">Antonello Zanini</a></div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-01-16">16 Jan 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="8 min read">8 min read</span>
    
</div>    </div>
</div>
        <aside class="post-share u-flex0 u-flexCenter u-hide-before-md">
            <span class="share-label u-textMuted u-fontSizeSmaller">Share:</span>
            <a href="https://x.com/share?text=A%20Modern%20JavaScript%20Video%20Editor%3A%20Integration%20Guide&amp;url=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Twitter"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-twitter"></use></svg>
            </a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/&amp;title=A%20Modern%20JavaScript%20Video%20Editor%3A%20Integration%20Guide"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Linkedin"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-linkedin"></use></svg>
            </a>
            <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
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
                  srcset="https://blog.img.ly/2025/01/video-editor-javascript.jpg 300w,
                          https://blog.img.ly/2025/01/video-editor-javascript.jpg 600w,
                          https://blog.img.ly/2025/01/video-editor-javascript.jpg 1000w,
                          https://blog.img.ly/2025/01/video-editor-javascript.jpg 2000w"
                  sizes="(max-width: 400px) 300px,(max-width: 730px) 600px, (max-width: 1600px) 100vw"
                  src="https://blog.img.ly/2025/01/video-editor-javascript.jpg"
                  alt="A Modern JavaScript Video Editor: Integration Guide"
              />
          </figure>

      <div class="post-wrap u-maxWidth1080 u-relative u-marginAuto">
          <div id="post-body" class="u-container u-maxWidth688 u-relative">
            <section class="post-body gh-content gh-canvas">
                <aside class="gh-sidebar"><div class="gh-toc">
                    <h4 class="toc-heading">On this Page</h4>
                </div></aside>
                <p><em>Discover how to integrate </em><a href="https://img.ly/docs/cesdk/js/prebuilt-solutions/video-editor-9e533a/?ref=img.ly" rel="noreferrer"><em>IMG.LY's JavaScript video editor</em></a><em> into your web application and unlock its full range of features.</em></p><p>Video content has always been a powerhouse for engagement, becoming even more impactful with the rise of short-form videos. Platforms like YouTube and TikTok have built their empires on video content, as that remains the preferred medium for both creating and consuming information.</p><p>Not only have those platforms changed how we consume information, but they have also transformed user behavior. We do not just want to watch videos—we want to create them, expecting the process to be both simple and professional.</p><p>Here is why embedding video creation and editing capabilities directly into your website, web or mobile application can significantly boost user engagement and satisfaction.</p><p>In this guide, you will learn how to integrate a JavaScript video editor using CreativeEditor SDK (CE.SDK). We will explore when it is most useful and what customizations it supports to suit your unique needs.</p><p>Want to jump into the code? For a quick start, visit our <a href="https://github.com/imgly/cesdk-web-examples/tree/main/integrate-with-vanilla-js?ref=img.ly">GitHub repository</a>.</p><p>Let's dive in!</p><h2 id="why-does-your-javascript-web-app-need-a-video-editor">Why Does Your JavaScript Web App Need a Video Editor?</h2><p>The world of content is constantly evolving—from text to images, from static visuals to long-form videos, and now from long videos to bite-sized clips. What stays consistent is that <a href="https://www.idomoo.com/blog/surprising-video-engagement-statistics/?ref=img.ly">video content resonates deeply with us as humans</a>.</p><p>No wonder, <a href="https://www.statista.com/statistics/1285960/top-downloaded-mobile-apps-worldwide/?ref=img.ly" rel="noreferrer">TikTok tops global app download charts</a>, while <a href="https://www.similarweb.com/top-websites/?ref=img.ly">YouTube, Facebook, and Instagram rank among the most visited sites</a> right after Google. These platforms have not just built their empires on video—they have revolutionized how we think about video production.</p><p>They set the gold standard by enabling anyone to create professional-looking videos with minimal effort, offering tools for adding filters, overlays, audio, and text in just a few clicks. This ease of use has made intuitive video editing a must-have for web applications featuring social media integration, marketing ambitions, or content management capabilities.</p><p>By embedding a user-friendly JavaScript video editor in your application, you can ride this trend, providing a feature billions of users are already familiar with. The payoff? Lower barriers to user-generated content, enhanced engagement, and wider content distribution.</p><p><a href="https://img.ly/products/creative-sdk?ref=img.ly">CreativeEditor SDK</a> from <a href="https://img.ly/?ref=img.ly" rel="noreferrer">IMG.LY</a> delivers a seamless, high-performance, and feature-rich JavaScript solution for in-browser design, video, and photo editing—ready to meet your users' expectations.</p><h2 id="getting-started-adding-a-video-editor-in-javascript">Getting Started: Adding a Video Editor in JavaScript</h2><p>Follow this step-by-step guide to learn how to integrate a JavaScript video editor into your site using CreativeEditor SDK.</p><p>Get started with integrating CE.SDK in a vanilla JavaScript application!</p><h3 id="requirements">Requirements</h3><p>CreativeEditor SDK runs directly in your browser's JavaScript engine, so no specific prerequisites are needed.</p><p>If your web application relies on Node.js, ensure that you have the <a href="https://nodejs.org/en/download?ref=img.ly">latest stable versions of Node.js and NPM installed</a>.</p><h3 id="installation-and-library-import">Installation and Library Import</h3><p>In a vanilla JavaScript application, create a JavaScript module file (e.g., video-editor.js) and import the CreativeEditorSDK library:</p><pre><code class="language-jsx">import CreativeEditorSDK from "&lt;https://cdn.img.ly/packages/imgly/cesdk-js/1.42.0/index.js&gt;"
</code></pre><p><strong>Note</strong>: In this example, the SDK is served from our CDN for convenience. In a production environment, you should <a href="https://img.ly/docs/cesdk/js/serve-assets-b0827c/?ref=img.ly" rel="noreferrer">host assets on your own servers</a> for improved control and performance.</p><p>Alternatively, if you are using a bundler like Webpack, Rollup, Parcel, or Vite, and you want to integrate the CreativeEditor module within your existing project, simply add the <a href="https://www.npmjs.com/package/@cesdk/cesdk-js?ref=img.ly">@cesdk/cesdk-js</a> npm package as a dependency to your project:</p><pre><code class="language-bash">npm install [@cesdk/cesdk-js](&lt;https://www.npmjs.com/package/@cesdk/cesdk-js&gt;)
</code></pre><p>You can then import it as below:</p><pre><code class="language-bash">import CreativeEditorSDK from "@cesdk/cesdk-js";
</code></pre><p>Well done!</p><h3 id="initialize-the-video-editor">Initialize the Video Editor</h3><p>In your JavaScript module, right below the library import, initialize CreativeEditor SDK with the following logic:</p><pre><code class="language-jsx">
// src/video-editor.js

import CreativeEditorSDK from "&lt;https://cdn.img.ly/packages/imgly/cesdk-js/1.42.0/index.js&gt;"

// your CE.SDK license and user configs
const config = {
  license: "&lt;YOUR_LICENSE&gt;",
  userId: "&lt;YOUR_USER_ID&gt;",
};

CreativeEditorSDK.create("#cesdk_container", config).then(async (editor) =&gt; {
  // do something with your instance of CreativeEditor SDK...

  // when done, clean up and free up resources
  editor.dispose();
});
</code></pre><p>Replace <code>&lt;YOUR_LICENSE&gt;</code> with the license key you get from CreativeEditor SDK and <code>&lt;YOUR_USER_ID&gt;</code> with your user ID. The user ID is optional and helps track MAUs (Monthly Active Users) across different devices.</p><p>To integrate the video-editor.js file, import it into your HTML page like this:</p><pre><code class="language-html">&lt;script type="module" src="video-editor.js"&gt;&lt;/script&gt;
</code></pre><p>Note the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules?ref=img.ly">type="module"</a> attribute. This tells the browser to treat the script as an ES6 module, so that you can use import and export statements within your JavaScript code.</p><p>Make sure the same HTML page includes the following div element where the video editor will be embedded:</p><pre><code class="language-html">&lt;div id="cesdk_container" style="width: 100%; height: 100vh;"&gt;&lt;/div&gt;
</code></pre><p>This will load the video editor with the default video preset, giving users the ability to trim, cut, apply filters, add text overlays, include music, and more to enhance their videos.</p><p>Congratulations, you have successfully integrated the video editor!</p><h2 id="creativeeditor-sdk-javascript-video-editing-api-for-web-desktop-and-mobile">CreativeEditor SDK: JavaScript Video Editing API for Web, Desktop, and Mobile</h2><p>You just saw how to integrate the CE.SDK into a browser application. Yet, do not forget that the SDK supports a wide variety of frameworks and libraries—including mobile and web applications.</p><h3 id="web-framework-support">Web Framework Support</h3><p>CE.SDK is designed to work with several popular JavaScript frameworks and libraries. For more detailed integration instructions, take a look at the official page on the documentation for each framework:</p><ul><li><a href="https://img.ly/docs/cesdk/react/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">React</a></li><li><a href="https://img.ly/docs/cesdk/angular/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">Angular</a></li><li><a href="https://img.ly/docs/cesdk/vue/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">Vue</a></li><li><a href="https://img.ly/docs/cesdk/svelte/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">Svelte</a></li><li><a href="https://img.ly/docs/cesdk/js/get-started/overview-e18f40/?ref=img.ly">JavaScript</a></li></ul><p>Additionally, the SDK is available for headless mode and works well in a <a href="https://img.ly/docs/cesdk/node/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">Node.js environment</a>.</p><h3 id="cross-platform-support">Cross-Platform Support</h3><p>One of the standout features of CreativeEditor SDK is its cross-platform philosophy. This extends beyond JavaScript ecosystems for the web, and includes mobile (iOS and Android) and desktop, thanks to support for:</p><ul><li><a href="https://img.ly/docs/cesdk/react-native/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">React Native</a></li><li><a href="https://img.ly/docs/cesdk/electron/get-started/overview-e18f40/?ref=img.ly" rel="noreferrer">Electron</a></li></ul><p>That is made possible through a powerful engine that powers your app via features like:</p><ul><li><strong>Unified API</strong>: The same underlying API is shared across web, desktop, iOS, and Android applications.</li><li><strong>Cross-Platform Feature Parity</strong>: CE.SDK guarantees that features are available consistently across platforms. Since core functionality is implemented at the engine level, features you use on one platform will be available on others, with only slight differences in release timelines.</li><li><strong>Interoperable Designs</strong>: Designs created in the editor component on one platform work on all platforms supported by CE.SDK. Whether a user is designing on iOS, Android, or the web, their design files can be imported seamlessly between platforms.</li></ul><p>Native iOS and Android libraries, along with other frameworks, are also available. <a href="https://img.ly/docs/cesdk/?ref=img.ly">Learn more in our documentation!</a></p><h2 id="javascript-video-editor-use-cases">JavaScript Video Editor Use Cases</h2><p>It is time to explore some key use cases. Let’s see how the unique features of the CreativeEditor SDK can cover many scenarios!</p><h3 id="social-media-publishing">Social Media Publishing</h3><p>CreativeEditor SDK features what users need to create engaging and easy-to-share videos optimized for popular social media platforms like Instagram, TikTok, YouTube, LinkedIn, and more. This is possible due to a large set of capabilities, which include:</p><ul><li><strong>Reusable Templates</strong>: Users can either design their own templates and share them with the community or download those created by others. This variety of ready-to-use templates for different scenarios helps users skip the daunting blank canvas to bring their ideas to life. Explore various templates in our <a href="https://img.ly/showcases/cesdk/video-ui/web?template=month-in-review&ref=img.ly">video editor demo</a>.</li><li><strong>Music and Audio Library</strong>: In CE.SDK, adding audio to videos is simple and intuitive. Given the impact of audio, users can set the tone with music or narration in just a few clicks, creating a more immersive atmosphere for their content.</li><li><strong>Animations</strong>: The SDK includes a <a href="https://img.ly/docs/cesdk/js/animation/overview-6a2ef2/?ref=img.ly" rel="noreferrer">wide selection of animations</a> to enhance the design elements positioned within video scenes.</li></ul><p>After creating a video within your web app, users can export it directly from CE.SDK in the appropriate formats and aspect ratios for their target social media platforms.</p><h3 id="product-showcase-for-e-commerce-applications">Product Showcase for E-Commerce Applications</h3><p>Images have long been a simple yet powerful tool for showcasing products on e-commerce platforms, and sites like eBay, Amazon, AliExpress, and Walmart have relied on them for years (and still do!).</p><p>However, in recent years, customer expectations have shifted. Today’s buyers crave more interactive and immersive ways to visualize products—they want to see how items look and perform in real-world settings.</p><p>Short, dynamic product videos offer a superior presentation experience. According to <a href="https://www.retaildive.com/spons/the-future-of-e-commerce-is-video-5-undeniable-consumer-stats/711062/?ref=img.ly">an analysis by Firework</a>, video content increases purchase likelihood by 51%, highlighting its undeniable impact on buying decisions. This is why many sellers have already embraced video to enhance product displays.</p><p>With a CE.SDK-powered JavaScript video editor, producing compelling videos that deliver a seamless, multi-device shopping experience becomes effortless. Plus, reusable templates help you generate unique product videos while maintaining brand consistency.</p><h3 id="engaging-video-messages-for-sales-outreach">Engaging Video Messages for Sales Outreach</h3><p>Marketers and sales teams know that cold emails often come across as impersonal and boring. The solution to this challenge? Personalized video messages!</p><p>Customized video messages are proving to be an effective outreach tool, with studies showing <a href="https://www.tavus.io/post/video-marketing-statistics?ref=img.ly">significantly higher conversion rates</a>.</p><p>With CreativeEditor SDK, sales and marketing teams can easily create personalized videos tailored to individual clients or leads, making their outreach more engaging and impactful. Unlike traditional email campaigns, personalized videos create a sense of real, one-on-one interaction.</p><p>Additionally, the SDK’s translation features help sales teams break down language barriers, allowing them to reach a global audience. This ensures that the personalized messages resonate with clients from different regions.</p><p>Explore this feature in our <a href="https://img.ly/showcases/cesdk/language/web?ref=img.ly">translation and internationalization demo</a>.</p><h3 id="digital-asset-management">Digital Asset Management</h3><p>DAM, short for <a href="https://www.ibm.com/think/topics/digital-asset-management?ref=img.ly">Digital Asset Management</a>, is the process of organizing, storing, and managing digital assets, including video content. As your business grows, an effective DAM system becomes key to enabling multiple teams to easily access and collaborate on assets across different projects.</p><p>CreativeEditor SDK backs DAM workflows by offering powerful tools to organize, edit, and repurpose video content through an embeddable, centralized interface. Its core JavaScript video editor component empowers users to:</p><ul><li>Effortlessly adapt and customize video assets.</li><li>Ensure brand consistency while automating updates across various assets.</li><li>Edit content efficiently within a collaborative environment.</li></ul><p>Although CE.SDK does not provide built-in role-based permissions, it integrates smoothly with backend systems to control user access. In particular, its flexible architecture supports the definition of custom hooks for permission checks to customize the editor’s behavior.</p><h3 id="automated-video-creation">Automated Video Creation</h3><p>CreativeEditor SDK streamlines the automation of asset creation by enabling users to generate on-brand video content variations for multiple channels. Thanks to adaptable templates, <a href="https://img.ly/docs/cesdk/js/create-templates/add-dynamic-content/text-variables-7ecb50/?ref=img.ly" rel="noreferrer">dynamic text variables</a>, and lockable designs, the SDK ensures consistency and brand compliance over all produced videos.</p><p>Given a template, the creative engine automates the generation of countless personalized assets by populating them with resources from various data sources. That eliminates manual effort, reduces design bottlenecks, and accelerates production, making it perfect for scaling campaign-specific videos or building dedicated <a href="https://img.ly/industries/marketing-tech?ref=img.ly">marketing tech</a>.</p><h2 id="customizing-your-creativeeditor-sdk-instance">Customizing your CreativeEditor SDK Instance</h2><p>CreativeEditor SDK is not a one-size-fits-all JavaScript video editor. Instead, it is built for flexibility, offering a wide set of customization options to tailor the editor to your unique requirements and brand identity. These include:</p><ul><li><strong>Theming Options</strong>: Match the editor’s look to your app’s style with built-in themes, generate new ones using the <a href="https://img.ly/docs/cesdk/js/user-interface/appearance/theming-4b0938/?ref=img.ly#using-the-theme-generator" rel="noreferrer">theme generator</a>, or create custom themes manually. Explore theming possibilities in our <a href="https://img.ly/showcases/cesdk/theming/web?ref=img.ly">dedicated demo</a>.</li><li><strong>Custom UI</strong>: Build entirely bespoke JavaScript video editing user interfaces that align with your specific use case.</li><li><strong>Media Library Integration</strong>: Set up sortable, flexible media libraries and integrate popular third-party libraries like <a href="https://img.ly/showcases/cesdk/unsplash-image-assets/web?ref=img.ly">Unsplash and others</a>. Get easy access to external assets.</li><li><strong>Localization</strong>: Adapt the editor to different languages and regions with <a href="https://img.ly/docs/cesdk/js/user-interface/localization-508e20/?ref=img.ly" rel="noreferrer">full i18n support</a>, letting you extend or overwrite any language setting.</li><li><strong>Toolbar Customization</strong>: Rearrange toolbar elements, update icons, or rename tools to deliver a tailored user experience.</li></ul><p>With these customization options, CreativeEditor SDK ensures your video editor is as unique as your JavaScript application.</p><h2 id="conclusion">Conclusion</h2><p>Implementing a JavaScript video editor in your web app can greatly improve the user experience and provide a powerful feature to drive higher engagement, retention, and even product distribution. This is true whether you are developing an e-commerce platform, a social media app, a tool for influencers, or a SaaS web solution.</p><p>With the CreativeEditor SDK, adding a fully customizable video editing experience to your web application takes only a few minutes. Explore CE.SDK’s video capabilities and <a href="https://img.ly/docs/cesdk/flutter/prebuilt-solutions/video-editor-9e533a/?ref=img.ly" rel="noreferrer">dive into the docs</a>.</p><p>Stay tuned for more updates, and please <a href="https://img.ly/forms/contact-sales?utm_source=imgly&utm_medium=blog&utm_campaign=plugins1">reach out</a> if you have any questions. Thank you for reading.</p><p><strong>Over 3,000 creative professionals gain early access to our new features, demos, and updates—don't miss out, and </strong><a href="https://share.hsforms.com/1IgAOV1wASXGPnFG4ZPLejg1hk3i?ref=img.ly"><strong>subscribe</strong></a><strong> to our newsletter.</strong></p>
            </section>
        </div>
      </div>
    </div>

    <footer class="post-footer u-container u-maxWidth868">
            <div class="post-tags buttonSet u-marginTop30">
        <a href="https://img.ly/blog/tag/javascript/" title="JavaScript" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="JavaScript" data-event-non-interaction="true">JavaScript</a><a href="https://img.ly/blog/tag/video-editor/" title="Video Editor" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Video Editor" data-event-non-interaction="true">Video Editor</a><a href="https://img.ly/blog/tag/ce-sdk/" title="CE.SDK" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="CE.SDK" data-event-non-interaction="true">CE.SDK</a>
    </div>

        <hr>
        <div class="prev-next">
                <div class="u-flex u-relative godo-tracking prev-article u-marginBottom30"
    data-event-category="Article"
    data-event-action="Previous article"
    data-event-label="https://img.ly/blog/modern-react-design-editor/"
    data-event-non-interaction="true">

    <a href="/blog/modern-react-design-editor/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="A Modern React Design Editor: Integration Guide">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2025/01/react-web-design-editor.jpg" alt="A Modern React Design Editor: Integration Guide"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Previous article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/modern-react-design-editor/" class="u-relative zindex3">A Modern React Design Editor: Integration Guide</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Learn how to integrate IMG.LY&#39;s design editor for React into your web app and how to best leverage its capabilities.</p>
    </div>

    <a href="/blog/modern-react-design-editor/" aria-label="A Modern React Design Editor: Integration Guide" class="u-absolute0 zindex2"></a>
</div>
                <div class="u-flex u-relative godo-tracking prev-article "
    data-event-category="Article"
    data-event-action="Next article"
    data-event-label="https://img.ly/blog/how-to-video-generation-with-javascript/"
    data-event-non-interaction="true">

    <a href="/blog/how-to-video-generation-with-javascript/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="How To: Video Generation With Javascript">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2025/01/javascript-generate-video.jpg" alt="How To: Video Generation With Javascript"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Next article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/how-to-video-generation-with-javascript/" class="u-relative zindex3">How To: Video Generation With Javascript</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Learn how to programmatically create videos at scale with Javascript and CreativeEditor SDK.</p>
    </div>

    <a href="/blog/how-to-video-generation-with-javascript/" aria-label="How To: Video Generation With Javascript" class="u-absolute0 zindex2"></a>
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
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/creative-editor-sdk-v-1-69-0-release-notes/" data-event-non-interaction="true">
    <a href="/blog/creative-editor-sdk-v-1-69-0-release-notes/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2026/02/creative-editor-sdk-v169-imgly-whitelabel-design-editor-video-editor-react.jpg"
            srcset="https://blog.img.ly/2026/02/creative-editor-sdk-v169-imgly-whitelabel-design-editor-video-editor-react.jpg"
            data-srcset="https://blog.img.ly/2026/02/creative-editor-sdk-v169-imgly-whitelabel-design-editor-video-editor-react.jpg 300w,https://blog.img.ly/2026/02/creative-editor-sdk-v169-imgly-whitelabel-design-editor-video-editor-react.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="CE.SDK v1.69 Release Notes"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/creative-editor-sdk-v-1-69-0-release-notes/">CE.SDK v1.69 Release Notes</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2026-02-27">27 Feb 2026</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="3 min read">3 min read</span>
    
</div>    </div>

    <a href="/blog/creative-editor-sdk-v-1-69-0-release-notes/" class="u-absolute0 zindex3" aria-label="CE.SDK v1.69 Release Notes"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/capcut-like-video-editor-web-react/" data-event-non-interaction="true">
    <a href="/blog/capcut-like-video-editor-web-react/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2026/02/blogcover.png"
            srcset="https://blog.img.ly/2026/02/blogcover.png"
            data-srcset="https://blog.img.ly/2026/02/blogcover.png 300w,https://blog.img.ly/2026/02/blogcover.png 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="Building a CapCut-Like Video Editor with CE.SDK and AI"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/capcut-like-video-editor-web-react/">Building a CapCut-Like Video Editor with CE.SDK and AI</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2026-02-26">26 Feb 2026</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="10 min read">10 min read</span>
    
</div>    </div>

    <a href="/blog/capcut-like-video-editor-web-react/" class="u-absolute0 zindex3" aria-label="Building a CapCut-Like Video Editor with CE.SDK and AI"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/img-ly-agent-skills-web/" data-event-non-interaction="true">
    <a href="/blog/img-ly-agent-skills-web/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2026/02/Build-Design-Video-Photo-Editor-With-AI-Agent-sdk-imgly-2.jpg"
            srcset="https://blog.img.ly/2026/02/Build-Design-Video-Photo-Editor-With-AI-Agent-sdk-imgly-2.jpg"
            data-srcset="https://blog.img.ly/2026/02/Build-Design-Video-Photo-Editor-With-AI-Agent-sdk-imgly-2.jpg 300w,https://blog.img.ly/2026/02/Build-Design-Video-Photo-Editor-With-AI-Agent-sdk-imgly-2.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="The End of the Integration Tax: Introducing IMG.LY Agent Skills"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/img-ly-agent-skills-web/">The End of the Integration Tax: Introducing IMG.LY Agent Skills</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2026-02-16">16 Feb 2026</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="2 min read">2 min read</span>
    
</div>    </div>

    <a href="/blog/img-ly-agent-skills-web/" class="u-absolute0 zindex3" aria-label="The End of the Integration Tax: Introducing IMG.LY Agent Skills"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/from-prompt-to-editor-running-ce-sdk-inside-chatgpt-with-the-apps-sdk/" data-event-non-interaction="true">
    <a href="/blog/from-prompt-to-editor-running-ce-sdk-inside-chatgpt-with-the-apps-sdk/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/12/chatgpt-open-design-editor-tempalte.jpg"
            srcset="https://blog.img.ly/2025/12/chatgpt-open-design-editor-tempalte.jpg"
            data-srcset="https://blog.img.ly/2025/12/chatgpt-open-design-editor-tempalte.jpg 300w,https://blog.img.ly/2025/12/chatgpt-open-design-editor-tempalte.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="From Prompt to Editor: Running CE.SDK Inside ChatGPT with the Apps SDK"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/from-prompt-to-editor-running-ce-sdk-inside-chatgpt-with-the-apps-sdk/">From Prompt to Editor: Running CE.SDK Inside ChatGPT with the Apps SDK</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-12-19">19 Dec 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="3 min read">3 min read</span>
    
</div>    </div>

    <a href="/blog/from-prompt-to-editor-running-ce-sdk-inside-chatgpt-with-the-apps-sdk/" class="u-absolute0 zindex3" aria-label="From Prompt to Editor: Running CE.SDK Inside ChatGPT with the Apps SDK"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/best-video-sdks-for-mobile-applications-a-comprehensive-comparison-for-developers/" data-event-non-interaction="true">
    <a href="/blog/best-video-sdks-for-mobile-applications-a-comprehensive-comparison-for-developers/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/12/best-video-mobile-editor-sdk.jpg"
            srcset="https://blog.img.ly/2025/12/best-video-mobile-editor-sdk.jpg"
            data-srcset="https://blog.img.ly/2025/12/best-video-mobile-editor-sdk.jpg 300w,https://blog.img.ly/2025/12/best-video-mobile-editor-sdk.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="Best Video SDKs for Mobile Applications: A Comprehensive Comparison for Developers"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/best-video-sdks-for-mobile-applications-a-comprehensive-comparison-for-developers/">Best Video SDKs for Mobile Applications: A Comprehensive Comparison for Developers</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-12-02">2 Dec 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="18 min read">18 min read</span>
    
</div>    </div>

    <a href="/blog/best-video-sdks-for-mobile-applications-a-comprehensive-comparison-for-developers/" class="u-absolute0 zindex3" aria-label="Best Video SDKs for Mobile Applications: A Comprehensive Comparison for Developers"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/best-open-source-video-editor-sdks-2025-roundup/" data-event-non-interaction="true">
    <a href="/blog/best-open-source-video-editor-sdks-2025-roundup/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/11/open-source-video-editor-sdk-whitelabel-best-comparison--1-.jpg"
            srcset="https://blog.img.ly/2025/11/open-source-video-editor-sdk-whitelabel-best-comparison--1-.jpg"
            data-srcset="https://blog.img.ly/2025/11/open-source-video-editor-sdk-whitelabel-best-comparison--1-.jpg 300w,https://blog.img.ly/2025/11/open-source-video-editor-sdk-whitelabel-best-comparison--1-.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="Best Open Source Video Editor SDKs: 2026 Roundup"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/best-open-source-video-editor-sdks-2025-roundup/">Best Open Source Video Editor SDKs: 2026 Roundup</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-11-10">10 Nov 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="12 min read">12 min read</span>
    
</div>    </div>

    <a href="/blog/best-open-source-video-editor-sdks-2025-roundup/" class="u-absolute0 zindex3" aria-label="Best Open Source Video Editor SDKs: 2026 Roundup"></a>
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
        <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
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
        <a href="https://x.com/share?text=A%20Modern%20JavaScript%20Video%20Editor%3A%20Integration%20Guide&amp;url=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
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
        <a href="whatsapp://send?text=https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/"
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
        this.page.url = 'https://img.ly/blog/a-modern-javascript-video-editor-integration-guide/';
        this.page.identifier = 'ghost-67878f8303db320001a75110';
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
