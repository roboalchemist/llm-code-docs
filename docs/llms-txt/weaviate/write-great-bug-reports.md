# Source: https://docs.weaviate.io/weaviate/more-resources/write-great-bug-reports

<!doctype html>
<html lang="en" dir="ltr" class="docs-wrapper plugin-docs plugin-id-default docs-version-current docs-doc-page docs-doc-id-weaviate/more-resources/write-great-bug-reports" data-has-hydrated="false">
<head>
<meta charset="UTF-8">
<meta name="generator" content="Docusaurus v3.9.2">
<title data-rh="true">How to write great bug reports | Weaviate Documentation</title><meta data-rh="true" name="viewport" content="width=device-width,initial-scale=1"><meta data-rh="true" name="twitter:card" content="summary_large_image"><meta data-rh="true" property="og:url" content="https://docs.weaviate.io/weaviate/more-resources/write-great-bug-reports"><meta data-rh="true" property="og:locale" content="en"><meta data-rh="true" name="docusaurus_locale" content="en"><meta data-rh="true" name="docsearch:language" content="en"><meta data-rh="true" name="docusaurus_version" content="current"><meta data-rh="true" name="docusaurus_tag" content="docs-default-current"><meta data-rh="true" name="docsearch:version" content="current"><meta data-rh="true" name="docsearch:docusaurus_tag" content="docs-default-current"><meta data-rh="true" property="og:title" content="How to write great bug reports | Weaviate Documentation"><meta data-rh="true" name="description" content="Write great bug reports!"><meta data-rh="true" property="og:description" content="Write great bug reports!"><meta data-rh="true" property="og:image" content="https://docs.weaviate.io/og/docs/more-resources.jpg"><meta data-rh="true" name="twitter:image" content="https://docs.weaviate.io/og/docs/more-resources.jpg"><link data-rh="true" rel="icon" href="/img/favicon.ico"><link data-rh="true" rel="canonical" href="https://docs.weaviate.io/weaviate/more-resources/write-great-bug-reports"><link data-rh="true" rel="alternate" href="https://docs.weaviate.io/weaviate/more-resources/write-great-bug-reports" hreflang="en"><link data-rh="true" rel="alternate" href="https://docs.weaviate.io/weaviate/more-resources/write-great-bug-reports" hreflang="x-default"><link rel="preconnect" href="https://www.googletagmanager.com">
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

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WS8CG676" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript><div id="__docusaurus"><link rel="preload" as="image" href="/img/site/weaviate-logo-horizontal-light-1.svg"><link rel="preload" as="image" href="/img/site/weaviate-logo-horizontal-dark-1.svg"><link rel="preload" as="image" href="/img/site/weaviate-logo-w.png"><div role="region" aria-label="Skip to main content"><a class="skipToContent_fXgn" href="#__docusaurus_skipToContent_fallback">Skip to main content</a></div><div class="theme-announcement-bar announcementBar_mb4j" style="background-color:#1C1468;color:#F5F5F5" role="banner"><div class="announcementBarPlaceholder_vyr4"></div><div class="content_knG7 announcementBarContent_xLdY"><a href="https://academy.weaviate.io/">The new <b>Weaviate Academy</b> learning platform is here!</a></div><button type="button" aria-label="Close" class="clean-btn close closeButton_CVFx announcementBarClose_gvF7"><svg viewBox="0 0 15 15" width="14" height="14"><g stroke="currentColor" stroke-width="3.1"><path d="M.75.75l13.5 13.5M14.25.75L.75 14.25"></path></g></svg></button></div><div class="defaultNavbar_mOWn"><nav aria-label="Main" class="theme-layout-navbar navbar navbar--fixed-top"><div class="navbar__inner"><div class="theme-layout-navbar-left navbar__items"><button aria-label="Toggle navigation bar" aria-expanded="false" class="navbar__toggle clean-btn" type="button"><svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><path stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="2" d="M4 7h22M4 15h22M4 23h22"></path></svg></button><a href="https://weaviate.io" target="_blank" rel="noopener noreferrer" class="navbar__brand"><div class="navbar__logo"><img src="/img/site/weaviate-logo-horizontal-light-1.svg" alt="Weaviate" class="themedComponent_mlkZ themedComponent--light_NVdE"><img src="/img/site/weaviate-logo-horizontal-dark-1.svg" alt="Weaviate" class="themedComponent_mlkZ themedComponent--dark_xIcU"></div><b class="navbar__title text--truncate"></b></a><a class="navbar__item navbar__link" href="/weaviate/api/rest"></a></div><div class="theme-layout-navbar-right navbar__items navbar__items--right"><a href="https://github.com/weaviate/weaviate" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link"><svg class="githubStars" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>GitHub</title><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a><a href="https://academy.weaviate.io" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link academy-button">Academy</a><a href="https://weaviate.io/go/console?utm_source=docs&amp;utm_content=navbar" target="_blank" rel="noopener noreferrer" class="navbar__item navbar__link cloud-button">Weaviate Cloud</a><div class="hiddenSearch navbarSearchContainer_Bca1"><div class="searchBox"><button class="searchButton"><span class="searchPlaceholder"><i class="searchIcon fas fa-magnifying-glass"></i><span class="searchPlaceholderText">Ask AI or Search</span></span><div class="commandIconContainer"><span class="commandIcon">⌘K</span></div></button></div></div><div class="toggle_vylO colorModeToggle_DEke"><button class="clean-btn toggleButton_gllP toggleButtonDisabled_aARS" type="button" disabled="" title="system mode" aria-label="Switch between dark and light mode (currently system mode)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP lightToggleIcon_pyhR"><path fill="currentColor" d="M12,9c1.65,0,3,1.35,3,3s-1.35,3-3,3s-3-1.35-3-3S10.35,9,12,9 M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5 S14.76,7,12,7L12,7z M2,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13l2,0c0.55,0,1-0.45,1-1 s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1C11.45,19,11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0 c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95 c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41 L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41 s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06 c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z"></path></svg><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP darkToggleIcon_wfgR"><path fill="currentColor" d="M9.37,5.51C9.19,6.15,9.1,6.82,9.1,7.5c0,4.08,3.32,7.4,7.4,7.4c0.68,0,1.35-0.09,1.99-0.27C17.45,17.19,14.93,19,12,19 c-3.86,0-7-3.14-7-7C5,9.07,6.81,6.55,9.37,5.51z M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36 c-0.98,1.37-2.58,2.26-4.4,2.26c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z"></path></svg><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" class="toggleIcon_g3eP systemToggleIcon_QzmC"><path fill="currentColor" d="m12 21c4.971 0 9-4.029 9-9s-4.029-9-9-9-9 4.029-9 9 4.029 9 9 9zm4.95-13.95c1.313 1.313 2.05 3.093 2.05 4.95s-0.738 3.637-2.05 4.95c-1.313 1.313-3.093 2.05-4.95 2.05v-14c1.857 0 3.637 0.737 4.95 2.05z"></path></svg></button></div></div></div><div role="presentation" class="navbar-sidebar__backdrop"></div></nav></div><div class="secondaryNavbar_Zq6r"><nav class="secondaryNavLinks_WJZI"><a class="navLink_kzb_" href="/weaviate">Get started</a><a class="navLink_kzb_" href="/weaviate/guides">How-to manuals &amp; Guides</a><a class="navLink_kzb_" href="/weaviate/model-providers">Model integrations</a><a class="navLink_kzb_" href="/weaviate/config-refs">Reference &amp; APIs</a><a class="navLink_kzb_" href="/weaviate/concepts">Concepts</a><a class="navLink_kzb_" href="/weaviate/recipes">Recipes</a><a class="navLink_kzb_" href="/weaviate/release-notes">Other</a></nav></div><div class="modalOverlay_BeVA"><div class="modalContent_CPV2"><div class="modalHeader_aBIn"><div class="modalHeaderLeft_Jnp2"><strong>Go to documentation:</strong></div><div class="modalHeaderRight_pW31"><div class="modalHeaderButton_lyv9"><span class="buttonShortcut_rHzY">⌘U</span><div class="verticalDivider_TWYg"></div><button class="headerCloseIcon_Nc0n">✕</button></div></div></div><div class="modalBody_bZ4G"><div class="modalOptionsContainer_GF7c"><div class="modalOption_Zqj6"><i class="fa fa-database modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Database</strong><p>Develop AI applications using Weaviate&#x27;s APIs and tools</p></div></div><div class="modalOption_Zqj6"><i class="fa fa-database modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Deploy</strong><p>Deploy, configure, and maintain Weaviate Database</p></div></div><div class="modalOption_Zqj6"><i class="fa fa-robot modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Agents</strong><p>Build and deploy intelligent agents with Weaviate</p></div></div><div class="modalOption_Zqj6"><i class="fa fa-cloud modalIcon__725" aria-hidden="true"></i><div class="modalText_gt5h"><strong>Weaviate Cloud</strong><p>Manage and scale Weaviate in the cloud</p></div></div></div><div class="resourcesSection__QVP"><h4 class="sectionTitle_TjaJ">Additional resources</h4><div class="resourcesGrid_Fe8L"><div class="resourceCard_qG9v"><i class="fa fa-puzzle-piece resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Integrations</span></div><div class="resourceCard_qG9v"><i class="fa fa-edit resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Contributor guide</span></div><div class="resourceCard_qG9v"><i class="fa fa-calendar-days resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Events &amp; Workshops</span></div><div class="resourceCard_qG9v"><i class="fa-solid fa-graduation-cap resourceIcon_KgrH" aria-hidden="true"></i><span class="resourceTitle__PWa">Weaviate Academy</span></div></div></div><div class="aiAssistantSection_Qefr"><h4 class="sectionTitle_TjaJ">Need help?</h4><div class="resourcesGrid_Fe8L"><div class="askAiButton_snh2"><img src="/img/site/weaviate-logo-w.png" alt="Weaviate Logo" class="askAiIcon_T_rP"><span class="askAiText_snFq">Ask AI Assistant</span><span class="askAiShortcut_kkRQ">⌘K</span></div><div class="resourceCard_qG9v"><i class="fa fa-comments styles.resourceIcon" aria-hidden="true"></i><span class="resourceTitle__PWa">Community Forum</span></div></div></div></div></div></div><div id="__docusaurus_skipToContent_fallback" class="theme-layout-main main-wrapper mainWrapper_z2l0"><div class="docsWrapper_hBAB"><button aria-label="Scroll back to top" class="clean-btn theme-back-to-top-button backToTopButton_sjWU" type="button"></button><div class="docRoot_UBD9"><main class="docMainContainer_TBSr docMainContainerEnhanced_lQrH"><div class="container padding-top--md padding-bottom--lg"><div class="row"><div class="col docItemCol_z5aJ"><div class="docItemContainer_c0TR"><article><div class="tocCollapsible_ETCw theme-doc-toc-mobile tocMobile_ITEo"><button type="button" class="clean-btn tocCollapsibleButton_TO0P">On this page</button></div><div class="theme-doc-markdown markdown"><header><h1>How to write great bug reports</h1></header><h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="write-great-bug-reports">Write great bug reports!<a href="#write-great-bug-reports" class="hash-link" aria-label="Direct link to Write great bug reports!" title="Direct link to Write great bug reports!" translate="no">​</a></h2>
<p>This page outlines what an ideal bug report would look like. We know that it is
not always possible to write a perfect bug report, and we don&#x27;t want to
discourage you from reporting a bug just because you might not be able to
provide all the info needed to make the report great. At the same time we want
to provide you with the information to make the lives of our engineers a bit
easier. Sometimes we also need to prioritize and decide about which bug ticket
to pick up first. If a bug report is well-prepared, it has a greater chance of
being picked up first.</p>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="what-makes-a-great-bug-report-stand-out">What makes a great bug report stand out?<a href="#what-makes-a-great-bug-report-stand-out" class="hash-link" aria-label="Direct link to What makes a great bug report stand out?" title="Direct link to What makes a great bug report stand out?" translate="no">​</a></h3>
<p>Here are some points that make a bug report great:</p>
<ul>
<li class="">
<p><strong>Providing Context</strong>
When you have been working on a specific use-case or fighting against a
specific bug for ages there is probably a lot of context in your or your
teams&#x27; head(s). Sometimes this context gets lost when handing over a bug
report to one of our engineers. Since they have probably been working on
something completely different before, it may be difficult for them to
understand all your goals and assumptions that are like second-nature to you.
A great bug reports sets that context and makes sure that any engineer -
whether an inside our outside contributor - can get started on this ticket
easily.</p>
</li>
<li class="">
<p><strong>Right level of information</strong>
Depending on the kind of bug, there is a different need for information.
Let&#x27;s consider two different possible bugs: For the first one an image when
using the <code>img2vec</code> module was not vectorized correctly and your results are
off because of it. For the second one, consider a scenario where you a
performing a lookup by id and it is much slower than you think it should be.
Those are both valid bugs, but we need different kind of information for
each. For example, for the image-vectorization bug we need to know a lot of
the details about the <code>img2vec</code> module: What versions were used? Which
inference container was running? Was there a GPU involved? What file format
did the image have? But looking at the performance bug, we probably need more
info regarding your hardware. How was the machine sized? What kind of disks
were used? What were the vitals (CPU usage, Memory usage, Disk pressure)
during the slow query, etc.? We do not expect you to know all the internals
of Weaviate, but we ask you to think about what details may be helpful in
reproducing the bug and which are most likely superfluous.</p>
</li>
<li class="">
<p><strong>Quick to reproduce</strong>
Every bug is important and we are happy about every single report. However,
we must still prioritize. A bug report that is easier for us to reproduce is
a bug report we might prefer. A great bug report contains a reproducing
example that makes no assumptions about prior state and reproduces be bug in
its entirety. Below are some examples for a great reproducing example in a
bug report.</p>
</li>
<li class="">
<p><strong>Narrowed down to a particular area</strong>
Weaviate is more than just the Weaviate server, it&#x27;s an entire ecosystem that
often contains the Weaviate Server, a language-specific Weaviate client and
any number of optional modules. Those modules may bring their own inference
containers if they make use of a Machine-Learning model. A great bug report
tries to narrow down where the problem goes wrong. There are some helpful
tips below to see how you can find out where the bug occurs.</p>
</li>
</ul>
<p>Now that we have established <em>what</em> makes a great bug report, let&#x27;s look at
some of the individual areas and see <em>how</em> we can write better reports.</p>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="what-is-the-minimal-information-and-context-that-should-always-be-provided">What is the minimal information and context that should always be provided?<a href="#what-is-the-minimal-information-and-context-that-should-always-be-provided" class="hash-link" aria-label="Direct link to What is the minimal information and context that should always be provided?" title="Direct link to What is the minimal information and context that should always be provided?" translate="no">​</a></h2>
<ul>
<li class="">Make sure that all the versions used are explicitly listed. This includes at
the minimum the version of the Weaviate server and the client.</li>
<li class="">Is there a chance that the bug was introduced in a recent version? In this
case, report the last version that does not have the specified issue.</li>
<li class="">Is there module involved that is vital to reproducing the bug? If so, specify
the module. If the module uses different models, specify the model names too.</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="how-do-i-provide-a-good-reproducing-example">How do I provide a good reproducing example?<a href="#how-do-i-provide-a-good-reproducing-example" class="hash-link" aria-label="Direct link to How do I provide a good reproducing example?" title="Direct link to How do I provide a good reproducing example?" translate="no">​</a></h2>
<ul>
<li class="">A great reproducing example makes zero assumptions about state. This means
that the example always starts with an empty Weaviate instance and imports
any object that is required to reproduce the bug. Our engineers cannot predict
what kind of objects should be imported based on a read/search query.</li>
<li class="">Anything that is required to reproduce the error is part of the reproducing
example. Our engineers should be able to copy/paste the example and
immediately see that something is wrong.</li>
<li class="">The reproducing example is expressed as code. This could be one of Weaviate&#x27;s
language clients or a series of <code>curl</code> commands.</li>
<li class="">The reproducing example tells us what you expected to happen. In some cases
it might not be obvious why the actual behavior is not the desired behavior.
Let us know what you expected to happen instead. This can be either in
the form of code, a code comment, or text accompanying your example.</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="how-do-i-know-if-a-problem-occurs-in-weaviate-a-client-or-somewhere-else">How do I know if a problem occurs in Weaviate, a client or somewhere else?<a href="#how-do-i-know-if-a-problem-occurs-in-weaviate-a-client-or-somewhere-else" class="hash-link" aria-label="Direct link to How do I know if a problem occurs in Weaviate, a client or somewhere else?" title="Direct link to How do I know if a problem occurs in Weaviate, a client or somewhere else?" translate="no">​</a></h2>
<ul>
<li class="">If you have a suspicion that a problem doesn&#x27;t actually occur in the Weaviate
server, but possibly in one of the clients, you can verify sending a similar
request using a different language client or no language client. The latter
case is the best as it rules out client problems altogether. If you can
still reproduce the error by sending a request using pure HTTP (e.g. via
<code>curl</code>, Postman, etc.), you can be sure that the error occurs on the Weaviate
server-side.</li>
<li class="">If you see a stack trace from your language-client you can make an educated
guess about where the error occurred. If the stack trace contains a network
request, a non-2xx HTTP status code or an error message containing
information about shards and indexes, there is a good chance the bug occurred
inside the Weaviate server. If you see something that is very specific to the
client&#x27;s language however, it may be an indication that the error occurred in
the client.</li>
<li class="">If you are using any other tools from the Weaviate eco-system, for example
the <code>weaviate-helm</code> repository to run on Kubernetes, there is also a chance
that something goes wrong there. If you think that the bug might be specific
to the runtime and its manifests, it might make sense to also try the setup
on a different runtime. Let us know what you have already tried.</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="what-if-its-not-feasible-to-provide-the-information-mentioned-above">What if it&#x27;s not feasible to provide the information mentioned above?<a href="#what-if-its-not-feasible-to-provide-the-information-mentioned-above" class="hash-link" aria-label="Direct link to What if it&#x27;s not feasible to provide the information mentioned above?" title="Direct link to What if it&#x27;s not feasible to provide the information mentioned above?" translate="no">​</a></h2>
<p>Don&#x27;t worry about it. We know that sometimes bugs are tricky and not so easy to
reproduce. If it is simply not feasible to write a perfect bug report, write one
anyway. We are very happy when we see that you made an effort to write a good
report.</p>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="thank-you">Thank you<a href="#thank-you" class="hash-link" aria-label="Direct link to Thank you" title="Direct link to Thank you" translate="no">​</a></h2>
<p>A bug report is a contribution to Weaviate. We are really thankful for you
taking the time to report the issue and helping us improve Weaviate. Thank you!</p></div><footer class="theme-doc-footer docusaurus-mt-lg"><div class="row margin-top--sm theme-doc-footer-edit-meta-row"><div class="col noPrint_WFHX"><a href="https://github.com/weaviate/docs/tree/main/docs/weaviate/more-resources/write-great-bug-reports.md" target="_blank" rel="noopener noreferrer" class="theme-edit-this-page"><svg fill="currentColor" height="20" width="20" viewBox="0 0 40 40" class="iconEdit_Z9Sw" aria-hidden="true"><g><path d="m34.5 11.7l-3 3.1-6.3-6.3 3.1-3q0.5-0.5 1.2-0.5t1.1 0.5l3.9 3.9q0.5 0.4 0.5 1.1t-0.5 1.2z m-29.5 17.1l18.4-18.5 6.3 6.3-18.4 18.4h-6.3v-6.2z"></path></g></svg>Edit this page</a></div><div class="col lastUpdated_JAkA"></div></div><footer class="footer_G0fi"><div class="container"><div class="footerContent_oI6g"><div class="leftSection_TIm0"><div class="socialIcons_Okfn"><a href="https://github.com/weaviate/weaviate" target="_blank" rel="noopener noreferrer" title="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a><a href="https://weaviate.io/slack" target="_blank" rel="noopener noreferrer" title="Slack"><i class="fab fa-slack" aria-hidden="true"></i></a><a href="https://x.com/weaviate_io" target="_blank" rel="noopener noreferrer" title="X"><i class="fab fa-twitter" aria-hidden="true"></i></a><a href="https://instagram.com/weaviate.io" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a><a href="https://youtube.com/@Weaviate" target="_blank" rel="noopener noreferrer" title="YouTube"><i class="fab fa-youtube" aria-hidden="true"></i></a><a href="https://www.linkedin.com/company/weaviate-io" target="_blank" rel="noopener noreferrer" title="LinkedIn"><i class="fab fa-linkedin" aria-hidden="true"></i></a></div></div><div class="rightSection_LCNx"><div class="footerSection_l31a"><h5>Documentation</h5><ul><li><a href="/weaviate">Weaviate Database</a></li><li><a href="/deploy">Deployment documentation</a></li><li><a href="/cloud">Weaviate Cloud</a></li><li><a href="/agents">Weaviate Agents</a></li></ul></div><div class="footerSection_l31a"><h5>Support</h5><ul><li><a href="https://forum.weaviate.io/c/support/" target="_blank" rel="noopener noreferrer">Forum</a></li><li><a href="https://weaviate.io/slack" target="_blank" rel="noopener noreferrer">Slack</a></li></ul></div></div></div></div></footer></footer></article></div></div><div class="col col--3"><div class="customTocStickyContainer_xbxO"><div class="tableOfContents_bqdL thin-scrollbar theme-doc-toc-desktop"><ul class="table-of-contents table-of-contents__left-border"><li><a href="#write-great-bug-reports" class="table-of-contents__link toc-highlight">Write great bug reports!</a><ul><li><a href="#what-makes-a-great-bug-report-stand-out" class="table-of-contents__link toc-highlight">What makes a great bug report stand out?</a></li></ul></li><li><a href="#what-is-the-minimal-information-and-context-that-should-always-be-provided" class="table-of-contents__link toc-highlight">What is the minimal information and context that should always be provided?</a></li><li><a href="#how-do-i-provide-a-good-reproducing-example" class="table-of-contents__link toc-highlight">How do I provide a good reproducing example?</a></li><li><a href="#how-do-i-know-if-a-problem-occurs-in-weaviate-a-client-or-somewhere-else" class="table-of-contents__link toc-highlight">How do I know if a problem occurs in Weaviate, a client or somewhere else?</a></li><li><a href="#what-if-its-not-feasible-to-provide-the-information-mentioned-above" class="table-of-contents__link toc-highlight">What if it&#39;s not feasible to provide the information mentioned above?</a></li><li><a href="#thank-you" class="table-of-contents__link toc-highlight">Thank you</a></li></ul></div><div class="container_jpeN"><p class="text_tGp7">Was this page helpful?</p><div class="buttonContainer_rFWk"><button class="voteButton_HXmX undefined" aria-label="Vote up"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10v12"></path><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"></path></svg>Yes</button><button class="voteButton_HXmX undefined" aria-label="Vote down"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 14V2"></path><path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22a3.13 3.13 0 0 1-3-3.88Z"></path></svg>No</button></div></div></div><div class="feedbackWrapper_JTi0"></div></div></div></div></main></div></div></div></div>
</body>
</html>