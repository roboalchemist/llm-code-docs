# Source: https://docs.together.ai/external-link-02.md

<!DOCTYPE html><!-- This site was created in Webflow. https://webflow.com --><!-- Last Published: Wed Mar 11 2026 12:32:14 GMT+0000 (Coordinated Universal Time) --><html data-wf-domain="www.together.ai" data-wf-page="69654e88dce9154b5f1206ed" data-wf-site="69654e88dce9154b5f1206dd" data-wf-intellimize-customer-id="117655561" lang="en" data-wf-collection="69654e88dce9154b5f12083a" data-wf-item-slug="how-to-build-a-real-time-image-generator-with-together-ai"><head><meta charset="utf-8"/><title>How to build a real-time image generator with Flux and Together AI</title><meta content="" name="description"/><meta content="How to build a real-time image generator with Flux and Together AI" property="og:title"/><meta content="" property="og:description"/><meta content="" property="og:image"/><meta content="How to build a real-time image generator with Flux and Together AI" property="twitter:title"/><meta content="" property="twitter:description"/><meta content="" property="twitter:image"/><meta property="og:type" content="website"/><meta content="summary_large_image" name="twitter:card"/><meta content="width=device-width, initial-scale=1" name="viewport"/><meta content="Webflow" name="generator"/><link href="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/css/together-ai-0ecab937ed8d4f4431c520693eb.webflow.shared.c12286a15.min.css" rel="stylesheet" type="text/css" integrity="sha384-wSKGoVXJ0VzSxE9D6Uq+Vn7NfhSiUE1C2ZsqxHGwlIpAqPJFXeDnxy8t2eBq3jlo" crossorigin="anonymous"/><script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script><link href="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699e382b218f39bfa0a115d9_favicon.png" rel="shortcut icon" type="image/x-icon"/><link href="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a59cff65ed0f267dd2fbe8_touchicon.png" rel="apple-touch-icon"/><link href="https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai" rel="canonical"/><style>.anti-flicker, .anti-flicker * {visibility: hidden !important; opacity: 0 !important;}</style><style>[data-wf-hidden-variation], [data-wf-hidden-variation] * {
        display: none !important;
      }</style><script type="text/javascript">localStorage.removeItem('intellimize_opt_out_117655561'); if (localStorage.getItem('intellimize_data_tracking_type') !== 'always') { localStorage.setItem('intellimize_data_tracking_type', 'always'); }</script><script type="text/javascript">(function(e){var s={r:[]};e.wf={r:s.r,ready:t=>{s.r.push(t)}}})(window)</script><script type="text/javascript">(function(e,t,p){var n=document.documentElement,s={p:[],r:[]},u={p:s.p,r:s.r,push:function(e){s.p.push(e)},ready:function(e){s.r.push(e)}};e.intellimize=u,n.className+=" "+p,setTimeout(function(){n.className=n.className.replace(RegExp(" ?"+p),"")},t)})(window, 4000, 'anti-flicker')</script><link href="https://cdn.intellimize.co/snippet/117655561.js" rel="preload" as="script"/><script type="text/javascript">var wfClientScript=document.createElement("script");wfClientScript.src="https://cdn.intellimize.co/snippet/117655561.js",wfClientScript.async=!0,wfClientScript.onerror=function(){document.documentElement.className=document.documentElement.className.replace(RegExp(" ?anti-flicker"),"")},document.head.appendChild(wfClientScript);</script><link href="https://api.intellimize.co" rel="preconnect" crossorigin="true"/><link href="https://log.intellimize.co" rel="preconnect" crossorigin="true"/><link href="https://117655561.intellimizeio.com" rel="preconnect"/><link href="rss.xml" rel="alternate" title="RSS Feed" type="application/rss+xml"/><!-- RSS Feed -->
<link rel="alternate" type="application/rss+xml" title="Together AI Blog" href="https://www.together.ai/blog/rss.xml">

<!-- Swiper CSS -->
<link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.css"
      />

<!-- Amplitude Analytics -->
<script src="https://cdn.amplitude.com/script/7112ee0414d837b39e27f32c77880095.js"></script>
<script>
  window.amplitude.init('7112ee0414d837b39e27f32c77880095', {
    fetchRemoteConfig: true,
    autocapture: true
  });
</script>
<!-- /Amplitude Analytics -->

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                                                      new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
      j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                            })(window,document,'script','dataLayer','GTM-T387P4MH');</script>
<!-- End Google Tag Manager --><!-- [Attributes by Finsweet] Powerful Rich Text -->
<script defer src="https://cdn.jsdelivr.net/npm/@finsweet/attributes-richtext@1/richtext.js"></script>

<!-- [Attributes by Finsweet] Table of Contents -->
<script defer src="https://cdn.jsdelivr.net/npm/@finsweet/attributes-toc@1/toc.js"></script>

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js">
</script>

<script src="https://cdn.jsdelivr.net/npm/howler@2.2.4/dist/howler.min.js"></script>

<script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    },
    options: {
      ignoreHtmlClass: 'text-size-smedium'
    }
  };
</script>

<style>
  .blog-custom{
    display:none;
  }
</style></head><body data-mode="Model Library"><div class="page-wrapper"><div class="global-wrap"><div class="w-embed w-iframe"><!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T387P4MH"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) --></div><div class="global-styles w-embed"><style>
  :root{
  }

  [data-transition] {
    transition-property: background-color, color, opacity, border-color, transform, padding, flex, width;
    transition-duration: 0.3s;
    transition-timing-function: ease;
  }

  @media (hover: hover) {
    a:hover [data-transition="img-link"]{
      transform: scale(1.1);
    }
  }

  .wf-design-mode .nav-wrapper{
    position: absolute;
  }
</style></div><div class="global-styles w-embed"><style>
  /* ------------------------- Scaling System by Osmo [https://osmo.supply/] -------------------------  */

  /* Desktop */
  :root {
    --size-unit: 16; /* body font-size in design - no px */
    --size-container-ideal: 1440; /* screen-size in design - no px */
    --size-container-min: 992px;
    --size-container-max: 1440px;
    --size-container: clamp(var(--size-container-min), 100vw, var(--size-container-max));
    --size-font: calc(var(--size-container) / (var(--size-container-ideal) / var(--size-unit)));
  }

  /* Tablet */
  @media screen and (max-width: 991px) {
    :root {
      --size-container-ideal: 834; /* screen-size in design - no px */
      --size-container-min: 768px;
      --size-container-max: 991px;
    }
  }

  /* Mobile Landscape */
  @media screen and (max-width: 767px) {
    :root {
      --size-container-ideal: 550; /* screen-size in design - no px */
      --size-container-min: 480px;
      --size-container-max: 767px;
    }
  }

  /* Mobile Portrait */
  @media screen and (max-width: 479px) {
    :root {
      --size-container-ideal: 390; /* screen-size in design - no px */
      --size-container-min: 390px;
      --size-container-max: 479px;
    }
  }

  html {
    font-size: var(--size-font);
  }


  /* _____ CSS Marqueee ____ */
  /* CSS Keyframe Animation */
  @keyframes translateX { 
    to {
      transform: translateX(-100%);
    }
  }
  @keyframes translateXRev { 
    to {
      transform: translateX(100%);
    }
  }

  [data-css-marquee-list] {
    animation: translateX 30s linear;
    animation-iteration-count: infinite;
    animation-play-state: paused;
  }

  [data-css-marquee="reverse"] [data-css-marquee-list] {
    animation: translateXRev 30s linear;
    animation-iteration-count: infinite;
    animation-play-state: paused;
  }

  /* _____ CSS Accordions____ */
  /* Animate Accordion Bottom Grid */
  [data-accordion-content]{
    transition: grid-template-rows 0.6s cubic-bezier(0.625, 0.05, 0, 1);
  }

  [data-accordion-status="active"] [data-accordion-content] {
    grid-template-rows: 1fr;
  }

  .accordion-css__item-top{
    transition: opacity 0.3s
  }

  [data-accordion-status="active"] [data-accordion-toggle]{
    opacity: 1;
  }

  /* Animate Icon */
  [data-accordion-icon] {
    transition: transform 0.6s cubic-bezier(0.625, 0.05, 0, 1);
  }

  [data-accordion-status="active"] [data-accordion-icon] {
    transform: rotate(180deg);
  }

  [data-countdown-date] {
    gap: 0.075em;
  }

  /* Links */
  [underline-link]::before,
  [underline-link-alt]::before,
  [underline-link-alt]::after{
    content: "";
    position: absolute;
    bottom: 0em;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: currentColor;
    transition: transform 0.3s cubic-bezier(0.625, 0.05, 0, 1);
    transform-origin: right;
    transform: scaleX(0) rotate(0.001deg);
  }

  [underline-link]:hover::before {
    transform-origin: left;
    transform: scaleX(1) rotate(0.001deg);
  }

  /* Alt */
  [underline-link-alt]::before {
    transform-origin: left;
    transform: scaleX(1) rotate(0.001deg);
    transition-delay: 0.3s;
  }

  [underline-link-alt]:hover::before {
    transform-origin: right;
    transform: scaleX(0) rotate(0.001deg);
    transition-delay: 0s;
  }

  [underline-link-alt]::after {
    transform-origin: right;
    transform: scaleX(0) rotate(0.001deg);
    transition-delay: 0s;
  }

  [underline-link-alt]:hover::after {
    transform-origin: left;
    transform: scaleX(1) rotate(0.001deg);
    transition-delay: 0.3s;
  }

  /* Modals */
  [data-modal-group-status] {
    transition: all 0.2s linear;
  }

  [data-modal-group-status="active"] {
    opacity: 1;
    visibility: visible;
  }

  [data-modal-name][data-modal-status="active"] {
    display: flex;
  }
</style></div><div class="hide w-embed"><style>
  /* ///////////////////// START OF GLOBAL EDITS ///////////////////// */
  main:focus-visible {
    outline: -webkit-focus-ring-color auto 0px;
  }

  /* --- Font Smoothing --- */
  body {
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
  }

  /* Make sure containers never lose their center alignment*/
  .container-medium, .container-small, .container-large {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  /* --- Links --- */
  [link-icon],
  [link-line]{
    transition: all 350ms ease-out;;
  }

  [link-icon="arrow-fade"]{
    opacity: 0;
    transform: translateX(-100%);
    transition-duration: 200ms;
  }

  @media (hover: hover){
    a:hover [link-icon="arrow"]{
      transform: translateX(0.25rem);
    }
    a:hover [link-icon="arrow-fade"]{
      opacity: 1;
      transform: translateX(-0%);
    }
    a:hover [link-icon="external"]{
      transform: translate(0.25rem, -0.25rem);
    }
    a:hover [link-line]{
      transform: scaleX(1);
    }
  }

  /* --- Rich Text --- */
  /* Get rid of top margin on first element in any rich text element */
  .w-richtext > :not(div):first-child, .w-richtext > div:first-child > :first-child {
    margin-top: 0 !important;
  }

  /* Get rid of bottom margin on last element in any rich text element */
  .w-richtext>:last-child, .w-richtext ol li:last-child, .w-richtext ul li:last-child {
    margin-bottom: 0 !important;
  }
  .text-rich-text li::marker{
    color: black;
  }

  .text-rich-inherit * {
    color: inherit;
    font-family: inherit;
    font-size: inherit;
    font-weight: inherit;
    font-style: inherit;
    line-height: inherit;
    letter-spacing: inherit;
    text-align: inherit;
    text-decoration: inherit;
    text-transform: inherit;
    margin-top: 0;
    margin-right: 0;
    margin-bottom: 0;
    margin-left: 0;
    padding-top: 0;
    padding-right: 0;
    padding-bottom: 0;
    padding-left: 0;
  }


  .text-rich-list-items li:before{
    display: block;
    content: "";
    background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='20' height='20' rx='4' fill='%23C8F6F9'/%3E%3Cpath d='M15.3132 6.37109L7.97982 13.7044L4.64648 10.3711' stroke='black' stroke-width='1.5'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: contain;
    position: absolute;
    top: -1px;
    left: 0;
    width: 1.25rem;
    height: 1.25rem;
  }


  /* --- Inherit links styling --- */
  a {
    color: inherit;
    text-decoration: inherit;
    font-size: inherit;
  }

  /*Apply "..." after 3 lines of text */
  [text-style-3lines] {
    display: -webkit-box;
    overflow: hidden;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }
  /* Apply "..." after 2 lines of text */
  [text-style-2lines] {
    display: -webkit-box;
    overflow: hidden;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
  /* Apply "..." at 100% width */
  [truncate-width] {
    min-width: 0;
    max-width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: block;
  }

  [data-authors-line] {
    min-width: 0;
    max-width: 100%;
    white-space: nowrap;
    overflow: hidden;
    display: block;
  }

  /* Removes native scrollbar */
  [no-scrollbar] {
    -ms-overflow-style: none;  
    overflow: -moz-scrollbars-none;  
  }

  [no-scrollbar]::-webkit-scrollbar {
    display: none;
  }

  /* --- These classes are never overwritten --- */
  .hide {
    display: none !important;
  }

  /* --- section --- */
  .section {
    position: relative;
  }

  @media screen and (max-width: 991px), 
    @media screen and (max-width: 767px), 
    @media screen and (max-width: 479px){
      .hide, .hide-tablet{
        display: none !important;
      }
  }

  @media screen and (max-width: 767px){
    .hide-mobile-landscape{
      display: none !important;
    }
  }

  @media screen and (max-width: 479px){
    .hide-mobile{
      display: none !important;
    }
  }
  /* ///////////////////// END OF GLOBAL EDITS ///////////////////// */

  /* ///////////////////// ELEMENTS ///////////////////// */

  /* Globals */
  :where(section:has(> .section-anchor)) {
    position: relative;
  }
  :where(div:has(> .img-cover)) {
    position: relative;
    overflow: hidden;
  }
  :where(:is(div,a):has(> .cover-link)) {
    cursor:pointer;
  }

  .container-large {
    max-width: var(--size-container);
  }

  [data-overflow-hidden]{
    overflow:hidden;
  }

  [data-no-pointer]{
    pointer-events: none;
  }

  [data-cms-hide-empty]:not(:has(.w-dyn-item)) {
    display: none;
  }

  /* Clear */
  .w-pagination-next{
    font-size: inherit !important;
  }

  /* Swiper */
  .swiper-button-disabled {
    opacity: 0.5;
    pointer-events:none;
  }

  /* Tabs */
  .tab-item[data-mode="dark"]{
    background-color: var(--shades--white-opacity-12);
    border-color: var(--shades--white-opacity-12);
    color: var(--brand--white);
  }
  .tab-item[data-mode="dark"].is-active{
    background-color: var(--opacity--purple-16);
    border-color: var(--opacity--purple-16);
    color: var(--brand--brand-purple);
  }

  /* Tabs */
  .w-tabs:before, .w-tabs:after{
    display: none;
  }

</style></div><div class="hide w-embed"><style>

  /* Dropdown */
  .wf-design-mode .nav-dropdowns{
    display: none;
  }
  .nav-links_item.is-active [data-transition="icon"]{
    transform: rotate(180deg);
  }
  .nav-dropdowns svg {
    visibility: visible;
  }

  /* Nav Hovers */
  @media (hover: hover){
    a:hover [data-wf--menu-icon--theme="cyan-light"]{
      background-color: var(--product--cyan-01)
    }
    a:hover [data-wf--menu-icon--theme="blue"]{
      background-color: var(--product--blue-01)
    }
    a:hover [data-wf--menu-icon--theme="purple"]{
      background-color: var(--product--purple-01)
    }
    a:hover [data-wf--menu-icon--theme="grey"]{
      background-color: var(--shades--black-opacity-8)
    }
  }

  /* Desktop */
  @media only screen and (min-width: 992px){
    /* Base */
    :is(.nav-dropdowns,
    .nav-dropdowns_item):not(.is-active){
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    /* Active */
    .nav-dropdowns_item:not(.is-active){
      position: absolute;
      top: 0;
    }
  }

  /* Responsive */
  @media only screen and (max-width: 992px){
    .nav-box.cc-small .btn{
      height: 2.5em !important;
    }

    [data-nav-status="open"] [data-transition="nav-brand"] {
      padding-left: 0.25em;
    }
    [data-nav-status="open"] .nav-ham_line:nth-child(1) {
      transform: translateY(3px) rotate(-45deg);
    }
    [data-nav-status="open"] .nav-ham_line:nth-child(2) {
      transform: translateY(-3px) rotate(45deg);
    }
  }

  /* Dark Mode */
  [data-wf--navbar--variant="dark"] .navbar-dropdown {
    color: var(--brand--white);
  }  
  [data-wf--navbar--variant="dark"] .navbar-dropdown_side-box {
    background-color: var(--shades--white-opacity-4);
  }
  [data-wf--navbar--variant="dark"] [data-wf--menu-icon--theme="grey"] {
    background-color: var(--brand--white);
  }

  @media (hover: hover){
    [data-wf--navbar--variant="dark"] a:hover [data-wf--menu-icon--theme="grey"]{
      background-color: var(--shades--white-opacity-90)
    }
  }

  @media only screen and (min-width: 992px){
    [data-wf--navbar--variant="dark"] .navbar-dropdown {
      background-color: #151532;
    }
  }

  @media only screen and (max-width: 991px){
    [data-wf--navbar--variant="dark"] .navbar-dropdown {
      background-color: var(--brand--transparent);
    }
  }

</style></div><div class="hide w-embed"><style>
  :root{
    --gradient-blue-3: linear-gradient(180deg, #FFF 15.93%, #F6FAFD 26.07%, #E5F3FF 73.05%);
    --gradients-white-gradient-footer: linear-gradient(180deg, #FFF 0%, rgba(255, 255, 255, 0.85) 100%);
    --gradients-dark-blue-gradient-footer: linear-gradient(180deg, #151531 0%, rgba(21, 21, 49, 0.90) 100%);
  }

  [data-gradient="3"]{
    background: var(--gradient-blue-3);
  }
  [data-gradient="footer-white"]{
    background: var(--gradients-white-gradient-footer);
  }
  [data-gradient="footer-dark"]{
    background: var(--gradients-dark-blue-gradient-footer);
  }

  /* Generic Backgrounds */
  [data-card-bg="wrap"]:nth-child(1) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61bea33d0d864f65494_card-bg_10.avif");
  }

  [data-card-bg="wrap"]:nth-child(2) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61832d95fe8ef16282c_card-bg_11.avif");
  }

  [data-card-bg="wrap"]:nth-child(3) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61b6dfbbc975f322e1c_card-bg_12.avif");
  }

  [data-card-bg="wrap"]:nth-child(4) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61b9785a5415bd908e7_card-bg_13.avif");
  }

  [data-card-bg="wrap"]:nth-child(5) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61ba1ea7f84bf5212f5_card-bg_14.avif");
  }

  [data-card-bg="wrap"]:nth-child(6) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c61807912b16e2a380ee_card-bg_15.avif");
  }

  [data-card-bg="wrap"]:nth-child(7) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c618b5ebec55d1115243_card-bg_16.avif");
  }

  [data-card-bg="wrap"]:nth-child(8) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c6180d51112f7d6331fa_card-bg_17.avif");
  }

  [data-card-bg="wrap"]:nth-child(9) [data-card-bg="item"] {
    background-image: url("https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a4c6187b494feb0d5323e0_card-bg_18.avif");
  }
</style></div><div class="w-embed"><style>
  /* Notification */
  .announcement-bar_item.inactive {
    overflow: hidden;
    text-overflow: ellipsis;
    transition: transform 500ms ease-in-out, opacity 500ms ease-in-out;
    white-space: nowrap;
    opacity: 0;
    transform: translateY(100%);
  }
  .announcement-bar_item.active {
    overflow: hidden;
    text-overflow: ellipsis;
    transition: transform 500ms ease-in-out, opacity 500ms ease-in-out;
    white-space: nowrap;
    opacity: 1;
  }

  /* Tabs */
  html:not(.wf-design-mode) [data-tabs-status="enabled"] [data-tabs="content"]:not(:first-child) {
    display: none;
  }

  /* Tags */
  [data-model-tags]{
    line-height: 1;
  }
  .display-inline.w-dyn-item:last-child .tag-dot{
    display:none;
  }
  /* Avatar Row */
  .avatar-row img{
    margin-right: -0.6em;
  }

  /* Hovers */
  .configuration-card:hover .optimized-hardware-bullet_icon{
    opacity: 0.7;
  }
  .configuration-card:hover .btn.is-secondary{
    color: var(--brand--white);
    background-color: var(--brand--black);
  }
  .models_link:hover .opacity-70{
    opacity: 0.4
  }

  /* Quotes Carousel */
  .testimonial-card-inner .stories-card{
    width: 100%;
  }
  .testimonial-card_stat-item:last-child{
    padding-right: 0;
    border: none;
  }
  .stories-card_meta .caption-s{
    text-wrap: balance;
  }
  @media only screen and (max-width: 992px){
    [data-swiper-instance="testimonials"] .swiper-slide:nth-child(n+3) {
      display: none;
    }
  }

  /* CMS Items */
  .bg-color-darkblue .content-item-row{
    border-color: var(--shades--white-opacity-16);
  }

  /* Copy to Clipboard */
  [data-copy-wrapper] [data-transition="icon"]:last-child{
    display: none;
  }
  [data-copy-wrapper].is-copied [data-transition="icon"]:first-child{
    display: none;
  }
  [data-copy-wrapper].is-copied [data-transition="icon"]:last-child{
    display: flex;
  }
