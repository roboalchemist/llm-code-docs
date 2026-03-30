# Source: https://img.ly/blog/ultimate-guide-to-ffmpeg/

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

    <title>FFmpeg - Ultimate Guide | IMG.LY Blog</title>

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

    <meta name="description" content="This guide covers the ins and outs of FFmpeg starting with fundamental concepts and moving to media transcoding and video and audio processing along with practical examples.">
    <link rel="icon" href="https://blog.img.ly/2024/10/publication-icon.png" type="image/png">
    <link rel="canonical" href="https://img.ly/blog/ultimate-guide-to-ffmpeg/">
    <meta name="referrer" content="no-referrer-when-downgrade">
    <link rel="amphtml" href="https://img.ly/blog/ultimate-guide-to-ffmpeg/amp/">
    
    <meta property="og:site_name" content="IMG.LY: Blog">
    <meta property="og:type" content="article">
    <meta property="og:title" content="FFmpeg - Ultimate Guide | IMG.LY Blog">
    <meta property="og:description" content="This guide covers the ins and outs of FFmpeg starting with fundamental concepts and moving to media transcoding and video and audio processing providing practical examples along the way.">
    <meta property="og:url" content="https://img.ly/blog/ultimate-guide-to-ffmpeg/">
    <meta property="og:image" content="https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png">
    <meta property="article:published_time" content="2022-11-21T12:16:19.000Z">
    <meta property="article:modified_time" content="2025-11-11T13:49:03.000Z">
    <meta property="article:tag" content="FFmpeg">
    <meta property="article:tag" content="Video App">
    <meta property="article:tag" content="Audio">
    <meta property="article:tag" content="Tech">
    <meta property="article:tag" content="Tutorial">
    
    <meta property="article:publisher" content="https://www.facebook.com/imgly">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="FFmpeg - Ultimate Guide | IMG.LY Blog">
    <meta name="twitter:description" content="This guide covers the ins and outs of FFmpeg starting with fundamental concepts and moving to media transcoding and video and audio processing providing practical examples along the way.">
    <meta name="twitter:url" content="https://img.ly/blog/ultimate-guide-to-ffmpeg/">
    <meta name="twitter:image" content="https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png">
    <meta name="twitter:label1" content="Written by">
    <meta name="twitter:data1" content="Csaba Kopias">
    <meta name="twitter:label2" content="Filed under">
    <meta name="twitter:data2" content="FFmpeg, Video App, Audio, Tech, Tutorial">
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
        "name": "Csaba Kopias",
        "image": {
            "@type": "ImageObject",
            "url": "https://imgly-blog-prod.storage.googleapis.com/2022/11/csaba.jpeg",
            "width": 800,
            "height": 790
        },
        "url": "https://img.ly/blog/author/csaba/",
        "sameAs": [
            "https://kopiascsaba.hu/"
        ]
    },
    "headline": "FFmpeg - Ultimate Guide | IMG.LY Blog",
    "url": "https://img.ly/blog/ultimate-guide-to-ffmpeg/",
    "datePublished": "2022-11-21T12:16:19.000Z",
    "dateModified": "2025-11-11T13:49:03.000Z",
    "image": {
        "@type": "ImageObject",
        "url": "https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png",
        "width": 1200,
        "height": 675
    },
    "keywords": "FFmpeg, Video App, Audio, Tech, Tutorial",
    "description": "This guide covers the ins and outs of FFmpeg starting with fundamental concepts and moving to media transcoding and video and audio processing providing practical examples along the way.",
    "mainEntityOfPage": "https://img.ly/blog/ultimate-guide-to-ffmpeg/"
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
    <h1 class="post-title u-marginBottom24">FFmpeg - The Ultimate Guide</h1>
    <p class="post-excerpt u-textMuted subheadline read-font">This guide covers the ins and outs of FFmpeg starting with fundamental concepts and moving to media transcoding and video and audio processing providing practical examples along the way.</p>

    <hr>

    <div class="u-flex post-share">
        <div class="hh u-flex u-flexCenter u-relative zindex4 u-flex1">
    <ul class="hh-author u-flex u-flexWrap u-flex0">
        <li class="hh-author-item u-realtive">
            <a href="/blog/author/csaba/" title="Go to the profile of Csaba Kopias" class="u-relative u-block avatar-image img-md">
                <img
                    class="u-absolute u-image u-block u-round"
                    src="https://imgly-blog-prod.storage.googleapis.com/2022/11/csaba.jpeg"
                    alt="Go to the profile of  Csaba Kopias"
                />
            </a>
        </li>
    </ul>

    <div class="hh-right u-flex1 u-overflowHidden">
        <div class="hh-author-name u-fontSize15 u-noWrapWithEllipsis"><a href="/blog/author/csaba/">Csaba Kopias</a></div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2022-11-21">21 Nov 2022</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="59 min read">59 min read</span>
    
</div>    </div>
</div>
        <aside class="post-share u-flex0 u-flexCenter u-hide-before-md">
            <span class="share-label u-textMuted u-fontSizeSmaller">Share:</span>
            <a href="https://x.com/share?text=FFmpeg%20-%20The%20Ultimate%20Guide&amp;url=https://img.ly/blog/ultimate-guide-to-ffmpeg/"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Twitter"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-twitter"></use></svg>
            </a>
            <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://img.ly/blog/ultimate-guide-to-ffmpeg/&amp;title=FFmpeg%20-%20The%20Ultimate%20Guide"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Share on Linkedin"
                class="share-link button button--circle godo-tracking js-share">
                <svg class="icon"><use xlink:href="#icon-linkedin"></use></svg>
            </a>
            <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/ultimate-guide-to-ffmpeg/"
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
                  srcset="https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png 300w,
                          https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png 600w,
                          https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png 1000w,
                          https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png 2000w"
                  sizes="(max-width: 400px) 300px,(max-width: 730px) 600px, (max-width: 1600px) 100vw"
                  src="https://blog.img.ly/2022/11/FFmpeg_ultimate_guide.png"
                  alt="FFmpeg - The Ultimate Guide"
              />
          </figure>

      <div class="post-wrap u-maxWidth1080 u-relative u-marginAuto">
          <div id="post-body" class="u-container u-maxWidth688 u-relative">
            <section class="post-body gh-content gh-canvas">
                <aside class="gh-sidebar"><div class="gh-toc">
                    <h4 class="toc-heading">On this Page</h4>
                </div></aside>
                <p>In this guide, we'll go through the hot topics of FFmpeg. But before that, we'll cover some base ground to help you understand basic media concepts and FFmpeg. Feel free to skip the parts that are already trivial for you!</p><h2 id="introduction-to-ffmpeg">Introduction to FFmpeg</h2><p><a href="https://ffmpeg.org/about.html?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg.org</a>'s definition is the following: "FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation."</p><p>I think of FFmpeg as the go-to application for audio/video manipulation in an automated or scripted manner.</p><p>When you need to implement a service that manipulates video, or just have 300 media files that need to be converted into a different format, FFmpeg is your - nerdy - friend.</p><p>FFmpeg can do large chunks of the basic functionalities of a modern Non-linear (NLE) video editors, e.g., Davinci Resolve Studio or Premiere Pro. But, it does not have a graphical interface in that sense as those behemoths do, and unarguably it is way less friendly.</p><p>In a general NLE, you might do things like these:</p><ol><li>Click to import a file</li><li>Drop it into the timeline</li><li>Trim and Cut</li><li>Add an overlay image</li><li>Crop that overlay</li><li>Add vignette</li><li>Add some color changing effects, e.g. change the hue</li><li>Add an extra audio track to the mix</li><li>Change the volume</li><li>Add some effects, e.g.: echo</li><li>Export into various formats</li><li>Export into a deployable video format</li><li>Export the master audio in wav</li></ol><p>Learn how to <a href="https://img.ly/blog/how-to-crop-and-trim-videos-in-flutter/#get-started">crop and trim videos in Flutter</a>. Or, to achieve the exact same thing, you could also execute this command:</p><pre><code class="language-shell">ffmpeg -y  \
    -ss 20 -t 60 -i bbb_sunflower_1080p_60fps_normal.mp4 \
    -i train.jpg \
    -ss 4 -i voice_recording.wav \
    -filter_complex "[0:v]hue=h=80:s=1[main] ; [1:v]crop=w=382:h=304:x=289:y=227[train] ; [main][train]overlay=x=200:y=200,vignette=PI/4[video] ; [2:a]volume=1.5,aecho=0.8:0.9:100:0.3[speech] ; [0:a][speech]amix=duration=shortest,asplit[audio1][audio2]" \
    -map '[video]' -map '[audio1]' -metadata title="Editor's cut" bbb_edited.mp4 \
    -map '[audio2]' bbb_edited_audio_only.wav</code></pre><p>Yes, it isn't friendly at all, but it is very, very powerful once you become friends with FFmpeg.</p><p>Check out this comparison of the original and the edited one:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-1-edit-before-after.png" class="kg-image" alt="" loading="lazy" width="1520" height="488"></figure><p>If you want to try this command out, get the <a href="#example-material">example</a> files and see it for yourself!</p><h3 id="installing-ffmpeg">Installing FFmpeg</h3><p>FFmpeg is available for most common and even uncommon platforms and architectures. You can be on Linux, Mac OS X or Microsoft Windows, and you'll be able to run or link to FFmpeg.</p><p>Installing FFmpeg is easy on most platforms! There is no installer, usually just a compressed archive you need to get for your platform and architecture.</p><p>In the case of Linux, most distributions include a pre-built FFmpeg in their software repositories. Therefore, you can install FFmpeg from those even more quickly.</p><ul><li><a href="https://ffmpeg.org/download.html?ref=img.ly#build-windows" rel="nofollow noreferrer noopener">Download for Microsoft Windows</a></li><li><a href="https://ffmpeg.org/download.html?ref=img.ly#build-mac" rel="nofollow noreferrer noopener">Download for Mac</a></li><li><a href="https://ffmpeg.org/download.html?ref=img.ly#build-linux" rel="nofollow noreferrer noopener">Download for Linux</a></li></ul><h3 id="ffmpeg-history">FFmpeg history</h3><p>The project was started in 2000 by the awesome <a href="https://bellard.org/?ref=img.ly" rel="nofollow noreferrer noopener">Fabrice Bellard</a>. The name is a concatenation of "FF" meaning "fast-forward" and MPEG, the name of a video standards group. It has been very well, active and alive since then, <a href="https://ffmpeg.org/releases/?ref=img.ly" rel="nofollow noreferrer noopener">releasing</a> a new release about every three months.</p><h3 id="ffmpeg-supported-codecs-and-formats">FFmpeg supported codecs and formats</h3><p>The default FFmpeg shipped with my Ubuntu Linux distribution supports about 460 codecs and 370 formats.</p><p>See it for yourself:</p><pre><code class="language-shell">ffmpeg -codecs
