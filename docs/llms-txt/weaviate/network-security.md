# Source: https://docs.weaviate.io/deploy/production/aws/network-security

<!doctype html>
<html lang="en" dir="ltr" class="docs-wrapper plugin-docs plugin-id-default docs-version-current docs-doc-page docs-doc-id-deploy/production/aws/network-security" data-has-hydrated="false">
<head>
<meta charset="UTF-8">
<meta name="generator" content="Docusaurus v3.9.2">
<title data-rh="true">AWS: Network security - Best practices | Weaviate Documentation</title><meta data-rh="true" name="viewport" content="width=device-width,initial-scale=1"><meta data-rh="true" name="twitter:card" content="summary_large_image"><meta data-rh="true" property="og:image" content="https://docs.weaviate.io/og/default.jpg"><meta data-rh="true" name="twitter:image" content="https://docs.weaviate.io/og/default.jpg"><meta data-rh="true" property="og:url" content="https://docs.weaviate.io/deploy/production/aws/network-security"><meta data-rh="true" property="og:locale" content="en"><meta data-rh="true" name="docusaurus_locale" content="en"><meta data-rh="true" name="docsearch:language" content="en"><meta data-rh="true" name="docusaurus_version" content="current"><meta data-rh="true" name="docusaurus_tag" content="docs-default-current"><meta data-rh="true" name="docsearch:version" content="current"><meta data-rh="true" name="docsearch:docusaurus_tag" content="docs-default-current"><meta data-rh="true" property="og:title" content="AWS: Network security - Best practices | Weaviate Documentation"><meta data-rh="true" name="description" content="Expert recommendations for maximizing network security in your Weaviate deployment."><meta data-rh="true" property="og:description" content="Expert recommendations for maximizing network security in your Weaviate deployment."><link data-rh="true" rel="icon" href="/img/favicon.ico"><link data-rh="true" rel="canonical" href="https://docs.weaviate.io/deploy/production/aws/network-security"><link data-rh="true" rel="alternate" href="https://docs.weaviate.io/deploy/production/aws/network-security" hreflang="en"><link data-rh="true" rel="alternate" href="https://docs.weaviate.io/deploy/production/aws/network-security" hreflang="x-default"><script data-rh="true" type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"AWS","item":"https://docs.weaviate.io/deploy/production/aws/"},{"@type":"ListItem","position":2,"name":"Network security - Best practices","item":"https://docs.weaviate.io/deploy/production/aws/network-security"}]}</script><link rel="preconnect" href="https://www.googletagmanager.com">
<script>window.dataLayer=window.dataLayer||[]</script>
<script>!function(e,t,a,n){e[n]=e[n]||[],e[n].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var g=t.getElementsByTagName(a)[0],m=t.createElement(a);m.async=!0,m.src="https://www.googletagmanager.com/gtm.js?id=GTM-WS8CG676",g.parentNode.insertBefore(m,g)}(window,document,"script","dataLayer")</script>

<script>!function(){if("undefined"!=typeof window&&void 0===window.signals){var n=document.createElement("script");n.src="https://cdn.cr-relay.com/v1/site/3709e2b3-c0eb-4239-9087-775e484fab16/signals.js",n.async=!0,window.signals=Object.assign([],["page","identify","form"].reduce((function(n,e){return n[e]=function(){return signals.push([e,arguments]),signals},n}),{})),document.head.appendChild(n)}}()</script>
<script id="hs-script-loader" async="true" defer="true" src="https://js.hs-scripts.com/8738733.js"></script>
<link rel="stylesheet" href="/fonts/font-awesome/fontawesome.css">
<link rel="stylesheet" href="/fonts/font-awesome/solid.css">
<link rel="stylesheet" href="/fonts/font-awesome/regular.css">
<link rel="stylesheet" href="/fonts/font-awesome/brands.css"><link rel="stylesheet" href="/assets/css/styles.f4cdad07.css">
<script src="/assets/js/runtime~main.444b5859.js" defer="defer"></script>
<script src="/assets/js/main.6a4a6ee2.js" defer="defer"></script>
</head>
<body class="navigation-with-keyboard">
<svg style="display: none;"><defs>
<symbol id="theme-svg-external-link" viewBox="0 0 24 24"><path fill="currentColor" d="M21 13v10h-21v-19h12v2h-10v15h17v-8h2zm3-12h-10.988l4.035 4-6.977 7.07 2.828 2.828 6.977-7.07 4.125 4.172v-11z"/></symbol>
</defs></svg>
<script>!function(){var t=function(){try{return new URLSearchParams(window.location.search).get("docusaurus-theme")}catch(t){}}()||function(){try{return window.localStorage.getItem("theme")}catch(t){}}();document.documentElement.setAttribute("data-theme",t||"light"),document.documentElement.setAttribute("data-theme-choice",t||"light")}(),function(){try{const a=new URLSearchParams(window.location.search).entries();for(var[t,e]of a)if(t.startsWith("docusaurus-data-")){var n=t.replace("docusaurus-data-","data-");document.documentElement.setAttribute(n,e)}}catch(t){}}(),document.documentElement.setAttribute("data-announcement-bar-initially-dismissed",function(){try{return"true"===localStorage.getItem("docusaurus.announcement.dismiss")}catch(t){}return!1}())</script>