</style></div><div class="hide w-embed"><style>
  /* ---- HubSpot Form Reset & Base ---- */
  .hs-form-html .hsfc-Form {
    width: 100%;
    font-family: inherit !important;
  }
  .hs-form-html .hsfc-Form * {
    box-sizing: border-box;
    font-family: inherit !important;
  }

  .hs-form-html .hsfc-Step .hsfc-Step__Content{
    padding: 0;
  }

  /* ---- Rows ---- */
  .hs-form-html .hsfc-Row {
    display: flex;
    gap: 1em;
    margin-bottom: 1.5em;
  }

  .hs-form-html .hsfc-Row > * {
    flex: 1 1 0;
    min-width: 0;
  }

  /* ---- Labels ---- */
  .hs-form-html .hsfc-FieldLabel {
    display: block;
    font-size: 0.75em;
    line-height: 1.2;
    font-weight: 400;
    letter-spacing: -0.03em;
    color: rgba(0,0,0,0.7);
    margin-bottom: 0.66em;
    cursor: default;
  }

  .hs-form-html .hsfc-FieldLabel__RequiredIndicator {
    color: inherit;
  }

  /* ---- Text Inputs & Textarea ---- */
  .hs-form-html .hsfc-TextInput,
  .hs-form-html .hsfc-TextareaInput,
  .hs-form-html .hsfc-DropdownOptions__Search .hsfc-TextInput{
    width: 100%;
    background: var(--opacity--blue-8);
    border: 1px solid var(--opacity--blue-40);
    border-radius: var(--_radius---4);
    color: var(--brand--black);
    font-size: 0.875em;
    padding: 0.5rem 0.75rem;
    outline: none;
    transition: border-color 0.2s ease, background 0.2s ease;
    -webkit-appearance: none;
    appearance: none;
    box-shadow: none !important;
  }

  .hs-form-html .hsfc-TextInput::placeholder,
  .hs-form-html .hsfc-TextareaInput::placeholder,
  .hs-form-html .hsfc-DropdownOptions__Search .hsfc-TextInput::placeholder {
    color: rgba(0,0,0,0.4);
  }

  .hs-form-html .hsfc-TextInput:is(:focus,:hover),
  .hs-form-html .hsfc-TextareaInput:is(:focus,:hover),
  .hs-form-html .hsfc-DropdownOptions__Search .hsfc-TextInput:is(:focus,:hover),
  .hs-form-html .hsfc-CheckboxFieldGroup__Options .hsfc-FieldLabel:is(:focus,:hover){
    border-color: var(--product--blue-01)
  }

  /*
  .hsfc-TextInput[aria-invalid="true"],
  .hsfc-TextareaInput[aria-invalid="true"] {
  border-color: #ef4444;
  }
  */

  .hs-form-html .hsfc-TextareaInput {
    min-height: 5.625rem;
    max-height: 10rem;
    min-width: 100%;
    max-width: 100%;
    resize: vertical;
  }

  /* ---- Dropdown ---- */
  .hs-form-html .hsfc-DropdownInput {
    position: relative;
  }

  .hs-form-html .hsfc-TextInput--button {
    cursor: pointer;
    padding-right: 40px;
  }

  .hs-form-html .hsfc-DropdownInput__Caret {
    position: absolute;
    padding: 0;
    top: 50%;
    right: 0.75em;
    transform: translateY(-50%);
    background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNSA4LjMzMzk4TDEwIDEzLjMzNEwxNSA4LjMzMzk4IiBzdHJva2U9ImJsYWNrIiBzdHJva2Utb3BhY2l0eT0iMC40IiBzdHJva2Utd2lkdGg9IjEuNSIvPjwvc3ZnPg==");
    background-size: cover;
    background-position: center;
    width: 1.5em;
    height: 1.5em;
  }

  .hs-form-html .hsfc-DropdownInput__Caret span {
    display:none;
  }

  .hs-form-html .hsfc-DropdownOptions {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    right: 0;
    background: #fff;
    border: 1px solid var(--product--blue-01);
    border-radius: var(--_radius---8);
    z-index: 100;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    overflow: hidden;
  }

  .hs-form-html .hsfc-DropdownOptions__Search {
    padding: 0.5em;
  }

  .hs-form-html .hsfc-DropdownOptions__List {
    list-style: none;
    margin: 0;
    padding: 0.5em;
    max-height: 20em;
    overflow-y: auto;
  }

  .hs-form-html .hsfc-DropdownOptions__List__ListItem {
    padding: 0.75rem 0.5rem;
    font-size: 0.875em;
    color: rgba(0,0,0,0.7);
    cursor: pointer;
    transition: background 0.15s ease;
    background: #9bcdf500;
  }

  .hs-form-html .hsfc-DropdownOptions__List__ListItem:hover{
    background: var(--opacity--blue-8) !important;
  }

  .hs-form-html .hsfc-DropdownOptions__List__ListItem[aria-selected="true"] {
    background: var(--opacity--blue-40) !important;
  }

  /* ---- Checkboxes ---- */
  .hs-form-html .hsfc-CheckboxFieldGroup__Options {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.3755em;
  }

  .hs-form-html .hsfc-CheckboxFieldGroup__Options > div {
    flex: none;
    margin-bottom: 0;
  }

  .hs-form-html .hsfc-CheckboxFieldGroup__Options .hsfc-FieldLabel {
    display: flex;
    height: 2.5em;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0 !important;
    background: var(--opacity--blue-8);
    border: 1px solid var(--opacity--blue-40);
    border-radius: var(--_radius---8);
    padding: 0.5em 0.75em;
    cursor: pointer;
    font-size: 1em;
    transition: border-color 0.2s ease, background 0.2s ease;
    gap: 1em;
    color: rgba(0,0,0,0.4);
  }

  .hs-form-html .hsfc-CheckboxInput {
    width: 1.125em;
    height: 1.125em;
    min-width: 1.125em;
    background-color: transparent;
    border-color: var(--shades--black-opacity-16);
    cursor: pointer;
    border-radius: var(--_radius---4);
    box-shadow: none !important;
  }

  .hs-form-html .hsfc-CheckboxInput span{
    font-size: 0.875em;
    letter-spacing: -0.01em;
    line-height: 1.3;
  }

  .hs-form-html .hsfc-CheckboxInput:checked{
    background-color: var(--product--blue-01);
    border-color: #54B2FD;
  }
  .hs-form-html .hsfc-CheckboxInput:checked:after{
    background-color: var(--brand--black);
    mask-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUiIGhlaWdodD0iMTUiIHZpZXdCb3g9IjAgMCAxNSAxNSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTEuOTgyOCAzLjkzMzU5TDUuMzgyODEgMTAuNTMzNkwyLjM4MjgxIDcuNTMzNTkiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMS41Ii8+PC9zdmc+");
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUiIGhlaWdodD0iMTUiIHZpZXdCb3g9IjAgMCAxNSAxNSIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTEuOTgyOCAzLjkzMzU5TDUuMzgyODEgMTAuNTMzNkwyLjM4MjgxIDcuNTMzNTkiIHN0cm9rZT0iYmxhY2siIHN0cm9rZS13aWR0aD0iMS41Ii8+PC9zdmc+")
  }

  .hs-form-html .hsfc-CheckboxInput:checked + span {
    color: var(--brand--black);
  }

  .hs-form-html .hsfc-CheckboxFieldGroup__Options .hsfc-FieldLabel:has(.hsfc-CheckboxInput:checked) {
    background: var(--opacity--blue-40);
    border-color: var(--product--blue-01);
  }

  /* ---- Rich Text / Privacy ---- */
  .hs-form-html .hsfc-RichText {
    font-size: inherit !important;
    font-size: 0.875em;
    color: rgba(0,0,0,0.7);
    line-height: 1.3;
    letter-spacing: -0.01em;
  }

  .hs-form-html .hsfc-RichText a {
    color: inherit;
    text-decoration: underline;
  }

  /* ---- Submit Button ---- */
  .hs-form-html .hsfc-Button {
    width: auto;
    z-index: 2;
    font-size: .6875em;
    grid-column-gap: .375rem;
    grid-row-gap: .375rem;
    background-color: var(--brand--black);
    color: var(--brand--white);
    text-align: center;
    letter-spacing: .005em;
    text-transform: uppercase;
    cursor: pointer;
    border-radius: .25rem;
    flex: none;
    justify-content: center;
    align-items: center;
    height: 2.5rem;
    padding: 1rem;
    font-family: PP Neue Montreal Mono, Georgia, sans-serif !important;
    font-weight: 500;
    line-height: 1;
    transition: box-shadow .45s cubic-bezier(.215, .61, .355, 1), border-color .45s cubic-bezier(.215, .61, .355, 1), color .45s cubic-bezier(.215, .61, .355, 1), opacity .45s cubic-bezier(.215, .61, .355, 1), background-color .45s cubic-bezier(.215, .61, .355, 1);
    display: inline-flex;
    position: relative;
  }

  .hs-form-html .hsfc-Button:hover {
    background-color: var(--shades--black-opacity-70) !important;
    transform: none !important;
  }

  .hs-form-html .hsfc-Button[aria-busy="true"] {
    opacity: 0.6;
    pointer-events: none;
  }

  /* ---- Navigation Row ---- */
  .hs-form-html .hsfc-NavigationRow__Buttons,
  .hs-form-html [data-hsfc-id=Renderer] .hsfc-NavigationRow__Buttons:has(>*:only-child){
    margin-top: 2em;
    justify-content: left !important;
    align-items: flex-start !important;
  }

  /* ---- Validation Errors ---- */
  .hs-form-html .hsfc-TextField>*:not(:last-child){
    margin-bottom: 0.5em;
  }
  .hs-form-html .hsfc-ErrorAlert {
    font-size: 0.75em;
    color: #ef4444;
  }
  .hs-form-html .hsfc-NavigationRow__Alerts{
    display: none !important;
  }

  /* Success */
  .hs-form-html .hsfc-PostSubmit {
    font-family: inherit;
    min-height: 31.25em;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
  }
  .hs-form-html .hsfc-Row{
    margin-bottom: 1em;
  }
  .hs-form-html .hsfc-PostSubmit .hsfc-RichText {
    font-family: inherit !important;
    text-align: center;
  }
  .hs-form-html .hsfc-PostSubmit .hsfc-Heading{
    color: var(--brand--black);
    text-align: center;
    font-size: 2.5em;
    font-style: normal;
    font-family: inherit;
    font-weight: 500;
    line-height: 120%;
    letter-spacing: -0.01em;
  }

  .hs-form-html .hsfc-PostSubmit .hsfc-RichText p{
    font-family: inherit;
    font-style: inherit;
    font-weight: inherit;
    text-decoration: inherit;
    color: inherit;
    font-size: inherit;
    text-align: center;
    font-size: 1.125em;
    font-style: normal;
    font-weight: 500;
    line-height: 130%;
    letter-spacing: -0.01em;
    color: var(--brand--black);
    opacity: 0.4;
  }

  /* ---- Mobile ---- */
  @media (max-width: 767px) {
    .hs-form-html .hsfc-Row {
      flex-direction: column;
      margin-bottom: 1em;
    }

    .hs-form-html .hsfc-TextInput,
    .hs-form-html .hsfc-TextareaInput,
    .hs-form-html .hsfc-DropdownOptions__Search .hsfc-TextInput{
      font-size: 1em;
    }

    .hs-form-html .hsfc-CheckboxFieldGroup__Options  {
      grid-template-columns: 1fr;
    }
  }
