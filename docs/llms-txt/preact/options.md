# Source: https://preactjs.com/guide/v10/options

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Option Hooks – Preact Guide</title>
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
	<meta name="description" content="Preact has several option hooks that allow you to attach callbacks to various stages of the diffing process">
<meta property="og:url" content="https://preactjs.com/guide/v10/options">
<meta property="og:title" content="Option Hooks – Preact Guide">
<meta property="og:description" content="Preact has several option hooks that allow you to attach callbacks to various stages of the diffing process">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/options.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/options.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/options" can-edit><div class="markup"><h1>Option Hooks</h1><p>Callbacks for plugins that can change Preact's rendering.</p>
<p>Preact supports a number of different callbacks that can be used to observe or change each stage of the rendering process, commonly referred to as &quot;Option Hooks&quot; (not to be confused with <a href="/guide/v10/hooks">hooks</a>). These are frequently used to extend the feature-set of Preact itself, or to create specialized testing tools. All of our addons like <code>preact/hooks</code>, <code>preact/compat</code> and our devtools extension are based on these callbacks.</p>
<p>This API is primarily intended for tooling or library authors who wish to extend Preact.</p>
<hr>
<nav><ul><li><a href="#versioning-and-support">Versioning and Support</a></li><li><a href="#setting-option-hooks">Setting Option Hooks</a></li><li><a href="#available-option-hooks">Available Option Hooks</a></li></ul></nav><hr>

				<h2 id="versioning-and-support">
					<a class="fragment-link" href="#versioning-and-support">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Versioning and Support (#versioning-and-support)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Versioning and Support</span>
				</h2><p>Option Hooks are shipped in Preact, and as such are semantically versioned. However, they do not have the same deprecation policy, which means major versions can change the API without an extended announcement period leading up to release. This is also true for the structure of internal APIs exposed through Options Hooks, like <code>VNode</code> objects.</p>

				<h2 id="setting-option-hooks">
					<a class="fragment-link" href="#setting-option-hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Setting Option Hooks (#setting-option-hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Setting Option Hooks</span>
				</h2><p>You can set Options Hooks in Preact by modifying the exported <code>options</code> object.</p>
<p>When defining a hook, always make sure to call a previously defined hook of that name if there was one. Without this, the callchain will be broken and code that depends on the previously-installed hook will break, resulting in addons like <code>preact/hooks</code> or DevTools ceasing to work. Make sure to pass the same arguments to the original hook, too - unless you have a specific reason to change them.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-js"><span class="token keyword">import</span> <span class="token punctuation">{</span> options <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact'</span><span class="token punctuation">;</span>

<span class="token comment">// Store previous hook</span>
<span class="token keyword">const</span> oldHook <span class="token operator">=</span> options<span class="token punctuation">.</span>vnode<span class="token punctuation">;</span>

<span class="token comment">// Set our own options hook</span>
options<span class="token punctuation">.</span><span class="token function-variable function">vnode</span> <span class="token operator">=</span> <span class="token parameter">vnode</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
	console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">&quot;Hey I'm a vnode&quot;</span><span class="token punctuation">,</span> vnode<span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token comment">// Call previously defined hook if there was any</span>
	<span class="token keyword">if</span> <span class="token punctuation">(</span>oldHook<span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token function">oldHook</span><span class="token punctuation">(</span>vnode<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>None of the currently available hooks excluding <code>options.event</code> have return values, so handling return values from the original hook is not necessary.</p>

				<h2 id="available-option-hooks">
					<a class="fragment-link" href="#available-option-hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Available Option Hooks (#available-option-hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Available Option Hooks</span>
				</h2>
				<h4 id="optionsvnode">
					<a class="fragment-link" href="#optionsvnode">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.vnode` (#optionsvnode)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.vnode`</span>
				</h4><p><strong>Signature:</strong> <code>(vnode: VNode) => void</code></p>
<p>The most common Options Hook, <code>vnode</code> is invoked whenever a VNode object is created. VNodes are Preact's representation of Virtual DOM elements, commonly thought of as &quot;JSX Elements&quot;.</p>

				<h4 id="optionsunmount">
					<a class="fragment-link" href="#optionsunmount">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.unmount` (#optionsunmount)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.unmount`</span>
				</h4><p><strong>Signature:</strong> <code>(vnode: VNode) => void</code></p>
<p>Invoked immediately before a vnode is unmounted, when its DOM representation is still attached.</p>

				<h4 id="optionsdiffed">
					<a class="fragment-link" href="#optionsdiffed">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.diffed` (#optionsdiffed)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.diffed`</span>
				</h4><p><strong>Signature:</strong> <code>(vnode: VNode) => void</code></p>
<p>Invoked immediately after a vnode is rendered, once its DOM representation is constructed or transformed into the correct state.</p>

				<h4 id="optionsevent">
					<a class="fragment-link" href="#optionsevent">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.event` (#optionsevent)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.event`</span>
				</h4><p><strong>Signature:</strong> <code>(event: Event) => any</code></p>
<p>Invoked just before a DOM event is handled by its associated Virtual DOM listener. When <code>options.event</code> is set, the event which is event listener argument is replaced return value of <code>options.event</code>.</p>

				<h4 id="optionsrequestanimationframe">
					<a class="fragment-link" href="#optionsrequestanimationframe">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.requestAnimationFrame` (#optionsrequestanimationframe)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.requestAnimationFrame`</span>
				</h4><p><strong>Signature:</strong> <code>(callback: () => void) => void</code></p>
<p>Controls the scheduling of effects and effect-based based functionality in <code>preact/hooks</code>.</p>

				<h4 id="optionsdebouncerendering">
					<a class="fragment-link" href="#optionsdebouncerendering">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.debounceRendering` (#optionsdebouncerendering)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.debounceRendering`</span>
				</h4><p><strong>Signature:</strong> <code>(callback: () => void) => void</code></p>
<p>A timing &quot;deferral&quot; function that is used to batch processing of updates in the global component rendering queue.</p>
<p>By default, Preact uses a zero duration <code>setTimeout</code>.</p>

				<h4 id="optionsusedebugvalue">
					<a class="fragment-link" href="#optionsusedebugvalue">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: `options.useDebugValue` (#optionsusedebugvalue)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>`options.useDebugValue`</span>
				</h4><p><strong>Signature:</strong> <code>(value: string | number) => void</code></p>
<p>Called when the <code>useDebugValue</code> hook in <code>preact/hooks</code> is called.</p>
</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/Almo7aya" target="_blank" rel="noopener noreferrer">@Almo7aya</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
