# Source: https://preactjs.com/guide/v10/web-components

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Web Components – Preact Guide</title>
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
	<meta name="description" content="How to use web components with Preact">
<meta property="og:url" content="https://preactjs.com/guide/v10/web-components">
<meta property="og:title" content="Web Components – Preact Guide">
<meta property="og:description" content="How to use web components with Preact">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/web-components.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/web-components.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/web-components" can-edit><div class="markup"><h1>Web Components</h1><p>Web Components are a set of different technologies that allow you to create reusable, encapsulated custom HTML elements that are entirely framework-agnostic. Examples of Web Components include elements like <code>&lt;material-card></code> or <code>&lt;tab-bar></code>.</p>
<p>As a platform primitive, Preact <a href="https://custom-elements-everywhere.com/#preact" target="_blank" rel="noopener noreferrer">fully supports Web Components</a>, allowing seamless use of Custom Element lifecycles, properties, and events in your Preact apps.</p>
<p>Preact and Web Components are complementary technologies: Web Components provide a set of low-level primitives for extending the browser, and Preact provides a high-level component model that can sit atop those primitives.</p>
<hr>
<nav><ul><li><a href="#rendering-web-components">Rendering Web Components</a><ul><li><a href="#properties-and-attributes">Properties and Attributes</a></li><li><a href="#accessing-instance-methods">Accessing Instance Methods</a></li><li><a href="#triggering-custom-events">Triggering custom events</a></li></ul></li></ul></nav><hr>

				<h2 id="rendering-web-components">
					<a class="fragment-link" href="#rendering-web-components">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Rendering Web Components (#rendering-web-components)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Rendering Web Components</span>
				</h2><p>In Preact, web components work just like other DOM Elements. They can be rendered using their registered tag name:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx">customElements<span class="token punctuation">.</span><span class="token function">define</span><span class="token punctuation">(</span>
	<span class="token string">'x-foo'</span><span class="token punctuation">,</span>
	<span class="token keyword">class</span> <span class="token class-name">extends</span> HTMLElement <span class="token punctuation">{</span>
		<span class="token comment">// ...</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>x-foo</span> <span class="token punctuation">/></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="properties-and-attributes">
					<a class="fragment-link" href="#properties-and-attributes">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Properties and Attributes (#properties-and-attributes)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Properties and Attributes</span>
				</h3><p>JSX does not provide a way to differentiate between properties and attributes. Custom Elements generally rely on custom properties in order to support setting complex values that can't be expressed as attributes. This works well in Preact, because the renderer automatically determines whether to set values using a property or attribute by inspecting the affected DOM element. When a Custom Element defines a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set" target="_blank" rel="noopener noreferrer">setter</a> for a given property, Preact detects its existence and will use the setter instead of an attribute.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx">customElements<span class="token punctuation">.</span><span class="token function">define</span><span class="token punctuation">(</span>
	<span class="token string">'context-menu'</span><span class="token punctuation">,</span>
	<span class="token keyword">class</span> <span class="token class-name">extends</span> HTMLElement <span class="token punctuation">{</span>
		<span class="token keyword">set</span> <span class="token function">position</span><span class="token punctuation">(</span><span class="token parameter"><span class="token punctuation">{</span> x<span class="token punctuation">,</span> y <span class="token punctuation">}</span></span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
			<span class="token keyword">this</span><span class="token punctuation">.</span>style<span class="token punctuation">.</span>cssText <span class="token operator">=</span> <span class="token template-string"><span class="token template-punctuation string">`</span><span class="token string">left:</span><span class="token interpolation"><span class="token interpolation-punctuation punctuation">${</span>x<span class="token interpolation-punctuation punctuation">}</span></span><span class="token string">px; top:</span><span class="token interpolation"><span class="token interpolation-punctuation punctuation">${</span>y<span class="token interpolation-punctuation punctuation">}</span></span><span class="token string">px;</span><span class="token template-punctuation string">`</span></span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>context-menu</span> <span class="token attr-name">position</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">x</span><span class="token operator">:</span> <span class="token number">10</span><span class="token punctuation">,</span> <span class="token literal-property property">y</span><span class="token operator">:</span> <span class="token number">20</span> <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text"> ... </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>context-menu</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<blockquote>
<p><strong>Note:</strong> Preact makes no assumptions over naming schemes and will not attempt to coerce names, in JSX or otherwise, to DOM properties. If a custom element has a property name <code>someProperty</code>, then it will need to be set using that exact same capitalization and spelling (<code>someProperty=...</code>). <code>someproperty=...</code> or <code>some-property=...</code> will not work.</p>
</blockquote>
<p>When rendering static HTML using <code>preact-render-to-string</code> (&quot;SSR&quot;), complex property values like the object above are not automatically serialized. They are applied once the static HTML is hydrated on the client.</p>

				<h3 id="accessing-instance-methods">
					<a class="fragment-link" href="#accessing-instance-methods">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Accessing Instance Methods (#accessing-instance-methods)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Accessing Instance Methods</span>
				</h3><p>To be able to access the instance of your custom web component, we can leverage <code>refs</code>:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> myRef <span class="token operator">=</span> <span class="token function">useRef</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token function">useEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token keyword">if</span> <span class="token punctuation">(</span>myRef<span class="token punctuation">.</span>current<span class="token punctuation">)</span> <span class="token punctuation">{</span>
			myRef<span class="token punctuation">.</span>current<span class="token punctuation">.</span><span class="token function">doSomething</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>x-foo</span> <span class="token attr-name">ref</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>myRef<span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="triggering-custom-events">
					<a class="fragment-link" href="#triggering-custom-events">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Triggering custom events (#triggering-custom-events)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Triggering custom events</span>
				</h3><p>Preact normalizes the casing of standard built-in DOM Events, which are normally case-sensitive. This is the reason it's possible to pass an <code>onChange</code> prop to <code>&lt;input></code>, despite the actual event name being <code>&quot;change&quot;</code>. Custom Elements often fire custom events as part of their public API, however there is no way to know what custom events might be fired. In order to ensure Custom Elements are seamlessly supported in Preact, unrecognized event handler props passed to a DOM Element are registered using their casing exactly as specified.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token comment">// Built-in DOM event: listens for a &quot;click&quot; event</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'click'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span>

<span class="token comment">// Custom Element: listens for &quot;TabChange&quot; event (case-sensitive!)</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>tab-bar</span> <span class="token attr-name">onTabChange</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'tab change'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span>

<span class="token comment">// Corrected: listens for &quot;tabchange&quot; event (lower-case)</span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>tab-bar</span> <span class="token attr-name">ontabchange</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span><span class="token string">'tab change'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span></code></pre>
					
				</div>
			</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/shelacek" target="_blank" rel="noopener noreferrer">@shelacek</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