ffmpeg -formats</code></pre><h3 id="compilation-of-ffmpeg">Compilation of FFmpeg</h3><p>Keep in mind that the supported codecs and formats (and filters, demuxers, muxers, input and output methods, etc.) are highly dependent on the so-called compilation flags.</p><p>This means that the above number only represents the fact that it supports at least this many codecs and formats. Still, there are even more that the package builders excluded for various reasons, e.g.: licensing, architecture, size considerations, etc.</p><p>Since FFmpeg is <a href="https://ffmpeg.org/download.html?ref=img.ly#repositories" rel="nofollow noreferrer noopener">open source</a>, you can <a href="https://trac.ffmpeg.org/wiki/CompilationGuide?ref=img.ly" rel="nofollow noreferrer noopener">compile FFmpeg</a> for yourself at any time.</p><p>Suppose for example, that you care about your layer's size (therefore the bootstrap speed) in AWS Lambda. In this case, you can compile an FFmpeg binary that only contains the mp3 encoder for example, and nothing else. For a full tutorial on <a href="https://img.ly/blog/how-to-run-ffmpeg-on-aws-spot-instances-for-scalable-low-cost-video-processing/">running FFmpeg on AWS&nbsp;Spot&nbsp;Instances</a>, see our cloud guide. Prefer Google Cloud? Our guide on <a href="https://img.ly/blog/ffmpeg-on-google-cloud-platform-guide/">running FFmpeg on Google&nbsp;Cloud Platform</a> shows you how.</p><p>Also, you might not want to run into licensing issues and leave out stuff that would cause problems for your use case. Therefore you choose to leave out particular codecs/formats. I highly recommend checking out the "--enable-gpl", "--enable-nonfree" and "--enable-version3" <a href="https://github.com/FFmpeg/FFmpeg/blob/master/configure?ref=img.ly" rel="nofollow noreferrer noopener">compilation flags</a> in this case, as well as <a href="https://ffmpeg.org/legal.html?ref=img.ly" rel="nofollow noreferrer noopener">this</a>.</p><p>Or you might want to have a standalone FFmpeg binary in your project (e.g.: embedded, or some cloud instance), that does not depend on any operating system libraries. Then you want to make a so-called static build, that compiles in all the libraries into a single binary file, and does not depend on your OS' libraries and the runtime loading of other FFmpeg libraries. Search around for "--enable-static" in this case. </p><p>Finally, you can find pre-built static FFmpeg builds <a href="https://johnvansickle.com/ffmpeg/?ref=img.ly" rel="nofollow noreferrer noopener">right here</a> too. Alternatively, you can <a href="https://img.ly/blog/how-to-run-ffmpeg-inside-a-docker-container/">package FFmpeg in a Docker container</a> for consistent environments - our Docker guide covers this approach.</p><h3 id="ffmpegs-strengths">FFmpeg's strengths</h3><p>FFmpeg reads and writes most video and audio formats that matter for most of us. It is a very capable and high-performance tool for converting and manipulating these formats.</p><p>But FFmpeg can do even more! For examples of these operations integrated into an automated pipeline, read our article on a <a href="https://img.ly/blog/building-a-production-ready-batch-video-processing-server-with-ffmpeg/">batch video processing server.</a></p><h3 id="filtering">Filtering</h3><p>FFmpeg has vast amounts of filters for audio and video. Therefore, video manipulation is also a key feature of FFmpeg.</p><h3 id="hardware-acceleration">Hardware acceleration</h3><p>It does support many kinds of hardware accelerations! Video encoding is a very resource-intensive operation, and you might come across quite a few hardware devices or features that might speed up your process!</p><p>Most notably, if you have an NVIDIA card, you can increase your H.264 or H.265 encoding and decoding throughput by multipliers compared to your CPU. But other things, such as VDPAU, VAAPI, or OpenCL, can be leveraged to boost your pipeline's throughput.</p><p>Learn more about the supported hardware acceleration methods <a href="https://trac.ffmpeg.org/wiki/HWAccelIntro?ref=img.ly" rel="nofollow noreferrer noopener">here</a>.</p><h3 id="versatile-inputoutput-methods">Versatile input/output methods</h3><p>FFmpeg is also very capable when it comes to accessing input and output data.</p><p>Just to name a few: it can use your webcam, record from your microphone, grab your screen, or capture from your Blackmagic DeckLink. But FFmpeg can download directly from a web address, open all kinds of streams, read from a pipe, a socket, and of course, from files.</p><p>The same holds true for outputting the data. It can write to your webcam, play audio on your microphone... Just kidding:) It can output to files, streams, pipes, sockets and so on.</p><h3 id="running-example-commands">Running example commands</h3><p>This article is full of FFmpeg commands that are working examples. The reason for that is that you could test these out for yourself! But the command line interfaces of different operating systems are slightly different, so the commands in this article are meant to be executed in a Linux bash shell.</p><p>To adopt these command lines to Microsoft Windows, you might need to:</p><ol><li>Change (cd) into the directory where you extracted the ffmpeg.exe. Alternatively, add that directory to the <a href="https://duckduckgo.com/?t=ffab&q=add+binary+to+path+windows&ref=img.ly" rel="nofollow noreferrer noopener">path</a> to make it callable from anywhere.</li><li>You might need to replace "ffmpeg" to "ffmpeg.exe"</li><li>You will need to replace "<strong>\</strong>"-s (backslashes) at the end of the lines with "<strong>^</strong>"-s (hats)</li><li>You'll need to replace the <code>fontfile</code> argument's value to something like this:  <code>fontfile=/Windows/Fonts/arial.ttf</code> to get commands with the drawtext filter working.</li></ol><p>MacOS users will need steps #1 and #4.</p><h2 id="introduction-to-media-concepts">Introduction to media concepts</h2><p>Now let's have a quick overview of media concepts. These concepts will be vital for us if we want to understand the latter sections of this article and FFmpeg's workings. To keep this section brief, it is a higher-level, simplified explanation of these concepts.</p><h3 id="audio">Audio</h3><p>We'll briefly cover the following terms:</p><ol><li>Sampling rate</li><li>Bitrate</li><li>Channels</li></ol><h3 id="sampling-rate">Sampling Rate</h3><p>The sampling rate is the factor that shows how many times we measure/scan/sample the input data stream.</p><p>The image below shows the measurement windows (quantization) as gray bars.</p><p>Why does this matter? Because it is a balancing act. If we measure the signal less often, we'll lose more details (bad). Also, by having fewer samples, we'll have less data in the end. Therefore the file size will be smaller (good).</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-2-sampling-rate.png" class="kg-image" alt="" loading="lazy" width="1600" height="1200"></figure><p>Here are some ballpark values:</p><ul><li>8 kHz (GSM - Low quality)</li><li>44.1 kHz (CD - High quality)</li><li>48 kHz (Very high quality)</li><li>88.2 kHz (Insane - usually for production only)</li><li>96 kHz (Insane - usually for production only)</li></ul><p>There are no definite "right answers" here. The question is what is "good enough" for your use case? GSM focuses on speech, and not even quality but understandability and the least possible amount of data. Therefore, they found that 8 kHz is enough (there are quite a few more tricks), for their purposes.</p><p>The "CD quality" aimed for high quality. Therefore they chose 44.1 kHz, that number has some history in it, but the main reason for aiming above 40 kHz lies in physics and how the human ear works.</p><p>There were two very smart guys whose <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem?ref=img.ly" rel="nofollow noreferrer noopener">theorem</a> basically says that if you want a quite good signal representation, you have to sample it at twice the speed as its original frequency. Human hearing generally <a href="https://en.wikipedia.org/wiki/Hearing_range?ref=img.ly" rel="nofollow noreferrer noopener">works</a> up until about 20 kHz, so if you want "good quality", you should aim for at least 40 kHz. And 40 kHz + some headroom + some more physics + historical reasons = 44.1 kHz! :)</p><p>As for the higher rates, those are only used when very high-quality audio editing is needed.</p><h3 id="bitrate">Bitrate</h3><p>Bitrate represents the amount of data per second that results from our transcoding/quantization process. If it is 1411 kbit/s, that means that for every second of audio data, about 1411 kbit of output data will be produced.</p><p>Therefore, you can say that 1 minute of audio with 1411 kbit/sec will require:</p><p><code>(1411 kbit / 8) kbyte * 60 second = 10582 kbyte = 10.33 mbyte</code></p><p>Now, it is only easy like that with raw audio data and with a few simple codecs, e.g. PCM in WAVs.</p><p>Codecs compressing hard might throw your numbers around a little, as input data might be compressible with different rates. Variable bitrate is usually happening to save space. The encoder might output a lower bitrate if the data is "simple" and does not require high precision.</p><p>Here are some ballpark values:</p><ul><li>13 kbits/s (GSM quality)</li><li>320 kbit/s (High-quality MP3)</li><li>1411 kbit/s (16bit WAV, CD quality, PCM)</li></ul><h3 id="channels">Channels</h3><p>Inside of most audio formats, you can have more audio channels. This means multiple, separated audio streams can be in the same file.</p><p>Many times, multiple channels have their own name:</p><ul><li>If you have a single microphone, you will most probably record it into a single channel called Mono.</li><li>General music from the FM radio or streaming services usually has two channels in a so-called "Stereo" configuration.</li></ul><p>With stereo, there could be several methods how the audio "image" can be made richer by leveraging audio <a href="https://en.wikipedia.org/wiki/Panning_(audio)?ref=img.ly" rel="nofollow noreferrer noopener">panning</a>, time and phase-shifting and much more. There is a special recording technique too, called <a href="https://en.wikipedia.org/wiki/Binaural_recording?ref=img.ly" rel="nofollow noreferrer noopener">Binaural recording</a>, which is super awesome. Wear headphones for <a href="https://www.youtube.com/watch?v=aQH-jwE_kfo&ref=img.ly" rel="nofollow noreferrer noopener">this</a>, and don't be scared:)</p><p>For example, here are <a href="https://peach.blender.org/?ref=img.ly" rel="nofollow noreferrer noopener">Big Buck Bunny</a>'s audio waveforms in <a href="https://www.audacityteam.org/?ref=img.ly" rel="nofollow noreferrer noopener">Audacity</a>:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-3-waveforms.png" class="kg-image" alt="" loading="lazy" width="1756" height="307"></figure><p>You can see that there are two lines of waveforms and also that they are pretty similar. That is normal, as you usually hear the same thing with your two ears, but the matter is in the subtle differences between the two. That's where directionality, richness, and all kinds of other effects lie.</p><p>But why stop at two? The list continues:</p><ul><li>2.1, as it is often called, means three channels: 2 for stereo and one for the LFE ("low-frequency effects" a.k.a.: "bass").</li><li>5.1 is similar, with five directional channels (2 front, 1 center, 2 rear) and the LFE.</li></ul><p>So channels are just separate "recordings" or "streams" of audio signals.</p><h3 id="image-properties">Image properties</h3><p>For images, there are quite a few parameters, but we'll check out only these:</p><ul><li>Resolution</li><li>Bit-depth</li><li>Transparency</li></ul><h3 id="resolution">Resolution</h3><p>An image consists of pixels, single points that have a single color. The resolution of an image determines how many columns and rows of pixels are in an image. In other words: an image has a width and a height.</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-4-resolution-1.png" class="kg-image" alt="" loading="lazy" width="1520" height="572"></figure><p>This image shows the first 10 pixels in the first row.</p><p>Here are some ballpark values for resolution:</p><ul><li>"HD" or "Full HD" or "1K" or "1080p" means 1920x1080 pixels.</li><li>"4K" could mean a few values, but it should be about 3840x2160 pixels.</li><li>A regular 16mp photo you make of your cat is about 4608x3456 pixels.</li><li>General social media image posts are about 1080x1080 pixels.</li></ul><h3 id="bit-depth">Bit-depth</h3><p>Bit-depth represents the number of bits used for storing a single pixel's color value. This is the same balancing game, and you need to decide between quality or file size.</p><p>General ballpark values for bit-depth:</p>
<!--kg-card-begin: html-->
<table dir="auto" data-sourcepos="370:1-375:55">
<thead>
<tr data-sourcepos="370:1-370:55">
<th data-sourcepos="370:2-370:7">Bits</th>
<th data-sourcepos="370:9-370:16">Colors</th>
<th data-sourcepos="370:18-370:54">Notes</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="372:1-372:55">
<td data-sourcepos="372:2-372:7">1</td>
<td data-sourcepos="372:9-372:16">2</td>
<td data-sourcepos="372:18-372:54">Black &amp; White</td>
</tr>
<tr data-sourcepos="373:1-373:55">
<td data-sourcepos="373:2-373:7">8</td>
<td data-sourcepos="373:9-373:16">256</td>
<td data-sourcepos="373:18-373:54">B/W or Limited color palette</td>
</tr>
<tr data-sourcepos="374:1-374:55">
<td data-sourcepos="374:2-374:7">24</td>
<td data-sourcepos="374:9-374:16">16.7m</td>
<td data-sourcepos="374:18-374:54">3x<strong>8 bit</strong> for R-G-B "True color"</td>
</tr>
<tr data-sourcepos="375:1-375:55">
<td data-sourcepos="375:2-375:7">30</td>
<td data-sourcepos="375:9-375:16">1073m</td>
<td data-sourcepos="375:18-375:54">3x<strong>10 bit</strong> for R-G-B "Deep color"</td>
</tr>
</tbody>
</table>
<!--kg-card-end: html-->
<p>These last two sometimes are referred to as "8 bit" or "10 bit" respectively, especially when talking about videos. That means 8/10 bits per single color channel.</p><h3 id="transparency">Transparency</h3><p>Some image formats support an additional channel together with the red, green, and blue components: the alpha channel. The alpha channel determines how transparent a single pixel is, and it can have different bit-depths, it is usually either 1, 8 or 16 bits.</p><p>If the alpha channel is 1 bit, then the format can encode a pixel to be either transparent or non-transparent. If it is 8 or more bits, then the format can encode 256 or more steps of transparency.</p><h3 id="video-properties">Video properties</h3><p>Video data is built by single images shown right after each other. This brings in most attributes of images and a few more!</p><p>So a video has a <code>resolution</code> that is its width and height.</p><p>Then the first obvious parameter of a video is the <code>framerate</code>, which defines how many images are shown in a second. Common values for this are 24, 25, 30, or 60.</p><p>A video file also has a <code>codec</code> assigned to it, which is the format describing how all those images were compressed into this video file. There are many more attributes of videos, but this is a good start.</p><h3 id="video-codecs">Video codecs</h3><p>Compression is a super important thing when it comes to video because you have thousands of images to keep together. If you aren't doing it in a smart way, then the resulting video will be very, very large.</p><p>Just imagine a 2-minute video, with 30 fps. That means it will have 60 s * 2 * 30 fps = 3600 frames! I have just taken a screenshot of an HD video, which was 730 kbyte in JPEG format. Now 3600 frame * 730 kbyte equals 2.5 gigabytes!</p><p>Can you imagine that? I hope not, and that's because compression brings that way, way down, to the level of tens of megabytes. These days a video of that size is quite high quality and about 2 hours long. Also, don't forget, that JPEG is already compressed, a single frame would be 6 mbyte when uncompressed. Now that 2-minute video would be 21 gigabytes if we'd store it uncompressed.</p><p>Standard codecs such as H.264 and H.265 are doing very clever and complex operations to achieve high compression ratios with good quality.</p><p>Just think about that, most frames in a video are quite similar, only containing small differences. So if we could only store that little difference between frames, we'd won a huge bonus! And that's just one of the many tricks codecs do.</p><p>Codec designers are also exploiting the weaknesses and features of the human eye. Such as the fact that we are more sensitive to light intensity changes than color changes (say hello to <a href="https://en.wikipedia.org/wiki/YUV?ref=img.ly" rel="nofollow noreferrer noopener">YUV</a>). And they can get away with lower quality details for parts <a href="https://en.wikipedia.org/wiki/Motion_blur?ref=img.ly#Biology" rel="nofollow noreferrer noopener">that are moving fast</a>, and so on.</p><p>Because why lose precious bits for things that you can't even notice?!</p><p>There are many codecs out there, with different goals in mind, although the majority focus on keeping the file size low.</p><ul><li>H.264, H.265: These are the most common ones, with the widest support in browsers, phones, players, etc. It focuses on small file sizes with good quality. (At the cost of resource intensiveness.)</li><li>Apple ProRes, DNxHD: These are common formats for production. They focus on quality and ease of processing and not on file size.</li></ul><h3 id="audio-codecs">Audio codecs</h3><p>The goal of audio codecs is the same as what we saw with the video codecs. It is just harder to demonstrate it as audio does not consist of single image frames but audio frames/packets. So an analog audio signal is of an almost infinite, or at least very high quality if you think of it.</p><p>At the lowest level, the speed and amplitude resolution is very high. We could say "atomic", as we need to measure and store the speed and direction of atoms. So if you want to store that exactly, that will require a super high-quality measurement, which will also result in a very high bitrate data stream.</p><p>Thankfully, the sound is at least not propagating with light speed so we can save quite a lot just by that fact. (There's no need for an extreme sampling rate.) Then our hearing is very limited if we take the previous paragraph as a scale, so we win there again. We don't need most of that high precision that is there.</p><p>But still, if we take our hearing capability and want to store raw audio data with about 44.1 kHz of sample rate with about 1 Mbit/sec bitrate, we'd still get quite a lot of data. Check the calculations in the <a href="#bitrate">audio bitrate</a> section above.</p><p>So raw audio can be compressed further, which is what many popular codecs do. They also exploit the human senses, but this time the human ear. We started with the basics that the human ear has a limit on the frequencies it can detect. Therefore, we can save a lot by cutting out the range of frequencies outside our hearing range. Unless you are a bat, you are fine between 20-20khz! :)</p><p>But there are other tricks, for example, <a href="https://en.wikipedia.org/wiki/Auditory_masking?ref=img.ly" rel="nofollow noreferrer noopener">auditory masking</a>. That means that the presence of one frequency can affect your capability to detect a different frequency. From the codec's viewpoint, it can skip encoding a few frequencies if it is smart enough to know which ones you'll not notice. I'm sure there are a lot more tricks, let me know if you know about a few more interesting ones!</p><p>Here is a list of common codecs:</p><ul><li>MP3, AAC, OGG: These are common lossy audio formats.</li><li>PCM (e.g. in a WAV container), FLAC: These are lossless formats.</li><li>MIDI: It is a funny format. It is like a music sheet that might sound different on different players or settings. It is usually not made from real audio data, but from recording a digital keyboard or as an output from an audio composing software.</li></ul><h3 id="containers">Containers</h3><p>Now we got through the fundamental building blocks, the image, the video, the video codecs, and the audio codecs, and we reached the top of this iceberg: the containers.</p><p>A container is a format specification, that combines all these streams into a single file format. It defines how to put all these data together, how to attach metadata (e.g. author, description, etc), how to synchronize these streams, and sometimes a container even contains indexes to aid seeking.</p><p>So, for example, a MOV container can contain an H.264 video stream and an AAC audio stream together.</p><p>Common containers:</p><ul><li>MOV</li><li>MP4</li><li>MKV</li><li>WebM</li><li>WAV (audio only)</li></ul><h2 id="example-material">Example Material</h2><p>I will use these example materials as inputs in the following parts of this article. If you'd like to follow along, save these files for yourself!</p>
<!--kg-card-begin: html-->
<table dir="auto" data-sourcepos="467:1-473:213">
<thead>
<tr data-sourcepos="467:1-467:213">
<th data-sourcepos="467:2-467:25">Name</th>
<th data-sourcepos="467:27-467:212">Resource</th>
</tr>
</thead>
<tbody>
<tr data-sourcepos="469:1-469:213">
<td data-sourcepos="469:2-469:25">Big Buck Bunny</td>
<td data-sourcepos="469:27-469:212"><a rel="nofollow noreferrer noopener" href="http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4?ref=img.ly" target="_blank">http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4</a></td>
</tr>
<tr data-sourcepos="470:1-470:213">
<td data-sourcepos="470:2-470:25">Train</td>
<td data-sourcepos="470:27-470:212"><a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-examples/train.jpg?ref=img.ly">train.jpg</a></td>
</tr>
<tr data-sourcepos="471:1-471:213">
<td data-sourcepos="471:2-471:25">Smiley</td>
<td data-sourcepos="471:27-471:212"><a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-examples/smiley.png?ref=img.ly">smiley.png</a></td>
</tr>
<tr data-sourcepos="472:1-472:213">
<td data-sourcepos="472:2-472:25">Voice recording</td>
<td data-sourcepos="472:27-472:212"><a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-examples/voice_recording.wav?ref=img.ly">voice_recording.wav</a></td>
</tr>
<tr data-sourcepos="473:1-473:213">
<td data-sourcepos="473:2-473:25">Big Buck Bunny's audio</td>
<td data-sourcepos="473:27-473:212">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -map 0:1 bbb_audio.wav</td>
</tr>
</tbody>
</table>n
<!--kg-card-end: html-->
<p>And we will make our own audio file by extracting the audio from the Big Buck Bunny movie! We'll use this file as an example, so after downloading the video file, please execute this:</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -map 0:1 bbb_audio.wav</code></pre><p>By the middle of this article, you'll understand this command, but for now, just make sure to have the WAV file next to your video file to test out the commands later in the article.</p><p>We'll use these files in the following parts of this article. Therefore make sure to get them!</p><h2 id="ffplay-and-ffprobe">FFplay and FFprobe</h2><p>FFmpeg is the name of the main binary and the project itself, but it is shipped together with two other binaries, ffplay and ffprobe.</p><p>Let's check them out quickly, right in the command line!</p><h3 id="ffplay">FFplay</h3><p>FFplay is a basic video player, that can be used for playing media. It's not a friendly video player, but it is a good testing ground for various things.</p><p>To execute it, just simply supply a media file:</p><pre><code class="language-shell">ffplay bbb_sunflower_1080p_60fps_normal.mp4</code></pre><p>If you want to test this exact command, you'll need to get the <a href="#example-material">example</a> files.</p><p>For example, it can be used to preview filters (we'll discuss those <a href="#filtering">later</a>), but let's see an example:</p><pre><code class="language-shell">ffplay -vf "drawtext=text='HELLO THERE':y=h-text_h-10:x=(w/2-text_w/2):fontsize=200:f</code></pre><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-5-big-bunny.png" class="kg-image" alt="" loading="lazy" width="1962" height="1145"></figure><h3 id="ffprobe">FFprobe</h3><p>FFprobe, as its name implies, is a tool for getting information about media files.</p><p>This command:</p><pre><code class="language-shell">ffprobe bbb_sunflower_1080p_60fps_normal.mp4</code></pre><p>Will return us some general information about the video file:</p><pre><code class="language-plaintext">Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'bbb_sunflower_1080p_60fps_normal.mp4':
  Metadata:
[...]
    title           : Big Buck Bunny, Sunflower version
    artist          : Blender Foundation 2008, Janus Bager Kristensen 2013
[...]
  Stream #0:0[0x1](und): Video: h264 [...]
[...]
  Stream #0:1[0x2](und): Audio: mp3 [...]
[...]
  Stream #0:2[0x3](und): Audio: ac3 [...]</code></pre><p>I have abbreviated it heavily, as we'll check this out later.</p><p>But FFprobe is way more powerful than just this!</p><p>With the following command, we can get the same listing in JSON format, which is machine-readable!</p><pre><code class="language-shell">ffprobe -v error -hide_banner -print_format json -show_streams bbb_sunflower_1080p_60fps_normal.mp4</code></pre><p>The explanation of this command is the following:</p><ul><li>"<strong>-v error -hide_banner</strong>": This part hides extra output, such as headers and the default build information.</li><li>"<strong>-print_format json</strong>": Obviously, this causes ffprobe to output a JSON.</li><li>"<strong>-show_streams</strong>" is the main switch that requests the stream information.</li></ul><pre><code class="language-json">{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "width": 1920,
      "height": 1080,
      "bit_rate": "4001453",
      "duration": "634.533333",
      "############################": "[~50 lines removed]"
    },
    {
      "index": 1,
      "codec_name": "mp3",
      "channels": 2,
      "bit_rate": "160000",
      "############################": "[~40 lines removed]"
    },
    {
      "index": 2,
      "codec_name": "ac3",
      "channels": 6,
      "############################": "[~20 lines removed]"
    }
  ]
}
</code></pre><p>In this output, you can see three streams of data in this video file. The first (index: 0) is a video stream, that is an HD video with an H.264 codec. Then we have two audio streams, the first (index: 1) is a simple mp3 stream with stereo audio, and the second (index: 2) is an ac3 stream with 6 channels, most likely in an 5.1 configuration.</p><p>I have removed quite a lot of output for brevity, but you can get way more information out of these streams, e.g. fps for the video stream and so on.</p><p>Other than <strong>-show_streams</strong>, there are 3 more: <strong>-show_format</strong>, <strong>-show_packets</strong> and <strong>-show_frames</strong>. Unless you are really deep in the rabbit hole, you'll not need the last two, but <strong>-show_format</strong> could be useful:</p><pre><code class="language-shell">ffprobe -v error -hide_banner -print_format json -show_format bbb_sunflower_1080p_60fps_normal.mp4</code></pre><pre><code class="language-json">{
  "format": {
    "filename": "bbb_sunflower_1080p_60fps_normal.mp4",
    "nb_streams": 3,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "634.533333",
    "size": "355856562",
    "bit_rate": "4486529",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "1",
      "compatible_brands": "isomavc1",
      "creation_time": "2013-12-16T17:59:32.000000Z",
      "title": "Big Buck Bunny, Sunflower version",
      "artist": "Blender Foundation 2008, Janus Bager Kristensen 2013",
      "comment": "Creative Commons Attribution 3.0 - http://bbb3d.renderfarming.net",
      "genre": "Animation",
      "composer": "Sacha Goedegebure"
    }
  }
}</code></pre><p>This is an overview of "what is this file". As we see, it is a MOV file (format_name), with three streams (nb_streams), and it is 634 seconds long. Also, there are some tags where we can see the title, the artist, and other information.</p><h2 id="ffmpeg-concepts">FFmpeg concepts</h2><p>Here is a quick intro to how FFmpeg actually works!</p><p>For those who are just joining in: please get the <a href="#example-material">example assets</a> if you want to test out the commands shown in this chapter!</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-6-input-output.png" class="kg-image" alt="" loading="lazy" width="1592" height="948"></figure><p>FFmpeg opens the file, decodes it into memory, then encodes the in-memory packets back and puts them into some container: some output file. The term "codec" is a mix of the words "<strong>cod</strong>er &amp; <strong>e</strong>n<strong>c</strong>oder". Those are the magic parts before and after the "decoded frames".</p><p>The decoded frames are uncompressed images in-memory, e.g. the most basic pixel format for video frames is called "rgb24". This just stores red, green, and blue values right after each other in 3x8 bits, or 3x1 byte, which could hold 16m colors.</p><p>The importance of this is that other than <a href="#editing-without-reencoding">a few exceptions</a>, you can only manipulate or encode the decoded frames. So when we get to different audio/video filters or transcoding, you'll need the decoded frames for all that. But don't worry, FFmpeg does this automatically for you.</p><h3 id="inputs">Inputs</h3><p>So you see and probably guessed, that FFmpeg must access the input data somehow. FFmpeg knows how to handle most media files, as the awesome people who develop FFmpeg and the related libraries made encoders and decoders for most formats available!</p><p>Don't think that it is a trivial thing.  Many formats are reverse engineered, a hard task requiring brilliant people.</p><p>So although we often refer to input files, the input could come from many sources, such as the network, a hardware device and so on. We'll learn more about that <a href="#inputs">later</a> on in this article.</p><p>Many media files are containers for different streams, meaning that a single file might contain multiple streams of content.</p><p>For example, a .mov file might contain one or more streams:</p><ul><li>video tracks</li><li>audio tracks (e.g. for the different languages or audio formats such as stereo or 5.1)</li><li>subtitle tracks</li><li>thumbnails</li><li>...</li></ul><p>All these are streams of data from the viewpoint of FFmpeg. Input files and their streams are numerically differentiated with a 0-based index. So, for example, 1:0 means the first(0) stream of the second(1) input file. We'll <a href="#mapping">learn more</a> about that later too!</p><p>Important to note that FFmpeg can open any number of input files simultaneously, and the filtering and mapping will decide what it will do with those. Again more on that later!</p><h3 id="streams">Streams</h3><p>As we have seen in the previous section, streams are the fundamental building blocks of containers. So every input file must have at least one stream. And that's what you can list by the simple <code>ffmpeg -i</code> command for example.</p><p>A stream might contain an audio format such as MP3, or a video format such as an H.264 stream.</p><p>Also, a stream, depending on the codec, might contain multiple "things". For example, an mp3 or a WAV stream might include various audio channels.</p><p>So the building block hierarchy, in this case is: File → Stream → Channels.</p><h3 id="outputs">Outputs</h3><p>Of course, an output could be a local file, but it doesn't need to be. It could be a socket, a stream and so on. In the same way as with inputs, you could have multiple outputs, and the mapping determines what goes into which output file.</p><p>The output also must have some format or container. Most of the time FFmpeg can and will guess that for us, mostly from the extension, but we can specify it too.</p><h3 id="mapping">Mapping</h3><p>Mapping refers to the act of connecting input file streams with output file streams. So if you give 3 input files and 4 output files to FFmpeg, you must also define what should go to where.</p><p>If you give a single input and a single output, then FFmpeg will guess it for you without specifying any mapping, but make sure you know how exactly that happens, to avoid surprises. More on all that later!</p><h3 id="filtering-1">Filtering</h3><p>Filtering stands for the feature of FFmpeg to modify the decoded frames (audio or video). Other applications might call them effects, but i'm sure there is a reason why FFmpeg calls them filters.</p><p>There are two kinds of filtering supported by FFmpeg, simple and complex. In this article we'll only discuss the complex filters, as it is a superset of the simple filters, and this way, we avoid confusion and redundant content.</p><p>Simple filters are a single chain of filters between a single input and output. Complex filters can have more chains of filters, with any number of inputs and outputs.</p><p>The following figure extends the previous overview image with the filtering module:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-7-encode-decode.png" class="kg-image" alt="" loading="lazy" width="1686" height="1520"></figure><p>A <code>complex filter graph</code> is built from <code>filter chains</code>, which are built from <code>filters</code>.</p><p>So a single <strong>filter</strong> does a single thing, for example, changes the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#volume" rel="nofollow noreferrer noopener">volume</a>. This filter is quite trivial, it has a single input, changes the volume, and it has a single output.</p><p>For video, we could check out the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scale" rel="nofollow noreferrer noopener">scale</a> filter, which is also quite straightforward: it has a single input, scales the incoming frames, and it has a single output too.</p><p>You can <strong>chain</strong> these filters, meaning that you connect the output of one to the input of the next one! So you can have a <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#volume" rel="nofollow noreferrer noopener">volume</a> filter after an <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#aecho" rel="nofollow noreferrer noopener">echo</a> filter, for example, and this way, you'll add echo, and then you change the volume.</p><p>This way, your chain will have a single input, and it will do several things with it and will output something at the end.</p><p>Now, the "<strong>complex</strong>" comes in when you have multiple chains of these filters!</p><p>But before we go there, you should also know that some single filters might have multiple inputs or outputs!</p><p>For example:</p><ul><li>The <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#overlay" rel="nofollow noreferrer noopener">overlay</a> filter puts 2 video streams above each other and will output a single video stream.</li><li>The <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#split" rel="nofollow noreferrer noopener">split</a> filter splits a single video stream into 2+ video streams (by copying).</li></ul><p>So let's discuss a complex example from a bird's eye view! I have two video files, I want to put them above each other, and I want the output in two files/sizes, 720p and 1080p.</p><p>Now, that's where complex filtering will be faithful to its name: to achieve this, you'll need several filter chains!</p><ul><li>Chain 1: <code>[input1.mp4] [input2.mp4]</code> → <strong>overlay</strong> → <strong>split</strong> → <code>[overlaid1] [overlaid2]</code></li><li>Chain 2: <code>[overlaid1]</code> → <strong>scale</strong> → <code>[720p_output]</code></li><li>Chain 3: <code>[overlaid2]</code> → <strong>scale</strong> → <code>[1080p_output]</code></li></ul><p>As you see, you can connect chains, and you can connect chains to output files. There is a rule that you can only consume a chain once, and that's why we used split instead of the same input for chains 2 and 3.</p><p>The takeaway is this: with complex filter graphs (and mapping), you can:</p><ul><li>build individual chains of filters</li><li>connect input files to filter chains</li><li>connect filter chains to filter chains</li><li>connect filter chains to output files</li></ul><h2 id="ffmpegs-command-line-system">FFmpeg's command line system</h2><p>For those who are just joining in: please get the <a href="#example-material">example assets</a> if you want to test out the commands shown in this chapter!</p><h3 id="ffmpeg-cli">FFmpeg CLI</h3><p>Finally, we arrived at FFmpeg, and trust me, we'll execute it quite a lot of times! Let's see how FFmpeg's command line options are organized, as that is the first tricky part we need to understand!</p><p>FFmpeg mostly thinks about input and output files and their options together with global options. You specify input files with the "-i" flag followed by a file name. For the output file, specify it as-is without any preceding CLI (command line interface) flag.</p><h3 id="specifying-an-input-file">Specifying an input file</h3><p>Let's specify just an input file:</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 </code></pre><p>The following image helps to understand the output:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-8-output.png" class="kg-image" alt="" loading="lazy" width="1623" height="907"></figure><ol><li>First, you get the "banner", where you see the build information and lib versions. If you watch closely, you'll see the compilation flags, starting with <strong>--</strong>, e.g. --enable-shared.</li><li>Then you get the same output as we have seen with ffprobe earlier.</li><li>And then you get a complaint that there is no output file(s) specified. That's fine for now.</li></ol><p>You can remove the banner here with "-hide_banner", but for brevity's sake I'll not include that anymore in the commands here, and I will leave it out from the outputs too.</p><p>Now, let's get brave, and specify an output file!</p><h3 id="specifying-an-output">Specifying an output</h3><p>As I've said earlier, the output file is understood by FFmpeg as it is just a filename. But more specifically, it is after the input(s) specifications, and it is not a value of any other switches.</p><p>Don't be confused for now, but yes, FFmpeg can have as many inputs and outputs as you'd like. We'll cover that in more detail soon!</p><p>This command line specifies a single output file:</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 audio_only.wav</code></pre><p>Before taking a look at the output, let me congratulate you! You have just converted a video file into an audio file, by keeping just the audio content!</p><p>This is how you transcode! Of course, you'll want to specify more parameters later on.</p><p>So, here is the output:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-9-output.png" class="kg-image" alt="" loading="lazy" width="1174" height="533"></figure><p>Let's analyze it!</p><p>(1) First, we have our input metadata printing, which we saw many times already.</p><p>(2) Then we have something called "stream mapping". We forced FFmpeg into a decision situation, as we specified an input file with 1 video and 2 audio streams. We said we wanted an audio output (guessed from the .wav extension). But we didn't specify which audio stream we wanted, so let's see what FFmpeg decided:</p><ul><li>"<strong>Stream #0:2</strong>" means "The first input file's third stream" or "input file index 0's stream with index 2." This is the input.</li><li>"<strong>-&gt; #0:0</strong>" means the first output file's first stream. This is the output.</li><li><a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly#Automatic-stream-selection" rel="nofollow noreferrer noopener">Here</a> you can learn more about how FFmpeg decide this.</li><li>Later on, we'll manually override the mapping.</li><li>Summary: FFmpeg decided to convert the third stream in the input file (the ac3 5.1 audio) into the first stream of the output file.</li></ul><p>(3) Then we have our output metadata information. This reveals what FFmpeg will output. It usually copies most of the metadata, and here you also see the container/format information too.</p><p>(4) And then we see the output summary. For example, the transcoding was 181x faster than the playback speed. Nice!</p><h3 id="understanding-the-command-line-order">Understanding the command line order</h3><p>Before going further, let's understand FFmpeg's command line arguments from a bird's eye view!</p><p>In the <a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly#Synopsis" rel="nofollow noreferrer noopener">manual</a>, you'll see this:</p><pre><code class="language-shell">ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...</code></pre><p>(Parts in [...] are meant to be optional, and parts in {...} are meant to be specified 1 or more times.)</p><p>This is the general outline of how to specify inputs, outputs, input options, output options, and global options. The order matters, but it is easy to remember: global options, inputs and outputs. Also, i/o options come BEFORE the i/o specification.</p><p>Let's put these into pseudo command line options, to understand it better:</p><pre><code class="language-shell"># One inputs, one output, nothing fancy
ffmpeg -i input1.mp4 output1.wav

