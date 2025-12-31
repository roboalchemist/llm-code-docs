# Source: https://www.promptfoo.dev/docs/model-audit/scanners/

<!doctype html>
<html lang="en" dir="ltr" class="docs-wrapper plugin-docs plugin-id-default docs-version-current docs-doc-page docs-doc-id-model-audit/scanners" data-has-hydrated="false">
<head>
<meta charset="UTF-8">
<meta name="generator" content="Docusaurus v3.9.2">
<title data-rh="true">ModelAudit Scanners | Promptfoo</title><meta data-rh="true" name="viewport" content="width=device-width,initial-scale=1"><meta data-rh="true" name="twitter:card" content="summary_large_image"><meta data-rh="true" property="og:image" content="https://www.promptfoo.dev/img/og/docs-model-audit-scanners--og.png"><meta data-rh="true" name="twitter:image" content="https://www.promptfoo.dev/img/og/docs-model-audit-scanners--og.png"><meta data-rh="true" property="og:url" content="https://www.promptfoo.dev/docs/model-audit/scanners/"><meta data-rh="true" property="og:locale" content="en"><meta data-rh="true" name="docusaurus_locale" content="en"><meta data-rh="true" name="docsearch:language" content="en"><meta data-rh="true" name="docusaurus_version" content="current"><meta data-rh="true" name="docusaurus_tag" content="docs-default-current"><meta data-rh="true" name="docsearch:version" content="current"><meta data-rh="true" name="docsearch:docusaurus_tag" content="docs-default-current"><meta data-rh="true" property="og:title" content="ModelAudit Scanners | Promptfoo"><meta data-rh="true" name="description" content="Complete guide to ModelAudit&#x27;s security scanners for different ML model formats including PyTorch, TensorFlow, Keras, ONNX, GGUF, and more."><meta data-rh="true" property="og:description" content="Complete guide to ModelAudit&#x27;s security scanners for different ML model formats including PyTorch, TensorFlow, Keras, ONNX, GGUF, and more."><meta data-rh="true" name="keywords" content="modelaudit,model security,AI security,ML security scanning,pickle scanner,pytorch security,tensorflow security,keras security,onnx security,model vulnerability detection,malicious code detection,backdoor detection,model file scanning"><link data-rh="true" rel="icon" href="/favicon.ico"><link data-rh="true" rel="canonical" href="https://www.promptfoo.dev/docs/model-audit/scanners/"><link data-rh="true" rel="alternate" href="https://www.promptfoo.dev/docs/model-audit/scanners/" hreflang="en"><link data-rh="true" rel="alternate" href="https://www.promptfoo.dev/docs/model-audit/scanners/" hreflang="x-default"><link data-rh="true" rel="preconnect" href="https://VPUDC1V4TA-dsn.algolia.net" crossorigin="anonymous"><script data-rh="true" type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Scanners","item":"https://www.promptfoo.dev/docs/model-audit/scanners"}]}</script><link rel="alternate" type="application/rss+xml" href="/blog/rss.xml" title="Promptfoo RSS Feed">
<link rel="alternate" type="application/atom+xml" href="/blog/atom.xml" title="Promptfoo Atom Feed">




<link rel="search" type="application/opensearchdescription+xml" title="Promptfoo" href="/opensearch.xml">


<link rel="preconnect" href="https://www.google-analytics.com">
<link rel="preconnect" href="https://www.googletagmanager.com">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3TS8QLZQ93"></script>
<script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","G-3TS8QLZQ93",{anonymize_ip:!0}),gtag("config","G-3YM29CN26E",{anonymize_ip:!0}),gtag("config","AW-17347444171",{anonymize_ip:!0})</script>