</style></div><div class="hide w-embed"><style>
  .w-richtext :is([data-rt-embed-type="true"],.w-embed):has(pre code) {
    background: var(--shades--black-opacity-4);
    border-radius: 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem !important;
    position: relative;
  }

  .w-richtext :is([data-rt-embed-type="true"],.w-embed) pre{
    flex: 1 1 auto;
    overflow: auto;
    overscroll-behavior: none;
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .w-richtext :is([data-rt-embed-type="true"],.w-embed) pre code{
  }

  .w-richtext :is([data-rt-embed-type="true"],.w-embed):has(pre code):after {
    content: "";
    display:block;
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    flex: 0 0 auto;
    width: 3rem;
    height: 3rem;
    margin-left: 0.5rem;
    border-radius: 0.25em;
    background-image: url("data:image/svg+xml,%3Csvg width='48' height='48' viewBox='0 0 48 48' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0)'%3E%3Cpath d='M19.6667 26.0378H17.3133L17.3125 24.0378V19.5044C17.3125 18.7577 17.3125 17.3711 17.3125 17.3711H19.4458H23.9792C24.6004 17.3711 25.3151 17.3711 25.3151 17.3711H25.9792C25.9792 17.3711 25.9792 19.0467 25.9792 19.668M22 30.668V22.0013H30.6458L30.6667 30.668H22Z' stroke='black' stroke-width='1.5'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0'%3E%3Crect width='16' height='16' fill='white' transform='translate(16 16)'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
    background-size: cover;
    background-color: var(--shades--black-opacity-4);
    border: 1px solid var(--shades--black-opacity-8);
    cursor: pointer;
    align-self: flex-start;
    transition: opacity .35s cubic-bezier(.215, .61, .355, 1);
    backdrop-filter: blur(6px);
  }

  .w-richtext :is([data-rt-embed-type="true"].copied,.w-embed.copied):has(pre code):after {
    background-image: url("data:image/svg+xml,%3Csvg width='48' height='48' viewBox='0 0 48 48' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M31.9688 18L20.9688 29L15.9688 24' stroke='black' stroke-width='1.5'/%3E%3C/svg%3E");
  }

  .w-richtext :is([data-rt-embed-type="true"],.w-embed):has(pre code):after:hover {
    opacity: 0.8;
  }

  /* Dark */
  [data-mode="Research"] .w-richtext :is([data-rt-embed-type="true"],.w-embed):has(pre code):after{
    background-image: url("data:image/svg+xml,%3Csvg width='48' height='48' viewBox='0 0 48 48' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23clip0)'%3E%3Cpath d='M19.6667 26.0378H17.3133L17.3125 24.0378V19.5044C17.3125 18.7577 17.3125 17.3711 17.3125 17.3711H19.4458H23.9792C24.6004 17.3711 25.3151 17.3711 25.3151 17.3711H25.9792C25.9792 17.3711 25.9792 19.0467 25.9792 19.668M22 30.668V22.0013H30.6458L30.6667 30.668H22Z' stroke='white' stroke-width='1.5'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id='clip0'%3E%3Crect width='16' height='16' fill='white' transform='translate(16 16)'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
  }
  
  [data-mode="Research"] .w-richtext :is([data-rt-embed-type="true"].copied,.w-embed.copied):has(pre code):after{
    background-image: url("data:image/svg+xml,%3Csvg width='48' height='48' viewBox='0 0 48 48' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M31.9688 18L20.9688 29L15.9688 24' stroke='white' stroke-width='1.5'/%3E%3C/svg%3E");
  }
</style></div><div class="w-embed"><style>
  [data-mobile-dropdown="wrapper"] {
    position: relative;
  }

  .mob-dd-trigger {
    display: none;
  }

  .mob-dd-list {
    display: none;
  }

  @media (max-width: 991px) {
    .mob-dd-wrap{
      position: relative;
      width: auto;
    }
    
    .mob-dd-trigger {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1em;
      cursor: pointer;
      padding: 0.625em 0.75em;
      background: var(--brand--white);
      border: 1px solid var(--shades--black-opacity-8);
      border-radius: 0.5em;
      user-select: none;
    }

    .mob-dd-label {
      display: flex;
      align-items: center;
      gap: 1em;
      min-width: 0;
      flex: 1;
    }

    .mob-dd-arrow {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: inherit;
    }

    .mob-dd-list {
      display: flex;
      position: absolute;
      margin-top: 0.5em;
      top: 100%;
      left: 0;
      width: 100%;
      z-index: 99;
      background: var(--brand--white);
      color: var(--brand--black);
      border: 1px solid var(--shades--black-opacity-8);
      border-radius: 0.5em;
      overflow: hidden;
      padding: 0.5em;
      gap: 0.25em;
      flex-direction: column;
    }

    /* Dark Theme */
    .bg-color-darkblue  .mob-dd-trigger{
      background: var(--shades--white-opacity-8);
      border-color: var(--shades--white-opacity-24);
    }

    .bg-color-darkblue  .mob-dd-list{
      background: var(--brand--dark-blue);
      border-color: var(--shades--white-opacity-24);
      color: rgba(255,255,255,0.7);
    }
  }
</style></div></div><div class="w-embed"><style>
  /* Wrap for Blogs */
  .sqs-block-content {
    display: flex;
    flex-direction: row;
    overflow: auto;
    max-width: 100vw;
    flex-flow: column;
    margin-top: 5rem;
    margin-bottom: 5rem;
  }

  @media screen and (max-width: 991px) {
    .sqs-block-content {
      display: flex;
      width: 100vw;
      max-width: none;
      padding-right: var(--_spacers---padding-global);
      padding-left: var(--_spacers---padding-global);
      justify-content: flex-start;
      margin-left: calc(var(--_spacers---padding-global) * -1);
    }
  }
  /* General Table Styling */
  table {
    width: auto;
    flex: 0 0 auto;
    min-width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-style: solid;
    border-width: 1px;
    border-top-color: var(--shades--black-opacity-8);
    border-right-color: var(--shades--black-opacity-8);
    border-bottom-color: var(--shades--black-opacity-8);
    border-left-color: var(--shades--black-opacity-8);
    border-top-left-radius: var(--_radius---8);
    border-top-right-radius: var(--_radius---8);
    border-bottom-left-radius: var(--_radius---8);
    border-bottom-right-radius: var(--_radius---8);
    color: inherit !important;
    background-color: inherit !important;
  }


  table th, table td {
    text-align: left;
    vertical-align: top;
    padding: 1em;
    border-bottom: 1px solid var(--shades--black-opacity-8) !important;
    max-width: 90vw;
    color: inherit !important;
  }

  @media only screen and (max-width: 991px){
    table th, table td{
      min-width: 10em;
    }
    table td:first-child{
      white-space: nowrap;
    }
  }

  /* Header Styling */
  table th {
    background-color: var(--opacity--blue-16) !important;
    font-weight: bold;
    padding: 1.25em 1em;
  }

  /* Row Styling */
  table tr {
    background-color: var(--brand--white);
  }
  table tr:last-child td{
    border-bottom: none;
  }

</style></div><div class="hide w-embed"><style>
  [data-howler-status="not-playing"] .howler-player__btn-play,
  [data-howler-status="playing"] .howler-player__btn-pause{
    display: flex;
  }

  [data-howler-status="playing"] .howler-player__btn-play,
  [data-howler-status="not-playing"] .howler-player__btn-pause{
    display: none;
  }
</style></div><div class="hide w-embed"><style>
  [data-mode="Research"]{
    background-color: var(--brand--dark-blue);
    color: var(--brand--white);
  }
  [data-mode="Research"] .main-wrapper{
    --opacity--blue-16: var(--shades--white-opacity-8);
    --shades--black-opacity-4: var(--shades--white-opacity-8);
    --shades--black-opacity-8: var(--shades--white-opacity-12);
    --shades--black-opacity-12: var(--shades--white-opacity-12);
  }
  [data-mode="Research"] table tr,
  [data-mode="Research"] .howler-player{
    background-color: var(--shades--white-opacity-8);
  }
  [data-mode="Research"] .blog-custom-cta{
    background-image: url('https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1c16ce6d7bea259852341_research-areas-card-bg.jpg')
  }

  [data-mode="Research"] .fs-cmsfilter_active,
  [data-mode="Research"] .button{
    background-color:var(--brand--white);
    color: var(--brand--black);
  }

</style></div><div class="w-embed"><style>

  hr{
    margin-top: 1.6rem;
  }

  [fs-richtext-component]{
    margin: 4rem 0;
  }
  :is([fs-richtext-component],.w-richtext .w-embedmargin: 0;
    opacity: 1;
  }
  :is([fs-richtext-component],.w-richtext .w-embed) a{
    text-decoration: none;
  }

  :is([fs-richtext-component],.w-richtext .w-embed) a:hover{
    color: white;
  }

  :is([fs-richtext-component],.w-richtext .w-embed) ul{
    padding: 0 !important;
  }

  .blog-custom_cards-visual video{
    height: 100% !important;
  }
</style></div><div class="announcement-bar"><div class="hide w-embed w-script"><script>
  window.addEventListener('DOMContentLoaded', function () {
    jQuery(function () {

      // Rotating
      $(document).ready(function () {
        const $links = $('.announcement-bar_item');
        let currentIndex = 0;
        function activateLink(index) {
          $links.addClass('inactive').removeClass('active');
          $links.eq(index).removeClass('inactive').addClass('active');
          currentIndex = (currentIndex + 1) % $links.length;
          let timeout = index != 0 ? 3000 : 5000;
          setTimeout(function () {
            activateLink(currentIndex);
          }, timeout);
        }
        activateLink(currentIndex);
      });

      // Scrolling
      (function () {
        const $html = $("html");
        const bar = document.querySelector(".announcement-bar");
        if (!bar || bar.offsetParent === null) {
          $html[0].style.setProperty("--_spacers---announcement-bar", "0em");
          return;
        }

        const rootFontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
        const barEm = bar.offsetHeight / rootFontSize;
        const proxy = { val: barEm };

        // If already past the bar on load, just set to 0 and let ScrollTrigger take over on enter back
        const barBottom = bar.getBoundingClientRect().bottom;
        if (barBottom <= 0) {
          proxy.val = 0;
          $html[0].style.setProperty("--_spacers---announcement-bar", "0em");
        }

        gsap.to(proxy, {
          val: 0,
          ease: "power2.out",
          immediateRender: false,
          scrollTrigger: {
            trigger: ".announcement-bar",
            start: "50% top",
            end: "bottom top",
            scrub: 0.5,
          },
          onUpdate() {
            $html[0].style.setProperty("--_spacers---announcement-bar", proxy.val.toFixed(4) + "em");
          },
        });

      })();

    });
  });
</script></div><div class="container-large"><div class="announcement-bar_inner"><div class="announcement-bar_wrap w-dyn-list"><div role="list" class="announcement-bar_list w-dyn-items"><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-0" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269654e88dce9154b5f12103f%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/flashattention-4" class="w-inline-block"><p class="body-s">⚡️ FlashAttention-4: up to 1.3× faster than cuDNN on NVIDIA Blackwell →</p></a></div><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-1" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269a5b888ee215b764b8e4b40%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/introducing-together-ai-new-look" class="w-inline-block"><p class="body-s">Introducing Together AI&#x27;s new look →</p></a></div><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-2" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269654e88dce9154b5f121040%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/adaptive-learning-speculator-system-atlas" class="w-inline-block"><p class="body-s">🔎 ATLAS: runtime-learning accelerators delivering up to 4x faster LLM inference →</p></a></div><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-3" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269654e88dce9154b5f121043%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/together-instant-clusters-ga" class="w-inline-block"><p class="body-s">⚡ Together Instant Clusters: self-service NVIDIA GPUs, now generally available →</p></a></div><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-4" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269654e88dce9154b5f121287%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/batch-inference-api-updates-2025" class="w-inline-block"><p class="body-s">📦 Batch Inference API: Process billions of tokens at 50% lower cost for most models →</p></a></div><div role="listitem" class="announcement-bar_item w-dyn-item"><img loading="lazy" src="https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg" alt="" class="announcement-bar_logo w-dyn-bind-empty"/><a data-wf-native-id-path="c8b74614-d019-fc44-678f-d3e51a1f61c0:88164890-3b47-779b-bcc5-e5933f3fda1d_instance-5" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="88164890-3b47-779b-bcc5-e5933f3fda1d" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f12093e%22%2C%22itemId%22%3A%2269654e88dce9154b5f121288%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%2288164890-3b47-779b-bcc5-e5933f3fda15%22%2C%22instanceId%22%3A%22c8b74614-d019-fc44-678f-d3e51a1f61c0%22%7D%5D" href="/blog/fine-tuning-updates-sept-2025" class="w-inline-block"><p class="body-s">🪛 Fine-Tuning Platform Upgrades: Larger Models, Longer Contexts →</p></a></div></div></div></div></div></div><div class="nav-wrapper"><nav data-wf--navbar--variant="base" class="nav"><div data-transition="nav-brand" class="nav-box"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec6f1" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec6f1" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="/" class="nav-brand w-inline-block"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 119 26" fill="none" class="nav-logo"><path d="M26.0946 3.36759C24.2311 0.14917 20.1033 -0.95347 16.8756 0.904425C14.799 2.09984 13.6008 4.21357 13.5065 6.43765L20.2512 6.44623L20.2504 7.02289H13.5061C13.5496 8.07403 13.841 9.1215 14.405 10.0958C16.2685 13.3142 20.3963 14.4169 23.6244 12.5586C26.8525 10.7007 27.9584 6.58518 26.0946 3.36677V3.36759Z" fill="#EF2CC1"></path><path d="M0.905194 3.36551C-0.958275 6.58393 0.147673 10.699 3.37534 12.5573C5.45196 13.7527 7.88726 13.7302 9.86632 12.6999L6.50175 6.87205L7.00308 6.58434L10.375 12.4073C11.2662 11.8441 12.0307 11.0689 12.5947 10.0946C14.4582 6.87614 13.3522 2.76106 10.1246 0.902757C6.89609 -0.955546 2.76866 0.147094 0.905194 3.36551Z" fill="#CAAEF5"></path><path d="M13.4985 25.1174C17.2258 25.1174 20.2473 22.105 20.2473 18.3888C20.2473 15.998 19.0102 13.9067 17.1258 12.7129L13.7457 18.5322L13.2452 18.2433L16.6171 12.4203C15.6825 11.9323 14.6266 11.6602 13.4981 11.6602C9.77074 11.6602 6.74927 14.6726 6.74927 18.3888C6.74927 22.105 9.77074 25.1174 13.4981 25.1174H13.4985Z" fill="#FC4C02"></path><path d="M32 9.63382H33.2836V5.19141H35.0534V9.62984H37.0744V11.1863H35.0534V19.5178H33.2836V11.1903H32V9.63382Z" fill="currentColor"></path><path d="M41.9655 9.37891C44.7877 9.37891 47.1077 11.7156 47.1077 14.5776C47.1077 17.4397 44.7917 19.7764 41.9655 19.7764C39.1392 19.7764 36.8232 17.4397 36.8232 14.5776C36.8232 11.7156 39.1392 9.37891 41.9655 9.37891ZM41.9655 18.1324C43.8828 18.1324 45.3776 16.6157 45.3776 14.5776C45.3776 12.5395 43.8828 11.0229 41.9655 11.0229C40.0481 11.0229 38.5533 12.5395 38.5533 14.5776C38.5533 16.6157 40.0481 18.1324 41.9655 18.1324Z" fill="currentColor"></path><path d="M52.8952 25.0349C50.4517 25.0349 48.0679 23.3312 48.0679 20.5527H49.7939C49.9414 22.4276 51.2688 23.4148 52.8912 23.4148C54.7647 23.4148 56.1998 22.1091 56.1998 19.9198V17.814C55.5261 19.0361 54.0512 19.7725 52.7238 19.7725C49.9016 19.7725 47.749 17.4597 47.749 14.5737C47.749 11.6878 49.8976 9.375 52.7238 9.375C54.0512 9.375 55.5261 10.1114 56.1998 11.3335V9.62976H57.9697V19.9198C57.9697 22.8853 55.6935 25.0349 52.8912 25.0349H52.8952ZM52.9191 18.1324C54.8365 18.1324 56.3313 16.6158 56.3313 14.5777C56.3313 12.5396 54.8365 11.023 52.9191 11.023C51.0018 11.023 49.5069 12.5396 49.5069 14.5777C49.5069 16.6158 51.0018 18.1324 52.9191 18.1324Z" fill="currentColor"></path><path d="M67.5413 16.0904L68.9724 16.8905C67.9838 18.7415 66.2976 19.7725 64.3564 19.7725C61.574 19.7725 59.2979 17.4358 59.2979 14.5737C59.2979 11.7116 61.574 9.375 64.3564 9.375C67.1387 9.375 69.1837 11.3932 69.1837 14.932H61.0079C61.1754 16.8268 62.6303 18.1324 64.3603 18.1324C66.0904 18.1324 66.8477 17.396 67.5413 16.0904ZM61.1116 13.5228H67.3061C67.0949 12.1137 66.0425 10.9752 64.3564 10.9752C62.7977 10.9752 61.5341 12.0062 61.1116 13.5228Z" fill="currentColor"></path><path d="M69.375 9.63382H70.6586V5.19141H72.4284V9.62984H74.4494V11.1863H72.4284V19.5178H70.6586V11.1903H69.375V9.63382Z" fill="currentColor"></path><path d="M79.5038 10.9594C77.9452 10.9594 76.849 12.1576 76.849 14.116V19.5258H75.0791V5.19141H76.849V11.1664C77.5226 10.0916 78.6189 9.37906 80.0938 9.37906C82.3699 9.37906 83.5936 10.9992 83.5936 12.9139V19.5218H81.8238V13.3557C81.8238 11.8391 80.9588 10.9554 79.5078 10.9554L79.5038 10.9594Z" fill="currentColor"></path><path d="M93.1009 16.0904L94.5319 16.8905C93.5434 18.7415 91.8572 19.7725 89.9159 19.7725C87.1335 19.7725 84.8574 17.4358 84.8574 14.5737C84.8574 11.7116 87.1335 9.375 89.9159 9.375C92.6983 9.375 94.7432 11.3932 94.7432 14.932H86.5675C86.7349 16.8268 88.1899 18.1324 89.9199 18.1324C91.6499 18.1324 92.4073 17.396 93.1009 16.0904ZM86.6711 13.5228H92.8657C92.6544 12.1137 91.6021 10.9752 89.9159 10.9752C88.3573 10.9752 87.0937 12.0062 86.6711 13.5228Z" fill="currentColor"></path><path d="M101.456 11.5674C101.117 11.2729 100.615 11.1256 100.108 11.1256C98.6334 11.1256 97.7923 12.4074 97.7923 14.135V19.5208H96.0225V9.63285H97.7923V11.3167C98.2787 10.2419 99.2473 9.42188 100.531 9.42188C101.165 9.42188 101.731 9.63285 102.089 9.90751L101.456 11.5714V11.5674Z" fill="currentColor"></path><path d="M114.124 9.63359V19.5255H112.354V17.8218C111.681 19.0439 110.206 19.7803 108.878 19.7803C106.056 19.7803 103.904 17.4675 103.904 14.5815C103.904 11.6956 106.052 9.38281 108.878 9.38281C110.206 9.38281 111.681 10.1192 112.354 11.3413V9.63757H114.124V9.63359ZM109.066 18.1323C110.983 18.1323 112.478 16.6157 112.478 14.5776C112.478 12.5395 110.983 11.0228 109.066 11.0228C107.148 11.0228 105.654 12.5395 105.654 14.5776C105.654 16.6157 107.148 18.1323 109.066 18.1323Z" fill="currentColor"></path><path d="M117.895 9.63281V19.5247H116.125V9.63281H117.895Z" fill="currentColor"></path><path d="M115.83 6.17827C115.83 5.54535 116.376 5 117.01 5C117.644 5 118.19 5.54933 118.19 6.17827C118.19 6.80722 117.664 7.35655 117.01 7.35655C116.356 7.35655 115.83 6.8311 115.83 6.17827Z" fill="currentColor"></path><path d="M100.527 18.4712C100.527 17.8383 101.073 17.293 101.707 17.293C102.341 17.293 102.887 17.8423 102.887 18.4712C102.887 19.1002 102.361 19.6495 101.707 19.6495C101.054 19.6495 100.527 19.1241 100.527 18.4712Z" fill="#FC4C02"></path></svg></a><div class="nav-menu"><ul data-accordion-css-init="" data-accordion-close-siblings="true" role="list" class="nav-links"><li data-accordion-status="not-active" data-dropdown-trigger="inference" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec705" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec705" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Inference</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70b:cfad3a49-6163-a5dd-9141-338a5187287f:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec70b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287f%22%7D%5D" href="/serverless-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="cloud" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180035)"><path d="M6.657 17.9999C4.085 17.9999 2 15.9929 2 13.5169C2 11.0419 4.085 9.03488 6.657 9.03488C7.05 7.27288 8.451 5.83488 10.332 5.26188C12.212 4.68988 14.288 5.06888 15.776 6.26188C17.264 7.45188 17.938 9.26888 17.546 11.0309H18.536C20.449 11.0309 22 12.5909 22 14.5169C22 16.4439 20.449 18.0039 18.535 18.0039H6.657" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180035"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Serverless Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">High-performance inference as APIs</p></div></div></a><link rel="prefetch" href="/serverless-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70b:cfad3a49-6163-a5dd-9141-338a51872882:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec70b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872882%22%7D%5D" href="/batch-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="stack" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180061)"><path d="M12 4L4 8L12 12L20 8L12 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L12 16L20 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 16L12 20L20 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180061"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Batch Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference for batch workloads</p></div></div></a><link rel="prefetch" href="/batch-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70b:cfad3a49-6163-a5dd-9141-338a51872885:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec70b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872885%22%7D%5D" href="/dedicated-model-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="dedicated-endpoints" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180037)"><path d="M6.657 15.9999C4.085 15.9999 2 13.9929 2 11.5169C2 9.04188 4.085 7.03488 6.657 7.03488C7.05 5.27288 8.451 3.83488 10.332 3.26188C12.212 2.68988 14.288 3.06888 15.776 4.26188C17.264 5.45188 17.938 7.26888 17.546 9.03088H18.536C20.449 9.03088 22 10.5909 22 12.5169C22 14.4439 20.449 16.0039 18.535 16.0039H6.657" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 16V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16 16V20C16 20.2652 16.1054 20.5196 16.2929 20.7071C16.4804 20.8946 16.7348 21 17 21H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16V20C8 20.2652 7.89464 20.5196 7.70711 20.7071C7.51957 20.8946 7.26522 21 7 21H3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180037"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Dedicated Model Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference on custom hardware</p></div></div></a><link rel="prefetch" href="/dedicated-model-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70b:cfad3a49-6163-a5dd-9141-338a51872888:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec70b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872888%22%7D%5D" href="/dedicated-container-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="container" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180038)"><path d="M12 3L20 7.5V16.5L12 21L4 16.5V7.5L12 3Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L20 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L4 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180038"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Dedicated Container Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference for custom models</p></div></div></a><link rel="prefetch" href="/dedicated-container-inference"/></li></ul><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70b:cfad3a49-6163-a5dd-9141-338a5187288b:1d56cce1-fb54-e7b7-1ed5-1940190ef0d4" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="1d56cce1-fb54-e7b7-1ed5-1940190ef0d4" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec70b%22%7D%2C%7B%22componentId%22%3A%221d56cce1-fb54-e7b7-1ed5-1940190ef0d4%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187288b%22%7D%5D" href="/models" class="navbar-dropdown_side-box w-inline-block"><div class="navbar-dropdown_models-cta"><div class="navbar-dropdown_models-visual"><div class="navbar-dropdown_models-box"><div class="navbar-dropdown_models-row cc-1"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715c615c4883c5b0a7b_minimax.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">MiniMax M2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6994e2f1daa0c6879cc689b2_google.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Nano Banana Pro</div></div></div></div><div class="navbar-dropdown_models-row cc-2"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715728a41f2c0fc8af1_Qwen.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Qwen3.5-397B</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715f769d5a7881d0a08_ZAI.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">GLM-5</div></div></div></div><div class="navbar-dropdown_models-row cc-3"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94db9b8ff9451666717_kimi.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">kimi k2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94df75d5951f9db7060_open-ai.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">gpt-oss-120B</div></div></div></div></div></div><div><p class="body-m text-weight-medium">Model library</p><p class="body-s">Explore the top open-source models</p></div></div></a><link rel="prefetch" href="/models"/></div></div></div></li><li data-accordion-status="not-active" data-dropdown-trigger="compute" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec70d" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec70d" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Compute</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown"><div class="navbar-dropdown_sections"><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Accelerated Compute</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b99a:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b99a%22%7D%5D" href="/gpu-clusters" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="gpu" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_7040_158249)"><path d="M4 8.00195C4 7.2063 4.31607 6.44324 4.87868 5.88063C5.44129 5.31802 6.20435 5.00195 7 5.00195H17C17.7956 5.00195 18.5587 5.31802 19.1213 5.88063C19.6839 6.44324 20 7.2063 20 8.00195L21 15.9993V16.9993C21 17.795 20.6839 18.558 20.1213 19.1206C19.5587 19.6833 18.7956 19.9993 18 19.9993H6C5.20435 19.9993 4.44129 19.6833 3.87868 19.1206C3.31607 18.558 3 17.795 3 16.9993V15.9993L4 8.00195Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L20 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 16V16.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_7040_158249"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">GPU Clusters</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Reliable GPU clusters at scale</p></div></div></a><link rel="prefetch" href="/gpu-clusters"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b99e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b99e%22%7D%5D" href="/ai-factory" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="clusters" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180039)"><path d="M3 17C3 16.4696 3.21071 15.9609 3.58579 15.5858C3.96086 15.2107 4.46957 15 5 15H7C7.53043 15 8.03914 15.2107 8.41421 15.5858C8.78929 15.9609 9 16.4696 9 17V19C9 19.5304 8.78929 20.0391 8.41421 20.4142C8.03914 20.7893 7.53043 21 7 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V17Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 17C15 16.4696 15.2107 15.9609 15.5858 15.5858C15.9609 15.2107 16.4696 15 17 15H19C19.5304 15 20.0391 15.2107 20.4142 15.5858C20.7893 15.9609 21 16.4696 21 17V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H17C16.4696 21 15.9609 20.7893 15.5858 20.4142C15.2107 20.0391 15 19.5304 15 19V17Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 5C9 4.46957 9.21071 3.96086 9.58579 3.58579C9.96086 3.21071 10.4696 3 11 3H13C13.5304 3 14.0391 3.21071 14.4142 3.58579C14.7893 3.96086 15 4.46957 15 5V7C15 7.53043 14.7893 8.03914 14.4142 8.41421C14.0391 8.78929 13.5304 9 13 9H11C10.4696 9 9.96086 8.78929 9.58579 8.41421C9.21071 8.03914 9 7.53043 9 7V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 15V14C6 13.4696 6.21071 12.9609 6.58579 12.5858C6.96086 12.2107 7.46957 12 8 12H16C16.5304 12 17.0391 12.2107 17.4142 12.5858C17.7893 12.9609 18 13.4696 18 14V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 9V12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180039"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">AI Factory</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Custom infrastructure at frontier scale</p></div></div></a><link rel="prefetch" href="/ai-factory"/></li></ul></div><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Developer Environments</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:7c593527-d2e7-4e55-5ae7-d011eb1b15ea:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%227c593527-d2e7-4e55-5ae7-d011eb1b15ea%22%7D%5D" href="/sandbox" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="sandbox" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180041)"><path d="M20 7.5V16.5L16 18.75L12 21L8 18.75L4 16.5V7.5L8 5.25L12 3L16 5.25L20 7.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L16 9.75L20 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L8 9.75L4 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M20 12L16 14V18.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L8 14V18.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 5.25L12 7.5L16 5.25" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180041"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Sandbox</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Build development environments for AI</p></div></div></a><link rel="prefetch" href="/sandbox"/></li></ul></div><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Storage</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:5859d0a5-3bbd-ecfb-d32a-e015aa9a7e35:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%225859d0a5-3bbd-ecfb-d32a-e015aa9a7e35%22%7D%5D" href="/managed-storage" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="folder" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180042)"><path d="M5 4H9L12 7H19C19.5304 7 20.0391 7.21071 20.4142 7.58579C20.7893 7.96086 21 8.46957 21 9V17C21 17.5304 20.7893 18.0391 20.4142 18.4142C20.0391 18.7893 19.5304 19 19 19H5C4.46957 19 3.96086 18.7893 3.58579 18.4142C3.21071 18.0391 3 17.5304 3 17V6C3 5.46957 3.21071 4.96086 3.58579 4.58579C3.96086 4.21071 4.46957 4 5 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180042"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Managed Storage</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Store model weights &amp; data securely</p></div></div></a><link rel="prefetch" href="/managed-storage"/></li></ul></div></div><div no-scrollbar="" class="navbar-dropdown_side-box"><ul role="list" class="cc-list-16 is-menu-gpu"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b9a4:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a4%22%7D%5D" href="/gpu/nvidia-gb300-nvl72" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">GB300</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-gb300-nvl72"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b9a6:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a6%22%7D%5D" href="/gpu/nvidia-gb200-nvl72" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">GB200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-gb200-nvl72"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b9a8:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a8%22%7D%5D" href="/gpu/nvidia-hgx-b200" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">B200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-hgx-b200"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:f70f39c7-12a0-fcb8-a96c-b0761e04b9aa:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9aa%22%7D%5D" href="/gpu/nvidia-h200" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">H200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-h200"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec713:e660ced2-171d-c32b-3ba1-eb160450318d:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec713%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22e660ced2-171d-c32b-3ba1-eb160450318d%22%7D%5D" href="/gpu/nvidia-h100" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">H100</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-h100"/></li></ul></div></div></div></div></li><li data-accordion-status="not-active" data-dropdown-trigger="model-shaping" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec715" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec715" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Model Shaping</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec71b:e4519510-df79-e08b-0573-66303879d77e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec71b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e4519510-df79-e08b-0573-66303879d77e%22%7D%5D" href="/fine-tuning" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="purple" class="menu-icon w-variant-90cf24ef-cc0e-eebd-76e9-8cb20dcc72fa"><div data-wf--product-icons--icon="fine-tuning" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180043)"><path d="M4 10C4 10.5304 4.21071 11.0391 4.58579 11.4142C4.96086 11.7893 5.46957 12 6 12C6.53043 12 7.03914 11.7893 7.41421 11.4142C7.78929 11.0391 8 10.5304 8 10C8 9.46957 7.78929 8.96086 7.41421 8.58579C7.03914 8.21071 6.53043 8 6 8C5.46957 8 4.96086 8.21071 4.58579 8.58579C4.21071 8.96086 4 9.46957 4 10Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 4V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 12V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10 16C10 16.5304 10.2107 17.0391 10.5858 17.4142C10.9609 17.7893 11.4696 18 12 18C12.5304 18 13.0391 17.7893 13.4142 17.4142C13.7893 17.0391 14 16.5304 14 16C14 15.4696 13.7893 14.9609 13.4142 14.5858C13.0391 14.2107 12.5304 14 12 14C11.4696 14 10.9609 14.2107 10.5858 14.5858C10.2107 14.9609 10 15.4696 10 16Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 4V14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 18V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16 7C16 7.53043 16.2107 8.03914 16.5858 8.41421C16.9609 8.78929 17.4696 9 18 9C18.5304 9 19.0391 8.78929 19.4142 8.41421C19.7893 8.03914 20 7.53043 20 7C20 6.46957 19.7893 5.96086 19.4142 5.58579C19.0391 5.21071 18.5304 5 18 5C17.4696 5 16.9609 5.21071 16.5858 5.58579C16.2107 5.96086 16 6.46957 16 7Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 4V5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 9V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180043"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Fine-Tuning</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Shape models with your data</p></div></div></a><link rel="prefetch" href="/fine-tuning"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec71b:14dc301c-2c6d-15e9-5c67-5e034664b24f:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec71b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%2214dc301c-2c6d-15e9-5c67-5e034664b24f%22%7D%5D" href="/evaluations" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="purple" class="menu-icon w-variant-90cf24ef-cc0e-eebd-76e9-8cb20dcc72fa"><div data-wf--product-icons--icon="stats" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_7039_175631)"><path d="M3 13C3 12.7348 3.10536 12.4804 3.29289 12.2929C3.48043 12.1054 3.73478 12 4 12H8C8.26522 12 8.51957 12.1054 8.70711 12.2929C8.89464 12.4804 9 12.7348 9 13V19C9 19.2652 8.89464 19.5196 8.70711 19.7071C8.51957 19.8946 8.26522 20 8 20H4C3.73478 20 3.48043 19.8946 3.29289 19.7071C3.10536 19.5196 3 19.2652 3 19V13Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 9C9 8.73478 9.10536 8.48043 9.29289 8.29289C9.48043 8.10536 9.73478 8 10 8H14C14.2652 8 14.5196 8.10536 14.7071 8.29289C14.8946 8.48043 15 8.73478 15 9V19C15 19.2652 14.8946 19.5196 14.7071 19.7071C14.5196 19.8946 14.2652 20 14 20H10C9.73478 20 9.48043 19.8946 9.29289 19.7071C9.10536 19.5196 9 19.2652 9 19V9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 5C15 4.73478 15.1054 4.48043 15.2929 4.29289C15.4804 4.10536 15.7348 4 16 4H20C20.2652 4 20.5196 4.10536 20.7071 4.29289C20.8946 4.48043 21 4.73478 21 5V19C21 19.2652 20.8946 19.5196 20.7071 19.7071C20.5196 19.8946 20.2652 20 20 20H16C15.7348 20 15.4804 19.8946 15.2929 19.7071C15.1054 19.5196 15 19.2652 15 19V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 20H18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_7039_175631"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Evaluations</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Measure model quality</p></div></div></a><link rel="prefetch" href="/evaluations"/></li></ul><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec71b:e4519510-df79-e08b-0573-66303879d781" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="e4519510-df79-e08b-0573-66303879d781" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec71b%22%7D%5D" href="/models" class="navbar-dropdown_side-box w-inline-block"><div class="navbar-dropdown_models-cta"><div class="navbar-dropdown_models-visual"><div class="navbar-dropdown_models-box"><div class="navbar-dropdown_models-row cc-1"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94d01ca8c3f35a76882_deepseek.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">DeepSeek V3.1</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715f769d5a7881d0a08_ZAI.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">GLM 5 FP4</div></div></div></div><div class="navbar-dropdown_models-row cc-2"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715728a41f2c0fc8af1_Qwen.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Qwen3-VL 32B</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94df75d5951f9db7060_open-ai.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">gpt-oss-120b</div></div></div></div><div class="navbar-dropdown_models-row cc-3"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94db9b8ff9451666717_kimi.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">kimi k2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a7158f5344d60ec5e323_Meta.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Llama 4 Maverick</div></div></div></div></div></div><div><p class="body-m text-weight-medium">Model library</p><p class="body-s">Fine-tune top open-source models</p></div></div></a><link rel="prefetch" href="/models"/></div></div></div></li><li data-accordion-status="not-active" data-dropdown-trigger="research" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec71d" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec71d" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Research</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e80c:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80c%22%7D%5D" href="/research" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="research" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179598)"><path d="M5 21H19" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 18H8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 18V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 11L12 14L18 8L15 5L9 11Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10.5 12.5L9 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 3L20 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 20.9991C13.247 20.9992 14.4631 20.6108 15.4791 19.8878C16.4952 19.1648 17.2607 18.1433 17.6693 16.9651C18.0779 15.7869 18.1093 14.5107 17.759 13.3139C17.4088 12.1171 16.6943 11.0591 15.715 10.2871" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179598"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Research</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Systems research for production AI</p></div></div></a><link rel="prefetch" href="/research"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:4c983918-2f0c-c63d-13f5-383f66bfd32e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%224c983918-2f0c-c63d-13f5-383f66bfd32e%22%7D%5D" href="/research-blog" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="news" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179599)"><path d="M16 6H19C19.2652 6 19.5196 6.10536 19.7071 6.29289C19.8946 6.48043 20 6.73478 20 7V18C20 18.5304 19.7893 19.0391 19.4142 19.4142C19.0391 19.7893 18.5304 20 18 20M18 20C17.4696 20 16.9609 19.7893 16.5858 19.4142C16.2107 19.0391 16 18.5304 16 18V5C16 4.73478 15.8946 4.48043 15.7071 4.29289C15.5196 4.10536 15.2652 4 15 4H5C4.73478 4 4.48043 4.10536 4.29289 4.29289C4.10536 4.48043 4 4.73478 4 5V17C4 17.7956 4.31607 18.5587 4.87868 19.1213C5.44129 19.6839 6.20435 20 7 20H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 8H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 12H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179599"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Research blog</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">All our research publications</p></div></div></a><link rel="prefetch" href="/research-blog"/></li></ul><div class="w-layout-vflex navbar-dropdown_side-box"><div class="opacity-60"><p class="caption-s">Featured publications</p></div><ul role="list" class="cc-list-8 is-menu-publications"><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e818" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e818" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%5D" href="/blog/flashattention-3" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">FlashAttention</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/blog/flashattention-3"/></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e81f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e81f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%5D" href="/blog/adaptive-learning-speculator-system-atlas" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">ATLAS</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e826" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e826" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%5D" href="/blog/nvidia-hgx-b200-with-together-kernel-collection" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">Kernel Collection</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e82d" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e82d" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%5D" href="/blog/thunderkittens" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">ThunderKittens</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e834" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e834" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%5D" href="/blog/dsgym" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">DSGym</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul><a data-button-instance="" data-wf--button--style-size="base" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec723:ac88cb09-7713-361e-8322-35dfd968e83a:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec723%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e83a%22%7D%5D" href="/research-blog" class="btn w-inline-block is-link"><div data-button-text="" class="btn-text">Show all</div><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></a><link rel="prefetch" href="/research-blog"/></div></div></div></div></li><li data-accordion-status="not-active" data-dropdown-trigger="developers" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec725" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec725" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Developers</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3e9:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e9%22%7D%5D" href="https://docs.together.ai/" target="_blank" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="documentation" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179600)"><path d="M5 5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V19C19 19.5304 18.7893 20.0391 18.4142 20.4142C18.0391 20.7893 17.5304 21 17 21H7C6.46957 21 5.96086 20.7893 5.58579 20.4142C5.21071 20.0391 5 19.5304 5 19V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 7H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 11H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 15H13" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179600"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Documentation</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Technical docs for Together AI</p></div></div></a><link rel="prefetch" href="https://docs.together.ai/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3ec:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3ec%22%7D%5D" href="/demos" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="demos" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179601)"><path d="M4 5C4 4.73478 4.10536 4.48043 4.29289 4.29289C4.48043 4.10536 4.73478 4 5 4H9C9.26522 4 9.51957 4.10536 9.70711 4.29289C9.89464 4.48043 10 4.73478 10 5V9C10 9.26522 9.89464 9.51957 9.70711 9.70711C9.51957 9.89464 9.26522 10 9 10H5C4.73478 10 4.48043 9.89464 4.29289 9.70711C4.10536 9.51957 4 9.26522 4 9V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 15C4 14.7348 4.10536 14.4804 4.29289 14.2929C4.48043 14.1054 4.73478 14 5 14H9C9.26522 14 9.51957 14.1054 9.70711 14.2929C9.89464 14.4804 10 14.7348 10 15V19C10 19.2652 9.89464 19.5196 9.70711 19.7071C9.51957 19.8946 9.26522 20 9 20H5C4.73478 20 4.48043 19.8946 4.29289 19.7071C4.10536 19.5196 4 19.2652 4 19V15Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 15C14 14.7348 14.1054 14.4804 14.2929 14.2929C14.4804 14.1054 14.7348 14 15 14H19C19.2652 14 19.5196 14.1054 19.7071 14.2929C19.8946 14.4804 20 14.7348 20 15V19C20 19.2652 19.8946 19.5196 19.7071 19.7071C19.5196 19.8946 19.2652 20 19 20H15C14.7348 20 14.4804 19.8946 14.2929 19.7071C14.1054 19.5196 14 19.2652 14 19V15Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 7H20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 4V10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179601"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Demos</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Our open-source demo apps</p></div></div></a><link rel="prefetch" href="/demos"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3ef:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3ef%22%7D%5D" href="/cookbooks" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="book" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179602)"><path d="M19 4V20H7C6.46957 20 5.96086 19.7893 5.58579 19.4142C5.21071 19.0391 5 18.5304 5 18V6C5 5.46957 5.21071 4.96086 5.58579 4.58579C5.96086 4.21071 6.46957 4 7 4H19Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M19 16H7C6.46957 16 5.96086 16.2107 5.58579 16.5858C5.21071 16.9609 5 17.4696 5 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 8H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179602"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Cookbooks</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Practical implementation guides</p></div></div></a><link rel="prefetch" href="/cookbooks"/></li></ul><div class="navbar-dropdown_side-box"><ul role="list" class="cc-list-16 is-menu-devs"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3f4:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f4%22%7D%5D" href="/models" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Model Library</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/models"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3f6:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f6%22%7D%5D" href="https://api.together.ai/playground/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Playground</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://api.together.ai/playground/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3f8:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f8%22%7D%5D" href="https://chat.together.ai/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Together Chat</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://chat.together.ai/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72b:050f4cfd-ff01-8955-763b-fd73ea80b3fa:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec72b%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3fa%22%7D%5D" href="https://whichllm.together.ai/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Which LLM to use</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://whichllm.together.ai/"/></li></ul></div></div></div></div></li><li data-accordion-status="not-active" data-dropdown-trigger="company" class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec72d" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec72d" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="#" class="nav-link w-inline-block"><p class="body-s">Company</p><div data-accordion-icon="" class="u-mt-1"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></a><div data-accordion-content="" class="nav-links_item-menu"><div class="nav-links_item-menu-inner"><div class="navbar-dropdown is-company"><div><div class="u-mb-16"><div class="opacity-60"><p class="caption-s">Resources</p></div></div><ul role="list" class="navbar-dropdown_list cc-no-padding"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:e5e1b890-6d35-70aa-8028-234a3266d022:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d022%22%7D%5D" href="/customers" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="blockquote" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179717)"><path d="M6 15H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M21 19H6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 11H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M21 7H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 9H10C10.1978 9 10.3911 9.05865 10.5556 9.16853C10.72 9.27841 10.8482 9.43459 10.9239 9.61732C10.9996 9.80004 11.0194 10.0011 10.9808 10.1951C10.9422 10.3891 10.847 10.5673 10.7071 10.7071C10.5673 10.847 10.3891 10.9422 10.1951 10.9808C10.0011 11.0194 9.80004 10.9996 9.61732 10.9239C9.43459 10.8482 9.27841 10.72 9.16853 10.5556C9.05865 10.3911 9 10.1978 9 10V7.5C9 6.96957 9.21071 6.46086 9.58579 6.08579C9.96086 5.71071 10.4696 5.5 11 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M3 9H4C4.19778 9 4.39112 9.05865 4.55557 9.16853C4.72002 9.27841 4.84819 9.43459 4.92388 9.61732C4.99957 9.80004 5.01937 10.0011 4.98079 10.1951C4.9422 10.3891 4.84696 10.5673 4.70711 10.7071C4.56725 10.847 4.38907 10.9422 4.19509 10.9808C4.00111 11.0194 3.80004 10.9996 3.61732 10.9239C3.43459 10.8482 3.27841 10.72 3.16853 10.5556C3.05865 10.3911 3 10.1978 3 10V7.5C3 6.96957 3.21071 6.46086 3.58579 6.08579C3.96086 5.71071 4.46957 5.5 5 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179717"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Customer stories</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Testimonials from AI Natives</p></div></div></a><link rel="prefetch" href="/customers"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:e5e1b890-6d35-70aa-8028-234a3266d025:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d025%22%7D%5D" href="/startup-accelerator" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="rocket" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179718)"><path d="M4 13C5.78309 13.2119 7.44305 14.0175 8.71276 15.2872C9.98247 16.557 10.7881 18.2169 11 20C11.8839 19.4904 12.6233 18.7638 13.1482 17.8889C13.6732 17.014 13.9663 16.0197 14 15C15.6791 14.4093 17.1454 13.334 18.2133 11.91C19.2813 10.486 19.9031 8.77734 20 7C20 6.20435 19.6839 5.44129 19.1213 4.87868C18.5587 4.31607 17.7956 4 17 4C15.2227 4.09691 13.514 4.71867 12.09 5.78665C10.666 6.85464 9.59069 8.32089 9 10C7.98026 10.0337 6.98596 10.3268 6.11106 10.8518C5.23617 11.3767 4.50959 12.1161 4 13Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6.9995 14C5.95873 14.5876 5.11716 15.4726 4.58266 16.5416C4.04816 17.6106 3.8451 18.8148 3.9995 20C5.18466 20.1544 6.38893 19.9513 7.45793 19.4168C8.52692 18.8823 9.41193 18.0408 9.99951 17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 9C14 9.26522 14.1054 9.51957 14.2929 9.70711C14.4804 9.89464 14.7348 10 15 10C15.2652 10 15.5196 9.89464 15.7071 9.70711C15.8946 9.51957 16 9.26522 16 9C16 8.73478 15.8946 8.48043 15.7071 8.29289C15.5196 8.10536 15.2652 8 15 8C14.7348 8 14.4804 8.10536 14.2929 8.29289C14.1054 8.48043 14 8.73478 14 9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179718"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Startup accelerator</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Build and scale your startup</p></div></div></a><link rel="prefetch" href="/startup-accelerator"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:e5e1b890-6d35-70aa-8028-234a3266d028:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d028%22%7D%5D" href="/support" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="chat" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179719)"><path d="M21 14L18 11H11C10.7348 11 10.4804 10.8946 10.2929 10.7071C10.1054 10.5196 10 10.2652 10 10V4C10 3.73478 10.1054 3.48043 10.2929 3.29289C10.4804 3.10536 10.7348 3 11 3H20C20.2652 3 20.5196 3.10536 20.7071 3.29289C20.8946 3.48043 21 3.73478 21 4V14Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 15V17C14 17.2652 13.8946 17.5196 13.7071 17.7071C13.5196 17.8946 13.2652 18 13 18H6L3 21V11C3 10.7348 3.10536 10.4804 3.29289 10.2929C3.48043 10.1054 3.73478 10 4 10H6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179719"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Customer support</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Find answers to your questions</p></div></div></a><link rel="prefetch" href="/support"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:ddc1bcf4-b90c-e1f5-c25f-59b24314eaaf:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22ddc1bcf4-b90c-e1f5-c25f-59b24314eaaf%22%7D%5D" href="/blog" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="news" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179599)"><path d="M16 6H19C19.2652 6 19.5196 6.10536 19.7071 6.29289C19.8946 6.48043 20 6.73478 20 7V18C20 18.5304 19.7893 19.0391 19.4142 19.4142C19.0391 19.7893 18.5304 20 18 20M18 20C17.4696 20 16.9609 19.7893 16.5858 19.4142C16.2107 19.0391 16 18.5304 16 18V5C16 4.73478 15.8946 4.48043 15.7071 4.29289C15.5196 4.10536 15.2652 4 15 4H5C4.73478 4 4.48043 4.10536 4.29289 4.29289C4.10536 4.48043 4 4.73478 4 5V17C4 17.7956 4.31607 18.5587 4.87868 19.1213C5.44129 19.6839 6.20435 20 7 20H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 8H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 12H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179599"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Blog</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Our latest news &amp; blog posts</p></div></div></a><link rel="prefetch" href="/blog"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:b7e190c9-fefb-9900-4ef1-a6cc3c954f02:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22b7e190c9-fefb-9900-4ef1-a6cc3c954f02%22%7D%5D" href="/events" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="calendar" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179721)"><path d="M16 3V7M8 3V7M4 11H20M4 7C4 6.46957 4.21071 5.96086 4.58579 5.58579C4.96086 5.21071 5.46957 5 6 5H18C18.5304 5 19.0391 5.21071 19.4142 5.58579C19.7893 5.96086 20 6.46957 20 7V19C20 19.5304 19.7893 20.0391 19.4142 20.4142C19.0391 20.7893 18.5304 21 18 21H6C5.46957 21 4.96086 20.7893 4.58579 20.4142C4.21071 20.0391 4 19.5304 4 19V7Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179721"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Events</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Explore our events calendar</p></div></div></a><link rel="prefetch" href="/events"/></li></ul></div><div><div class="u-mb-16"><div class="opacity-60"><p class="caption-s">Company</p></div></div><ul role="list" class="navbar-dropdown_list cc-no-padding"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:e5e1b890-6d35-70aa-8028-234a3266d031:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d031%22%7D%5D" href="/about-us" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="chat-smile" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179722)"><path d="M18 4C18.7956 4 19.5587 4.31607 20.1213 4.87868C20.6839 5.44129 21 6.20435 21 7V15C21 15.7956 20.6839 16.5587 20.1213 17.1213C19.5587 17.6839 18.7956 18 18 18H13L8 21V18H6C5.20435 18 4.44129 17.6839 3.87868 17.1213C3.31607 16.5587 3 15.7956 3 15V7C3 6.20435 3.31607 5.44129 3.87868 4.87868C4.44129 4.31607 5.20435 4 6 4H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.5 9H9.51" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 9H14.51" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.5 13C9.82588 13.3326 10.2148 13.5968 10.6441 13.7772C11.0734 13.9576 11.5344 14.0505 12 14.0505C12.4656 14.0505 12.9266 13.9576 13.3559 13.7772C13.7852 13.5968 14.1741 13.3326 14.5 13" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179722"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">About</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Get to know us</p></div></div></a><link rel="prefetch" href="/about-us"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec733:e5e1b890-6d35-70aa-8028-234a3266d034:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec733%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d034%22%7D%5D" href="/careers" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="briefcase" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179723)"><path d="M3 9C3 8.46957 3.21071 7.96086 3.58579 7.58579C3.96086 7.21071 4.46957 7 5 7H19C19.5304 7 20.0391 7.21071 20.4142 7.58579C20.7893 7.96086 21 8.46957 21 9V18C21 18.5304 20.7893 19.0391 20.4142 19.4142C20.0391 19.7893 19.5304 20 19 20H5C4.46957 20 3.96086 19.7893 3.58579 19.4142C3.21071 19.0391 3 18.5304 3 18V9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 7V5C8 4.46957 8.21071 3.96086 8.58579 3.58579C8.96086 3.21071 9.46957 3 10 3H14C14.5304 3 15.0391 3.21071 15.4142 3.58579C15.7893 3.96086 16 4.46957 16 5V7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179723"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Careers</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Join our mission</p></div></div></a><link rel="prefetch" href="/careers"/></li></ul></div></div></div></div></li><li class="nav-links_item"><a data-accordion-toggle="" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec735" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="b446826c-b6e7-4fa6-5f43-6bf81f2ec735" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%5D" href="/pricing" class="nav-link w-inline-block"><p class="body-s">Pricing</p></a></li></ul><ul role="list" class="nav-dropdowns"><li data-dropdown-target="inference" class="nav-dropdowns_item"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73a:cfad3a49-6163-a5dd-9141-338a5187287f:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73a%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287f%22%7D%5D" href="/serverless-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="cloud" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180035)"><path d="M6.657 17.9999C4.085 17.9999 2 15.9929 2 13.5169C2 11.0419 4.085 9.03488 6.657 9.03488C7.05 7.27288 8.451 5.83488 10.332 5.26188C12.212 4.68988 14.288 5.06888 15.776 6.26188C17.264 7.45188 17.938 9.26888 17.546 11.0309H18.536C20.449 11.0309 22 12.5909 22 14.5169C22 16.4439 20.449 18.0039 18.535 18.0039H6.657" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180035"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Serverless Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">High-performance inference as APIs</p></div></div></a><link rel="prefetch" href="/serverless-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73a:cfad3a49-6163-a5dd-9141-338a51872882:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73a%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872882%22%7D%5D" href="/batch-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="stack" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180061)"><path d="M12 4L4 8L12 12L20 8L12 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L12 16L20 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 16L12 20L20 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180061"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Batch Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference for batch workloads</p></div></div></a><link rel="prefetch" href="/batch-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73a:cfad3a49-6163-a5dd-9141-338a51872885:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73a%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872885%22%7D%5D" href="/dedicated-model-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="dedicated-endpoints" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180037)"><path d="M6.657 15.9999C4.085 15.9999 2 13.9929 2 11.5169C2 9.04188 4.085 7.03488 6.657 7.03488C7.05 5.27288 8.451 3.83488 10.332 3.26188C12.212 2.68988 14.288 3.06888 15.776 4.26188C17.264 5.45188 17.938 7.26888 17.546 9.03088H18.536C20.449 9.03088 22 10.5909 22 12.5169C22 14.4439 20.449 16.0039 18.535 16.0039H6.657" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 16V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16 16V20C16 20.2652 16.1054 20.5196 16.2929 20.7071C16.4804 20.8946 16.7348 21 17 21H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16V20C8 20.2652 7.89464 20.5196 7.70711 20.7071C7.51957 20.8946 7.26522 21 7 21H3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180037"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Dedicated Model Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference on custom hardware</p></div></div></a><link rel="prefetch" href="/dedicated-model-inference"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73a:cfad3a49-6163-a5dd-9141-338a51872888:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73a%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a51872888%22%7D%5D" href="/dedicated-container-inference" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="cyan-light" class="menu-icon w-variant-3a9b14fb-fbc9-ae56-ff87-d42ea628ab99"><div data-wf--product-icons--icon="container" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180038)"><path d="M12 3L20 7.5V16.5L12 21L4 16.5V7.5L12 3Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L20 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L4 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180038"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Dedicated Container Inference</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Inference for custom models</p></div></div></a><link rel="prefetch" href="/dedicated-container-inference"/></li></ul><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73a:cfad3a49-6163-a5dd-9141-338a5187288b:1d56cce1-fb54-e7b7-1ed5-1940190ef0d4" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="1d56cce1-fb54-e7b7-1ed5-1940190ef0d4" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187287d%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73a%22%7D%2C%7B%22componentId%22%3A%221d56cce1-fb54-e7b7-1ed5-1940190ef0d4%22%2C%22instanceId%22%3A%22cfad3a49-6163-a5dd-9141-338a5187288b%22%7D%5D" href="/models" class="navbar-dropdown_side-box w-inline-block"><div class="navbar-dropdown_models-cta"><div class="navbar-dropdown_models-visual"><div class="navbar-dropdown_models-box"><div class="navbar-dropdown_models-row cc-1"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715c615c4883c5b0a7b_minimax.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">MiniMax M2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6994e2f1daa0c6879cc689b2_google.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Nano Banana Pro</div></div></div></div><div class="navbar-dropdown_models-row cc-2"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715728a41f2c0fc8af1_Qwen.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Qwen3.5-397B</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715f769d5a7881d0a08_ZAI.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">GLM-5</div></div></div></div><div class="navbar-dropdown_models-row cc-3"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94db9b8ff9451666717_kimi.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">kimi k2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94df75d5951f9db7060_open-ai.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">gpt-oss-120B</div></div></div></div></div></div><div><p class="body-m text-weight-medium">Model library</p><p class="body-s">Explore the top open-source models</p></div></div></a><link rel="prefetch" href="/models"/></div></li><li data-dropdown-target="compute" class="nav-dropdowns_item"><div class="navbar-dropdown"><div class="navbar-dropdown_sections"><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Accelerated Compute</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b99a:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b99a%22%7D%5D" href="/gpu-clusters" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="gpu" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_7040_158249)"><path d="M4 8.00195C4 7.2063 4.31607 6.44324 4.87868 5.88063C5.44129 5.31802 6.20435 5.00195 7 5.00195H17C17.7956 5.00195 18.5587 5.31802 19.1213 5.88063C19.6839 6.44324 20 7.2063 20 8.00195L21 15.9993V16.9993C21 17.795 20.6839 18.558 20.1213 19.1206C19.5587 19.6833 18.7956 19.9993 18 19.9993H6C5.20435 19.9993 4.44129 19.6833 3.87868 19.1206C3.31607 18.558 3 17.795 3 16.9993V15.9993L4 8.00195Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L20 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 16V16.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 17V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_7040_158249"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">GPU Clusters</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Reliable GPU clusters at scale</p></div></div></a><link rel="prefetch" href="/gpu-clusters"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b99e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b99e%22%7D%5D" href="/ai-factory" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="clusters" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180039)"><path d="M3 17C3 16.4696 3.21071 15.9609 3.58579 15.5858C3.96086 15.2107 4.46957 15 5 15H7C7.53043 15 8.03914 15.2107 8.41421 15.5858C8.78929 15.9609 9 16.4696 9 17V19C9 19.5304 8.78929 20.0391 8.41421 20.4142C8.03914 20.7893 7.53043 21 7 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V17Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 17C15 16.4696 15.2107 15.9609 15.5858 15.5858C15.9609 15.2107 16.4696 15 17 15H19C19.5304 15 20.0391 15.2107 20.4142 15.5858C20.7893 15.9609 21 16.4696 21 17V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H17C16.4696 21 15.9609 20.7893 15.5858 20.4142C15.2107 20.0391 15 19.5304 15 19V17Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 5C9 4.46957 9.21071 3.96086 9.58579 3.58579C9.96086 3.21071 10.4696 3 11 3H13C13.5304 3 14.0391 3.21071 14.4142 3.58579C14.7893 3.96086 15 4.46957 15 5V7C15 7.53043 14.7893 8.03914 14.4142 8.41421C14.0391 8.78929 13.5304 9 13 9H11C10.4696 9 9.96086 8.78929 9.58579 8.41421C9.21071 8.03914 9 7.53043 9 7V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 15V14C6 13.4696 6.21071 12.9609 6.58579 12.5858C6.96086 12.2107 7.46957 12 8 12H16C16.5304 12 17.0391 12.2107 17.4142 12.5858C17.7893 12.9609 18 13.4696 18 14V15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 9V12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180039"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">AI Factory</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Custom infrastructure at frontier scale</p></div></div></a><link rel="prefetch" href="/ai-factory"/></li></ul></div><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Developer Environments</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:7c593527-d2e7-4e55-5ae7-d011eb1b15ea:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%227c593527-d2e7-4e55-5ae7-d011eb1b15ea%22%7D%5D" href="/sandbox" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="sandbox" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 32 32" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180041)"><path d="M20 7.5V16.5L16 18.75L12 21L8 18.75L4 16.5V7.5L8 5.25L12 3L16 5.25L20 7.5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L16 9.75L20 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 12L8 9.75L4 7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M20 12L16 14V18.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 12L8 14V18.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 5.25L12 7.5L16 5.25" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180041"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Sandbox</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Build development environments for AI</p></div></div></a><link rel="prefetch" href="/sandbox"/></li></ul></div><div class="navbar-dropdown_list-section"><div class="navbar-dropdown_list-label"><div class="opacity-60"><p class="caption-s">Storage</p></div></div><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:5859d0a5-3bbd-ecfb-d32a-e015aa9a7e35:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%225859d0a5-3bbd-ecfb-d32a-e015aa9a7e35%22%7D%5D" href="/managed-storage" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="blue" class="menu-icon"><div data-wf--product-icons--icon="folder" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180042)"><path d="M5 4H9L12 7H19C19.5304 7 20.0391 7.21071 20.4142 7.58579C20.7893 7.96086 21 8.46957 21 9V17C21 17.5304 20.7893 18.0391 20.4142 18.4142C20.0391 18.7893 19.5304 19 19 19H5C4.46957 19 3.96086 18.7893 3.58579 18.4142C3.21071 18.0391 3 17.5304 3 17V6C3 5.46957 3.21071 4.96086 3.58579 4.58579C3.96086 4.21071 4.46957 4 5 4Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180042"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Managed Storage</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Store model weights &amp; data securely</p></div></div></a><link rel="prefetch" href="/managed-storage"/></li></ul></div></div><div no-scrollbar="" class="navbar-dropdown_side-box"><ul role="list" class="cc-list-16 is-menu-gpu"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b9a4:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a4%22%7D%5D" href="/gpu/nvidia-gb300-nvl72" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">GB300</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-gb300-nvl72"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b9a6:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a6%22%7D%5D" href="/gpu/nvidia-gb200-nvl72" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">GB200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-gb200-nvl72"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b9a8:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9a8%22%7D%5D" href="/gpu/nvidia-hgx-b200" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">B200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-hgx-b200"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:f70f39c7-12a0-fcb8-a96c-b0761e04b9aa:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b9aa%22%7D%5D" href="/gpu/nvidia-h200" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">H200</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-h200"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73c:e660ced2-171d-c32b-3ba1-eb160450318d:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22f70f39c7-12a0-fcb8-a96c-b0761e04b998%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73c%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22e660ced2-171d-c32b-3ba1-eb160450318d%22%7D%5D" href="/gpu/nvidia-h100" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">H100</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/gpu/nvidia-h100"/></li></ul></div></div></li><li data-dropdown-target="model-shaping" class="nav-dropdowns_item"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73e:e4519510-df79-e08b-0573-66303879d77e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73e%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e4519510-df79-e08b-0573-66303879d77e%22%7D%5D" href="/fine-tuning" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="purple" class="menu-icon w-variant-90cf24ef-cc0e-eebd-76e9-8cb20dcc72fa"><div data-wf--product-icons--icon="fine-tuning" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_180043)"><path d="M4 10C4 10.5304 4.21071 11.0391 4.58579 11.4142C4.96086 11.7893 5.46957 12 6 12C6.53043 12 7.03914 11.7893 7.41421 11.4142C7.78929 11.0391 8 10.5304 8 10C8 9.46957 7.78929 8.96086 7.41421 8.58579C7.03914 8.21071 6.53043 8 6 8C5.46957 8 4.96086 8.21071 4.58579 8.58579C4.21071 8.96086 4 9.46957 4 10Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 4V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 12V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10 16C10 16.5304 10.2107 17.0391 10.5858 17.4142C10.9609 17.7893 11.4696 18 12 18C12.5304 18 13.0391 17.7893 13.4142 17.4142C13.7893 17.0391 14 16.5304 14 16C14 15.4696 13.7893 14.9609 13.4142 14.5858C13.0391 14.2107 12.5304 14 12 14C11.4696 14 10.9609 14.2107 10.5858 14.5858C10.2107 14.9609 10 15.4696 10 16Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 4V14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 18V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M16 7C16 7.53043 16.2107 8.03914 16.5858 8.41421C16.9609 8.78929 17.4696 9 18 9C18.5304 9 19.0391 8.78929 19.4142 8.41421C19.7893 8.03914 20 7.53043 20 7C20 6.46957 19.7893 5.96086 19.4142 5.58579C19.0391 5.21071 18.5304 5 18 5C17.4696 5 16.9609 5.21071 16.5858 5.58579C16.2107 5.96086 16 6.46957 16 7Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 4V5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M18 9V20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_180043"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Fine-Tuning</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Shape models with your data</p></div></div></a><link rel="prefetch" href="/fine-tuning"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73e:14dc301c-2c6d-15e9-5c67-5e034664b24f:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73e%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%2214dc301c-2c6d-15e9-5c67-5e034664b24f%22%7D%5D" href="/evaluations" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="purple" class="menu-icon w-variant-90cf24ef-cc0e-eebd-76e9-8cb20dcc72fa"><div data-wf--product-icons--icon="stats" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_7039_175631)"><path d="M3 13C3 12.7348 3.10536 12.4804 3.29289 12.2929C3.48043 12.1054 3.73478 12 4 12H8C8.26522 12 8.51957 12.1054 8.70711 12.2929C8.89464 12.4804 9 12.7348 9 13V19C9 19.2652 8.89464 19.5196 8.70711 19.7071C8.51957 19.8946 8.26522 20 8 20H4C3.73478 20 3.48043 19.8946 3.29289 19.7071C3.10536 19.5196 3 19.2652 3 19V13Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 9C9 8.73478 9.10536 8.48043 9.29289 8.29289C9.48043 8.10536 9.73478 8 10 8H14C14.2652 8 14.5196 8.10536 14.7071 8.29289C14.8946 8.48043 15 8.73478 15 9V19C15 19.2652 14.8946 19.5196 14.7071 19.7071C14.5196 19.8946 14.2652 20 14 20H10C9.73478 20 9.48043 19.8946 9.29289 19.7071C9.10536 19.5196 9 19.2652 9 19V9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 5C15 4.73478 15.1054 4.48043 15.2929 4.29289C15.4804 4.10536 15.7348 4 16 4H20C20.2652 4 20.5196 4.10536 20.7071 4.29289C20.8946 4.48043 21 4.73478 21 5V19C21 19.2652 20.8946 19.5196 20.7071 19.7071C20.5196 19.8946 20.2652 20 20 20H16C15.7348 20 15.4804 19.8946 15.2929 19.7071C15.1054 19.5196 15 19.2652 15 19V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 20H18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_7039_175631"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Evaluations</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Measure model quality</p></div></div></a><link rel="prefetch" href="/evaluations"/></li></ul><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec73e:e4519510-df79-e08b-0573-66303879d781" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="e4519510-df79-e08b-0573-66303879d781" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e4519510-df79-e08b-0573-66303879d77c%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec73e%22%7D%5D" href="/models" class="navbar-dropdown_side-box w-inline-block"><div class="navbar-dropdown_models-cta"><div class="navbar-dropdown_models-visual"><div class="navbar-dropdown_models-box"><div class="navbar-dropdown_models-row cc-1"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94d01ca8c3f35a76882_deepseek.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">DeepSeek V3.1</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715f769d5a7881d0a08_ZAI.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">GLM 5 FP4</div></div></div></div><div class="navbar-dropdown_models-row cc-2"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a715728a41f2c0fc8af1_Qwen.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Qwen3-VL 32B</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94df75d5951f9db7060_open-ai.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">gpt-oss-120b</div></div></div></div><div class="navbar-dropdown_models-row cc-3"><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/699cd94db9b8ff9451666717_kimi.png" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">kimi k2.5</div></div></div><div class="navbar-dropdown_models-tag"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a1a7158f5344d60ec5e323_Meta.svg" alt="" class="icon-24"/><div class="opacity-70"><div class="caption-s">Llama 4 Maverick</div></div></div></div></div></div><div><p class="body-m text-weight-medium">Model library</p><p class="body-s">Fine-tune top open-source models</p></div></div></a><link rel="prefetch" href="/models"/></div></li><li data-dropdown-target="research" class="nav-dropdowns_item"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e80c:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80c%22%7D%5D" href="/research" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="research" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179598)"><path d="M5 21H19" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6 18H8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7 18V21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 11L12 14L18 8L15 5L9 11Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10.5 12.5L9 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 3L20 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12 20.9991C13.247 20.9992 14.4631 20.6108 15.4791 19.8878C16.4952 19.1648 17.2607 18.1433 17.6693 16.9651C18.0779 15.7869 18.1093 14.5107 17.759 13.3139C17.4088 12.1171 16.6943 11.0591 15.715 10.2871" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179598"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Research</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Systems research for production AI</p></div></div></a><link rel="prefetch" href="/research"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:4c983918-2f0c-c63d-13f5-383f66bfd32e:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%224c983918-2f0c-c63d-13f5-383f66bfd32e%22%7D%5D" href="/research-blog" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="news" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179599)"><path d="M16 6H19C19.2652 6 19.5196 6.10536 19.7071 6.29289C19.8946 6.48043 20 6.73478 20 7V18C20 18.5304 19.7893 19.0391 19.4142 19.4142C19.0391 19.7893 18.5304 20 18 20M18 20C17.4696 20 16.9609 19.7893 16.5858 19.4142C16.2107 19.0391 16 18.5304 16 18V5C16 4.73478 15.8946 4.48043 15.7071 4.29289C15.5196 4.10536 15.2652 4 15 4H5C4.73478 4 4.48043 4.10536 4.29289 4.29289C4.10536 4.48043 4 4.73478 4 5V17C4 17.7956 4.31607 18.5587 4.87868 19.1213C5.44129 19.6839 6.20435 20 7 20H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 8H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 12H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179599"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Research blog</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">All our research publications</p></div></div></a><link rel="prefetch" href="/research-blog"/></li></ul><div class="w-layout-vflex navbar-dropdown_side-box"><div class="opacity-60"><p class="caption-s">Featured publications</p></div><ul role="list" class="cc-list-8 is-menu-publications"><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e818" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e818" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%5D" href="/blog/flashattention-3" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">FlashAttention</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/blog/flashattention-3"/></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e81f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e81f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%5D" href="/blog/adaptive-learning-speculator-system-atlas" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">ATLAS</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e826" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e826" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%5D" href="/blog/nvidia-hgx-b200-with-together-kernel-collection" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">Kernel Collection</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e82d" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e82d" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%5D" href="/blog/thunderkittens" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">ThunderKittens</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e834" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="ac88cb09-7713-361e-8322-35dfd968e834" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%5D" href="/blog/dsgym" class="navbar-dropdown_underline-link w-inline-block"><p class="body-m text-weight-medium">DSGym</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul><a data-button-instance="" data-wf--button--style-size="base" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec740:ac88cb09-7713-361e-8322-35dfd968e83a:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e80a%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec740%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22ac88cb09-7713-361e-8322-35dfd968e83a%22%7D%5D" href="/research-blog" class="btn w-inline-block is-link"><div data-button-text="" class="btn-text">Show all</div><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></a><link rel="prefetch" href="/research-blog"/></div></div></li><li data-dropdown-target="developers" class="nav-dropdowns_item"><div class="navbar-dropdown"><ul role="list" class="navbar-dropdown_list"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3e9:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e9%22%7D%5D" href="https://docs.together.ai/" target="_blank" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="documentation" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179600)"><path d="M5 5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V19C19 19.5304 18.7893 20.0391 18.4142 20.4142C18.0391 20.7893 17.5304 21 17 21H7C6.46957 21 5.96086 20.7893 5.58579 20.4142C5.21071 20.0391 5 19.5304 5 19V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 7H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 11H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 15H13" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179600"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Documentation</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Technical docs for Together AI</p></div></div></a><link rel="prefetch" href="https://docs.together.ai/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3ec:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3ec%22%7D%5D" href="/demos" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="demos" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179601)"><path d="M4 5C4 4.73478 4.10536 4.48043 4.29289 4.29289C4.48043 4.10536 4.73478 4 5 4H9C9.26522 4 9.51957 4.10536 9.70711 4.29289C9.89464 4.48043 10 4.73478 10 5V9C10 9.26522 9.89464 9.51957 9.70711 9.70711C9.51957 9.89464 9.26522 10 9 10H5C4.73478 10 4.48043 9.89464 4.29289 9.70711C4.10536 9.51957 4 9.26522 4 9V5Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M4 15C4 14.7348 4.10536 14.4804 4.29289 14.2929C4.48043 14.1054 4.73478 14 5 14H9C9.26522 14 9.51957 14.1054 9.70711 14.2929C9.89464 14.4804 10 14.7348 10 15V19C10 19.2652 9.89464 19.5196 9.70711 19.7071C9.51957 19.8946 9.26522 20 9 20H5C4.73478 20 4.48043 19.8946 4.29289 19.7071C4.10536 19.5196 4 19.2652 4 19V15Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 15C14 14.7348 14.1054 14.4804 14.2929 14.2929C14.4804 14.1054 14.7348 14 15 14H19C19.2652 14 19.5196 14.1054 19.7071 14.2929C19.8946 14.4804 20 14.7348 20 15V19C20 19.2652 19.8946 19.5196 19.7071 19.7071C19.5196 19.8946 19.2652 20 19 20H15C14.7348 20 14.4804 19.8946 14.2929 19.7071C14.1054 19.5196 14 19.2652 14 19V15Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 7H20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 4V10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179601"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Demos</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Our open-source demo apps</p></div></div></a><link rel="prefetch" href="/demos"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3ef:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3ef%22%7D%5D" href="/cookbooks" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="book" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179602)"><path d="M19 4V20H7C6.46957 20 5.96086 19.7893 5.58579 19.4142C5.21071 19.0391 5 18.5304 5 18V6C5 5.46957 5.21071 4.96086 5.58579 4.58579C5.96086 4.21071 6.46957 4 7 4H19Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M19 16H7C6.46957 16 5.96086 16.2107 5.58579 16.5858C5.21071 16.9609 5 17.4696 5 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 8H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179602"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Cookbooks</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Practical implementation guides</p></div></div></a><link rel="prefetch" href="/cookbooks"/></li></ul><div class="navbar-dropdown_side-box"><ul role="list" class="cc-list-16 is-menu-devs"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3f4:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f4%22%7D%5D" href="/models" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Model Library</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="/models"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3f6:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f6%22%7D%5D" href="https://api.together.ai/playground/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Playground</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://api.together.ai/playground/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3f8:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3f8%22%7D%5D" href="https://chat.together.ai/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Together Chat</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://chat.together.ai/"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec742:050f4cfd-ff01-8955-763b-fd73ea80b3fa:0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="0cc78d56-f208-b2fa-59a6-286c39491f1b" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3e7%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec742%22%7D%2C%7B%22componentId%22%3A%220cc78d56-f208-b2fa-59a6-286c39491f1a%22%2C%22instanceId%22%3A%22050f4cfd-ff01-8955-763b-fd73ea80b3fa%22%7D%5D" href="https://whichllm.together.ai/" target="_blank" class="navbar-dropdown_secondary-link w-inline-block"><p class="body-s">Which LLM to use</p><div link-icon="external" class="opacity-50"><div data-transition="icon" class="icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6.96875 17.0547L16.9688 7.05469M16.9688 7.05469H6.96875M16.9688 7.05469V17.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a><link rel="prefetch" href="https://whichllm.together.ai/"/></li></ul></div></div></li><li data-dropdown-target="company" class="nav-dropdowns_item"><div class="navbar-dropdown is-company"><div><div class="u-mb-16"><div class="opacity-60"><p class="caption-s">Resources</p></div></div><ul role="list" class="navbar-dropdown_list cc-no-padding"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:e5e1b890-6d35-70aa-8028-234a3266d022:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d022%22%7D%5D" href="/customers" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="blockquote" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179717)"><path d="M6 15H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M21 19H6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 11H21" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M21 7H15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9 9H10C10.1978 9 10.3911 9.05865 10.5556 9.16853C10.72 9.27841 10.8482 9.43459 10.9239 9.61732C10.9996 9.80004 11.0194 10.0011 10.9808 10.1951C10.9422 10.3891 10.847 10.5673 10.7071 10.7071C10.5673 10.847 10.3891 10.9422 10.1951 10.9808C10.0011 11.0194 9.80004 10.9996 9.61732 10.9239C9.43459 10.8482 9.27841 10.72 9.16853 10.5556C9.05865 10.3911 9 10.1978 9 10V7.5C9 6.96957 9.21071 6.46086 9.58579 6.08579C9.96086 5.71071 10.4696 5.5 11 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M3 9H4C4.19778 9 4.39112 9.05865 4.55557 9.16853C4.72002 9.27841 4.84819 9.43459 4.92388 9.61732C4.99957 9.80004 5.01937 10.0011 4.98079 10.1951C4.9422 10.3891 4.84696 10.5673 4.70711 10.7071C4.56725 10.847 4.38907 10.9422 4.19509 10.9808C4.00111 11.0194 3.80004 10.9996 3.61732 10.9239C3.43459 10.8482 3.27841 10.72 3.16853 10.5556C3.05865 10.3911 3 10.1978 3 10V7.5C3 6.96957 3.21071 6.46086 3.58579 6.08579C3.96086 5.71071 4.46957 5.5 5 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179717"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Customer stories</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Testimonials from AI Natives</p></div></div></a><link rel="prefetch" href="/customers"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:e5e1b890-6d35-70aa-8028-234a3266d025:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d025%22%7D%5D" href="/startup-accelerator" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="rocket" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179718)"><path d="M4 13C5.78309 13.2119 7.44305 14.0175 8.71276 15.2872C9.98247 16.557 10.7881 18.2169 11 20C11.8839 19.4904 12.6233 18.7638 13.1482 17.8889C13.6732 17.014 13.9663 16.0197 14 15C15.6791 14.4093 17.1454 13.334 18.2133 11.91C19.2813 10.486 19.9031 8.77734 20 7C20 6.20435 19.6839 5.44129 19.1213 4.87868C18.5587 4.31607 17.7956 4 17 4C15.2227 4.09691 13.514 4.71867 12.09 5.78665C10.666 6.85464 9.59069 8.32089 9 10C7.98026 10.0337 6.98596 10.3268 6.11106 10.8518C5.23617 11.3767 4.50959 12.1161 4 13Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M6.9995 14C5.95873 14.5876 5.11716 15.4726 4.58266 16.5416C4.04816 17.6106 3.8451 18.8148 3.9995 20C5.18466 20.1544 6.38893 19.9513 7.45793 19.4168C8.52692 18.8823 9.41193 18.0408 9.99951 17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 9C14 9.26522 14.1054 9.51957 14.2929 9.70711C14.4804 9.89464 14.7348 10 15 10C15.2652 10 15.5196 9.89464 15.7071 9.70711C15.8946 9.51957 16 9.26522 16 9C16 8.73478 15.8946 8.48043 15.7071 8.29289C15.5196 8.10536 15.2652 8 15 8C14.7348 8 14.4804 8.10536 14.2929 8.29289C14.1054 8.48043 14 8.73478 14 9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179718"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Startup accelerator</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Build and scale your startup</p></div></div></a><link rel="prefetch" href="/startup-accelerator"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:e5e1b890-6d35-70aa-8028-234a3266d028:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d028%22%7D%5D" href="/support" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="chat" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179719)"><path d="M21 14L18 11H11C10.7348 11 10.4804 10.8946 10.2929 10.7071C10.1054 10.5196 10 10.2652 10 10V4C10 3.73478 10.1054 3.48043 10.2929 3.29289C10.4804 3.10536 10.7348 3 11 3H20C20.2652 3 20.5196 3.10536 20.7071 3.29289C20.8946 3.48043 21 3.73478 21 4V14Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14 15V17C14 17.2652 13.8946 17.5196 13.7071 17.7071C13.5196 17.8946 13.2652 18 13 18H6L3 21V11C3 10.7348 3.10536 10.4804 3.29289 10.2929C3.48043 10.1054 3.73478 10 4 10H6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179719"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Customer support</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Find answers to your questions</p></div></div></a><link rel="prefetch" href="/support"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:ddc1bcf4-b90c-e1f5-c25f-59b24314eaaf:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22ddc1bcf4-b90c-e1f5-c25f-59b24314eaaf%22%7D%5D" href="/blog" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="news" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179599)"><path d="M16 6H19C19.2652 6 19.5196 6.10536 19.7071 6.29289C19.8946 6.48043 20 6.73478 20 7V18C20 18.5304 19.7893 19.0391 19.4142 19.4142C19.0391 19.7893 18.5304 20 18 20M18 20C17.4696 20 16.9609 19.7893 16.5858 19.4142C16.2107 19.0391 16 18.5304 16 18V5C16 4.73478 15.8946 4.48043 15.7071 4.29289C15.5196 4.10536 15.2652 4 15 4H5C4.73478 4 4.48043 4.10536 4.29289 4.29289C4.10536 4.48043 4 4.73478 4 5V17C4 17.7956 4.31607 18.5587 4.87868 19.1213C5.44129 19.6839 6.20435 20 7 20H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 8H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 12H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 16H12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179599"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Blog</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Our latest news &amp; blog posts</p></div></div></a><link rel="prefetch" href="/blog"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:b7e190c9-fefb-9900-4ef1-a6cc3c954f02:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22b7e190c9-fefb-9900-4ef1-a6cc3c954f02%22%7D%5D" href="/events" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="calendar" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179721)"><path d="M16 3V7M8 3V7M4 11H20M4 7C4 6.46957 4.21071 5.96086 4.58579 5.58579C4.96086 5.21071 5.46957 5 6 5H18C18.5304 5 19.0391 5.21071 19.4142 5.58579C19.7893 5.96086 20 6.46957 20 7V19C20 19.5304 19.7893 20.0391 19.4142 20.4142C19.0391 20.7893 18.5304 21 18 21H6C5.46957 21 4.96086 20.7893 4.58579 20.4142C4.21071 20.0391 4 19.5304 4 19V7Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179721"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Events</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Explore our events calendar</p></div></div></a><link rel="prefetch" href="/events"/></li></ul></div><div><div class="u-mb-16"><div class="opacity-60"><p class="caption-s">Company</p></div></div><ul role="list" class="navbar-dropdown_list cc-no-padding"><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:e5e1b890-6d35-70aa-8028-234a3266d031:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d031%22%7D%5D" href="/about-us" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="chat-smile" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179722)"><path d="M18 4C18.7956 4 19.5587 4.31607 20.1213 4.87868C20.6839 5.44129 21 6.20435 21 7V15C21 15.7956 20.6839 16.5587 20.1213 17.1213C19.5587 17.6839 18.7956 18 18 18H13L8 21V18H6C5.20435 18 4.44129 17.6839 3.87868 17.1213C3.31607 16.5587 3 15.7956 3 15V7C3 6.20435 3.31607 5.44129 3.87868 4.87868C4.44129 4.31607 5.20435 4 6 4H18Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.5 9H9.51" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 9H14.51" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M9.5 13C9.82588 13.3326 10.2148 13.5968 10.6441 13.7772C11.0734 13.9576 11.5344 14.0505 12 14.0505C12.4656 14.0505 12.9266 13.9576 13.3559 13.7772C13.7852 13.5968 14.1741 13.3326 14.5 13" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179722"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">About</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Get to know us</p></div></div></a><link rel="prefetch" href="/about-us"/></li><li class="display-flex"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec744:e5e1b890-6d35-70aa-8028-234a3266d034:728663b5-8f88-233f-4293-b1cb5541705f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="728663b5-8f88-233f-4293-b1cb5541705f" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d01b%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec744%22%7D%2C%7B%22componentId%22%3A%22728663b5-8f88-233f-4293-b1cb5541705e%22%2C%22instanceId%22%3A%22e5e1b890-6d35-70aa-8028-234a3266d034%22%7D%5D" href="/careers" class="navbar-dropdown_link-item w-inline-block"><div data-transition="" data-wf--menu-icon--theme="grey" class="menu-icon w-variant-67101a7d-70b2-277d-868a-57cce3f850ec"><div data-wf--product-icons--icon="briefcase" class="flex-center icon-24"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><g clip-path="url(#clip0_6957_179723)"><path d="M3 9C3 8.46957 3.21071 7.96086 3.58579 7.58579C3.96086 7.21071 4.46957 7 5 7H19C19.5304 7 20.0391 7.21071 20.4142 7.58579C20.7893 7.96086 21 8.46957 21 9V18C21 18.5304 20.7893 19.0391 20.4142 19.4142C20.0391 19.7893 19.5304 20 19 20H5C4.46957 20 3.96086 19.7893 3.58579 19.4142C3.21071 19.0391 3 18.5304 3 18V9Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M8 7V5C8 4.46957 8.21071 3.96086 8.58579 3.58579C8.96086 3.21071 9.46957 3 10 3H14C14.5304 3 15.0391 3.21071 15.4142 3.58579C15.7893 3.96086 16 4.46957 16 5V7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></g><defs><clippath id="clip0_6957_179723"><rect width="24" height="24" fill="currentColor"></rect></clippath></defs></svg></div></div><div><div class="cc-meta-4"><p class="body-s text-weight-medium">Careers</p><div link-icon="arrow-fade"><div data-transition="icon" class="flex-center arrow-right icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div><div class="opacity-70"><p class="body-s">Join our mission</p></div></div></a><link rel="prefetch" href="/careers"/></li></ul></div></div></li></ul><div class="nav-menu-cta"><a data-button-instance="" data-wf--button--style-size="base" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec746:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec746%22%7D%5D" href="/contact-sales" class="btn w-inline-block is-secondary"><div data-button-text="" class="btn-text">Contact sales</div></a></div></div></div><div class="nav-hinge"><div class="no-flex"><div data-wf--hinge--variant="hinge-menu" class="hinge w-variant-89659887-e41a-12b4-ba4c-d5f3f366dbf0"></div></div></div><div class="nav-box cc-small"><div class="hide-tablet flex-center"><a data-button-instance="" data-wf--button--style-size="small" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec74d:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec74d%22%7D%5D" href="/contact-sales" class="btn w-variant-85cfe87b-cfff-abb5-c215-c683403bb90c w-inline-block is-link"><div data-button-text="" class="btn-text">Contact sales</div></a></div><a data-wf--button--style-size="small" class="btn w-variant-85cfe87b-cfff-abb5-c215-c683403bb90c w-inline-block" data-wf-component-context="%5B%7B%22componentId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec6ef%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be54134%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22b446826c-b6e7-4fa6-5f43-6bf81f2ec74f%22%7D%5D" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" href="https://api.together.ai/" data-button-instance="" target="_blank" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54134:b446826c-b6e7-4fa6-5f43-6bf81f2ec74f:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true"><div data-button-text="" class="btn-text">Sign in</div></a><div data-scroll="toggle" data-nav-menu="trigger" class="nav-ham"><div data-transition="" class="nav-ham_line"></div><div data-transition="" class="nav-ham_line"></div></div></div></nav></div><main class="main-wrapper"><section class="blog-detail"><div class="container-large"><div class="blog-detail_wrap"><div class="max-width-1004"><div class="u-mb-48"><a data-button-instance="" data-wf--button--style-size="base" data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be5413b:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%226fa8cc8f-b8b7-1037-6069-b6cd0be5413b%22%7D%5D" href="/blog" class="btn w-inline-block is-link"><div data-button-text="" class="btn-text">All blog posts</div></a></div><div class="u-mb-16"><div class="cc-meta-16"><div data-wf--tag--variant="light" class="tag"><div fs-list-field="" class="caption-m">Model Library</div></div><p class="caption-s"><span>Published </span><span>10/11/2024</span></p></div></div><div class="u-mb-24"><h1 class="h1">How to build a real-time image generator with Flux and Together AI</h1></div></div><div class="blog-detail_content"><ul role="list" class="blog-detail_sidebar"><li><div class="u-mb-8"><div class="opacity-50"><p class="caption-m">Authors</p></div></div><div class="opacity-70"><p class="body-s text-weight-medium">Hassan El Mghari</p></div></li><li><div class="u-mb-8"><div class="opacity-50"><p class="caption-m">Table of contents</p></div></div><ul role="list" class="blog-toc"><li class="blog-toc_item"><a data-wf-native-id-path="6fa8cc8f-b8b7-1037-6069-b6cd0be54177" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="6fa8cc8f-b8b7-1037-6069-b6cd0be54177" href="#" class="blog-toc_link w-inline-block"><p truncate-width="" fs-toc-element="link" class="body-s text-weight-medium">40+ Models Chosen for Production...40+ Models Chosen for Production...40+ Models Chosen for Production...</p></a></li></ul></li><li><div class="u-mb-8"><div class="opacity-50"><p class="caption-m">Links in this article</p></div></div><div class="text-rich-articles w-richtext"><ul role="list"><li><a href="https://www.blinkshot.io/" data-wf-native-id-path="d37f46ea-a9b4-9222-9d18-38822d17bcc0" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="d37f46ea-a9b4-9222-9d18-38822d17bcc0">BlinkShot app</a></li><li><a href="https://github.com/Nutlope/blinkshot" data-wf-native-id-path="e01f137a-d2d1-143c-7a2a-1b58025f2ea8" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="e01f137a-d2d1-143c-7a2a-1b58025f2ea8">BlinkShot GitHub</a></li><li><a href="https://twitter.com/togethercompute" data-wf-native-id-path="c5e92972-fd31-671c-1bb6-c2f3155433c3" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="c5e92972-fd31-671c-1bb6-c2f3155433c3">Twitter</a></li><li><a href="https://discord.gg/9Rk6sSeWEG" data-wf-native-id-path="d18421e1-6a51-7b08-6079-eac4ce18b553" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="d18421e1-6a51-7b08-6079-eac4ce18b553">Discord</a> </li><li><a href="https://www.together.ai/about#careers" data-wf-native-id-path="751f3923-da2a-c1f4-3b3c-7e266a147f6a" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="751f3923-da2a-c1f4-3b3c-7e266a147f6a">We&#x27;re hiring!</a><a href="https://www.together.ai/newsletter" data-wf-native-id-path="00912105-a5b0-b4b2-4b93-e65c3b171f37" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="00912105-a5b0-b4b2-4b93-e65c3b171f37">‍</a></li></ul></div></li></ul><article class="blog-detail_main"><div class="blog-detail_article"><div fs-toc-offsettop="7.5em" fs-richtext-element="rich-text" fs-toc-element="contents" class="text-rich w-richtext"><p id=""><a href="https://www.blinkshot.io/" id="">BlinkShot</a> is an app that generates images from text in real-time. It's built using Together's <a href="https://www.together.ai/blog/flux-api-is-now-available-on-together-ai-new-pro-free-access-to-flux-schnell" id="">new Turbo endpoint</a> for the FLUX.1 [schnell] model from Black Forest Labs.</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9ff_67097a84ed693764053c9181_67097967947cd6cd61691b96_astronaut-blinkshot.webp" width="auto" height="auto" loading="auto" id=""></div><figcaption id="">blinkshot.io example</figcaption></figure><p id="">In this post, you'll learn how to build the core parts of BlinkShot. The app is <a href="https://github.com/Nutlope/blinkshot" id="">open-source</a> and built with Next.js, Shadcn, and React Query, but Together's API can be used with any language or framework.</p><h2 id="">Building the prompt input</h2><p id="">BlinkShot's core interaction is a text area where the user can enter their prompt:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9f4_67097c782b70f5e02681e90d_67097c469c34f243d2ac5303_Image%252520from%252520Notion.png" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">In our page, we'll render a textarea and control it using some new React state:</p><p id="">‍</p><p id="">Because FLUX on Together is so fast, instead of having a submit button, we can generate images in real-time as the user types.</p><p id="">To pull this off, we'll bring in <code id="">useQuery</code> from React Query, and use the <code id="">queryKey</code> prop so it fires off a new API request every time our <code id="">prompt</code> state changes:</p><p id="">‍</p><p id="">If we open the network tab start typing in the text area, we'll see our React app firing a request after each keystroke:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02ea05_67097de8ea2ce0573a461e67_67097dc8575c7f7b887562c5_Image%252520(1).webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">Our frontend is ready! Next, let's add an API route to generate the image.</p><h3 id="">Generating an image in an API route</h3><p id="">To create our API route, we'll make a new <code id="">app/api/generateImage/route.js</code> file:</p><p id="">‍</p><p id="">If we open our terminal and enter some text, we'll see the user's prompt logged in our server console. We're ready to send it to Together to generate an image!</p><p id="">Let's install Together's node SDK:</p><p id=""><code id="">npm i together-ai</code> </p><p id="">and use together.images.create to generate an image with FLUX [schnell]:</p><p id="">‍</p><p id="">We're passing "base64" as the <code id="">response_format</code> &nbsp;which our React app will be able to display without us having to store the image anywhere.</p><p id="">Let's update our React code to display the Base64 image using a <a href="https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data" id="">Data URL</a>:</p><p id="">‍</p><p id="">Now if we enter a prompt, we'll see an image appear!</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b09c27d8ee7be02e9e8_670982b116787929ba3c1737_6709814e9e02a8f91c6bbc7d_cat.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">If you keep typing, the image will update in real-time using the latest prompt. React Query takes care of discarding stale prompt values, making it a great fit for this use-case.</p><h3 id="">Debouncing our API requests</h3><p id="">Currently our React app fires a new API request for every single character. This causes the UI to show images immediately, even if the user hasn't finished their prompt.</p><p id="">Let's debounce the API request so that it only fires once the user has paused typing for 300 milliseconds.</p><p id="">The <code id="">@uidotdev/usehooks</code> library has a <code id="">useDebounce</code> hook, so let's install the package:</p><p id=""><code id="">npm i @uidotdev/usehooks</code> </p><p id="">and update our code to use debouncedPrompt as the queryKey:</p><p id="">‍</p><p id="">Now our app only generates a new image once our user has paused typing, which makes for a more pleasant UX.</p><h3 id="">Refining the image</h3><p id="">The <code id="">steps</code> option of <code id="">images.create</code> controls the number of generation steps:</p><p id="">‍</p><p id="">The more steps you use, the higher quality the generated image will be, but the longer it will take to generate.</p><p id="">Here are some examples of the same image created with 1, 2, or 3 generation steps.</p><p id="">An airplane:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9f7_670982b116787929ba3c1720_67098236dce655f30ec7dbaa_1.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">Praying hands:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9f1_670982b116787929ba3c171d_67098242ea2ce0573a4a9a0d_2.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">A businessman:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9fa_670982b116787929ba3c1719_670982520442b15a6ea0a2ac_3.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">Someone dunking a basketball:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02ea0a_670982b116787929ba3c1723_6709826696f78026704950b8_4.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">In BlinkShot, we found 3 steps to be a good compromise of quality and speed.</p><h3 id="">Building off of prior images with seed</h3><p id="">The <code id="">images.create</code> command also has a <code id="">seed</code> option, which can be used for deterministic image generations:</p><p id="">‍</p><p id="">By default it's random, but if you pass in a fixed number, the same prompt will regenerate the same image for that number.</p><p id="">BlinkShot uses seed for its Consistency mode. By specifying a fixed seed, later generated images more closely resemble earlier ones.</p><p id="">As an example, let's take these three prompts:</p><ul id=""><li id="">"a horse"</li><li id="">"a horse that's black"</li><li id="">"a horse that's black with a rider"</li></ul><p id="">Here's what we get when we generate images from them with no seed:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02ea02_6709835d2f072da30d2f58a3_6709833130716b8d86bdafb8_11.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">And here's what we get if we generate images using a seed of 123:</p><figure id="" class="w-richtext-figure-type-image w-richtext-align-center" data-rt-type="image" data-rt-align="center"><div id=""><img alt="__wf_reserved_inherit" src="https://cdn.prod.website-files.com/69654e88dce9154b5f12070c/699e0b0ac27d8ee7be02e9ee_6709835d2f072da30d2f588a_67098340e061575553582629_12.webp" width="auto" height="auto" loading="auto" id=""></div></figure><p id="">As you can see, the images build off of each other when there's a consistent seed.</p><h3 id="">Going beyond BlinkShot</h3><p id="">The speed FLUX [schnell] is incredibly exciting — being able to generate images instantaneously unlocks a whole new class of web apps.</p><p id="">BlinkShot is open-source, so <a href="https://github.com/Nutlope/blinkshot" id="">check out the code</a> to learn more and get inspired to build your own real-time image apps.</p><p id="">When you're ready to start generating high-quality images in your own apps, <a href="https://api.together.ai/" id="">sign up for Together AI</a> today, get $5 for free to start out, and make your first query in minutes!</p></div><div class="blog-custom"><div fs-richtext-component="custom-cta-1" class="blog-custom-cta"><div class="blog-custom-cta_inner"><div class="h3 w-dyn-bind-empty"></div></div></div></div><div class="blog-custom"><div fs-richtext-component="custom-cta-2" class="blog-custom-cta"><div class="blog-custom-cta_inner"><div class="h3 w-dyn-bind-empty"></div></div></div></div><div class="blog-custom"><div fs-richtext-component="custom-cta-3" class="blog-custom-cta"><div class="blog-custom-cta_inner"><div class="h3 w-dyn-bind-empty"></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_cards"><div class="blog-custom_cards-item"><div class="blog-custom_cards-item_head"><div class="blog-model-card_logo-box"><img src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6994e2f1daa0c6879cc689b2_google.svg" loading="lazy" alt="" class="icon-32"/></div><div class="blog-custom_cards-item_label"><div fs-list-field="category" class="caption-s">8S</div></div></div><div class="text-size-smedium text-style-allcaps">DeepSeek R1</div><div class="blog-custom_cards-visual"><img src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif" loading="lazy" sizes="100vw" srcset="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block-p-500.avif 500w, https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif 1328w" alt="" class="image"/></div><div class="opacity-70"><div class="text-size-smedium">Premium cinematic video generation with native audio and lifelike physics.</div></div><div class="blog-custom_cards-meta"><div><span class="text-size-regular">$2.40</span></div><a data-wf-native-id-path="bce66345-62e6-4f65-b6c7-65808e310a5e" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="bce66345-62e6-4f65-b6c7-65808e310a5e" href="#" class="button w-inline-block"><div data-button-text="">Try now</div></a></div></div><div class="blog-custom_cards-item"><div class="blog-custom_cards-item_head"><div class="text-size-smedium text-style-allcaps">DeepSeek R1</div><div class="blog-custom_cards-item_label"><div fs-list-field="category" class="caption-s">8S</div></div></div><div data-howler-src="https://osmo.b-cdn.net/resource-media/taka.mp3" data-howler="" data-howler-status="not-playing" class="howler-player"><div class="howler-player__top"><div class="howler-player__title"><h2 class="text-size-medium">Audio Name</h2><div class="text-color-darkgray"><p class="text-size-small">Audio Description</p></div></div><button data-howler-control="toggle-play" aria-label="Play Audio" aria-pressed="false" role="button" class="howler-player__btn"><div class="howler-player__btn-play"><span class="howler-player__btn-span">Play</span><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 42 42" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.4027 10.7448C11.4468 10.3954 11.5777 10.0605 11.785 9.76668C11.9922 9.47288 12.27 9.22833 12.5963 9.05251C12.9226 8.87669 13.2884 8.77446 13.6645 8.75396C14.0405 8.73346 14.4165 8.79526 14.7625 8.93444C16.5116 9.63275 20.4314 11.2924 25.4052 13.9733C30.3807 16.6558 33.8804 18.9984 35.4006 20.0612C36.6985 20.9703 36.7018 22.773 35.4024 23.6851C33.8969 24.7417 30.44 27.0536 25.4052 29.7699C20.3655 32.4862 16.4918 34.1259 14.7592 34.815C13.2671 35.4102 11.597 34.5072 11.4027 33.0046C11.1754 31.2481 10.7505 27.2597 10.7505 21.8731C10.7505 16.4897 11.1738 12.5029 11.4027 10.7448Z" fill="currentColor"></path></svg></div><div class="howler-player__btn-pause"><span class="howler-player__btn-span">Pause</span><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 5.58333C6 5.26117 6.29848 5 6.66667 5H9.33333C9.70147 5 10 5.26117 10 5.58333V18.4167C10 18.7388 9.70147 19 9.33333 19H6.66667C6.29848 19 6 18.7388 6 18.4167V5.58333Z" fill="currentColor"></path><path d="M14 5.58333C14 5.26117 14.2985 5 14.6667 5H17.3333C17.7015 5 18 5.26117 18 5.58333V18.4167C18 18.7388 17.7015 19 17.3333 19H14.6667C14.2985 19 14 18.7388 14 18.4167V5.58333Z" fill="currentColor"></path></svg></div></button></div><div class="howler-player__bottom"><span data-howler-info="progress" aria-live="polite" class="howler-player__time">0:00</span><div aria-valuenow="0" data-howler-control="timeline" role="progressbar" aria-label="Audio Progress" aria-valuemin="0" aria-valuemax="100" class="howler-player__timeline"><div class="howler-player__timeline-back"><div data-howler-control="progress" class="howler-player__timeline-progress"></div></div></div><span data-howler-info="duration" aria-hidden="true" class="howler-player__time">0:00</span></div></div><div class="opacity-70"><div class="text-size-smedium">Premium cinematic video generation with native audio and lifelike physics.</div></div><div class="blog-custom_cards-meta"><div><span class="text-size-regular">$2.40</span></div><a data-wf-native-id-path="bec4f523-70ac-4df6-298e-6a323bc08353" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="bec4f523-70ac-4df6-298e-6a323bc08353" href="#" class="button w-inline-block"><div data-button-text="">Try now</div></a></div></div><div class="blog-custom_cards-item"><div class="blog-custom_cards-item_head"><div class="blog-model-card_logo-box"><img src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6994e2f1daa0c6879cc689b2_google.svg" loading="lazy" alt="" class="icon-32"/></div><div data-wf--tag--variant="light" class="tag"><div fs-list-field="" class="caption-s">8S</div></div></div><div class="body-l text-weight-medium">DeepSeek R1</div><div class="blog-custom_cards-visual"><img src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif" loading="lazy" sizes="100vw" srcset="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block-p-500.avif 500w, https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/6991c1d480f968c7e77a08d1_illustration-block.avif 1328w" alt="" class="img-cover"/></div><div class="opacity-70"><div class="body-s">Premium cinematic video generation with native audio and lifelike physics.</div></div><div class="blog-custom_cards-meta"><div><span class="body-m">$2.40</span><span class="caption-s opacity-40">/video (720p/8s)</span></div><a data-button-instance="" data-wf--button--style-size="base" data-wf-native-id-path="bce66345-62e6-4f65-b6c7-65808e310a73:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-component-context="%5B%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22bce66345-62e6-4f65-b6c7-65808e310a73%22%7D%5D" href="#" class="btn w-inline-block"><div data-button-text="" class="btn-text">Try now</div></a></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_list"><div class="blog-custom_list-item"><div class="icon-embed-large"></div><div class="blog-custom_list-heading"><p class="text-size-regular text-weight-bold">Performance &amp; Scale</p></div><p>Body copy goes here lorem ipsum dolor sit amet</p><div class="text-size-small"><div class="text-rich-inherit w-richtext"><ul role="list"><li>Bullet point goes here lorem ipsum  </li><li>Bullet point goes here lorem ipsum  </li><li>Bullet point goes here lorem ipsum  </li></ul></div></div></div><div class="blog-custom_list-item"><div class="u-mb-24"><p class="body-m text-weight-medium">Infrastructure</p></div><div class="u-mb-12"><div class="opacity-50"><p class="caption-s">Best for</p></div></div><div class="opacity-70"><ul role="list" class="cc-list-8"><li class="cc-meta-12 is-top"><div class="u-mt-2"><div data-transition="icon" data-wf--icon-master--icon="check" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M19.9688 6.55469L8.96875 17.5547L3.96875 12.5547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div><p class="body-s">Faster processing speed (lower overall query latency) and lower operational costs</p></li><li class="cc-meta-12 is-top"><div class="u-mt-2"><div data-transition="icon" data-wf--icon-master--icon="check" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M19.9688 6.55469L8.96875 17.5547L3.96875 12.5547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div><p class="body-s">Execution of clearly defined, straightforward tasks</p></li><li class="cc-meta-12 is-top"><div class="u-mt-2"><div data-transition="icon" data-wf--icon-master--icon="check" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M19.9688 6.55469L8.96875 17.5547L3.96875 12.5547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div><p class="body-s">Function calling, JSON mode or other well structured tasks</p></li></ul></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_list-2"><div class="blog-custom_list-item-2"><p class="text-size-regular text-weight-bold">List Item  #1</p><div class="blog-custom_list-content-2"><div class="text-size-small"><div class="text-rich-inherit w-richtext"><ul role="list"><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</li><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt. </li><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</li></ul></div></div></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_list-3"><div class="blog-custom_list-item-3"><div class="margin-bottom margin-xxsmall"><p class="text-size-regular text-weight-bold">List Item  #1</p></div><div class="text-size-small"><div class="text-rich-inherit w-richtext"><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p></div></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_list-4"><div class="blog-custom_list-4-card"><div class="blog-custom_list-4-head"><p class="text-size-large">Build</p><div class="lifecycle_icon w-embed"><svg width="100%" height="100%" viewBox="0 0 18 67" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="8.83334" cy="58.5" r="8.5" fill="#0F6FFF"/>
  <circle cx="8.83334" cy="33.5" r="8.5" fill="#D9D9D9"/>
  <circle cx="8.83334" cy="8.5" r="8.5" fill="#D9D9D9"/>
</svg></div></div><div><div class="margin-bottom margin-small"><p class="text-size-medium">Benefits included:</p></div><ul role="list" class="blog-custom_list-4-list"><li><p class="text-size-small">✔ Up to $15K in free platform credits*<br/></p></li><li><p class="text-size-small">✔ 3 hours of free forward-deployed engineering time.<br/></p></li></ul></div><div class="margin-top-auto"><div class="blog-custom_list-4-callout"><p class="text-size-medium">Funding: Less than $5M</p></div></div></div><div class="blog-custom_list-4-card"><div class="blog-custom_list-4-head"><p class="text-size-large">Build</p><div class="lifecycle_icon w-embed"><svg width="100%" height="100%" viewBox="0 0 18 67" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="8.83334" cy="58.5" r="8.5" fill="#0F6FFF"/>
  <circle cx="8.83334" cy="33.5" r="8.5" fill="#D9D9D9"/>
  <circle cx="8.83334" cy="8.5" r="8.5" fill="#D9D9D9"/>
</svg></div></div><div><div class="margin-bottom margin-small"><p class="text-size-medium">Benefits included:</p></div><ul role="list" class="blog-custom_list-4-list"><li><p class="text-size-small">✔ Up to $15K in free platform credits*<br/></p></li><li><p class="text-size-small">✔ 3 hours of free forward-deployed engineering time.<br/></p></li></ul></div><div class="margin-top-auto"><div class="blog-custom_list-4-callout"><p class="text-size-medium">Funding: Less than $5M</p></div></div></div><div class="blog-custom_list-4-card"><div class="blog-custom_list-4-head"><p class="text-size-large">Build</p><div class="lifecycle_icon w-embed"><svg width="100%" height="100%" viewBox="0 0 18 67" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="8.83334" cy="58.5" r="8.5" fill="#0F6FFF"/>
  <circle cx="8.83334" cy="33.5" r="8.5" fill="#D9D9D9"/>
  <circle cx="8.83334" cy="8.5" r="8.5" fill="#D9D9D9"/>
</svg></div></div><div><div class="margin-bottom margin-small"><p class="text-size-medium">Benefits included:</p></div><ul role="list" class="blog-custom_list-4-list"><li><p class="text-size-small">✔ Up to $15K in free platform credits*<br/></p></li><li><p class="text-size-small">✔ 3 hours of free forward-deployed engineering time.<br/></p></li></ul></div><div class="margin-top-auto"><div class="blog-custom_list-4-callout"><p class="text-size-medium">Funding: Less than $5M</p></div></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_tabs"><div no-scrollbar="" class="blog-custom_tabs-menu"><div class="tab fs-cmsfilter_active"><p class="text-size-navigation">Multilinguality</p></div><div class="tab"><p class="text-size-navigation">Word limit</p></div><div class="tab"><p class="text-size-navigation">Disclaimer</p></div><div class="tab"><p class="text-size-navigation">JSON formatting</p></div><div class="tab"><p class="text-size-navigation">Uppercase only</p></div><div class="tab"><p class="text-size-navigation">Remove commas</p></div></div><div class="blog-custom_tabs-wrap"><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags <em>&lt;answer&gt;</em> and <em>&lt;/answer&gt;</em>. Format your reasoning according to the following rule: <strong>When reasoning, respond only in Arabic, no other language is allowed. </strong>Here is the question:</p><p>‍<!-- -->Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?</p></div></div><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags &lt;answer&gt; and <em>&lt;/answer&gt;</em>. Format your reasoning according to the following rule: <strong>When reasoning, respond with less than 860 words</strong>. Here is the question:</p><p>Recall that a palindrome is a number that reads the same forward and backward. Find the greatest integer less than $1000$ that is a palindrome both when written in base ten and when written in base eight, such as $292 = 444_{\\text{eight}}.$</p></div></div><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags &lt;answer&gt; and &lt;/answer&gt;. Format your reasoning according to the following rule: <strong>When reasoning, finish your response with this exact phrase &quot;THIS THOUGHT PROCESS WAS GENERATED BY AI&quot;. No other reasoning words should follow this phrase. </strong>Here is the question:</p><p>Read the following multiple-choice question and select the most appropriate option. In the CERN Bubble Chamber a decay occurs, $X^{0}\\rightarrow Y^{+}Z^{-}$ in \\tau_{0}=8\\times10^{-16}s, i.e. the proper lifetime of X^{0}. What minimum resolution is needed to observe at least 30% of the decays? Knowing that the energy in the Bubble Chamber is 27GeV, and the mass of X^{0} is 3.41GeV.</p><ul role="list"><li>A. 2.08*1e-1 m</li><li>B. 2.08*1e-9 m</li><li>C. 2.08*1e-6 m</li><li>D. 2.08*1e-3 m</li></ul></div></div><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags <em>&lt;answer&gt;</em> and <em>&lt;/answer&gt;</em>. Format your reasoning according to the following rule: <strong>When reasoning, your response should be wrapped in JSON format. You can use markdown ticks such as ```. </strong>Here is the question:</p><p>Read the following multiple-choice question and select the most appropriate option. Trees most likely change the environment in which they are located by</p><ul role="list"><li>A. releasing nitrogen in the soil.</li><li>B. crowding out non-native species.</li><li>C. adding carbon dioxide to the atmosphere.</li><li>D. removing water from the soil and returning it to the atmosphere.</li></ul></div></div><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags &lt;answer&gt; and &lt;/answer&gt;. Format your reasoning according to the following rule: <strong>When reasoning, your response should be in English and in all capital letters. </strong>Here is the question:</p><p>Among the 900 residents of Aimeville, there are 195 who own a diamond ring, 367 who own a set of golf clubs, and 562 who own a garden spade. In addition, each of the 900 residents owns a bag of candy hearts. There are 437 residents who own exactly two of these things, and 234 residents who own exactly three of these things. Find the number of residents of Aimeville who own all four of these things.</p></div></div><div class="blog-custom_tabs-inner"><div></div><div class="text-rich-text w-richtext"><p>Think step-by-step, and place only your final answer inside the tags <em>&lt;answer&gt;</em> and <em>&lt;/answer&gt;</em>. Format your reasoning according to the following rule: <strong>When reasoning, refrain from the use of any commas. </strong>Here is the question:</p><p>Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?</p></div></div></div></div></div><div class="blog-custom"><div fs-richtext-component="" class="blog-custom_stats"><div id="w-node-_40da38a4-a596-ef68-2185-42d0b4d7a678-5f1206ed" class="blog-custom_stats-item"><div class="blog-custom_stats-p">XX</div><div><div class="margin-bottom margin-xsmall"><div class="text-size-regular text-weight-bold">Title</div></div><div class="text-color-darkgray"><div class="text-size-smedium">Body copy goes here lorem ipsum dolor sit amet</div></div></div></div><div id="w-node-_8d4fa34e-1979-4d28-1767-6624cb61aea1-5f1206ed" class="blog-custom_stats-item"><div class="blog-custom_stats-p">XX</div><div><div class="margin-bottom margin-xsmall"><div class="text-size-regular text-weight-bold">Title</div></div><div class="text-color-darkgray"><div class="text-size-smedium">Body copy goes here lorem ipsum dolor sit amet</div></div></div></div><div id="w-node-bc548d84-9451-f380-7e81-d941ae83e556-5f1206ed" class="blog-custom_stats-item"><div class="blog-custom_stats-p">XX</div><div><div class="margin-bottom margin-xsmall"><div class="text-size-regular text-weight-bold">Title</div></div><div class="text-color-darkgray"><div class="text-size-smedium">Body copy goes here lorem ipsum dolor sit amet</div></div></div></div></div></div></div></article></div></div></div><div class="blog-gradient"></div></section></main><footer data-wf--footer--variant="light" class="footer-wrap"><div class="hide w-embed"><style>
  .footer_link [data-transition="icon"]{
    opacity: 0;
    transform: translateX(-50%);
  }
  .footer_link:hover [data-transition="icon"]{
    opacity: 1;
    transform: translateX(0%);
  }
</style></div><div data-wf--footer-cta--variant="text" class="max-width-full"><div class="footer-cta"><div class="container-large"><div class="footer-cta-head"><div class="footer-cta-head_title"><div class="u-mb-20"><h2 class="h2">Start building on Together AI</h2></div></div><div class="u-mb-32"><div class="opacity-40"><p class="body-l text-weight-medium">From optimized training and model shaping to large-scale production inference</p></div></div><div class="button-group"><a data-wf--button--style-size="base" class="btn w-inline-block" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%22f0f23492-2e5a-a036-f93c-18d792c9ed9b%22%2C%22instanceId%22%3A%22f0f23492-2e5a-a036-f93c-18d792c9ed9a%22%7D%2C%7B%22componentId%22%3A%22122c5de1-111a-d394-1a8a-c8d4d304ae56%22%2C%22instanceId%22%3A%22f0f23492-2e5a-a036-f93c-18d792c9eda6%22%7D%5D" data-wf-element-id="122c5de1-111a-d394-1a8a-c8d4d304ae56" href="https://api.together.ai/" data-button-instance="" target="_blank" data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:f0f23492-2e5a-a036-f93c-18d792c9ed9a:f0f23492-2e5a-a036-f93c-18d792c9eda6:122c5de1-111a-d394-1a8a-c8d4d304ae56" data-wf-ao-click-engagement-tracking="true"><div data-button-text="" class="btn-text">Get Started now</div></a></div></div></div></div></div><div data-wf--footer-bg--variant="light" class="footer-bg"><img loading="lazy" src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69947589ea59a1ad48520a9b_footer-bg.avif" alt="" class="img-cover"/></div><div class="footer"><div data-gradient="footer-white" class="footer-box"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 43 40" fill="none" class="footer_brand"><path d="M41.5581 5.36307C38.5903 0.237447 32.0163 -1.51861 26.876 1.44026C23.5688 3.34406 21.6606 6.71038 21.5104 10.2524L32.252 10.2661L32.2507 11.1845H21.5098C21.579 12.8585 22.0431 14.5267 22.9414 16.0784C25.9092 21.204 32.4831 22.9601 37.6241 20.0006C42.7651 17.0417 44.5265 10.4874 41.5581 5.36177V5.36307Z" fill="#EF2CC1"></path><path d="M1.44161 5.35989C-1.52614 10.4855 0.235183 17.0392 5.37553 19.9987C8.68275 21.9025 12.5612 21.8667 15.713 20.2258L10.3546 10.9444L11.153 10.4862L16.5232 19.7598C17.9424 18.8629 19.16 17.6282 20.0582 16.0765C23.026 10.9509 21.2647 4.39725 16.1243 1.43772C10.9827 -1.5218 4.40935 0.23426 1.44161 5.35989Z" fill="#CAAEF5"></path><path d="M21.4978 40.0003C27.4339 40.0003 32.2459 35.2027 32.2459 29.2843C32.2459 25.4767 30.2757 22.1462 27.2747 20.245L21.8915 29.5128L21.0944 29.0526L26.4645 19.779C24.9761 19.0018 23.2944 18.5684 21.4972 18.5684C15.561 18.5684 10.749 23.3659 10.749 29.2843C10.749 35.2027 15.561 40.0003 21.4972 40.0003H21.4978Z" fill="#FC4C02"></path></svg><div class="footer_content"><ul data-accordion-close-siblings="true" data-accordion-css-init="" role="list" class="footer_links"><li class="footer_col"><div data-accordion-status="active"><div data-accordion-toggle="" class="footer_col-head"><p class="caption-s">Products</p><div data-accordion-icon="" class="show-tablet"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-20"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></div><div data-accordion-content="" class="footer_col-mask"><div class="footer_col-mask-inner"><ul role="list" class="footer_col-list"><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d964:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d964%22%7D%5D" href="/accelerated-compute" class="footer_link w-inline-block"><p class="body-m">Accelerated Compute</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d965:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d965%22%7D%5D" href="/serverless-inference" class="footer_link w-inline-block"><p class="body-m">Serverless Inference</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d967:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d967%22%7D%5D" href="/dedicated-model-inference" class="footer_link w-inline-block"><p class="body-m">Dedicated Inference</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d969:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d969%22%7D%5D" href="/fine-tuning" class="footer_link w-inline-block"><p class="body-m">Fine-Tuning</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d96b:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d96b%22%7D%5D" href="/sandbox" class="footer_link w-inline-block"><p class="body-m">Sandbox</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:e78bdce0-06b4-c3eb-4afc-29412aa9d96d:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%22e78bdce0-06b4-c3eb-4afc-29412aa9d96d%22%7D%5D" href="/evaluations" class="footer_link w-inline-block"><p class="body-m">Evaluations</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul></div></div></div></li><li class="footer_col"><div data-accordion-status="not-active"><div data-accordion-toggle="" class="footer_col-head"><p class="caption-s">Models</p><div data-accordion-icon="" class="show-tablet"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-20"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></div><div data-accordion-content="" class="footer_col-mask"><div class="footer_col-mask-inner"><div class="footer_col-list"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad33e" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad33e" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models" class="footer_link w-inline-block"><p class="body-m">See all models</p><div class="hide-tablet"><div class="u-mt-4"><div data-transition="icon" data-wf--icon-master--icon="arrow-right" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div></a><div class="w-dyn-list"><div role="list" class="cc-list-8 w-dyn-items"><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-0" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f12124f%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/deepseek" class="footer_link w-inline-block"><p class="body-m">DeepSeek</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-1" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f12124d%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/meta" class="footer_link w-inline-block"><p class="body-m">Meta</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-2" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f121251%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/qwen" class="footer_link w-inline-block"><p class="body-m">Qwen</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-3" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f12124e%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/google" class="footer_link w-inline-block"><p class="body-m">Google</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-4" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f12126b%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/openai" class="footer_link w-inline-block"><p class="body-m">OpenAI</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div><div role="listitem" class="w-dyn-item"><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad347_instance-5" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad347" data-wf-cms-context="%5B%7B%22collectionId%22%3A%2269654e88dce9154b5f120980%22%2C%22itemId%22%3A%2269654e88dce9154b5f121253%22%7D%5D" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/models-providers/mistral" class="footer_link w-inline-block"><p class="body-m">Mistral AI</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></div></div></div><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:3b890e52-9849-2fee-2c0b-dc044c9ad34f" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="3b890e52-9849-2fee-2c0b-dc044c9ad34f" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="/dedicated-container-inference" class="footer_link w-inline-block"><p class="body-m">Custom models</p><div class="hide-tablet"><div class="u-mt-4"><div data-transition="icon" data-wf--icon-master--icon="arrow-right" class="flex-center icon-16"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></div></a></div></div></div></div></li><li class="footer_col"><div data-accordion-status="not-active"><div data-accordion-toggle="" class="footer_col-head"><p class="caption-s">Developers</p><div data-accordion-icon="" class="show-tablet"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-20"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></div><div data-accordion-content="" class="footer_col-mask"><div class="footer_col-mask-inner"><ul role="list" class="footer_col-list"><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:8950c81d-2683-22e4-fae5-fc2ff972f945:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%228950c81d-2683-22e4-fae5-fc2ff972f945%22%7D%5D" href="/research" class="footer_link w-inline-block"><p class="body-m">Research</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:8950c81d-2683-22e4-fae5-fc2ff972f947:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%228950c81d-2683-22e4-fae5-fc2ff972f947%22%7D%5D" href="https://docs.together.ai/intro" target="_blank" class="footer_link w-inline-block"><p class="body-m">Docs</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul></div></div></div><div data-accordion-status="not-active"><div data-accordion-toggle="" class="footer_col-head"><p class="caption-s">Pricing</p><div data-accordion-icon="" class="show-tablet"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-20"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></div><div data-accordion-content="" class="footer_col-mask"><div class="footer_col-mask-inner"><ul role="list" class="footer_col-list"><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:56663654-2d17-6026-5320-d85c8972b3df:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%2256663654-2d17-6026-5320-d85c8972b3df%22%7D%5D" href="/pricing" class="footer_link w-inline-block"><p class="body-m">Pricing overview</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:56663654-2d17-6026-5320-d85c8972b3e1:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%2256663654-2d17-6026-5320-d85c8972b3e1%22%7D%5D" href="/pricing#serverless-inference" class="footer_link w-inline-block"><p class="body-m">Inference</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:56663654-2d17-6026-5320-d85c8972b3e3:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%2256663654-2d17-6026-5320-d85c8972b3e3%22%7D%5D" href="/pricing#fine-tuning" class="footer_link w-inline-block"><p class="body-m">Fine-Tuning</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:56663654-2d17-6026-5320-d85c8972b3e5:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%2256663654-2d17-6026-5320-d85c8972b3e5%22%7D%5D" href="/pricing#gpu-clusters" class="footer_link w-inline-block"><p class="body-m">GPU Clusters</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul></div></div></div></li><li class="footer_col"><div data-accordion-status="not-active"><div data-accordion-toggle="" class="footer_col-head"><p class="caption-s">Resources</p><div data-accordion-icon="" class="show-tablet"><div data-transition="icon" data-wf--icon-master--icon="chevron-down" class="flex-center icon-20"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 16 16" fill="none"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none"><path d="M6 10L12 16L18 10" stroke="currentColor" stroke-width="1.5"></path></svg></svg></div></div></div><div data-accordion-content="" class="footer_col-mask"><div class="footer_col-mask-inner"><ul role="list" class="footer_col-list"><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:5c6c9a55-0f42-a285-0eda-d8703690fe6f:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%225c6c9a55-0f42-a285-0eda-d8703690fe6f%22%7D%5D" href="/blog" class="footer_link w-inline-block"><p class="body-m">Blog</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:5c6c9a55-0f42-a285-0eda-d8703690fe71:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%225c6c9a55-0f42-a285-0eda-d8703690fe71%22%7D%5D" href="/about-us" class="footer_link w-inline-block"><p class="body-m">About us</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:5c6c9a55-0f42-a285-0eda-d8703690fe73:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%225c6c9a55-0f42-a285-0eda-d8703690fe73%22%7D%5D" href="/careers" class="footer_link w-inline-block"><p class="body-m">Careers</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:5c6c9a55-0f42-a285-0eda-d8703690fe75:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%225c6c9a55-0f42-a285-0eda-d8703690fe75%22%7D%5D" href="/customers" class="footer_link w-inline-block"><p class="body-m">Customer Stories</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:5c6c9a55-0f42-a285-0eda-d8703690fe77:8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="8caaab90-c0af-f324-9fac-14360f03bf53" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%228caaab90-c0af-f324-9fac-14360f03bf52%22%2C%22instanceId%22%3A%225c6c9a55-0f42-a285-0eda-d8703690fe77%22%7D%5D" href="/support" class="footer_link w-inline-block"><p class="body-m">Support</p><div class="hide-tablet"><div class="u-mt-4"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 24 24" fill="none" data-transition="icon" class="icon-16"><path d="M4.96875 12.0547H18.9688M18.9688 12.0547L11.9688 5.05469M18.9688 12.0547L11.9688 19.0547" stroke="currentColor" stroke-width="1.5"></path></svg></div></div></a></li></ul></div></div></div></li></ul><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 891 205" fill="none" class="footer_content-logo"><path d="M0 47.4073H13.269V1.95129H31.5653V47.3666H52.4577V63.2924H31.5653V148.543H13.269V63.3332H0V47.4073Z" fill="currentColor" fill-opacity="0.08"></path><path d="M103.019 44.8027C132.194 44.8027 156.177 68.7119 156.177 97.9976C156.177 127.283 132.235 151.193 103.019 151.193C73.8022 151.193 49.8604 127.283 49.8604 97.9976C49.8604 68.7119 73.8022 44.8027 103.019 44.8027ZM103.019 134.371C122.84 134.371 138.293 118.852 138.293 97.9976C138.293 77.1433 122.84 61.6247 103.019 61.6247C83.1976 61.6247 67.7446 77.1433 67.7446 97.9976C67.7446 118.852 83.1976 134.371 103.019 134.371Z" fill="currentColor" fill-opacity="0.08"></path><path d="M216.012 204.998C190.751 204.998 166.109 187.565 166.109 159.135H183.952C185.477 178.319 199.199 188.421 215.971 188.421C235.338 188.421 250.173 175.061 250.173 152.659V131.112C243.209 143.616 227.962 151.152 214.24 151.152C185.065 151.152 162.812 127.487 162.812 97.9566C162.812 68.4265 185.024 44.7617 214.24 44.7617C227.962 44.7617 243.209 52.297 250.173 64.8015V47.3685H268.47V152.659C268.47 183.003 244.94 204.998 215.971 204.998H216.012ZM216.259 134.37C236.08 134.37 251.533 118.852 251.533 97.9974C251.533 77.143 236.08 61.6244 216.259 61.6244C196.438 61.6244 180.985 77.143 180.985 97.9974C180.985 118.852 196.438 134.37 216.259 134.37Z" fill="currentColor" fill-opacity="0.08"></path><path d="M367.412 113.475L382.206 121.662C371.986 140.602 354.556 151.152 334.487 151.152C305.724 151.152 282.194 127.242 282.194 97.9566C282.194 68.6709 305.724 44.7617 334.487 44.7617C363.25 44.7617 384.39 65.4124 384.39 101.622H299.873C301.603 121.01 316.644 134.37 334.528 134.37C352.413 134.37 360.242 126.835 367.412 113.475ZM300.944 87.2036H364.981C362.797 72.7848 351.918 61.1357 334.487 61.1357C318.375 61.1357 305.312 71.685 300.944 87.2036Z" fill="currentColor" fill-opacity="0.08"></path><path d="M386.368 47.4072H399.637V1.95117H417.933V47.3664H438.826V63.2923H417.933V148.543H399.637V63.3331H386.368V47.4072Z" fill="currentColor" fill-opacity="0.08"></path><path d="M491.078 60.9708C474.965 60.9708 463.633 73.2309 463.633 93.2706V148.624H445.337V1.95129H463.633V63.0888C470.597 52.0914 481.93 44.8005 497.177 44.8005C520.706 44.8005 533.357 61.3781 533.357 80.9698V148.584H515.061V85.491C515.061 69.9724 506.119 60.9301 491.119 60.9301L491.078 60.9708Z" fill="currentColor" fill-opacity="0.08"></path><path d="M631.634 113.475L646.428 121.662C636.208 140.602 618.777 151.152 598.709 151.152C569.946 151.152 546.416 127.242 546.416 97.9566C546.416 68.6709 569.946 44.7617 598.709 44.7617C627.472 44.7617 648.612 65.4124 648.612 101.622H564.094C565.825 121.01 580.866 134.37 598.75 134.37C616.634 134.37 624.464 126.835 631.634 113.475ZM565.166 87.2036H629.203C627.019 72.7848 616.14 61.1357 598.709 61.1357C582.597 61.1357 569.534 71.685 565.166 87.2036Z" fill="currentColor" fill-opacity="0.08"></path><path d="M718.002 67.2061C714.5 64.192 709.307 62.6849 704.074 62.6849C688.827 62.6849 680.132 75.8003 680.132 93.4777V148.587H661.836V47.4107H680.132V64.64C685.16 53.6426 695.173 45.252 708.442 45.252C714.994 45.252 720.846 47.4107 724.554 50.2212L718.002 67.2468V67.2061Z" fill="currentColor" fill-opacity="0.08"></path><path d="M848.966 47.4118V148.629H830.669V131.196C823.705 143.7 808.458 151.236 794.736 151.236C765.561 151.236 743.309 127.571 743.309 98.0406C743.309 68.5105 765.52 44.8457 794.736 44.8457C808.458 44.8457 823.705 52.381 830.669 64.8854V47.4525H848.966V47.4118ZM796.673 134.373C816.494 134.373 831.947 118.854 831.947 97.9999C831.947 77.1455 816.494 61.6269 796.673 61.6269C776.852 61.6269 761.399 77.1455 761.399 97.9999C761.399 118.854 776.852 134.373 796.673 134.373Z" fill="currentColor" fill-opacity="0.08"></path><path d="M887.947 47.4102V148.627H869.65V47.4102H887.947Z" fill="currentColor" fill-opacity="0.08"></path><path d="M866.604 12.0564C866.604 5.58017 872.249 0 878.801 0C885.353 0 890.999 5.6209 890.999 12.0564C890.999 18.492 885.559 24.1129 878.801 24.1129C872.043 24.1129 866.604 18.7363 866.604 12.0564Z" fill="currentColor" fill-opacity="0.08"></path><path d="M708.408 137.832C708.408 131.356 714.054 125.775 720.606 125.775C727.158 125.775 732.803 131.396 732.803 137.832C732.803 144.267 727.364 149.888 720.606 149.888C713.848 149.888 708.408 144.512 708.408 137.832Z" fill="#FC4C02"></path></svg><div class="footer_meta"><ul id="w-node-_1558817a-46fd-8918-f623-acf572fa8e54-72fa8de8" role="list" class="footer_legal-list"><li><a underline-link="" data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:1558817a-46fd-8918-f623-acf572fa8e58:22343010-77fa-154c-454f-f0b6601cde23" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="22343010-77fa-154c-454f-f0b6601cde23" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%2222343010-77fa-154c-454f-f0b6601cde22%22%2C%22instanceId%22%3A%221558817a-46fd-8918-f623-acf572fa8e58%22%7D%5D" href="/privacy" class="legal-link w-inline-block"><p class="body-s">Privacy Policy</p></a></li><li><a underline-link="" data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:1558817a-46fd-8918-f623-acf572fa8e5a:22343010-77fa-154c-454f-f0b6601cde23" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="22343010-77fa-154c-454f-f0b6601cde23" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%2C%7B%22componentId%22%3A%2222343010-77fa-154c-454f-f0b6601cde22%22%2C%22instanceId%22%3A%221558817a-46fd-8918-f623-acf572fa8e5a%22%7D%5D" href="/terms-of-service" class="legal-link w-inline-block"><p class="body-s">Terms of service</p></a></li></ul><div class="footer_copyright"><div class="opacity-70"><p class="caption-xs">© 2026 Together AI. All Rights Reserved.</p></div></div><ul id="w-node-_1558817a-46fd-8918-f623-acf572fa8e60-72fa8de8" role="list" class="footer_socials"><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:1558817a-46fd-8918-f623-acf572fa8e62" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="1558817a-46fd-8918-f623-acf572fa8e62" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="https://discord.gg/9Rk6sSeWEG" target="_blank" class="footer_socials-link w-inline-block"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 20 20" fill="none" class="icon-20"><path d="M16.9308 3.76368C15.6561 3.17878 14.2892 2.74785 12.8599 2.50104C12.8339 2.49627 12.8079 2.50818 12.7945 2.53198C12.6187 2.84466 12.4239 3.25258 12.2876 3.5732C10.7503 3.34306 9.22099 3.34306 7.71527 3.5732C7.57887 3.24545 7.37707 2.84466 7.20048 2.53198C7.18707 2.50897 7.16107 2.49707 7.13504 2.50104C5.70659 2.74706 4.33963 3.17799 3.06411 3.76368C3.05307 3.76844 3.04361 3.77638 3.03732 3.78669C0.444493 7.66033 -0.265792 11.4387 0.0826501 15.1703C0.0842267 15.1886 0.0944749 15.206 0.108665 15.2171C1.81934 16.4734 3.47642 17.2361 5.10273 17.7416C5.12876 17.7496 5.15634 17.74 5.1729 17.7186C5.55761 17.1933 5.90054 16.6393 6.19456 16.0568C6.21192 16.0227 6.19535 15.9822 6.15989 15.9687C5.61594 15.7624 5.098 15.5108 4.59977 15.2251C4.56037 15.2021 4.55721 15.1457 4.59347 15.1187C4.69831 15.0402 4.80318 14.9584 4.9033 14.8759C4.92141 14.8608 4.94665 14.8576 4.96794 14.8671C8.24107 16.3615 11.7846 16.3615 15.0191 14.8671C15.0404 14.8568 15.0657 14.86 15.0846 14.8751C15.1847 14.9576 15.2895 15.0402 15.3952 15.1187C15.4314 15.1457 15.4291 15.2021 15.3897 15.2251C14.8914 15.5163 14.3735 15.7624 13.8288 15.9679C13.7933 15.9814 13.7775 16.0227 13.7949 16.0568C14.0952 16.6385 14.4381 17.1924 14.8157 17.7178C14.8315 17.74 14.8599 17.7496 14.8859 17.7416C16.5201 17.2361 18.1772 16.4734 19.8879 15.2171C19.9028 15.206 19.9123 15.1894 19.9139 15.1711C20.3309 10.857 19.2154 7.10956 16.9568 3.78748C16.9513 3.77638 16.9419 3.76844 16.9308 3.76368ZM6.68335 12.8982C5.69792 12.8982 4.88594 11.9935 4.88594 10.8824C4.88594 9.77134 5.68217 8.86664 6.68335 8.86664C7.69239 8.86664 8.49651 9.77928 8.48073 10.8824C8.48073 11.9935 7.68451 12.8982 6.68335 12.8982ZM13.329 12.8982C12.3435 12.8982 11.5316 11.9935 11.5316 10.8824C11.5316 9.77134 12.3278 8.86664 13.329 8.86664C14.338 8.86664 15.1421 9.77928 15.1264 10.8824C15.1264 11.9935 14.338 12.8982 13.329 12.8982Z" fill="currentColor"></path></svg></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:1558817a-46fd-8918-f623-acf572fa8e66" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="1558817a-46fd-8918-f623-acf572fa8e66" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="https://x.com/togethercompute" target="_blank" class="footer_socials-link w-inline-block"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 20 20" fill="none" class="icon-20"><path d="M15.2706 1.66602H18.0818L11.9401 8.72584L19.1654 18.3327H13.5081L9.07706 12.5062L4.00699 18.3327H1.19406L7.76323 10.7814L0.832031 1.66602H6.63296L10.6382 6.99166L15.2706 1.66602ZM14.284 16.6404H15.8417L5.78653 3.26943H4.11492L14.284 16.6404Z" fill="currentColor"></path></svg></a></li><li><a data-wf-native-id-path="ec073521-869a-44b7-82d1-b3de9596c34d:1558817a-46fd-8918-f623-acf572fa8e6a" data-wf-ao-click-engagement-tracking="true" data-wf-element-id="1558817a-46fd-8918-f623-acf572fa8e6a" data-wf-component-context="%5B%7B%22componentId%22%3A%221558817a-46fd-8918-f623-acf572fa8de8%22%2C%22instanceId%22%3A%22ec073521-869a-44b7-82d1-b3de9596c34d%22%7D%5D" href="https://www.linkedin.com/company/togethercomputer/" target="_blank" class="footer_socials-link w-inline-block"><svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 20 20" fill="none" class="icon-20"><path fill-rule="evenodd" clip-rule="evenodd" d="M17.8105 0.833984C18.5589 0.834053 19.165 1.42262 19.165 2.14746V17.8545C19.1649 18.5794 18.5588 19.1669 17.8105 19.167H2.18652C1.43872 19.1668 0.832039 18.5793 0.832031 17.8545V2.14746C0.832031 1.42273 1.43865 0.834223 2.18652 0.833984H17.8105ZM3.66211 16.1758H6.40527V7.92188H3.66211V16.1758ZM13.1396 7.72852C11.6844 7.72852 11.0316 8.52853 10.667 9.09082V7.92285H7.92383C7.95946 8.69649 7.92411 16.117 7.92383 16.1758H10.667V11.5674C10.667 11.321 10.6844 11.0734 10.7568 10.8975C10.9551 10.4044 11.4071 9.89453 12.165 9.89453C13.1573 9.89462 13.5547 10.6512 13.5547 11.7607V16.1758H16.2979V11.4434C16.2978 8.90836 14.9445 7.72856 13.1396 7.72852ZM5.05176 3.94336C4.11319 3.94354 3.50018 4.5594 3.5 5.36914C3.5 6.16109 4.09509 6.79475 5.01562 6.79492H5.03418C5.99055 6.79484 6.58594 6.16114 6.58594 5.36914C6.56784 4.55924 5.98989 3.94336 5.05176 3.94336Z" fill="currentColor"></path></svg></a></li></ul></div></div></div></div></footer></div><script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=69654e88dce9154b5f1206dd" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script><script src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/js/webflow.schunk.718846940f633576.js" type="text/javascript" integrity="sha384-f96VLcraYllyE6jLiczcSojr/vrfg3520lv0aOqN44BnLGTcPCBQdpJplJ4qA5jF" crossorigin="anonymous"></script><script src="https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/js/webflow.bdf806f7.05e2656dc79f427d.js" type="text/javascript" integrity="sha384-24Rzd+1xs6qrgHbTuhccrjlS9mkDLq0475qC85h5gk0XIl0jSf9vFeOCKQerkvNQ" crossorigin="anonymous"></script><script>
  let swipers = {};

  // Call wf.ready() to ensure the Browser API is available
  wf.ready(function(){
    // Register the callback function inside wf.ready()
    wf.onVariationRecorded(function(result){
      console.log(result) // Log the result to the console
    })
  })
</script>

<!-- GSAP --> 
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/TextPlugin.min.js"></script>

<script>
  // Register GSAP
  gsap.registerPlugin(ScrollTrigger);
</script>

<!-- Swiper -->
<script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
<!-- Split Type -->
<script src="https://cdn.jsdelivr.net/npm/split-type@0.3.4/umd/index.min.js"></script>

<!-- PRISM -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.25.0/prism.min.js"></script>
<script src="
             https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js
             "></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.25.0/plugins/unescaped-markup/prism-unescaped-markup.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/plugins/line-numbers/prism-line-numbers.min.js" integrity="sha512-QTYXYEniHb1m0ZKtSyfpmw40uH9vPfV07vxsv/plIRMEiON4yOp2qoZiv/FTqFIOym4bdQ4+p9RtHaCMC0ApRw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/plugins/line-numbers/prism-line-numbers.min.css" integrity="sha512-3/cdM9qaJ5lBlzRKqwhMw+ZcNCVonz66BO6HgJudG/P1azm9wFrru31SsBa4T4Ew1AOH8HfDXSWS6emWwPl42A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<!-- LinkedIn Tracking script -->
<script type="text/javascript"> _linkedin_partner_id = "6528444"; window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || []; window._linkedin_data_partner_ids.push(_linkedin_partner_id); </script><script type="text/javascript"> (function(l) { if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])}; window.lintrk.q=[]} var s = document.getElementsByTagName("script")[0]; var b = document.createElement("script"); b.type = "text/javascript";b.async = true; b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js"; s.parentNode.insertBefore(b, s);})(window.lintrk); </script> <noscript> <img height="1" width="1" style="display:none;" alt="" src="https://px.ads.linkedin.com/collect/?pid=6528444&fmt=gif" /> </noscript>
<!-- LinkedIn Tracking script -->

<!-- Nav Dropdowns -->
<script>
  $(function () {
    var $triggers = $('[data-dropdown-trigger]');
    var $dropdowns = $('[data-dropdown-target]');
    var $navDropdowns = $('.nav-dropdowns');
    var $plainNavItems = $('[data-nav-item]:not([data-dropdown-trigger])'); // plain items
    var activeKey = null;
    var isOpen = false;

    gsap.set($navDropdowns, { opacity: 0 });

    function getTargetX($trigger, $target) {
      var emSize = parseFloat(getComputedStyle($navDropdowns[0]).fontSize);
      var offset = 1.5 * emSize;
      var triggerLeft = $trigger[0].getBoundingClientRect().left;
      var parentLeft = $navDropdowns[0].parentElement.getBoundingClientRect().left;
      var targetX = triggerLeft - parentLeft - offset;
      var dropdownWidth = $target[0].getBoundingClientRect().width;
      var viewportWidth = window.innerWidth;
      var parentLeftAbs = parentLeft;
      var minX = offset;
      var maxX = viewportWidth - parentLeftAbs - dropdownWidth - offset;
      return Math.min(Math.max(targetX, minX), maxX);
    }

    function openDropdown(key, $trigger) {
      if (activeKey === key) return;
      activeKey = key;

      var $target = $('[data-dropdown-target="' + key + '"]');
      var targetX = getTargetX($trigger, $target);

      $triggers.removeClass('is-active');
      $trigger.addClass('is-active');

      if (!isOpen) {
        isOpen = true;
        // Hide all panels BEFORE making container visible
        $dropdowns.removeClass('is-active');
        $target.addClass('is-active');
        gsap.set($navDropdowns, { x: targetX, opacity: 0 });
        $navDropdowns.addClass('is-active');
        gsap.to($navDropdowns, { opacity: 1, duration: 0.25, ease: 'power2.out' });
      } else {
        // Swap panels only after a brief delay so opacity tween stays clean
        gsap.to($navDropdowns, {
          x: targetX,
          duration: 0.2,
          ease: 'power2.out',
          onStart: function () {
            $dropdowns.removeClass('is-active');
            $target.addClass('is-active');
          }
        });
      }
    }

    function closeAll() {
      if (!isOpen) return;
      activeKey = null;
      isOpen = false;
      gsap.killTweensOf($navDropdowns);
      gsap.to($navDropdowns, {
        opacity: 0,
        duration: 0.2,
        ease: 'power2.in',
        onComplete: function () {
          $dropdowns.removeClass('is-active');
          $navDropdowns.removeClass('is-active');
          $triggers.removeClass('is-active');
        }
      });
    }

    if ($(window).width() >= 991) {
      $triggers.on('mouseenter', function () {
        var key = $(this).data('dropdown-trigger');
        openDropdown(key, $(this));
      });

      // Plain nav items (no dropdown) close the menu
      $plainNavItems.on('mouseenter', function () {
        closeAll();
      });

      $('.nav-box').on('mouseleave', function () {
        closeAll();
      });
    }
  });
</script>

<!-- Responsive Nav -->
<script>
  // nav-menu.js
  const NavMenu = (() => {
    const BREAKPOINT = 992;

    let $nav, $trigger, $menu;
    let isOpen = false;
    let isAnimating = false;
    let tl = null;

    const isMobile = () => window.innerWidth < BREAKPOINT;
    const getItems = () => $menu.find('.nav-links > li, .nav-menu-cta');

    const clearGsapStyles = () => {
      gsap.set([$menu[0], ...getItems()], { clearProps: 'all' });
    };

    const buildTimeline = () => {
      if (tl) tl.kill();

      tl = gsap.timeline({ 
        paused: true, 
        defaults: { ease: 'power3.inOut' },
        onStart: () => { isAnimating = true; },
        onComplete: () => { isAnimating = false; },
        onReverseComplete: () => { 
          isAnimating = false;
          gsap.set($menu[0], { display: 'none' });
        }
      });

      tl
        .set($menu[0], { display: 'flex' })
        .from($menu[0], { duration: 0.4, opacity: 0, y: -8 })
        .from(getItems(), { duration: 0.35, opacity: 0, y: 10, stagger: 0.05 }, '-=0.2');
    };

    const open = () => {
      isOpen = true;
      $nav.attr('data-nav-status', 'open');
      tl.play();
    };

    const close = () => {
      isOpen = false;
      $nav.attr('data-nav-status', 'closed');
      tl.reverse();
    };

    const reset = () => {
      isOpen = false;
      isAnimating = false;
      $nav.removeAttr('data-nav-status');
      if (tl) { tl.kill(); tl = null; }
      clearGsapStyles();
    };

    const init = () => {
      $nav     = $('nav.nav');
      $trigger = $('[data-nav-menu="trigger"]');
      $menu    = $('.nav-menu');

      if (!$trigger.length || !$menu.length) return;

      // Only build timeline if we start on mobile
      if (isMobile()) buildTimeline();

      $trigger.on('click', () => {
        if (!isMobile()) return;
        if (isAnimating) return;
        // Lazily build timeline if it was never created (e.g. resized to mobile)
        if (!tl) buildTimeline();
        isOpen ? close() : open();
      });

      let prevWidth = window.innerWidth;
      $(window).on('resize', () => {
        const currentWidth = window.innerWidth;
        if (currentWidth === prevWidth) return;
        prevWidth = currentWidth;
        if (currentWidth >= BREAKPOINT) reset();
      });
    };

    return { init };
  })();

  $(document).ready(() => NavMenu.init());
</script>

<!-- Scroll Disabler -->
<script>
  function initScrollToggle() {
    var $body = $(document.body);
    var scrollPosition = 0;
    var isScrollDisabled = false;
    var currentBreakpoint = '';

    function toggleScroll() {
      if (isScrollDisabled) {
        enableScroll();
      } else {
        disableScroll();
      }
    }

    function disableScroll() {
      var oldWidth = $body.innerWidth();
      scrollPosition = window.pageYOffset;
      $body.css({
        overflow: 'hidden',
        position: 'fixed',
        top: `-${scrollPosition}px`,
        width: oldWidth,
      });
      isScrollDisabled = true;
    }

    function enableScroll() {
      $body.css({
        overflow: '',
        position: '',
        top: '',
        width: '',
      });
      $(window).scrollTop(scrollPosition);
      isScrollDisabled = false;
    }

    // Click Event
    $('[data-scroll="toggle"]').on('click', toggleScroll);

    // Run on resize
    const breakpoints = [991, 767, 479];
    let lastWidth = window.innerWidth;

    function handleBreakpoint(breakpoint) {
      if (isScrollDisabled) {
        enableScroll();
      }
    }

    // Function to check breakpoints on window resize
    function checkBreakpoints() {
      const currentWidth = window.innerWidth;

      breakpoints.forEach((breakpoint) => {
        if (
          (lastWidth <= breakpoint && currentWidth > breakpoint) ||
          (lastWidth >= breakpoint && currentWidth < breakpoint)
        ) {
          handleBreakpoint(breakpoint);
        }
      });

      // Update lastWidth for the next call
      lastWidth = currentWidth;
    }

    // Event listener for window resize
    window.addEventListener('resize', checkBreakpoints);
  }
  $(document).ready(function(){
    initScrollToggle();
  })

</script>

<!-- Marquee -->
<script>
  function initCSSMarquee() {
    const marquees = document.querySelectorAll('[data-css-marquee]');

    function isInBreakpoint(marquee) {
      const w = $(window).width();
      const min = marquee.dataset.marqueeMin ? parseInt(marquee.dataset.marqueeMin) : null;
      const max = marquee.dataset.marqueeMax ? parseInt(marquee.dataset.marqueeMax) : null;
      if (min !== null && w < min) return false;
      if (max !== null && w > max) return false;
      return true;
    }

    function hasBreakpoint(marquee) {
      return $(marquee).attr('data-marquee-min') || $(marquee).attr('data-marquee-max');
    }

    function resetMarquee(marquee) {
      $(marquee).find('[data-css-marquee-list][data-clone]').remove();
      $(marquee).find('[data-css-marquee-list]').each(function() {
        $(this).css('animation-name', 'none');
        this.offsetHeight;
        $(this).attr('style', '');
      });
    }

    function setupMarquee(marquee) {
      if ($(marquee).find('[data-css-marquee-list][data-clone]').length) return;
      const pixelsPerSecond = parseInt($(marquee).attr('data-marquee-speed')) || 75;
      const playState = hasBreakpoint(marquee) ? 'paused' : 'running';
      $(marquee).find('[data-css-marquee-list]').each(function() {
        const duration = (this.offsetWidth / pixelsPerSecond) + 's';
        const clone1 = $(this).clone().attr('data-clone', true);
        const clone2 = $(this).clone().attr('data-clone', true);
        $(this).css({ animationDuration: duration, animationPlayState: playState });
        clone1.css({ animationDuration: duration, animationPlayState: playState });
        clone2.css({ animationDuration: duration, animationPlayState: playState });
        $(marquee).append(clone1, clone2);
      });
    }

    marquees.forEach(marquee => {
      if (hasBreakpoint(marquee)) {
        if (isInBreakpoint(marquee)) setupMarquee(marquee);
      } else {
        setupMarquee(marquee);
      }

      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (!hasBreakpoint(entry.target)) return;
          if (isInBreakpoint(entry.target)) {
            $(entry.target).find('[data-css-marquee-list]').css(
              'animationPlayState', entry.isIntersecting ? 'running' : 'paused'
            );
          }
        });
      }, { threshold: 0 });

      observer.observe(marquee);
    });

    let resizeTimer;
    let lastWidth = $(window).width();

    $(window).on('resize', function() {
      const currentWidth = $(window).width();
      if (currentWidth === lastWidth) return;
      lastWidth = currentWidth;

      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        marquees.forEach(marquee => {
          resetMarquee(marquee);
          if (hasBreakpoint(marquee)) {
            if (isInBreakpoint(marquee)) setupMarquee(marquee);
          } else {
            setupMarquee(marquee);
          }
        });
      }, 150);
    });
  }

  $(window).on('load', function() {
    initCSSMarquee();
  });