# Two inputs, one output 
ffmpeg -i input1.mp4 -i input2.mp4 output1.wav

# Two inputs, two outputs 
ffmpeg -i input1.mp4 -i input2.mp4 output1.wav output2.mp3

# One input, one output, with options
ffmpeg [input1 options] -i input1.mp4 [output2 options] output1.wav

# Two inputs, two outputs with options
ffmpeg [input1 options] -i input1.mp4 \
       [input2 options] -i input2.mp4 \
       [output1 options] output1.wav \
       [output2 options] output2.mp3
</code></pre><p>As for the global options, these are the ones you might care about:</p><ul><li><strong>-hide_banner</strong>: To skip printing the banner.</li><li><strong>-y</strong>: To overwrite the output even if it exists.</li></ul><p>For example, you can run this as many times as you want:</p><pre><code class="language-shell">ffmpeg -y -hide_banner -i bbb_sunflower_1080p_60fps_normal.mp4 audio_only.wav</code></pre><p>And it will overwrite the output and be less verbose than earlier.</p><p>Without explaining the options themselves, let's just see some real-world examples with options:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-10-cmd-order.png" class="kg-image" alt="" loading="lazy" width="1047" height="345"></figure><p>And here it is with two inputs and two outputs:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-11-cmd-order.png" class="kg-image" alt="" loading="lazy" width="1296" height="381"></figure><h3 id="mapping-files">Mapping files</h3><p>We saw above that this command:</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 audio_only.wav</code></pre><p>... will result in an audio file that contains one of the audio streams from the input video chosen by FFmpeg. This <a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly#Automatic-stream-selection" rel="nofollow noreferrer noopener">automatic stream selection</a> is usually handy when it is trivial. For example, when you have one stream as input and one output file, you don't need to specify any mapping manually.</p><p>But in cases where it is not so trivial, you are usually better off manually specifying what you really want to do.</p><p>The following image summarises what our current situation is:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-12-mapping.png" class="kg-image" alt="" loading="lazy" width="1770" height="918"></figure><p>The video stream was not matched, as the output format was an audio file (.wav). But then FFmpeg chose Stream #2, because it has more channels.</p><p>So what if we'd like to get the stereo track instead? That is where mapping comes in! The mapping is a parameter of the OUTPUT file. Therefore the mapping arguments should come right before our output file definition!</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -map 0:1 stereo_audio_only.wav</code></pre><p>The argument <strong>-map 0:1</strong> means, that in the <code>output</code> (since we specify it as an output option) we'd like to have <code>Input #0</code>'s (the first input file) <code>Stream #1</code>!</p><p>Let's see the relevant parts from the output!</p><pre><code class="language-plaintext">Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'bbb_sunflower_1080p_60fps_normal.mp4':

