# Source: https://preactjs.com/guide/v10/server-side-rendering

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Server-Side Rendering – Preact Guide</title>
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
	<meta name="description" content="Render your Preact application on the server to show content to users quicker">
<meta property="og:url" content="https://preactjs.com/guide/v10/server-side-rendering">
<meta property="og:title" content="Server-Side Rendering – Preact Guide">
<meta property="og:description" content="Render your Preact application on the server to show content to users quicker">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/server-side-rendering.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/server-side-rendering.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/server-side-rendering" can-edit><div class="markup"><h1>Server-Side Rendering</h1><p>Server-Side Rendering (often abbreviated as &quot;SSR&quot;) allows you to render your application to an HTML string that can be sent to the client to improve load time. Outside of that there are other scenarios, like testing, where SSR proves really useful.</p>
<hr>
<nav><ul><li><a href="#installation">Installation</a></li><li><a href="#html-strings">HTML Strings</a><ul><li><a href="#rendertostring">renderToString</a></li><li><a href="#rendertostringasync">renderToStringAsync</a></li></ul></li><li><a href="#html-streams">HTML Streams</a><ul><li><a href="#rendertopipeablestream">renderToPipeableStream</a></li><li><a href="#rendertoreadablestream">renderToReadableStream</a></li></ul></li><li><a href="#customize-renderer-output">Customize Renderer Output</a><ul><li><a href="#jsx-mode">JSX Mode</a></li><li><a href="#pretty-mode">Pretty Mode</a></li><li><a href="#shallow-mode">Shallow Mode</a></li><li><a href="#xml-mode">XML Mode</a></li></ul></li></ul></nav><hr>

				<h2 id="installation">
					<a class="fragment-link" href="#installation">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Installation (#installation)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Installation</span>
				</h2><p>The server-side renderer for Preact lives in its <a href="https://github.com/preactjs/preact-render-to-string/" target="_blank" rel="noopener noreferrer">own repository</a> and can be installed via your packager of choice:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-bash"><span class="token function">npm</span> <span class="token function">install</span> <span class="token parameter variable">-S</span> preact-render-to-string</code></pre>
					
				</div>
			<p>After the command above finished, we can start using it right away.</p>

				<h2 id="html-strings">
					<a class="fragment-link" href="#html-strings">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: HTML Strings (#html-strings)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>HTML Strings</span>
				</h2><p>Both of the following options return a single HTML string that represents the full rendered output of your Preact application.</p>

				<h3 id="rendertostring">
					<a class="fragment-link" href="#rendertostring">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: renderToString (#rendertostring)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>renderToString</span>
				</h3><p>The most basic and straightforward rendering method, <code>renderToString</code> transforms a Preact tree into a string of HTML synchronously.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> renderToString <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact-render-to-string'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> name <span class="token operator">=</span> <span class="token string">'Preact User!'</span><span class="token punctuation">;</span>
<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>foo<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">Hello </span><span class="token punctuation">{</span>name<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>

<span class="token keyword">const</span> html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div class=&quot;foo&quot;>Hello Preact User!&lt;/div></span></code></pre>
					
				</div>
			
				<h3 id="rendertostringasync">
					<a class="fragment-link" href="#rendertostringasync">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: renderToStringAsync (#rendertostringasync)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>renderToStringAsync</span>
				</h3><p>Awaits the resolution of promises before returning the complete HTML string. This is particularly useful when utilizing suspense for lazy-loaded components or data fetching.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token comment">// app.js</span>
<span class="token keyword">import</span> <span class="token punctuation">{</span> Suspense<span class="token punctuation">,</span> lazy <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> HomePage <span class="token operator">=</span> <span class="token function">lazy</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token keyword">import</span><span class="token punctuation">(</span><span class="token string">'./pages/home.js'</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Suspense</span></span> <span class="token attr-name">fallback</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Loading</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">HomePage</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Suspense</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> renderToStringAsync <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact-render-to-string'</span><span class="token punctuation">;</span>
<span class="token keyword">import</span> <span class="token punctuation">{</span> App <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'./app.js'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> html <span class="token operator">=</span> <span class="token keyword">await</span> <span class="token function">renderToStringAsync</span><span class="token punctuation">(</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">App</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;h1>Home page&lt;/h1></span></code></pre>
					
				</div>
			<blockquote>
<p><strong>Note:</strong> Unfortunately there's a handful of known limitations in Preact v10's implementation of &quot;resumed hydration&quot; — that is, hydration that can pause and wait for JS chunks or data to be downloaded &amp; available before continuing. This has been solved in the upcoming Preact v11 release.</p>
<p>For now, you'll want to avoid async boundaries that return 0 or more than 1 DOM node as children, such as in the following examples:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token constant">X</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token comment">// Some lazy operation, such as initializing analytics</span>
  <span class="token keyword">return</span> <span class="token keyword">null</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> LazyOperation <span class="token operator">=</span> <span class="token function">lazy</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token comment">/* import X */</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			
				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token constant">Y</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
  <span class="token comment">// `&lt;Fragment>` disappears upon rendering, leaving two `&lt;p>` DOM elements</span>
  <span class="token keyword">return</span> <span class="token punctuation">(</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span><span class="token plain-text">
      </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Foo</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
      </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Bar</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span>
  <span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> SuspendingMultipleChildren <span class="token operator">=</span> <span class="token function">lazy</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token comment">/* import Y */</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>For a more comprehensive write up of the known problems and how we have addressed them, please see <a href="https://github.com/preactjs/preact/issues/4442" target="_blank" rel="noopener noreferrer">Hydration 2.0 (preactjs/preact#4442)</a></p>
</blockquote>

				<h2 id="html-streams">
					<a class="fragment-link" href="#html-streams">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: HTML Streams (#html-streams)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>HTML Streams</span>
				</h2><p>Streaming is a method of rendering that allows you to send parts of your Preact application to the client as they are ready rather than waiting for the entire render to complete.</p>

				<h3 id="rendertopipeablestream">
					<a class="fragment-link" href="#rendertopipeablestream">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: renderToPipeableStream (#rendertopipeablestream)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>renderToPipeableStream</span>
				</h3><p><code>renderToPipeableStream</code> is a streaming method that utilizes <a href="https://nodejs.org/api/stream.html" target="_blank" rel="noopener noreferrer">Node.js Streams</a> to render your application. If you are not using Node, you should look to <a href="#rendertoreadablestream">renderToReadableStream</a> instead.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> renderToPipeableStream <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/stream-node'</span><span class="token punctuation">;</span>

<span class="token comment">// Request handler syntax and form will vary across frameworks</span>
<span class="token keyword">function</span> <span class="token function">handler</span><span class="token punctuation">(</span><span class="token parameter">req<span class="token punctuation">,</span> res</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">{</span> pipe<span class="token punctuation">,</span> abort <span class="token punctuation">}</span> <span class="token operator">=</span> <span class="token function">renderToPipeableStream</span><span class="token punctuation">(</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">App</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">,</span> <span class="token punctuation">{</span>
		<span class="token function">onShellReady</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
			res<span class="token punctuation">.</span>statusCode <span class="token operator">=</span> <span class="token number">200</span><span class="token punctuation">;</span>
			res<span class="token punctuation">.</span><span class="token function">setHeader</span><span class="token punctuation">(</span><span class="token string">'Content-Type'</span><span class="token punctuation">,</span> <span class="token string">'text/html'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
			<span class="token function">pipe</span><span class="token punctuation">(</span>res<span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span><span class="token punctuation">,</span>
		<span class="token function">onError</span><span class="token punctuation">(</span><span class="token parameter">error</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
			res<span class="token punctuation">.</span>statusCode <span class="token operator">=</span> <span class="token number">500</span><span class="token punctuation">;</span>
			res<span class="token punctuation">.</span><span class="token function">send</span><span class="token punctuation">(</span>
				<span class="token template-string"><span class="token template-punctuation string">`</span><span class="token string">&lt;!doctype html>&lt;p>An error ocurred:&lt;/p>&lt;pre></span><span class="token interpolation"><span class="token interpolation-punctuation punctuation">${</span>error<span class="token punctuation">.</span>message<span class="token interpolation-punctuation punctuation">}</span></span><span class="token string">&lt;/pre></span><span class="token template-punctuation string">`</span></span>
			<span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span>
	<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token comment">// Abandon and switch to client rendering if enough time passes.</span>
	<span class="token function">setTimeout</span><span class="token punctuation">(</span>abort<span class="token punctuation">,</span> <span class="token number">2000</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="rendertoreadablestream">
					<a class="fragment-link" href="#rendertoreadablestream">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: renderToReadableStream (#rendertoreadablestream)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>renderToReadableStream</span>
				</h3><p><code>renderToReadableStream</code> is another streaming method and similar to <code>renderToPipeableStream</code>, but designed for use in environments that support standardized <a href="https://developer.mozilla.org/en-US/docs/Web/API/Streams_API" target="_blank" rel="noopener noreferrer">Web Streams</a> instead.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> renderToReadableStream <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/stream'</span><span class="token punctuation">;</span>

<span class="token comment">// Request handler syntax and form will vary across frameworks</span>
<span class="token keyword">function</span> <span class="token function">handler</span><span class="token punctuation">(</span><span class="token parameter">req<span class="token punctuation">,</span> res</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> stream <span class="token operator">=</span> <span class="token function">renderToReadableStream</span><span class="token punctuation">(</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">App</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token keyword">new</span> <span class="token class-name">Response</span><span class="token punctuation">(</span>stream<span class="token punctuation">,</span> <span class="token punctuation">{</span>
		<span class="token literal-property property">headers</span><span class="token operator">:</span> <span class="token punctuation">{</span>
			<span class="token string-property property">'Content-Type'</span><span class="token operator">:</span> <span class="token string">'text/html'</span>
		<span class="token punctuation">}</span>
	<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h2 id="customize-renderer-output">
					<a class="fragment-link" href="#customize-renderer-output">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Customize Renderer Output (#customize-renderer-output)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Customize Renderer Output</span>
				</h2><p>We offer a number of options through the <code>/jsx</code> module to customize the output of the renderer for a handful of popular use cases.</p>

				<h3 id="jsx-mode">
					<a class="fragment-link" href="#jsx-mode">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: JSX Mode (#jsx-mode)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>JSX Mode</span>
				</h3><p>The JSX rendering mode is especially useful if you're doing any kind of snapshot testing. It renders the output as if it was written in JSX.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> renderToString <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/jsx'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">data-foo</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token boolean">true</span><span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">;</span>

<span class="token keyword">const</span> html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">{</span> <span class="token literal-property property">jsx</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div data-foo={true} /></span></code></pre>
					
				</div>
			
				<h3 id="pretty-mode">
					<a class="fragment-link" href="#pretty-mode">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Pretty Mode (#pretty-mode)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Pretty Mode</span>
				</h3><p>If you need to get the rendered output in a more human friendly way, we've got you covered! By passing the <code>pretty</code> option, we'll preserve whitespace and indent the output as expected.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> renderToString <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/jsx'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> <span class="token function-variable function">Foo</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">foo</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token punctuation">(</span>
	<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>foo<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Foo</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
	</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">{</span> <span class="token literal-property property">pretty</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div class=&quot;foo&quot;></span>
<span class="token comment">//   &lt;div>foo&lt;/div></span>
<span class="token comment">// &lt;/div></span></code></pre>
					
				</div>
			
				<h3 id="shallow-mode">
					<a class="fragment-link" href="#shallow-mode">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Shallow Mode (#shallow-mode)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Shallow Mode</span>
				</h3><p>For some purposes it's often preferable to not render the whole tree, but only one level. For that we have a shallow renderer which will print child components by name, instead of their return value.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> renderToString <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/jsx'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> <span class="token function-variable function">Foo</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">foo</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token punctuation">(</span>
	<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>foo<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Foo</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
	</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">{</span> <span class="token literal-property property">shallow</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div class=&quot;foo&quot;>&lt;Foo />&lt;/div></span></code></pre>
					
				</div>
			
				<h3 id="xml-mode">
					<a class="fragment-link" href="#xml-mode">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: XML Mode (#xml-mode)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>XML Mode</span>
				</h3><p>For elements without children, XML mode will instead render them as self-closing tags.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> renderToString <span class="token keyword">from</span> <span class="token string">'preact-render-to-string/jsx'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> <span class="token function-variable function">Foo</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token punctuation">(</span>
	<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>foo<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Foo</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
	</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">let</span> html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">{</span> <span class="token literal-property property">xml</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div class=&quot;foo&quot;>&lt;div />&lt;/div></span>

html <span class="token operator">=</span> <span class="token function">renderToString</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> <span class="token punctuation">{</span><span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">{</span> <span class="token literal-property property">xml</span><span class="token operator">:</span> <span class="token boolean">false</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>html<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// &lt;div class=&quot;foo&quot;>&lt;div>&lt;/div>&lt;/div></span></code></pre>
					
				</div>
			</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/JoviDeCroock" target="_blank" rel="noopener noreferrer">@JoviDeCroock</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