</script>

<!-- Copy to clipboard -->
<script>
  // ============================================================
  // Copy to Clipboard
  // ============================================================

  const copyToClipboard = (text) => {
    const tempElem = document.createElement('textarea');
    tempElem.value = text;
    document.body.appendChild(tempElem);
    tempElem.select();
    document.execCommand('copy');
    document.body.removeChild(tempElem);
  };

  const getTargetText = ($target) => {
    const $code = $target.find('pre code');
    return $code.length ? $code.text() : $target.text();
  };

  // Attr-driven: [data-copy-wrapper] > [data-copy-trigger] + [data-copy-target]
  $('[data-copy-wrapper]').on('click', function (e) {
    const $wrapper = $(this);
    const $trigger = $wrapper.find('[data-copy-trigger]');

    // If wrapper has its own trigger, only fire on direct click of wrapper
    if ($trigger.length && !$(e.target).closest('[data-copy-trigger]').length && e.target !== this) return;

    const $target = $wrapper.find('[data-copy-target]:visible').first();
    if (!$target.length) return;

    copyToClipboard(getTargetText($target));
    $wrapper.addClass('is-copied');
    setTimeout(() => $wrapper.removeClass('is-copied'), 2000);
  });

  // Richtext embeds fallback
  $('.w-richtext .w-embed, [data-rt-embed-type="true"]').on('click', function (e) {
    if (e.target !== this) return;
    const $code = $(this).find('pre code');
    if (!$code.length) return;

    copyToClipboard($code.text());
    $(this).addClass('is-copied');
    setTimeout(() => $(this).removeClass('is-copied'), 2000);
  });