[...]

Stream mapping:
  Stream #0:1 -&gt; #0:0 (mp3 (mp3float) -&gt; pcm_s16le (native))
  
[...]

Output #0, wav, to 'stereo_audio_only.wav':
  Metadata:
[...]
    Stream #0:0(und): [...] stereo [...]
</code></pre><p>The "Stream #0:1 -&gt; #0:0" part means that we have successfully overridden the mapping, to get the mp3 stream (0:1) into our output! Also, the output metadata reveals that we'll get a stereo result instead of the 5.1 earlier.</p><h3 id="multiple-outputs">Multiple outputs</h3><p>You can have multiple outputs from a single input, let's see when that might be useful!</p><p>Let's say, we want to extract BOTH audio streams into two separate WAV files! It is super easy:</p><pre><code class="language-shell">ffmpeg -y -i bbb_sunflower_1080p_60fps_normal.mp4 -map 0:1 stereo_audio_only.wav -map 0:2 ac3_audio_only.wav</code></pre><p>See? I have just specified two output files with two mapping specifications! Also, I have sneaked in the "-y" to have it overwrite our previous file!</p><p>Let's check out the relevant parts of the output!</p><pre><code class="language-plaintext">Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'bbb_sunflower_1080p_60fps_normal.mp4':

[...]

Stream mapping:
  Stream #0:1 -&gt; #0:0 (mp3 (mp3float) -&gt; pcm_s16le (native))
  Stream #0:2 -&gt; #1:0 (ac3 (native) -&gt; pcm_s16le (native))

[...]

Output #0, wav, to 'stereo_audio_only.wav':
    Stream #0:0(und): [...] stereo
    
[...]

Output #1, wav, to 'ac3_audio_only.wav':
    Stream #1:0(und): Audio: [...] 5.1(side)</code></pre><p>Now the mapping reveals two lines, as we have two outputs! And indeed, you'll get two .wav files as the output, one is stereo, and one is 5.1!</p><p>There might be several other reasons why you'd want to get multiple outputs. Let's briefly check out a few!</p><p>Different formats:</p><pre><code class="language-shell">ffmpeg -y -i bbb_sunflower_1080p_60fps_normal.mp4 stereo_audio_only.wav  stereo_audio_only.mp3 </code></pre><p>Wow, did you catch that? We just created a WAV and an mp3 in a single command line! I've reverted to the automatic stream selection for brevity's sake.</p><p>A bit closer to real-life needs, you might want different output qualities:</p><pre><code class="language-shell">ffmpeg -y  -i bbb_sunflower_1080p_60fps_normal.mp4  \
-map 0:1 -b:a 320k stereo_audio_only_high_quality.mp3 \
-map 0:1 -b:a 64k  stereo_audio_only_low_quality.mp3 </code></pre><p>Here <strong>-b:a 320k</strong> means "<strong>b</strong>itrate of <strong>a</strong>udio should be around <strong>320 kbit/sec</strong>". So I have requested FFmpeg to make two mp3s for me, from the stereo stream of the input.</p><p>Checking on the files, this is what we got:</p><pre><code class="language-plaintext"> 25Mb stereo_audio_only_high_quality.mp3
4,9Mb stereo_audio_only_low_quality.mp3</code></pre><p>One more common reason for having multiple outputs or using mapping is when we introduce filters into our pipeline, but that will be discussed later!</p><p>Now you understand the foundations of how to communicate your basic requirements to FFmpeg via its command line! Great job! Now we can dive even deepert.</p><h2 id="hands-on-with-ffmpeg">Hands-on with FFmpeg</h2><p>In this section, we will discover and even try out some common features of FFmpeg!</p><p>For those who are just joining in: please get the <a href="#example-material">example assets</a> if you want to test out the commands shown in this chapter!</p><h3 id="inputs-1">Inputs</h3><p>Let's see the common ways FFmpeg is fed with different data!</p><h3 id="file">File</h3><p>Of course, you have already seen that if you have a local file on your filesystem, FFmpeg is happy to read it!</p><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -map 0:1 stereo_audio_only.wav</code></pre><p>This command which is exactly the same as one of our previous ones just reads a local file. Really, that's it.</p><h3 id="network">Network</h3><p>Did you know, that FFmpeg can open a file directly on the network?!</p><pre><code class="language-shell">ffmpeg -t 5 -i http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4 bbb_first_5_seconds.mp4</code></pre><p>The command above opens the file directly from the network and saves the first 5 seconds into a local file!</p><p>I wanted to spare bandwidth for these awesome guys over renderfarming.net, so I added the duration flag: <strong>-t 5</strong>. FFmpeg doesn't even download the full video for this operation. Isn't that wonderful?!</p><h3 id="webcam">Webcam</h3><p>FFmpeg can also open your webcam!</p><p>This is an example command for Linux:</p><pre><code class="language-shell">ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -t 10 -i /dev/video0 10seconds_of_webcam.webm</code></pre><p>This would record 10 seconds of your webcam!</p><p>Accessing the webcam happens differently on different platforms. Also specifying parameters is different for each platform, so for this reason, if you'd like to access your webcam with FFmpeg, please refer to the documentation:</p><ul><li><a href="https://trac.ffmpeg.org/wiki/Capture/Webcam?ref=img.ly#Linux" rel="nofollow noreferrer noopener">Linux</a></li><li><a href="https://trac.ffmpeg.org/wiki/Capture/Webcam?ref=img.ly#Windows" rel="nofollow noreferrer noopener">Windows</a></li><li><a href="https://trac.ffmpeg.org/wiki/Capture/Webcam?ref=img.ly#OSX" rel="nofollow noreferrer noopener">OS X</a></li></ul><h3 id="microphone">Microphone</h3><p>Let's record some audio directly from your microphone!</p><p>List microphones:</p><pre><code class="language-shell">arecord -l</code></pre><p>Start 10 seconds of recording:</p><pre><code class="language-shell">ffmpeg -f alsa -i hw:0,0 -t 10 out.wav</code></pre><p>This command was meant to work on Linux, but you can check out how to do that on <a href="https://trac.ffmpeg.org/wiki/Capture/Desktop?ref=img.ly#Windows" rel="nofollow noreferrer noopener">Microsoft Windows</a> or <a href="https://trac.ffmpeg.org/wiki/Capture/Desktop?ref=img.ly#macOS" rel="nofollow noreferrer noopener">macOS</a>.</p><h3 id="pipe">Pipe</h3><p>Finally, FFmpeg can read from a pipe, and also output to a pipe.</p><p>On Linux, you could do something like this:</p><pre><code class="language-shell">cat bbb_sunflower_1080p_60fps_normal.mp4 | ffmpeg -i - -f wav pipe:1 | pv &gt; output.wav

# Alternative, without pv:
cat bbb_sunflower_1080p_60fps_normal.mp4 | ffmpeg -i - -f wav pipe:1 &gt; output.wav</code></pre><p>This command would use the <strong>cat</strong> program to simply read in the video file and output it to its standard output. Then this output is piped INTO FFmpeg, through its standard input. The combination "<strong>-i -</strong>" means "read from standard input". By the way, standard input would be your keyboard otherwise, if we wouldn't use any redirection here.</p><p>Then we specify the required output format for FFmpeg, with "<strong>-f wav</strong>". This is needed because now we'll have no output file name, and FFmpeg will not be able to guess the format. Then we specify "<strong>pipe:1</strong>" as an output, meaning we'd like FFmpeg to output to its standard output.</p><p>From then, we pipe the data into a program called "<strong>pv</strong>", it is just a metering tool, that dumps information on the throughput (from its stdin to its stdout). Finally, we redirect pv's output into a WAV file.</p><p>You might ask why we'd want to do that, why we talk about this. Piping can be useful if you build a complex pipeline from different programs or if you want to spare reading and writing to a local file.</p><p>For example, the node package <a href="https://www.npmjs.com/package/fluent-ffmpeg?ref=img.ly" rel="nofollow noreferrer noopener">fluent-ffmpeg</a> can leverage this functionality by supplying input and output streams. For example, you can read from an S3 bucket and write to one directly.</p><p>But be warned, hell is awaiting you on that road. No kidding. You need to research the limitations of this technique. For example, many formats can not be streamed in this manner, as they need random access to the output data to write the indices at the beginning of the file after processing.</p><h3 id="outputs-1">Outputs</h3><p>FFmpeg can output into many protocols, from local file storage and ftp to message queue protocols all the way to streaming protocols.</p><p>For more information, check out the documentation <a href="https://ffmpeg.org/ffmpeg-protocols.html?ref=img.ly#Protocols" rel="nofollow noreferrer noopener">here</a>.</p><h2 id="transcoding-audio-with-ffmpeg">Transcoding audio with FFmpeg</h2><p>In this chapter, we'll be going to see how to transcode into audio with FFmpeg!</p><p>The general formula is:</p><pre><code class="language-shell">ffmpeg -i {input audio or video file with audio} [output options] output_audio.ext</code></pre><h3 id="choosing-a-format">Choosing a format</h3><p>FFmpeg is quite smart, and by the extension, it can determine which codec to use. If you specify "audio.wav" or "audio.mp3" for example, FFmpeg will use the appropriate codec to do the encoding.</p><p>It is perfectly guessing most of the time. But if you want to specify the format manually, then the "-f" flag is your friend.</p><p>For this, you might want to consult the list of formats:</p><pre><code class="language-shell">ffmpeg -formats</code></pre><p>So, these three commands will do exactly the same, but the last two requires the <strong>-f</strong> flag.</p><pre><code class="language-shell"># Output codec is determined from the extension
ffmpeg -i bbb_audio.wav bbb_audio.mp3

# No extension in the filename
ffmpeg -i bbb_audio.wav -f mp3 bbb_audio

# Piped output therefore no filename, so no extension to use for guessing
ffmpeg -i bbb_audio.wav -f mp3 pipe:1 &gt; bbb_audio</code></pre><h3 id="setting-the-bitrate">Setting the bitrate</h3><p>In most cases. you want to specify the target bitrate you expect from your codec to output. If you are unsure what bitrate is, please read this article's <a href="#bitrate">audio bitrate</a> section.</p><p>To specify the audio bitrate, use the "<strong>-b:a</strong>" option with a corresponding value, e.g.:</p><ul><li><strong>-b:a 320k</strong>: For the mp3 codec this is considered high quality.</li><li><strong>-b:a 128k</strong>: Lower quality.</li><li><strong>-b:a 64k</strong>: Low quality.</li></ul><p>For example:</p><pre><code class="language-shell">ffmpeg -i bbb_audio.wav -b:a 320k bbb_audio_320k.mp3</code></pre><h3 id="setting-the-sample-rate">Setting the sample rate</h3><p>You may want to specify the sample rate to ensure quality or low output file size. Half the sample rate could mean half the output file size. If you are unsure what the sample rate is, please read the "<a href="#sampling-rate">audio sample rate</a>" section of this article.</p><p>To specify the audio sample rate, use the "<strong>-ar</strong>" option with a corresponding value, e.g.:</p><ul><li><strong>-ar 48000</strong>: For high quality.</li><li><strong>-ar 44100</strong>: For CD quality (still high).</li><li><strong>-ar 22500</strong>: A bit of a compromise, not recommended for music, but for speech, it might be enough.</li><li><strong>-ar 8000</strong>: Low quality, e.g. if you only want "understandable" speech.</li></ul><p>For example:</p><pre><code class="language-shell">ffmpeg -i bbb_audio.wav -ar 44100 bbb_audio_44100khz.mp3</code></pre><h3 id="setting-the-channel-count">Setting the channel count</h3><p>Setting the channel count can be useful, for example, if you have a stereo recording of a single person's speech. In that case, you might be content with just a mono output half the size of the original recording.</p><p>If you are unsure what an audio channel is, please read the "<a href="#channels">audio channels</a>" section of this article.</p><p>To specify the channel count use the  "<strong>-ac</strong>" option with a corresponding value, e.g.:</p><ul><li><strong>-ac 1</strong>: For mono</li><li><strong>-ac 2</strong>: For stereo</li><li><strong>-ac 6</strong>: For 5.1</li></ul><p>For example:</p><pre><code class="language-shell">ffmpeg -i bbb_audio.wav -ac 1 bbb_audio_mono.mp3</code></pre><h3 id="complete-command-line-for-converting-audio-with-ffmpeg">Complete command line for converting audio with FFmpeg</h3><p>This is how you produce a high-quality output:</p><pre><code class="language-shell"># Convert wav to mp3
ffmpeg -i bbb_audio.wav -ac 2 -ar 44100 -b:a 320k bbb_audio_hqfull.mp3

# Convert wav to m4a (aac)
ffmpeg -i bbb_audio.wav -ac 2 -ar 44100 -b:a 320k bbb_audio_hqfull.m4a

# Convert wav to ogg (vorbis)
ffmpeg -i bbb_audio.wav -ac 2 -ar 44100 -b:a 320k bbb_audio_hqfull.ogg
</code></pre><p>Check out <a href="https://trac.ffmpeg.org/wiki/Encode/HighQualityAudio?ref=img.ly" rel="nofollow noreferrer noopener">this</a> documentation about good quality audio transcoding too!.</p><h3 id="lossless-formats">Lossless formats</h3><p>If you want to convert audio into a lossless format, here are a few choices for you:</p><pre><code class="language-shell"># Convert to flac (Free Lossless Audio Codec)
ffmpeg -i bbb_audio.wav -compression_level 12 bbb_audio_lossless_12.flac # Best compression, slowest
ffmpeg -i bbb_audio.wav -compression_level 5 bbb_audio_lossless_5.flac   # Default
ffmpeg -i bbb_audio.wav -compression_level 0 bbb_audio_lossless_0.flac   # Least compression, fastest


# Convert to wav
cp bbb_audio.wav bbb_audio_lossless.wav # Just kidding:)