<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="true">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&amp;display=swap">
<script src="/js/scripts.js" async></script><link rel="stylesheet" href="/assets/css/styles.de7eafd7.css">
<script src="/assets/js/runtime~main.8ef058f4.js" defer="defer"></script>
<script src="/assets/js/main.3e1bf4a4.js" defer="defer"></script>
</head>
<body class="navigation-with-keyboard">
<svg style="display: none;"><defs>
<symbol id="theme-svg-external-link" viewBox="0 0 24 24"><path fill="currentColor" d="M21 13v10h-21v-19h12v2h-10v15h17v-8h2zm3-12h-10.988l4.035 4-6.977 7.07 2.828 2.828 6.977-7.07 4.125 4.172v-11z"/></symbol>
</defs></svg>
<script>document.documentElement.setAttribute("data-theme","light"),document.documentElement.setAttribute("data-theme-choice","light"),function(){try{const c=new URLSearchParams(window.location.search).entries();for(var[t,e]of c)if(t.startsWith("docusaurus-data-")){var a=t.replace("docusaurus-data-","data-");document.documentElement.setAttribute(a,e)}}catch(t){}}()</script><div id="__docusaurus"><link rel="preload" as="image" href="/img/logo-panda.svg"><div role="region" aria-label="Skip to main content"><a class="skipToContent_oPtH" href="#__docusaurus_skipToContent_fallback">Skip to main content</a></div><nav aria-label="Main" class="theme-layout-navbar navbar navbar--fixed-top"><div class="navbar__inner"><div class="theme-layout-navbar-left navbar__items"><button aria-label="Toggle navigation bar" aria-expanded="false" class="navbar__toggle clean-btn" type="button"><svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><path stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2" d="M4 7h22M4 15h22M4 23h22"></path></svg></button><a class="navbar__brand" href="/"><div class="navbar__logo"><img src="/img/logo-panda.svg" alt="promptfoo logo" class="themedComponent_siVc themedComponent--light_hHel"><img src="/img/logo-panda.svg" alt="promptfoo logo" class="themedComponent_siVc themedComponent--dark_yETr"></div><b class="navbar__title text--truncate">promptfoo</b></a><div class="navMenuCard_gbxm"><div class="navMenuCardButton_ymam navbar__link" role="button" tabindex="0" aria-expanded="false" aria-haspopup="true">Products<svg class="navMenuCardIcon_auzk" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"></path></svg></div><div class="navMenuCardDropdown_iu1u"><div class="navMenuCardContainer_O1hF"><div class="navMenuCardSection_dSaY"><div class="navMenuCardGrid_IZE2"><a class="navMenuCardItem__hM1" href="/red-teaming/"><div class="navMenuCardItemTitle_w7Zb">Red Teaming</div><div class="navMenuCardItemDescription_ZlX1">Proactively identify and fix vulnerabilities in your AI applications</div></a><a class="navMenuCardItem__hM1" href="/guardrails/"><div class="navMenuCardItemTitle_w7Zb">Guardrails</div><div class="navMenuCardItemDescription_ZlX1">Real-time protection against jailbreaks and adversarial attacks</div></a><a class="navMenuCardItem__hM1" href="/model-security/"><div class="navMenuCardItemTitle_w7Zb">Model Security</div><div class="navMenuCardItemDescription_ZlX1">Comprehensive security testing and monitoring for AI models</div></a><a class="navMenuCardItem__hM1" href="/mcp/"><div class="navMenuCardItemTitle_w7Zb">MCP Proxy</div><div class="navMenuCardItemDescription_ZlX1">Secure proxy for Model Context Protocol communications</div></a><a class="navMenuCardItem__hM1" href="/code-scanning/"><div class="navMenuCardItemTitle_w7Zb">Code Scanning</div><div class="navMenuCardItemDescription_ZlX1">Find LLM vulnerabilities in your IDE and CI/CD</div></a><a class="navMenuCardItem__hM1" href="/docs/getting-started/"><div class="navMenuCardItemTitle_w7Zb">Evaluations</div><div class="navMenuCardItemDescription_ZlX1">Test and evaluate your prompts, models, and RAG pipelines</div></a></div></div></div></div></div><div class="navMenuCard_gbxm"><div class="navMenuCardButton_ymam navbar__link" role="button" tabindex="0" aria-expanded="false" aria-haspopup="true">Solutions<svg class="navMenuCardIcon_auzk" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"></path></svg></div><div class="navMenuCardDropdown_iu1u"><div class="navMenuCardContainer_O1hF"><div class="navMenuCardSection_dSaY"><div class="navMenuCardSectionTitle_r2uM">By Industry</div><div class="navMenuCardGrid_IZE2"><a class="navMenuCardItem__hM1" href="/solutions/healthcare/"><div class="navMenuCardItemTitle_w7Zb">Healthcare</div><div class="navMenuCardItemDescription_ZlX1">HIPAA-compliant medical AI security</div></a><a class="navMenuCardItem__hM1" href="/solutions/finance/"><div class="navMenuCardItemTitle_w7Zb">Financial Services</div><div class="navMenuCardItemDescription_ZlX1">FINRA-aligned security testing</div></a><a class="navMenuCardItem__hM1" href="/solutions/insurance/"><div class="navMenuCardItemTitle_w7Zb">Insurance</div><div class="navMenuCardItemDescription_ZlX1">PHI protection &amp; compliance</div></a></div></div></div></div></div><div class="navMenuCard_gbxm"><div class="navMenuCardButton_ymam navbar__link" role="button" tabindex="0" aria-expanded="false" aria-haspopup="true">Company<svg class="navMenuCardIcon_auzk" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"></path></svg></div><div class="navMenuCardDropdown_iu1u"><div class="navMenuCardContainer_O1hF"><div class="navMenuCardSection_dSaY"><div class="navMenuCardGrid_IZE2"><a class="navMenuCardItem__hM1" href="/about/"><div class="navMenuCardItemTitle_w7Zb">About</div><div class="navMenuCardItemDescription_ZlX1">Learn about our mission and team</div></a><a class="navMenuCardItem__hM1" href="/press/"><div class="navMenuCardItemTitle_w7Zb">Press</div><div class="navMenuCardItemDescription_ZlX1">Media coverage and press releases</div></a><a class="navMenuCardItem__hM1" href="/events/"><div class="navMenuCardItemTitle_w7Zb">Events</div><div class="navMenuCardItemDescription_ZlX1">Meet the team at conferences and events</div></a><a class="navMenuCardItem__hM1" href="/careers/"><div class="navMenuCardItemTitle_w7Zb">Careers</div><div class="navMenuCardItemDescription_ZlX1">Join our growing team</div></a><a class="navMenuCardItem__hM1" href="/store/"><div class="navMenuCardItemTitle_w7Zb">Swag</div><div class="navMenuCardItemDescription_ZlX1">Official Promptfoo merch and swag</div></a></div></div></div></div></div><a class="navbar__item navbar__link" href="/docs/intro/">Docs</a><a class="navbar__item navbar__link" href="/blog/">Blog</a><a class="navbar__item navbar__link" href="/pricing/">Pricing</a></div><div class="theme-layout-navbar-right navbar__items navbar__items--right"><a class="navbar__item navbar__link header-book-demo-link" aria-label="Book a Demo" href="/contact/">Book a Demo</a><a href="https://promptfoo.app" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link" aria-label="Promptfoo App">Log in</a><a href="https://github.com/promptfoo/promptfoo" target="_blank" rel="noopener noreferrer" class="githubStars_ekUx" aria-label="9k stars on GitHub"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="githubIcon_Gy4v" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"></path></svg><span class="starCount_kuMA">9k</span></a><a href="https://discord.gg/promptfoo" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link header-discord-link" aria-label="Discord community"></a><div class="navbarSearchContainer_bzqh"><button type="button" class="DocSearch DocSearch-Button" aria-label="Search (Meta+k)" aria-keyshortcuts="Meta+k"><span class="DocSearch-Button-Container"><svg width="20" height="20" class="DocSearch-Search-Icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="8" stroke="currentColor" fill="none" stroke-width="1.4"></circle><path d="m21 21-4.3-4.3" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg><span class="DocSearch-Button-Placeholder">Search</span></span><span class="DocSearch-Button-Keys"></span></button></div></div></div><div role="presentation" class="navbar-sidebar__backdrop"></div></nav><div id="__docusaurus_skipToContent_fallback" class="theme-layout-main main-wrapper mainWrapper_MB5r"><div class="docsWrapper__sE8"><button aria-label="Scroll back to top" class="clean-btn theme-back-to-top-button backToTopButton_iEvu" type="button"></button><div class="docRoot_DfVB"><aside class="theme-doc-sidebar-container docSidebarContainer_c7NB"><div class="sidebarViewport_KYo0"><div class="sidebar_CUen"><nav aria-label="Docs sidebar" class="menu thin-scrollbar menu_jmj1"><ul class="theme-doc-sidebar-menu menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/"><span title="Intro" class="linkLabel_fEdy">Intro</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/quickstart/"><span title="Quickstart" class="linkLabel_fEdy">Quickstart</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/configuration/"><span title="Configuration" class="linkLabel_fEdy">Configuration</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/architecture/"><span title="Architecture" class="linkLabel_fEdy">Architecture</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/llm-vulnerability-types/"><span title="Types of LLM vulnerabilities" class="linkLabel_fEdy">Types of LLM vulnerabilities</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class="menu__link" href="/docs/red-team/risk-scoring/"><span title="Risk Scoring" class="linkLabel_fEdy">Risk Scoring</span></a></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item menu__list-item--collapsed"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist" href="/docs/red-team/plugins/"><span title="Plugins" class="categoryLinkLabel_ufhF">Plugins</span></a><button aria-label="Expand sidebar category &#x27;Plugins&#x27;" aria-expanded="false" type="button" class="clean-btn menu__caret"></button></div></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item menu__list-item--collapsed"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist" href="/docs/red-team/strategies/"><span title="Strategies" class="categoryLinkLabel_ufhF">Strategies</span></a><button aria-label="Expand sidebar category &#x27;Strategies&#x27;" aria-expanded="false" type="button" class="clean-btn menu__caret"></button></div></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item menu__list-item--collapsed"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist menu__link--sublist-caret" role="button" aria-expanded="false" href="/docs/red-team/nist-ai-rmf/"><span title="Frameworks" class="categoryLinkLabel_ufhF">Frameworks</span></a></div></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist menu__link--sublist-caret menu__link--active" role="button" aria-expanded="true" href="/docs/red-team/discovery/"><span title="Tools" class="categoryLinkLabel_ufhF">Tools</span></a></div><ul class="menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class="menu__link" tabindex="0" href="/docs/red-team/discovery/"><span title="Target Discovery" class="linkLabel_fEdy">Target Discovery</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class="menu__link" tabindex="0" href="/docs/red-team/guardrails/"><span title="Adaptive Guardrails" class="linkLabel_fEdy">Adaptive Guardrails</span></a></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist menu__link--sublist-caret menu__link--active" role="button" aria-expanded="true" tabindex="0" href="/docs/model-audit/"><span title="Model Scanner" class="categoryLinkLabel_ufhF">Model Scanner</span></a></div><ul class="menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-3 menu__list-item"><a class="menu__link" tabindex="0" href="/docs/model-audit/"><span title="Overview" class="linkLabel_fEdy">Overview</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-3 menu__list-item"><a class="menu__link" tabindex="0" href="/docs/model-audit/usage/"><span title="Advanced Usage" class="linkLabel_fEdy">Advanced Usage</span></a></li><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-3 menu__list-item"><a class="menu__link menu__link--active" aria-current="page" tabindex="0" href="/docs/model-audit/scanners/"><span title="Scanners" class="linkLabel_fEdy">Scanners</span></a></li></ul></li></ul></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item menu__list-item--collapsed"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist menu__link--sublist-caret" role="button" aria-expanded="false" href="/docs/red-team/troubleshooting/overview/"><span title="Troubleshooting" class="categoryLinkLabel_ufhF">Troubleshooting</span></a></div></li><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item menu__list-item--collapsed"><div class="menu__list-item-collapsible"><a class="categoryLink_ROYx menu__link menu__link--sublist menu__link--sublist-caret" role="button" aria-expanded="false" href="/docs/guides/llm-redteaming/"><span title="Guides" class="categoryLinkLabel_ufhF">Guides</span></a></div></li></ul></nav></div></div></aside><main class="docMainContainer_a9sJ"><div class="container padding-top--md padding-bottom--lg"><div class="row"><div class="col docItemCol_Qr34"><div class="docItemContainer_tjFy"><article><nav class="theme-doc-breadcrumbs breadcrumbsContainer_T5ub" aria-label="Breadcrumbs"><ul class="breadcrumbs"><li class="breadcrumbs__item"><a aria-label="Home page" class="breadcrumbs__link" href="/"><svg viewBox="0 0 24 24" class="breadcrumbHomeIcon_sfvy"><path d="M10 19v-5h4v5c0 .55.45 1 1 1h3c.55 0 1-.45 1-1v-7h1.7c.46 0 .68-.57.33-.87L12.67 3.6c-.38-.34-.96-.34-1.34 0l-8.36 7.53c-.34.3-.13.87.33.87H5v7c0 .55.45 1 1 1h3c.55 0 1-.45 1-1z" fill="currentColor"></path></svg></a></li><li class="breadcrumbs__item"><span class="breadcrumbs__link">Tools</span></li><li class="breadcrumbs__item"><span class="breadcrumbs__link">Model Scanner</span></li><li class="breadcrumbs__item breadcrumbs__item--active"><span class="breadcrumbs__link">Scanners</span></li></ul></nav><div class="tocCollapsible_wXna theme-doc-toc-mobile tocMobile_Ojys"><button type="button" class="clean-btn tocCollapsibleButton_iI2p">On this page</button></div><div class="theme-doc-markdown markdown"><div style="position:relative"><header><h1>ModelAudit Scanners</h1></header>
<p>ModelAudit includes specialized scanners for different model formats and file types. Each scanner is designed to identify specific security issues relevant to that format.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="pickle-scanner">Pickle Scanner<a href="#pickle-scanner" class="hash-link" aria-label="Direct link to Pickle Scanner" title="Direct link to Pickle Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pkl</code>, <code>.pickle</code>, <code>.dill</code>, <code>.bin</code> (when containing pickle data), <code>.pt</code>, <code>.pth</code>, <code>.ckpt</code></p>
<p>The Pickle Scanner analyzes Python pickle files for security risks, which are common in many ML frameworks. It supports standard pickle files as well as dill-serialized files (an extended pickle format).</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious module imports (e.g., <code>os</code>, <code>subprocess</code>, <code>sys</code>)</li>
<li class="">Dangerous functions (e.g., <code>eval</code>, <code>exec</code>, <code>system</code>)</li>
<li class="">Malicious pickle opcodes (REDUCE, INST, OBJ, NEWOBJ, STACK_GLOBAL)</li>
<li class="">Encoded payloads and suspicious string patterns</li>
<li class="">Embedded executables in binary content</li>
<li class="">ML context detection to reduce false positives</li>
<li class="">Network communication patterns (URLs, IPs, sockets)</li>
<li class="">Embedded credentials (API keys, tokens, passwords)</li>
<li class="">JIT/Script execution patterns</li>
</ul>
<p><strong>Why it matters:</strong>
Pickle files are a common serialization format for ML models but can execute arbitrary code during unpickling. Attackers can craft malicious pickle files that execute harmful commands when loaded.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="tensorflow-savedmodel-scanner">TensorFlow SavedModel Scanner<a href="#tensorflow-savedmodel-scanner" class="hash-link" aria-label="Direct link to TensorFlow SavedModel Scanner" title="Direct link to TensorFlow SavedModel Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pb</code> files and SavedModel directories</p>
<p>This scanner examines TensorFlow models saved in the SavedModel format.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious TensorFlow operations that could access files or the system</li>
<li class="">Python function calls embedded in the graph</li>
<li class="">Operations that allow arbitrary code execution (e.g., <code>PyFunc</code>)</li>
<li class="">File I/O operations that might access unexpected locations</li>
<li class="">Execution operations that could run system commands</li>
</ul>
<p><strong>Why it matters:</strong>
TensorFlow models can contain operations that interact with the filesystem or execute arbitrary code, which could be exploited if a malicious model is loaded.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="tensorflow-lite-scanner">TensorFlow Lite Scanner<a href="#tensorflow-lite-scanner" class="hash-link" aria-label="Direct link to TensorFlow Lite Scanner" title="Direct link to TensorFlow Lite Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.tflite</code></p>
<p>This scanner examines TensorFlow Lite model files, which are optimized for mobile and embedded devices.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Custom operations that could contain malicious code</li>
<li class="">Flex delegate operations that enable full TensorFlow ops execution</li>
<li class="">Model metadata that could contain executable content</li>
<li class="">Suspicious operator configurations or patterns</li>
<li class="">Buffer validation to detect tampering</li>
</ul>
<p><strong>Why it matters:</strong>
While TensorFlow Lite models are generally safer than full TensorFlow models due to their limited operator set, they can still include custom operations or use the Flex delegate to access the full TensorFlow runtime, potentially introducing security risks. Malicious actors could embed harmful code in custom ops or metadata.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="tensorrt-scanner">TensorRT Scanner<a href="#tensorrt-scanner" class="hash-link" aria-label="Direct link to TensorRT Scanner" title="Direct link to TensorRT Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.engine</code>, <code>.plan</code></p>
<p>This scanner examines NVIDIA TensorRT engine files, which are optimized inference engines for NVIDIA GPUs.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious file paths (<code>/tmp/</code>, <code>../</code>) that might indicate unauthorized access</li>
<li class="">Embedded shared library references (<code>.so</code> files) that could contain malicious code</li>
<li class="">Script execution patterns (<code>exec</code>, <code>eval</code>) that could run arbitrary code</li>
<li class="">Unauthorized plugin references that might load malicious extensions</li>
</ul>
<p><strong>Why it matters:</strong>
TensorRT engines can contain custom plugins and operations. While generally safer than pickle files, they could be crafted to include malicious plugins or reference unauthorized system resources.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="keras-h5-scanner">Keras H5 Scanner<a href="#keras-h5-scanner" class="hash-link" aria-label="Direct link to Keras H5 Scanner" title="Direct link to Keras H5 Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.h5</code>, <code>.hdf5</code>, <code>.keras</code></p>
<p>This scanner analyzes Keras models stored in HDF5 format.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Unsafe Lambda layers that could contain arbitrary Python code</li>
<li class="">Suspicious layer configurations with embedded code</li>
<li class="">Custom layers or metrics that might execute malicious code</li>
<li class="">Dangerous string patterns in model configurations</li>
</ul>
<p><strong>Why it matters:</strong>
Keras models with Lambda layers can contain arbitrary Python code that executes when the model is loaded or run. This could be exploited to execute malicious code on the host system.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="keras-zip-scanner">Keras ZIP Scanner<a href="#keras-zip-scanner" class="hash-link" aria-label="Direct link to Keras ZIP Scanner" title="Direct link to Keras ZIP Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.keras</code></p>
<p>This scanner analyzes ZIP-based Keras model files (new <code>.keras</code> format introduced in Keras 3).</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Unsafe Lambda layers with base64-encoded Python code</li>
<li class="">Suspicious layer configurations and custom objects</li>
<li class="">Python files or executables embedded in the ZIP archive</li>
<li class="">Dangerous patterns in model configuration JSON</li>
</ul>
<p><strong>Why it matters:</strong>
The new <code>.keras</code> ZIP format stores Lambda layers as base64-encoded functions that execute during inference. Malicious actors could embed arbitrary code in these layers or hide executables within the archive structure.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="onnx-scanner">ONNX Scanner<a href="#onnx-scanner" class="hash-link" aria-label="Direct link to ONNX Scanner" title="Direct link to ONNX Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.onnx</code></p>
<p>This scanner examines ONNX (Open Neural Network Exchange) model files for security issues and integrity problems.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Custom operators that might contain malicious functionality</li>
<li class="">External data file references and path traversal attempts</li>
<li class="">Tensor size and data integrity validation</li>
<li class="">File size mismatches that could indicate tampering</li>
</ul>
<p><strong>Why it matters:</strong>
ONNX models can reference external data files and custom operators. Malicious actors could exploit these features to include harmful custom operations or manipulate external data references to access unauthorized files on the system.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="openvino-scanner">OpenVINO Scanner<a href="#openvino-scanner" class="hash-link" aria-label="Direct link to OpenVINO Scanner" title="Direct link to OpenVINO Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.xml</code>, <code>.bin</code> (OpenVINO IR format)</p>
<p>This scanner examines Intel OpenVINO Intermediate Representation (IR) model files.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious custom layer configurations</li>
<li class="">External data references with path traversal attempts</li>
<li class="">Malformed XML structure or oversized files</li>
<li class="">Dangerous layer types that could access system resources</li>
<li class="">Plugin references that might load unauthorized code</li>
</ul>
<p><strong>Why it matters:</strong>
OpenVINO models consist of XML topology files and binary weight files. The XML can contain custom layer definitions or external references that could be exploited to execute malicious code or access unauthorized files.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="pytorch-zip-scanner">PyTorch Zip Scanner<a href="#pytorch-zip-scanner" class="hash-link" aria-label="Direct link to PyTorch Zip Scanner" title="Direct link to PyTorch Zip Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pt</code>, <code>.pth</code></p>
<p>This scanner examines PyTorch model files, which are ZIP archives containing pickled data.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Malicious pickle files embedded within the PyTorch model</li>
<li class="">Python code files included in the model archive</li>
<li class="">Executable scripts or binaries bundled with the model</li>
<li class="">Suspicious serialization patterns in the embedded pickles</li>
</ul>
<p><strong>Why it matters:</strong>
PyTorch models are essentially ZIP archives containing pickled objects, which can include malicious code. The scanner unpacks these archives and applies pickle security checks to the contents.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="executorch-scanner">ExecuTorch Scanner<a href="#executorch-scanner" class="hash-link" aria-label="Direct link to ExecuTorch Scanner" title="Direct link to ExecuTorch Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pte</code>, <code>.pt</code> (ExecuTorch archives)</p>
<p>This scanner examines PyTorch ExecuTorch model files designed for mobile and edge deployment.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Embedded pickle files within ExecuTorch archives</li>
<li class="">Python code or executables bundled in the archive</li>
<li class="">Suspicious serialization patterns</li>
<li class="">Custom operators that might contain malicious functionality</li>
<li class="">Dangerous metadata or configuration data</li>
</ul>
<p><strong>Why it matters:</strong>
ExecuTorch models package PyTorch models for edge devices but can still contain pickled data and embedded code. Mobile deployment environments are often resource-constrained and may have limited security monitoring, making them attractive targets.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="ggufggml-scanner">GGUF/GGML Scanner<a href="#ggufggml-scanner" class="hash-link" aria-label="Direct link to GGUF/GGML Scanner" title="Direct link to GGUF/GGML Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.gguf</code>, <code>.ggml</code>, <code>.ggmf</code>, <code>.ggjt</code>, <code>.ggla</code>, <code>.ggsa</code></p>
<p>This scanner validates GGUF (GPT-Generated Unified Format) and GGML model files commonly used for large language models like LLaMA, Alpaca, and other quantized models.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Header validation</strong>: Verifies file format integrity and header structure</li>
<li class=""><strong>Metadata security</strong>: Scans JSON metadata for suspicious content and path traversal attempts</li>
<li class=""><strong>Tensor integrity</strong>: Validates tensor dimensions, types, and data alignment</li>
<li class=""><strong>Resource limits</strong>: Enforces security limits to prevent denial-of-service attacks</li>
<li class=""><strong>Compression validation</strong>: Checks for reasonable tensor sizes and prevents decompression bombs</li>
</ul>
<p><strong>Why it matters:</strong>
GGUF/GGML files are increasingly popular for distributing large language models. While generally safer than pickle formats, they can still contain malicious metadata or be crafted to cause resource exhaustion attacks. The scanner ensures these files are structurally sound and don&#x27;t contain hidden threats.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="joblib-scanner">Joblib Scanner<a href="#joblib-scanner" class="hash-link" aria-label="Direct link to Joblib Scanner" title="Direct link to Joblib Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.joblib</code></p>
<p>This scanner analyzes joblib serialized files, which are commonly used by ML libraries for model persistence.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Compression bomb detection</strong>: Identifies files with suspicious compression ratios that could cause resource exhaustion</li>
<li class=""><strong>Embedded pickle analysis</strong>: Decompresses and scans embedded pickle content for malicious code</li>
<li class=""><strong>Size limits</strong>: Enforces maximum decompressed size limits to prevent memory exhaustion</li>
<li class=""><strong>Format validation</strong>: Distinguishes between ZIP archives and compressed pickle data</li>
</ul>
<p><strong>Why it matters:</strong>
Joblib files often contain compressed pickle data, inheriting the same security risks as pickle files. Additionally, malicious actors could craft compression bombs that consume excessive memory or CPU resources when loaded. The scanner provides safe decompression with security limits.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="skops-scanner">Skops Scanner<a href="#skops-scanner" class="hash-link" aria-label="Direct link to Skops Scanner" title="Direct link to Skops Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.skops</code>, <code>.pkl</code> (skops format)</p>
<p>This scanner detects known vulnerabilities in scikit-learn models saved with the skops library.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>CVE-2025-54412</strong>: Remote code execution via malicious sklearn estimator</li>
<li class=""><strong>CVE-2025-54413</strong>: Arbitrary code execution through sklearn.compose.ColumnTransformer</li>
<li class=""><strong>CVE-2025-54886</strong>: Code execution via callable arguments in estimators</li>
<li class="">Version detection for vulnerable skops versions (&lt; 0.12.0)</li>
<li class="">Dangerous sklearn components (Pipeline, ColumnTransformer, FunctionTransformer)</li>
<li class="">Malicious callable arguments in estimator configurations</li>
</ul>
<p><strong>Why it matters:</strong>
Skops versions before 0.12.0 contain multiple critical vulnerabilities allowing remote code execution through specially crafted sklearn estimators. Attackers can embed malicious callables in pipelines, transformers, or estimator parameters that execute when the model is loaded or used.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="flaxjax-scanner">Flax/JAX Scanner<a href="#flaxjax-scanner" class="hash-link" aria-label="Direct link to Flax/JAX Scanner" title="Direct link to Flax/JAX Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.msgpack</code>, <code>.flax</code>, <code>.orbax</code>, <code>.jax</code></p>
<p>This scanner analyzes Flax/JAX model files serialized in MessagePack format and other JAX-specific formats.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious MessagePack structures that could exploit deserializers</li>
<li class="">Embedded code objects or executable content</li>
<li class="">Malformed or oversized data structures that could cause resource exhaustion</li>
<li class="">Potentially dangerous nested objects or recursive structures</li>
<li class="">Unusual data types that might indicate tampering</li>
</ul>
<p><strong>Why it matters:</strong>
Flax models serialized as msgpack files can potentially contain embedded code or malicious data structures. While MessagePack is generally safer than pickle, it can still be exploited through carefully crafted payloads that target specific deserializer vulnerabilities or cause denial-of-service attacks through resource exhaustion.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="jax-checkpoint-scanner">JAX Checkpoint Scanner<a href="#jax-checkpoint-scanner" class="hash-link" aria-label="Direct link to JAX Checkpoint Scanner" title="Direct link to JAX Checkpoint Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.ckpt</code>, <code>.checkpoint</code>, <code>.orbax-checkpoint</code>, <code>.pickle</code> (when in JAX context)</p>
<p>This scanner analyzes JAX checkpoint files in various serialization formats, including Orbax checkpoints and JAX-specific pickle files.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Dangerous JAX operations like experimental callbacks (<code>jax.experimental.host_callback.call</code>)</li>
<li class="">Custom restore functions in Orbax checkpoint metadata</li>
<li class="">Dangerous pickle opcodes in JAX-serialized files</li>
<li class="">Directory-based checkpoint structure validation</li>
<li class="">Resource limits to prevent denial-of-service attacks</li>
</ul>
<p><strong>Why it matters:</strong>
JAX checkpoints can contain custom restore functions or experimental callbacks that could be exploited. Orbax checkpoints may include metadata with arbitrary restore functions that execute during model loading.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="numpy-scanner">NumPy Scanner<a href="#numpy-scanner" class="hash-link" aria-label="Direct link to NumPy Scanner" title="Direct link to NumPy Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.npy</code>, <code>.npz</code></p>
<p>This scanner validates NumPy binary array files for integrity issues and potential security risks.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Array validation</strong>: Checks array dimensions and data types for malicious manipulation</li>
<li class=""><strong>Header integrity</strong>: Validates NumPy file headers and magic numbers</li>
<li class=""><strong>Dangerous data types</strong>: Detects potentially harmful data types like object arrays</li>
<li class=""><strong>Size validation</strong>: Prevents loading of excessively large arrays that could cause memory exhaustion</li>
<li class=""><strong>Dimension limits</strong>: Enforces reasonable limits on array dimensions to prevent DoS attacks</li>
</ul>
<p><strong>Why it matters:</strong>
While NumPy files are generally safer than pickle files, they can still be crafted maliciously. Object arrays can contain arbitrary Python objects (including code), and extremely large arrays can cause denial-of-service attacks. The scanner ensures arrays are safe to load and don&#x27;t contain hidden threats.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="oci-layer-scanner">OCI Layer Scanner<a href="#oci-layer-scanner" class="hash-link" aria-label="Direct link to OCI Layer Scanner" title="Direct link to OCI Layer Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.manifest</code> (with <code>.tar.gz</code> layer references)</p>
<p>This scanner examines OCI (Open Container Initiative) and Docker manifest files that contain embedded model files in compressed layers.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Layer extraction</strong>: Safely extracts and scans model files from <code>.tar.gz</code> layers</li>
<li class=""><strong>Manifest validation</strong>: Parses JSON and YAML manifest formats</li>
<li class=""><strong>Recursive scanning</strong>: Applies appropriate scanners to model files found within container layers</li>
<li class=""><strong>Path validation</strong>: Prevents directory traversal attacks during layer extraction</li>
</ul>
<p><strong>Why it matters:</strong>
Container images are increasingly used to distribute ML models and datasets. These containers can contain multiple layers with various file types, potentially hiding malicious models within what appears to be a legitimate container image. The scanner ensures that all model files within container layers are safe.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="manifest-scanner">Manifest Scanner<a href="#manifest-scanner" class="hash-link" aria-label="Direct link to Manifest Scanner" title="Direct link to Manifest Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.json</code>, <code>.yaml</code>, <code>.yml</code>, <code>.xml</code>, <code>.toml</code>, <code>.config</code>, etc.</p>
<p>This scanner analyzes model configuration files and manifests.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Blacklisted model names that might indicate known vulnerable models</li>
<li class="">Suspicious configuration patterns related to:<!-- -->
<ul>
<li class="">Network access (URLs, endpoints, webhooks)</li>
<li class="">File system access (paths, directories, file operations)</li>
<li class="">Code execution (commands, scripts, shell access)</li>
<li class="">Credentials (passwords, tokens, secrets)</li>
</ul>
</li>
<li class="">Framework-specific patterns in popular ML library configurations</li>
</ul>
<p><strong>Why it matters:</strong>
Model configuration files can contain settings that lead to insecure behavior, such as downloading content from untrusted sources, accessing sensitive files, or executing commands.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="text-scanner">Text Scanner<a href="#text-scanner" class="hash-link" aria-label="Direct link to Text Scanner" title="Direct link to Text Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.txt</code>, <code>.md</code>, <code>.markdown</code>, <code>.rst</code></p>
<p>This scanner analyzes ML-specific text files like vocabulary lists, README files, and model documentation.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Unusually large text files that may indicate data hiding</li>
<li class="">File type identification (vocabulary, labels, documentation)</li>
<li class="">Basic content validation for ML-related text files</li>
</ul>
<p><strong>Why it matters:</strong>
Text files in ML repositories like vocab.txt, labels.txt, and README files should follow expected patterns. Deviations may indicate tampering or hidden data.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="jinja2-template-scanner">Jinja2 Template Scanner<a href="#jinja2-template-scanner" class="hash-link" aria-label="Direct link to Jinja2 Template Scanner" title="Direct link to Jinja2 Template Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.gguf</code>, <code>.json</code>, <code>.yaml</code>, <code>.yml</code>, <code>.jinja</code>, <code>.j2</code>, <code>.template</code></p>
<p>This scanner detects template injection vulnerabilities in Jinja2 templates embedded in model files and configurations.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Server-side template injection (SSTI) patterns</li>
<li class="">Dangerous Jinja2 filters or functions (e.g., <code>eval</code>, <code>exec</code>, <code>import</code>)</li>
<li class="">Unrestricted variable access that could leak sensitive data</li>
<li class="">Code execution patterns in template expressions</li>
<li class="">CVE-2024-34359 exploitation in GGUF chat templates</li>
</ul>
<p><strong>Why it matters:</strong>
Jinja2 templates in GGUF models, tokenizer configs, and deployment files can execute arbitrary code when processed. CVE-2024-34359 affects llama-cpp-python when loading malicious chat templates. Template injection allows full system compromise.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="metadata-scanner">Metadata Scanner<a href="#metadata-scanner" class="hash-link" aria-label="Direct link to Metadata Scanner" title="Direct link to Metadata Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>README.md</code>, <code>MODEL_CARD.md</code>, <code>METADATA.md</code>, model card files</p>
<p>This scanner analyzes model documentation and metadata files for security concerns.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Embedded credentials or API keys in documentation</li>
<li class="">Suspicious URLs or download links</li>
<li class="">References to malicious code repositories</li>
<li class="">Known vulnerable model versions or components</li>
<li class="">Misleading or deceptive model descriptions</li>
<li class="">Missing or inadequate security disclosures</li>
</ul>
<p><strong>Why it matters:</strong>
Model documentation often contains setup instructions, example code, and configuration that may reference malicious resources or expose sensitive information. Attackers can embed malicious download links or credentials in README files that users may execute without careful review.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="pytorch-binary-scanner">PyTorch Binary Scanner<a href="#pytorch-binary-scanner" class="hash-link" aria-label="Direct link to PyTorch Binary Scanner" title="Direct link to PyTorch Binary Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.bin</code> (raw PyTorch tensor files)</p>
<p>This scanner examines raw PyTorch binary tensor files that contain serialized weight data. It performs binary content scanning to detect various threats.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Embedded code patterns (imports, function calls, eval/exec)</li>
<li class="">Executable file signatures (Windows PE with DOS stub validation, Linux ELF, macOS Mach-O)</li>
<li class="">Shell script shebangs that might indicate embedded scripts</li>
<li class="">Blacklisted patterns specified in configuration</li>
<li class="">Suspiciously small files that might not be valid tensor data</li>
<li class="">Validation of tensor structure</li>
<li class="">PE file detection with MS-DOS stub signature validation</li>
</ul>
<p><strong>Why it matters:</strong>
While <code>.bin</code> files typically contain raw tensor data, attackers could embed malicious code or executables within these files. The scanner performs deep content analysis with PE file detection (including DOS stub validation) to detect such threats.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="zip-archive-scanner">ZIP Archive Scanner<a href="#zip-archive-scanner" class="hash-link" aria-label="Direct link to ZIP Archive Scanner" title="Direct link to ZIP Archive Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.zip</code>, <code>.npz</code></p>
<p>This scanner examines ZIP archives and their contents recursively.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Directory traversal attacks:</strong> Detects entries with paths containing &quot;..&quot; or absolute paths that could overwrite system files</li>
<li class=""><strong>Zip bombs:</strong> Identifies files with suspicious compression ratios (&gt;100x) that could cause resource exhaustion</li>
<li class=""><strong>Nested archives:</strong> Scans ZIP files within ZIP files up to a configurable depth to prevent infinite recursion attacks</li>
<li class=""><strong>Malicious content:</strong> Each file within the archive is scanned with its appropriate scanner (e.g., pickle files with PickleScanner)</li>
<li class=""><strong>Resource limits:</strong> Enforces maximum number of entries and file sizes to prevent denial-of-service attacks</li>
</ul>
<p><strong>Why it matters:</strong>
ZIP archives are commonly used to distribute models and datasets. Malicious actors can craft ZIP files that exploit extraction vulnerabilities, contain malware, or cause resource exhaustion. This scanner ensures that archives are safe to extract and that their contents don&#x27;t pose security risks.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="tar-scanner">TAR Scanner<a href="#tar-scanner" class="hash-link" aria-label="Direct link to TAR Scanner" title="Direct link to TAR Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.tar</code>, <code>.tar.gz</code>, <code>.tgz</code>, <code>.tar.bz2</code></p>
<p>This scanner examines TAR archives and their contents recursively.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Directory traversal attacks with paths containing &quot;..&quot; or absolute paths</li>
<li class="">Symlink attacks that could point to sensitive system files</li>
<li class="">TAR bombs with excessive file counts or decompression ratios</li>
<li class="">Malicious content within archived files (scans with appropriate scanners)</li>
<li class="">Resource limits to prevent denial-of-service attacks</li>
</ul>
<p><strong>Why it matters:</strong>
TAR archives are commonly used in Linux environments and container images to distribute models. They can contain symlinks that point outside the extraction directory, potentially allowing access to sensitive files. TAR bombs can exhaust system resources during extraction.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="7-zip-scanner">7-Zip Scanner<a href="#7-zip-scanner" class="hash-link" aria-label="Direct link to 7-Zip Scanner" title="Direct link to 7-Zip Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.7z</code></p>
<p>This scanner examines 7-Zip archives and their contents.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Directory traversal attacks in entry paths</li>
<li class="">Compression bombs with suspicious ratios</li>
<li class="">Encrypted archives that might hide malicious content</li>
<li class="">Nested archives to prevent infinite recursion</li>
<li class="">Resource limits for memory and CPU usage</li>
<li class="">Malicious content within archived files</li>
</ul>
<p><strong>Why it matters:</strong>
7-Zip archives offer high compression ratios, making them attractive for compression bomb attacks. They support encryption, which can hide malicious content from initial inspection. The scanner safely extracts and analyzes 7z files with appropriate security limits.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="weight-distribution-scanner">Weight Distribution Scanner<a href="#weight-distribution-scanner" class="hash-link" aria-label="Direct link to Weight Distribution Scanner" title="Direct link to Weight Distribution Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pt</code>, <code>.pth</code>, <code>.h5</code>, <code>.keras</code>, <code>.hdf5</code>, <code>.pb</code>, <code>.onnx</code>, <code>.safetensors</code></p>
<p>This scanner analyzes neural network weight distributions to detect potential backdoors or trojaned models by identifying statistical anomalies.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Outlier neurons:</strong> Detects output neurons with abnormally high weight magnitudes using Z-score analysis</li>
<li class=""><strong>Dissimilar weight vectors:</strong> Identifies neurons whose weight patterns are significantly different from others in the same layer (using cosine similarity)</li>
<li class=""><strong>Extreme weight values:</strong> Flags neurons containing unusually large individual weight values that deviate from the layer&#x27;s distribution</li>
<li class=""><strong>Final layer focus:</strong> Prioritizes analysis of classification heads and output layers where backdoors are typically implemented</li>
</ul>
<p><strong>Configuration options:</strong></p>
<ul>
<li class=""><code>z_score_threshold</code>: Controls sensitivity for outlier detection (default: 3.0, higher for LLMs)</li>
<li class=""><code>cosine_similarity_threshold</code>: Minimum similarity required between neurons (default: 0.7)</li>
<li class=""><code>weight_magnitude_threshold</code>: Threshold for extreme weight detection (default: 3.0 standard deviations)</li>
<li class=""><code>llm_vocab_threshold</code>: Vocabulary size threshold to identify LLM models (default: 10,000)</li>
<li class=""><code>enable_llm_checks</code>: Whether to perform checks on large language models (default: false)</li>
</ul>
<p><strong>Why it matters:</strong>
Backdoored or trojaned models often contain specific neurons that activate on trigger inputs. These malicious neurons typically have weight patterns that are statistically anomalous compared to benign neurons. By analyzing weight distributions, this scanner can detect models that have been tampered with to include hidden behaviors.</p>
<p><strong>Special handling for LLMs:</strong>
Large language models with vocabulary layers (&gt;10,000 outputs) use more conservative thresholds due to their naturally varied weight distributions. LLM checking is disabled by default but can be enabled via configuration.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="safetensors-scanner">SafeTensors Scanner<a href="#safetensors-scanner" class="hash-link" aria-label="Direct link to SafeTensors Scanner" title="Direct link to SafeTensors Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.safetensors</code>, <code>.bin</code> (when containing SafeTensors data)</p>
<p>This scanner examines SafeTensors format files, which are designed to be a safer alternative to pickle files.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>Header validation</strong>: Verifies SafeTensors format structure and JSON header integrity</li>
<li class=""><strong>Metadata security</strong>: Scans metadata for suspicious content, encoded payloads, and unusually large sections</li>
<li class=""><strong>Tensor validation</strong>: Validates tensor offsets, sizes, and data type consistency</li>
<li class=""><strong>Offset integrity</strong>: Ensures tensor data offsets are contiguous and within file bounds</li>
</ul>
<p><strong>Why it matters:</strong>
While SafeTensors is designed to be safer than pickle files, the metadata section can still contain malicious content. Attackers might try to exploit parsers or include encoded payloads in the metadata. The scanner ensures the format integrity and metadata safety.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="paddlepaddle-scanner">PaddlePaddle Scanner<a href="#paddlepaddle-scanner" class="hash-link" aria-label="Direct link to PaddlePaddle Scanner" title="Direct link to PaddlePaddle Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pdmodel</code>, <code>.pdiparams</code></p>
<p>This scanner examines PaddlePaddle model files, including model definitions and parameter files.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious operations in model definitions</li>
<li class="">Embedded pickle data within PaddlePaddle files</li>
<li class="">Custom operators that might contain malicious code</li>
<li class="">Dangerous configuration patterns</li>
<li class="">Executable content or embedded scripts</li>
</ul>
<p><strong>Why it matters:</strong>
PaddlePaddle models can contain custom operators and may use pickle serialization internally. Malicious actors could embed harmful code in model definitions or exploit custom operators to execute unauthorized operations.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="xgboost-scanner">XGBoost Scanner<a href="#xgboost-scanner" class="hash-link" aria-label="Direct link to XGBoost Scanner" title="Direct link to XGBoost Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.bst</code>, <code>.model</code>, <code>.json</code>, <code>.ubj</code></p>
<p>This scanner examines XGBoost model files in binary, JSON, and UBJSON formats.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class="">Suspicious custom objectives or evaluation metrics</li>
<li class="">Embedded code in JSON configurations</li>
<li class="">Malformed model structures</li>
<li class="">Dangerous callback functions</li>
<li class="">Path traversal in external feature maps</li>
<li class="">Pickle-based custom functions in binary models</li>
</ul>
<p><strong>Why it matters:</strong>
XGBoost models can include custom Python functions for objectives, metrics, and callbacks. In binary format, these are often pickled, inheriting pickle security risks. JSON formats can contain embedded code strings or references to malicious external resources.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="pmml-scanner">PMML Scanner<a href="#pmml-scanner" class="hash-link" aria-label="Direct link to PMML Scanner" title="Direct link to PMML Scanner" translate="no">​</a></h2>
<p><strong>File types:</strong> <code>.pmml</code></p>
<p>This scanner performs security checks on PMML (Predictive Model Markup Language) files to detect potential XML External Entity (XXE) attacks, malicious scripts, and suspicious external references.</p>
<p><strong>Key checks:</strong></p>
<ul>
<li class=""><strong>XXE Attack Prevention</strong>: Detects <code>&lt;!DOCTYPE</code>, <code>&lt;!ENTITY</code>, <code>&lt;!ELEMENT</code>, and <code>&lt;!ATTLIST</code> declarations that could enable XML External Entity attacks</li>
<li class=""><strong>Safe XML Parsing</strong>: Uses defusedxml when available for secure XML parsing; warns when using unsafe parsers</li>
<li class=""><strong>Malicious Content Detection</strong>: Scans for suspicious patterns like <code>&lt;script&gt;</code>, <code>eval()</code>, <code>exec()</code>, system commands, and imports</li>
<li class=""><strong>External Resource References</strong>: Identifies suspicious URLs (HTTP, HTTPS, FTP, file://) in model content</li>
<li class=""><strong>PMML Structure Validation</strong>: Validates PMML version and root element structure</li>
<li class=""><strong>Extension Element Analysis</strong>: Performs deep inspection of <code>&lt;Extension&gt;</code> elements which can contain arbitrary content</li>
</ul>
<p><strong>Security features:</strong></p>
<ul>
<li class=""><strong>XML Security</strong>: Uses defusedxml library when available to prevent XXE and billion laughs attacks</li>
<li class=""><strong>Content Scanning</strong>: Recursive analysis of all element text content and attributes for malicious patterns</li>
<li class=""><strong>Well-formedness Validation</strong>: Ensures XML structure integrity and UTF-8 encoding compliance</li>
</ul>
<p><strong>Why it matters:</strong>
PMML files are XML-based and can be exploited through XML vulnerabilities like XXE attacks. Extension elements can contain arbitrary content that might execute scripts or access external resources. The scanner ensures PMML files don&#x27;t contain hidden security threats while maintaining model functionality.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="auto-format-detection">Auto Format Detection<a href="#auto-format-detection" class="hash-link" aria-label="Direct link to Auto Format Detection" title="Direct link to Auto Format Detection" translate="no">​</a></h2>
<p>ModelAudit includes comprehensive file format detection for ambiguous file extensions, particularly <code>.bin</code> files, which can contain different types of model data:</p>
<ul>
<li class=""><strong>Pickle format</strong>: Detected by pickle protocol magic bytes (\x80\x02, \x80\x03, etc.)</li>
<li class=""><strong>SafeTensors format</strong>: Detected by JSON header structure and metadata patterns</li>
<li class=""><strong>ONNX format</strong>: Detected by ONNX protobuf signatures</li>
<li class=""><strong>PyTorch ZIP format</strong>: Detected by ZIP magic bytes (PK headers)</li>
<li class=""><strong>Raw PyTorch tensors</strong>: Default for <code>.bin</code> files without other recognizable signatures</li>
</ul>
<p><strong>Detection Features:</strong></p>
<ul>
<li class=""><strong>Magic byte analysis</strong>: Reads file headers to determine actual format regardless of extension</li>
<li class=""><strong>Content-based routing</strong>: Automatically applies the most appropriate scanner based on detected format</li>
<li class=""><strong>Multi-format support</strong>: Handles cases where files might be misnamed or have generic extensions</li>
<li class=""><strong>Fallback handling</strong>: Gracefully handles unknown formats with generic binary scanning</li>
</ul>
<p>This allows ModelAudit to automatically apply the correct scanner based on the actual file content, not just the extension. When a <code>.bin</code> file contains SafeTensors data, the SafeTensors scanner is automatically applied instead of assuming it&#x27;s a raw binary file.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="license-checking-and-compliance">License Checking and Compliance<a href="#license-checking-and-compliance" class="hash-link" aria-label="Direct link to License Checking and Compliance" title="Direct link to License Checking and Compliance" translate="no">​</a></h2>
<p>ModelAudit includes license detection across all file formats to help organizations identify legal obligations before deployment.</p>
<p><strong>Key features:</strong></p>
<ul>
<li class=""><strong>License Detection</strong>: Scans headers, LICENSE files, and metadata for license information</li>
<li class=""><strong>AGPL Warnings</strong>: Alerts about network copyleft obligations</li>
<li class=""><strong>Commercial Restrictions</strong>: Identifies non-commercial licenses</li>
<li class=""><strong>Unlicensed Content</strong>: Flags large datasets without clear licensing</li>
<li class=""><strong>SBOM Generation</strong>: Creates CycloneDX-compliant Software Bill of Materials</li>
</ul>
<p><strong>Example warnings:</strong></p>
<div class="language-text codeBlockContainer_mQmQ theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_t_Hd"><pre tabindex="0" class="prism-code language-text codeBlock_RMoD thin-scrollbar" style="color:#393A34;background-color:#f6f8fa"><code class="codeBlockLines_AclH"><span class="token-line" style="color:#393A34"><span class="token plain">⚠️ AGPL license detected: Component is under AGPL-3.0</span><br></span><span class="token-line" style="color:#393A34"><span class="token plain">   This may require source code disclosure if used in network services</span><br></span><span class="token-line" style="color:#393A34"><span class="token plain" style="display:inline-block"></span><br></span><span class="token-line" style="color:#393A34"><span class="token plain">🚨 Non-commercial license detected: Creative Commons NonCommercial</span><br></span><span class="token-line" style="color:#393A34"><span class="token plain">   This component cannot be used for commercial purposes</span><br></span></code></pre></div></div>
<p><strong>Generate SBOM:</strong></p>
<div class="language-bash codeBlockContainer_mQmQ theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_t_Hd"><pre tabindex="0" class="prism-code language-bash codeBlock_RMoD thin-scrollbar" style="color:#393A34;background-color:#f6f8fa"><code class="codeBlockLines_AclH"><span class="token-line" style="color:#393A34"><span class="token plain">promptfoo scan-model ./models/ </span><span class="token parameter variable" style="color:#36acaa">--sbom</span><span class="token plain"> model-sbom.json</span><br></span></code></pre></div></div>
<p>The SBOM includes component information, license metadata, risk scores, and copyright details in CycloneDX format.</p>
<p><strong>Why it matters:</strong>
AI/ML projects often combine components with different licenses. AGPL requires source disclosure for network services, non-commercial licenses block commercial use, and unlicensed datasets create legal risks.</p>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="network-communication-detection">Network Communication Detection<a href="#network-communication-detection" class="hash-link" aria-label="Direct link to Network Communication Detection" title="Direct link to Network Communication Detection" translate="no">​</a></h2>
<p>ModelAudit includes comprehensive detection of network communication capabilities that could be used for data exfiltration or command &amp; control:</p>
<p><strong>Detection capabilities:</strong></p>
<ul>
<li class=""><strong>URL patterns</strong>: HTTP(S), FTP, SSH, WebSocket URLs embedded in model data</li>
<li class=""><strong>IP addresses</strong>: Both IPv4 and IPv6 addresses that could indicate hardcoded endpoints</li>
<li class=""><strong>Domain names</strong>: Suspicious domain patterns that might be C&amp;C servers</li>
<li class=""><strong>Network libraries</strong>: Imports of socket, urllib, requests, and 50+ other network libraries</li>
<li class=""><strong>Network functions</strong>: Calls to urlopen, socket.connect, requests.get, and other network operations</li>
<li class=""><strong>C&amp;C patterns</strong>: Known command &amp; control patterns like beacon_url, callback_url, exfil_endpoint</li>
<li class=""><strong>Port numbers</strong>: Common and suspicious port numbers for various protocols</li>
</ul>
<p><strong>Why it matters:</strong>
Malicious models could contain embedded network communication code to:</p>
<ul>
<li class="">Exfiltrate sensitive data from the deployment environment</li>
<li class="">Download additional payloads or updates</li>
<li class="">Establish command &amp; control channels</li>
<li class="">Report telemetry to unauthorized servers</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="secrets-detection">Secrets Detection<a href="#secrets-detection" class="hash-link" aria-label="Direct link to Secrets Detection" title="Direct link to Secrets Detection" translate="no">​</a></h2>
<p>ModelAudit scans for embedded credentials and sensitive information:</p>
<p><strong>Detection patterns:</strong></p>
<ul>
<li class=""><strong>API Keys</strong>: AWS, Azure, GCP, OpenAI, and other service API keys</li>
<li class=""><strong>Tokens</strong>: JWT tokens, OAuth tokens, GitHub tokens, etc.</li>
<li class=""><strong>Passwords</strong>: Hardcoded passwords and authentication strings</li>
<li class=""><strong>Private Keys</strong>: SSH keys, SSL certificates, cryptographic keys</li>
<li class=""><strong>Database Credentials</strong>: Connection strings with embedded passwords</li>
<li class=""><strong>Webhook URLs</strong>: Slack, Discord, and other webhook endpoints</li>
</ul>
<p><strong>Why it matters:</strong>
Credentials embedded in models could:</p>
<ul>
<li class="">Expose production infrastructure access</li>
<li class="">Lead to unauthorized cloud resource usage</li>
<li class="">Enable lateral movement in compromised systems</li>
<li class="">Result in data breaches or compliance violations</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="jitscript-detection">JIT/Script Detection<a href="#jitscript-detection" class="hash-link" aria-label="Direct link to JIT/Script Detection" title="Direct link to JIT/Script Detection" translate="no">​</a></h2>
<p>ModelAudit detects Just-In-Time compilation and script execution patterns:</p>
<p><strong>Detection capabilities:</strong></p>
<ul>
<li class=""><strong>TorchScript</strong>: Embedded TorchScript code that could execute arbitrary operations</li>
<li class=""><strong>ONNX Custom Ops</strong>: Custom operators that might contain malicious functionality</li>
<li class=""><strong>TensorFlow Eager Execution</strong>: Dynamic execution patterns in TF models</li>
<li class=""><strong>Compilation Patterns</strong>: eval(), exec(), compile() calls in various contexts</li>
<li class=""><strong>Script Injections</strong>: JavaScript, Python, or shell script injection attempts</li>
</ul>
<p><strong>Why it matters:</strong>
JIT-compiled code can:</p>
<ul>
<li class="">Bypass static analysis security checks</li>
<li class="">Execute arbitrary code at runtime</li>
<li class="">Modify model behavior dynamically</li>
<li class="">Access system resources without detection</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_tleR" id="huggingface-url-support">HuggingFace URL Support<a href="#huggingface-url-support" class="hash-link" aria-label="Direct link to HuggingFace URL Support" title="Direct link to HuggingFace URL Support" translate="no">​</a></h2>
<p>ModelAudit can scan models directly from HuggingFace URLs without manual downloading. When a HuggingFace URL is provided, ModelAudit:</p>
<ol>
<li class=""><strong>Downloads the model</strong>: Uses the <code>huggingface-hub</code> library to download all model files to a temporary directory</li>
<li class=""><strong>Scans all files</strong>: Applies appropriate scanners to each file based on its format (config.json, pytorch_model.bin, model.safetensors, etc.)</li>
<li class=""><strong>Cleans up</strong>: Automatically removes downloaded files after scanning</li>
</ol>
<p><strong>Supported URL formats:</strong></p>
<ul>
<li class=""><code>https://huggingface.co/user/model</code></li>
<li class=""><code>https://hf.co/user/model</code></li>
<li class=""><code>hf://user/model</code></li>
</ul>
<p>This feature requires the <code>huggingface-hub</code> package to be installed.</p></div></div><footer class="theme-doc-footer docusaurus-mt-lg"><div class="row margin-top--sm theme-doc-footer-edit-meta-row"><div class="col noPrint_QeZL"><a href="https://github.com/promptfoo/promptfoo/tree/main/site/docs/model-audit/scanners.md" target="_blank" rel="noopener noreferrer" class="theme-edit-this-page"><svg fill="currentColor" height="20" width="20" viewBox="0 0 40 40" class="iconEdit_bHB7" aria-hidden="true"><g><path d="m34.5 11.7l-3 3.1-6.3-6.3 3.1-3q0.5-0.5 1.2-0.5t1.1 0.5l3.9 3.9q0.5 0.4 0.5 1.1t-0.5 1.2z m-29.5 17.1l18.4-18.5 6.3 6.3-18.4 18.4h-6.3v-6.2z"></path></g></svg>Edit this page</a></div><div class="col lastUpdated_ydrU"><span class="theme-last-updated">Last updated<!-- --> on <b><time datetime="2025-12-31T17:26:49.000Z" itemprop="dateModified">Dec 31, 2025</time></b> by <b>Justin Beckwith</b></span></div></div></footer></article><nav class="docusaurus-mt-lg pagination-nav" aria-label="Docs pages"><a class="pagination-nav__link pagination-nav__link--prev" href="/docs/model-audit/usage/"><div class="pagination-nav__sublabel">Previous</div><div class="pagination-nav__label">Advanced Usage</div></a><a class="pagination-nav__link pagination-nav__link--next" href="/docs/red-team/troubleshooting/overview/"><div class="pagination-nav__sublabel">Next</div><div class="pagination-nav__label">Overview</div></a></nav></div></div><div class="col col--3"><div class="tableOfContents_XG6w thin-scrollbar theme-doc-toc-desktop"><ul class="table-of-contents table-of-contents__left-border"><li><a href="#pickle-scanner" class="table-of-contents__link toc-highlight">Pickle Scanner</a></li><li><a href="#tensorflow-savedmodel-scanner" class="table-of-contents__link toc-highlight">TensorFlow SavedModel Scanner</a></li><li><a href="#tensorflow-lite-scanner" class="table-of-contents__link toc-highlight">TensorFlow Lite Scanner</a></li><li><a href="#tensorrt-scanner" class="table-of-contents__link toc-highlight">TensorRT Scanner</a></li><li><a href="#keras-h5-scanner" class="table-of-contents__link toc-highlight">Keras H5 Scanner</a></li><li><a href="#keras-zip-scanner" class="table-of-contents__link toc-highlight">Keras ZIP Scanner</a></li><li><a href="#onnx-scanner" class="table-of-contents__link toc-highlight">ONNX Scanner</a></li><li><a href="#openvino-scanner" class="table-of-contents__link toc-highlight">OpenVINO Scanner</a></li><li><a href="#pytorch-zip-scanner" class="table-of-contents__link toc-highlight">PyTorch Zip Scanner</a></li><li><a href="#executorch-scanner" class="table-of-contents__link toc-highlight">ExecuTorch Scanner</a></li><li><a href="#ggufggml-scanner" class="table-of-contents__link toc-highlight">GGUF/GGML Scanner</a></li><li><a href="#joblib-scanner" class="table-of-contents__link toc-highlight">Joblib Scanner</a></li><li><a href="#skops-scanner" class="table-of-contents__link toc-highlight">Skops Scanner</a></li><li><a href="#flaxjax-scanner" class="table-of-contents__link toc-highlight">Flax/JAX Scanner</a></li><li><a href="#jax-checkpoint-scanner" class="table-of-contents__link toc-highlight">JAX Checkpoint Scanner</a></li><li><a href="#numpy-scanner" class="table-of-contents__link toc-highlight">NumPy Scanner</a></li><li><a href="#oci-layer-scanner" class="table-of-contents__link toc-highlight">OCI Layer Scanner</a></li><li><a href="#manifest-scanner" class="table-of-contents__link toc-highlight">Manifest Scanner</a></li><li><a href="#text-scanner" class="table-of-contents__link toc-highlight">Text Scanner</a></li><li><a href="#jinja2-template-scanner" class="table-of-contents__link toc-highlight">Jinja2 Template Scanner</a></li><li><a href="#metadata-scanner" class="table-of-contents__link toc-highlight">Metadata Scanner</a></li><li><a href="#pytorch-binary-scanner" class="table-of-contents__link toc-highlight">PyTorch Binary Scanner</a></li><li><a href="#zip-archive-scanner" class="table-of-contents__link toc-highlight">ZIP Archive Scanner</a></li><li><a href="#tar-scanner" class="table-of-contents__link toc-highlight">TAR Scanner</a></li><li><a href="#7-zip-scanner" class="table-of-contents__link toc-highlight">7-Zip Scanner</a></li><li><a href="#weight-distribution-scanner" class="table-of-contents__link toc-highlight">Weight Distribution Scanner</a></li><li><a href="#safetensors-scanner" class="table-of-contents__link toc-highlight">SafeTensors Scanner</a></li><li><a href="#paddlepaddle-scanner" class="table-of-contents__link toc-highlight">PaddlePaddle Scanner</a></li><li><a href="#xgboost-scanner" class="table-of-contents__link toc-highlight">XGBoost Scanner</a></li><li><a href="#pmml-scanner" class="table-of-contents__link toc-highlight">PMML Scanner</a></li><li><a href="#auto-format-detection" class="table-of-contents__link toc-highlight">Auto Format Detection</a></li><li><a href="#license-checking-and-compliance" class="table-of-contents__link toc-highlight">License Checking and Compliance</a></li><li><a href="#network-communication-detection" class="table-of-contents__link toc-highlight">Network Communication Detection</a></li><li><a href="#secrets-detection" class="table-of-contents__link toc-highlight">Secrets Detection</a></li><li><a href="#jitscript-detection" class="table-of-contents__link toc-highlight">JIT/Script Detection</a></li><li><a href="#huggingface-url-support" class="table-of-contents__link toc-highlight">HuggingFace URL Support</a></li></ul></div></div></div></div></main></div></div></div><footer class="theme-layout-footer footer footer--dark"><div class="container container-fluid"><div class="row footer__links"><div class="theme-layout-footer-column col footer__col"><div class="footer__title">Product</div><ul class="footer__items clean-list"><li class="footer__item"><a class="footer__link-item" href="/red-teaming/">Red Teaming</a></li><li class="footer__item"><a class="footer__link-item" href="/guardrails/">Guardrails</a></li><li class="footer__item"><a class="footer__link-item" href="/model-security/">Model Security</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/getting-started/">Evaluations</a></li><li class="footer__item"><a class="footer__link-item" href="/pricing/">Enterprise</a></li><li class="footer__item"><a class="footer__link-item" href="/mcp/">MCP Proxy</a></li><li class="footer__item"><a href="https://status.promptfoo.app/" target="_blank" rel="noopener noreferrer" class="footer__link-item">Status<svg width="13.5" height="13.5" aria-label="(opens in new tab)" class="iconExternalLink_nPrP"><use href="#theme-svg-external-link"></use></svg></a></li></ul></div><div class="theme-layout-footer-column col footer__col"><div class="footer__title">Solutions</div><ul class="footer__items clean-list"><li class="footer__item"><a class="footer__link-item" href="/solutions/healthcare/">Healthcare</a></li><li class="footer__item"><a class="footer__link-item" href="/solutions/finance/">Financial Services</a></li><li class="footer__item"><a class="footer__link-item" href="/solutions/insurance/">Insurance</a></li></ul></div><div class="theme-layout-footer-column col footer__col"><div class="footer__title">Resources</div><ul class="footer__items clean-list"><li class="footer__item"><a class="footer__link-item" href="/docs/api-reference/">API Reference</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/red-team/">LLM Red Teaming</a></li><li class="footer__item"><a href="https://www.promptfoo.dev/models/" target="_blank" rel="noopener noreferrer" class="footer__link-item">Foundation Model Reports</a></li><li class="footer__item"><a href="https://www.promptfoo.dev/lm-security-db/" target="_blank" rel="noopener noreferrer" class="footer__link-item">Language Model Security DB</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/guides/llama2-uncensored-benchmark-ollama/">Running Benchmarks</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/guides/factuality-eval/">Evaluating Factuality</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/guides/evaluate-rag/">Evaluating RAGs</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/guides/prevent-llm-hallucinations/">Minimizing Hallucinations</a></li><li class="footer__item"><a class="footer__link-item" href="/validator/">Config Validator</a></li></ul></div><div class="theme-layout-footer-column col footer__col"><div class="footer__title">Company</div><ul class="footer__items clean-list"><li class="footer__item"><a class="footer__link-item" href="/about/">About</a></li><li class="footer__item"><a class="footer__link-item" href="/blog/">Blog</a></li><li class="footer__item"><a class="footer__link-item" href="/docs/releases/">Release Notes</a></li><li class="footer__item"><a class="footer__link-item" href="/press/">Press</a></li><li class="footer__item"><a class="footer__link-item" href="/events/">Events</a></li><li class="footer__item"><a class="footer__link-item" href="/contact/">Contact</a></li><li class="footer__item"><a class="footer__link-item" href="/careers/">Careers</a></li><li class="footer__item"><a class="footer__link-item" href="/store/">Swag</a></li><li class="footer__item"><a href="https://promptfoo.app" target="_blank" rel="noopener noreferrer" class="footer__link-item">Log in</a></li></ul></div><div class="theme-layout-footer-column col footer__col"><div class="footer__title">Legal &amp; Social</div><ul class="footer__items clean-list"><li class="footer__item"><a href="https://github.com/promptfoo/promptfoo" target="_blank" rel="noopener noreferrer" class="footer__link-item">GitHub<svg width="13.5" height="13.5" aria-label="(opens in new tab)" class="iconExternalLink_nPrP"><use href="#theme-svg-external-link"></use></svg></a></li><li class="footer__item"><a href="https://discord.gg/promptfoo" target="_blank" rel="noopener noreferrer" class="footer__link-item">Discord<svg width="13.5" height="13.5" aria-label="(opens in new tab)" class="iconExternalLink_nPrP"><use href="#theme-svg-external-link"></use></svg></a></li><li class="footer__item"><a href="https://www.linkedin.com/company/promptfoo/" target="_blank" rel="noopener noreferrer" class="footer__link-item">LinkedIn<svg width="13.5" height="13.5" aria-label="(opens in new tab)" class="iconExternalLink_nPrP"><use href="#theme-svg-external-link"></use></svg></a></li><li class="footer__item"><a class="footer__link-item" href="/privacy/">Privacy Policy</a></li><li class="footer__item"><a class="footer__link-item" href="/terms-of-service/">Terms of Service</a></li><li class="footer__item"><a href="https://trust.promptfoo.dev" target="_blank" rel="noopener noreferrer" class="footer__link-item">Trust Center<svg width="13.5" height="13.5" aria-label="(opens in new tab)" class="iconExternalLink_nPrP"><use href="#theme-svg-external-link"></use></svg></a></li><li class="footer__item">
                <div style="display: flex; gap: 16px; align-items: center; margin-top: 12px;">
                  <img loading="lazy" src="/img/badges/soc2.png" alt="SOC2 Certified" style="width:80px; height: auto">
                  <img loading="lazy" src="/img/badges/iso27001.png" alt="ISO 27001 Certified" style="width:80px; height: auto">
                  <img loading="lazy" src="/img/badges/hipaa.png" alt="HIPAA Compliant" style="width:80px; height: auto">
                </div>
                </li></ul></div></div><div class="footer__bottom text--center"><div class="footer__copyright">© 2025 Promptfoo, Inc.</div></div></div></footer><style data-emotion="css 14yoxd">.css-14yoxd{z-index:1200;}</style></div>
<!-- Cloudflare Pages Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "1c4bd5e1107e49379a47b948d21d50e1"}'></script><!-- Cloudflare Pages Analytics --></body>
</html>