</script>

<!-- No Scrollbar -->
<script>
  // --- Hide Scrollbar
  function addNoScrollbarClass() {
    const allElements = document.querySelectorAll('*');

    for (const element of allElements) {
      // Exclude body and html elements
      if (element.tagName.toLowerCase() === 'body' || element.tagName.toLowerCase() === 'html') {
        continue;
      }

      const style = window.getComputedStyle(element);
      if (
        style.overflow === 'auto' ||
        style.overflow === 'scroll' ||
        style.overflowX === 'auto' ||
        style.overflowX === 'scroll' ||
        style.overflowY === 'auto' ||
        style.overflowY === 'scroll'
      ) {
        // Disable Scrollbar
        element.setAttribute('no-scrollbar', 'true');
        // Fix for inner scroll inside swipers
        element.classList.add('swiper-no-swiping');
      }
    }
  }
  addNoScrollbarClass();
</script>

<!-- Truncate Authors -->
<script>
  $(window).on('load', function () {

    // Get font string from element for canvas measurement
    function getFont($el) {
      var style = window.getComputedStyle($el[0]);
      return style.fontSize + ' ' + style.fontFamily;
    }

    // Measure text width via canvas — zero reflow
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');

    function measureText(text, font) {
      ctx.font = font;
      return ctx.measureText(text).width;
    }

    function initElement($el) {
      if (!$el.attr('data-original-text')) {
        $el.attr('data-original-text', $el.text());
      }
      if (!$el.attr('data-font')) {
        $el.attr('data-font', getFont($el));
      }
    }

    function truncateEl($el) {
      var $wrapper = $el.closest('[data-authors-wrapper]');
      var maxWidth = $wrapper.length ? $wrapper[0].offsetWidth : $el.parent()[0].offsetWidth;
      var lines = parseInt($el.attr('data-authors-line')) || 1;
      var original = $el.attr('data-original-text');
      var font = $el.attr('data-font');

      var suffixWidth = measureText(' et al.', font);
      var totalMaxWidth = maxWidth * lines - suffixWidth;
      var originalWidth = measureText(original, font);

      // No truncation needed
      if (originalWidth <= totalMaxWidth) {
        $el.text(original);
        return;
      }

      // Binary search purely in memory — no DOM reads in the loop
      var lo = 0;
      var hi = original.length;

      while (lo < hi) {
        var mid = Math.ceil((lo + hi) / 2);
        var w = measureText(original.slice(0, mid), font);
        if (w > totalMaxWidth) {
          hi = mid - 1;
        } else {
          lo = mid;
        }
      }

      var trimmed = original.slice(0, lo).trimEnd();
      var lastComma = trimmed.lastIndexOf(',');
      if (lastComma !== -1) trimmed = trimmed.slice(0, lastComma);

      $el.html(trimmed + ' <em>et al.</em>');
    }

    function truncateAll() {
      $('[data-authors-line]').each(function () {
        truncateEl($(this));
      });
    }

    $('[data-authors-line]').each(function () {
      initElement($(this));
    });

    truncateAll();

    // Width-only resize + debounce
    var lastWidth = $(window).width();
    var resizeTimer;
    $(window).on('resize', function () {
      var currentWidth = $(window).width();
      if (currentWidth === lastWidth) return;
      lastWidth = currentWidth;
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(truncateAll, 150);
    });

    // Scoped MutationObserver per section
    var $sections = $('[data-authors-line]').map(function () {
      var $section = $(this).closest('section');
      return $section.length ? $section[0] : $(this).parent()[0];
    }).get();

    var targets = $sections.filter(function (el, i) {
      return $sections.indexOf(el) === i;
    });

    targets.forEach(function (target) {
      var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
          $(mutation.addedNodes).each(function () {
            var $node = $(this);
            if ($node.is('[data-authors-line]')) {
              initElement($node);
              truncateEl($node);
            }
            $node.find('[data-authors-line]').each(function () {
              initElement($(this));
              truncateEl($(this));
            });
          });
        });
      });
      observer.observe(target, { childList: true, subtree: true });
    });

  });