# Convert to wav 
ffmpeg -i any_audio.ext bbb_audio_lossless.wav</code></pre><p>It's good if you know that flac results in a smaller file than WAV, as WAV doesn't actually compress by default:</p><pre><code class="language-plaintext">117M bbb_audio.wav
52M  bbb_audio_lossless_0.flac
45M  bbb_audio_lossless_5.flac
43M  bbb_audio_lossless_12.flac</code></pre><p>WAV is generally thought of as a lossless format, but keep in mind that the WAV container can contain lossy content too, but by default FFmpeg uses the pcm_s16le format, which is the 16 bit PCM, that could be understood as lossless.</p><p>Learn more <a href="https://en.wikipedia.org/wiki/WAV?ref=img.ly#Comparison_of_coding_schemes" rel="nofollow noreferrer noopener">here</a> and <a href="https://trac.ffmpeg.org/wiki/audio%20types?ref=img.ly" rel="nofollow noreferrer noopener">here</a>.</p><h2 id="transcoding-video-with-ffmpeg">Transcoding video with FFmpeg</h2><p>In this chapter, we'll be going to see how to transcode a video file into the two most common formats!</p><h3 id="converting-to-h264">Converting to H.264</h3><p><a href="https://en.wikipedia.org/wiki/Advanced_Video_Coding?ref=img.ly" rel="nofollow noreferrer noopener">H264</a> is one of the most popular video codecs. Most devices, browsers and video players understand how to play it. It is efficient in storing video content, but as with most advanced video codecs, it is a resource intensive-process to encode and decode.</p><p>A complete command line for a high-quality H.264 transcoding with high-quality AAC audio is the following:</p><pre><code class="language-shell">ffmpeg -y -i bbb_sunflower_1080p_60fps_normal.mp4 \
-c:v libx264 -preset slow -crf 22 \
-profile:v main -g 250 -pix_fmt yuv420p \
-map 0:0 -map 0:1 \
-acodec aac -ar 44100 -b:a 320k bbb_transcoded_h264_HQ.mov</code></pre><p>Make sure to understand this command and to customize it to match your needs.</p><p>To help you do that, let's dissect this command!</p><p>Global options:</p><ul><li><strong>-y</strong>: Overwrite the output.</li></ul><p>Input options:</p><ul><li><strong>-i bbb_sunflower_1080p_60fps_normal.mp4</strong>: The input file.</li></ul><p>Output options:</p><p><strong>-c:v libx264</strong>: Set the codec to libx264.</p><p><strong>-preset slow</strong>: libx264 has a lot of variables that you can be tune, and most of them balance the coding speed and the resulting file size. To make your life easier, there are <a href="https://trac.ffmpeg.org/wiki/Encode/H.264?ref=img.ly#Preset" rel="nofollow noreferrer noopener">presets</a> by which you can easily declare what you need: small size or speed.</p><p><strong>-crf 22</strong>: This is the constant rate factor, the main option for setting image quality. It is a number between 0-51, where 0 is lossless, and 51 is the worst quality. Generally, you want something between 17 and 28. This is the option to tune the balance between image quality and file size. Check my comparison video <a href="#comparing-crf-values-with-h264-and-h265">here</a>.</p><p><strong>-profile:v main -g 250 -pix_fmt yuv420p</strong>: These are advanced options, guaranteeing you a quite backward compatible result. (See <a href="https://ffmpeg.org/ffmpeg-codecs.html?ref=img.ly#Options-26" rel="nofollow noreferrer noopener">this</a>, <a href="https://trac.ffmpeg.org/wiki/Encode/H.264?ref=img.ly#Profile" rel="nofollow noreferrer noopener">this</a>, and <a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly#Advanced-Video-options" rel="nofollow noreferrer noopener">this</a>.)</p><p><strong>-map 0:0 -map 0:1</strong>: You might not need this: these options are selecting the correct video and audio streams. <a href="#ffprobe">In our case</a>, we have two audio streams, and we need the stereo one to avoid some issues with our aac stream.</p><p><strong>-acodec aac</strong>: Select the AAC (Advanced Audio Coding) <a href="#audio-codecs">codec</a> for the audio in the output. We need to be more specific than just <strong>-f</strong> for the format. We need to specify the audio codec here manually.</p><p><strong>-ar 44100</strong>: Set the audio <a href="#sampling-rate">sampling rate</a> (learn more about that in previous chapters of this article).</p><p><strong>-b:a 320k</strong>: Set the audio <a href="#bitrate">bitrate</a> (learn more about that in previous chapters of this article).</p><p><strong>30seconds_of_bb.mkv</strong>: The output file name. All the options since the last -i (or the last output file) considered to be a modifier for this output.</p><p>Let's see the output:</p><pre><code class="language-plaintext">Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'bbb_sunflower_1080p_60fps_normal.mp4':

[...]

Stream mapping:
  Stream #0:0 -&gt; #0:0 (h264 (native) -&gt; h264 (libx264))
  Stream #0:1 -&gt; #0:1 (mp3 (mp3float) -&gt; aac (native))

[...]

Output #0, mov, to 'bbb_transcoded_h264_HQ.mov':
    Stream #0:0(und): Video: h264 (libx264) (avc1 / 0x31637661), yuv420p(progressive), 1920x1080 [SAR 1:1 DAR 16:9], q=-1--1, 60 fps, 15360 tbn, 60 tbc (default)
    Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, 5.1(side), fltp, 320 kb/s (default)

[...]

frame=38074 fps= 35 q=-1.0 Lsize=  324855kB time=00:10:34.51 bitrate=4194.1kbits/s dup=2 drop=0 speed=0.58x </code></pre><p>From this, we understand that FFmpeg chose the mp3 stream from the input file because we told it to do so. (Remember, it has two audio streams in it, a stereo mp3 and a 5.1 ac3.) We also see that my machine could transcode with 35fps (0.58 times the playback speed), and our settings resulted in an average video bitrate of 4200 kbit/s.</p><p>The video bitrate is an interesting question in this mode. With the CRF option, we specify the "constant visual quality" we want. To reach a constant visual quality, the encoder works hard to guess how much it can compress certain parts of every frame, and the result of that guess defines the final average video bitrate.</p><p>If you want even better results with H.264, and you can afford a bit more processing time and a bit more complicated process, check out the <a href="https://trac.ffmpeg.org/wiki/Encode/H.264?ref=img.ly#twopass" rel="nofollow noreferrer noopener">2-pass encoding</a> instead of the constant rate factor method introduced above.</p><p>To learn more about these two different rate control methods, read the awesome <a href="https://slhck.info/video/2017/03/01/rate-control.html?ref=img.ly" rel="nofollow noreferrer noopener">Understanding Rate Control Modes</a> article. And to learn more about the intricacies of H.264 encoding, check out the <a href="https://trac.ffmpeg.org/wiki/Encode/H.264?ref=img.ly" rel="nofollow noreferrer noopener">H264 encoding guide</a>.</p><p>Finally, <a href="#comparing-crf-values-with-h264-and-h265">later on</a>, I will show you a comparison video that shows how different CRF values perform!</p><h3 id="converting-to-h265">Converting to H.265</h3><p>H.265 is the successor of H.264, according to the <a href="https://trac.ffmpeg.org/wiki/Encode/H.265?ref=img.ly" rel="nofollow noreferrer noopener">official FFmpeg manual</a>, it offers 25-50% bitrate savings while retaining the same visual quality.</p><p>A complete command line for a high-quality H.265 transcoding with high-quality AAC audio is the following:</p><pre><code class="language-shell">ffmpeg -y -i bbb_sunflower_1080p_60fps_normal.mp4 \
-c:v libx265 -preset slow -crf 27 \
-profile:v main -g 250 -pix_fmt yuv420p \
-map 0:0 -map 0:1 \
-acodec aac -ar 44100 -b:a 320k bbb_transcoded_h265_HQ.mov</code></pre><p>And the result is:</p><pre><code class="language-plaintext">...
encoded 38074 frames in 3384.84s (11.25 fps), 1720.32 kb/s, Avg QP:35.29</code></pre><p>H.265 also has multiple rate control algorithms, I used the CRF method here. If you want to use a different rate control algorithm, then you may check out the <a href="https://trac.ffmpeg.org/wiki/Encode/H.265?ref=img.ly" rel="nofollow noreferrer noopener">H.265 encoding guide</a>. Also, check out the next section, where I'll reveal how different CRF values perform!</p><p>This command is almost the same as what we used in the <a href="#converting-to-h264">H.264 example</a> above, so please refer to that section to understand the arguments.</p><p>If we compare H.264 and H.265 with our commands above, taking into account this 10-minute long video on my system, these are the results:</p><ul><li>H.264 is 3 times faster (35 fps vs 11 fps)</li><li>H.264 produces a 2 times larger file (318 mb vs 156 mb)</li></ul><h3 id="comparing-crf-values-with-h264-and-h265">Comparing CRF values with H.264 and H.265</h3><p>I have created a video for your convenience, that shows the different crf values in action. The selected frame had some movement on it with the leaves in the bunny's hand. Movement is important with video codecs, as usually that's where quality losses are first visible.</p><p>This video shows how the different CRF values perform, from 0-51 with the H.264 and H.265 formats!</p><p><a href="https://storage.googleapis.com/imgly-static-assets/static/blog/videos/vid-1-comparison-264-265.mov?ref=img.ly">H.264 &amp; H.265 CRF comparison video</a></p><p>(Can you guess which program I was using to make this?:))</p><h2 id="basic-editing-with-ffmpeg">Basic editing with FFmpeg</h2><p>In this section, we'll achieve basic editing tasks by using FFmpeg only!</p><p>We'll just get a basic mp4 with default settings in these examples to keep things simple. But to encode the result in a proper, high quality way, please check the earlier sections where we learned how to encode into H.264 and H.265!</p><h3 id="trimming-from-the-beginning-of-the-clip">Trimming from the beginning of the clip</h3><p>It is possible to specify an in-point for a media file. By doing that, you essentially cut off the specified amount from the beginning of the input file. Therefore, FFmpeg will skip the first part of the file and only transcode the remainder!</p><p>For this, you need the "<strong>-ss</strong>" flag! The value can be specified in seconds (5 or 5.2) or as a timestamp (HOURS:MM:SS.MILLISECONDS).</p><p>To get the outro only, we could seek all the way to the end of the video! (It is 00:10:34.53 or 635 seconds long!)</p><pre><code class="language-shell"># Get 
# 635 - 4 = 631
ffmpeg -y -ss 631 -i bbb_sunflower_1080p_60fps_normal.mp4 last_4_seconds.mp4


# 00:10:34.53 - 4 = 00:10:30.53
ffmpeg -y -ss 00:10:30.53 -i bbb_sunflower_1080p_60fps_normal.mp4 last_4_seconds.mp4</code></pre><p>Seeking can be a bit tricky, so you may want to learn more about seeking <a href="https://trac.ffmpeg.org/wiki/Seeking?ref=img.ly" rel="nofollow noreferrer noopener">here</a>.</p><h3 id="trimming-from-the-end-of-the-clip">Trimming from the end of the clip</h3><p>You can also set an out-point for an input file, therefore shortening it. There are two options for this:</p><ul><li><strong>-t</strong>: This sets the duration.</li><li><strong>-to</strong>: This sets the timestamp where the input video should stop.</li></ul><p>These two are mutually exclusive, and also they do the same if no -ss is specified. The value can be specified in seconds (5 or 5.2) or as a timestamp (HOURS:MM:SS.MILLISECONDS).</p><p>Let's experiment with them!</p><pre><code class="language-shell"># "Get 30 seconds of the input."
ffmpeg -y -t 30 -i bbb_sunflower_1080p_60fps_normal.mp4 first_30_seconds.mp4
ffmpeg -y -t 00:00:30.0 -i bbb_sunflower_1080p_60fps_normal.mp4 first_30_seconds.mp4

# "Get everything until the content's 30th second." 
ffmpeg -y -to 30 -i bbb_sunflower_1080p_60fps_normal.mp4 first_30_seconds.mp4
ffmpeg -y -to 00:00:30.0 -i bbb_sunflower_1080p_60fps_normal.mp4 first_30_seconds.mp4</code></pre><p>All four above commands result in exactly the same video. (For nerds: even the md5sum is the same.)</p><p>But let's see how they perform when we introduce seeking!</p><pre><code class="language-shell"># "Seek to the 10th second and get me 30 seconds of the input."
ffmpeg -y -ss 10 -t 30 -i bbb_sunflower_1080p_60fps_normal.mp4 part_between_10_and_40.mp4

# "Seek to the 10th second and get the content until the 30th second."
ffmpeg -y -ss 10 -to 30 -i bbb_sunflower_1080p_60fps_normal.mp4 part_between_10_and_30.mp4</code></pre><p>The first command will result in a 30 second long video, while the second command will be 20 seconds long only!</p><p>The figure below shows the difference:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-13-trimming.png" class="kg-image" alt="" loading="lazy" width="2554" height="665"></figure><h3 id="editing-without-reencoding">Editing without reencoding</h3><p>FFmpeg can do something I'm not aware of in any other popular NLE: it can edit videos without reencoding them!</p><p>The usual <a href="#ffmpeg-concepts">workflow</a> is to decode the data frames (a/v) into memory, modify them as much as we like and then encode them into a new video file. The problem with this is that unless you work with raw or lossless codecs, you'll lose some quality in the process. Another issue with this approach is that it is computationally intensive.</p><p>For certain operations, you can configure FFmpeg, to keep the data frames intact, and this way, you can avoid decoding and encoding them! This is incredibly faster than regular transcoding, usually hundreds of times faster.</p><p>The "certain operations" are those that don't need to modify the data frames themselves. For example, you can cut and trim this way. Also, you can manipulate streams while keeping others, like you can replace the audio track without touching the video frames.</p><p>All this is a bit of magic, and there are caveats you need to prepare for, but it is good if you know about this, as it is often handy!</p><p>The trick lies in two options:</p><ul><li><strong>-c:v copy</strong>: The "copy" video codec</li><li><strong>-c:a copy</strong>: The "copy" audio codec</li></ul><p>Let's see a few examples!</p><h4 id="remove-audio-while-keeping-the-video-without-reencoding">Remove audio while keeping the video without reencoding</h4><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -c:v copy -an copied_video_only.mp4</code></pre><p>Here, we used the "<strong>-an</strong>" option, which removes all audio streams. I remembered it as "<strong>a</strong>udio <strong>n</strong>o", but that is just my mnemonic:)</p><p>Let's see how fast it was:</p><pre><code class="language-plaintext">frame=38072 fps=20950 q=-1.0 Lsize=  310340kB time=00:10:34.51 bitrate=4006.7kbits/s speed= 349x</code></pre><p>So It processed the whole 10 minutes of video in 2 seconds, 349x faster than playback, with 20950 fps!</p><h4 id="remove-video-while-keeping-the-audio-without-reencoding">Remove video while keeping the audio without reencoding</h4><pre><code class="language-shell">ffmpeg -i bbb_sunflower_1080p_60fps_normal.mp4 -c:a copy -vn copied_audio_only.wav</code></pre><p>Here, we used the "<strong>-vn</strong>" option, which removes all video streams. I remembered it as "<strong>v</strong>ideo <strong>n</strong>o".</p><p>Let's see how fast it was:</p><pre><code class="language-plaintext">size=   24772kB time=00:10:34.14 bitrate= 320.0kbits/s speed= 776x </code></pre><p>776x faster than playback, finished in about a second, not bad!</p><h4 id="cut-and-trim-without-reencoding">Cut and trim without reencoding</h4><pre><code class="language-shell">ffmpeg -ss 10 -t 10  -i bbb_sunflower_1080p_60fps_normal.mp4 -c:a copy -c:v copy part_from_10_to_20_copied.mp4</code></pre><p>There could be precision issues with seeking while you do this, so you may want to learn more about seeking and copying <a href="https://trac.ffmpeg.org/wiki/Seeking?ref=img.ly" rel="nofollow noreferrer noopener">here</a>.</p><h4 id="replace-audio-on-video-file-without-reencoding">Replace audio on video file without reencoding</h4><p>We have removed audio and video already, but what if we want to swap them?</p><pre><code class="language-shell">ffmpeg -y \
-i bbb_sunflower_1080p_60fps_normal.mp4 \
-i voice_recording.wav \
-map "0:v" -map "1:a" \
-c:v copy -c:a copy \
bbb_with_replaced_audio.mov</code></pre><p>There is quite a lot going on in here, so let's explain the parts!</p><p>First, we have two inputs (<strong>-i</strong>), meaning we are better off manually specifying the <a href="#mapping">mapping</a>. The command would work without the "<strong>-map</strong>" options, but it would ignore our second input.</p><p><code>-map "0:v" -map "1:a"</code> means that please use the first file's (first) video stream and the second file's (first) audio stream.</p><p>With <code>-c:v copy -c:a copy</code>, we require FFmpeg to copy the already encoded data packets without touching them. Therefore FFmpeg's work is mostly really just copying bytes, no decoding, no encoding.</p><p>Not surprisingly, that's what we see in the stream mapping too:</p><pre><code class="language-plaintext">Stream mapping:
  Stream #0:0 -&gt; #0:0 (copy)
  Stream #1:0 -&gt; #0:1 (copy)
Press [q] to stop, [?] for help
frame=38072 fps=9750 q=-1.0 Lsize=  320645kB time=00:10:34.51 bitrate=4139.7kbits/s speed= 162x  </code></pre><p>And since it is just copying, it was crazy fast, 162x of the playback speed, or almost 10k frames per second!</p><p>But!</p><p>Execute the exact same command, but with "bbb_with_replaced_audio.<strong>mp4</strong>" (.mp4 container instead of .mov) as an output file! You'll get this:</p><pre><code class="language-plaintext">Could not find tag for codec pcm_s16le in stream #1, codec not currently supported in container</code></pre><p>The message is quite clear. You can not have a pcm_s16le (raw WAV, say that 10 times:)) stream in an MP4 container. I'm not sure if it is FFmpeg's or the container's lack of support, but we need to solve this. If you run into this situation, you might consider two solutions:</p><ol><li>Change the container: I've just tried MOV, and it worked.</li><li>Encode the audio: We still copy the video data, and encoding audio isn't that painful.</li></ol><p>I just showed you option #1, so let's see option #2:</p><pre><code class="language-shell">ffmpeg -y \
-i bbb_sunflower_1080p_60fps_normal.mp4 \
-i voice_recording.wav \
-map "0:v" -map "1:a" \
-c:v copy \
-c:a aac -b:a 320k -ar 44100 \
bbb_with_replaced_audio_aac.mp4</code></pre><p>This copies the video frames and encodes our WAV into a supported codec to be held in the mp4 container. You can refer back to the <a href="#how-to-transcode-audio-with-ffmpeg">audio encoding</a> section if you want to learn more about that.</p><p>Here is the output:</p><pre><code class="language-plaintext">Stream mapping:
  Stream #0:0 -&gt; #0:0 (copy)
  Stream #1:0 -&gt; #0:1 (pcm_s16le (native) -&gt; aac (native))
Press [q] to stop, [?] for help
...
frame=38072 fps=2176 q=-1.0 Lsize=  313058kB time=00:10:34.51 bitrate=4041.8kbits/s speed=36.3x </code></pre><p>"Only" 36x faster than playback, 2176 fps, still not that bad!</p><h2 id="filtering-overview">Filtering overview</h2><p>FFmpeg supports many audio and video <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly" rel="nofollow noreferrer noopener">filters</a>. Currently, there are 116 audio and 286 video filters, but there are a bit more if we count the hardware accelerated ones too.</p><p>So how do we leverage them?</p><p>There are two ways to define filters, but I'm going to explain the complex filter, as the difference is not much, but it is more versatile. So there is a global option for FFmpeg, called: <strong><code>-filter_complex</code></strong>. With quite a weird syntax, you can specify all your filters and their parameters right after this option.</p><p>You can imagine the process with the following image:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-14-complex_filter_intro.png" class="kg-image" alt="" loading="lazy" width="1352" height="512"></figure><p>Basically, your filter graph can access all the inputs (-i a.mp4 -i b.mp4 -i c.mp4), and it can produce as many outputs as you like (-map might be needed).</p><h3 id="basic-syntax">Basic syntax</h3><p>Let's take a look at a simple, basic example:</p><pre><code class="language-shell">ffmpeg -y  -t 5 \
-i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='HELLO THERE':y=20:x=30:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex1.mp4</code></pre><p>Although <code>-filter_complex</code> is a global option, I like to put it after the inputs and before the outputs as it is a bit easier to overlook the whole command that way. Thankfully the command line parser of FFmpeg is smart enough, and it works.</p><p>The command above produces a 5-second-long video, where the text "HELLO THERE" is overlaid on the intro of Big Buck Bunny.</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-15-hello-there.png" class="kg-image" alt="" loading="lazy" width="1397" height="912"></figure><p>Let's understand the weird format for specifying filters!</p><p>We'll go bottom-up, and we'll build it from there. So the most basic format is this:</p><pre><code class="language-plaintext">FILTER_NAME=ARGUMENT1=VALUE1:ARGUMENT2=VALUE2</code></pre><p>For example:</p><pre><code class="language-plaintext">drawtext=text='HELLO THERE':y=20:x=30</code></pre><p>The first thing before the first equal (=) sign is the filter's name, which is the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#drawtext-1" rel="nofollow noreferrer noopener">drawtext</a> filter in this case. Then we have our first argument, "text" and its value "'HELLO THERE'". Right after that, separated with a colon (:) comes the next argument, "y" with a value of "20".</p><p>You can guess what each of the text, y, x, fontsize and fontfile arguments do, as it is quite self-explaining. But especially for the first time, you'll heavily rely on the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly" rel="nofollow noreferrer noopener">filtering documentation</a> to understand every filter and every argument.</p><p>Also, several characters are reserved, such as: <code>, : =</code> and a few others depending on your environment, so sooner or later you need to learn about <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#toc-Notes-on-filtergraph-escaping" rel="nofollow noreferrer noopener">escaping</a> too.</p><p>To recap, our pipeline looks like this now:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-16-complex_filter_multi.png" class="kg-image" alt="" loading="lazy" width="2384" height="594"></figure><h3 id="multiple-filters-in-a-chain">Multiple filters in a chain</h3><p>This previous command is a single filter chain that consists of a single filter only, but you could have more filters put right after each other! It means that the output of one filter will be the input for the next! The way to do this is by separating them with a comma!</p><p>Let's draw two boxes with the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#drawbox" rel="nofollow noreferrer noopener">drawbox</a> filter!</p><pre><code class="language-shell">ffmpeg -y  -t 5 \
-i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "  drawbox=x=10:y=10:w=100:h=100:color=red  ,  drawbox=x=200:y=200:w=100:h=100:color=blue  " \
filter_complex2.mp4</code></pre><p>See? The output of the first filter is passed to the output of the second filter!</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-17-filter-bick-buck.png" class="kg-image" alt="" loading="lazy" width="1596" height="1044"></figure><p>Let's visualize our pipeline again:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-18-complex_filter_multi_2.png" class="kg-image" alt="" loading="lazy" width="2384" height="594"></figure><h3 id="input-and-output-pads">Input and output pads</h3><p>Now, we have skipped something this far, because for simple uses FFmpeg is smart enough to do it for us. And this is the specification of a chain's input and output pads!</p><p>Let's draw just a single rectangle for now:</p><pre><code class="language-shell">ffmpeg -y  -t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 -filter_complex "drawbox=x=10:y=10:w=100:h=100:color=red" filter_complex3.mp4</code></pre><p>FFmpeg sees that the input for our filter chain is a single video file, and the output is a single output video file. Therefore, it safely assumes that we want that single input as the input of our single filter chain. And that single output should be the single output of our single output chain.</p><p>That's really nice, as, in simple situations like this, we don't need to assign and map inputs and outputs manually! But when we get more inputs, filter chains, or outputs, it is no longer possible. Therefore, we need to understand how to assign inputs and outputs!</p><p>First of all, let's compare the following two command lines. They result in exactly the same result, but the second one represents what FFmpeg does internally (roughly):</p><pre><code class="language-shell">ffmpeg -y  -t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 -filter_complex "drawbox=x=10:y=10:w=100:h=100:color=red" filter_complex3.mp4

ffmpeg -y  -t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 -filter_complex "[0:v]drawbox=x=10:y=10:w=100:h=100:color=red[out_link_0]" -map "[out_link_0]" filter_complex3.mp4</code></pre><p>Do you see the difference? Before our filter chain, an "input pad" is defined: <code>[0:v]</code>. The expected format between the square brackets is documented in the <a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly#Stream-selection" rel="nofollow noreferrer noopener">stream selection</a> section of the official documentation, and this article already <a href="#mapping" rel="nofollow noreferrer noopener">covered</a> it.</p><p>But, a quick summary:</p><ul><li><strong>0:v</strong>: This means the first video stream of the first input file.</li><li><strong>0:v:0</strong>: Means exactly the same thing but in a long form.</li><li><strong>0:0</strong>: Means the first stream of the first input file (not recommended, as it could be anything in theory. It could be a subtitle stream, a thumbnail, a video or an audio stream...)</li><li><strong>0:a</strong>: This means the first audio stream of the first input file.</li><li><strong>0:a:0</strong>: Means exactly the same thing but in a long form.</li><li><strong>0:a:1</strong>: Means the second (index #1) audio stream of the first input file.</li></ul><p>So we can specify which input file should be connected to which input of the filter graph!</p><p>Also, something similar is going on at the end! Do you see, the <code>[out_link_0]</code> output pad definition at the end of our filter chain?</p><p>The naming here is easier, as basically you can specify any arbitrary name in here. It roughly means, "please store the output data under this name".</p><p>And when you specify your output file, you can or need to map it by selecting one of your filter graph outputs! Therefore, we must add the -map "[out_link_0]" option before our output file.</p><p>This map option means this: "Please save the data stream with this name into the following output file."</p><p>This is how you can visualize this input/output mapping:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-19-complex_filter_multi_3.png" class="kg-image" alt="" loading="lazy" width="2590" height="724"></figure><h3 id="multiple-chains">Multiple chains</h3><p>Coming from the previous sections, you are now ready to see and understand an even more complicated configuration, which has multiple input files, output files, and filter chains!</p><pre><code class="language-shell">ffmpeg -y  \
-i train.jpg \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "[0:v]drawbox=x=10:y=10:w=100:h=100:color=red[train_box] ; [1:v]drawbox=x=10:y=10:w=100:h=100:color=red[bbb_box]" \
-map "[train_box]" filter_complex4_train.jpg \
-map "[bbb_box]" filter_complex4_bbb.mp4</code></pre><p>Let's see the output (two files next to each other):</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-20-filters_output_3.png" class="kg-image" alt="" loading="lazy" width="1470" height="656"></figure><p>We had two inputs, and we got two output files, an image, and a video, with a red rectangle on them, with a single command!</p><p>Are you still here? I hope! Let's understand what happened in that crazy command! We have two input files:</p><ul><li><strong>-i train.jpg</strong>: A simple image file</li><li><strong>-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4</strong>: Our video file, but to make it quick, just the first five seconds of it</li></ul><p>Then the first thing to note is that we have two filter chains! They are separated with a "<strong>;</strong>".</p><p>Our first filter graph is this: <code>[0:v]...[train_box]</code></p><ul><li>This requests the first input file as an input</li><li>Draws a red box</li><li>Saves the output into the "train_box" output pad</li></ul><p>Our second filter graph is this: <code>[1:v]...[bbb_box]</code></p><ul><li>This requests the second input file as an input</li><li>Draws a red box</li><li>Saves the output into the "bbb_box" output pad</li></ul><p>And finally, we got two outputs, each mapping to one of the outputs of the filter graph:</p><ul><li><strong>-map "[train_box]" filter_complex4_train.jpg</strong></li><li><strong>-map "[bbb_box]" filter_complex4_bbb.mp4</strong></li></ul><p>Here is the same thing visually:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-21-complex_filter_multi_4.png" class="kg-image" alt="" loading="lazy" width="2898" height="988"></figure><p>If you are thinking about making it even more complex and making filter graphs that combine multiple inputs into one for example, you are on the right track! It is possible, and we will get to that!</p><p>This was the introduction to the filtering system and its syntax.</p><h2 id="editing-video">Editing video</h2><p>Now let's get to know a few filters and make some interesting stuff!</p><h3 id="resizing-or-scaling">Resizing or scaling</h3><p>The <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scale" rel="nofollow noreferrer noopener">scale</a> filter is a simple one, yet it is quite powerful!</p><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "scale=width=600:height=-1:force_original_aspect_ratio=decrease" \
filter_complex5_scaled1.mp4</code></pre><p>The arguments speak for themselves, but a few things:</p><ul><li>Specifying -1 to either width or height means rescaling while keeping the aspect ratio.</li><li>"force_original_aspect_ratio" can be <code>increase</code>, <code>decrease</code>. Meaning it will increase or decrease the image to fit the specified bounding box while keeping the aspect ratio.</li></ul><h3 id="adding-text">Adding text</h3><p>We have already covered this a little, so let's dive deeper!</p><p>This is what we used earlier:</p><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='HELLO THERE':y=20:x=30:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex1.mp4</code></pre><p>Now let's discover how to align the text!</p><p>Many filters, including drawtext, support variables in some of its argument's values. If you scroll down in the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#drawtext-1" rel="nofollow noreferrer noopener">documentation of drawtext</a>, you'll find this:</p><blockquote>"The parameters for x and y are expressions containing the following constants and functions: "</blockquote><p>And after this part, you'll see many variables which you can include in your x and y variables!</p><p>Let's see:</p><pre><code class="language-shell"># Align the text to the center
ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='HELLO THERE':y=h/2-text_h/2:x=w/2-text_w/2:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex6_center.mp4
# y=h/2-text_h/2 means: y position = (image height / 2) - (text height / 2)

# Align the text to the right:
ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='HELLO THERE':y=30:x=w-text_w-20:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex6_right.mp4
# x=w-text_w-20 means: x position = image width - text width - 20pixel padding


# Align the text to the bottom:
ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='HELLO THERE':y=h-text_h-20:x=30:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex6_bottom.mp4
# y=h-text_h-20 means: y position = image height - text height - 20pixel padding</code></pre><p>And this is what we'll get in the end:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-22-filters_output_4.png" class="kg-image" alt="" loading="lazy" width="1802" height="1043"></figure><p>I need to mention one good trick that might not be obvious at first. So the <code>text_h</code> variable is a tricky one, because different text will be of different height! E.g.: "____" and "WWW"  will result in a different height.</p><p>For this reason, you do not always want to use text_h or even just a constant y=value expression but rather, you need to align text by its <a href="https://en.wikipedia.org/wiki/Baseline_(typography)?ref=img.ly" rel="nofollow noreferrer noopener"><strong>baseline</strong></a>. So just remember to use the "<strong>ascent</strong>" variable whenever you need to align text vertically!</p><p>Check out these two examples! Each has two drawtext filters printing "_" and "_H":</p><pre><code class="language-shell"># This one uses y=200 for both, still the text isn't aligned properly!
ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='_':y=200:x=30:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf,drawtext=text='_H':y=200:x=500:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex7_bad_text.mp4

# This one uses y=200-ascent for both and the text is aligned as expected!
ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-filter_complex "drawtext=text='_':y=200-ascent:x=30:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf,drawtext=text='_H':y=200-ascent:x=500:fontsize=200:fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf" \
filter_complex7_good_text.mp4
</code></pre><p>Now let's compare the difference:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-23-filters_output_4_textalign.png" class="kg-image" alt="" loading="lazy" width="1771" height="525"></figure><p>See? This is the difference between aligning the "top left" or the "baseline" of the text!</p><h3 id="adding-an-overlay">Adding an overlay</h3><p>Overlaying is a very interesting thing to do with FFmpeg. Let's jump right in!</p><h4 id="basic">Basic</h4><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-i smiley.png \
-filter_complex "overlay" \
filter_complex8_overlay1.mp4</code></pre><p>Easy as that!</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-24-overlay_1.png" class="kg-image" alt="" loading="lazy" width="1497" height="980"></figure><p>Of course, the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#overlay" rel="nofollow noreferrer noopener">overlay</a> filter has a ton of options, but I wanted to demonstrate the easiest possible command line. We don't even need to mess with input/output pads, as FFmpeg automatically understands the situation: two inputs for the overlay filter and its single output into a single output.</p><p>But just to exercise, we could have executed it like this:</p><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-i smiley.png \
-filter_complex "[0:v][1:v]overlay[output]" \
-map "[output]" filter_complex8_overlay2.mp4</code></pre><p>And this would result in the same output! Check it out, now I have specified the two inputs for the overlay: <code>[0:v][1:v]</code>!</p><h4 id="aligned">Aligned</h4><p>Let's align the smiley into the center!</p><p>As we have seen with the drawtext, the overlay filter's arguments also support a few dynamic variables. We'll use those to achieve what we want!</p><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-i smiley.png \
-filter_complex "overlay=x=main_w/2-overlay_w/2:y=main_h/2-overlay_h/2" \
filter_complex8_overlay3.mp4</code></pre><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-25-overlay_2.png" class="kg-image" alt="" loading="lazy" width="869" height="627"></figure><h4 id="preprocessing-the-input-for-overlay">Preprocessing the input for overlay</h4><p>Let's get a bit creative!</p><p>I want to make it <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scale" rel="nofollow noreferrer noopener">smaller</a>, and I also want to <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scale" rel="nofollow noreferrer noopener">blur</a> it!</p><p>Now pause for a minute, and think about it, how you'd do that?!</p><p>...</p><p>Ready?</p><pre><code class="language-shell">ffmpeg -y  \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-i smiley.png \
-filter_complex "[1:v]scale=w=200:h=-1,gblur=sigma=3[smiley] ; [0:v][smiley]overlay=x=100:y=100" \
filter_complex8_overlay4.mp4</code></pre><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-26-overlay_3.png" class="kg-image" alt="" loading="lazy" width="996" height="703"></figure><p>For this we needed to have two filter graphs!</p><p>The first one is this: <code>[1:v]scale=w=200:h=-1,gblur=sigma=3[smiley]</code></p><ul><li>Scales the input image (the smiley).</li><li>Then the scaled output is also blurred.</li><li>Then the output is saved into the output pad named "smiley".</li></ul><p>Then, we have our second filter graph: <code>[0:v][smiley]overlay=x=100:y=100</code></p><ul><li>This takes as input the first input file (the video).</li><li>This also takes as input the output pad named "smiley". (We are connecting two chains this time!)</li><li>Then the overlay filter does its overlaying thing, and we trust FFmpeg to pair the unnamed output with the single output file we specified.</li></ul><h4 id="reusing-content">Reusing content</h4><p>Let's do one more, a really complicated one!</p><p>Let's have the outro overlaid over the intro!</p><pre><code class="language-shell">ffmpeg -y \
-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-t 5 -ss 00:09:40 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-filter_complex " [1:v]scale=w=1920/2:h=-1[outro]; [0:v][outro]overlay" \
filter_complex8_overlay5.mp4</code></pre><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-27-overlay_4.png" class="kg-image" alt="" loading="lazy" width="1170" height="794"></figure><p>We could have achieved it in several ways, e.g. we could use the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#trim" rel="nofollow noreferrer noopener">trim</a> filter, but to keep it easy, we just open the same file twice and <a href="#cutting-off-from-the-beginning-of-the-clip" rel="nofollow noreferrer noopener">seek/trim</a> them.</p><ul><li><strong>-t 5 -i bbb_sunflower_1080p_60fps_normal.mp4</strong>: Open the video, and keep the first five seconds of it.</li><li><strong>-t 5 -ss 00:09:40 -i bbb_sunflower_1080p_60fps_normal.mp4</strong>: Open the same video again, but seek to the end and keep five seconds from there.</li></ul><p>Then we have two filter graphs again, one scales down the outro, and the second is just an overlay.</p><p>Are you excited?:) I hope these made-up examples opened up your eye for the possibilities, and I hope you'll create very creative stuff with this knowledge!</p><h3 id="chroma-keying-green-screen-blue-screen">Chroma keying, green screen, blue screen</h3><p>In this section, we'll use chroma keying to remove the background from Big Buck Bunny's intro, and then we will put the transparent logo over the original video, as if it would be some kind of a logo overlay!</p><pre><code class="language-shell">ffmpeg -y \
-ss 0.5 -t 2 -i bbb_sunflower_1080p_60fps_normal.mp4 \
-ss 10 -i bbb_sunflower_1080p_60fps_normal.mp4  \
-filter_complex " [0:v]chromakey=color=0xfdfdfd:similarity=0.1:blend=0.2 , scale=w=-1:h=300 , loop=loop=-1:start=0:size=120[intro] ; [1:v][intro]overlay=x=-40:y=-40" \
-t 10 filter_complex9.mp4</code></pre><p>So just to recap, Big Buck Bunny's first few seconds are like this:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-28-chroma_basic.png" class="kg-image" alt="" loading="lazy" width="854" height="614"></figure><p>And this is the result:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-29-chroma1.png" class="kg-image" alt="" loading="lazy" width="1114" height="764"></figure><p>Also, the butterfly moves its wings repeatedly!</p><p>Let's examine the command!</p><ul><li><strong>-ss 0.5 -t 2 -i bbb_sunflower_1080p_60fps_normal.mp4</strong>: We read in the intro from 0.5 to 2.5 seconds.</li><li><strong>-ss 10 -i bbb_sunflower_1080p_60fps_normal.mp4</strong>: We read in the video, starting from the 10th second.</li></ul><p>Then we have two filter graphs, the first being this:</p><p><code>[0:v]chromakey=color=0xfdfdfd:similarity=0.1:blend=0.2 , scale=w=-1:h=300 , loop=loop=-1:start=0:size=120[intro]</code></p><p>As we see, we have three filters in here!</p><ul><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#chromakey" rel="nofollow noreferrer noopener"><strong>chromakey</strong></a>: This one takes a color and a few parameters as input, and outputs transparent frames. The specified color + the blended areas will be the transparent sections. In our case we replaced the white-ish (#fdfdfd) background color with transparency.</li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scale" rel="nofollow noreferrer noopener"><strong>scale</strong></a>: We resize the full 1080p image into something around 300px high.</li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#loop" rel="nofollow noreferrer noopener"><strong>loop</strong></a>: With the loop filter, we repeat all the 2 seconds worth of 120 frames (60*2) over and over again, to have the butterfly move its wings continuously.</li></ul><p>And then, finally we have the second filter graph:</p><p><code>[1:v][intro]overlay=x=-40:y=-40</code></p><p>Nothing fancy, just an overlay of the original video and our chrome keyed intro.</p><h3 id="what-else">What else?</h3><p>You might want to check out a few more <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#toc-Video-Filters" rel="nofollow noreferrer noopener">filters</a>, that I didn't cover here.</p><p>Here are just a few interesting ones:</p><ul><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#colorcorrect" rel="nofollow noreferrer noopener">colorcorrect</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#colorchannelmixer" rel="nofollow noreferrer noopener">colorchannelmixer</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#colorize" rel="nofollow noreferrer noopener">colorize</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#fps" rel="nofollow noreferrer noopener">fps</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#trim" rel="nofollow noreferrer noopener">trim</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#crop" rel="nofollow noreferrer noopener">crop</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#delogo" rel="nofollow noreferrer noopener">delogo</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#derain" rel="nofollow noreferrer noopener">derain</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#deshake" rel="nofollow noreferrer noopener">deshake</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#erosion" rel="nofollow noreferrer noopener">erosion</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#edgedetect" rel="nofollow noreferrer noopener">edgedetect</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#hflip" rel="nofollow noreferrer noopener">hflip</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#vflip" rel="nofollow noreferrer noopener">vflip</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#hstack" rel="nofollow noreferrer noopener">hstack</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#vstack" rel="nofollow noreferrer noopener">vstack</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#xstack" rel="nofollow noreferrer noopener">xstack</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#lumakey" rel="nofollow noreferrer noopener">lumakey</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#reverse" rel="nofollow noreferrer noopener">reverse</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#rotate" rel="nofollow noreferrer noopener">rotate</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#scroll" rel="nofollow noreferrer noopener">scroll</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#pad" rel="nofollow noreferrer noopener">pad</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#vignette" rel="nofollow noreferrer noopener">vignette</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#zoompan" rel="nofollow noreferrer noopener">zoompan</a></li></ul><h2 id="audio-manipulation">Audio manipulation</h2><p>In this chapter, we'll be going to check out some <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#toc-Audio-Filters" rel="nofollow noreferrer noopener">audio manipulation techniques</a> with FFmpeg!</p><p>First of all, let's see our <a href="#example-material">example</a> file:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-30-voice_recording.png" class="kg-image" alt="" loading="lazy" width="1920" height="400"></figure><p>It is a voice recording, and it is intentionally... well, quite bad.</p><p>From the waveform, it is obvious that there are very different volume ranges in it. This is an example recording where each sentence was read in different strengths: "normal", "whisper" or "powerful", this is why you see repeating patterns of amplitude ranges on the image.</p><p>It isn't visible, but it has some noise too, and of course, it is not normalized or enhanced in any way. Yet.</p><p>Please note that there are different scenarios, requirements, and ways to enhance audio. This is a simplified method to show the outline of the process in this article. I'm not an audio engineer, although I have some experience in the area. So if you know it better, feel free to fine-tune it for yourself even more, or contact me and recommend improvements!</p><p>I'm showing an example here with a very rough input, one that you'd just reject in real life as it would be useless due to its quality. But it is an excellent example to show the different steps of the enhancing process and to see what can be done to it!</p><p>The following steps are built upon each other, and we'll reach the complete command at the <a href="#putting-it-all-together">end</a>!</p><p>Don't forget that these settings are specific to this voice recording. Sadly this can not be generalized too much.</p><h3 id="gate">Gate</h3><p>Let's start with the <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#agate" rel="nofollow noreferrer noopener">gate</a> filter!</p><p>A gate is like a switch that opens only if the signal is stronger than the threshold. So if the signal level is lower than the threshold, it cuts to complete silence. Although you might soften or delay this cut with the <em>knee</em>, <em>attack</em>, and <em>release</em> arguments.</p><p>We'll use this filter as a basic noise reduction method now! This helps us remove the noise between words and sentences by cutting it to silence. It doesn't remove noise in any other way, e.g. it doesn't touch the static on the voice itself.</p><p>Check this out!</p><pre><code class="language-shell">ffmpeg -y \
-i voice_recording.wav \
-filter_complex "agate=threshold=0.01:attack=80:release=840:makeup=1:ratio=3:knee=8" \
gate.wav</code></pre><p>Let's hear it: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-5-gate.wav?ref=img.ly">gate.wav</a></p><p>And let's see it:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-31-a_compression_result.png" class="kg-image" alt="" loading="lazy" width="655" height="599"></figure><p>As you can see, the "silent" parts were attenuated heavily, while the above-the-threshold parts remained similar. Those parts were still affected by the knee, attack, and release arguments determining how hard (knee) and quick (attack/release) the cut is.</p><p>I've left a quite high release timeout here to avoid sudden dips in the amplitude.</p><p>This is where we are right now:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-32-gate.png" class="kg-image" alt="" loading="lazy" width="1920" height="400"></figure><p>The silent parts are more silent than before, but still, the amplitude range or the dynamic range is quite high. You must change your volume levels to hear everything and void blowing your speakers/brain out.</p><h3 id="equalization">Equalization</h3><p>Before fixing that, let's do a bit more housekeeping. Let's do some equalization and frequency filtering!</p><p>We'll use these filters:</p><ul><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#highpass" rel="nofollow noreferrer noopener">highpass</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#lowpass" rel="nofollow noreferrer noopener">lowpass</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#anequalizer" rel="nofollow noreferrer noopener">anequalizer</a></li></ul><pre><code class="language-shell">ffmpeg -y \
-i gate.wav  \
-filter_complex "highpass=f=100:width_type=q:width=0.5 , lowpass=f=10000 , anequalizer=c0 f=250 w=100 g=2 t=1|c0 f=700 w=500 g=-5 t=1|c0 f=2000 w=1000 g=2 t=1" \
gate_eq.wav</code></pre><p>Let's hear it: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-5-gate.wav?ref=img.ly">gate_eq.wav</a></p><p>This command gradually attenuates frequencies below 100hz, as there are not much valuable content in there, but it can really lower the clarity of the speech.</p><p>Then we do the same, but for frequencies above 10 kHz. This is mostly needed because we have a lot of high-frequency noise, so this is a workaround for those. Also, a male voice is generally deeper than a woman's, so you might want to pay attention to how low you can put the bar.</p><p>Then comes anequalizer, which has a crazy an exceptional way of setting its arguments:</p><p>This: <code>anequalizer=c0 f=250 w=100 g=2 t=1|c0 f=700 w=500 g=-5 t=1|c0 f=2000 w=1000 g=2 t=1</code> means:</p><ul><li>at 250hz with a width of 100hz boost by 2 db, with Chebyshev type 1 filter on channel 0.</li><li>at 700hz with a width of 500hz attenuate by 5 db, with Chebyshev type 1 filter on channel 0.</li><li>at 2000hz with a width of 1000hz attenuate by 2 db, with Chebyshev type 1 filter on channel 0.</li></ul><p>I agree. You might have used a friendlier equalizer in your life than this one:)</p><p>Those values are based on experimentation and common recommendations for voice. Feel free to tune it for your own needs!</p><p>Let's compare the frequency plots before and after:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-33-a_eq.png" class="kg-image" alt="" loading="lazy" width="1463" height="386"></figure><p>Tip: To see the frequency plot in Audacity, open a file, select all, and choose Analyze → Plot spectrum!</p><h3 id="compression">Compression</h3><p>The <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#acompressor" rel="nofollow noreferrer noopener">compressor</a> filter applies <a href="https://en.wikipedia.org/wiki/Dynamic_range_compression?ref=img.ly" rel="nofollow noreferrer noopener">dynamic range compression</a> on the incoming audio data. To simplify this, the compressor varies the attenuation based on the incoming signal level. Basically, when you watch a badly mastered movie, this is what you are doing. When it is way too loud in some action scene, you reach for the remote control or mouse to lower the volume, but in the next moment, you will not hear what your heroes are saying, so you increase it back again.</p><p>Dynamic range compression roughly does the same. You may set it up in a way so that it would attenuate louder parts, therefore keeping the overall volume range relatively small.</p><p>It often happens that performers on the stage use a high dynamic range. Many performers will shout at one moment and then whisper in the next to increase drama or keep the attention. If you want to avoid manually adjusting the volume in real-time (while blowing off your speakers and pulling your hair out), then a compressor will save you in these situations!</p><p>This is why our example audio consists of different speaking strengths, so that we could see the dramatic effect of this filter.</p><pre><code class="language-shell">ffmpeg -y \
-i gate_eq.wav \
-filter_complex "acompressor=level_in=6:threshold=0.025:ratio=20:makeup=6" \
gate_eq_comp.wav</code></pre><p>Let's hear it: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-1-gate-eq-comp.wav?ref=img.ly">gate_eq_comp.wav</a></p><p>And let's compare the result of this with the original waveform!</p><p>Original:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-34-voice_recording.png" class="kg-image" alt="" loading="lazy" width="1920" height="400"></figure><p>Result:</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-35-gate_eq_comp.png" class="kg-image" alt="" loading="lazy" width="1920" height="400"></figure><p>Quite dramatic, isn't it?:)</p><p>Let's analyze this: <code>acompressor=level_in=6:threshold=0.025:ratio=20:makeup=6</code></p><p>First, <code>level_in=6</code>  sets the input gain. It is 1 by default, but since our example, audio is extremely silent at places, we boost up the whole thing before processing.</p><p>Then <code>threshold=0.025</code> defines that everything above 0.025 should be attenuated.</p><p>Based on the image below, I've decided to cut at this point, as this is above most of the whispering, which cuts hard pops and "s"-es even in the "whisper zone".</p><figure class="kg-card kg-image-card"><img src="https://blog.img.ly/2022/11/img-36-eq.png" class="kg-image" alt="" loading="lazy" width="1916" height="455"></figure><p>Then <code>ratio=20</code> means 1:20 in attenuation ratio, which means that if the level rises 20 dB above the threshold, it will be only 1 dB above the line after the attenuation. Basically, this is a very strong compression ratio, it is almost a <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#alimiter" rel="nofollow noreferrer noopener">limiter</a>.</p><p>This far, we boosted the signal, then turned down everything that was above our "whisper line" with a quite strong ratio, and now, everything is basically at the whisper level, even the parts that are shouting.</p><p>Finally, with the <code>makeup=6</code> we just bring back everything to the level where the "normal" parts were before.</p><p>Let's take a look back now, to understand why we used the gate and did the equalization before the compressor.</p><p>Generally, you want to remove unneeded parts and frequencies before compression, as the compressor will likely increase those too! So by removing most of the noise in the gaps, we avoided <code>level_in=6</code> to increase them too! And the same goes for the high- and lowpass filtering.</p><h3 id="changing-the-volume">Changing the volume</h3><p>Now, if we want to make the result a bit louder, we could increase the previous step's <code>makeup</code> argument, or leverage the volume <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#volume" rel="nofollow noreferrer noopener">filter</a>.</p><p>While we are at it, let's cut the first 4 seconds too with <code>-ss 4</code>.</p><pre><code class="language-shell">ffmpeg -y \
-ss 4 -i gate_eq_comp.wav \
-filter_complex "volume=1.1" \
gate_eq_volume_comp.wav</code></pre><p>Let's hear it: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-2-gate_eq_volume_comp.wav?ref=img.ly">gate_eq_volume_comp.wav</a></p><h3 id="lets-make-audio-gate-again">Let's make audio gate again</h3><p>Excuse me for that title:)</p><p>So as I've described earlier, compression can amplify the noises, so you might want to run the result through a gate again:</p><pre><code class="language-shell">ffmpeg -y \
-i gate_eq_volume_comp.wav \
-filter_complex "agate=threshold=0.1:attack=50:release=50:ratio=1.5:knee=4" \
gate_eq_volume_comp_gate.wav</code></pre><p>Let's hear it: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-3-gate_eq_volume_comp_gate.wav?ref=img.ly">gate_eq_volume_comp_gate.wav</a></p><p>In this case, I've used a softer gate, with <code>ratio=1.5</code>. Because of this, I could use shorter attack and release delays too, as the attenuation is not that strong, it isn't causing hard dips in the audio.</p><h3 id="putting-it-all-together">Putting it all together</h3><p>Just a single command could have achieved all the steps above:</p><pre><code class="language-shell">ffmpeg -y \
-i voice_recording.wav \
-filter_complex "agate=threshold=0.01:attack=80:release=840:makeup=1:ratio=3:knee=8 , highpass=f=100:width_type=q:width=0.5 , lowpass=f=10000 , anequalizer=c0 f=250 w=100 g=2 t=1|c0 f=700 w=500 g=-5 t=1|c0 f=2000 w=1000 g=2 t=1 , acompressor=level_in=6:threshold=0.025:ratio=20:makeup=6 , volume=1.1 , agate=threshold=0.1:attack=50:release=50:ratio=1.5:knee=4" \
gate_eq_volume_comp_gate_together.wav</code></pre><p>I just copy-pasted all the filters right after each other with a comma between them.</p><p>Isn't it beautiful? Yeah, it isn't, but it is very practical:)</p><p>For the last time, check out the difference:</p><ul><li>Original: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-4-voice_recording.wav?ref=img.ly">voice_recording.wav</a> </li><li>Final: <a href="https://storage.googleapis.com/imgly-static-assets/static/blog/ffmpeg-audio/audio-3-gate_eq_volume_comp_gate.wav?ref=img.ly">gate_eq_volume_comp_gate.wav</a></li></ul><p>It has less noise, more clear voice, and a small volume range. Therefore it is easy on your ears!</p><h3 id="what-else-1">What else?</h3><p>You might want to check out a few more <a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#toc-Audio-Filters" rel="nofollow noreferrer noopener">filters</a> that I didn't cover here.</p><p>Here are just a few interesting ones:</p><ul><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#adeclick" rel="nofollow noreferrer noopener">adeclick</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#adeclip" rel="nofollow noreferrer noopener">adeclip</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#aecho" rel="nofollow noreferrer noopener">aecho</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#deesser" rel="nofollow noreferrer noopener">deesser</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly#alimiter" rel="nofollow noreferrer noopener">alimiter</a></li></ul><h2 id="documentation">Documentation</h2><p>For your convenience, let me list the most important documentations that might be important for you! Most of these were already linked many times in this article.</p><ul><li><a href="https://ffmpeg.org/ffmpeg.html?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg main documentation</a></li><li><a href="https://trac.ffmpeg.org/wiki?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg WIKI</a></li><li><a href="https://trac.ffmpeg.org/wiki/CompilationGuide?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg compilation guide</a></li><li><a href="https://ffmpeg.org/ffmpeg-filters.html?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg filters documentation</a></li><li><a href="https://ffmpeg.org/ffmpeg-formats.html?ref=img.ly" rel="nofollow noreferrer noopener">FFmpeg formats documentation</a></li><li><a href="https://trac.ffmpeg.org/wiki/Encode/H.264?ref=img.ly" rel="nofollow noreferrer noopener">H.264 Video Encoding Guide</a></li><li><a href="https://trac.ffmpeg.org/wiki/Encode/H.265?ref=img.ly" rel="nofollow noreferrer noopener">H.265 Video Encoding Guide</a></li></ul><p>If you got this far from top to bottom, then you are a true hero! I hope you enjoyed this, and I also hope that it inspired you to create something awesome with FFmpeg! Please consider <a href="https://ffmpeg.org/donations.html?ref=img.ly" rel="nofollow noreferrer noopener">donating</a> to FFmpeg – they are fantastic.<br></p><p>If you're looking to take your creative projects to the next level, check out our products -  <a href="https://img.ly/products/creative-sdk?ref=img.ly">Creative Editor SDK</a>, <a href="https://img.ly/products/video-sdk?ref=img.ly">Video Editor SDK</a>, and <a href="https://img.ly/products/photo-sdk?ref=img.ly">Photo Editor SDK</a>. These versatile tools empower you to bring your vision to life, whether you're editing images, crafting stunning videos, or unleashing your artistic talents.</p><p><br><strong>Thanks for reading! Let us know what you think on </strong><a href="https://twitter.com/imgly?ref=img.ly"><strong>Twitter</strong></a><strong>! To stay in the loop, subscribe to our </strong><a href="https://img.us13.list-manage.com/subscribe?u=dc9f652839dbb620d14d6d28d&id=04a306e4b2&ref=img.ly"><strong>Newsletter</strong></a><strong>.</strong></p>
            </section>
        </div>
      </div>
    </div>

    <footer class="post-footer u-container u-maxWidth868">
            <div class="post-tags buttonSet u-marginTop30">
        <a href="https://img.ly/blog/tag/ffmpeg/" title="FFmpeg" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="FFmpeg" data-event-non-interaction="true">FFmpeg</a><a href="https://img.ly/blog/tag/video-app/" title="Video App" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Video App" data-event-non-interaction="true">Video App</a><a href="https://img.ly/blog/tag/audio/" title="Audio" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Audio" data-event-non-interaction="true">Audio</a><a href="https://img.ly/blog/tag/tech/" title="Tech" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Tech" data-event-non-interaction="true">Tech</a><a href="https://img.ly/blog/tag/tutorial/" title="Tutorial" class="button button--tags godo-tracking" data-event-category="Article" data-event-action="Tags" data-event-label="Tutorial" data-event-non-interaction="true">Tutorial</a>
    </div>

        <hr>
        <div class="prev-next">
                <div class="u-flex u-relative godo-tracking prev-article u-marginBottom30"
    data-event-category="Article"
    data-event-action="Previous article"
    data-event-label="https://img.ly/blog/how-to-add-stickers-and-overlays-to-a-video-in-flutter-test/"
    data-event-non-interaction="true">

    <a href="/blog/how-to-add-stickers-and-overlays-to-a-video-in-flutter-test/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="How to Apply Filters and Effects to an Image in Flutter">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2022/11/apply-filters-and-effects-to-an-image-in-Flutter.png" alt="How to Apply Filters and Effects to an Image in Flutter"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Previous article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/how-to-add-stickers-and-overlays-to-a-video-in-flutter-test/" class="u-relative zindex3">How to Apply Filters and Effects to an Image in Flutter</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Learn how to manipulate images in Flutter with filters and effects.</p>
    </div>

    <a href="/blog/how-to-add-stickers-and-overlays-to-a-video-in-flutter-test/" aria-label="How to Apply Filters and Effects to an Image in Flutter" class="u-absolute0 zindex2"></a>
