# Source: https://preactjs.com/repl?example=todo-signals

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>REPL: Try Preact in the browser – Preact</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, minimal-ui">
		<meta name="color-scheme" content="dark light">
		<meta name="theme-color" content="#673AB8">
		<link rel="alternate" type="application/rss+xml" href="https://preactjs.com/feed.xml">
		<link rel="alternate" type="application/atom+xml" href="https://preactjs.com/feed.atom">
		<meta property="og:image" content="https://preactjs.com/app-icon.png">
		<meta name="twitter:card" content="summary">
		<link href="https://esm.sh" rel="preconnect" crossorigin="anonymous">
		<link href="https://www.google-analytics.com" rel="preconnect" crossorigin="anonymous">
		<script type="module" crossorigin src="/assets/index-nodqeQT7.js"></script>
		<link rel="stylesheet" crossorigin href="/assets/index-CzbcAXL9.css">
	<meta name="description" content="Try Preact instantly using our simple in-browser editor / IDE">
<meta property="og:url" content="https://preactjs.com/repl">
<meta property="og:title" content="REPL: Try Preact in the browser – Preact">
<meta property="og:description" content="Try Preact instantly using our simple in-browser editor / IDE">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/repl.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl" class="_current_nxrmc_92 ">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><!--$s--><div class="_repl_1tb0j_1"><style>
				main {
					height: 100% !important;
					overflow: hidden !important;
				}
			</style></div><!--/$s--><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