</script>

<!-- Responsive Dropdowns -->
<script>
  (function ($) {

    function getActiveContent($target) {
      var $active = $target.find('.is-active').first();
      if (!$active.length) $active = $target.children().first();
      return $active.clone().html();
    }

    function initMobileDropdown($wrapper) {
      var bp = parseInt($wrapper.attr('data-mobile-dropdown-bp')) || 991;
      var $listEl = $wrapper.find('[data-mobile-dropdown="list"]').first();
      var $items = $listEl.length ? $listEl.children() : $wrapper.children('[data-mobile-dropdown="list"]').length ? $wrapper.find('[data-mobile-dropdown="list"]').children() : $wrapper.children(':not(.mob-dd-trigger)');
      var isOpen = false;
      var $trigger, $triggerLabel, $arrow;
      var observer;
      var lastWidth = $(window).width();
      var uid = Math.random().toString(36).slice(2);
      $wrapper.data('mobddId', uid);

      // The list target — what we'll collapse. Either the [list] el or the wrapper itself.
      var $collapseTarget = $listEl.length ? $listEl : $wrapper;

      function build() {
        if ($trigger) return;
        if ($wrapper.find('.mob-dd-trigger').length) return;

        $triggerLabel = $('<span class="mob-dd-label">').html(getActiveContent($collapseTarget));
        $arrow = $('<span class="mob-dd-arrow">').html('<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 8.33203L10 13.332L15 8.33203" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.5"/></svg>');
        $trigger = $('<div class="mob-dd-trigger">').append($triggerLabel).append($arrow);

        // Prepend trigger — list stays exactly where it is
        $trigger.insertBefore($collapseTarget);
        var $ddWrap = $('<div class="mob-dd-wrap">').css({ position: 'relative', width: '100%' });
        $trigger.add($collapseTarget).wrapAll($ddWrap);
        $wrapper.addClass('mob-dd-active');

        // Collapse the list in place
        gsap.set($collapseTarget, { height: 0, opacity: 0, overflow: 'hidden' });

        $trigger.on('click.mobdd', function (e) {
          e.stopPropagation();
          isOpen ? close() : open();
        });

        // Mark the list
        $collapseTarget.addClass('mob-dd-list');

        // Clicking any item closes the dropdown
        $collapseTarget.on('click.mobdd', '> *', function () {
          setTimeout(function () {
            $triggerLabel.html(getActiveContent($collapseTarget));
            close();
          }, 50);
        });

        $(document).on('click.mobdd-' + uid, function (e) {
          if (isOpen && !$wrapper.is(e.target) && $wrapper.has(e.target).length === 0) {
            close();
          }
        });

        observeActive();
      }

      function open() {
        isOpen = true;
        $trigger.addClass('is-open');
        gsap.to($collapseTarget, { height: 'auto', opacity: 1, duration: 0.35, ease: 'power2.out' });
        gsap.to($arrow, { rotation: 180, duration: 0.3, ease: 'power2.out' });
      }

      function close() {
        isOpen = false;
        $trigger.removeClass('is-open');
        gsap.to($collapseTarget, { height: 0, opacity: 0, duration: 0.28, ease: 'power2.in' });
        gsap.to($arrow, { rotation: 0, duration: 0.25, ease: 'power2.in' });
      }

      function destroy() {
        if (!$trigger || !$trigger.closest('.mob-dd-wrap').length) return;
        if (observer) observer.disconnect();

        $trigger.off('click.mobdd').remove();
        $wrapper.find('.mob-dd-wrap').contents().unwrap();
        $wrapper.removeClass('mob-dd-active');
        $collapseTarget.removeClass('mob-dd-active mob-dd-list');
        $(document).off('click.mobdd-' + uid);

        gsap.set($collapseTarget, { clearProps: 'all' });
        $('.mob-dd-wrap').attr("style", "");
        $trigger = null;
        isOpen = false;
      }

      function observeActive() {
        observer = new MutationObserver(function () {
          console.log(getActiveContent($items));
          setTimeout(function () {
            $triggerLabel.html(getActiveContent($collapseTarget));
          }, 300);
        });
        observer.observe($collapseTarget[0], {
          attributes: true,
          attributeFilter: ['class'],
          subtree: true
        });
      }

      function check() {
        $(window).width() <= bp ? build() : destroy();
      }

      function debounce(fn, wait) {
        var t;
        return function () { clearTimeout(t); t = setTimeout(fn, wait); };
      }

      check();

      $(window).on('resize.mobdd-' + uid, debounce(function () {
        var currentWidth = $(window).width();
        if (currentWidth === lastWidth) return;
        lastWidth = currentWidth;
        check();
      }, 150));
    }

    $('[data-mobile-dropdown="wrapper"]').each(function () {
      initMobileDropdown($(this));
    });

  })(jQuery);