</div>
                <div class="u-flex u-relative godo-tracking prev-article "
    data-event-category="Article"
    data-event-action="Next article"
    data-event-label="https://img.ly/blog/creative-editor-sdk-v_1_9_0-release-notes/"
    data-event-non-interaction="true">

    <a href="/blog/creative-editor-sdk-v_1_9_0-release-notes/" class="prev-next-image-link u-relative u-bgColorGrayLight u-flex0" aria-label="CE.SDK v1.9.0 Release">
        <img class="u-absolute u-image blur-up lazyload" data-src="https://blog.img.ly/2022/12/creative-editor-sdk-1.png" alt="CE.SDK v1.9.0 Release"/>
    </a>

    <div class="prev-next-body u-flex1">
        <div class="u-fontSizeSmaller u-textMuted u-marginBottom10">Next article</div>
        <h2 class="prev-next-title u-contentTitle u-marginBottom10 u-fontSize21"><a href="/blog/creative-editor-sdk-v_1_9_0-release-notes/" class="u-relative zindex3">CE.SDK v1.9.0 Release</a></h2>
        <p class="prev-next-excerpt u-fontSizeSmall u-textMuted u-lineClamp2 u-lineHeightTight">Get ready to take your creative applications to the next level! This release is packed with exciting new features like video support for web, and more.</p>
    </div>

    <a href="/blog/creative-editor-sdk-v_1_9_0-release-notes/" aria-label="CE.SDK v1.9.0 Release" class="u-absolute0 zindex2"></a>
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
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/building-a-production-ready-batch-video-processing-server-with-ffmpeg/" data-event-non-interaction="true">
    <a href="/blog/building-a-production-ready-batch-video-processing-server-with-ffmpeg/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/11/ffmpeg-batch-editing-processing-videos-how-to--1-.jpg"
            srcset="https://blog.img.ly/2025/11/ffmpeg-batch-editing-processing-videos-how-to--1-.jpg"
            data-srcset="https://blog.img.ly/2025/11/ffmpeg-batch-editing-processing-videos-how-to--1-.jpg 300w,https://blog.img.ly/2025/11/ffmpeg-batch-editing-processing-videos-how-to--1-.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="A Guide to Batch Video Editing &amp; Server Automation with FFmpeg"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/building-a-production-ready-batch-video-processing-server-with-ffmpeg/">A Guide to Batch Video Editing &amp; Server Automation with FFmpeg</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-11-10">10 Nov 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="10 min read">10 min read</span>
    
