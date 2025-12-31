# Source: https://docs.streamlit.io/develop/api-reference/configuration/config.toml

<!DOCTYPE html><html><head><meta charSet="utf-8"/><meta name="viewport" content="width=device-width"/><title>config.toml - Streamlit Docs</title><link rel="icon" href="/favicon.svg"/><link rel="alternate icon" href="/favicon32.ico"/><meta name="theme-color" content="#ffffff"/><meta name="keywords" content="config.toml, streamlit configuration, toml configuration file, streamlit settings, theme configuration, server configuration, client configuration, logger configuration, browser configuration, mapbox configuration, secrets configuration, sidebar theme, configuration options, streamlit config show"/><link rel="canonical" href="https://docs.streamlit.io/develop/api-reference/configuration/config.toml"/><meta content="config.toml - Streamlit Docs" property="og:title"/><meta content="config.toml - Streamlit Docs" name="twitter:title"/><meta content="Complete reference guide for Streamlit&#x27;s config.toml configuration file, including all available sections and options for customizing your Streamlit application settings." name="description"/><meta content="Complete reference guide for Streamlit&#x27;s config.toml configuration file, including all available sections and options for customizing your Streamlit application settings." property="og:description"/><meta content="Complete reference guide for Streamlit&#x27;s config.toml configuration file, including all available sections and options for customizing your Streamlit application settings." name="twitter:description"/><meta property="og:type" content="website"/><meta property="og:url" content="https://docs.streamlit.io/"/><meta content="summary_large_image" name="twitter:card"/><meta property="og:image" content="https://docs.streamlit.io/sharing-image-facebook.jpg"/><meta name="twitter:image" content="https://docs.streamlit.io/sharing-image-twitter.jpg"/><meta name="next-head-count" content="18"/><script>!function(){try{var e=localStorage.getItem("theme"),t=e==="dark"||e==="light"?e:(matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"),o=document.documentElement;o.classList.add(t),o.classList.remove(t==="dark"?"light":"dark"),o.style.colorScheme=t}catch(e){}}();</script><script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" type="text/javascript" charset="UTF-8" data-domain-script="01990a3a-a865-7092-a22e-9094bfac985a"></script><script src="/scripts/onetrustsetup.js"></script><script src="https://cdn.jsdelivr.net/npm/@segment/analytics-consent-wrapper-onetrust@latest/dist/umd/analytics-onetrust.umd.js"></script><script src="/scripts/segment.js"></script><link data-next-font="" rel="preconnect" href="/" crossorigin="anonymous"/><link rel="preload" href="/_next/static/css/16f9694e79fc83d9.css" as="style"/><link rel="stylesheet" href="/_next/static/css/16f9694e79fc83d9.css" data-n-g=""/><link rel="preload" href="/_next/static/css/18e6a016e3922260.css" as="style"/><link rel="stylesheet" href="/_next/static/css/18e6a016e3922260.css" data-n-p=""/><link rel="preload" href="/_next/static/css/ba82b97d4d12abf0.css" as="style"/><link rel="stylesheet" href="/_next/static/css/ba82b97d4d12abf0.css" data-n-p=""/><link rel="preload" href="/_next/static/css/7ba3d5ddf72ff697.css" as="style"/><link rel="stylesheet" href="/_next/static/css/7ba3d5ddf72ff697.css" data-n-p=""/><link rel="preload" href="/_next/static/css/226eca27334e053a.css" as="style"/><link rel="stylesheet" href="/_next/static/css/226eca27334e053a.css" data-n-p=""/><noscript data-n-css=""></noscript><script defer="" nomodule="" src="/_next/static/chunks/polyfills-42372ed130431b0a.js"></script><script src="/_next/static/chunks/webpack-f1f1ca17543ca075.js" defer=""></script><script src="/_next/static/chunks/framework-45219a46ebd8d536.js" defer=""></script><script src="/_next/static/chunks/main-3c13dfac536accbd.js" defer=""></script><script src="/_next/static/chunks/pages/_app-3705e8dee8bb2312.js" defer=""></script><script src="/_next/static/chunks/41629-fe4fdf68fa434e86.js" defer=""></script><script src="/_next/static/chunks/57259-ffc76c08c720951c.js" defer=""></script><script src="/_next/static/chunks/52732-ed413f03ccf7ca49.js" defer=""></script><script src="/_next/static/chunks/49818-ea88d00aee756fda.js" defer=""></script><script src="/_next/static/chunks/7690-43233032c4bb1839.js" defer=""></script><script src="/_next/static/chunks/26969-48fe46a451fa6c51.js" defer=""></script><script src="/_next/static/chunks/pages/%5B...slug%5D-3d3d0328304da262.js" defer=""></script><script src="/_next/static/Zwhy24kJ8WALZgyY-V3Bw/_buildManifest.js" defer=""></script><script src="/_next/static/Zwhy24kJ8WALZgyY-V3Bw/_ssgManifest.js" defer=""></script></head><body><div id="__next"><main id="root" class="dark:bg-gray-100"><header class="header_Container__HqLwQ header_standardContainer__ogw62"><nav class="header_Navigation__EVpxH" id="main-header"><a class="header_LogoContainer__FHkVy not-link" href="/"><img src="/logo.svg" alt=""/><h4 class="header_LogoText__Lw8pf">Documentation</h4></a><section class="header_NavigationContainer__couJc"><section class="search_SearchBarContainer__ZbDRN"><section class="group search_SearchBar__e7yiR"><i class="search_SearchIcon__XiooP" style="transform:rotateY(180deg)">search</i><p class="search_SearchText__Jy9Yf">Search</p></section></section></section></nav></header><div><section class="container_Container__SKLob"><section class="sideBar_Container__N_beZ sideBar_ClosedNav__9dfMo sideBar_CollapsedNav__RiEB5"><div class="sideBar_TopGradient__76xby"></div><nav><ul class="sideBar_NavList__IHKFv"><li class="navItem_NavItem__Bi5Et" id="Get-started"><a class="not-link" href="/get-started"><section class="navItem_HeadingContainer__nbVP9"><div class="navItem_HeadingIconContainer__4xrWh navItem_OrangeBackground__WG4L0"><i class="navItem_Icon__nuc2C">rocket_launch</i></div><p class="navItem_CategoryName__y68aH">Get started</p></section></a><ul class="navItem_SubNav__fh44s navItem_ExpandedSubNav__QnJLg"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/get-started/installation"><span class="navChild_Circle__kJcki navChild_OrangeCircle__mvsl9"></span><span class="navChild_PageName__cnHSh">Installation</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/get-started/fundamentals"><span class="navChild_Circle__kJcki navChild_OrangeCircle__mvsl9"></span><span class="navChild_PageName__cnHSh">Fundamentals</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/get-started/tutorials"><span class="navChild_Circle__kJcki navChild_OrangeCircle__mvsl9"></span><span class="navChild_PageName__cnHSh">First steps</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li></ul></li><li class="navItem_NavItem__Bi5Et" id="Develop"><a class="not-link" href="/develop"><section class="navItem_HeadingContainer__nbVP9"><div class="navItem_HeadingIconContainer__4xrWh navItem_IndigoBackground__SMSDw"><i class="navItem_Icon__nuc2C">code</i></div><p class="navItem_CategoryName__y68aH navItem_IndigoForeground__gz3U7">Develop</p></section></a><ul class="navItem_SubNav__fh44s navItem_ExpandedSubNav__QnJLg"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/concepts"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Concepts</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">API reference</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me close">remove</i></div></div><ul class="navChild_List__t3gYX"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><span class="navChild_DividerText__95KaR">PAGE ELEMENTS</span><hr class="navChild_DividerLine__g8mlk"/></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/write-magic"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Write and magic</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/text"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Text elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/data"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Data elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/charts"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Chart elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/widgets"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Input widgets</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/media"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Media elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/layout"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Layouts and containers</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/chat"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Chat elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/status"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Status elements</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" target="_blank" href="https://streamlit.io/components"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Third-party components</span><i class="navChild_ExternalIcon__CUggp">open_in_new</i></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><span class="navChild_DividerText__95KaR">APPLICATION LOGIC</span><hr class="navChild_DividerLine__g8mlk"/></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/user"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Authentication and user info</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/navigation"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Navigation and pages</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/execution-flow"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Execution flow</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/caching-and-state"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Caching and state</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/connections"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Connections and secrets</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/custom-components"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Custom components</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/configuration"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Configuration</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me close">remove</i></div></div><ul class="navChild_List__t3gYX"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/configuration/config.toml"><span class="navChild_Circle__kJcki navChild_ActiveCircle__twhGY navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh navChild_ActivePage__jBMhF">config.toml</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/configuration/st.get_option"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">st.get_option</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/configuration/st.set_option"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">st.set_option</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/configuration/st.set_page_config"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">st.set_page_config</span></a></div></li></ul></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><span class="navChild_DividerText__95KaR">TOOLS</span><hr class="navChild_DividerLine__g8mlk"/></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/app-testing"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">App testing</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/api-reference/cli"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Command line</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li></ul></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/tutorials"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Tutorials</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/develop/quick-reference"><span class="navChild_Circle__kJcki navChild_IndigoCircle__bvmdD"></span><span class="navChild_PageName__cnHSh">Quick reference</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li></ul></li><li class="navItem_NavItem__Bi5Et" id="Deploy"><a class="not-link" href="/deploy"><section class="navItem_HeadingContainer__nbVP9"><div class="navItem_HeadingIconContainer__4xrWh navItem_LightBlueBackground__AHDFw"><i class="navItem_Icon__nuc2C">web_asset</i></div><p class="navItem_CategoryName__y68aH">Deploy</p></section></a><ul class="navItem_SubNav__fh44s navItem_ExpandedSubNav__QnJLg"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/deploy/concepts"><span class="navChild_Circle__kJcki navChild_LightBlueCircle__SRxlQ"></span><span class="navChild_PageName__cnHSh">Concepts</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/deploy/streamlit-community-cloud"><span class="navChild_Circle__kJcki navChild_LightBlueCircle__SRxlQ"></span><span class="navChild_PageName__cnHSh">Streamlit Community Cloud</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/deploy/snowflake"><span class="navChild_Circle__kJcki navChild_LightBlueCircle__SRxlQ"></span><span class="navChild_PageName__cnHSh">Snowflake</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/deploy/tutorials"><span class="navChild_Circle__kJcki navChild_LightBlueCircle__SRxlQ"></span><span class="navChild_PageName__cnHSh">Other platforms</span></a><div class="navChild_Accordion__AK1NX"><i class="navChild_AccordionIcon__RJ_me open">add</i></div></div></li></ul></li><li class="navItem_NavItem__Bi5Et" id="Knowledge-base"><a class="not-link" href="/knowledge-base"><section class="navItem_HeadingContainer__nbVP9"><div class="navItem_HeadingIconContainer__4xrWh navItem_DarkBlueBackground__DVGoD"><i class="navItem_Icon__nuc2C">school</i></div><p class="navItem_CategoryName__y68aH">Knowledge base</p></section></a><ul class="navItem_SubNav__fh44s navItem_ExpandedSubNav__QnJLg"><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/knowledge-base/using-streamlit"><span class="navChild_Circle__kJcki navChild_DarkBlueCircle__rAAMS"></span><span class="navChild_PageName__cnHSh">FAQ</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/knowledge-base/dependencies"><span class="navChild_Circle__kJcki navChild_DarkBlueCircle__rAAMS"></span><span class="navChild_PageName__cnHSh">Installing dependencies</span></a></div></li><li class="navChild_Container__WoYpe"><div class="navChild_LinkContainer__h89Ed"><a class="not-link navChild_Link__Z0HVR" href="/knowledge-base/deploy"><span class="navChild_Circle__kJcki navChild_DarkBlueCircle__rAAMS"></span><span class="navChild_PageName__cnHSh">Deployment issues</span></a></div></li></ul></li></ul></nav></section><section class="container_InnerContainer__b_ufe" id="documentation"><nav><ul class="breadCrumbs_Container__80K4H"><li class="breadCrumbs_InnerContainer__RhiS_"><a class="not-link breadCrumbs_Link__pVcOI" href="/">Home</a><span class="breadCrumbs_Separator__aNfE7">/</span></li><li class="breadCrumbs_InnerContainer__RhiS_"><a class="not-link breadCrumbs_Link__pVcOI" href="/develop">Develop</a><span class="breadCrumbs_Separator__aNfE7">/</span></li><li class="breadCrumbs_InnerContainer__RhiS_"><a class="not-link breadCrumbs_Link__pVcOI" href="/develop/api-reference">API reference</a><span class="breadCrumbs_Separator__aNfE7">/</span></li><li class="breadCrumbs_InnerContainer__RhiS_"><a class="not-link breadCrumbs_Link__pVcOI" href="/develop/api-reference/configuration">Configuration</a><span class="breadCrumbs_Separator__aNfE7">/</span></li><li class="breadCrumbs_InnerContainer__RhiS_"><a class="not-link breadCrumbs_ActiveLink__rWno9 breadCrumbs_Link__pVcOI" href="/develop/api-reference/configuration/config.toml">config.toml</a></li></ul></nav><article id="content-container" class="leaf-page container_ArticleContainer__57dAJ"><div class="content container_ContentContainer__rpCwA"><a name="configtoml" class="headerLink_HashLink__wuW0v"></a><h2 class="headerLink_HeaderContainer__RZUrb group"><a href="/develop/api-reference/configuration/config.toml#configtoml"><span class="icon icon-link"></span></a>config.toml<div class="headerLink_CopyLink__GJbCz"><svg width="14" height="17" viewBox="0 0 14 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.7548 0.0313721C10.7051 0.0194702 10.6571 0.00793457 10.609 0H9.87278C9.83686 0.0178223 9.81891 0.0356445 9.783 0.0356445C9.20842 0.124878 8.70565 0.374573 8.29268 0.784851L4.14488 4.90521C3.57029 5.47601 3.283 6.18951 3.31892 7.01001C3.33686 7.38464 3.42665 7.74133 3.60621 8.09808L4.43217 7.27759C4.46809 7.25977 4.46809 7.18842 4.46809 7.15271C4.41421 6.59979 4.57582 6.11816 4.97085 5.72577L8.54405 2.17615L9.13659 1.58752C9.76504 0.998901 10.7167 0.998901 11.3452 1.58752C12.0095 2.21179 12.0095 3.2464 11.3452 3.90637L7.25123 7.97327C6.8562 8.36566 6.38936 8.54401 5.83273 8.49054C5.77885 8.47266 5.72499 8.47272 5.68908 8.50836L4.86311 9.32886C4.95289 9.36456 5.00676 9.40021 5.06062 9.41803C6.15593 9.81049 7.17941 9.66779 8.02333 8.84729C9.45979 7.45599 10.8783 6.06464 12.2609 4.6377C13.7333 3.12152 12.9971 0.606445 10.9501 0.0713501C10.8805 0.0614624 10.8164 0.0461426 10.7548 0.0313721ZM7.34082 7.47388C7.62811 7.2063 7.9154 6.9209 8.20269 6.6355C8.18016 6.62988 8.16114 6.62427 8.14401 6.6192C8.10655 6.60822 8.07805 6.59985 8.04109 6.59985C7.03556 6.15393 5.83253 6.3501 5.04246 7.11713C3.606 8.52625 2.1875 9.93542 0.768994 11.3624C0.14053 11.9867 -0.0928837 12.7715 0.032803 13.6277C0.194409 14.7515 0.840817 15.5184 1.9002 15.8752C2.97755 16.2319 3.94717 16.0001 4.75517 15.2152C5.6766 14.3118 6.59005 13.4004 7.50616 12.4864C7.96467 12.0289 8.42384 11.5708 8.88501 11.1127C9.56733 10.4348 9.81871 9.61432 9.67506 8.66895C9.63916 8.41925 9.56733 8.16949 9.42369 7.9198C9.13639 8.2052 8.8491 8.47272 8.57975 8.75812C8.54385 8.776 8.54385 8.84735 8.54385 8.90082C8.61567 9.41809 8.47203 9.8819 8.09495 10.2565C6.71235 11.6478 5.31181 13.0391 3.91125 14.4125C3.51623 14.8228 2.99551 14.9655 2.43889 14.8406C1.81042 14.6979 1.4154 14.3234 1.23584 13.7347C1.05629 13.1282 1.19993 12.5753 1.64882 12.1294C2.34011 11.4337 3.03141 10.747 3.72271 10.0603C4.41401 9.37354 5.10531 8.68677 5.79661 7.99115C6.17369 7.59869 6.65849 7.45599 7.19717 7.50952C7.25103 7.50952 7.3049 7.50952 7.34082 7.47388Z" fill="#808495"></path></svg></div></h2>
<p><code>config.toml</code> is an optional file you can define for your working directory or global development environment. When <code>config.toml</code> is defined both globally and in your working directory, Streamlit combines the configuration options and gives precedence to the working-directory configuration. Additionally, you can use environment variables and command-line options to override additional configuration options. For more information, see <a href="/develop/concepts/configuration/options">Configuration options</a>.</p>
<a name="file-location" class="headerLink_HashLink__wuW0v"></a><h3 class="headerLink_HeaderContainer__RZUrb group"><a href="/develop/api-reference/configuration/config.toml#file-location"><span class="icon icon-link"></span></a>File location<div class="headerLink_CopyLink__GJbCz"><svg width="14" height="17" viewBox="0 0 14 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.7548 0.0313721C10.7051 0.0194702 10.6571 0.00793457 10.609 0H9.87278C9.83686 0.0178223 9.81891 0.0356445 9.783 0.0356445C9.20842 0.124878 8.70565 0.374573 8.29268 0.784851L4.14488 4.90521C3.57029 5.47601 3.283 6.18951 3.31892 7.01001C3.33686 7.38464 3.42665 7.74133 3.60621 8.09808L4.43217 7.27759C4.46809 7.25977 4.46809 7.18842 4.46809 7.15271C4.41421 6.59979 4.57582 6.11816 4.97085 5.72577L8.54405 2.17615L9.13659 1.58752C9.76504 0.998901 10.7167 0.998901 11.3452 1.58752C12.0095 2.21179 12.0095 3.2464 11.3452 3.90637L7.25123 7.97327C6.8562 8.36566 6.38936 8.54401 5.83273 8.49054C5.77885 8.47266 5.72499 8.47272 5.68908 8.50836L4.86311 9.32886C4.95289 9.36456 5.00676 9.40021 5.06062 9.41803C6.15593 9.81049 7.17941 9.66779 8.02333 8.84729C9.45979 7.45599 10.8783 6.06464 12.2609 4.6377C13.7333 3.12152 12.9971 0.606445 10.9501 0.0713501C10.8805 0.0614624 10.8164 0.0461426 10.7548 0.0313721ZM7.34082 7.47388C7.62811 7.2063 7.9154 6.9209 8.20269 6.6355C8.18016 6.62988 8.16114 6.62427 8.14401 6.6192C8.10655 6.60822 8.07805 6.59985 8.04109 6.59985C7.03556 6.15393 5.83253 6.3501 5.04246 7.11713C3.606 8.52625 2.1875 9.93542 0.768994 11.3624C0.14053 11.9867 -0.0928837 12.7715 0.032803 13.6277C0.194409 14.7515 0.840817 15.5184 1.9002 15.8752C2.97755 16.2319 3.94717 16.0001 4.75517 15.2152C5.6766 14.3118 6.59005 13.4004 7.50616 12.4864C7.96467 12.0289 8.42384 11.5708 8.88501 11.1127C9.56733 10.4348 9.81871 9.61432 9.67506 8.66895C9.63916 8.41925 9.56733 8.16949 9.42369 7.9198C9.13639 8.2052 8.8491 8.47272 8.57975 8.75812C8.54385 8.776 8.54385 8.84735 8.54385 8.90082C8.61567 9.41809 8.47203 9.8819 8.09495 10.2565C6.71235 11.6478 5.31181 13.0391 3.91125 14.4125C3.51623 14.8228 2.99551 14.9655 2.43889 14.8406C1.81042 14.6979 1.4154 14.3234 1.23584 13.7347C1.05629 13.1282 1.19993 12.5753 1.64882 12.1294C2.34011 11.4337 3.03141 10.747 3.72271 10.0603C4.41401 9.37354 5.10531 8.68677 5.79661 7.99115C6.17369 7.59869 6.65849 7.45599 7.19717 7.50952C7.25103 7.50952 7.3049 7.50952 7.34082 7.47388Z" fill="#808495"></path></svg></div></h3>
<p>To define your configuration locally or per-project, add <code>.streamlit/config.toml</code> to your working directory. Your working directory is wherever you call <code>streamlit run</code>. If you haven&#x27;t previously created the <code>.streamlit</code> directory, you will need to add it.</p>
<p>To define your configuration globally, you must first locate your global <code>.streamlit</code> directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be <code>~/.streamlit/config.toml</code>. For Windows, this will be <code>%userprofile%/.streamlit/config.toml</code>.</p>
<a name="file-format" class="headerLink_HashLink__wuW0v"></a><h3 class="headerLink_HeaderContainer__RZUrb group"><a href="/develop/api-reference/configuration/config.toml#file-format"><span class="icon icon-link"></span></a>File format<div class="headerLink_CopyLink__GJbCz"><svg width="14" height="17" viewBox="0 0 14 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.7548 0.0313721C10.7051 0.0194702 10.6571 0.00793457 10.609 0H9.87278C9.83686 0.0178223 9.81891 0.0356445 9.783 0.0356445C9.20842 0.124878 8.70565 0.374573 8.29268 0.784851L4.14488 4.90521C3.57029 5.47601 3.283 6.18951 3.31892 7.01001C3.33686 7.38464 3.42665 7.74133 3.60621 8.09808L4.43217 7.27759C4.46809 7.25977 4.46809 7.18842 4.46809 7.15271C4.41421 6.59979 4.57582 6.11816 4.97085 5.72577L8.54405 2.17615L9.13659 1.58752C9.76504 0.998901 10.7167 0.998901 11.3452 1.58752C12.0095 2.21179 12.0095 3.2464 11.3452 3.90637L7.25123 7.97327C6.8562 8.36566 6.38936 8.54401 5.83273 8.49054C5.77885 8.47266 5.72499 8.47272 5.68908 8.50836L4.86311 9.32886C4.95289 9.36456 5.00676 9.40021 5.06062 9.41803C6.15593 9.81049 7.17941 9.66779 8.02333 8.84729C9.45979 7.45599 10.8783 6.06464 12.2609 4.6377C13.7333 3.12152 12.9971 0.606445 10.9501 0.0713501C10.8805 0.0614624 10.8164 0.0461426 10.7548 0.0313721ZM7.34082 7.47388C7.62811 7.2063 7.9154 6.9209 8.20269 6.6355C8.18016 6.62988 8.16114 6.62427 8.14401 6.6192C8.10655 6.60822 8.07805 6.59985 8.04109 6.59985C7.03556 6.15393 5.83253 6.3501 5.04246 7.11713C3.606 8.52625 2.1875 9.93542 0.768994 11.3624C0.14053 11.9867 -0.0928837 12.7715 0.032803 13.6277C0.194409 14.7515 0.840817 15.5184 1.9002 15.8752C2.97755 16.2319 3.94717 16.0001 4.75517 15.2152C5.6766 14.3118 6.59005 13.4004 7.50616 12.4864C7.96467 12.0289 8.42384 11.5708 8.88501 11.1127C9.56733 10.4348 9.81871 9.61432 9.67506 8.66895C9.63916 8.41925 9.56733 8.16949 9.42369 7.9198C9.13639 8.2052 8.8491 8.47272 8.57975 8.75812C8.54385 8.776 8.54385 8.84735 8.54385 8.90082C8.61567 9.41809 8.47203 9.8819 8.09495 10.2565C6.71235 11.6478 5.31181 13.0391 3.91125 14.4125C3.51623 14.8228 2.99551 14.9655 2.43889 14.8406C1.81042 14.6979 1.4154 14.3234 1.23584 13.7347C1.05629 13.1282 1.19993 12.5753 1.64882 12.1294C2.34011 11.4337 3.03141 10.747 3.72271 10.0603C4.41401 9.37354 5.10531 8.68677 5.79661 7.99115C6.17369 7.59869 6.65849 7.45599 7.19717 7.50952C7.25103 7.50952 7.3049 7.50952 7.34082 7.47388Z" fill="#808495"></path></svg></div></h3>
<p><code>config.toml</code> is a <a href="https://toml.io/en/">TOML</a> file.</p>
<h4 id="example"><a href="/develop/api-reference/configuration/config.toml#example"><span class="icon icon-link"></span></a>Example</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[client]
showErrorDetails = &quot;none&quot;

[theme]
primaryColor = &quot;#F63366&quot;
backgroundColor = &quot;black&quot;
</code></div></section>
<a name="available-configuration-options" class="headerLink_HashLink__wuW0v"></a><h3 class="headerLink_HeaderContainer__RZUrb group"><a href="/develop/api-reference/configuration/config.toml#available-configuration-options"><span class="icon icon-link"></span></a>Available configuration options<div class="headerLink_CopyLink__GJbCz"><svg width="14" height="17" viewBox="0 0 14 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M10.7548 0.0313721C10.7051 0.0194702 10.6571 0.00793457 10.609 0H9.87278C9.83686 0.0178223 9.81891 0.0356445 9.783 0.0356445C9.20842 0.124878 8.70565 0.374573 8.29268 0.784851L4.14488 4.90521C3.57029 5.47601 3.283 6.18951 3.31892 7.01001C3.33686 7.38464 3.42665 7.74133 3.60621 8.09808L4.43217 7.27759C4.46809 7.25977 4.46809 7.18842 4.46809 7.15271C4.41421 6.59979 4.57582 6.11816 4.97085 5.72577L8.54405 2.17615L9.13659 1.58752C9.76504 0.998901 10.7167 0.998901 11.3452 1.58752C12.0095 2.21179 12.0095 3.2464 11.3452 3.90637L7.25123 7.97327C6.8562 8.36566 6.38936 8.54401 5.83273 8.49054C5.77885 8.47266 5.72499 8.47272 5.68908 8.50836L4.86311 9.32886C4.95289 9.36456 5.00676 9.40021 5.06062 9.41803C6.15593 9.81049 7.17941 9.66779 8.02333 8.84729C9.45979 7.45599 10.8783 6.06464 12.2609 4.6377C13.7333 3.12152 12.9971 0.606445 10.9501 0.0713501C10.8805 0.0614624 10.8164 0.0461426 10.7548 0.0313721ZM7.34082 7.47388C7.62811 7.2063 7.9154 6.9209 8.20269 6.6355C8.18016 6.62988 8.16114 6.62427 8.14401 6.6192C8.10655 6.60822 8.07805 6.59985 8.04109 6.59985C7.03556 6.15393 5.83253 6.3501 5.04246 7.11713C3.606 8.52625 2.1875 9.93542 0.768994 11.3624C0.14053 11.9867 -0.0928837 12.7715 0.032803 13.6277C0.194409 14.7515 0.840817 15.5184 1.9002 15.8752C2.97755 16.2319 3.94717 16.0001 4.75517 15.2152C5.6766 14.3118 6.59005 13.4004 7.50616 12.4864C7.96467 12.0289 8.42384 11.5708 8.88501 11.1127C9.56733 10.4348 9.81871 9.61432 9.67506 8.66895C9.63916 8.41925 9.56733 8.16949 9.42369 7.9198C9.13639 8.2052 8.8491 8.47272 8.57975 8.75812C8.54385 8.776 8.54385 8.84735 8.54385 8.90082C8.61567 9.41809 8.47203 9.8819 8.09495 10.2565C6.71235 11.6478 5.31181 13.0391 3.91125 14.4125C3.51623 14.8228 2.99551 14.9655 2.43889 14.8406C1.81042 14.6979 1.4154 14.3234 1.23584 13.7347C1.05629 13.1282 1.19993 12.5753 1.64882 12.1294C2.34011 11.4337 3.03141 10.747 3.72271 10.0603C4.41401 9.37354 5.10531 8.68677 5.79661 7.99115C6.17369 7.59869 6.65849 7.45599 7.19717 7.50952C7.25103 7.50952 7.3049 7.50952 7.34082 7.47388Z" fill="#808495"></path></svg></div></h3>
<p>Below are all the sections and options you can have in your <code>.streamlit/config.toml</code> file. To see all configurations, use the following command in your terminal or CLI:</p>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-bash">streamlit config show
</code></div></section>
<h4 id="global"><a href="/develop/api-reference/configuration/config.toml#global"><span class="icon icon-link"></span></a>Global</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[global]

# By default, Streamlit displays a warning when a user sets both a widget
# default value in the function defining the widget and a widget value via
# the widget&#x27;s key in `st.session_state`.
#
# If you&#x27;d like to turn off this warning, set this to True.
#
# Default: false
disableWidgetStateDuplicationWarning = false

# If True, will show a warning when you run a Streamlit-enabled script
# via &quot;python my_script.py&quot;.
#
# Default: true
showWarningOnDirectExecution = true
</code></div></section>
<h4 id="logger"><a href="/develop/api-reference/configuration/config.toml#logger"><span class="icon icon-link"></span></a>Logger</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[logger]

# Level of logging for Streamlit&#x27;s internal logger: &quot;error&quot;, &quot;warning&quot;,
# &quot;info&quot;, or &quot;debug&quot;.
#
# Default: &quot;info&quot;
level = &quot;info&quot;

# String format for logging messages. If logger.datetimeFormat is set,
# logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`.
#
# See Python&#x27;s documentation for available attributes:
# https://docs.python.org/3/library/logging.html#formatter-objects
#
# Default: &quot;%(asctime)s %(message)s&quot;
messageFormat = &quot;%(asctime)s %(message)s&quot;
</code></div></section>
<h4 id="client"><a href="/develop/api-reference/configuration/config.toml#client"><span class="icon icon-link"></span></a>Client</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[client]

# Controls whether uncaught app exceptions and deprecation warnings
# are displayed in the browser. This can be one of the following:
#
# - &quot;full&quot;       : In the browser, Streamlit displays app deprecation
#                  warnings and exceptions, including exception types,
#                  exception messages, and associated tracebacks.
# - &quot;stacktrace&quot; : In the browser, Streamlit displays exceptions,
#                  including exception types, generic exception messages,
#                  and associated tracebacks. Deprecation warnings and
#                  full exception messages will only print to the
#                  console.
# - &quot;type&quot;       : In the browser, Streamlit displays exception types and
#                  generic exception messages. Deprecation warnings, full
#                  exception messages, and associated tracebacks only
#                  print to the console.
# - &quot;none&quot;       : In the browser, Streamlit displays generic exception
#                  messages. Deprecation warnings, full exception
#                  messages, associated tracebacks, and exception types
#                  will only print to the console.
# - True         : This is deprecated. Streamlit displays &quot;full&quot;
#                  error details.
# - False        : This is deprecated. Streamlit displays &quot;stacktrace&quot;
#                  error details.
#
# Default: &quot;full&quot;
showErrorDetails = &quot;full&quot;

# Change the visibility of items in the toolbar, options menu,
# and settings dialog (top right of the app).
#
# Allowed values:
# - &quot;auto&quot;      : Show the developer options if the app is accessed through
#                 localhost or through Streamlit Community Cloud as a developer.
#                 Hide them otherwise.
# - &quot;developer&quot; : Show the developer options.
# - &quot;viewer&quot;    : Hide the developer options.
# - &quot;minimal&quot;   : Show only options set externally (e.g. through
#                 Streamlit Community Cloud) or through st.set_page_config.
#                 If there are no options left, hide the menu.
#
# Default: &quot;auto&quot;
toolbarMode = &quot;auto&quot;

# Controls whether to display the default sidebar page navigation in a
# multi-page app. This only applies when app&#x27;s pages are defined by the
# `pages/` directory.
#
# Default: true
showSidebarNavigation = true
</code></div></section>
<h4 id="runner"><a href="/develop/api-reference/configuration/config.toml#runner"><span class="icon icon-link"></span></a>Runner</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[runner]

# Allows you to type a variable or string by itself in a single line of
# Python code to write it to the app.
#
# Default: true
magicEnabled = true

# Handle script rerun requests immediately, rather than waiting for
# script execution to reach a yield point.
#
# This makes Streamlit much more responsive to user interaction, but it
# can lead to race conditions in apps that mutate session_state data
# outside of explicit session_state assignment statements.
#
# Default: true
fastReruns = true

# Raise an exception after adding unserializable data to Session State.
#
# Some execution environments may require serializing all data in Session
# State, so it may be useful to detect incompatibility during development,
# or when the execution environment will stop supporting it in the future.
#
# Default: false
enforceSerializableSessionState = false

# Adjust how certain &#x27;options&#x27; widgets like radio, selectbox, and
# multiselect coerce Enum members.
#
# This is useful when the Enum class gets re-defined during a script
# re-run. For more information, check out the docs:
# https://docs.streamlit.io/develop/concepts/design/custom-classes#enums
#
# Allowed values:
# - &quot;off&quot;          : Disables Enum coercion.
# - &quot;nameOnly&quot;     : Enum classes can be coerced if their member names match.
# - &quot;nameAndValue&quot; : Enum classes can be coerced if their member names AND
#                    member values match.
#
# Default: &quot;nameOnly&quot;
enumCoercion = &quot;nameOnly&quot;
</code></div></section>
<h4 id="server"><a href="/develop/api-reference/configuration/config.toml#server"><span class="icon icon-link"></span></a>Server</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[server]

# List of directories to watch for changes.
#
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify additional
# directories to watch. Paths must be absolute.
#
# Default: []
folderWatchList = []

# List of directories to ignore for changes.
#
# By default, Streamlit watches files in the current working directory
# and its subdirectories. Use this option to specify exceptions within
# watched directories. Paths can be absolute or relative to the current
# working directory.
#
# Example: [&#x27;/home/user1/env&#x27;, &#x27;relative/path/to/folder&#x27;]
#
# Default: []
folderWatchBlacklist = []

# Change the type of file watcher used by Streamlit, or turn it off
# completely.
#
# Allowed values:
# - &quot;auto&quot;     : Streamlit will attempt to use the watchdog module, and
#                falls back to polling if watchdog isn&#x27;t available.
# - &quot;watchdog&quot; : Force Streamlit to use the watchdog module.
# - &quot;poll&quot;     : Force Streamlit to always use polling.
# - &quot;none&quot;     : Streamlit will not watch files.
#
# Default: &quot;auto&quot;
fileWatcherType = &quot;auto&quot;

# Symmetric key used to produce signed cookies. If deploying on multiple
# replicas, this should be set to the same value across all replicas to ensure
# they all share the same secret.
#
# Default: randomly generated secret key.
cookieSecret = &quot;a-random-key-appears-here&quot;

# If false, will attempt to open a browser window on start.
#
# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or
# (2) we are running in the Streamlit Atom plugin.
headless = false

# Whether to show a terminal prompt for the user&#x27;s email address when
# they run Streamlit (locally) for the first time. If you set
# `server.headless=True`, Streamlit will not show this prompt.
#
# Default: true
showEmailPrompt = true

# Automatically rerun script when the file is modified on disk.
#
# Default: false
runOnSave = false

# The address where the server will listen for client and browser
# connections.
#
# Use this if you want to bind the server to a specific address.
# If set, the server will only be accessible from this address, and not from
# any aliases (like localhost).
#
# Default: (unset)
address =

# The port where the server will listen for browser connections.
#
# Default: 8501
port = 8501

# The base path for the URL where Streamlit should be served from.
#
# Default: &quot;&quot;
baseUrlPath = &quot;&quot;

# Enables support for Cross-Origin Resource Sharing (CORS) protection,
# for added security.
#
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
#
# Default: true
enableCORS = true

# Allowed list of origins.
#
# If CORS protection is enabled (`server.enableCORS=True`), use this
# option to set a list of allowed origins that the Streamlit server will
# accept traffic from.
#
# This config option does nothing if CORS protection is disabled.
#
# Example: [&#x27;http://example.com&#x27;, &#x27;https://streamlit.io&#x27;]
#
# Default: []
corsAllowedOrigins = []

# Enables support for Cross-Site Request Forgery (XSRF) protection, for
# added security.
#
# If XSRF protection is enabled and CORS protection is disabled at the
# same time, Streamlit will enable them both instead.
#
# Default: true
enableXsrfProtection = true

# Max size, in megabytes, for files uploaded with the file_uploader.
#
# Default: 200
maxUploadSize = 200

# Max size, in megabytes, of messages that can be sent via the WebSocket
# connection.
#
# Default: 200
maxMessageSize = 200

# Enables support for websocket compression.
#
# Default: false
enableWebsocketCompression = false

# The interval (in seconds) at which the server pings the client to keep
# the websocket connection alive.
#
# The default value should work for most deployments. However, if you&#x27;re
# experiencing frequent disconnections in certain proxy setups (e.g.,
# &quot;Connection error&quot; messages), you may want to try adjusting this value.
#
# Note: When you set this option, Streamlit automatically sets the ping
# timeout to match this interval. For Tornado &gt;=6.5, a value less than 30
# may cause connection issues.
websocketPingInterval =

# Enable serving files from a `static` directory in the running app&#x27;s
# directory.
#
# Default: false
enableStaticServing = false

# TTL in seconds for sessions whose websockets have been disconnected.
#
# The server may choose to clean up session state, uploaded files, etc
# for a given session with no active websocket connection at any point
# after this time has passed. If you are using load balancing or
# replication in your deployment, you must enable session stickiness
# in your proxy to guarantee reconnection to the existing session. For
# more information, see https://docs.streamlit.io/replication.
#
# Default: 120
disconnectedSessionTTL = 120

# Server certificate file for connecting via HTTPS.
# Must be set at the same time as &quot;server.sslKeyFile&quot;.
#
# [&#x27;DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For a production environment, we
# recommend performing SSL termination through a load balancer or reverse
# proxy.&#x27;]
sslCertFile =

# Cryptographic key file for connecting via HTTPS.
# Must be set at the same time as &quot;server.sslCertFile&quot;.
#
# [&#x27;DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For a production environment, we
# recommend performing SSL termination through a load balancer or reverse
# proxy.&#x27;]
sslKeyFile =
</code></div></section>
<h4 id="browser"><a href="/develop/api-reference/configuration/config.toml#browser"><span class="icon icon-link"></span></a>Browser</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[browser]

# Internet address where users should point their browsers in order to
# connect to the app. Can be IP address or DNS name and path.
#
# This is used to:
# - Set the correct URL for CORS and XSRF protection purposes.
# - Show the URL on the terminal
# - Open the browser
#
# Default: &quot;localhost&quot;
serverAddress = &quot;localhost&quot;

# Whether to send usage statistics to Streamlit.
#
# Default: true
gatherUsageStats = true

# Port where users should point their browsers in order to connect to the
# app.
#
# This is used to:
# - Set the correct URL for XSRF protection purposes.
# - Show the URL on the terminal (part of `streamlit run`).
# - Open the browser automatically (part of `streamlit run`).
#
# This option is for advanced use cases. To change the port of your app, use
# `server.Port` instead.
#
# Default: whatever value is set in server.port.
serverPort = 8501
</code></div></section>
<h4 id="mapbox"><a href="/develop/api-reference/configuration/config.toml#mapbox"><span class="icon icon-link"></span></a>Mapbox</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[mapbox]

# If you&#x27;d like to show maps using Mapbox rather than Carto, use this
# to pass the Mapbox API token.
#
# THIS IS DEPRECATED.
#
# Instead of this, you should use either the MAPBOX_API_KEY environment
# variable or PyDeck&#x27;s `api_keys` argument.
#
# This option will be removed on or after 2026-05-01.
#
# Default: &quot;&quot;
token = &quot;&quot;
</code></div></section>
<h4 id="theme"><a href="/develop/api-reference/configuration/config.toml#theme"><span class="icon icon-link"></span></a>Theme</h4>
<p>To define switchable light and dark themes, the configuration options in the
<code>[theme]</code> table can be used in separate <code>[theme.dark]</code> and <code>[theme.light]</code>
tables, except for the following options:</p>
<ul>
<li><code>base</code></li>
<li><code>fontFaces</code></li>
<li><code>baseFontSize</code></li>
<li><code>baseFontWeight</code></li>
<li><code>showSidebarBorder</code></li>
<li><code>chartCategoricalColors</code></li>
<li><code>chartSequentialColors</code></li>
</ul>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[theme]

# The theme that your custom theme inherits from.
#
# This can be one of the following:
# - &quot;light&quot;: Streamlit&#x27;s default light theme.
# - &quot;dark&quot; : Streamlit&#x27;s default dark theme.
# - A local file path to a TOML theme file: A local custom theme, like
#   &quot;themes/custom.toml&quot;.
# - A URL to a TOML theme file: An externally hosted custom theme, like
#   &quot;https://example.com/theme.toml&quot;.
#
# A TOML theme file must contain a [theme] table with theme options.
# Any theme options defined in the app&#x27;s config.toml file will override
# those defined in the TOML theme file.
base =

# Primary accent color.
primaryColor =

# Background color of the app.
backgroundColor =

# Background color used for most interactive widgets.
secondaryBackgroundColor =

# Color used for almost all text.
textColor =

# Red color used in the basic color palette.
#
# By default, this is #ff4b4b for the light theme and #ff2b2b for the
# dark theme.
#
# If `redColor` is provided, and `redBackgroundColor` isn&#x27;t, then
# `redBackgroundColor` will be derived from `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
redColor =

# Orange color used in the basic color palette.
#
# By default, this is #ffa421 for the light theme and #ff8700 for the
# dark theme.
#
# If `orangeColor` is provided, and `orangeBackgroundColor` isn&#x27;t, then
# `orangeBackgroundColor` will be derived from `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
orangeColor =

# Yellow color used in the basic color palette.
#
# By default, this is #faca2b for the light theme and #ffe312 for the
# dark theme.
#
# If `yellowColor` is provided, and `yellowBackgroundColor` isn&#x27;t, then
# `yellowBackgroundColor` will be derived from `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
yellowColor =

# Blue color used in the basic color palette.
#
# By default, this is #1c83e1 for the light theme and #0068c9 for the
# dark theme.
#
# If a `blueColor` is provided, and `blueBackgroundColor` isn&#x27;t, then
# `blueBackgroundColor` will be derived from `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
blueColor =

# Green color used in the basic color palette.
#
# By default, this is #21c354 for the light theme and #09ab3b for the
# dark theme.
#
# If `greenColor` is provided, and `greenBackgroundColor` isn&#x27;t, then
# `greenBackgroundColor` will be derived from `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
greenColor =

# Violet color used in the basic color palette.
#
# By default, this is #803df5 for both the light and dark themes.
#
# If a `violetColor` is provided, and `violetBackgroundColor` isn&#x27;t, then
# `violetBackgroundColor` will be derived from `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
violetColor =

# Gray color used in the basic color palette.
#
# By default, this is #a3a8b8 for the light theme and #555867 for the
# dark theme.
#
# If `grayColor` is provided, and `grayBackgroundColor` isn&#x27;t, then
# `grayBackgroundColor` will be derived from `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
grayColor =

# Red background color used in the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ff2b2b with 10% opacity for light theme and
# #ff6c6c with 20% opacity for dark theme.
redBackgroundColor =

# Orange background color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffa421 with 10% opacity for the light theme and
# #ff8700 with 20% opacity for the dark theme.
orangeBackgroundColor =

# Yellow background color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffff12 with 10% opacity for the light theme and
# #ffff12 with 20% opacity for the dark theme.
yellowBackgroundColor =

# Blue background color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #1c83ff with 10% opacity for the light theme and
# #3d9df3 with 20% opacity for the dark theme.
blueBackgroundColor =

# Green background color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #21c354 with 10% opacity for the light theme and
# #3dd56d with 20% opacity for the dark theme.
greenBackgroundColor =

# Violet background color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #9a5dff with 10% opacity for light theme and
# #9a5dff with 20% opacity for dark theme.
violetBackgroundColor =

# Gray background color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #31333f with 10% opacity for the light theme and
# #808495 with 20% opacity for the dark theme.
grayBackgroundColor =

# Red text color used for the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor`, darkened by 15%
# for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark
# theme.
redTextColor =

# Orange text color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark
# theme.
orangeTextColor =

# Yellow text color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark
# theme.
yellowTextColor =

# Blue text color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark
# theme.
blueTextColor =

# Green text color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #158237 for the light theme and #5ce488 for the dark
# theme.
greenTextColor =

# Violet text color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #583f84 for the light theme and #b27eff for the dark
# theme.
violetTextColor =

# Gray text color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #31333f with 60% opacity for the light theme and
# #fafafa with 60% opacity for the dark theme.
grayTextColor =

# Color used for all links.
#
# This defaults to the resolved value of `blueTextColor`.
linkColor =

# Whether or not links should be displayed with an underline.
linkUnderline =

# Text color used for code blocks.
#
# This defaults to the resolved value of `greenTextColor`.
codeTextColor =

# Background color used for code blocks.
codeBackgroundColor =

# The font family for all text, except code blocks.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;Nunito:https://fonts.googleapis.com/css2?family=Nunito&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# For example, you can use the following:
#
# font = &quot;cool-font, fallback-cool-font, sans-serif&quot;
font =

# An array of fonts to use in your app.
#
# Each font in the array is a table (dictionary) that can have the
# following attributes, closely resembling CSS font-face definitions:
# - family
# - url
# - weight (optional)
# - style (optional)
# - unicodeRange (optional)
#
# To host a font with your app, enable static file serving with
# `server.enableStaticServing=true`.
#
# You can define multiple [[theme.fontFaces]] tables, including multiple
# tables with the same family if your font is defined by multiple files.
#
# For example, a font hosted with your app may have a [[theme.fontFaces]]
# table as follows:
#
# [[theme.fontFaces]]
# family = &quot;font_name&quot;
# url = &quot;app/static/font_file.woff&quot;
# weight = &quot;400&quot;
# style = &quot;normal&quot;
fontFaces =

# The root font size (in pixels) for the app.
#
# This determines the overall scale of text and UI elements. This is a
# positive integer.
#
# If this isn&#x27;t set, the font size will be 16px.
baseFontSize =

# The root font weight for the app.
#
# This determines the overall weight of text and UI elements. This is an
# integer multiple of 100. Values can be between 100 and 600, inclusive.
#
# If this isn&#x27;t set, the font weight will be set to 400 (normal weight).
baseFontWeight =

# The font family to use for headings.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;Nunito:https://fonts.googleapis.com/css2?family=Nunito&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# If this isn&#x27;t set, Streamlit uses `theme.font` for headings.
headingFont =

# One or more font sizes for h1-h6 headings.
#
# If no sizes are set, Streamlit will use the default sizes for h1-h6
# headings. Heading font sizes set in [theme] are not inherited by
# [theme.sidebar]. The following sizes are used by default:
# [
#     &quot;2.75rem&quot;, # h1 (1.5rem for sidebar)
#     &quot;2.25rem&quot;, # h2 (1.25rem for sidebar)
#     &quot;1.75rem&quot;, # h3 (1.125rem for sidebar)
#     &quot;1.5rem&quot;, # h4 (1rem for sidebar)
#     &quot;1.25rem&quot;, # h5 (0.875rem for sidebar)
#     &quot;1rem&quot;, # h6 (0.75rem for sidebar)
# ]
#
# If you specify an array with fewer than six sizes, the unspecified
# heading sizes will be the default values. For example, you can use the
# following array to set the font sizes for h1-h3 headings while keeping
# h4-h6 headings at their default sizes:
# headingFontSizes = [&quot;3rem&quot;, &quot;2.875rem&quot;, &quot;2.75rem&quot;]
#
# Setting a single value (not in an array) will set the font size for all
# h1-h6 headings to that value:
# headingFontSizes = &quot;2.75rem&quot;
#
# Font sizes can be specified in pixels or rem, but rem is recommended.
headingFontSizes =

# One or more font weights for h1-h6 headings.
#
# If no weights are set, Streamlit will use the default weights for h1-h6
# headings. Heading font weights set in [theme] are not inherited by
# [theme.sidebar]. The following weights are used by default:
# [
#     700, # h1 (bold)
#     600, # h2 (semi-bold)
#     600, # h3 (semi-bold)
#     600, # h4 (semi-bold)
#     600, # h5 (semi-bold)
#     600, # h6 (semi-bold)
# ]
#
# If you specify an array with fewer than six weights, the unspecified
# heading weights will be the default values. For example, you can use
# the following array to set the font weights for h1-h2 headings while
# keeping h3-h6 headings at their default weights:
# headingFontWeights = [800, 700]
#
# Setting a single value (not in an array) will set the font weight for
# all h1-h6 headings to that value:
# headingFontWeights = 500
headingFontWeights =

# The font family to use for code (monospace) in the sidebar.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;&#x27;Space Mono&#x27;:https://fonts.googleapis.com/css2?family=Space+Mono&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
codeFont =

# The font size (in pixels or rem) for code blocks and code text.
#
# This applies to font in code blocks, `st.json`, and `st.help`. It
# doesn&#x27;t apply to inline code, which is set by default to 0.75em.
#
# If this isn&#x27;t set, the code font size will be 0.875rem.
codeFontSize =

# The font weight for code blocks and code text.
#
# This applies to font in inline code, code blocks, `st.json`, and
# `st.help`. This is an integer multiple of 100. Values can be between
# 100 and 600, inclusive.
#
# If this isn&#x27;t set, the code font weight will be 400 (normal weight).
codeFontWeight =

# The radius used as basis for the corners of most UI elements.
#
# This can be one of the following:
# - &quot;none&quot;
# - &quot;small&quot;
# - &quot;medium&quot;
# - &quot;large&quot;
# - &quot;full&quot;
# - The number in pixels or rem.
#
# For example, you can use &quot;10px&quot;, &quot;0.5rem&quot;, or &quot;2rem&quot;. To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =

# The radius used as basis for the corners of buttons.
#
# This can be one of the following:
# - &quot;none&quot;
# - &quot;small&quot;
# - &quot;medium&quot;
# - &quot;large&quot;
# - &quot;full&quot;
# - The number in pixels or rem.
#
# For example, you can use &quot;10px&quot;, &quot;0.5rem&quot;, or &quot;2rem&quot;. To follow best
# practices, use rem instead of pixels when specifying a numeric size.
#
# If this isn&#x27;t set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =

# The color of the border around elements.
borderColor =

# The color of the border around dataframes and tables.
#
# If this isn&#x27;t set, Streamlit uses `theme.borderColor` instead.
dataframeBorderColor =

# The background color of the dataframe&#x27;s header.
#
# This color applies to all non-interior cells of the dataframe. This
# includes the header row, the row-selection column (if present), and
# the bottom row of data editors with a dynamic number of rows. If this
# isn&#x27;t set, Streamlit uses a mix of `theme.backgroundColor` and
# `theme.secondaryBackgroundColor`.
dataframeHeaderBackgroundColor =

# Whether to show a border around input widgets.
showWidgetBorder =

# Whether to show a vertical separator between the sidebar and the main
# content area.
showSidebarBorder =

# An array of colors to use for categorical chart data.
#
# This is a list of one or more color strings which are applied in order
# to categorical data. These colors apply to Plotly, Altair, and
# Vega-Lite charts.
#
# Invalid colors are skipped, and colors repeat cyclically if there are
# more categories than colors. If no chart categorical colors are set,
# Streamlit uses a default set of colors.
#
# For light themes, the following colors are the default:
# [
#     &quot;#0068c9&quot;, # blue80
#     &quot;#83c9ff&quot;, # blue40
#     &quot;#ff2b2b&quot;, # red80
#     &quot;#ffabab&quot;, # red40
#     &quot;#29b09d&quot;, # blueGreen80
#     &quot;#7defa1&quot;, # green40
#     &quot;#ff8700&quot;, # orange80
#     &quot;#ffd16a&quot;, # orange50
#     &quot;#6d3fc0&quot;, # purple80
#     &quot;#d5dae5&quot;, # gray40
# ]
# For dark themes, the following colors are the default:
# [
#     &quot;#83c9ff&quot;, # blue40
#     &quot;#0068c9&quot;, # blue80
#     &quot;#ffabab&quot;, # red40
#     &quot;#ff2b2b&quot;, # red80
#     &quot;#7defa1&quot;, # green40
#     &quot;#29b09d&quot;, # blueGreen80
#     &quot;#ffd16a&quot;, # orange50
#     &quot;#ff8700&quot;, # orange80
#     &quot;#6d3fc0&quot;, # purple80
#     &quot;#d5dae5&quot;, # gray40
# ]
chartCategoricalColors =

# An array of ten colors to use for sequential or continuous chart data.
#
# The ten colors create a gradient color scale. These colors apply to
# Plotly, Altair, and Vega-Lite charts.
#
# Invalid color strings are skipped. If there are not exactly ten
# valid colors specified, Streamlit uses a default set of colors.
#
# For light themes, the following colors are the default:
# [
#     &quot;#e4f5ff&quot;, #blue10
#     &quot;#c7ebff&quot;, #blue20
#     &quot;#a6dcff&quot;, #blue30
#     &quot;#83c9ff&quot;, #blue40
#     &quot;#60b4ff&quot;, #blue50
#     &quot;#3d9df3&quot;, #blue60
#     &quot;#1c83e1&quot;, #blue70
#     &quot;#0068c9&quot;, #blue80
#     &quot;#0054a3&quot;, #blue90
#     &quot;#004280&quot;, #blue100
# ]
# For dark themes, the following colors are the default:
# [
#     &quot;#004280&quot;, #blue100
#     &quot;#0054a3&quot;, #blue90
#     &quot;#0068c9&quot;, #blue80
#     &quot;#1c83e1&quot;, #blue70
#     &quot;#3d9df3&quot;, #blue60
#     &quot;#60b4ff&quot;, #blue50
#     &quot;#83c9ff&quot;, #blue40
#     &quot;#a6dcff&quot;, #blue30
#     &quot;#c7ebff&quot;, #blue20
#     &quot;#e4f5ff&quot;, #blue10
# ]
chartSequentialColors =
</code></div></section>
<h4 id="sidebar-theme"><a href="/develop/api-reference/configuration/config.toml#sidebar-theme"><span class="icon icon-link"></span></a>Sidebar theme</h4>
<p>To define switchable light and dark themes, the configuration options in the
<code>[theme.sidebar]</code> table can be used in separate <code>[theme.dark.sidebar]</code> and
<code>[theme.light.sidebar]</code>.</p>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[theme.sidebar]

# Primary accent color.
primaryColor =

# Background color of the app.
backgroundColor =

# Background color used for most interactive widgets.
secondaryBackgroundColor =

# Color used for almost all text.
textColor =

# Red color used in the basic color palette.
#
# By default, this is #ff4b4b for the light theme and #ff2b2b for the
# dark theme.
#
# If `redColor` is provided, and `redBackgroundColor` isn&#x27;t, then
# `redBackgroundColor` will be derived from `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
redColor =

# Orange color used in the basic color palette.
#
# By default, this is #ffa421 for the light theme and #ff8700 for the
# dark theme.
#
# If `orangeColor` is provided, and `orangeBackgroundColor` isn&#x27;t, then
# `orangeBackgroundColor` will be derived from `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
orangeColor =

# Yellow color used in the basic color palette.
#
# By default, this is #faca2b for the light theme and #ffe312 for the
# dark theme.
#
# If `yellowColor` is provided, and `yellowBackgroundColor` isn&#x27;t, then
# `yellowBackgroundColor` will be derived from `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
yellowColor =

# Blue color used in the basic color palette.
#
# By default, this is #1c83e1 for the light theme and #0068c9 for the
# dark theme.
#
# If a `blueColor` is provided, and `blueBackgroundColor` isn&#x27;t, then
# `blueBackgroundColor` will be derived from `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
blueColor =

# Green color used in the basic color palette.
#
# By default, this is #21c354 for the light theme and #09ab3b for the
# dark theme.
#
# If `greenColor` is provided, and `greenBackgroundColor` isn&#x27;t, then
# `greenBackgroundColor` will be derived from `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
greenColor =

# Violet color used in the basic color palette.
#
# By default, this is #803df5 for both the light and dark themes.
#
# If a `violetColor` is provided, and `violetBackgroundColor` isn&#x27;t, then
# `violetBackgroundColor` will be derived from `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
violetColor =

# Gray color used in the basic color palette.
#
# By default, this is #a3a8b8 for the light theme and #555867 for the
# dark theme.
#
# If `grayColor` is provided, and `grayBackgroundColor` isn&#x27;t, then
# `grayBackgroundColor` will be derived from `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
grayColor =

# Red background color used in the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ff2b2b with 10% opacity for light theme and
# #ff6c6c with 20% opacity for dark theme.
redBackgroundColor =

# Orange background color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffa421 with 10% opacity for the light theme and
# #ff8700 with 20% opacity for the dark theme.
orangeBackgroundColor =

# Yellow background color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #ffff12 with 10% opacity for the light theme and
# #ffff12 with 20% opacity for the dark theme.
yellowBackgroundColor =

# Blue background color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #1c83ff with 10% opacity for the light theme and
# #3d9df3 with 20% opacity for the dark theme.
blueBackgroundColor =

# Green background color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #21c354 with 10% opacity for the light theme and
# #3dd56d with 20% opacity for the dark theme.
greenBackgroundColor =

# Violet background color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #9a5dff with 10% opacity for light theme and
# #9a5dff with 20% opacity for dark theme.
violetBackgroundColor =

# Gray background color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor` using 10%
# opacity for the light theme and 20% opacity for the dark theme.
#
# Otherwise, this is #31333f with 10% opacity for the light theme and
# #808495 with 20% opacity for the dark theme.
grayBackgroundColor =

# Red text color used for the basic color palette.
#
# If `redColor` is provided, this defaults to `redColor`, darkened by 15%
# for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark
# theme.
redTextColor =

# Orange text color used for the basic color palette.
#
# If `orangeColor` is provided, this defaults to `orangeColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark
# theme.
orangeTextColor =

# Yellow text color used for the basic color palette.
#
# If `yellowColor` is provided, this defaults to `yellowColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark
# theme.
yellowTextColor =

# Blue text color used for the basic color palette.
#
# If `blueColor` is provided, this defaults to `blueColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark
# theme.
blueTextColor =

# Green text color used for the basic color palette.
#
# If `greenColor` is provided, this defaults to `greenColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #158237 for the light theme and #5ce488 for the dark
# theme.
greenTextColor =

# Violet text color used for the basic color palette.
#
# If `violetColor` is provided, this defaults to `violetColor`, darkened
# by 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #583f84 for the light theme and #b27eff for the dark
# theme.
violetTextColor =

# Gray text color used for the basic color palette.
#
# If `grayColor` is provided, this defaults to `grayColor`, darkened by
# 15% for the light theme and lightened by 15% for the dark theme.
#
# Otherwise, this is #31333f with 60% opacity for the light theme and
# #fafafa with 60% opacity for the dark theme.
grayTextColor =

# Color used for all links.
#
# This defaults to the resolved value of `blueTextColor`.
linkColor =

# Whether or not links should be displayed with an underline.
linkUnderline =

# Text color used for code blocks.
#
# This defaults to the resolved value of `greenTextColor`.
codeTextColor =

# Background color used for code blocks.
codeBackgroundColor =

# The font family for all text, except code blocks.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;Nunito:https://fonts.googleapis.com/css2?family=Nunito&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# For example, you can use the following:
#
# font = &quot;cool-font, fallback-cool-font, sans-serif&quot;
font =

# The font family to use for headings.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;Nunito:https://fonts.googleapis.com/css2?family=Nunito&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
#   fallbacks
#
# If this isn&#x27;t set, Streamlit uses `theme.font` for headings.
headingFont =

# One or more font sizes for h1-h6 headings.
#
# If no sizes are set, Streamlit will use the default sizes for h1-h6
# headings. Heading font sizes set in [theme] are not inherited by
# [theme.sidebar]. The following sizes are used by default:
# [
#     &quot;2.75rem&quot;, # h1 (1.5rem for sidebar)
#     &quot;2.25rem&quot;, # h2 (1.25rem for sidebar)
#     &quot;1.75rem&quot;, # h3 (1.125rem for sidebar)
#     &quot;1.5rem&quot;, # h4 (1rem for sidebar)
#     &quot;1.25rem&quot;, # h5 (0.875rem for sidebar)
#     &quot;1rem&quot;, # h6 (0.75rem for sidebar)
# ]
#
# If you specify an array with fewer than six sizes, the unspecified
# heading sizes will be the default values. For example, you can use the
# following array to set the font sizes for h1-h3 headings while keeping
# h4-h6 headings at their default sizes:
# headingFontSizes = [&quot;3rem&quot;, &quot;2.875rem&quot;, &quot;2.75rem&quot;]
#
# Setting a single value (not in an array) will set the font size for all
# h1-h6 headings to that value:
# headingFontSizes = &quot;2.75rem&quot;
#
# Font sizes can be specified in pixels or rem, but rem is recommended.
headingFontSizes =

# One or more font weights for h1-h6 headings.
#
# If no weights are set, Streamlit will use the default weights for h1-h6
# headings. Heading font weights set in [theme] are not inherited by
# [theme.sidebar]. The following weights are used by default:
# [
#     700, # h1 (bold)
#     600, # h2 (semi-bold)
#     600, # h3 (semi-bold)
#     600, # h4 (semi-bold)
#     600, # h5 (semi-bold)
#     600, # h6 (semi-bold)
# ]
#
# If you specify an array with fewer than six weights, the unspecified
# heading weights will be the default values. For example, you can use
# the following array to set the font weights for h1-h2 headings while
# keeping h3-h6 headings at their default weights:
# headingFontWeights = [800, 700]
#
# Setting a single value (not in an array) will set the font weight for
# all h1-h6 headings to that value:
# headingFontWeights = 500
headingFontWeights =

# The font family to use for code (monospace) in the sidebar.
#
# This can be one of the following:
# - &quot;sans-serif&quot;
# - &quot;serif&quot;
# - &quot;monospace&quot;
# - The `family` value for a custom font table under [[theme.fontFaces]]
# - A URL to a CSS file in the format of &quot;&lt;font name&gt;:&lt;url&gt;&quot; (like
#   &quot;&#x27;Space Mono&#x27;:https://fonts.googleapis.com/css2?family=Space+Mono&amp;display=swap&quot;)
# - A comma-separated list of these (as a single string) to specify
# fallbacks
codeFont =

# The font size (in pixels or rem) for code blocks and code text.
#
# This applies to font in code blocks, `st.json`, and `st.help`. It
# doesn&#x27;t apply to inline code, which is set by default to 0.75em.
#
# If this isn&#x27;t set, the code font size will be 0.875rem.
codeFontSize =

# The font weight for code blocks and code text.
#
# This applies to font in inline code, code blocks, `st.json`, and
# `st.help`. This is an integer multiple of 100. Values can be between
# 100 and 600, inclusive.
#
# If this isn&#x27;t set, the code font weight will be 400 (normal weight).
codeFontWeight =

# The radius used as basis for the corners of most UI elements.
#
# This can be one of the following:
# - &quot;none&quot;
# - &quot;small&quot;
# - &quot;medium&quot;
# - &quot;large&quot;
# - &quot;full&quot;
# - The number in pixels or rem.
#
# For example, you can use &quot;10px&quot;, &quot;0.5rem&quot;, or &quot;2rem&quot;. To follow best
# practices, use rem instead of pixels when specifying a numeric size.
baseRadius =

# The radius used as basis for the corners of buttons.
#
# This can be one of the following:
# - &quot;none&quot;
# - &quot;small&quot;
# - &quot;medium&quot;
# - &quot;large&quot;
# - &quot;full&quot;
# - The number in pixels or rem.
#
# For example, you can use &quot;10px&quot;, &quot;0.5rem&quot;, or &quot;2rem&quot;. To follow best
# practices, use rem instead of pixels when specifying a numeric size.
#
# If this isn&#x27;t set, Streamlit uses `theme.baseRadius` instead.
buttonRadius =

# The color of the border around elements.
borderColor =

# The color of the border around dataframes and tables.
#
# If this isn&#x27;t set, Streamlit uses `theme.borderColor` instead.
dataframeBorderColor =

# The background color of the dataframe&#x27;s header.
#
# This color applies to all non-interior cells of the dataframe. This
# includes the header row, the row-selection column (if present), and
# the bottom row of data editors with a dynamic number of rows. If this
# isn&#x27;t set, Streamlit uses a mix of `theme.backgroundColor` and
# `theme.secondaryBackgroundColor`.
dataframeHeaderBackgroundColor =

# Whether to show a border around input widgets.
showWidgetBorder =
</code></div></section>
<h4 id="secrets"><a href="/develop/api-reference/configuration/config.toml#secrets"><span class="icon icon-link"></span></a>Secrets</h4>
<section class="code_Container__pq3Nr"><div class="code_Pre__3lyyf"><code class="language-toml">[secrets]

# List of locations where secrets are searched.
#
# An entry can be a path to a TOML file or directory path where
# Kubernetes style secrets are saved. Order is important, import is
# first to last, so secrets in later files will take precedence over
# earlier ones.
#
# Default: [ &lt;path to local environment&#x27;s secrets.toml file&gt;, &lt;path to project&#x27;s secrets.toml file&gt;,]
files = [ &quot;~/.streamlit/secrets.toml&quot;, &quot;~/project directory/.streamlit/secrets.toml&quot;,]
</code></div></section><section class="arrowLinkContainer_Container__QwLgW"><a class="not-link group iconLink_Link__qHAvu" target="_self" href="/develop/api-reference/configuration"><i class="iconLink_Icon__Qdy_b">arrow_back</i><span class="iconLink_Truncate__ZFSBK"><span class="arrowLink_Text__Xu0t4">Previous: </span>Configuration</span></a><a class="not-link group iconLink_Link__qHAvu" target="_self" href="/develop/api-reference/configuration/st.get_option"><i class="iconLink_Icon__Qdy_b arrowLink_NextIcon__btU_f">arrow_forward</i><span class="iconLink_Truncate__ZFSBK"><span class="arrowLink_Text__Xu0t4">Next: </span>st.get_option</span></a></section><section class="psa_Container__YutqA"><i class="psa_Icon__7ImKM">forum</i><article><h3 class="psa_Title__7EKIa">Still have questions?</h3><p class="psa_Text__mBnWO">Our<!-- --> <a href="https://discuss.streamlit.io" target="_blank" class="psa_Link__cbXKJ">forums</a> <!-- -->are full of helpful information and Streamlit experts.</p></article></section></div></article></section><footer class="footer_Container__r6lKu"><section class="footer_InnerContainer__9_p3M"><hr class="footer_Separator__TSG4w"/><nav class="footer_Navigation__zXrVS"><a class="
              not-link
              footer_Link__TT7vI
            " href="/">Home</a><a class="
              not-link
              footer_Link__TT7vI
            " href="mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20">Contact Us</a><a class="
              not-link
              footer_Link__TT7vI
            " href="https://discuss.streamlit.io" target="_blank" rel="noopener noreferrer">Community</a></nav><section class="footer_SocialNetworks__R4rxr"><a class="
              group
              not-link
              footer_IconLink__V7Rkz
            " href="https://github.com/streamlit" target="_blank" title="GitHub"><i class="footer_IconContainer__ujaTd"><svg width="22" height="20" viewBox="0 0 22 20" fill="none" xmlns="http://www.w3.org/2000/svg" class="
                  footer_Icon___CVBl
                  footer_GitHubIcon__uXZXa
                "><path d="M12.8513 14.5613C13.2388 14.4967 13.56 14.4506 13.8718 14.3768C16.168 13.8508 17.3491 12.4668 17.4908 10.1508C17.5664 8.98815 17.368 7.91781 16.5837 6.99511C16.5081 6.90283 16.5081 6.70907 16.5459 6.57989C16.716 5.8694 16.6688 5.17737 16.4609 4.48534C16.3759 4.20853 16.2152 4.07013 15.9601 4.1624C15.242 4.42075 14.5427 4.71602 13.8246 4.97438C13.5978 5.05742 13.3238 5.13124 13.0876 5.0851C11.6135 4.78984 10.1489 4.79906 8.6843 5.09433C8.46697 5.14047 8.21184 5.06665 7.99451 4.98361C7.32363 4.72525 6.67164 4.42075 6.00075 4.18085C5.62279 4.04244 5.33932 4.20853 5.32042 4.62375C5.29207 5.27887 5.30152 5.92477 5.28262 6.57989C5.28262 6.73675 5.28262 6.92129 5.19758 7.04124C3.00539 10.1323 4.70623 13.9246 8.56146 14.5059C8.6654 14.5244 8.77879 14.5336 8.86383 14.5428C8.70319 14.9581 8.55201 15.3733 8.37248 15.77C8.32523 15.8715 8.17405 15.9638 8.05121 16.0007C7.01181 16.3698 6.0858 16.0653 5.44326 15.1887C5.19758 14.8566 4.92356 14.5152 4.58339 14.2937C4.31882 14.1184 3.94085 14.0999 3.61013 14.0446C3.52509 14.0261 3.37391 14.1092 3.34556 14.1738C3.31721 14.2384 3.37391 14.4044 3.44005 14.4506C4.28102 14.9304 4.60229 15.7793 5.07474 16.5451C5.55665 17.3386 6.41651 17.4401 7.27638 17.4401C7.6071 17.4401 7.92837 17.394 8.32523 17.3571C8.32523 18.003 8.34413 18.612 8.31578 19.221C8.29688 19.6177 7.94727 19.8023 7.50316 19.6085C6.69054 19.2579 5.84957 18.9165 5.11254 18.4367C1.58803 16.1484 -0.112807 11.9408 0.803755 7.90858C1.71087 3.88558 5.07474 0.776064 9.23234 0.130169C14.4671 -0.69104 19.5319 2.51075 20.8642 7.49337C22.2059 12.4944 19.4563 17.717 14.5522 19.5162C13.7018 19.83 13.4655 19.6639 13.4655 18.7781C13.475 18.1783 13.475 17.5785 13.4844 16.9788C13.5033 16.1299 13.5033 15.2902 12.8513 14.5613Z"></path></svg></i></a><a class="
              group
              not-link
              footer_IconLink__V7Rkz
            " href="https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q" target="_blank" title="YouTube"><i class="footer_IconContainer__ujaTd"><svg width="26" height="18" viewBox="0 0 26 18" fill="none" xmlns="http://www.w3.org/2000/svg" class="
                  footer_Icon___CVBl
                  footer_YouTubeIcon__zFYFV
                "><path d="M12.8276 17.8757C11.0323 17.845 9.2319 17.845 7.43665 17.7734C6.06686 17.7172 4.69189 17.6251 3.33767 17.4308C1.63581 17.1853 0.546208 16.0449 0.333476 14.3471C0.17263 13.0227 0.058481 11.6879 0.0221609 10.3532C-0.0193478 8.93159 0.0117837 7.50995 0.0792353 6.0883C0.125933 5.13713 0.271213 4.19107 0.411305 3.25012C0.634414 1.74666 2.0509 0.723891 3.25984 0.57559C4.56736 0.417061 5.89045 0.284101 7.20835 0.253418C10.1555 0.186939 13.1026 0.156256 16.0445 0.181825C17.8398 0.197166 19.635 0.325012 21.4251 0.422175C21.8972 0.447744 22.3694 0.514224 22.8364 0.606273C24.284 0.892648 25.1609 1.77223 25.4722 3.18364C25.7627 4.49279 25.8406 5.8275 25.908 7.16221C26.017 9.37138 25.9495 11.5703 25.6745 13.7642C25.5863 14.4443 25.5085 15.1449 25.1401 15.7483C24.5123 16.7711 23.568 17.3592 22.3746 17.4666C20.8024 17.6098 19.2251 17.7274 17.6478 17.7785C16.0445 17.8297 14.4309 17.7888 12.8276 17.7888C12.8276 17.8245 12.8276 17.8501 12.8276 17.8757ZM10.4875 12.9511C12.6667 11.6266 14.8096 10.3277 16.994 9.00319C14.7993 7.67359 12.6564 6.37468 10.4875 5.05531C10.4875 7.70427 10.4875 10.3021 10.4875 12.9511Z"></path></svg></i></a><a class="
              group
              not-link
              footer_IconLink__V7Rkz
            " href="https://twitter.com/streamlit" target="_blank" title="Twitter"><i class="footer_IconContainer__ujaTd"><svg width="24" height="18" viewBox="0 0 24 18" xmlns="http://www.w3.org/2000/svg" class="
                  footer_Icon___CVBl
                  footer_TwitterIcon__wmehw
                "><path d="M22.9683 0.526535C22.5928 1.56402 21.8955 2.36683 20.9031 2.95968C21.368 2.91851 21.8239 2.83205 22.271 2.71678C22.7225 2.60562 23.1561 2.45741 23.5986 2.28449C23.5986 2.32566 23.5763 2.34625 23.5629 2.36683C22.946 3.19435 22.1994 3.91071 21.3233 4.51179C21.2428 4.56943 21.207 4.61883 21.2115 4.71764C21.2651 6.1133 21.0595 7.47603 20.6214 8.81405C20.1029 10.3867 19.3072 11.8277 18.2119 13.1287C16.9334 14.6478 15.3554 15.8376 13.469 16.6693C12.3156 17.1798 11.1042 17.5174 9.8391 17.7068C9.10597 17.8138 8.37284 17.8673 7.63078 17.8797C5.98571 17.9044 4.38982 17.6656 2.83863 17.1674C1.87305 16.8545 0.952171 16.4428 0.0804651 15.9365C0.0536434 15.92 0.0178811 15.9118 0 15.8788C2.633 16.1217 5.00672 15.5206 7.11669 14.0426C5.87395 13.9809 4.79662 13.5774 3.89362 12.787C3.29907 12.2682 2.87886 11.6465 2.62406 10.9178C3.34824 11.0372 4.05902 11.0208 4.79215 10.8478C3.3393 10.5308 2.24408 9.7939 1.52437 8.61232C1.10863 7.93301 0.920879 7.19607 0.925349 6.40149C1.60483 6.7432 2.32008 6.92847 3.10238 6.9614C2.93698 6.84201 2.78052 6.7432 2.64194 6.62793C1.82835 5.96921 1.29638 5.15404 1.07287 4.18243C0.822532 3.09554 0.992403 2.06218 1.5646 1.08645C1.61824 0.991756 1.62271 0.995873 1.69424 1.0741C2.70452 2.19392 3.88468 3.13259 5.23917 3.88189C6.67413 4.67647 8.22085 5.20756 9.87039 5.4834C10.4113 5.57398 10.9567 5.63161 11.5065 5.66043C11.5914 5.66455 11.6183 5.66043 11.6004 5.56574C11.3053 4.10009 11.6674 2.79088 12.7403 1.67106C13.5271 0.843544 14.5284 0.357738 15.7131 0.221878C17.1167 0.0571976 18.3729 0.398908 19.4726 1.23054C19.6022 1.32935 19.7184 1.43227 19.8347 1.54343C19.8749 1.58049 19.9106 1.58872 19.9732 1.58049C21.0059 1.38699 21.9714 1.04116 22.8834 0.559471C22.9057 0.543003 22.9236 0.522418 22.9683 0.526535Z"></path></svg></i></a><a class="
              group
              not-link
              footer_IconLink__V7Rkz
            " href="https://www.linkedin.com/company/streamlit" target="_blank" title="LinkedIn"><i class="footer_IconContainer__ujaTd"><svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="
                  footer_Icon___CVBl
                  footer_LinkedInIcon__5XBpv
                "><path d="M22.228 0H1.772A1.772 1.772 0 0 0 0 1.772v20.456A1.772 1.772 0 0 0 1.772 24h20.456A1.772 1.772 0 0 0 24 22.228V1.772A1.772 1.772 0 0 0 22.228 0ZM7.153 20.445H3.545V8.983h3.608v11.462ZM5.347 7.395a2.072 2.072 0 1 1 2.083-2.07 2.042 2.042 0 0 1-2.083 2.07Zm15.106 13.06h-3.606v-6.262c0-1.846-.785-2.416-1.799-2.416-1.07 0-2.12.806-2.12 2.463v6.215H9.32V8.992h3.47v1.588h.047c.348-.705 1.568-1.91 3.43-1.91 2.013 0 4.188 1.195 4.188 4.695l-.002 7.09Z"></path></svg></i></a><a class="
              group
              not-link
              footer_IconLink__V7Rkz
            " href="https://info.snowflake.com/streamlit-newsletter-sign-up.html" target="_blank" title="Newsletter"><i class="footer_IconContainer__ujaTd"><svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="
                  footer_Icon___CVBl
                  footer_NewsletterIcon__16vXD
                "><path d="M21.75 6.75v10.5a1.5 1.5 0 0 1-1.5 1.5H3.75a1.5 1.5 0 0 1-1.5-1.5V6.75m19.5 0a1.5 1.5 0 0 0-1.5-1.5H3.75a1.5 1.5 0 0 0-1.5 1.5m19.5 0-8.896 6.159a1.5 1.5 0 0 1-1.708 0L2.25 6.75" stroke="#a3a8b8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"></path></svg></i></a></section><div class="footer_Copyright__pxXlR"><span>© <!-- -->2025<!-- --> Snowflake Inc.</span></div></section></footer></section></div><div class="chatSticky_Container__G7L0R"><button id="kapa-ai" type="button" class="kapa_AskButton__ds4p5"><i class="kapa_AskIcon__fMtkD">forum</i> Ask AI</button><script src="https://widget.kapa.ai/kapa-widget.bundle.js" data-website-id="e81c2b35-6c03-4576-a56c-3c825f866e06" data-project-name="Streamlit" data-project-color="#000000" data-project-logo="https://docs.streamlit.io/logo.svg" data-modal-title="Streamlit docs assistant (beta)" data-modal-disclaimer=" This AI chatbot is powered by kapa.ai and public Streamlit information. Answers may be inaccurate, inefficient, or biased. Any use or decisions based on such answers should include reasonable practices including human oversight to ensure they are safe, accurate, and suitable for your intended purpose. Streamlit is not liable for any actions, losses, or damages resulting from the use of the chatbot.  You are hereby notified that this chat may be recorded, monitored, and stored to improve our services. Do not enter any private, sensitive, personal, or regulated data. By using this chatbot, you consent to such monitoring and recording.  You further acknowledge and agree that input you provide and answers you receive (collectively, “Content”) may be used by Streamlit and kapa.ai to provide, maintain, develop, and improve their respective offerings. For more information on how kapa.ai may use your Content, see https://www.kapa.ai/content/terms-of-service." data-button-hide="true" data-modal-override-open-id="kapa-ai" data-modal-lock-scroll="false" data-modal-border-radius="6px" data-modal-image-height="18px" data-answer-feedback-button-active-border="1px solid #808495" data-user-analytics-cookie-enabled="false"></script></div></main></div><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"docstrings":{},"notes":{},"versionFromSlug":null,"platformFromSlug":null,"menu":[{"menu_key":"Get-started","name":"Get started","depth":"0","children":[{"menu_key":"Installation","name":"Installation","depth":"1","children":[{"menu_key":"LOCAL-DEVELOPMENT","name":"LOCAL DEVELOPMENT","depth":"2","children":[],"category":"Get started / Installation / LOCAL DEVELOPMENT"},{"menu_key":"Use-Streamlit-Playground","name":"Use Streamlit Playground","depth":"2","children":[],"category":"Get started / Installation / Use Streamlit Playground","url":"/get-started/installation/streamlit-playground"},{"menu_key":"Install-via-command-line","name":"Install via command line","depth":"2","children":[],"category":"Get started / Installation / Install via command line","url":"/get-started/installation/command-line"},{"menu_key":"Install-via-Anaconda-Distribution","name":"Install via Anaconda Distribution","depth":"2","children":[],"category":"Get started / Installation / Install via Anaconda Distribution","url":"/get-started/installation/anaconda-distribution"},{"menu_key":"CLOUD-DEVELOPMENT","name":"CLOUD DEVELOPMENT","depth":"2","children":[],"category":"Get started / Installation / CLOUD DEVELOPMENT"},{"menu_key":"Use-GitHub-Codespaces","name":"Use GitHub Codespaces","depth":"2","children":[],"category":"Get started / Installation / Use GitHub Codespaces","url":"/get-started/installation/community-cloud"},{"menu_key":"Use-Snowflake","name":"Use Snowflake","depth":"2","children":[],"category":"Get started / Installation / Use Snowflake","url":"/get-started/installation/streamlit-in-snowflake"}],"category":"Get started / Installation","url":"/get-started/installation"},{"menu_key":"Fundamentals","name":"Fundamentals","depth":"1","children":[{"menu_key":"Basic-concepts","name":"Basic concepts","depth":"2","children":[],"category":"Get started / Fundamentals / Basic concepts","url":"/get-started/fundamentals/main-concepts"},{"menu_key":"Advanced-concepts","name":"Advanced concepts","depth":"2","children":[],"category":"Get started / Fundamentals / Advanced concepts","url":"/get-started/fundamentals/advanced-concepts"},{"menu_key":"Additional-features","name":"Additional features","depth":"2","children":[],"category":"Get started / Fundamentals / Additional features","url":"/get-started/fundamentals/additional-features"},{"menu_key":"Summary","name":"Summary","depth":"2","children":[],"category":"Get started / Fundamentals / Summary","url":"/get-started/fundamentals/summary"}],"category":"Get started / Fundamentals","url":"/get-started/fundamentals"},{"menu_key":"First-steps","name":"First steps","depth":"1","children":[{"menu_key":"Create-an-app","name":"Create an app","depth":"2","children":[],"category":"Get started / First steps / Create an app","url":"/get-started/tutorials/create-an-app"},{"menu_key":"Create-a-multipage-app","name":"Create a multipage app","depth":"2","children":[],"category":"Get started / First steps / Create a multipage app","url":"/get-started/tutorials/create-a-multipage-app"}],"category":"Get started / First steps","url":"/get-started/tutorials"}],"category":"Get started","url":"/get-started","color":"orange-70","icon":"rocket_launch"},{"menu_key":"Develop","name":"Develop","depth":"0","children":[{"menu_key":"Concepts","name":"Concepts","depth":"1","children":[{"menu_key":"CORE","name":"CORE","depth":"2","children":[],"category":"Develop / Concepts / CORE"},{"menu_key":"Architecture-and-execution","name":"Architecture and execution","depth":"2","children":[{"menu_key":"Running-your-app","name":"Running your app","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Running your app","url":"/develop/concepts/architecture/run-your-app"},{"menu_key":"Streamlit's-architecture","name":"Streamlit's architecture","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Streamlit's architecture","url":"/develop/concepts/architecture/architecture"},{"menu_key":"The-app-chrome","name":"The app chrome","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / The app chrome","url":"/develop/concepts/architecture/app-chrome"},{"menu_key":"Caching","name":"Caching","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Caching","url":"/develop/concepts/architecture/caching"},{"menu_key":"Session-State","name":"Session State","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Session State","url":"/develop/concepts/architecture/session-state"},{"menu_key":"Forms","name":"Forms","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Forms","url":"/develop/concepts/architecture/forms"},{"menu_key":"Fragments","name":"Fragments","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution / Fragments","url":"/develop/concepts/architecture/fragments"},{"menu_key":"Widget-behavior","name":"Widget behavior","depth":"3","children":[],"category":"Develop / Concepts / Architecture and execution/ Widget behavior","url":"/develop/concepts/architecture/widget-behavior"}],"category":"Develop / Concepts / Architecture and execution","url":"/develop/concepts/architecture"},{"menu_key":"Multipage-apps","name":"Multipage apps","depth":"2","children":[{"menu_key":"Overview","name":"Overview","depth":"3","children":[],"category":"Develop / Concepts / Multipage apps / Overview","url":"/develop/concepts/multipage-apps/overview"},{"menu_key":"Page-and-navigation","name":"Page and navigation","depth":"3","children":[],"category":"Develop / Concepts / Multipage apps / Page and navigation","url":"/develop/concepts/multipage-apps/page-and-navigation"},{"menu_key":"Pages-directory","name":"Pages directory","depth":"3","children":[],"category":"Develop / Concepts / Multipage apps / Pages directory","url":"/develop/concepts/multipage-apps/pages-directory"},{"menu_key":"Working-with-widgets","name":"Working with widgets","depth":"3","children":[],"category":"Develop / Concepts / Multipage apps / Working with widgets","url":"/develop/concepts/multipage-apps/widgets"}],"category":"Develop / Concepts / Multipage apps","url":"/develop/concepts/multipage-apps"},{"menu_key":"App-design","name":"App design","depth":"2","children":[{"menu_key":"Animate-and-update-elements","name":"Animate and update elements","depth":"3","children":[],"category":"Develop / Concepts / App design / Animate and update elements","url":"/develop/concepts/design/animate"},{"menu_key":"Button-behavior-and-examples","name":"Button behavior and examples","depth":"3","children":[],"category":"Develop / Concepts / App design / Button behavior and examples","url":"/develop/concepts/design/buttons"},{"menu_key":"Dataframes","name":"Dataframes","depth":"3","children":[],"category":"Develop / Concepts / App design / Dataframes","url":"/develop/concepts/design/dataframes"},{"menu_key":"Multithreading","name":"Multithreading","depth":"3","children":[],"category":"Develop / Concepts / App design / Multithreading","url":"/develop/concepts/design/multithreading"},{"menu_key":"Using-custom-classes","name":"Using custom classes","depth":"3","children":[],"category":"Develop / Concepts / App design / Using custom classes","url":"/develop/concepts/design/custom-classes"},{"menu_key":"Working-with-timezones","name":"Working with timezones","depth":"3","children":[],"category":"Develop / Concepts / App design / Working with timezones","url":"/develop/concepts/design/timezone-handling"}],"category":"Develop / Concepts / App design","url":"/develop/concepts/design"},{"menu_key":"ADDITIONAL","name":"ADDITIONAL","depth":"2","children":[],"category":"Develop / Concepts / ADDITIONAL"},{"menu_key":"Connections-secrets-and-authentication","name":"Connections, secrets, and authentication","depth":"2","children":[{"menu_key":"Connecting-to-data","name":"Connecting to data","depth":"3","children":[],"category":"Develop / Concepts / Connections, secrets, and authentication / Connecting to data","url":"/develop/concepts/connections/connecting-to-data"},{"menu_key":"Secrets-management","name":"Secrets management","depth":"3","children":[],"category":"Develop / Concepts / Connections, secrets, and authentication / Secrets management","url":"/develop/concepts/connections/secrets-management"},{"menu_key":"User-authentication","name":"User authentication","depth":"3","children":[],"category":"Develop / Concepts / Connections, secrets, and authentication / User authentication","url":"/develop/concepts/connections/authentication"},{"menu_key":"Security-reminders","name":"Security reminders","depth":"3","children":[],"category":"Develop / Concepts / Connections, secrets, and authentication / Security reminders","url":"/develop/concepts/connections/security-reminders"}],"category":"Develop / Concepts / Connections, secrets, and authentication","url":"/develop/concepts/connections"},{"menu_key":"Custom-components","name":"Custom components","depth":"2","children":[{"menu_key":"Intro-to-custom-components","name":"Intro to custom components","depth":"3","children":[],"category":"Develop / Concepts / Custom components / Intro to custom components","url":"/develop/concepts/custom-components/intro"},{"menu_key":"Create-a-Component","name":"Create a Component","depth":"3","children":[],"category":"Develop / Concepts / Custom components / Create a Component","url":"/develop/concepts/custom-components/create"},{"menu_key":"Publish-a-Component","name":"Publish a Component","depth":"3","children":[],"category":"Develop / Concepts / Custom components / Publish a Component","url":"/develop/concepts/custom-components/publish"},{"menu_key":"Limitations","name":"Limitations","depth":"3","children":[],"category":"Develop / Concepts / Custom components / Limitations","url":"/develop/concepts/custom-components/limitations"},{"menu_key":"Component-gallery","name":"Component gallery","depth":"3","children":[],"category":"Develop / Concepts / Custom components / Component gallery","url":"https://streamlit.io/components"}],"category":"Develop / Concepts / Custom components","url":"/develop/concepts/custom-components"},{"menu_key":"Configuration-and-theming","name":"Configuration and theming","depth":"2","children":[{"menu_key":"Configuration-options","name":"Configuration options","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / Configuration options","url":"/develop/concepts/configuration/options"},{"menu_key":"HTTPS-support","name":"HTTPS support","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / HTTPS support","url":"/develop/concepts/configuration/https-support"},{"menu_key":"Serving-static-files","name":"Serving static files","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / Serving static files","url":"/develop/concepts/configuration/serving-static-files"},{"menu_key":"THEMING","name":"THEMING","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / THEMING"},{"menu_key":"Customize-your-theme","name":"Customize your theme","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / Customize your theme","url":"/develop/concepts/configuration/theming"},{"menu_key":"Customize-colors-and-borders","name":"Customize colors and borders","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / Customize colors and borders","url":"/develop/concepts/configuration/theming-customize-colors-and-borders"},{"menu_key":"Customize-fonts","name":"Customize fonts","depth":"3","children":[],"category":"Develop / Concepts / Configuration and theming / Customize fonts","url":"/develop/concepts/configuration/theming-customize-fonts"}],"category":"Develop / Concepts / Configuration and theming","url":"/develop/concepts/configuration"},{"menu_key":"App-testing","name":"App testing","depth":"2","children":[{"menu_key":"Get-started","name":"Get started","depth":"3","children":[],"category":"Develop / Concepts / App testing / Get started","url":"/develop/concepts/app-testing/get-started"},{"menu_key":"Beyond-the-basics","name":"Beyond the basics","depth":"3","children":[],"category":"Develop / Concepts / App testing / Beyond the basics","url":"/develop/concepts/app-testing/beyond-the-basics"},{"menu_key":"Automate-your-tests","name":"Automate your tests","depth":"3","children":[],"category":"Develop / Concepts / App testing / Automate your tests","url":"/develop/concepts/app-testing/automate-tests"},{"menu_key":"Example","name":"Example","depth":"3","children":[],"category":"Develop / Concepts / App testing / Example","url":"/develop/concepts/app-testing/examples"},{"menu_key":"Cheat-sheet","name":"Cheat sheet","depth":"3","children":[],"category":"Develop / Concepts / App testing / Cheat sheet","url":"/develop/concepts/app-testing/cheat-sheet"}],"category":"Develop / Concepts / App testing","url":"/develop/concepts/app-testing"}],"category":"Develop / Concepts","url":"/develop/concepts"},{"menu_key":"API-reference","name":"API reference","depth":"1","children":[{"menu_key":"PAGE-ELEMENTS","name":"PAGE ELEMENTS","depth":"2","children":[],"category":"Develop / API reference / PAGE ELEMENTS"},{"menu_key":"Write-and-magic","name":"Write and magic","depth":"2","children":[{"menu_key":"st.write","name":"st.write","depth":"3","children":[],"category":"Develop / API reference / Write and magic / st.write","url":"/develop/api-reference/write-magic/st.write","isVersioned":true},{"menu_key":"st.write_stream","name":"st.write_stream","depth":"3","children":[],"category":"Develop / API reference / Write and magic / st.write_stream","url":"/develop/api-reference/write-magic/st.write_stream","isVersioned":true},{"menu_key":"magic","name":"magic","depth":"3","children":[],"category":"Develop / API reference / Write and magic / magic","url":"/develop/api-reference/write-magic/magic"}],"category":"Develop / API reference / Write and magic","url":"/develop/api-reference/write-magic"},{"menu_key":"Text-elements","name":"Text elements","depth":"2","children":[{"menu_key":"HEADINGS-AND-BODY","name":"HEADINGS AND BODY","depth":"3","children":[],"category":"Develop / API reference / Text elements / HEADINGS AND BODY"},{"menu_key":"st.title","name":"st.title","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.title","url":"/develop/api-reference/text/st.title","isVersioned":true},{"menu_key":"st.header","name":"st.header","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.header","url":"/develop/api-reference/text/st.header","isVersioned":true},{"menu_key":"st.subheader","name":"st.subheader","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.subheader","url":"/develop/api-reference/text/st.subheader","isVersioned":true},{"menu_key":"st.markdown","name":"st.markdown","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.markdown","url":"/develop/api-reference/text/st.markdown","isVersioned":true},{"menu_key":"FORMATTED-TEXT","name":"FORMATTED TEXT","depth":"3","children":[],"category":"Develop / API reference / Text elements / FORMATTED TEXT"},{"menu_key":"st.badge","name":"st.badge","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.badge","url":"/develop/api-reference/text/st.badge","isVersioned":true},{"menu_key":"st.caption","name":"st.caption","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.caption","url":"/develop/api-reference/text/st.caption","isVersioned":true},{"menu_key":"st.code","name":"st.code","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.code","url":"/develop/api-reference/text/st.code","isVersioned":true},{"menu_key":"st.divider","name":"st.divider","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.divider","url":"/develop/api-reference/text/st.divider","isVersioned":true},{"menu_key":"st.echo","name":"st.echo","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.echo","url":"/develop/api-reference/text/st.echo","isVersioned":true},{"menu_key":"st.latex","name":"st.latex","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.latex","url":"/develop/api-reference/text/st.latex","isVersioned":true},{"menu_key":"st.text","name":"st.text","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.text","url":"/develop/api-reference/text/st.text","isVersioned":true},{"menu_key":"UTILITIES","name":"UTILITIES","depth":"3","children":[],"category":"Develop / API reference / Text elements / UTILITIES"},{"menu_key":"st.help","name":"st.help","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.help","url":"/develop/api-reference/text/st.help","isVersioned":true},{"menu_key":"st.html","name":"st.html","depth":"3","children":[],"category":"Develop / API reference / Text elements / st.html","url":"/develop/api-reference/text/st.html","isVersioned":true}],"category":"Develop / API reference / Text elements","url":"/develop/api-reference/text"},{"menu_key":"Data-elements","name":"Data elements","depth":"2","children":[{"menu_key":"st.dataframe","name":"st.dataframe","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.dataframe","url":"/develop/api-reference/data/st.dataframe","isVersioned":true},{"menu_key":"st.data_editor","name":"st.data_editor","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.data_editor","url":"/develop/api-reference/data/st.data_editor","isVersioned":true},{"menu_key":"st.column_config","name":"st.column_config","depth":"3","children":[{"menu_key":"Column","name":"Column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Column","url":"/develop/api-reference/data/st.column_config/st.column_config.column","isVersioned":true},{"menu_key":"Text-column","name":"Text column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Text column","url":"/develop/api-reference/data/st.column_config/st.column_config.textcolumn","isVersioned":true},{"menu_key":"Number-column","name":"Number column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Number column","url":"/develop/api-reference/data/st.column_config/st.column_config.numbercolumn","isVersioned":true},{"menu_key":"Checkbox-column","name":"Checkbox column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Checkbox column","url":"/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn","isVersioned":true},{"menu_key":"Selectbox-column","name":"Selectbox column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Selectbox column","url":"/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn","isVersioned":true},{"menu_key":"Multiselect-column","name":"Multiselect column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Multiselect column","url":"/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn","isVersioned":true},{"menu_key":"Datetime-column","name":"Datetime column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Datetime column","url":"/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn","isVersioned":true},{"menu_key":"Date-column","name":"Date column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Date column","url":"/develop/api-reference/data/st.column_config/st.column_config.datecolumn","isVersioned":true},{"menu_key":"Time-column","name":"Time column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Time column","url":"/develop/api-reference/data/st.column_config/st.column_config.timecolumn","isVersioned":true},{"menu_key":"JSON-column","name":"JSON column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / JSON column","url":"/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn","isVersioned":true},{"menu_key":"List-column","name":"List column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / List column","url":"/develop/api-reference/data/st.column_config/st.column_config.listcolumn","isVersioned":true},{"menu_key":"Link-column","name":"Link column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Link column","url":"/develop/api-reference/data/st.column_config/st.column_config.linkcolumn","isVersioned":true},{"menu_key":"Image-column","name":"Image column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Image column","url":"/develop/api-reference/data/st.column_config/st.column_config.imagecolumn","isVersioned":true},{"menu_key":"Area-chart-column","name":"Area chart column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Area chart column","url":"/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn","isVersioned":true},{"menu_key":"Line-chart-column","name":"Line chart column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Line chart column","url":"/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn","isVersioned":true},{"menu_key":"Bar-chart-column","name":"Bar chart column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Bar chart column","url":"/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn","isVersioned":true},{"menu_key":"Progress-column","name":"Progress column","depth":"4","children":[],"category":"Develop / API reference / Data elements / st.column_config / Progress column","url":"/develop/api-reference/data/st.column_config/st.column_config.progresscolumn","isVersioned":true}],"category":"Develop / API reference / Data elements / st.column_config","url":"/develop/api-reference/data/st.column_config"},{"menu_key":"st.table","name":"st.table","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.table","url":"/develop/api-reference/data/st.table","isVersioned":true},{"menu_key":"st.metric","name":"st.metric","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.metric","url":"/develop/api-reference/data/st.metric","isVersioned":true},{"menu_key":"st.json","name":"st.json","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.json","url":"/develop/api-reference/data/st.json","isVersioned":true},{"menu_key":"st.experimental_data_editor","name":"st.experimental_data_editor","depth":"3","children":[],"category":"Develop / API reference / Data elements / st.experimental_data_editor","url":"/develop/api-reference/data/st.experimental_data_editor","isVersioned":true,"isDeprecated":true,"visible":false}],"category":"Develop / API reference / Data elements","url":"/develop/api-reference/data"},{"menu_key":"Chart-elements","name":"Chart elements","depth":"2","children":[{"menu_key":"SIMPLE","name":"SIMPLE","depth":"3","children":[],"category":"Develop / API reference / Chart elements / SIMPLE"},{"menu_key":"st.area_chart","name":"st.area_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.area_chart","url":"/develop/api-reference/charts/st.area_chart","isVersioned":true},{"menu_key":"st.bar_chart","name":"st.bar_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.bar_chart","url":"/develop/api-reference/charts/st.bar_chart","isVersioned":true},{"menu_key":"st.line_chart","name":"st.line_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.line_chart","url":"/develop/api-reference/charts/st.line_chart","isVersioned":true},{"menu_key":"st.map","name":"st.map","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.map","url":"/develop/api-reference/charts/st.map","isVersioned":true},{"menu_key":"st.scatter_chart","name":"st.scatter_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.scatter_chart","url":"/develop/api-reference/charts/st.scatter_chart","isVersioned":true},{"menu_key":"ADVANCED","name":"ADVANCED","depth":"3","children":[],"category":"Develop / API reference / Chart elements / ADVANCED"},{"menu_key":"st.altair_chart","name":"st.altair_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.altair_chart","url":"/develop/api-reference/charts/st.altair_chart","isVersioned":true},{"menu_key":"st.bokeh_chart","name":"st.bokeh_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.bokeh_chart","url":"/develop/api-reference/charts/st.bokeh_chart","isVersioned":true,"isDeprecated":true},{"menu_key":"st.graphviz_chart","name":"st.graphviz_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.graphviz_chart","url":"/develop/api-reference/charts/st.graphviz_chart","isVersioned":true},{"menu_key":"st.plotly_chart","name":"st.plotly_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.plotly_chart","url":"/develop/api-reference/charts/st.plotly_chart","isVersioned":true},{"menu_key":"st.pydeck_chart","name":"st.pydeck_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.pydeck_chart","url":"/develop/api-reference/charts/st.pydeck_chart","isVersioned":true},{"menu_key":"st.pyplot","name":"st.pyplot","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.pyplot","url":"/develop/api-reference/charts/st.pyplot","isVersioned":true},{"menu_key":"st.vega_lite_chart","name":"st.vega_lite_chart","depth":"3","children":[],"category":"Develop / API reference / Chart elements / st.vega_lite_chart","url":"/develop/api-reference/charts/st.vega_lite_chart","isVersioned":true}],"category":"Develop / API reference / Chart elements","url":"/develop/api-reference/charts"},{"menu_key":"Input-widgets","name":"Input widgets","depth":"2","children":[{"menu_key":"BUTTONS","name":"BUTTONS","depth":"3","children":[],"category":"Develop / API reference / Input widgets / BUTTONS"},{"menu_key":"st.button","name":"st.button","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.button","url":"/develop/api-reference/widgets/st.button","isVersioned":true},{"menu_key":"st.download_button","name":"st.download_button","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.download_button","url":"/develop/api-reference/widgets/st.download_button","isVersioned":true},{"menu_key":"st.form_submit_button","name":"st.form_submit_button","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.form_submit_button","url":"https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button","isVersioned":true},{"menu_key":"st.link_button","name":"st.link_button","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.link_button","url":"/develop/api-reference/widgets/st.link_button","isVersioned":true},{"menu_key":"st.page_link","name":"st.page_link","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.page_link","url":"/develop/api-reference/widgets/st.page_link","isVersioned":true},{"menu_key":"SELECTIONS","name":"SELECTIONS","depth":"3","children":[],"category":"Develop / API reference / Input widgets / SELECTIONS"},{"menu_key":"st.checkbox","name":"st.checkbox","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.checkbox","url":"/develop/api-reference/widgets/st.checkbox","isVersioned":true},{"menu_key":"st.color_picker","name":"st.color_picker","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.color_picker","url":"/develop/api-reference/widgets/st.color_picker","isVersioned":true},{"menu_key":"st.feedback","name":"st.feedback","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.feedback","url":"/develop/api-reference/widgets/st.feedback","isVersioned":true},{"menu_key":"st.multiselect","name":"st.multiselect","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.multiselect","url":"/develop/api-reference/widgets/st.multiselect","isVersioned":true},{"menu_key":"st.pills","name":"st.pills","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.pills","url":"/develop/api-reference/widgets/st.pills","isVersioned":true},{"menu_key":"st.radio","name":"st.radio","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.radio","url":"/develop/api-reference/widgets/st.radio","isVersioned":true},{"menu_key":"st.segmented_control","name":"st.segmented_control","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.segmented_control","url":"/develop/api-reference/widgets/st.segmented_control","isVersioned":true},{"menu_key":"st.selectbox","name":"st.selectbox","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.selectbox","url":"/develop/api-reference/widgets/st.selectbox","isVersioned":true},{"menu_key":"st.select_slider","name":"st.select_slider","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.select_slider","url":"/develop/api-reference/widgets/st.select_slider","isVersioned":true},{"menu_key":"st.toggle","name":"st.toggle","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.toggle","url":"/develop/api-reference/widgets/st.toggle","isVersioned":true},{"menu_key":"NUMERIC","name":"NUMERIC","depth":"3","children":[],"category":"Develop / API reference / Input widgets / NUMERIC"},{"menu_key":"st.number_input","name":"st.number_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.number_input","url":"/develop/api-reference/widgets/st.number_input","isVersioned":true},{"menu_key":"st.slider","name":"st.slider","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.slider","url":"/develop/api-reference/widgets/st.slider","isVersioned":true},{"menu_key":"DATE-AND-TIME","name":"DATE AND TIME","depth":"3","children":[],"category":"Develop / API reference / Input widgets / DATE AND TIME"},{"menu_key":"st.date_input","name":"st.date_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.date_input","url":"/develop/api-reference/widgets/st.date_input","isVersioned":true},{"menu_key":"st.datetime_input","name":"st.datetime_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.datetime_input","url":"/develop/api-reference/widgets/st.datetime_input","isVersioned":true},{"menu_key":"st.time_input","name":"st.time_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.time_input","url":"/develop/api-reference/widgets/st.time_input","isVersioned":true},{"menu_key":"TEXT","name":"TEXT","depth":"3","children":[],"category":"Develop / API reference / Input widgets / TEXT"},{"menu_key":"st.chat_input","name":"st.chat_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.chat_input","url":"https://docs.streamlit.io/develop/api-reference/chat/st.chat_input","isVersioned":true},{"menu_key":"st.text_area","name":"st.text_area","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.text_area","url":"/develop/api-reference/widgets/st.text_area","isVersioned":true},{"menu_key":"st.text_input","name":"st.text_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.text_input","url":"/develop/api-reference/widgets/st.text_input","isVersioned":true},{"menu_key":"MEDIA-AND-FILES","name":"MEDIA AND FILES","depth":"3","children":[],"category":"Develop / API reference / Input widgets / MEDIA AND FILES"},{"menu_key":"st.audio_input","name":"st.audio_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.audio_input","url":"/develop/api-reference/widgets/st.audio_input","isVersioned":true},{"menu_key":"st.camera_input","name":"st.camera_input","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.camera_input","url":"/develop/api-reference/widgets/st.camera_input","isVersioned":true},{"menu_key":"st.data_editor","name":"st.data_editor","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.data_editor","url":"https://docs.streamlit.io/develop/api-reference/data/st.data_editor","isVersioned":true},{"menu_key":"st.file_uploader","name":"st.file_uploader","depth":"3","children":[],"category":"Develop / API reference / Input widgets / st.file_uploader","url":"/develop/api-reference/widgets/st.file_uploader","isVersioned":true}],"category":"Develop / API reference / Input widgets","url":"/develop/api-reference/widgets"},{"menu_key":"Media-elements","name":"Media elements","depth":"2","children":[{"menu_key":"st.audio","name":"st.audio","depth":"3","children":[],"category":"Develop / API reference / Media elements / st.audio","url":"/develop/api-reference/media/st.audio","isVersioned":true},{"menu_key":"st.image","name":"st.image","depth":"3","children":[],"category":"Develop / API reference / Media elements / st.image","url":"/develop/api-reference/media/st.image","isVersioned":true},{"menu_key":"st.logo","name":"st.logo","depth":"3","children":[],"category":"Develop / API reference / Media elements / st.logo","url":"/develop/api-reference/media/st.logo","isVersioned":true},{"menu_key":"st.pdf","name":"st.pdf","depth":"3","children":[],"category":"Develop / API reference / Media elements / st.pdf","url":"/develop/api-reference/media/st.pdf","isVersioned":true},{"menu_key":"st.video","name":"st.video","depth":"3","children":[],"category":"Develop / API reference / Media elements / st.video","url":"/develop/api-reference/media/st.video","isVersioned":true}],"category":"Develop / API reference / Media elements","url":"/develop/api-reference/media"},{"menu_key":"Layouts-and-containers","name":"Layouts and containers","depth":"2","children":[{"menu_key":"st.columns","name":"st.columns","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.columns","url":"/develop/api-reference/layout/st.columns","isVersioned":true},{"menu_key":"st.container","name":"st.container","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.container","url":"/develop/api-reference/layout/st.container","isVersioned":true},{"menu_key":"st.dialog","name":"st.dialog","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.dialog","url":"https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog","isVersioned":true},{"menu_key":"st.empty","name":"st.empty","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.empty","url":"/develop/api-reference/layout/st.empty","isVersioned":true},{"menu_key":"st.expander","name":"st.expander","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.expander","url":"/develop/api-reference/layout/st.expander","isVersioned":true},{"menu_key":"st.form","name":"st.form","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.form","url":"https://docs.streamlit.io/develop/api-reference/execution-flow/st.form","isVersioned":true},{"menu_key":"st.popover","name":"st.popover","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.popover","url":"/develop/api-reference/layout/st.popover","isVersioned":true},{"menu_key":"st.sidebar","name":"st.sidebar","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.sidebar","url":"/develop/api-reference/layout/st.sidebar","isVersioned":true},{"menu_key":"st.space","name":"st.space","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.space","url":"/develop/api-reference/layout/st.space","isVersioned":true},{"menu_key":"st.tabs","name":"st.tabs","depth":"3","children":[],"category":"Develop / API reference / Layouts and containers / st.tabs","url":"/develop/api-reference/layout/st.tabs","isVersioned":true}],"category":"Develop / API reference / Layouts and containers","url":"/develop/api-reference/layout"},{"menu_key":"Chat-elements","name":"Chat elements","depth":"2","children":[{"menu_key":"st.chat_input","name":"st.chat_input","depth":"3","children":[],"category":"Develop / API reference / Chat elements / st.chat_input","url":"/develop/api-reference/chat/st.chat_input","isVersioned":true},{"menu_key":"st.chat_message","name":"st.chat_message","depth":"3","children":[],"category":"Develop / API reference / Chat elements / st.chat_message","url":"/develop/api-reference/chat/st.chat_message","isVersioned":true},{"menu_key":"st.status","name":"st.status","depth":"3","children":[],"category":"Develop / API reference / Chat elements / st.status","url":"https://docs.streamlit.io/develop/api-reference/status/st.status","isVersioned":true},{"menu_key":"st.write_stream","name":"st.write_stream","depth":"3","children":[],"category":"Develop / API reference / Chat elements / st.write_stream","url":"https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream","isVersioned":true}],"category":"Develop / API reference / Chat elements","url":"/develop/api-reference/chat"},{"menu_key":"Status-elements","name":"Status elements","depth":"2","children":[{"menu_key":"CALLOUTS","name":"CALLOUTS","depth":"3","children":[],"category":"Develop / API reference / Status elements / CALLOUTS"},{"menu_key":"st.success","name":"st.success","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.success","url":"/develop/api-reference/status/st.success","isVersioned":true},{"menu_key":"st.info","name":"st.info","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.info","url":"/develop/api-reference/status/st.info","isVersioned":true},{"menu_key":"st.warning","name":"st.warning","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.warning","url":"/develop/api-reference/status/st.warning","isVersioned":true},{"menu_key":"st.error","name":"st.error","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.error","url":"/develop/api-reference/status/st.error","isVersioned":true},{"menu_key":"st.exception","name":"st.exception","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.exception","url":"/develop/api-reference/status/st.exception","isVersioned":true},{"menu_key":"OTHER","name":"OTHER","depth":"3","children":[],"category":"Develop / API reference / Status elements / OTHER"},{"menu_key":"st.progress","name":"st.progress","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.progress","url":"/develop/api-reference/status/st.progress","isVersioned":true},{"menu_key":"st.spinner","name":"st.spinner","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.spinner","url":"/develop/api-reference/status/st.spinner","isVersioned":true},{"menu_key":"st.status","name":"st.status","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.status","url":"/develop/api-reference/status/st.status","isVersioned":true},{"menu_key":"st.toast","name":"st.toast","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.toast","url":"/develop/api-reference/status/st.toast","isVersioned":true},{"menu_key":"st.balloons","name":"st.balloons","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.balloons","url":"/develop/api-reference/status/st.balloons","isVersioned":true},{"menu_key":"st.snow","name":"st.snow","depth":"3","children":[],"category":"Develop / API reference / Status elements / st.snow","url":"/develop/api-reference/status/st.snow","isVersioned":true}],"category":"Develop / API reference / Status elements","url":"/develop/api-reference/status"},{"menu_key":"Third-party-components","name":"Third-party components","depth":"2","children":[],"category":"Develop / API reference / Third-party components","url":"https://streamlit.io/components"},{"menu_key":"APPLICATION-LOGIC","name":"APPLICATION LOGIC","depth":"2","children":[],"category":"Develop / API reference / APPLICATION LOGIC"},{"menu_key":"Authentication-and-user-info","name":"Authentication and user info","depth":"2","children":[{"menu_key":"st.login","name":"st.login","depth":"3","children":[],"category":"Develop / API reference / Authentication and user info / st.login","url":"/develop/api-reference/user/st.login","isVersioned":true},{"menu_key":"st.logout","name":"st.logout","depth":"3","children":[],"category":"Develop / API reference / Authentication and user info / st.logout","url":"/develop/api-reference/user/st.logout","isVersioned":true},{"menu_key":"st.user","name":"st.user","depth":"3","children":[],"category":"Develop / API reference / Authentication and user info / st.user","url":"/develop/api-reference/user/st.user","isVersioned":true}],"category":"Develop / API reference / Authentication and user info","url":"/develop/api-reference/user"},{"menu_key":"Navigation-and-pages","name":"Navigation and pages","depth":"2","children":[{"menu_key":"st.navigation","name":"st.navigation","depth":"3","children":[],"category":"Develop / API reference / Navigation and pages / st.navigation","url":"/develop/api-reference/navigation/st.navigation","isVersioned":true},{"menu_key":"st.Page","name":"st.Page","depth":"3","children":[],"category":"Develop / API reference / Navigation and pages / st.Page","url":"/develop/api-reference/navigation/st.page","isVersioned":true},{"menu_key":"st.page_link","name":"st.page_link","depth":"3","children":[],"category":"Develop / API reference / Navigation and pages / st.page_link","url":"https://docs.streamlit.io/develop/api-reference/widgets/st.page_link","isVersioned":true},{"menu_key":"st.switch_page","name":"st.switch_page","depth":"3","children":[],"category":"Develop / API reference / Navigation and pages / st.switch_page","url":"/develop/api-reference/navigation/st.switch_page","isVersioned":true}],"category":"Develop / API reference / Navigation and pages","url":"/develop/api-reference/navigation"},{"menu_key":"Execution-flow","name":"Execution flow","depth":"2","children":[{"menu_key":"st.dialog","name":"st.dialog","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.dialog","url":"/develop/api-reference/execution-flow/st.dialog","isVersioned":true},{"menu_key":"st.form","name":"st.form","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.form","url":"/develop/api-reference/execution-flow/st.form","isVersioned":true},{"menu_key":"st.form_submit_button","name":"st.form_submit_button","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.form_submit_button","url":"/develop/api-reference/execution-flow/st.form_submit_button","isVersioned":true},{"menu_key":"st.fragment","name":"st.fragment","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.fragment","url":"/develop/api-reference/execution-flow/st.fragment","isVersioned":true},{"menu_key":"st.rerun","name":"st.rerun","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.rerun","url":"/develop/api-reference/execution-flow/st.rerun","isVersioned":true},{"menu_key":"st.stop","name":"st.stop","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.stop","url":"/develop/api-reference/execution-flow/st.stop","isVersioned":true},{"menu_key":"st.experimental_rerun","name":"st.experimental_rerun","depth":"3","children":[],"category":"Develop / API reference / Execution flow / st.experimental_rerun","url":"/develop/api-reference/execution-flow/st.experimental_rerun","isVersioned":true,"isDeprecated":true,"visible":false}],"category":"Develop / API reference / Execution flow","url":"/develop/api-reference/execution-flow"},{"menu_key":"Caching-and-state","name":"Caching and state","depth":"2","children":[{"menu_key":"SERVER","name":"SERVER","depth":"3","children":[],"category":"Develop / API reference / Caching and state / SERVER"},{"menu_key":"st.cache_data","name":"st.cache_data","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.cache_data","url":"/develop/api-reference/caching-and-state/st.cache_data","isVersioned":true},{"menu_key":"st.cache_resource","name":"st.cache_resource","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.cache_resource","url":"/develop/api-reference/caching-and-state/st.cache_resource","isVersioned":true},{"menu_key":"st.experimental_memo","name":"st.experimental_memo","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.experimental_memo","url":"/develop/api-reference/caching-and-state/st.experimental_memo","isVersioned":true,"isDeprecated":true,"visible":false},{"menu_key":"st.experimental_singleton","name":"st.experimental_singleton","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.experimental_singleton","url":"/develop/api-reference/caching-and-state/st.experimental_singleton","isVersioned":true,"isDeprecated":true,"visible":false},{"menu_key":"st.session_state","name":"st.session_state","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.session_state","url":"/develop/api-reference/caching-and-state/st.session_state"},{"menu_key":"BROWSER","name":"BROWSER","depth":"3","children":[],"category":"Develop / API reference / Caching and state / BROWSER"},{"menu_key":"st.context","name":"st.context","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.context","url":"/develop/api-reference/caching-and-state/st.context","isVersioned":true},{"menu_key":"st.query_params","name":"st.query_params","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.query_params","url":"/develop/api-reference/caching-and-state/st.query_params","isVersioned":true},{"menu_key":"st.experimental_get_query_params","name":"st.experimental_get_query_params","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.experimental_get_query_params","url":"/develop/api-reference/caching-and-state/st.experimental_get_query_params","isVersioned":true,"isDeprecated":true},{"menu_key":"st.experimental_set_query_params","name":"st.experimental_set_query_params","depth":"3","children":[],"category":"Develop / API reference / Caching and state / st.experimental_set_query_params","url":"/develop/api-reference/caching-and-state/st.experimental_set_query_params","isVersioned":true,"isDeprecated":true}],"category":"Develop / API reference / Caching and state","url":"/develop/api-reference/caching-and-state"},{"menu_key":"Connections-and-secrets","name":"Connections and secrets","depth":"2","children":[{"menu_key":"SECRETS","name":"SECRETS","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / SECRETS"},{"menu_key":"st.secrets","name":"st.secrets","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / st.secrets","url":"/develop/api-reference/connections/st.secrets"},{"menu_key":"secrets.toml","name":"secrets.toml","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / secrets.toml","url":"/develop/api-reference/connections/secrets.toml"},{"menu_key":"CONNECTIONS","name":"CONNECTIONS","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / CONNECTIONS"},{"menu_key":"st.connection","name":"st.connection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / st.connection","url":"/develop/api-reference/connections/st.connection","isVersioned":true},{"menu_key":"SnowflakeConnection","name":"SnowflakeConnection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / SnowflakeConnection","url":"/develop/api-reference/connections/st.connections.snowflakeconnection","isVersioned":true},{"menu_key":"SQLConnection","name":"SQLConnection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / SQLConnection","url":"/develop/api-reference/connections/st.connections.sqlconnection","isVersioned":true},{"menu_key":"BaseConnection","name":"BaseConnection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / BaseConnection","url":"/develop/api-reference/connections/st.connections.baseconnection","isVersioned":true},{"menu_key":"st.experimental_connection","name":"st.experimental_connection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / st.experimental_connection","url":"/develop/api-reference/connections/st.experimental_connection","isVersioned":true,"isDeprecated":true,"visible":false},{"menu_key":"SnowparkConnection","name":"SnowparkConnection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / SnowparkConnection","url":"/develop/api-reference/connections/st.connections.snowparkconnection","isVersioned":true,"isDeprecated":true},{"menu_key":"ExperimentalBaseConnection","name":"ExperimentalBaseConnection","depth":"3","children":[],"category":"Develop / API reference / Connections and secrets / ExperimentalBaseConnection","url":"/develop/api-reference/connections/st.connections.experimentalbaseconnection","isVersioned":true,"isDeprecated":true,"visible":false}],"category":"Develop / API reference / Connections and secrets","url":"/develop/api-reference/connections"},{"menu_key":"Custom-components","name":"Custom components","depth":"2","children":[{"menu_key":"V2-BACKEND-(PYTHON)","name":"V2 BACKEND (PYTHON)","depth":"3","children":[],"category":"Develop / API reference / Custom components / V2 BACKEND (PYTHON)"},{"menu_key":"BidiComponentCallable","name":"BidiComponentCallable","depth":"3","children":[],"category":"Develop / API reference / Custom components / BidiComponentCallable","url":"/develop/api-reference/custom-components/st.components.v2.types.bidicomponentcallable","isVersioned":true},{"menu_key":"component","name":"component","depth":"3","children":[],"category":"Develop / API reference / Custom components / component","url":"/develop/api-reference/custom-components/st.components.v2.component","isVersioned":true},{"menu_key":"V2-FRONTEND-(TYPESCRIPT)","name":"V2 FRONTEND (TYPESCRIPT)","depth":"3","children":[],"category":"Develop / API reference / Custom components / V2 FRONTEND (TYPESCRIPT)"},{"menu_key":"component-v2-lib","name":"component-v2-lib","depth":"3","children":[],"category":"Develop / API reference / Custom components / component-v2-lib","url":"/develop/api-reference/custom-components/component-v2-lib"},{"menu_key":"Component","name":"Component","depth":"3","children":[],"category":"Develop / API reference / Custom components / Component","url":"/develop/api-reference/custom-components/component-v2-lib-component","isVersioned":true},{"menu_key":"ComponentArgs","name":"ComponentArgs","depth":"3","children":[],"category":"Develop / API reference / Custom components / ComponentArgs","url":"/develop/api-reference/custom-components/component-v2-lib-componentargs","isVersioned":true},{"menu_key":"ComponentState","name":"ComponentState","depth":"3","children":[],"category":"Develop / API reference / Custom components / ComponentState","url":"/develop/api-reference/custom-components/component-v2-lib-componentstate","isVersioned":true},{"menu_key":"OptionalComponentCleanupFunction","name":"OptionalComponentCleanupFunction","depth":"3","children":[],"category":"Develop / API reference / Custom components / OptionalComponentCleanupFunction","url":"/develop/api-reference/custom-components/component-v2-lib-optionalcomponentcleanupfunction","isVersioned":true},{"menu_key":"V1-COMPONENTS","name":"V1 COMPONENTS","depth":"3","children":[],"category":"Develop / API reference / Custom components / V1 COMPONENTS"},{"menu_key":"declare_component","name":"declare_component","depth":"3","children":[],"category":"Develop / API reference / Custom components / declare_component","url":"/develop/api-reference/custom-components/st.components.v1.declare_component","isVersioned":true},{"menu_key":"html","name":"html","depth":"3","children":[],"category":"Develop / API reference / Custom components / html","url":"/develop/api-reference/custom-components/st.components.v1.html","isVersioned":true},{"menu_key":"iframe","name":"iframe","depth":"3","children":[],"category":"Develop / API reference / Custom components / iframe","url":"/develop/api-reference/custom-components/st.components.v1.iframe","isVersioned":true}],"category":"Develop / API reference / Custom components","url":"/develop/api-reference/custom-components"},{"menu_key":"Configuration","name":"Configuration","depth":"2","children":[{"menu_key":"config.toml","name":"config.toml","depth":"3","children":[],"category":"Develop / API reference / Configuration / config.toml","url":"/develop/api-reference/configuration/config.toml"},{"menu_key":"st.get_option","name":"st.get_option","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.get_option","url":"/develop/api-reference/configuration/st.get_option","isVersioned":true},{"menu_key":"st.set_option","name":"st.set_option","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.set_option","url":"/develop/api-reference/configuration/st.set_option","isVersioned":true},{"menu_key":"st.set_page_config","name":"st.set_page_config","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.set_page_config","url":"/develop/api-reference/configuration/st.set_page_config","isVersioned":true}],"category":"Develop / API reference / Configuration","url":"/develop/api-reference/configuration","isVersioned":false},{"menu_key":"TOOLS","name":"TOOLS","depth":"2","children":[],"category":"Develop / API reference / TOOLS"},{"menu_key":"App-testing","name":"App testing","depth":"2","children":[{"menu_key":"AppTest","name":"AppTest","depth":"3","children":[],"category":"Develop / API reference / App testing / AppTest","url":"/develop/api-reference/app-testing/st.testing.v1.apptest","isVersioned":true},{"menu_key":"element_tree","name":"element_tree","depth":"3","children":[],"category":"Develop / API reference / App testing / element_tree","url":"/develop/api-reference/app-testing/testing-element-classes","isVersioned":true}],"category":"Develop / API reference / App testing","url":"/develop/api-reference/app-testing"},{"menu_key":"Command-line","name":"Command line","depth":"2","children":[{"menu_key":"streamlit-cache","name":"streamlit cache","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit cache","url":"/develop/api-reference/cli/cache"},{"menu_key":"streamlit-config","name":"streamlit config","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit config","url":"/develop/api-reference/cli/config"},{"menu_key":"streamlit-docs","name":"streamlit docs","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit docs","url":"/develop/api-reference/cli/docs"},{"menu_key":"streamlit-hello","name":"streamlit hello","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit hello","url":"/develop/api-reference/cli/hello"},{"menu_key":"streamlit-help","name":"streamlit help","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit help","url":"/develop/api-reference/cli/help"},{"menu_key":"streamlit-init","name":"streamlit init","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit init","url":"/develop/api-reference/cli/init"},{"menu_key":"streamlit-run","name":"streamlit run","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit run","url":"/develop/api-reference/cli/run"},{"menu_key":"streamlit-version","name":"streamlit version","depth":"3","children":[],"category":"Develop / API reference / Command line / streamlit version","url":"/develop/api-reference/cli/version"}],"category":"Develop / API reference / Command line","url":"/develop/api-reference/cli"}],"category":"Develop / API reference","url":"/develop/api-reference"},{"menu_key":"Tutorials","name":"Tutorials","depth":"1","children":[{"menu_key":"Authentication-and-personalization","name":"Authentication and personalization","depth":"2","children":[{"menu_key":"Google-Auth-Platform","name":"Google Auth Platform","depth":"3","children":[],"category":"Develop / Tutorials / Authentication and personalization / Google Auth Platform","url":"/develop/tutorials/authentication/google"},{"menu_key":"Microsoft-Entra","name":"Microsoft Entra","depth":"3","children":[],"category":"Develop / Tutorials / Authentication and personalization / Microsoft Entra","url":"/develop/tutorials/authentication/microsoft"}],"category":"Develop / Tutorials / Authentication and personalization","url":"/develop/tutorials/authentication"},{"menu_key":"Chat-and-LLM-apps","name":"Chat and LLM apps","depth":"2","children":[{"menu_key":"Build-a-basic-LLM-chat-app","name":"Build a basic LLM chat app","depth":"3","children":[],"category":"Develop / Tutorials / Chat and LLM apps / Build a basic LLM chat app","url":"/develop/tutorials/chat-and-llm-apps/build-conversational-apps"},{"menu_key":"Build-an-LLM-app-using-LangChain","name":"Build an LLM app using LangChain","depth":"3","children":[],"category":"Develop / Tutorials / Chat and LLM apps / Build an LLM app using LangChain","url":"/develop/tutorials/chat-and-llm-apps/llm-quickstart"},{"menu_key":"Get-chat-response-feedback","name":"Get chat response feedback","depth":"3","children":[],"category":"Develop / Tutorials / Chat and LLM apps / Get chat response feedback","url":"/develop/tutorials/chat-and-llm-apps/chat-response-feedback"},{"menu_key":"Validate-and-edit-chat-responses","name":"Validate and edit chat responses","depth":"3","children":[],"category":"Develop / Tutorials / Chat and LLM apps / Validate and edit chat responses","url":"/develop/tutorials/chat-and-llm-apps/validate-and-edit-chat-responses"}],"category":"Develop / Tutorials / Chat and LLM apps","url":"/develop/tutorials/chat-and-llm-apps"},{"menu_key":"Configuration-and-theming","name":"Configuration and theming","depth":"2","children":[{"menu_key":"Use-external-font-files","name":"Use external font files","depth":"3","children":[],"category":"Develop / Tutorials / Configuration and theming / Use external font files","url":"/develop/tutorials/configuration-and-theming/external-fonts"},{"menu_key":"Use-external-font-files-(streamlitless1.50.0)","name":"Use external font files (streamlit\u003c1.50.0)","depth":"3","children":[],"category":"Develop / Tutorials / Configuration and theming / Use external font files (streamlit\u003c1.50.0)","url":"/develop/tutorials/configuration-and-theming/external-fonts-old","visible":false},{"menu_key":"Use-static-font-files","name":"Use static font files","depth":"3","children":[],"category":"Develop / Tutorials / Configuration and theming / Use static font files","url":"/develop/tutorials/configuration-and-theming/static-fonts"},{"menu_key":"Use-variable-font-files","name":"Use variable font files","depth":"3","children":[],"category":"Develop / Tutorials / Configuration and theming / Use variable font files","url":"/develop/tutorials/configuration-and-theming/variable-fonts"}],"category":"Develop / Tutorials / Configuration and theming","url":"/develop/tutorials/configuration-and-theming"},{"menu_key":"Connect-to-data-sources","name":"Connect to data sources","depth":"2","children":[{"menu_key":"AWS-S3","name":"AWS S3","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / AWS S3","url":"/develop/tutorials/databases/aws-s3"},{"menu_key":"BigQuery","name":"BigQuery","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / BigQuery","url":"/develop/tutorials/databases/bigquery"},{"menu_key":"Firestore","name":"Firestore","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Firestore","url":"https://blog.streamlit.io/streamlit-firestore/"},{"menu_key":"Google-Cloud-Storage","name":"Google Cloud Storage","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Google Cloud Storage","url":"/develop/tutorials/databases/gcs"},{"menu_key":"Microsoft-SQL-Server","name":"Microsoft SQL Server","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Microsoft SQL Server","url":"/develop/tutorials/databases/mssql"},{"menu_key":"MongoDB","name":"MongoDB","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / MongoDB","url":"/develop/tutorials/databases/mongodb"},{"menu_key":"MySQL","name":"MySQL","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / MySQL","url":"/develop/tutorials/databases/mysql"},{"menu_key":"Neon","name":"Neon","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Neon","url":"/develop/tutorials/databases/neon"},{"menu_key":"PostgreSQL","name":"PostgreSQL","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / PostgreSQL","url":"/develop/tutorials/databases/postgresql"},{"menu_key":"Private-Google-Sheet","name":"Private Google Sheet","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Private Google Sheet","url":"/develop/tutorials/databases/private-gsheet"},{"menu_key":"Public-Google-Sheet","name":"Public Google Sheet","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Public Google Sheet","url":"/develop/tutorials/databases/public-gsheet"},{"menu_key":"Snowflake","name":"Snowflake","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Snowflake","url":"/develop/tutorials/databases/snowflake"},{"menu_key":"Supabase","name":"Supabase","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Supabase","url":"/develop/tutorials/databases/supabase"},{"menu_key":"Tableau","name":"Tableau","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / Tableau","url":"/develop/tutorials/databases/tableau"},{"menu_key":"TiDB","name":"TiDB","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / TiDB","url":"/develop/tutorials/databases/tidb"},{"menu_key":"TigerGraph","name":"TigerGraph","depth":"3","children":[],"category":"Develop / Tutorials / Connect to data sources / TigerGraph","url":"/develop/tutorials/databases/tigergraph"}],"category":"Develop / Tutorials / Connect to data sources","url":"/develop/tutorials/databases"},{"menu_key":"Elements","name":"Elements","depth":"2","children":[{"menu_key":"CHARTS","name":"CHARTS","depth":"3","children":[],"category":"Develop / Tutorials / Elements / CHARTS"},{"menu_key":"Annotate-an-Altair-chart","name":"Annotate an Altair chart","depth":"3","children":[],"category":"Develop / Tutorials / Elements / Annotate an Altair chart","url":"/develop/tutorials/elements/annotate-an-altair-chart"},{"menu_key":"DATAFRAMES","name":"DATAFRAMES","depth":"3","children":[],"category":"Develop / Tutorials / Elements / DATAFRAMES"},{"menu_key":"Get-dataframe-row-selections","name":"Get dataframe row-selections","depth":"3","children":[],"category":"Develop / Tutorials / Elements / Get dataframe row-selections","url":"/develop/tutorials/elements/dataframe-row-selections"},{"menu_key":"Get-dataframe-row-selections-(streamlitless1.35.0)","name":"Get dataframe row-selections (streamlit\u003c1.35.0)","depth":"3","children":[],"category":"Develop / Tutorials / Elements / Get dataframe row-selections (streamlit\u003c1.35.0)","url":"/develop/tutorials/elements/dataframe-row-selections-old","visible":false}],"category":"Develop / Tutorials / Elements","url":"/develop/tutorials/elements"},{"menu_key":"Execution-flow","name":"Execution flow","depth":"2","children":[{"menu_key":"FRAGMENTS","name":"FRAGMENTS","depth":"3","children":[],"category":"Develop / Tutorials / Execution flow / FRAGMENTS"},{"menu_key":"Rerun-your-app-from-a-fragment","name":"Rerun your app from a fragment","depth":"3","children":[],"category":"Develop / Tutorials / Execution flow / Rerun your app from a fragment","url":"/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment"},{"menu_key":"Create-a-multiple-container-fragment","name":"Create a multiple-container fragment","depth":"3","children":[],"category":"Develop / Tutorials / Execution flow / Create a multiple-container fragment","url":"/develop/tutorials/execution-flow/create-a-multiple-container-fragment"},{"menu_key":"Start-and-stop-a-streaming-fragment","name":"Start and stop a streaming fragment","depth":"3","children":[],"category":"Develop / Tutorials / Execution flow / Start and stop a streaming fragment","url":"/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns"}],"category":"Develop / Tutorials / Execution flow","url":"/develop/tutorials/execution-flow"},{"menu_key":"Multipage-apps","name":"Multipage apps","depth":"2","children":[{"menu_key":"Dynamic-navigation","name":"Dynamic navigation","depth":"3","children":[],"category":"Develop / Tutorials / Multipage apps / Dynamic navigation","url":"/develop/tutorials/multipage/dynamic-navigation"},{"menu_key":"Build-navigation-with-st.page_link","name":"Build navigation with st.page_link","depth":"3","children":[],"category":"Develop / Tutorials / Multipage apps / Build navigation with st.page_link","url":"/develop/tutorials/multipage/st.page_link-nav","visible":false}],"category":"Develop / Tutorials / Multipage apps","url":"/develop/tutorials/multipage"}],"category":"Develop / Tutorials","url":"/develop/tutorials"},{"menu_key":"Quick-reference","name":"Quick reference","depth":"1","children":[{"menu_key":"Cheat-sheet","name":"Cheat sheet","depth":"2","children":[],"category":"Develop / Quick reference / Cheat sheet","url":"/develop/quick-reference/cheat-sheet"},{"menu_key":"Release-notes","name":"Release notes","depth":"2","children":[{"menu_key":"2025","name":"2025","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2025","url":"/develop/quick-reference/release-notes/2025"},{"menu_key":"2024","name":"2024","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2024","url":"/develop/quick-reference/release-notes/2024"},{"menu_key":"2023","name":"2023","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2023","url":"/develop/quick-reference/release-notes/2023"},{"menu_key":"2022","name":"2022","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2022","url":"/develop/quick-reference/release-notes/2022"},{"menu_key":"2021","name":"2021","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2021","url":"/develop/quick-reference/release-notes/2021"},{"menu_key":"2020","name":"2020","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2020","url":"/develop/quick-reference/release-notes/2020"},{"menu_key":"2019","name":"2019","depth":"3","children":[],"category":"Develop / Quick reference / Release notes / 2019","url":"/develop/quick-reference/release-notes/2019"}],"category":"Develop / Quick reference / Release notes","url":"/develop/quick-reference/release-notes"},{"menu_key":"Pre-release-features","name":"Pre-release features","depth":"2","children":[],"category":"Develop / Quick reference / Pre-release features","url":"/develop/quick-reference/prerelease"},{"menu_key":"Roadmap","name":"Roadmap","depth":"2","children":[],"category":"Develop / Quick reference/ Roadmap","url":"https://roadmap.streamlit.app"}],"category":"Develop / Quick reference","url":"/develop/quick-reference"}],"category":"Develop","url":"/develop","color":"indigo-70","icon":"code"},{"menu_key":"Deploy","name":"Deploy","depth":"0","children":[{"menu_key":"Concepts","name":"Concepts","depth":"1","children":[{"menu_key":"Dependencies","name":"Dependencies","depth":"2","children":[],"category":"Deploy / Concepts / Dependencies","url":"/deploy/concepts/dependencies"},{"menu_key":"Secrets","name":"Secrets","depth":"2","children":[],"category":"Deploy / Concepts / Secrets","url":"/deploy/concepts/secrets"}],"category":"Deploy / Concepts","url":"/deploy/concepts"},{"menu_key":"Streamlit-Community-Cloud","name":"Streamlit Community Cloud","depth":"1","children":[{"menu_key":"Get-started","name":"Get started","depth":"2","children":[{"menu_key":"Quickstart","name":"Quickstart","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Quickstart","url":"/deploy/streamlit-community-cloud/get-started/quickstart"},{"menu_key":"Create-your-account","name":"Create your account","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Create your account","url":"/deploy/streamlit-community-cloud/get-started/create-your-account"},{"menu_key":"Connect-your-GitHub-account","name":"Connect your GitHub account","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Connect your GitHub account","url":"/deploy/streamlit-community-cloud/get-started/connect-your-github-account"},{"menu_key":"Explore-your-workspace","name":"Explore your workspace","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Explore your workspace","url":"/deploy/streamlit-community-cloud/get-started/explore-your-workspace"},{"menu_key":"Deploy-from-a-template","name":"Deploy from a template","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Deploy from a template","url":"/deploy/streamlit-community-cloud/get-started/deploy-from-a-template"},{"menu_key":"Fork-and-edit-a-public-app","name":"Fork and edit a public app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Fork and edit a public app","url":"/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app"},{"menu_key":"Trust-and-security","name":"Trust and security","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Get started / Trust and security","url":"/deploy/streamlit-community-cloud/get-started/trust-and-security"}],"category":"Deploy / Streamlit Community Cloud / Get started","url":"/deploy/streamlit-community-cloud/get-started"},{"menu_key":"Deploy-your-app","name":"Deploy your app","depth":"2","children":[{"menu_key":"File-organization","name":"File organization","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Deploy your app / File organization","url":"/deploy/streamlit-community-cloud/deploy-your-app/file-organization"},{"menu_key":"App-dependencies","name":"App dependencies","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Deploy your app / App dependencies","url":"/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies"},{"menu_key":"Secrets-management","name":"Secrets management","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Deploy your app / Secrets management","url":"/deploy/streamlit-community-cloud/deploy-your-app/secrets-management"},{"menu_key":"Deploy!","name":"Deploy!","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Deploy your app / Deploy!","url":"/deploy/streamlit-community-cloud/deploy-your-app/deploy"}],"category":"Deploy / Streamlit Community Cloud / Deploy your app","url":"/deploy/streamlit-community-cloud/deploy-your-app"},{"menu_key":"Manage-your-app","name":"Manage your app","depth":"2","children":[{"menu_key":"App-analytics","name":"App analytics","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / App analytics","url":"/deploy/streamlit-community-cloud/manage-your-app/app-analytics"},{"menu_key":"App-settings","name":"App settings","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / App settings","url":"/deploy/streamlit-community-cloud/manage-your-app/app-settings"},{"menu_key":"Delete-your-app","name":"Delete your app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Delete your app","url":"/deploy/streamlit-community-cloud/manage-your-app/delete-your-app"},{"menu_key":"Edit-your-app","name":"Edit your app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Edit your app","url":"/deploy/streamlit-community-cloud/manage-your-app/edit-your-app"},{"menu_key":"Favorite-your-app","name":"Favorite your app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Favorite your app","url":"/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app"},{"menu_key":"Reboot-your-app","name":"Reboot your app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Reboot your app","url":"/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app"},{"menu_key":"Rename-your-app-in-GitHub","name":"Rename your app in GitHub","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Rename your app in GitHub","url":"/deploy/streamlit-community-cloud/manage-your-app/rename-your-app"},{"menu_key":"Upgrade-Python","name":"Upgrade Python","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Upgrade Python","url":"/deploy/streamlit-community-cloud/manage-your-app/upgrade-python"},{"menu_key":"Upgrade-Streamlit","name":"Upgrade Streamlit","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your app / Upgrade Streamlit","url":"/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit"}],"category":"Deploy / Streamlit Community Cloud / Manage your app","url":"/deploy/streamlit-community-cloud/manage-your-app"},{"menu_key":"Share-your-app","name":"Share your app","depth":"2","children":[{"menu_key":"Embed-your-app","name":"Embed your app","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Share your app / Embed your app","url":"/deploy/streamlit-community-cloud/share-your-app/embed-your-app"},{"menu_key":"Search-indexability","name":"Search indexability","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Share your app / Search indexability","url":"/deploy/streamlit-community-cloud/share-your-app/indexability"},{"menu_key":"Share-previews","name":"Share previews","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Share your app / Share previews","url":"/deploy/streamlit-community-cloud/share-your-app/share-previews"}],"category":"Deploy / Streamlit Community Cloud / Share your app","url":"/deploy/streamlit-community-cloud/share-your-app"},{"menu_key":"Manage-your-account","name":"Manage your account","depth":"2","children":[{"menu_key":"Sign-in-and-sign-out","name":"Sign in and sign out","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your account / Sign in and sign out","url":"/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out"},{"menu_key":"Workspace-settings","name":"Workspace settings","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your account / Workspace settings","url":"/deploy/streamlit-community-cloud/manage-your-account/workspace-settings"},{"menu_key":"Manage-your-GitHub-connection","name":"Manage your GitHub connection","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your account / Manage your GitHub connection","url":"/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection"},{"menu_key":"Update-your-email","name":"Update your email","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your account / Update your email","url":"/deploy/streamlit-community-cloud/manage-your-account/update-your-email"},{"menu_key":"Delete-your-account","name":"Delete your account","depth":"3","children":[],"category":"Deploy / Streamlit Community Cloud / Manage your account / Delete your account","url":"/deploy/streamlit-community-cloud/manage-your-account/delete-your-account"}],"category":"Deploy / Streamlit Community Cloud / Manage your account","url":"/deploy/streamlit-community-cloud/manage-your-account"},{"menu_key":"Status-and-limitations","name":"Status and limitations","depth":"2","children":[],"category":"Deploy / Streamlit Community Cloud / Status and limitations","url":"/deploy/streamlit-community-cloud/status"}],"category":"Deploy / Streamlit Community Cloud","url":"/deploy/streamlit-community-cloud"},{"menu_key":"Snowflake","name":"Snowflake","depth":"1","children":[],"category":"Deploy / Snowflake","url":"/deploy/snowflake"},{"menu_key":"Other-platforms","name":"Other platforms","depth":"1","children":[{"menu_key":"Docker","name":"Docker","depth":"2","children":[],"category":"Deploy / Other platforms / Docker","url":"/deploy/tutorials/docker"},{"menu_key":"Kubernetes","name":"Kubernetes","depth":"2","children":[],"category":"Deploy / Other platforms / Kubernetes","url":"/deploy/tutorials/kubernetes"}],"category":"Deploy / Other platforms","url":"/deploy/tutorials"}],"category":"Deploy","url":"/deploy","color":"lightBlue-70","icon":"web_asset"},{"menu_key":"Knowledge-base","name":"Knowledge base","depth":"0","children":[{"menu_key":"FAQ","name":"FAQ","depth":"1","children":[{"menu_key":"How-do-I-create-an-anchor-link","name":"How do I create an anchor link?","depth":"2","children":[],"category":"Knowledge base / FAQ / How do I create an anchor link?","url":"/knowledge-base/using-streamlit/create-anchor-link","visible":false},{"menu_key":"Enabling-camera-access-in-your-browser","name":"Enabling camera access in your browser","depth":"2","children":[],"category":"Knowledge base / FAQ / Enabling camera access in your browser","url":"/knowledge-base/using-streamlit/enable-camera","visible":false},{"menu_key":"How-to-download-a-file-in-Streamlit","name":"How to download a file in Streamlit?","depth":"2","children":[],"category":"Knowledge base / FAQ / How to download a file in Streamlit?","url":"/knowledge-base/using-streamlit/how-download-file-streamlit","visible":false},{"menu_key":"How-to-download-a-Pandas-DataFrame-as-a-CSV","name":"How to download a Pandas DataFrame as a CSV?","depth":"2","children":[],"category":"Knowledge base / FAQ / How to download a Pandas DataFrame as a CSV?","url":"/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv","visible":false},{"menu_key":"How-do-I-upgrade-to-the-latest-version-of-Streamlit","name":"How do I upgrade to the latest version of Streamlit?","depth":"2","children":[],"category":"Knowledge base / FAQ / How do I upgrade to the latest version of Streamlit?","url":"/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit","visible":false},{"menu_key":"How-to-insert-elements-out-of-order","name":"How to insert elements out of order?","depth":"2","children":[],"category":"Knowledge base / FAQ / How to insert elements out of order?","url":"/knowledge-base/using-streamlit/insert-elements-out-of-order","visible":false},{"menu_key":"How-can-I-make-st.pydeck_chart-use-custom-Mapbox-styles","name":"How can I make st.pydeck_chart use custom Mapbox styles?","depth":"2","children":[],"category":"Knowledge base / FAQ / How can I make st.pydeck_chart use custom Mapbox styles?","url":"/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles","visible":false},{"menu_key":"How-to-remove-\"-Streamlit\"-from-the-app-title","name":"How to remove \"· Streamlit\" from the app title?","depth":"2","children":[],"category":"Knowledge base / FAQ / How to remove \"· Streamlit\" from the app title?","url":"/knowledge-base/using-streamlit/remove-streamlit-app-title","visible":false},{"menu_key":"How-do-you-retrieve-the-filename-of-a-file-uploaded-with-st.file_uploader","name":"How do you retrieve the filename of a file uploaded with st.file_uploader?","depth":"2","children":[],"category":"Knowledge base / FAQ / How do you retrieve the filename of a file uploaded with st.file_uploader?","url":"/knowledge-base/using-streamlit/retrieve-filename-uploaded","visible":false},{"menu_key":"Sanity-checks","name":"Sanity checks","depth":"2","children":[],"category":"Knowledge base / FAQ / Sanity checks","url":"/knowledge-base/using-streamlit/sanity-checks","visible":false},{"menu_key":"How-can-I-make-Streamlit-watch-for-changes-in-other-modules-I'm-importing-in-my-app","name":"How can I make Streamlit watch for changes in other modules I'm importing in my app?","depth":"2","children":[],"category":"Knowledge base / FAQ / How can I make Streamlit watch for changes in other modules I'm importing in my app?","url":"/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app","visible":false},{"menu_key":"What-browsers-does-Streamlit-support","name":"What browsers does Streamlit support?","depth":"2","children":[],"category":"Knowledge base / FAQ / What browsers does Streamlit support?","url":"/knowledge-base/using-streamlit/supported-browsers","visible":false},{"menu_key":"Where-does-st.file_uploader-store-uploaded-files-and-when-do-they-get-deleted","name":"Where does st.file_uploader store uploaded files and when do they get deleted?","depth":"2","children":[],"category":"Knowledge base / FAQ / Where does st.file_uploader store uploaded files and when do they get deleted?","url":"/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted","visible":false},{"menu_key":"Widget-updating-for-every-second-input-when-using-session-state","name":"Widget updating for every second input when using session state","depth":"2","children":[],"category":"Knowledge base / FAQ / Widget updating for every second input when using session state","url":"/knowledge-base/using-streamlit/widget-updating-session-state","visible":false},{"menu_key":"Why-does-Streamlit-restrict-nested-st.columns","name":"Why does Streamlit restrict nested st.columns?","depth":"2","children":[],"category":"Knowledge base / FAQ / Why does Streamlit restrict nested st.columns?","url":"/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns","visible":false},{"menu_key":"What-is-serializable-session-state","name":"What is serializable session state?","depth":"2","children":[],"category":"Knowledge base / FAQ / What is serializable session state?","url":"/knowledge-base/using-streamlit/serializable-session-state","visible":false}],"category":"Knowledge base / FAQ","url":"/knowledge-base/using-streamlit"},{"menu_key":"Installing-dependencies","name":"Installing dependencies","depth":"1","children":[{"menu_key":"How-to-install-a-package-not-on-PyPI-or-Conda-but-available-on-GitHub","name":"How to install a package not on PyPI or Conda but available on GitHub","depth":"2","children":[],"category":"Knowledge base / Installing dependencies / How to install a package not on PyPI or Conda but available on GitHub","url":"/knowledge-base/dependencies/install-package-not-pypi-conda-available-github","visible":false},{"menu_key":"ImportError-libGL.so.1-cannot-open-shared-object-file-No-such-file-or-directory","name":"ImportError libGL.so.1 cannot open shared object file No such file or directory","depth":"2","children":[],"category":"Knowledge base / Installing dependencies / ImportError libGL.so.1 cannot open shared object file No such file or directory","url":"/knowledge-base/dependencies/libgl","visible":false},{"menu_key":"ModuleNotFoundError-No-module-named","name":"ModuleNotFoundError No module named","depth":"2","children":[],"category":"Knowledge base / Installing dependencies / ModuleNotFoundError No module named","url":"/knowledge-base/dependencies/module-not-found-error","visible":false},{"menu_key":"ERROR-No-matching-distribution-found-for","name":"ERROR No matching distribution found for","depth":"2","children":[],"category":"Knowledge base / Installing dependencies / ERROR No matching distribution found for","url":"/knowledge-base/dependencies/no-matching-distribution","visible":false}],"category":"Knowledge base / Installing dependencies","url":"/knowledge-base/dependencies"},{"menu_key":"Deployment-issues","name":"Deployment issues","depth":"1","children":[{"menu_key":"How-can-I-deploy-multiple-Streamlit-apps-on-different-subdomains","name":"How can I deploy multiple Streamlit apps on different subdomains?","depth":"2","children":[],"category":"Knowledge base / Deployment issues / How can I deploy multiple Streamlit apps on different subdomains?","url":"/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains","visible":false},{"menu_key":"How-do-I-deploy-Streamlit-on-a-domain-so-it-appears-to-run-on-a-regular-port-(i.e.-port-80)","name":"How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?","depth":"2","children":[],"category":"Knowledge base / Deployment issues / How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?","url":"/knowledge-base/deploy/deploy-streamlit-domain-port-80","visible":false},{"menu_key":"Does-Streamlit-support-the-WSGI-Protocol-(aka-Can-I-deploy-Streamlit-with-gunicorn)","name":"Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)","url":"/knowledge-base/deploy/does-streamlit-support-wsgi-protocol","visible":false},{"menu_key":"How-do-I-increase-the-upload-limit-of-st.file_uploader-on-Streamlit-Community-Cloud","name":"How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?","depth":"2","children":[],"category":"Knowledge base / Deployment issues / How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?","url":"/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud","visible":false},{"menu_key":"Invoking-a-Python-subprocess-in-a-deployed-Streamlit-app","name":"Invoking a Python subprocess in a deployed Streamlit app","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Invoking a Python subprocess in a deployed Streamlit app","url":"/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app","visible":false},{"menu_key":"App-is-not-loading-when-running-remotely","name":"App is not loading when running remotely","depth":"2","children":[],"category":"Knowledge base / Deployment issues / App is not loading when running remotely","url":"/knowledge-base/deploy/remote-start","visible":false},{"menu_key":"Argh.-This-app-has-gone-over-its-resource-limits","name":"Argh. This app has gone over its resource limits","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Argh. This app has gone over its resource limits","url":"/knowledge-base/deploy/resource-limits","visible":false},{"menu_key":"How-do-I-share-apps-with-viewers-outside-my-organization","name":"How do I share apps with viewers outside my organization?","depth":"2","children":[],"category":"Knowledge base / Deployment issues / How do I share apps with viewers outside my organization?","url":"/knowledge-base/deploy/share-apps-with-viewers-outside-organization","visible":false},{"menu_key":"Upgrade-the-Streamlit-version-of-your-app-on-Streamlit-Community-Cloud","name":"Upgrade the Streamlit version of your app on Streamlit Community Cloud","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Upgrade the Streamlit version of your app on Streamlit Community Cloud","url":"/knowledge-base/deploy/upgrade-streamlit-version-on-streamlit-cloud","visible":false},{"menu_key":"Huh.-This-is-isn't-supposed-to-happen-message-after-trying-to-log-in","name":"Huh. This is isn't supposed to happen message after trying to log in","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Huh. This is isn't supposed to happen message after trying to log in","url":"/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in","visible":false},{"menu_key":"Login-attempt-to-Streamlit-Community-Cloud-fails-with-error-403","name":"Login attempt to Streamlit Community Cloud fails with error 403","depth":"2","children":[],"category":"Knowledge base / Deployment issues / Login attempt to Streamlit Community Cloud fails with error 403","url":"/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403","visible":false},{"menu_key":"How-to-submit-a-support-case-for-Streamlit-Community-Cloud","name":"How to submit a support case for Streamlit Community Cloud","depth":"2","children":[],"category":"Knowledge base / Deployment issues / How to submit a support case for Streamlit Community Cloud","url":"/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud","visible":false}],"category":"Knowledge base / Deployment issues","url":"/knowledge-base/deploy"}],"category":"Knowledge base","url":"/knowledge-base","color":"darkBlue-70","icon":"school"}],"data":{"title":"config.toml","slug":"/develop/api-reference/configuration/config.toml","description":"Complete reference guide for Streamlit's config.toml configuration file, including all available sections and options for customizing your Streamlit application settings.","keywords":"config.toml, streamlit configuration, toml configuration file, streamlit settings, theme configuration, server configuration, client configuration, logger configuration, browser configuration, mapbox configuration, secrets configuration, sidebar theme, configuration options, streamlit config show"},"filename":"/opt/build/repo/content/develop/api-reference/configuration/config-toml.md","slug":["develop","api-reference","configuration","config.toml"],"source":{"compiledSource":"/*@jsxRuntime automatic @jsxImportSource react*/\nconst {Fragment: _Fragment, jsx: _jsx, jsxs: _jsxs} = arguments[0];\nconst {useMDXComponents: _provideComponents} = arguments[0];\nfunction _createMdxContent(props) {\n  const _components = Object.assign({\n    h2: \"h2\",\n    a: \"a\",\n    span: \"span\",\n    p: \"p\",\n    code: \"code\",\n    h3: \"h3\",\n    h4: \"h4\",\n    pre: \"pre\",\n    ul: \"ul\",\n    li: \"li\"\n  }, _provideComponents(), props.components);\n  return _jsxs(_Fragment, {\n    children: [_jsxs(_components.h2, {\n      id: \"configtoml\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#configtoml\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"config.toml\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [_jsx(_components.code, {\n        children: \"config.toml\"\n      }), \" is an optional file you can define for your working directory or global development environment. When \", _jsx(_components.code, {\n        children: \"config.toml\"\n      }), \" is defined both globally and in your working directory, Streamlit combines the configuration options and gives precedence to the working-directory configuration. Additionally, you can use environment variables and command-line options to override additional configuration options. For more information, see \", _jsx(_components.a, {\n        href: \"/develop/concepts/configuration/options\",\n        children: \"Configuration options\"\n      }), \".\"]\n    }), \"\\n\", _jsxs(_components.h3, {\n      id: \"file-location\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#file-location\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"File location\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [\"To define your configuration locally or per-project, add \", _jsx(_components.code, {\n        children: \".streamlit/config.toml\"\n      }), \" to your working directory. Your working directory is wherever you call \", _jsx(_components.code, {\n        children: \"streamlit run\"\n      }), \". If you haven't previously created the \", _jsx(_components.code, {\n        children: \".streamlit\"\n      }), \" directory, you will need to add it.\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [\"To define your configuration globally, you must first locate your global \", _jsx(_components.code, {\n        children: \".streamlit\"\n      }), \" directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linux, this will be \", _jsx(_components.code, {\n        children: \"~/.streamlit/config.toml\"\n      }), \". For Windows, this will be \", _jsx(_components.code, {\n        children: \"%userprofile%/.streamlit/config.toml\"\n      }), \".\"]\n    }), \"\\n\", _jsxs(_components.h3, {\n      id: \"file-format\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#file-format\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"File format\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [_jsx(_components.code, {\n        children: \"config.toml\"\n      }), \" is a \", _jsx(_components.a, {\n        href: \"https://toml.io/en/\",\n        children: \"TOML\"\n      }), \" file.\"]\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"example\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#example\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Example\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[client]\\nshowErrorDetails = \\\"none\\\"\\n\\n[theme]\\nprimaryColor = \\\"#F63366\\\"\\nbackgroundColor = \\\"black\\\"\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h3, {\n      id: \"available-configuration-options\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#available-configuration-options\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Available configuration options\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [\"Below are all the sections and options you can have in your \", _jsx(_components.code, {\n        children: \".streamlit/config.toml\"\n      }), \" file. To see all configurations, use the following command in your terminal or CLI:\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-bash\",\n        children: \"streamlit config show\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"global\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#global\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Global\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[global]\\n\\n# By default, Streamlit displays a warning when a user sets both a widget\\n# default value in the function defining the widget and a widget value via\\n# the widget's key in `st.session_state`.\\n#\\n# If you'd like to turn off this warning, set this to True.\\n#\\n# Default: false\\ndisableWidgetStateDuplicationWarning = false\\n\\n# If True, will show a warning when you run a Streamlit-enabled script\\n# via \\\"python my_script.py\\\".\\n#\\n# Default: true\\nshowWarningOnDirectExecution = true\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"logger\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#logger\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Logger\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[logger]\\n\\n# Level of logging for Streamlit's internal logger: \\\"error\\\", \\\"warning\\\",\\n# \\\"info\\\", or \\\"debug\\\".\\n#\\n# Default: \\\"info\\\"\\nlevel = \\\"info\\\"\\n\\n# String format for logging messages. If logger.datetimeFormat is set,\\n# logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`.\\n#\\n# See Python's documentation for available attributes:\\n# https://docs.python.org/3/library/logging.html#formatter-objects\\n#\\n# Default: \\\"%(asctime)s %(message)s\\\"\\nmessageFormat = \\\"%(asctime)s %(message)s\\\"\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"client\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#client\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Client\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[client]\\n\\n# Controls whether uncaught app exceptions and deprecation warnings\\n# are displayed in the browser. This can be one of the following:\\n#\\n# - \\\"full\\\"       : In the browser, Streamlit displays app deprecation\\n#                  warnings and exceptions, including exception types,\\n#                  exception messages, and associated tracebacks.\\n# - \\\"stacktrace\\\" : In the browser, Streamlit displays exceptions,\\n#                  including exception types, generic exception messages,\\n#                  and associated tracebacks. Deprecation warnings and\\n#                  full exception messages will only print to the\\n#                  console.\\n# - \\\"type\\\"       : In the browser, Streamlit displays exception types and\\n#                  generic exception messages. Deprecation warnings, full\\n#                  exception messages, and associated tracebacks only\\n#                  print to the console.\\n# - \\\"none\\\"       : In the browser, Streamlit displays generic exception\\n#                  messages. Deprecation warnings, full exception\\n#                  messages, associated tracebacks, and exception types\\n#                  will only print to the console.\\n# - True         : This is deprecated. Streamlit displays \\\"full\\\"\\n#                  error details.\\n# - False        : This is deprecated. Streamlit displays \\\"stacktrace\\\"\\n#                  error details.\\n#\\n# Default: \\\"full\\\"\\nshowErrorDetails = \\\"full\\\"\\n\\n# Change the visibility of items in the toolbar, options menu,\\n# and settings dialog (top right of the app).\\n#\\n# Allowed values:\\n# - \\\"auto\\\"      : Show the developer options if the app is accessed through\\n#                 localhost or through Streamlit Community Cloud as a developer.\\n#                 Hide them otherwise.\\n# - \\\"developer\\\" : Show the developer options.\\n# - \\\"viewer\\\"    : Hide the developer options.\\n# - \\\"minimal\\\"   : Show only options set externally (e.g. through\\n#                 Streamlit Community Cloud) or through st.set_page_config.\\n#                 If there are no options left, hide the menu.\\n#\\n# Default: \\\"auto\\\"\\ntoolbarMode = \\\"auto\\\"\\n\\n# Controls whether to display the default sidebar page navigation in a\\n# multi-page app. This only applies when app's pages are defined by the\\n# `pages/` directory.\\n#\\n# Default: true\\nshowSidebarNavigation = true\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"runner\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#runner\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Runner\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[runner]\\n\\n# Allows you to type a variable or string by itself in a single line of\\n# Python code to write it to the app.\\n#\\n# Default: true\\nmagicEnabled = true\\n\\n# Handle script rerun requests immediately, rather than waiting for\\n# script execution to reach a yield point.\\n#\\n# This makes Streamlit much more responsive to user interaction, but it\\n# can lead to race conditions in apps that mutate session_state data\\n# outside of explicit session_state assignment statements.\\n#\\n# Default: true\\nfastReruns = true\\n\\n# Raise an exception after adding unserializable data to Session State.\\n#\\n# Some execution environments may require serializing all data in Session\\n# State, so it may be useful to detect incompatibility during development,\\n# or when the execution environment will stop supporting it in the future.\\n#\\n# Default: false\\nenforceSerializableSessionState = false\\n\\n# Adjust how certain 'options' widgets like radio, selectbox, and\\n# multiselect coerce Enum members.\\n#\\n# This is useful when the Enum class gets re-defined during a script\\n# re-run. For more information, check out the docs:\\n# https://docs.streamlit.io/develop/concepts/design/custom-classes#enums\\n#\\n# Allowed values:\\n# - \\\"off\\\"          : Disables Enum coercion.\\n# - \\\"nameOnly\\\"     : Enum classes can be coerced if their member names match.\\n# - \\\"nameAndValue\\\" : Enum classes can be coerced if their member names AND\\n#                    member values match.\\n#\\n# Default: \\\"nameOnly\\\"\\nenumCoercion = \\\"nameOnly\\\"\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"server\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#server\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Server\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[server]\\n\\n# List of directories to watch for changes.\\n#\\n# By default, Streamlit watches files in the current working directory\\n# and its subdirectories. Use this option to specify additional\\n# directories to watch. Paths must be absolute.\\n#\\n# Default: []\\nfolderWatchList = []\\n\\n# List of directories to ignore for changes.\\n#\\n# By default, Streamlit watches files in the current working directory\\n# and its subdirectories. Use this option to specify exceptions within\\n# watched directories. Paths can be absolute or relative to the current\\n# working directory.\\n#\\n# Example: ['/home/user1/env', 'relative/path/to/folder']\\n#\\n# Default: []\\nfolderWatchBlacklist = []\\n\\n# Change the type of file watcher used by Streamlit, or turn it off\\n# completely.\\n#\\n# Allowed values:\\n# - \\\"auto\\\"     : Streamlit will attempt to use the watchdog module, and\\n#                falls back to polling if watchdog isn't available.\\n# - \\\"watchdog\\\" : Force Streamlit to use the watchdog module.\\n# - \\\"poll\\\"     : Force Streamlit to always use polling.\\n# - \\\"none\\\"     : Streamlit will not watch files.\\n#\\n# Default: \\\"auto\\\"\\nfileWatcherType = \\\"auto\\\"\\n\\n# Symmetric key used to produce signed cookies. If deploying on multiple\\n# replicas, this should be set to the same value across all replicas to ensure\\n# they all share the same secret.\\n#\\n# Default: randomly generated secret key.\\ncookieSecret = \\\"a-random-key-appears-here\\\"\\n\\n# If false, will attempt to open a browser window on start.\\n#\\n# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or\\n# (2) we are running in the Streamlit Atom plugin.\\nheadless = false\\n\\n# Whether to show a terminal prompt for the user's email address when\\n# they run Streamlit (locally) for the first time. If you set\\n# `server.headless=True`, Streamlit will not show this prompt.\\n#\\n# Default: true\\nshowEmailPrompt = true\\n\\n# Automatically rerun script when the file is modified on disk.\\n#\\n# Default: false\\nrunOnSave = false\\n\\n# The address where the server will listen for client and browser\\n# connections.\\n#\\n# Use this if you want to bind the server to a specific address.\\n# If set, the server will only be accessible from this address, and not from\\n# any aliases (like localhost).\\n#\\n# Default: (unset)\\naddress =\\n\\n# The port where the server will listen for browser connections.\\n#\\n# Default: 8501\\nport = 8501\\n\\n# The base path for the URL where Streamlit should be served from.\\n#\\n# Default: \\\"\\\"\\nbaseUrlPath = \\\"\\\"\\n\\n# Enables support for Cross-Origin Resource Sharing (CORS) protection,\\n# for added security.\\n#\\n# If XSRF protection is enabled and CORS protection is disabled at the\\n# same time, Streamlit will enable them both instead.\\n#\\n# Default: true\\nenableCORS = true\\n\\n# Allowed list of origins.\\n#\\n# If CORS protection is enabled (`server.enableCORS=True`), use this\\n# option to set a list of allowed origins that the Streamlit server will\\n# accept traffic from.\\n#\\n# This config option does nothing if CORS protection is disabled.\\n#\\n# Example: ['http://example.com', 'https://streamlit.io']\\n#\\n# Default: []\\ncorsAllowedOrigins = []\\n\\n# Enables support for Cross-Site Request Forgery (XSRF) protection, for\\n# added security.\\n#\\n# If XSRF protection is enabled and CORS protection is disabled at the\\n# same time, Streamlit will enable them both instead.\\n#\\n# Default: true\\nenableXsrfProtection = true\\n\\n# Max size, in megabytes, for files uploaded with the file_uploader.\\n#\\n# Default: 200\\nmaxUploadSize = 200\\n\\n# Max size, in megabytes, of messages that can be sent via the WebSocket\\n# connection.\\n#\\n# Default: 200\\nmaxMessageSize = 200\\n\\n# Enables support for websocket compression.\\n#\\n# Default: false\\nenableWebsocketCompression = false\\n\\n# The interval (in seconds) at which the server pings the client to keep\\n# the websocket connection alive.\\n#\\n# The default value should work for most deployments. However, if you're\\n# experiencing frequent disconnections in certain proxy setups (e.g.,\\n# \\\"Connection error\\\" messages), you may want to try adjusting this value.\\n#\\n# Note: When you set this option, Streamlit automatically sets the ping\\n# timeout to match this interval. For Tornado \u003e=6.5, a value less than 30\\n# may cause connection issues.\\nwebsocketPingInterval =\\n\\n# Enable serving files from a `static` directory in the running app's\\n# directory.\\n#\\n# Default: false\\nenableStaticServing = false\\n\\n# TTL in seconds for sessions whose websockets have been disconnected.\\n#\\n# The server may choose to clean up session state, uploaded files, etc\\n# for a given session with no active websocket connection at any point\\n# after this time has passed. If you are using load balancing or\\n# replication in your deployment, you must enable session stickiness\\n# in your proxy to guarantee reconnection to the existing session. For\\n# more information, see https://docs.streamlit.io/replication.\\n#\\n# Default: 120\\ndisconnectedSessionTTL = 120\\n\\n# Server certificate file for connecting via HTTPS.\\n# Must be set at the same time as \\\"server.sslKeyFile\\\".\\n#\\n# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through\\n# security audits or performance tests. For a production environment, we\\n# recommend performing SSL termination through a load balancer or reverse\\n# proxy.']\\nsslCertFile =\\n\\n# Cryptographic key file for connecting via HTTPS.\\n# Must be set at the same time as \\\"server.sslCertFile\\\".\\n#\\n# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through\\n# security audits or performance tests. For a production environment, we\\n# recommend performing SSL termination through a load balancer or reverse\\n# proxy.']\\nsslKeyFile =\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"browser\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#browser\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Browser\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[browser]\\n\\n# Internet address where users should point their browsers in order to\\n# connect to the app. Can be IP address or DNS name and path.\\n#\\n# This is used to:\\n# - Set the correct URL for CORS and XSRF protection purposes.\\n# - Show the URL on the terminal\\n# - Open the browser\\n#\\n# Default: \\\"localhost\\\"\\nserverAddress = \\\"localhost\\\"\\n\\n# Whether to send usage statistics to Streamlit.\\n#\\n# Default: true\\ngatherUsageStats = true\\n\\n# Port where users should point their browsers in order to connect to the\\n# app.\\n#\\n# This is used to:\\n# - Set the correct URL for XSRF protection purposes.\\n# - Show the URL on the terminal (part of `streamlit run`).\\n# - Open the browser automatically (part of `streamlit run`).\\n#\\n# This option is for advanced use cases. To change the port of your app, use\\n# `server.Port` instead.\\n#\\n# Default: whatever value is set in server.port.\\nserverPort = 8501\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"mapbox\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#mapbox\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Mapbox\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[mapbox]\\n\\n# If you'd like to show maps using Mapbox rather than Carto, use this\\n# to pass the Mapbox API token.\\n#\\n# THIS IS DEPRECATED.\\n#\\n# Instead of this, you should use either the MAPBOX_API_KEY environment\\n# variable or PyDeck's `api_keys` argument.\\n#\\n# This option will be removed on or after 2026-05-01.\\n#\\n# Default: \\\"\\\"\\ntoken = \\\"\\\"\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"theme\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#theme\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Theme\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [\"To define switchable light and dark themes, the configuration options in the\\n\", _jsx(_components.code, {\n        children: \"[theme]\"\n      }), \" table can be used in separate \", _jsx(_components.code, {\n        children: \"[theme.dark]\"\n      }), \" and \", _jsx(_components.code, {\n        children: \"[theme.light]\"\n      }), \"\\ntables, except for the following options:\"]\n    }), \"\\n\", _jsxs(_components.ul, {\n      children: [\"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"base\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"fontFaces\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"baseFontSize\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"baseFontWeight\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"showSidebarBorder\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"chartCategoricalColors\"\n        })\n      }), \"\\n\", _jsx(_components.li, {\n        children: _jsx(_components.code, {\n          children: \"chartSequentialColors\"\n        })\n      }), \"\\n\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[theme]\\n\\n# The theme that your custom theme inherits from.\\n#\\n# This can be one of the following:\\n# - \\\"light\\\": Streamlit's default light theme.\\n# - \\\"dark\\\" : Streamlit's default dark theme.\\n# - A local file path to a TOML theme file: A local custom theme, like\\n#   \\\"themes/custom.toml\\\".\\n# - A URL to a TOML theme file: An externally hosted custom theme, like\\n#   \\\"https://example.com/theme.toml\\\".\\n#\\n# A TOML theme file must contain a [theme] table with theme options.\\n# Any theme options defined in the app's config.toml file will override\\n# those defined in the TOML theme file.\\nbase =\\n\\n# Primary accent color.\\nprimaryColor =\\n\\n# Background color of the app.\\nbackgroundColor =\\n\\n# Background color used for most interactive widgets.\\nsecondaryBackgroundColor =\\n\\n# Color used for almost all text.\\ntextColor =\\n\\n# Red color used in the basic color palette.\\n#\\n# By default, this is #ff4b4b for the light theme and #ff2b2b for the\\n# dark theme.\\n#\\n# If `redColor` is provided, and `redBackgroundColor` isn't, then\\n# `redBackgroundColor` will be derived from `redColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nredColor =\\n\\n# Orange color used in the basic color palette.\\n#\\n# By default, this is #ffa421 for the light theme and #ff8700 for the\\n# dark theme.\\n#\\n# If `orangeColor` is provided, and `orangeBackgroundColor` isn't, then\\n# `orangeBackgroundColor` will be derived from `orangeColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\norangeColor =\\n\\n# Yellow color used in the basic color palette.\\n#\\n# By default, this is #faca2b for the light theme and #ffe312 for the\\n# dark theme.\\n#\\n# If `yellowColor` is provided, and `yellowBackgroundColor` isn't, then\\n# `yellowBackgroundColor` will be derived from `yellowColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nyellowColor =\\n\\n# Blue color used in the basic color palette.\\n#\\n# By default, this is #1c83e1 for the light theme and #0068c9 for the\\n# dark theme.\\n#\\n# If a `blueColor` is provided, and `blueBackgroundColor` isn't, then\\n# `blueBackgroundColor` will be derived from `blueColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nblueColor =\\n\\n# Green color used in the basic color palette.\\n#\\n# By default, this is #21c354 for the light theme and #09ab3b for the\\n# dark theme.\\n#\\n# If `greenColor` is provided, and `greenBackgroundColor` isn't, then\\n# `greenBackgroundColor` will be derived from `greenColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\ngreenColor =\\n\\n# Violet color used in the basic color palette.\\n#\\n# By default, this is #803df5 for both the light and dark themes.\\n#\\n# If a `violetColor` is provided, and `violetBackgroundColor` isn't, then\\n# `violetBackgroundColor` will be derived from `violetColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nvioletColor =\\n\\n# Gray color used in the basic color palette.\\n#\\n# By default, this is #a3a8b8 for the light theme and #555867 for the\\n# dark theme.\\n#\\n# If `grayColor` is provided, and `grayBackgroundColor` isn't, then\\n# `grayBackgroundColor` will be derived from `grayColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\ngrayColor =\\n\\n# Red background color used in the basic color palette.\\n#\\n# If `redColor` is provided, this defaults to `redColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ff2b2b with 10% opacity for light theme and\\n# #ff6c6c with 20% opacity for dark theme.\\nredBackgroundColor =\\n\\n# Orange background color used for the basic color palette.\\n#\\n# If `orangeColor` is provided, this defaults to `orangeColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ffa421 with 10% opacity for the light theme and\\n# #ff8700 with 20% opacity for the dark theme.\\norangeBackgroundColor =\\n\\n# Yellow background color used for the basic color palette.\\n#\\n# If `yellowColor` is provided, this defaults to `yellowColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ffff12 with 10% opacity for the light theme and\\n# #ffff12 with 20% opacity for the dark theme.\\nyellowBackgroundColor =\\n\\n# Blue background color used for the basic color palette.\\n#\\n# If `blueColor` is provided, this defaults to `blueColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #1c83ff with 10% opacity for the light theme and\\n# #3d9df3 with 20% opacity for the dark theme.\\nblueBackgroundColor =\\n\\n# Green background color used for the basic color palette.\\n#\\n# If `greenColor` is provided, this defaults to `greenColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #21c354 with 10% opacity for the light theme and\\n# #3dd56d with 20% opacity for the dark theme.\\ngreenBackgroundColor =\\n\\n# Violet background color used for the basic color palette.\\n#\\n# If `violetColor` is provided, this defaults to `violetColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #9a5dff with 10% opacity for light theme and\\n# #9a5dff with 20% opacity for dark theme.\\nvioletBackgroundColor =\\n\\n# Gray background color used for the basic color palette.\\n#\\n# If `grayColor` is provided, this defaults to `grayColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #31333f with 10% opacity for the light theme and\\n# #808495 with 20% opacity for the dark theme.\\ngrayBackgroundColor =\\n\\n# Red text color used for the basic color palette.\\n#\\n# If `redColor` is provided, this defaults to `redColor`, darkened by 15%\\n# for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark\\n# theme.\\nredTextColor =\\n\\n# Orange text color used for the basic color palette.\\n#\\n# If `orangeColor` is provided, this defaults to `orangeColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark\\n# theme.\\norangeTextColor =\\n\\n# Yellow text color used for the basic color palette.\\n#\\n# If `yellowColor` is provided, this defaults to `yellowColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark\\n# theme.\\nyellowTextColor =\\n\\n# Blue text color used for the basic color palette.\\n#\\n# If `blueColor` is provided, this defaults to `blueColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark\\n# theme.\\nblueTextColor =\\n\\n# Green text color used for the basic color palette.\\n#\\n# If `greenColor` is provided, this defaults to `greenColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #158237 for the light theme and #5ce488 for the dark\\n# theme.\\ngreenTextColor =\\n\\n# Violet text color used for the basic color palette.\\n#\\n# If `violetColor` is provided, this defaults to `violetColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #583f84 for the light theme and #b27eff for the dark\\n# theme.\\nvioletTextColor =\\n\\n# Gray text color used for the basic color palette.\\n#\\n# If `grayColor` is provided, this defaults to `grayColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #31333f with 60% opacity for the light theme and\\n# #fafafa with 60% opacity for the dark theme.\\ngrayTextColor =\\n\\n# Color used for all links.\\n#\\n# This defaults to the resolved value of `blueTextColor`.\\nlinkColor =\\n\\n# Whether or not links should be displayed with an underline.\\nlinkUnderline =\\n\\n# Text color used for code blocks.\\n#\\n# This defaults to the resolved value of `greenTextColor`.\\ncodeTextColor =\\n\\n# Background color used for code blocks.\\ncodeBackgroundColor =\\n\\n# The font family for all text, except code blocks.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"Nunito:https://fonts.googleapis.com/css2?family=Nunito\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n#   fallbacks\\n#\\n# For example, you can use the following:\\n#\\n# font = \\\"cool-font, fallback-cool-font, sans-serif\\\"\\nfont =\\n\\n# An array of fonts to use in your app.\\n#\\n# Each font in the array is a table (dictionary) that can have the\\n# following attributes, closely resembling CSS font-face definitions:\\n# - family\\n# - url\\n# - weight (optional)\\n# - style (optional)\\n# - unicodeRange (optional)\\n#\\n# To host a font with your app, enable static file serving with\\n# `server.enableStaticServing=true`.\\n#\\n# You can define multiple [[theme.fontFaces]] tables, including multiple\\n# tables with the same family if your font is defined by multiple files.\\n#\\n# For example, a font hosted with your app may have a [[theme.fontFaces]]\\n# table as follows:\\n#\\n# [[theme.fontFaces]]\\n# family = \\\"font_name\\\"\\n# url = \\\"app/static/font_file.woff\\\"\\n# weight = \\\"400\\\"\\n# style = \\\"normal\\\"\\nfontFaces =\\n\\n# The root font size (in pixels) for the app.\\n#\\n# This determines the overall scale of text and UI elements. This is a\\n# positive integer.\\n#\\n# If this isn't set, the font size will be 16px.\\nbaseFontSize =\\n\\n# The root font weight for the app.\\n#\\n# This determines the overall weight of text and UI elements. This is an\\n# integer multiple of 100. Values can be between 100 and 600, inclusive.\\n#\\n# If this isn't set, the font weight will be set to 400 (normal weight).\\nbaseFontWeight =\\n\\n# The font family to use for headings.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"Nunito:https://fonts.googleapis.com/css2?family=Nunito\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n#   fallbacks\\n#\\n# If this isn't set, Streamlit uses `theme.font` for headings.\\nheadingFont =\\n\\n# One or more font sizes for h1-h6 headings.\\n#\\n# If no sizes are set, Streamlit will use the default sizes for h1-h6\\n# headings. Heading font sizes set in [theme] are not inherited by\\n# [theme.sidebar]. The following sizes are used by default:\\n# [\\n#     \\\"2.75rem\\\", # h1 (1.5rem for sidebar)\\n#     \\\"2.25rem\\\", # h2 (1.25rem for sidebar)\\n#     \\\"1.75rem\\\", # h3 (1.125rem for sidebar)\\n#     \\\"1.5rem\\\", # h4 (1rem for sidebar)\\n#     \\\"1.25rem\\\", # h5 (0.875rem for sidebar)\\n#     \\\"1rem\\\", # h6 (0.75rem for sidebar)\\n# ]\\n#\\n# If you specify an array with fewer than six sizes, the unspecified\\n# heading sizes will be the default values. For example, you can use the\\n# following array to set the font sizes for h1-h3 headings while keeping\\n# h4-h6 headings at their default sizes:\\n# headingFontSizes = [\\\"3rem\\\", \\\"2.875rem\\\", \\\"2.75rem\\\"]\\n#\\n# Setting a single value (not in an array) will set the font size for all\\n# h1-h6 headings to that value:\\n# headingFontSizes = \\\"2.75rem\\\"\\n#\\n# Font sizes can be specified in pixels or rem, but rem is recommended.\\nheadingFontSizes =\\n\\n# One or more font weights for h1-h6 headings.\\n#\\n# If no weights are set, Streamlit will use the default weights for h1-h6\\n# headings. Heading font weights set in [theme] are not inherited by\\n# [theme.sidebar]. The following weights are used by default:\\n# [\\n#     700, # h1 (bold)\\n#     600, # h2 (semi-bold)\\n#     600, # h3 (semi-bold)\\n#     600, # h4 (semi-bold)\\n#     600, # h5 (semi-bold)\\n#     600, # h6 (semi-bold)\\n# ]\\n#\\n# If you specify an array with fewer than six weights, the unspecified\\n# heading weights will be the default values. For example, you can use\\n# the following array to set the font weights for h1-h2 headings while\\n# keeping h3-h6 headings at their default weights:\\n# headingFontWeights = [800, 700]\\n#\\n# Setting a single value (not in an array) will set the font weight for\\n# all h1-h6 headings to that value:\\n# headingFontWeights = 500\\nheadingFontWeights =\\n\\n# The font family to use for code (monospace) in the sidebar.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n#   fallbacks\\ncodeFont =\\n\\n# The font size (in pixels or rem) for code blocks and code text.\\n#\\n# This applies to font in code blocks, `st.json`, and `st.help`. It\\n# doesn't apply to inline code, which is set by default to 0.75em.\\n#\\n# If this isn't set, the code font size will be 0.875rem.\\ncodeFontSize =\\n\\n# The font weight for code blocks and code text.\\n#\\n# This applies to font in inline code, code blocks, `st.json`, and\\n# `st.help`. This is an integer multiple of 100. Values can be between\\n# 100 and 600, inclusive.\\n#\\n# If this isn't set, the code font weight will be 400 (normal weight).\\ncodeFontWeight =\\n\\n# The radius used as basis for the corners of most UI elements.\\n#\\n# This can be one of the following:\\n# - \\\"none\\\"\\n# - \\\"small\\\"\\n# - \\\"medium\\\"\\n# - \\\"large\\\"\\n# - \\\"full\\\"\\n# - The number in pixels or rem.\\n#\\n# For example, you can use \\\"10px\\\", \\\"0.5rem\\\", or \\\"2rem\\\". To follow best\\n# practices, use rem instead of pixels when specifying a numeric size.\\nbaseRadius =\\n\\n# The radius used as basis for the corners of buttons.\\n#\\n# This can be one of the following:\\n# - \\\"none\\\"\\n# - \\\"small\\\"\\n# - \\\"medium\\\"\\n# - \\\"large\\\"\\n# - \\\"full\\\"\\n# - The number in pixels or rem.\\n#\\n# For example, you can use \\\"10px\\\", \\\"0.5rem\\\", or \\\"2rem\\\". To follow best\\n# practices, use rem instead of pixels when specifying a numeric size.\\n#\\n# If this isn't set, Streamlit uses `theme.baseRadius` instead.\\nbuttonRadius =\\n\\n# The color of the border around elements.\\nborderColor =\\n\\n# The color of the border around dataframes and tables.\\n#\\n# If this isn't set, Streamlit uses `theme.borderColor` instead.\\ndataframeBorderColor =\\n\\n# The background color of the dataframe's header.\\n#\\n# This color applies to all non-interior cells of the dataframe. This\\n# includes the header row, the row-selection column (if present), and\\n# the bottom row of data editors with a dynamic number of rows. If this\\n# isn't set, Streamlit uses a mix of `theme.backgroundColor` and\\n# `theme.secondaryBackgroundColor`.\\ndataframeHeaderBackgroundColor =\\n\\n# Whether to show a border around input widgets.\\nshowWidgetBorder =\\n\\n# Whether to show a vertical separator between the sidebar and the main\\n# content area.\\nshowSidebarBorder =\\n\\n# An array of colors to use for categorical chart data.\\n#\\n# This is a list of one or more color strings which are applied in order\\n# to categorical data. These colors apply to Plotly, Altair, and\\n# Vega-Lite charts.\\n#\\n# Invalid colors are skipped, and colors repeat cyclically if there are\\n# more categories than colors. If no chart categorical colors are set,\\n# Streamlit uses a default set of colors.\\n#\\n# For light themes, the following colors are the default:\\n# [\\n#     \\\"#0068c9\\\", # blue80\\n#     \\\"#83c9ff\\\", # blue40\\n#     \\\"#ff2b2b\\\", # red80\\n#     \\\"#ffabab\\\", # red40\\n#     \\\"#29b09d\\\", # blueGreen80\\n#     \\\"#7defa1\\\", # green40\\n#     \\\"#ff8700\\\", # orange80\\n#     \\\"#ffd16a\\\", # orange50\\n#     \\\"#6d3fc0\\\", # purple80\\n#     \\\"#d5dae5\\\", # gray40\\n# ]\\n# For dark themes, the following colors are the default:\\n# [\\n#     \\\"#83c9ff\\\", # blue40\\n#     \\\"#0068c9\\\", # blue80\\n#     \\\"#ffabab\\\", # red40\\n#     \\\"#ff2b2b\\\", # red80\\n#     \\\"#7defa1\\\", # green40\\n#     \\\"#29b09d\\\", # blueGreen80\\n#     \\\"#ffd16a\\\", # orange50\\n#     \\\"#ff8700\\\", # orange80\\n#     \\\"#6d3fc0\\\", # purple80\\n#     \\\"#d5dae5\\\", # gray40\\n# ]\\nchartCategoricalColors =\\n\\n# An array of ten colors to use for sequential or continuous chart data.\\n#\\n# The ten colors create a gradient color scale. These colors apply to\\n# Plotly, Altair, and Vega-Lite charts.\\n#\\n# Invalid color strings are skipped. If there are not exactly ten\\n# valid colors specified, Streamlit uses a default set of colors.\\n#\\n# For light themes, the following colors are the default:\\n# [\\n#     \\\"#e4f5ff\\\", #blue10\\n#     \\\"#c7ebff\\\", #blue20\\n#     \\\"#a6dcff\\\", #blue30\\n#     \\\"#83c9ff\\\", #blue40\\n#     \\\"#60b4ff\\\", #blue50\\n#     \\\"#3d9df3\\\", #blue60\\n#     \\\"#1c83e1\\\", #blue70\\n#     \\\"#0068c9\\\", #blue80\\n#     \\\"#0054a3\\\", #blue90\\n#     \\\"#004280\\\", #blue100\\n# ]\\n# For dark themes, the following colors are the default:\\n# [\\n#     \\\"#004280\\\", #blue100\\n#     \\\"#0054a3\\\", #blue90\\n#     \\\"#0068c9\\\", #blue80\\n#     \\\"#1c83e1\\\", #blue70\\n#     \\\"#3d9df3\\\", #blue60\\n#     \\\"#60b4ff\\\", #blue50\\n#     \\\"#83c9ff\\\", #blue40\\n#     \\\"#a6dcff\\\", #blue30\\n#     \\\"#c7ebff\\\", #blue20\\n#     \\\"#e4f5ff\\\", #blue10\\n# ]\\nchartSequentialColors =\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"sidebar-theme\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#sidebar-theme\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Sidebar theme\"]\n    }), \"\\n\", _jsxs(_components.p, {\n      children: [\"To define switchable light and dark themes, the configuration options in the\\n\", _jsx(_components.code, {\n        children: \"[theme.sidebar]\"\n      }), \" table can be used in separate \", _jsx(_components.code, {\n        children: \"[theme.dark.sidebar]\"\n      }), \" and\\n\", _jsx(_components.code, {\n        children: \"[theme.light.sidebar]\"\n      }), \".\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[theme.sidebar]\\n\\n# Primary accent color.\\nprimaryColor =\\n\\n# Background color of the app.\\nbackgroundColor =\\n\\n# Background color used for most interactive widgets.\\nsecondaryBackgroundColor =\\n\\n# Color used for almost all text.\\ntextColor =\\n\\n# Red color used in the basic color palette.\\n#\\n# By default, this is #ff4b4b for the light theme and #ff2b2b for the\\n# dark theme.\\n#\\n# If `redColor` is provided, and `redBackgroundColor` isn't, then\\n# `redBackgroundColor` will be derived from `redColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nredColor =\\n\\n# Orange color used in the basic color palette.\\n#\\n# By default, this is #ffa421 for the light theme and #ff8700 for the\\n# dark theme.\\n#\\n# If `orangeColor` is provided, and `orangeBackgroundColor` isn't, then\\n# `orangeBackgroundColor` will be derived from `orangeColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\norangeColor =\\n\\n# Yellow color used in the basic color palette.\\n#\\n# By default, this is #faca2b for the light theme and #ffe312 for the\\n# dark theme.\\n#\\n# If `yellowColor` is provided, and `yellowBackgroundColor` isn't, then\\n# `yellowBackgroundColor` will be derived from `yellowColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nyellowColor =\\n\\n# Blue color used in the basic color palette.\\n#\\n# By default, this is #1c83e1 for the light theme and #0068c9 for the\\n# dark theme.\\n#\\n# If a `blueColor` is provided, and `blueBackgroundColor` isn't, then\\n# `blueBackgroundColor` will be derived from `blueColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nblueColor =\\n\\n# Green color used in the basic color palette.\\n#\\n# By default, this is #21c354 for the light theme and #09ab3b for the\\n# dark theme.\\n#\\n# If `greenColor` is provided, and `greenBackgroundColor` isn't, then\\n# `greenBackgroundColor` will be derived from `greenColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\ngreenColor =\\n\\n# Violet color used in the basic color palette.\\n#\\n# By default, this is #803df5 for both the light and dark themes.\\n#\\n# If a `violetColor` is provided, and `violetBackgroundColor` isn't, then\\n# `violetBackgroundColor` will be derived from `violetColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\nvioletColor =\\n\\n# Gray color used in the basic color palette.\\n#\\n# By default, this is #a3a8b8 for the light theme and #555867 for the\\n# dark theme.\\n#\\n# If `grayColor` is provided, and `grayBackgroundColor` isn't, then\\n# `grayBackgroundColor` will be derived from `grayColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\ngrayColor =\\n\\n# Red background color used in the basic color palette.\\n#\\n# If `redColor` is provided, this defaults to `redColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ff2b2b with 10% opacity for light theme and\\n# #ff6c6c with 20% opacity for dark theme.\\nredBackgroundColor =\\n\\n# Orange background color used for the basic color palette.\\n#\\n# If `orangeColor` is provided, this defaults to `orangeColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ffa421 with 10% opacity for the light theme and\\n# #ff8700 with 20% opacity for the dark theme.\\norangeBackgroundColor =\\n\\n# Yellow background color used for the basic color palette.\\n#\\n# If `yellowColor` is provided, this defaults to `yellowColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #ffff12 with 10% opacity for the light theme and\\n# #ffff12 with 20% opacity for the dark theme.\\nyellowBackgroundColor =\\n\\n# Blue background color used for the basic color palette.\\n#\\n# If `blueColor` is provided, this defaults to `blueColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #1c83ff with 10% opacity for the light theme and\\n# #3d9df3 with 20% opacity for the dark theme.\\nblueBackgroundColor =\\n\\n# Green background color used for the basic color palette.\\n#\\n# If `greenColor` is provided, this defaults to `greenColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #21c354 with 10% opacity for the light theme and\\n# #3dd56d with 20% opacity for the dark theme.\\ngreenBackgroundColor =\\n\\n# Violet background color used for the basic color palette.\\n#\\n# If `violetColor` is provided, this defaults to `violetColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #9a5dff with 10% opacity for light theme and\\n# #9a5dff with 20% opacity for dark theme.\\nvioletBackgroundColor =\\n\\n# Gray background color used for the basic color palette.\\n#\\n# If `grayColor` is provided, this defaults to `grayColor` using 10%\\n# opacity for the light theme and 20% opacity for the dark theme.\\n#\\n# Otherwise, this is #31333f with 10% opacity for the light theme and\\n# #808495 with 20% opacity for the dark theme.\\ngrayBackgroundColor =\\n\\n# Red text color used for the basic color palette.\\n#\\n# If `redColor` is provided, this defaults to `redColor`, darkened by 15%\\n# for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #bd4043 for the light theme and #ff6c6c for the dark\\n# theme.\\nredTextColor =\\n\\n# Orange text color used for the basic color palette.\\n#\\n# If `orangeColor` is provided, this defaults to `orangeColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #e2660c for the light theme and #ffbd45 for the dark\\n# theme.\\norangeTextColor =\\n\\n# Yellow text color used for the basic color palette.\\n#\\n# If `yellowColor` is provided, this defaults to `yellowColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #926c05 for the light theme and #ffffc2 for the dark\\n# theme.\\nyellowTextColor =\\n\\n# Blue text color used for the basic color palette.\\n#\\n# If `blueColor` is provided, this defaults to `blueColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #0054a3 for the light theme and #3d9df3 for the dark\\n# theme.\\nblueTextColor =\\n\\n# Green text color used for the basic color palette.\\n#\\n# If `greenColor` is provided, this defaults to `greenColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #158237 for the light theme and #5ce488 for the dark\\n# theme.\\ngreenTextColor =\\n\\n# Violet text color used for the basic color palette.\\n#\\n# If `violetColor` is provided, this defaults to `violetColor`, darkened\\n# by 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #583f84 for the light theme and #b27eff for the dark\\n# theme.\\nvioletTextColor =\\n\\n# Gray text color used for the basic color palette.\\n#\\n# If `grayColor` is provided, this defaults to `grayColor`, darkened by\\n# 15% for the light theme and lightened by 15% for the dark theme.\\n#\\n# Otherwise, this is #31333f with 60% opacity for the light theme and\\n# #fafafa with 60% opacity for the dark theme.\\ngrayTextColor =\\n\\n# Color used for all links.\\n#\\n# This defaults to the resolved value of `blueTextColor`.\\nlinkColor =\\n\\n# Whether or not links should be displayed with an underline.\\nlinkUnderline =\\n\\n# Text color used for code blocks.\\n#\\n# This defaults to the resolved value of `greenTextColor`.\\ncodeTextColor =\\n\\n# Background color used for code blocks.\\ncodeBackgroundColor =\\n\\n# The font family for all text, except code blocks.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"Nunito:https://fonts.googleapis.com/css2?family=Nunito\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n#   fallbacks\\n#\\n# For example, you can use the following:\\n#\\n# font = \\\"cool-font, fallback-cool-font, sans-serif\\\"\\nfont =\\n\\n# The font family to use for headings.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"Nunito:https://fonts.googleapis.com/css2?family=Nunito\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n#   fallbacks\\n#\\n# If this isn't set, Streamlit uses `theme.font` for headings.\\nheadingFont =\\n\\n# One or more font sizes for h1-h6 headings.\\n#\\n# If no sizes are set, Streamlit will use the default sizes for h1-h6\\n# headings. Heading font sizes set in [theme] are not inherited by\\n# [theme.sidebar]. The following sizes are used by default:\\n# [\\n#     \\\"2.75rem\\\", # h1 (1.5rem for sidebar)\\n#     \\\"2.25rem\\\", # h2 (1.25rem for sidebar)\\n#     \\\"1.75rem\\\", # h3 (1.125rem for sidebar)\\n#     \\\"1.5rem\\\", # h4 (1rem for sidebar)\\n#     \\\"1.25rem\\\", # h5 (0.875rem for sidebar)\\n#     \\\"1rem\\\", # h6 (0.75rem for sidebar)\\n# ]\\n#\\n# If you specify an array with fewer than six sizes, the unspecified\\n# heading sizes will be the default values. For example, you can use the\\n# following array to set the font sizes for h1-h3 headings while keeping\\n# h4-h6 headings at their default sizes:\\n# headingFontSizes = [\\\"3rem\\\", \\\"2.875rem\\\", \\\"2.75rem\\\"]\\n#\\n# Setting a single value (not in an array) will set the font size for all\\n# h1-h6 headings to that value:\\n# headingFontSizes = \\\"2.75rem\\\"\\n#\\n# Font sizes can be specified in pixels or rem, but rem is recommended.\\nheadingFontSizes =\\n\\n# One or more font weights for h1-h6 headings.\\n#\\n# If no weights are set, Streamlit will use the default weights for h1-h6\\n# headings. Heading font weights set in [theme] are not inherited by\\n# [theme.sidebar]. The following weights are used by default:\\n# [\\n#     700, # h1 (bold)\\n#     600, # h2 (semi-bold)\\n#     600, # h3 (semi-bold)\\n#     600, # h4 (semi-bold)\\n#     600, # h5 (semi-bold)\\n#     600, # h6 (semi-bold)\\n# ]\\n#\\n# If you specify an array with fewer than six weights, the unspecified\\n# heading weights will be the default values. For example, you can use\\n# the following array to set the font weights for h1-h2 headings while\\n# keeping h3-h6 headings at their default weights:\\n# headingFontWeights = [800, 700]\\n#\\n# Setting a single value (not in an array) will set the font weight for\\n# all h1-h6 headings to that value:\\n# headingFontWeights = 500\\nheadingFontWeights =\\n\\n# The font family to use for code (monospace) in the sidebar.\\n#\\n# This can be one of the following:\\n# - \\\"sans-serif\\\"\\n# - \\\"serif\\\"\\n# - \\\"monospace\\\"\\n# - The `family` value for a custom font table under [[theme.fontFaces]]\\n# - A URL to a CSS file in the format of \\\"\u003cfont name\u003e:\u003curl\u003e\\\" (like\\n#   \\\"'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono\u0026display=swap\\\")\\n# - A comma-separated list of these (as a single string) to specify\\n# fallbacks\\ncodeFont =\\n\\n# The font size (in pixels or rem) for code blocks and code text.\\n#\\n# This applies to font in code blocks, `st.json`, and `st.help`. It\\n# doesn't apply to inline code, which is set by default to 0.75em.\\n#\\n# If this isn't set, the code font size will be 0.875rem.\\ncodeFontSize =\\n\\n# The font weight for code blocks and code text.\\n#\\n# This applies to font in inline code, code blocks, `st.json`, and\\n# `st.help`. This is an integer multiple of 100. Values can be between\\n# 100 and 600, inclusive.\\n#\\n# If this isn't set, the code font weight will be 400 (normal weight).\\ncodeFontWeight =\\n\\n# The radius used as basis for the corners of most UI elements.\\n#\\n# This can be one of the following:\\n# - \\\"none\\\"\\n# - \\\"small\\\"\\n# - \\\"medium\\\"\\n# - \\\"large\\\"\\n# - \\\"full\\\"\\n# - The number in pixels or rem.\\n#\\n# For example, you can use \\\"10px\\\", \\\"0.5rem\\\", or \\\"2rem\\\". To follow best\\n# practices, use rem instead of pixels when specifying a numeric size.\\nbaseRadius =\\n\\n# The radius used as basis for the corners of buttons.\\n#\\n# This can be one of the following:\\n# - \\\"none\\\"\\n# - \\\"small\\\"\\n# - \\\"medium\\\"\\n# - \\\"large\\\"\\n# - \\\"full\\\"\\n# - The number in pixels or rem.\\n#\\n# For example, you can use \\\"10px\\\", \\\"0.5rem\\\", or \\\"2rem\\\". To follow best\\n# practices, use rem instead of pixels when specifying a numeric size.\\n#\\n# If this isn't set, Streamlit uses `theme.baseRadius` instead.\\nbuttonRadius =\\n\\n# The color of the border around elements.\\nborderColor =\\n\\n# The color of the border around dataframes and tables.\\n#\\n# If this isn't set, Streamlit uses `theme.borderColor` instead.\\ndataframeBorderColor =\\n\\n# The background color of the dataframe's header.\\n#\\n# This color applies to all non-interior cells of the dataframe. This\\n# includes the header row, the row-selection column (if present), and\\n# the bottom row of data editors with a dynamic number of rows. If this\\n# isn't set, Streamlit uses a mix of `theme.backgroundColor` and\\n# `theme.secondaryBackgroundColor`.\\ndataframeHeaderBackgroundColor =\\n\\n# Whether to show a border around input widgets.\\nshowWidgetBorder =\\n\"\n      })\n    }), \"\\n\", _jsxs(_components.h4, {\n      id: \"secrets\",\n      children: [_jsx(_components.a, {\n        \"aria-hidden\": \"true\",\n        tabIndex: \"-1\",\n        href: \"#secrets\",\n        children: _jsx(_components.span, {\n          className: \"icon icon-link\"\n        })\n      }), \"Secrets\"]\n    }), \"\\n\", _jsx(_components.pre, {\n      children: _jsx(_components.code, {\n        className: \"language-toml\",\n        children: \"[secrets]\\n\\n# List of locations where secrets are searched.\\n#\\n# An entry can be a path to a TOML file or directory path where\\n# Kubernetes style secrets are saved. Order is important, import is\\n# first to last, so secrets in later files will take precedence over\\n# earlier ones.\\n#\\n# Default: [ \u003cpath to local environment's secrets.toml file\u003e, \u003cpath to project's secrets.toml file\u003e,]\\nfiles = [ \\\"~/.streamlit/secrets.toml\\\", \\\"~/project directory/.streamlit/secrets.toml\\\",]\\n\"\n      })\n    })]\n  });\n}\nfunction MDXContent(props = {}) {\n  const {wrapper: MDXLayout} = Object.assign({}, _provideComponents(), props.components);\n  return MDXLayout ? _jsx(MDXLayout, Object.assign({}, props, {\n    children: _jsx(_createMdxContent, props)\n  })) : _createMdxContent(props);\n}\nreturn {\n  default: MDXContent\n};\n","frontmatter":{},"scope":{"title":"config.toml","slug":"/develop/api-reference/configuration/config.toml","description":"Complete reference guide for Streamlit's config.toml configuration file, including all available sections and options for customizing your Streamlit application settings.","keywords":"config.toml, streamlit configuration, toml configuration file, streamlit settings, theme configuration, server configuration, client configuration, logger configuration, browser configuration, mapbox configuration, secrets configuration, sidebar theme, configuration options, streamlit config show"}},"currMenuItem":{"name":"config.toml","url":"/develop/api-reference/configuration/config.toml","isVersioned":false},"prevMenuItem":{"menu_key":"Configuration","name":"Configuration","depth":"2","children":[{"menu_key":"config.toml","name":"config.toml","depth":"3","children":[],"category":"Develop / API reference / Configuration / config.toml","url":"/develop/api-reference/configuration/config.toml"},{"menu_key":"st.get_option","name":"st.get_option","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.get_option","url":"/develop/api-reference/configuration/st.get_option","isVersioned":true},{"menu_key":"st.set_option","name":"st.set_option","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.set_option","url":"/develop/api-reference/configuration/st.set_option","isVersioned":true},{"menu_key":"st.set_page_config","name":"st.set_page_config","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.set_page_config","url":"/develop/api-reference/configuration/st.set_page_config","isVersioned":true}],"category":"Develop / API reference / Configuration","url":"/develop/api-reference/configuration","isVersioned":false},"nextMenuItem":{"menu_key":"st.get_option","name":"st.get_option","depth":"3","children":[],"category":"Develop / API reference / Configuration / st.get_option","url":"/develop/api-reference/configuration/st.get_option","isVersioned":true}},"__N_SSG":true},"page":"/[...slug]","query":{"slug":["develop","api-reference","configuration","config.toml"]},"buildId":"Zwhy24kJ8WALZgyY-V3Bw","runtimeConfig":{"VERSIONS_LIST":["1.52.0","1.51.0","1.50.0","1.49.0","1.48.0","1.47.0","1.46.0","1.45.0","1.44.0","1.43.0","1.42.0","1.41.0","1.40.0","1.39.0","1.38.0","1.37.0","1.36.0","1.35.0","1.34.0","1.33.0","1.32.0","1.31.0","1.30.0","1.29.0","1.28.0","1.27.0","1.26.0","1.25.0","1.24.0","1.23.0","1.22.0"],"LATEST_VERSION":"1.52.0","DEFAULT_VERSION":"latest","PLATFORM_VERSIONS":{},"PLATFORM_LATEST_VERSIONS":{},"PLATFORM_NAMES":{"oss":"All versions","sis":"Streamlit in Snowflake","na":"Snowflake Native Apps"},"DEFAULT_PLATFORM":"oss"},"isFallback":false,"gsp":true,"scriptLoader":[]}</script></body></html>