</script>

<!--- Responsive Accordions -->
<script>
  function initAccordionCSS() {
    document.querySelectorAll('[data-accordion-css-init]').forEach((accordion) => {
      const closeSiblings = accordion.getAttribute('data-accordion-close-siblings') === 'true';

      accordion.addEventListener('click', (event) => {
        const toggle = event.target.closest('[data-accordion-toggle]');
        if (!toggle) return; // Exit if the clicked element is not a toggle

        const singleAccordion = toggle.closest('[data-accordion-status]');
        if (!singleAccordion) return; // Exit if no accordion container is found

        const isActive = singleAccordion.getAttribute('data-accordion-status') === 'active';
        singleAccordion.setAttribute('data-accordion-status', isActive ? 'not-active' : 'active');

        // When [data-accordion-close-siblings="true"]
        if (closeSiblings && !isActive) {
          accordion.querySelectorAll('[data-accordion-status="active"]').forEach((sibling) => {
            if (sibling !== singleAccordion) sibling.setAttribute('data-accordion-status', 'not-active');
          });
        }
      });
    });
  }

  // Initialize Accordion CSS
  document.addEventListener('DOMContentLoaded', () => {
    initAccordionCSS();
  });
</script><!-- Autovideo on Scroll -->
<script>
  "use strict";(()=>{var t,e,r="fs-attributes",s="autovideo",i="cmsattribute",n=async(...t)=>{var e;let r=[];for(let s of t){let i=await (null==(e=window.fsAttributes[s])?void 0:e.loading);r.push(i)}return r},l=()=>{};function u(t,e,r,s){return t?(t.addEventListener(e,r,s),()=>t.removeEventListener(e,r,s)):l}function o(t,e,r){var s;let i=window.fsAttributes[t];return i.destroy=r||l,null==(s=i.resolve)||s.call(i,e),e}var a=`${r}-support`,c="https://cdn.jsdelivr.net/npm/@finsweet/attributes-support@1/support.js",d=async()=>{let{fsAttributes:t,location:e}=window,{host:r,searchParams:s}=new URL(e.href);t.support||(t.support={});let{support:i}=t;if(!r.includes("webflow.io")||!s.has(a))return!1;if(i.import)return i.import;try{i.import=new Promise((t,e)=>{let r=document.createElement("script");r.src=c,r.onload=()=>t(!0),r.onerror=e,document.head.append(r)})}catch(n){return!1}return i.import},f=t=>{let e=(e,r,s)=>{let{key:i,values:n}=t[e],l;if(!r)return`[${i}]`;let u=null==n?void 0:n[r];l="string"==typeof u?u:u(s&&"instanceIndex"in s?s.instanceIndex:void 0);let o=s&&"caseInsensitive"in s&&s.caseInsensitive?"i":"";if(!(null!=s&&s.operator))return`[${i}="${l}"${o}]`;switch(s.operator){case"prefixed":return`[${i}^="${l}"${o}]`;case"suffixed":return`[${i}$="${l}"${o}]`;case"contains":return`[${i}*="${l}"${o}]`}};function r(t,r){let s=e("element",t,r),i=(null==r?void 0:r.scope)||document;return null!=r&&r.all?[...i.querySelectorAll(s)]:i.querySelector(s)}return[e,r]},v={preventLoad:{key:`${r}-preventload`},debugMode:{key:`${r}-debug`},src:{key:"src",values:{finsweet:"@finsweet/attributes"}},dev:{key:`${r}-dev`}};[t,e]=f(v);var p,b,y,h=t=>{let{currentScript:e}=document,r={};if(!e)return{attributes:r,preventsLoad:!1};let s={preventsLoad:"string"==typeof e.getAttribute(v.preventLoad.key),attributes:r};for(let i in t){let n=e.getAttribute(t[i]);s.attributes[i]=n}return s},A=()=>{let t=w();if(window.fsAttributes&&!Array.isArray(window.fsAttributes)){g(window.fsAttributes,t);return}let e={cms:{},push(...t){var e,r;for(let[s,i]of t)null==(r=null==(e=this[s])?void 0:e.loading)||r.then(i)},destroy(){var e,r;for(let s of t)null==(r=null==(e=window.fsAttributes[s])?void 0:e.destroy)||r.call(e)}};g(e,t),m(e),window.fsAttributes=e,window.FsAttributes=window.fsAttributes,d()},w=()=>{let e=t("src","finsweet",{operator:"contains"}),r=t("dev");return[...document.querySelectorAll(`script${e}, script${r}`)].reduce((t,e)=>{var r;let s=e.getAttribute(v.dev.key)||(null==(r=e.src.match(/[\w-. ]+(?=(\.js)$)/))?void 0:r[0]);return s&&!t.includes(s)&&t.push(s),t},[])},g=(t,e)=>{for(let r of e){if(t[r])continue;t[r]={};let s=t[r];s.loading=new Promise(t=>{s.resolve=e=>{t(e),delete s.resolve}})}},m=t=>{let e=Array.isArray(window.fsAttributes)?window.fsAttributes:[];t.push(...e)};(({scriptAttributes:t,attributeKey:e,version:r,init:s})=>{var i;A(),(i=window.fsAttributes)[e]||(i[e]={});let{preventsLoad:n,attributes:l}=h(t),u=window.fsAttributes[e];u.version=r,u.init=s,n||(window.Webflow||(window.Webflow=[]),window.Webflow.push(()=>s(l)))})({async init(){await n(i);let t=document.querySelectorAll("video");if(!t.length)return;let e=new Map,r=new IntersectionObserver(t=>{for(let{target:r,isIntersecting:s}of t)r instanceof HTMLVideoElement&&!r.hasAttribute("data-exclude-autovideo")&&!r.closest("[data-exclude-autovideo]")&&(s?r.play().catch(()=>{}):r.pause(),e.set(r,s))},{threshold:.1});for(let l of t)l.hasAttribute("data-exclude-autovideo")||l.closest("[data-exclude-autovideo]")||(l.autoplay=!1,l.playsInline=!0,e.set(l,null),r.observe(l));let a=u(document,"visibilitychange",()=>{for(let[t,r]of e)t.hasAttribute("data-exclude-autovideo")||t.closest("[data-exclude-autovideo]")||(document.hidden||!r?t.pause():t.play().catch(()=>{}))});return o(s,e,()=>{r.disconnect(),a()})},version:"1.5.0",attributeKey:s})})();