</div>    </div>

    <a href="/blog/building-a-production-ready-batch-video-processing-server-with-ffmpeg/" class="u-absolute0 zindex3" aria-label="A Guide to Batch Video Editing &amp; Server Automation with FFmpeg"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/how-to-run-ffmpeg-inside-a-docker-container/" data-event-non-interaction="true">
    <a href="/blog/how-to-run-ffmpeg-inside-a-docker-container/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/10/ffmpeg-docker-container-how-to.jpg"
            srcset="https://blog.img.ly/2025/10/ffmpeg-docker-container-how-to.jpg"
            data-srcset="https://blog.img.ly/2025/10/ffmpeg-docker-container-how-to.jpg 300w,https://blog.img.ly/2025/10/ffmpeg-docker-container-how-to.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="How to run FFmpeg inside a Docker container"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/how-to-run-ffmpeg-inside-a-docker-container/">How to run FFmpeg inside a Docker container</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-10-29">29 Oct 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="6 min read">6 min read</span>
    
</div>    </div>

    <a href="/blog/how-to-run-ffmpeg-inside-a-docker-container/" class="u-absolute0 zindex3" aria-label="How to run FFmpeg inside a Docker container"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/ffmpeg-on-google-cloud-platform-guide/" data-event-non-interaction="true">
    <a href="/blog/ffmpeg-on-google-cloud-platform-guide/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/10/ffmpeg-GCP-tutorial-1.jpg"
            srcset="https://blog.img.ly/2025/10/ffmpeg-GCP-tutorial-1.jpg"
            data-srcset="https://blog.img.ly/2025/10/ffmpeg-GCP-tutorial-1.jpg 300w,https://blog.img.ly/2025/10/ffmpeg-GCP-tutorial-1.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="FFmpeg on GCP: Step-by-Step for Beginners"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/ffmpeg-on-google-cloud-platform-guide/">FFmpeg on GCP: Step-by-Step for Beginners</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-10-08">8 Oct 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="8 min read">8 min read</span>
    