<script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WS8CG676" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript><div id="__docusaurus"><link rel="preload" as="image" href="/img/site/weaviate-logo-horizontal-light-1.svg"><link rel="preload" as="image" href="/img/site/weaviate-logo-horizontal-dark-1.svg"><link rel="preload" as="image" href="/img/site/weaviate-logo-w.png"><div role="region" aria-label="Skip to main content"><a class="skipToContent_fXgn" href="#__docusaurus_skipToContent_fallback">Skip to main content</a></div><div class="theme-announcement-bar announcementBar_mb4j" style="background-color:#1C1468;color:#F5F5F5" role="banner"><div class="announcementBarPlaceholder_vyr4"></div><div class="content_knG7 announcementBarContent_xLdY"><a href="https://academy.weaviate.io/">The new <b>Weaviate Academy</b> learning platform is here!</a></div><button type="button" aria-label="Close" class="clean-btn close closeButton_CVFx announcementBarClose_gvF7"><svg viewBox="0 0 15 15" width="14" height="14"><g stroke="currentColor" stroke-width="3.1"><path d="M.75.75l13.5 13.5M14.25.75L.75 14.25"></path></g></svg></button></div><div class="defaultNavbar_mOWn"><nav aria-label="Main" class="theme-layout-navbar navbar navbar--fixed-top"><div class="navbar__inner"><div class="theme-layout-navbar-left navbar__items"><button aria-label="Toggle navigation bar" aria-expanded="false" class="navbar__toggle clean-btn" type="button"><svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><path stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2" d="M4 7h22M4 15h22M4 23h22"></path></svg></button><a href="https://weaviate.io" target="_blank" rel="noopener noreferrer" class="navbar__brand"><div class="navbar__logo"><img src="/img/site/weaviate-logo-horizontal-light-1.svg" alt="Weaviate" class="themedComponent_mlkZ themedComponent--light_NVdE"><img src="/img/site/weaviate-logo-horizontal-dark-1.svg" alt="Weaviate" class="themedComponent_mlkZ themedComponent--dark_xIcU"></div><b class="navbar__title text--truncate"></b></a><a class="navbar__item navbar__link" href="/weaviate/api/rest"></a></div><div class="theme-layout-navbar-right navbar__items navbar__items--right"><a href="https://github.com/weaviate/weaviate" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link"><svg class="githubStars" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>GitHub</title><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a><a href="https://academy.weaviate.io" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link academy-button">Academy</a><a href="https://weaviate.io/go/console?utm_source=docs&amp;utm_content=navbar" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link cloud-button">Weaviate Cloud</a><div class="hiddenSearch navbarSearchContainer_Bca1"><div class="searchBox"><button class="searchButton"><span class="searchPlaceholder"><i class="searchIcon fas fa-magnifying-glass"></i><span class="searchPlaceholderText">Ask AI or Search</span></span><div class="commandIconContainer"><span class="commandIcon">⌘K</span></div></button></div></div><div class="toggle_vylO colorModeToggle_DEke"><button class="clean-btn toggleButton_gllP toggleButtonDisabled_aARS" type="button" disabled="" title="system mode" aria-label="Switch between dark and light mode (currently system mode)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP lightToggleIcon_pyhR"><path fill="currentColor" d="M12,9c1.65,0,3,1.35,3,3s-1.35,3-3,3s-3-1.35-3-3S10.35,9,12,9 M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5 S14.76,7,12,7L12,7z M2,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13l2,0c0.55,0,1-0.45,1-1 s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1C11.45,19,11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0 c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95 c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41 L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41 s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06 c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z"></path></svg><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP darkToggleIcon_wfgR"><path fill="currentColor" d="M9.37,5.51C9.19,6.15,9.1,6.82,9.1,7.5c0,4.08,3.32,7.4,7.4,7.4c0.68,0,1.35-0.09,1.99-0.27C17.45,17.19,14.93,19,12,19 c-3.86,0-7-3.14-7-7C5,9.07,6.81,6.55,9.37,5.51z M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36 c-0.98,1.37-2.58,2.26-4.4,2.26c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z"></path></svg><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP systemToggleIcon_QzmC"><path fill="currentColor" d="m12 21c4.971 0 9-4.029 9-9s-4.029-9-9-9-9 4.029-9 9 4.029 9 9 9zm4.95-13.95c1.313 1.313 2.05 3.093 2.05 4.95s-0.738 3.637-2.05 4.95c-1.313 1.313-3.093 2.05-4.95 2.05v-14c1.857 0 3.637 0.737 4.95 2.05z"></path></svg></button></div></div></div><div role="presentation" class="navbar-sidebar__backdrop"></div></nav></div><div class="secondaryNavbar_Zq6r"><nav class="secondaryNavLinks_WJZI"><a class="navLink_kzb_" href="/deploy">Get started</a><a class="navLink_kzb_" href="/deploy/configuration">Configuration</a><a class="navLink_kzb_ activeNavLink_ObEy" href="/deploy/production">Production guides</a><a class="navLink_kzb_" href="/deploy/faqs">FAQs</a><a class="navLink_kzb_" href="/deploy/migration">Migration</a></nav></div><div class="modalOverlay_BeVA"><div class="modalContent_CPV2"><div class="modalHeader_aBIn"><div class="modalHeaderLeft_Jnp2"><strong>Go to documentation:</strong></div><div class="modalHeaderRight_pW31"><div class="modalHeaderButton_lyv9"><span class="buttonShortcut_rHzY">⌘U</span><div class="verticalDivider_TWYg"></div><button class="headerCloseIcon_Nc0n">✕</button></div></div></div><div class="modalBody_bZ4G"><div class="modalOptionsContainer_GF7c"><div class="modalOption_Zqj6"><i class="fa fa-database modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Database</strong><p>Develop AI applications using Weaviate&#x27;s APIs and tools</p></div></div><div class="modalOption_Zqj6 activeOption_IUKI"><i class="fa fa-database modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Deploy</strong><p>Deploy, configure, and maintain Weaviate Database</p></div><div class="activeIndicator_uCqh"></div></div><div class="modalOption_Zqj6"><i class="fa fa-robot modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Agents</strong><p>Build and deploy intelligent agents with Weaviate</p></div></div><div class="modalOption_Zqj6"><i class="fa fa-cloud modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Cloud</strong><p>Manage and scale Weaviate in the cloud</p></div></div></div><div class="resourcesSection__QVP"><h4 class="sectionTitle_TjaJ">Additional resources</h4><div class="resourcesGrid_Fe8L"><div class="resourceCard_qG9v"><i class="fa fa-puzzle-piece resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Integrations</span></div><div class="resourceCard_qG9v"><i class="fa fa-edit resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Contributor guide</span></div><div class="resourceCard_qG9v"><i class="fa fa-calendar-days resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Events &amp; Workshops</span></div><div class="resourceCard_qG9v"><i class="fa-solid fa-graduation-cap resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Weaviate Academy</span></div></div></div><div class="aiAssistantSection_Qefr"><h4 class="sectionTitle_TjaJ">Need help?</h4><div class="resourcesGrid_Fe8L"><div class="askAiButton_snh2"><img src="/img/site/weaviate-logo-w.png" alt="Weaviate Logo" class="askAiIcon_T_rP"><span class="askAiText_snFq">Ask AI Assistant</span><span class="askAiShortcut_kkRQ">⌘K</span></div><div class="resourceCard_qG9v"><i class="fa fa-comments styles.resourceIcon" aria-hidden="true"></i><span class="resourceTitle__PWa">Community Forum</span></div></div></div></div></div></div><div id="__docusaurus_skipToContent_fallback" class="theme-layout-main main-wrapper mainWrapper_z2l0"><div class="docsWrapper_hBAB"><button aria-label="Scroll back to top" class="clean-btn theme-back-to-top-button backToTopButton_sjWU" type="button"></button><div class="docRoot_UBD9"><aside class="theme-doc-sidebar-container docSidebarContainer_YfHR"><div class="sidebarViewport_aRkj"><div class="sidebar_njMd"><nav aria-label="Docs sidebar" class="menu thin-scrollbar menu_SIkG menuWithAnnouncementBar_GW3s"><ul class="theme-doc-sidebar-menu menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/deploy/production"><span title="Overview" class="linkLabel_WmDU">Overview</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1"><hr class="sidebar-divider"></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item sidebar-main-category"><div class="menu__list-item-collapsible"><a class="categoryLink_byQd menu__link" href="/deploy/production/kubernetes"><span title="Kubernetes" class="categoryLinkLabel_W154">Kubernetes</span></a></div><ul class="menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item sidebar-item"><a class="menu__link" tabindex="0" href="/deploy/production/kubernetes/get-to-production"><span title="Getting to production" class="linkLabel_WmDU">Getting to production</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item sidebar-item"><a class="menu__link" tabindex="0" href="/deploy/production/kubernetes/production-readiness"><span title="Production readiness self-assessment" class="linkLabel_WmDU">Production readiness self-assessment</span></a></li></ul></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1"><hr class="sidebar-divider"></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item sidebar-main-category"><div class="menu__list-item-collapsible"><a class="categoryLink_byQd menu__link menu__link--active" href="/deploy/production/aws"><span title="AWS" class="categoryLinkLabel_W154">AWS</span></a></div><ul class="menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item sidebar-item"><a class="menu__link" tabindex="0" href="/deploy/production/aws/hardening-eks"><span title="Hardening EKS deployments" class="linkLabel_WmDU">Hardening EKS deployments</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item sidebar-item"><a class="menu__link menu__link--active" aria-current="page" tabindex="0" href="/deploy/production/aws/network-security"><span title="Network security - Best practices" class="linkLabel_WmDU">Network security - Best practices</span></a></li></ul></li></ul></nav><button type="button" title="Collapse sidebar" aria-label="Collapse sidebar" class="button button--secondary button--outline collapseSidebarButton_PEFL"><svg width="20" height="20" aria-hidden="true" class="collapseSidebarButtonIcon_kv0_"><g fill="#7a7a7a"><path d="M9.992 10.023c0 .2-.062.399-.172.547l-4.996 7.492a.982.982 0 01-.828.454H1c-.55 0-1-.453-1-1 0-.2.059-.403.168-.551l4.629-6.942L.168 3.078A.939.939 0 010 2.528c0-.548.45-.997 1-.997h2.996c.352 0 .649.18.828.45L9.82 9.472c.11.148.172.347.172.55zm0 0"></path><path d="M19.98 10.023c0 .2-.058.399-.168.547l-4.996 7.492a.987.987 0 01-.828.454h-3c-.547 0-.996-.453-.996-1 0-.2.059-.403.168-.551l4.625-6.942-4.625-6.945a.939.939 0 01-.168-.55 1 1 0 01.996-.997h3c.348 0 .649.18.828.45l4.996 7.492c.11.148.168.347.168.55zm0 0"></path></g></svg></button></div></div></aside><main class="docMainContainer_TBSr"><div class="container padding-top--md padding-bottom--lg"><div class="row"><div class="col docItemCol_z5aJ"><div class="docItemContainer_c0TR"><article><nav class="theme-doc-breadcrumbs breadcrumbsContainer_Z_bl" aria-label="Breadcrumbs"><ul class="breadcrumbs"><li class="breadcrumbs__item"><a class="breadcrumbs__link" href="/deploy/production/aws"><span>AWS</span></a></li><li class="breadcrumbs__item breadcrumbs__item--active"><span class="breadcrumbs__link">Network security - Best practices</span></li></ul></nav><div class="tocCollapsible_ETCw theme-doc-toc-mobile tocMobile_ITEo"><button type="button" class="clean-btn tocCollapsibleButton_TO0P">On this page</button></div><div class="theme-doc-markdown markdown"><header><h1>AWS: Network security - Best practices</h1></header><p>This page serves as a reference for AWS-specific networking best practices for your Weaviate deployment. It outlines a network security architecture designed to protect your Weaviate deployments.</p>
<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewBox="0 0 12 16"><path fill-rule="evenodd" d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z"></path></svg></span>tip</div><div class="admonitionContent_BuS1"><ul>
<li class="">
<p>If you need general best practices, you can find them <a class="" href="/weaviate/best-practices">here</a>.</p>
</li>
<li class="">
<p>If you need deployment-specific best practices, you can find them <a class="" href="/deploy/faqs">here</a>.</p>
</li>
</ul></div></div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="a-robust-network-security-architecture-will">A robust network security architecture will:<a href="#a-robust-network-security-architecture-will" class="hash-link" aria-label="Direct link to A robust network security architecture will:" title="Direct link to A robust network security architecture will:" translate="no">​</a></h3>
<ul>
<li class="">Minimize the attack surface through network segmentation and access controls.</li>
<li class="">Enable automated scaling while maintaining security boundaries.</li>
<li class="">Ensure high availability with comprehensive disaster recovery.</li>
<li class="">Provide end-to-end observability and threat detection.</li>
<li class="">Establish secure administrative access patterns.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="access-control">Access control<a href="#access-control" class="hash-link" aria-label="Direct link to Access control" title="Direct link to Access control" translate="no">​</a></h3>
<p>Access control is the cornerstone of this network security strategy. It implements a zero-trust model where no resource is inherently trusted with continuous verification of all access requests.</p>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="private-subnet-strategy">Private subnet strategy<a href="#private-subnet-strategy" class="hash-link" aria-label="Direct link to Private subnet strategy" title="Direct link to Private subnet strategy" translate="no">​</a></h4>
<p>Network isolation is the foundation of our this strategy. Critical infrastructure should reside in private subnets with no direct internet connectivity. This eliminates internet-based attacks and forces all access through controlled entry points.</p>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="core-components">Core components<a href="#core-components" class="hash-link" aria-label="Direct link to Core components" title="Direct link to Core components" translate="no">​</a></h4>
<ul>
<li class="">Private subnets with NAT gateways providing controlled outbound internet access.</li>
<li class="">Multi-factor authentication (MFA) for all administrative access.</li>
<li class="">Security groups implementing the principle of least privilege enforced through granular permissions.</li>
<li class="">ALBs with integrated WAF protection.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="access-patterns">Access patterns<a href="#access-patterns" class="hash-link" aria-label="Direct link to Access patterns" title="Direct link to Access patterns" translate="no">​</a></h4>
<ul>
<li class="">Ingress traffic filtered through load balancers and security groups.</li>
<li class="">Egress traffic controlled through NAT gateways with logging.</li>
<li class="">Administrative access requiring a VPN and strong authentication.</li>
<li class="">RBAC aligned with organizational structure.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="vpn-strategy-for-secure-administrative-access">VPN strategy for secure administrative access<a href="#vpn-strategy-for-secure-administrative-access" class="hash-link" aria-label="Direct link to VPN strategy for secure administrative access" title="Direct link to VPN strategy for secure administrative access" translate="no">​</a></h4>
<ul>
<li class="">Site-to-site VPN for corporate office connectivity.</li>
<li class="">Client VPN with individual certificates for administrative access.</li>
<li class="">Multi-AZ VPN gateways ensuring high availability.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="kubernetes-access-control">Kubernetes access control<a href="#kubernetes-access-control" class="hash-link" aria-label="Direct link to Kubernetes access control" title="Direct link to Kubernetes access control" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="administrative-controls">Administrative controls<a href="#administrative-controls" class="hash-link" aria-label="Direct link to Administrative controls" title="Direct link to Administrative controls" translate="no">​</a></h4>
<ul>
<li class="">All <code>kubectl</code> access requires an established VPN connection.</li>
<li class="">Integration with corporate IDPs.</li>
<li class="">MFA for all administrative operations.</li>
<li class="">Session timeout and activity monitoring.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="network-architecture-with-defense-in-depth">Network architecture with defense-in-depth<a href="#network-architecture-with-defense-in-depth" class="hash-link" aria-label="Direct link to Network architecture with defense-in-depth" title="Direct link to Network architecture with defense-in-depth" translate="no">​</a></h3>
<p>Security boundaries are created with network segmentation, this limits the potential impact of security breaches. This defense-in-depth strategy implements both horizontal and vertical segmentation.</p>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="application-tier-segmentation">Application tier segmentation<a href="#application-tier-segmentation" class="hash-link" aria-label="Direct link to Application tier segmentation" title="Direct link to Application tier segmentation" translate="no">​</a></h4>
<p>The application tier hosts all customer-facing services and business logic components:</p>
<ul>
<li class="">Dedicated subnets per application environment (development,staging, production).</li>
<li class="">WAFs inspecting all inbound HTTP/HTTPS traffic.</li>
<li class="">Container network isolation using Kubernetes network policies.</li>
<li class="">API gateway enforcement of authentication and rate limiting.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="database-tier-isolation">Database tier isolation<a href="#database-tier-isolation" class="hash-link" aria-label="Direct link to Database tier isolation" title="Direct link to Database tier isolation" translate="no">​</a></h4>
<p>The database tier (where Weaviate is deployed) requires enhanced security due to potentially sensitive data storage.</p>
<ul>
<li class="">Private subnets with no internet route.</li>
<li class="">Database activity monitoring and audit logging.</li>
<li class="">Routine security patching and vulnerability assessments.</li>
<li class="">Backup systems in isolated subnets with restricted access.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="monitoring-infrastructure">Monitoring infrastructure<a href="#monitoring-infrastructure" class="hash-link" aria-label="Direct link to Monitoring infrastructure" title="Direct link to Monitoring infrastructure" translate="no">​</a></h4>
<p>Centralized monitoring and observability infrastructure requires special considerations to prevent blind spots during security incidents.</p>
<ul>
<li class="">Isolated subnets prevent monitoring system compromise.</li>
<li class="">Separate administrative access paths for monitoring systems.</li>
<li class="">Network-level isolation preventing lateral movement to monitoring systems.</li>
<li class="">Access controls limiting monitoring data to authorized personnel.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="vpc-endpoints-and-private-connectivity">VPC endpoints and private connectivity<a href="#vpc-endpoints-and-private-connectivity" class="hash-link" aria-label="Direct link to VPC endpoints and private connectivity" title="Direct link to VPC endpoints and private connectivity" translate="no">​</a></h3>
<p>Implementing CloudWatch VPC endpoint eliminates internet routing for monitoring data, these are the requirements for configuration:</p>
<ul>
<li class="">Interface VPC endpoint deployment in each availability zone.</li>
<li class="">DNS resolution configuration for seamless service integration.</li>
<li class="">Security group rules allowing HTTPS traffic from monitoring sources.</li>
<li class="">Route table configuration directing CloudWatch API calls to VPC endpoint.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="security-benefits">Security benefits<a href="#security-benefits" class="hash-link" aria-label="Direct link to Security benefits" title="Direct link to Security benefits" translate="no">​</a></h4>
<ul>
<li class="">Monitoring data will never reach the public internet.</li>
<li class="">Eliminating internet gateway dependency reduces attack surface.</li>
<li class="">Network-level access controls for monitoring data transmission.</li>
<li class="">Compliance with data residency requirements.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="s3-vpc-endpoint-for-secure-data-operations">S3 VPC endpoint for secure data operations<a href="#s3-vpc-endpoint-for-secure-data-operations" class="hash-link" aria-label="Direct link to S3 VPC endpoint for secure data operations" title="Direct link to S3 VPC endpoint for secure data operations" translate="no">​</a></h4>
<p>Data transfer for backups and application data can be secured, this is what is needed for configuration:</p>
<ul>
<li class="">Route table entries to direct S3 traffic through the VPC endpoint(s).</li>
<li class="">Bucket policies that restrict access to VPC endpoint traffic.</li>
<li class="">IAM policies to control which services can access S3 resources.</li>
<li class="">CloudTrail logging for all S3 API operations.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="performance-and-security-optimization">Performance and security optimization<a href="#performance-and-security-optimization" class="hash-link" aria-label="Direct link to Performance and security optimization" title="Direct link to Performance and security optimization" translate="no">​</a></h4>
<ul>
<li class="">Eliminates NAT gateway costs for S3 traffic.</li>
<li class="">Improved data transfer performance through AWS.</li>
<li class="">Network-level protection prevents data exfiltration through the internet.</li>
<li class="">Integration with AWS Config for compliance monitoring.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="scaling-and-performance-strategies">Scaling and performance strategies<a href="#scaling-and-performance-strategies" class="hash-link" aria-label="Direct link to Scaling and performance strategies" title="Direct link to Scaling and performance strategies" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="application-load-balancer-alb-configuration">Application load balancer (ALB) configuration<a href="#application-load-balancer-alb-configuration" class="hash-link" aria-label="Direct link to Application load balancer (ALB) configuration" title="Direct link to Application load balancer (ALB) configuration" translate="no">​</a></h4>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="ssltls-management">SSL/TLS management<a href="#ssltls-management" class="hash-link" aria-label="Direct link to SSL/TLS management" title="Direct link to SSL/TLS management" translate="no">​</a></h4>
<ul>
<li class="">Automated certificate provisioning through AWS Certificate Manager.</li>
<li class="">PFS enabled for all connections.</li>
<li class="">HTTP to HTTPS redirection preventing unencrypted communications.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="waf-integration">WAF integration<a href="#waf-integration" class="hash-link" aria-label="Direct link to WAF integration" title="Direct link to WAF integration" translate="no">​</a></h4>
<ul>
<li class="">WAF rules protecting against common web vulnerabilities.</li>
<li class="">Custom rules based on application-specific threat patterns.</li>
<li class="">Managed rule sets for OWASP Top 10 protection.</li>
<li class="">Real-time metrics and alerting for blocked requests.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="health-check-configuration">Health check configuration<a href="#health-check-configuration" class="hash-link" aria-label="Direct link to Health check configuration" title="Direct link to Health check configuration" translate="no">​</a></h4>
<ul>
<li class="">Application-specific health checks verifying service functionality.</li>
<li class="">Multi-tier health checks ensuring database connectivity.</li>
<li class="">Graceful handling of unhealthy targets during scaling events.</li>
<li class="">Custom health check endpoints providing details service status.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="autoscaling-security-considerations">Autoscaling security considerations<a href="#autoscaling-security-considerations" class="hash-link" aria-label="Direct link to Autoscaling security considerations" title="Direct link to Autoscaling security considerations" translate="no">​</a></h3>
<p>Secure scaling policies maintains security posture during capacity changes.</p>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="scaling-triggers">Scaling triggers<a href="#scaling-triggers" class="hash-link" aria-label="Direct link to Scaling triggers" title="Direct link to Scaling triggers" translate="no">​</a></h4>
<ul>
<li class="">CPU utilization with security-adjusted thresholds.</li>
<li class="">Memory utilization accounting for security tooling overhead.</li>
<li class="">Custom metrics, including security event rates.</li>
<li class="">Predictive scaling based on historical patterns and threat intelligence.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="security-during-scaling">Security during scaling<a href="#security-during-scaling" class="hash-link" aria-label="Direct link to Security during scaling" title="Direct link to Security during scaling" translate="no">​</a></h4>
<ul>
<li class="">Automated security group updates for new instances.</li>
<li class="">Security tooling deployment through user data scripts.</li>
<li class="">Configuration management to ensure consistent security baselines.</li>
<li class="">Monitoring integration providing immediate visibility into new instances.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="high-availability-and-disaster-recovery">High availability and disaster recovery<a href="#high-availability-and-disaster-recovery" class="hash-link" aria-label="Direct link to High availability and disaster recovery" title="Direct link to High availability and disaster recovery" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="multi-az-architecture">Multi-AZ architecture<a href="#multi-az-architecture" class="hash-link" aria-label="Direct link to Multi-AZ architecture" title="Direct link to Multi-AZ architecture" translate="no">​</a></h4>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="weaviate-configuration">Weaviate configuration<a href="#weaviate-configuration" class="hash-link" aria-label="Direct link to Weaviate configuration" title="Direct link to Weaviate configuration" translate="no">​</a></h4>
<ul>
<li class=""><strong>Minimum</strong> 3 replicas distributed across AZs.</li>
<li class="">Automatic failover and cross-AZ replication.</li>
<li class="">Automated backups to S3 with cross-region replication.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="observability-and-monitoring">Observability and monitoring<a href="#observability-and-monitoring" class="hash-link" aria-label="Direct link to Observability and monitoring" title="Direct link to Observability and monitoring" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="grafana-infrastructure">Grafana infrastructure<a href="#grafana-infrastructure" class="hash-link" aria-label="Direct link to Grafana infrastructure" title="Direct link to Grafana infrastructure" translate="no">​</a></h4>
<ul>
<li class="">Centralized dashboards for system health and security metrics.</li>
<li class="">Tiered alerting to prevent notification fatigue.</li>
<li class="">Integration with incident response systems.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="network-visibility">Network visibility<a href="#network-visibility" class="hash-link" aria-label="Direct link to Network visibility" title="Direct link to Network visibility" translate="no">​</a></h4>
<ul>
<li class="">VPC flow logs to capture traffic metadata for security analysis.</li>
<li class="">Real0time streaming to SIEMs.</li>
<li class="">Baseline establishment and anomaly detection.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="security-monitoring">Security monitoring<a href="#security-monitoring" class="hash-link" aria-label="Direct link to Security monitoring" title="Direct link to Security monitoring" translate="no">​</a></h4>
<ul>
<li class="">Threat detection using behavioral analysis and threat intelligence.</li>
<li class="">Automated incident creation and response workflows.</li>
<li class="">Forensic data collection and preservation capabilities.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="service-mesh-security">Service mesh security<a href="#service-mesh-security" class="hash-link" aria-label="Direct link to Service mesh security" title="Direct link to Service mesh security" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="istio-implementation">Istio implementation<a href="#istio-implementation" class="hash-link" aria-label="Direct link to Istio implementation" title="Direct link to Istio implementation" translate="no">​</a></h4>
<p>Istio is a service mesh that provides comprehensive security and observability for service communications.</p>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="key-features">Key features<a href="#key-features" class="hash-link" aria-label="Direct link to Key features" title="Direct link to Key features" translate="no">​</a></h4>
<ul>
<li class=""><strong>Mutual TLS (mTLS):</strong> Automatic encryption and authentication for all service communications.</li>
<li class=""><strong>Certificate management:</strong> Automated provisioning, rotation, and revocation.</li>
<li class=""><strong>Identity verification:</strong> Pod-level authentication before communication establishment.</li>
</ul>
<p>Istio also has a zero-trust model which has these features:</p>
<ul>
<li class="">Default deny-all policies requiring explicit communication permissions.</li>
<li class="">Continuous identity verification for all service requests.</li>
<li class="">Fine-grained traffic policies supporting security and deployment requirements.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="benefits">Benefits<a href="#benefits" class="hash-link" aria-label="Direct link to Benefits" title="Direct link to Benefits" translate="no">​</a></h4>
<ul>
<li class="">Encryption without application code changes.</li>
<li class="">Centralized policy enforcement across all services.</li>
<li class="">Detailed traffic analytics and security monitoring.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="kubernetes-network-policies">Kubernetes network policies<a href="#kubernetes-network-policies" class="hash-link" aria-label="Direct link to Kubernetes network policies" title="Direct link to Kubernetes network policies" translate="no">​</a></h3>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="calico-or-cilium-implementation">Calico or Cilium implementation<a href="#calico-or-cilium-implementation" class="hash-link" aria-label="Direct link to Calico or Cilium implementation" title="Direct link to Calico or Cilium implementation" translate="no">​</a></h4>
<ul>
<li class="">Advanced network policy features with pod-level segmentation.</li>
<li class="">eBPF-based enforcement for optimal performance.</li>
<li class="">Application-aware policies supporting HTTP/gRPC.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="policy-framework">Policy framework<a href="#policy-framework" class="hash-link" aria-label="Direct link to Policy framework" title="Direct link to Policy framework" translate="no">​</a></h4>
<ul>
<li class=""><strong>Default deny:</strong> all traffic is blocked by default.</li>
<li class=""><strong>Namespace isolation:</strong> prevents unauthorized cross-namespace communications.</li>
<li class=""><strong>Selective allow:</strong> Explicit rules for required communications.</li>
<li class=""><strong>GitOps management:</strong> Version-controlled policy deployment and testing.</li>
</ul>
<h4 class="anchor anchorTargetStickyNavbar_Vzrq" id="implementation">Implementation<a href="#implementation" class="hash-link" aria-label="Direct link to Implementation" title="Direct link to Implementation" translate="no">​</a></h4>
<ul>
<li class="">Network policies should prevent lateral movement between pods.</li>
<li class="">Integration with service mesh for consistent enforcement.</li>
<li class="">Regular policy auditing and optimization.</li>
<li class="">Automated testing to ensure policy effectiveness.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="framework-alignment">Framework alignment<a href="#framework-alignment" class="hash-link" aria-label="Direct link to Framework alignment" title="Direct link to Framework alignment" translate="no">​</a></h3>
<p>Our AWS-specific best practices are aligned with the following security frameworks:</p>
<ul>
<li class=""><strong>NIST Cybersecurity framework:</strong> Complete identify, protect, detect, respond, and recover capabilities.</li>
<li class=""><strong>ISO 27001:</strong> Information security management system implementation.</li>
<li class=""><strong>SOC 2:</strong> Trust services criteria compliance for security, availability, and confidentiality.</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="additional-resources-and-information">Additional resources and information<a href="#additional-resources-and-information" class="hash-link" aria-label="Direct link to Additional resources and information" title="Direct link to Additional resources and information" translate="no">​</a></h3>
<ul>
<li class=""><a class="" href="/deploy/configuration/monitoring">Monitoring documentation</a></li>
<li class=""><a class="" href="/deploy/configuration/replication">Replication documentation</a></li>
<li class=""><a class="" href="/deploy/configuration/backups">Backups documentation</a></li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="questions-and-feedback">Questions and feedback<a href="#questions-and-feedback" class="hash-link" aria-label="Direct link to Questions and feedback" title="Direct link to Questions and feedback" translate="no">​</a></h2>
<!-- -->
<p>If you have any questions or feedback, let us know in the <a href="https://forum.weaviate.io/" target="_blank" rel="noopener noreferrer" class="">user forum</a>.</p>
<!-- -->
<!-- -->
<div class="cardsSection_Ezca smallCards_eRph"><a href="https://forum.weaviate.io/new-topic?title=%5BQuestion%5D%20YOUR%20TOPIC&amp;body=Details%20here&amp;category=support&amp;tags=technical" target="_blank" rel="noopener noreferrer" class="card_OoQD"><div class="cardHeader_rXdg"><i class="fas fa-comments cardIcon_K4xK"></i><span class="cardTitle_TsZq">Technical questions</span></div><p class="cardDescription__QXy">If you have questions feel free to post on our<!-- --> <span class="highlight_acB9">Community forum</span>.</p></a><a href="https://github.com/weaviate/docs/issues" target="_blank" rel="noopener noreferrer" class="card_OoQD"><div class="cardHeader_rXdg"><i class="fa-brands fa-github cardIcon_K4xK"></i><span class="cardTitle_TsZq">Documentation feedback</span></div><p class="cardDescription__QXy">Leave feedback by opening a GitHub issue.</p></a></div></div><footer class="theme-doc-footer docusaurus-mt-lg"><div class="row margin-top--sm theme-doc-footer-edit-meta-row"><div class="col noPrint_WFHX"><a href="https://github.com/weaviate/docs/tree/main/docs/deploy/production/aws/network-security.md" target="_blank" rel="noopener noreferrer" class="theme-edit-this-page"><svg fill="currentColor" height="20" width="20" viewBox="0 0 40 40" class="iconEdit_Z9Sw" aria-hidden="true"><g><path d="m34.5 11.7l-3 3.1-6.3-6.3 3.1-3q0.5-0.5 1.2-0.5t1.1 0.5l3.9 3.9q0.5 0.4 0.5 1.1t-0.5 1.2z m-29.5 17.1l18.4-18.5 6.3 6.3-18.4 18.4h-6.3v-6.2z"></path></g></svg>Edit this page</a></div><div class="col lastUpdated_JAkA"></div></div><footer class="footer_G0fi"><div class="container"><div class="footerContent_oI6g"><div class="leftSection_TIm0"><div class="socialIcons_Okfn"><a href="https://github.com/weaviate/weaviate" target="_blank" rel="noopener noreferrer" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a><a href="https://weaviate.io/slack" target="_blank" rel="noopener noreferrer" title="Slack"><i class="fab fa-slack" aria-hidden="true"></i></a><a href="https://x.com/weaviate_io" target="_blank" rel="noopener noreferrer" title="X"><i class="fab fa-twitter" aria-hidden="true"></i></a><a href="https://instagram.com/weaviate.io" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a><a href="https://youtube.com/@Weaviate" target="_blank" rel="noopener noreferrer" title="YouTube"><i class="fab fa-youtube" aria-hidden="true"></i></a><a href="https://www.linkedin.com/company/weaviate-io" target="_blank" rel="noopener noreferrer" title="LinkedIn"><i class="fab fa-linkedin" aria-hidden="true"></i></a></div></div><div class="rightSection_LCNx"><div class="footerSection_l31a"><h5>Documentation</h5><ul><li><a href="/weaviate">Weaviate Database</a></li><li><a href="/deploy">Deployment documentation</a></li><li><a href="/cloud">Weaviate Cloud</a></li><li><a href="/agents">Weaviate Agents</a></li></ul></div><div class="footerSection_l31a"><h5>Support</h5><ul><li><a href="https://forum.weaviate.io/c/support/" target="_blank" rel="noopener noreferrer">Forum</a></li><li><a href="https://weaviate.io/slack" target="_blank" rel="noopener noreferrer">Slack</a></li></ul></div></div></div></div></footer></footer></article></div></div><div class="col col--3"><div class="customTocStickyContainer_xbxO"><div class="tableOfContents_bqdL thin-scrollbar theme-doc-toc-desktop"><ul class="table-of-contents table-of-contents__left-border"><li><a href="#a-robust-network-security-architecture-will" class="table-of-contents__link toc-highlight">A robust network security architecture will:</a></li><li><a href="#access-control" class="table-of-contents__link toc-highlight">Access control</a></li><li><a href="#kubernetes-access-control" class="table-of-contents__link toc-highlight">Kubernetes access control</a></li><li><a href="#network-architecture-with-defense-in-depth" class="table-of-contents__link toc-highlight">Network architecture with defense-in-depth</a></li><li><a href="#vpc-endpoints-and-private-connectivity" class="table-of-contents__link toc-highlight">VPC endpoints and private connectivity</a></li><li><a href="#scaling-and-performance-strategies" class="table-of-contents__link toc-highlight">Scaling and performance strategies</a></li><li><a href="#autoscaling-security-considerations" class="table-of-contents__link toc-highlight">Autoscaling security considerations</a></li><li><a href="#high-availability-and-disaster-recovery" class="table-of-contents__link toc-highlight">High availability and disaster recovery</a></li><li><a href="#observability-and-monitoring" class="table-of-contents__link toc-highlight">Observability and monitoring</a></li><li><a href="#service-mesh-security" class="table-of-contents__link toc-highlight">Service mesh security</a></li><li><a href="#kubernetes-network-policies" class="table-of-contents__link toc-highlight">Kubernetes network policies</a></li><li><a href="#framework-alignment" class="table-of-contents__link toc-highlight">Framework alignment</a></li><li><a href="#additional-resources-and-information" class="table-of-contents__link toc-highlight">Additional resources and information</a></li><li><a href="#questions-and-feedback" class="table-of-contents__link toc-highlight">Questions and feedback</a></li></ul></div><div class="container_jpeN"><p class="text_tGp7">Was this page helpful?</p><div class="buttonContainer_rFWk"><button class="voteButton_HXmX undefined" aria-label="Vote up"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10v12"></path><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"></path></svg>Yes</button><button class="voteButton_HXmX undefined" aria-label="Vote down"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 14V2"></path><path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22a3.13 3.13 0 0 1-3-3.88Z"></path></svg>No</button></div></div></div><div class="feedbackWrapper_JTi0"></div></div></div></div></main></div></div></div></div>
</body>
</html>