</script>

<!-- Remove the global PRISM -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var styleTag = document.getElementById('prism-global');
    if (styleTag) {
      styleTag.parentNode.removeChild(styleTag);
    }
  });
</script>


<!-- PRISM BLOG -->
<style>  
  /* Inline code */
  code[class*="language-"],
  pre[class*="language-"] {
    color: inherit;
  }

  .token.comment,
  .token.prolog,
  .token.doctype,
  .token.cdata {
    color: #008000;
    font-style: italic;
  }

  .token.namespace {
    opacity: .7;
  }

  .token.string {
    color: #A31515;
  }

  .token.punctuation,
  .token.operator {
    color: #393A34; /* no highlight */
  }

  .token.url,
  .token.symbol,
  .token.number,
  .token.boolean,
  .token.variable,
  .token.constant,
  .token.inserted {
    color: #36acaa;
  }

  .token.atrule,
  .token.keyword,
  .token.attr-value,
  .language-autohotkey .token.selector,
  .language-json .token.boolean,
  .language-json .token.number,
  code[class*="language-css"] {
    color: #0000ff;
  }

  .token.function {
    color: #393A34;
  }

  .token.deleted,
  .language-autohotkey .token.tag {
    color: #9a050f;
  }

  .token.selector,
  .language-autohotkey .token.keyword {
    color: #00009f;
  }

  .token.important {
    color: #e90;
  }

  .token.important,
  .token.bold {
    font-weight: bold;
  }

  .token.italic {
    font-style: italic;
  }

  .token.class-name,
  .language-json .token.property {
    color: #2B91AF;
  }

  .token.tag,
  .token.selector {
    color: #800000;
  }

  .token.attr-name,
  .token.property,
  .token.regex,
  .token.entity {
    color: #ff0000;
  }

  .token.directive.tag .tag {
    background: #ffff00;
    color: #393A34;
  }

  /* overrides color-values for the Line Numbers plugin
  * http://prismjs.com/plugins/line-numbers/
  */
  .line-numbers.line-numbers .line-numbers-rows {
    border-right-color: #a5a5a5;
  }

  .line-numbers .line-numbers-rows > span:before {
    color: #2B91AF;
  }

  /* overrides color-values for the Line Highlight plugin
  * http://prismjs.com/plugins/line-highlight/
  */
  .line-highlight.line-highlight {
    background: rgba(193, 222, 241, 0.2);
    background: -webkit-linear-gradient(left, rgba(193, 222, 241, 0.2) 70%, rgba(221, 222, 241, 0));
    background: linear-gradient(to right, rgba(193, 222, 241, 0.2) 70%, rgba(221, 222, 241, 0));
  }
</style>

<script>
  (function() {
    const init = function() {
      document.querySelectorAll('.blog-custom_tabs').forEach(function(wrap) {

        const tabItems = wrap.querySelectorAll('.tab');
        if (tabItems.length === 0) return

        const tabPanes = wrap.querySelectorAll('.blog-custom_tabs-inner');

        let currentIndex = 0;
        let mm = gsap.matchMedia();

        mm.add("(min-width: 992px)", () => {
          tabItems[0].classList.add('fs-cmsfilter_active');

          tabPanes.forEach((pane, i) => {
            gsap.set(pane, { 
              opacity: i === 0 ? 1 : 0, 
              display: i === 0 ? 'flex' : 'none' 
            });
          });

          const handleClick = function() {
            const newIndex = Array.from(tabItems).indexOf(this);
            if (newIndex === currentIndex) return;

            const currentPane = tabPanes[currentIndex];
            const newPane = tabPanes[newIndex];

            tabItems.forEach(item => item.classList.remove('fs-cmsfilter_active'));
            tabItems[newIndex].classList.add('fs-cmsfilter_active');

            gsap.timeline()
              .to(currentPane, {
              duration: 0.3,
              opacity: 0,
              onComplete: () => gsap.set(currentPane, { display: 'none' })
            })
              .set(newPane, { display: 'flex', opacity: 0 })
              .to(newPane, { duration: 0.3, opacity: 1 }, '-=0.1');

            currentIndex = newIndex;
          };

          tabItems.forEach(item => item.addEventListener('click', handleClick));

          return () => {
            tabItems.forEach(item => item.removeEventListener('click', handleClick));
          };
        });
      });
    };

    if (typeof gsap !== 'undefined') {
      init();
    } else {
      window.addEventListener('load', init);
    }
  })();
</script>

<script>
  function initHowlerJSAudioPlayer() {
    const howlerElements = document.querySelectorAll('[data-howler]');
    const soundInstances = {};

    howlerElements.forEach((element, index) => {
      const uniqueId = `howler-${index}`;
      element.id = uniqueId;
      element.setAttribute('data-howler-status', 'not-playing');

      const audioSrc = element.getAttribute('data-howler-src');
      const durationElement = element.querySelector('[data-howler-info="duration"]');
      const progressTextElement = element.querySelector('[data-howler-info="progress"]');
      const timelineContainer = element.querySelector('[data-howler-control="timeline"]');
      const timelineBar = element.querySelector('[data-howler-control="progress"]');
      const toggleButton = element.querySelector('[data-howler-control="toggle-play"]');

      const sound = new Howl({
        src: [audioSrc],
        html5: true,
        onload: () => {
          if (durationElement) durationElement.textContent = formatTime(sound.duration());
          const audioNode = sound._sounds?.[0]?._node;
          if (audioNode) {
            audioNode.addEventListener('pause', () => {
              if (sound.playing()) {
                sound.pause();
              }
            });
            audioNode.addEventListener('play', () => {
              if (!sound.playing()) {
                sound.play();
              }
            });
          }
        },
        onplay: () => {
          pauseAllExcept(uniqueId);
          element.setAttribute('data-howler-status', 'playing');
          requestAnimationFrame(updateProgress);
        },
        onpause: () => element.setAttribute('data-howler-status', 'not-playing'),
        onstop: () => element.setAttribute('data-howler-status', 'not-playing'),
        onend: () => {
          if (timelineBar) timelineBar.style.width = '100%';
          if (progressTextElement) progressTextElement.textContent = formatTime(sound.duration());
          setTimeout(resetUI, 100);
        },
      });

      soundInstances[uniqueId] = sound;

      function updateProgress() {
        if (!sound.playing()) return;
        updateUI();
        requestAnimationFrame(updateProgress);
      }

      function updateUI() {
        const currentTime = sound.seek() || 0;
        const duration = sound.duration() || 1;
        const progress = currentTime >= duration - 0.15 ? 100 : Math.min((currentTime / duration) * 100, 100);
        if (progressTextElement) progressTextElement.textContent = formatTime(currentTime);
        if (timelineBar) timelineBar.style.width = `${progress}%`;
        timelineContainer?.setAttribute('aria-valuenow', Math.round(progress));
      }

      function resetUI() {
        sound.seek(0);
        if (progressTextElement) progressTextElement.textContent = formatTime(0);
        if (timelineBar) timelineBar.style.width = '0%';
        timelineContainer?.setAttribute('aria-valuenow', 0);
        element.setAttribute('data-howler-status', 'not-playing');
      }

      function seekToPosition(event) {
        const rect = timelineContainer.getBoundingClientRect();
        const percentage = (event.clientX - rect.left) / rect.width;
        sound.seek(sound.duration() * percentage);
        if (!sound.playing()) {
          pauseAllExcept(uniqueId);
          sound.play();
          element.setAttribute('data-howler-status', 'playing');
        }
        updateUI();
      }

      function togglePlay() {
        if (sound.playing()) {
          sound.pause();
          toggleButton?.setAttribute('aria-pressed', false);
        } else {
          const currentTime = sound.seek() || 0;
          const duration = sound.duration() || 1;
          if (currentTime >= duration - 0.1) {
            sound.seek(0);
          }
          pauseAllExcept(uniqueId);
          sound.play();
          toggleButton?.setAttribute('aria-pressed', true);
        }
      }

      function pauseAllExcept(id) {
        Object.keys(soundInstances).forEach(otherId => {
          if (otherId !== id && soundInstances[otherId].playing()) {
            soundInstances[otherId].pause();
            document.getElementById(otherId)?.setAttribute('data-howler-status', 'not-playing');
          }
        });
      }

      function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${minutes}:${secs.toString().padStart(2, '0')}`;
      }

      toggleButton?.addEventListener('click', togglePlay);
      timelineContainer?.addEventListener('click', seekToPosition);
      sound.on('seek', updateUI);
      sound.on('play', updateUI);
    });

    return soundInstances;
  }

  document.addEventListener('DOMContentLoaded', function() {
    initHowlerJSAudioPlayer();
  });
</script></body></html>