</div>    </div>

    <a href="/blog/ffmpeg-on-google-cloud-platform-guide/" class="u-absolute0 zindex3" aria-label="FFmpeg on GCP: Step-by-Step for Beginners"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/how-to-run-ffmpeg-on-aws-spot-instances-for-scalable-low-cost-video-processing/" data-event-non-interaction="true">
    <a href="/blog/how-to-run-ffmpeg-on-aws-spot-instances-for-scalable-low-cost-video-processing/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2025/10/ffmpeg-awe.jpg"
            srcset="https://blog.img.ly/2025/10/ffmpeg-awe.jpg"
            data-srcset="https://blog.img.ly/2025/10/ffmpeg-awe.jpg 300w,https://blog.img.ly/2025/10/ffmpeg-awe.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="How to Run FFmpeg on AWS Spot Instances for Scalable, Low-Cost Video Processing"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/how-to-run-ffmpeg-on-aws-spot-instances-for-scalable-low-cost-video-processing/">How to Run FFmpeg on AWS Spot Instances for Scalable, Low-Cost Video Processing</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2025-10-06">6 Oct 2025</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="10 min read">10 min read</span>
    
</div>    </div>

    <a href="/blog/how-to-run-ffmpeg-on-aws-spot-instances-for-scalable-low-cost-video-processing/" class="u-absolute0 zindex3" aria-label="How to Run FFmpeg on AWS Spot Instances for Scalable, Low-Cost Video Processing"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/a-modern-video-editor-sdk-for-your-flutter-app/" data-event-non-interaction="true">
    <a href="/blog/a-modern-video-editor-sdk-for-your-flutter-app/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2024/09/how-to-flutter-photo-video-design-editor-sdk.png"
            srcset="https://blog.img.ly/2024/09/how-to-flutter-photo-video-design-editor-sdk.png"
            data-srcset="https://blog.img.ly/2024/09/how-to-flutter-photo-video-design-editor-sdk.png 300w,https://blog.img.ly/2024/09/how-to-flutter-photo-video-design-editor-sdk.png 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="A Modern Video Editor SDK for your Flutter App"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/a-modern-video-editor-sdk-for-your-flutter-app/">A Modern Video Editor SDK for your Flutter App</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2024-09-13">13 Sep 2024</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="5 min read">5 min read</span>
    
</div>    </div>

    <a href="/blog/a-modern-video-editor-sdk-for-your-flutter-app/" class="u-absolute0 zindex3" aria-label="A Modern Video Editor SDK for your Flutter App"></a>
</div>
            </div>
            <div class="col s12 m6 l4 u-flex">
                <div class="cr u-overflowHidden u-flexColumnTop u-relative u-flex1 godo-tracking" data-event-category="Article" data-event-action="Related Posts" data-event-label="https://img.ly/blog/img-ly-partners-with-soundstripe/" data-event-non-interaction="true">
    <a href="/blog/img-ly-partners-with-soundstripe/" class="cr-img u-relative u-overflowHidden u-sizeFullWidth u-block">
        <img class="cr-imagen u-absolute u-image u-block blur-up lazyload"
            src="https://blog.img.ly/2023/06/soundstripe-app.jpg"
            srcset="https://blog.img.ly/2023/06/soundstripe-app.jpg"
            data-srcset="https://blog.img.ly/2023/06/soundstripe-app.jpg 300w,https://blog.img.ly/2023/06/soundstripe-app.jpg 600w"
            data-sizes="(max-width: 1000px) 400px, 600px"
            alt="IMG.LY Partners with Soundstripe to Infuse Video Editing with Epic Royalty-Free Music &amp; SFX"
        />
    </a>

    <div class="cr-inner u-padding15 u-flexColumnTop">
        <div class="cr-body">
                <h2 class="cr-t u-fontSize21 u-lineClamp2 u-contentTitle" style="margin-bottom:5px"><a href="/blog/img-ly-partners-with-soundstripe/">IMG.LY Partners with Soundstripe to Infuse Video Editing with Epic Royalty-Free Music &amp; SFX</a></h2>
        </div>

        <div class="hh-date u-flexCenter u-textMuted u-fontSizeSmaller">
    <time class="datetime u-textCapitalize" datetime="2023-05-24">24 May 2023</time>
    <span class="bull">&bull;</span>
    <span class="readingTime" style="cursor:default" title="2 min read">2 min read</span>
    
</div>    </div>

    <a href="/blog/img-ly-partners-with-soundstripe/" class="u-absolute0 zindex3" aria-label="IMG.LY Partners with Soundstripe to Infuse Video Editing with Epic Royalty-Free Music &amp; SFX"></a>
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
        <a href="https://www.facebook.com/sharer/sharer.php?u=https://img.ly/blog/ultimate-guide-to-ffmpeg/"
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
        <a href="https://x.com/share?text=FFmpeg%20-%20The%20Ultimate%20Guide&amp;url=https://img.ly/blog/ultimate-guide-to-ffmpeg/"
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
        <a href="whatsapp://send?text=https://img.ly/blog/ultimate-guide-to-ffmpeg/"
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
        this.page.url = 'https://img.ly/blog/ultimate-guide-to-ffmpeg/';
        this.page.identifier = 'ghost-636cbbad5e9bca0001403712';
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
