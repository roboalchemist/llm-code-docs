# Source: https://preactjs.com/guide/v10/whats-new/#componentdidcatch

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>What's new in Preact X – Preact Guide</title>
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
	<meta name="description" content="New features and changes in Preact X">
<meta property="og:url" content="https://preactjs.com/guide/v10/whats-new">
<meta property="og:title" content="What's new in Preact X – Preact Guide">
<meta property="og:description" content="New features and changes in Preact X">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/whats-new.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/whats-new.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/whats-new" can-edit><div class="markup"><h1>What's new in Preact X</h1><p>Preact X is a huge step forward from Preact 8.x. We've rethought every bit and byte of our code and added a plethora of major features in the process. Same goes for compatibility enhancements to support more third-party libraries.</p>
<p>In a nutshell Preact X is what we always wanted Preact to be: A tiny, fast and feature-packed library. And speaking of size, you'll be happy to hear that all the new features and improved rendering fit into the same size footprint as <code>8.x</code>!</p>
<hr>
<nav><ul><li><a href="#fragments">Fragments</a></li><li><a href="#componentdidcatch">componentDidCatch</a></li><li><a href="#hooks">Hooks</a></li><li><a href="#createcontext">createContext</a></li><li><a href="#css-custom-properties">CSS Custom Properties</a></li><li><a href="#compat-lives-in-core">Compat lives in core</a></li><li><a href="#many-compatibility-fixes">Many compatibility fixes</a></li></ul></nav><hr>

				<h2 id="fragments">
					<a class="fragment-link" href="#fragments">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Fragments (#fragments)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Fragments</span>
				</h2><p><code>Fragments</code> are a major new feature of Preact X, and one of the main motivations for rethinking Preact's architecture. They are a special kind of component that renders children elements inline with their parent, without an extra wrapping DOM element. On top of that they allow you to return multiple nodes from <code>render</code>.</p>
<p><a href="/guide/v10/components#fragments">Fragment docs →</a></p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">A</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">B</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					<a class="repl-link" href="/repl?code=ZnVuY3Rpb24gRm9vKCkgewoJcmV0dXJuICgKCQk8PgoJCQk8ZGl2PkE8L2Rpdj4KCQkJPGRpdj5CPC9kaXY%2BCgkJPC8%2BCgkpOwp9">Run in REPL</a>
				</div>
			
				<h2 id="componentdidcatch">
					<a class="fragment-link" href="#componentdidcatch">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: componentDidCatch (#componentdidcatch)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>componentDidCatch</span>
				</h2><p>We all wish errors wouldn't happen in our applications, but sometimes they do. With <code>componentDidCatch</code>, it's now possible to catch and handle any errors that occur within lifecycle methods like <code>render</code>, including exceptions deep in the component tree. This can be used to display user-friendly error messages, or write a log entry to an external service in case something goes wrong.</p>
<p><a href="/guide/v10/components#error-boundaries">Lifecycle docs →</a></p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">class</span> <span class="token class-name">Catcher</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	state <span class="token operator">=</span> <span class="token punctuation">{</span> <span class="token literal-property property">errored</span><span class="token operator">:</span> <span class="token boolean">false</span> <span class="token punctuation">}</span><span class="token punctuation">;</span>

	<span class="token function">componentDidCatch</span><span class="token punctuation">(</span><span class="token parameter">error</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">this</span><span class="token punctuation">.</span><span class="token function">setState</span><span class="token punctuation">(</span><span class="token punctuation">{</span> <span class="token literal-property property">errored</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token parameter">props<span class="token punctuation">,</span> state</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">if</span> <span class="token punctuation">(</span>state<span class="token punctuation">.</span>errored<span class="token punctuation">)</span> <span class="token punctuation">{</span>
			<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Something went badly wrong</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span>
		<span class="token keyword">return</span> props<span class="token punctuation">.</span>children<span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span></code></pre>
					<a class="repl-link" href="/repl?code=Y2xhc3MgQ2F0Y2hlciBleHRlbmRzIENvbXBvbmVudCB7CglzdGF0ZSA9IHsgZXJyb3JlZDogZmFsc2UgfTsKCgljb21wb25lbnREaWRDYXRjaChlcnJvcikgewoJCXRoaXMuc2V0U3RhdGUoeyBlcnJvcmVkOiB0cnVlIH0pOwoJfQoKCXJlbmRlcihwcm9wcywgc3RhdGUpIHsKCQlpZiAoc3RhdGUuZXJyb3JlZCkgewoJCQlyZXR1cm4gPHA%2BU29tZXRoaW5nIHdlbnQgYmFkbHkgd3Jvbmc8L3A%2BOwoJCX0KCQlyZXR1cm4gcHJvcHMuY2hpbGRyZW47Cgl9Cn0%3D">Run in REPL</a>
				</div>
			
				<h2 id="hooks">
					<a class="fragment-link" href="#hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Hooks (#hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Hooks</span>
				</h2><p><code>Hooks</code> are a new way to make sharing logic easier between components. They represent an alternative to the existing class-based component API. In Preact they live inside an addon which can be imported via <code>preact/hooks</code></p>
<p><a href="/guide/v10/hooks">Hooks Docs →</a></p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Counter</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>value<span class="token punctuation">,</span> setValue<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> increment <span class="token operator">=</span> <span class="token function">useCallback</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">setValue</span><span class="token punctuation">(</span>value <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>value<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			Counter: </span><span class="token punctuation">{</span>value<span class="token punctuation">}</span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					<a class="repl-link" href="/repl?code=ZnVuY3Rpb24gQ291bnRlcigpIHsKCWNvbnN0IFt2YWx1ZSwgc2V0VmFsdWVdID0gdXNlU3RhdGUoMCk7Cgljb25zdCBpbmNyZW1lbnQgPSB1c2VDYWxsYmFjaygoKSA9PiBzZXRWYWx1ZSh2YWx1ZSArIDEpLCBbdmFsdWVdKTsKCglyZXR1cm4gKAoJCTxkaXY%2BCgkJCUNvdW50ZXI6IHt2YWx1ZX0KCQkJPGJ1dHRvbiBvbkNsaWNrPXtpbmNyZW1lbnR9PkluY3JlbWVudDwvYnV0dG9uPgoJCTwvZGl2PgoJKTsKfQ%3D%3D">Run in REPL</a>
				</div>
			
				<h2 id="createcontext">
					<a class="fragment-link" href="#createcontext">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: createContext (#createcontext)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>createContext</span>
				</h2><p>The <code>createContext</code>-API is a true successor for <code>getChildContext()</code>. Whereas <code>getChildContext</code> is fine when you're absolutely sure to never change a value, it falls apart as soon as a component in-between the provider and consumer blocks an update via <code>shouldComponentUpdate</code> when it returns <code>false</code>. With the new context API this problem is now a thing of the past. It is a true pub/sub solution to deliver updates deep down the tree.</p>
<p><a href="/guide/v10/context#createcontext">createContext Docs →</a></p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> Theme <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'light'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">ThemedButton</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Theme.Consumer</span></span><span class="token punctuation">></span></span><span class="token punctuation">{</span><span class="token parameter">theme</span> <span class="token operator">=></span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">Active theme: </span><span class="token punctuation">{</span>theme<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Theme.Consumer</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Theme.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>dark<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Theme.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h2 id="css-custom-properties">
					<a class="fragment-link" href="#css-custom-properties">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: CSS Custom Properties (#css-custom-properties)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>CSS Custom Properties</span>
				</h2><p>Sometimes it's the little things that make a huge difference. With the recent advancements in CSS you can leverage <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/--*" target="_blank" rel="noopener noreferrer">CSS variables</a> for styling:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token string-property property">'--theme-color'</span><span class="token operator">:</span> <span class="token string">'blue'</span> <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token punctuation">{</span>props<span class="token punctuation">.</span>children<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h2 id="compat-lives-in-core">
					<a class="fragment-link" href="#compat-lives-in-core">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Compat lives in core (#compat-lives-in-core)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Compat lives in core</span>
				</h2><p>Although we were always keen on adding new features and pushing Preact forward, the <code>preact-compat</code> package didn't receive as much love. Up until now it has lived in a separate repository making it harder to coordinate large changes spanning Preact and the compatibility layer. By moving compat into the same package as Preact itself, there's nothing extra to install in order to use libraries from the React ecosystem.</p>
<p>The compatibility layer is now called <a href="/guide/v10/differences-to-react#features-exclusive-to-preactcompat">preact/compat</a>, and has learned several new tricks such as <code>forwardRef</code>, <code>memo</code> and countless compatibility improvements.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-js"><span class="token comment">// Preact 8.x</span>
<span class="token keyword">import</span> React <span class="token keyword">from</span> <span class="token string">'preact-compat'</span><span class="token punctuation">;</span>

<span class="token comment">// Preact X</span>
<span class="token keyword">import</span> React <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			
				<h2 id="many-compatibility-fixes">
					<a class="fragment-link" href="#many-compatibility-fixes">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Many compatibility fixes (#many-compatibility-fixes)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Many compatibility fixes</span>
				</h2><p>These are too many to list, but we've grown bounds and leaps on the compatibility front with libraries from the React ecosystem. We specifically made sure to include several popular packages in our testing process to make sure that we can guarantee full support for them.</p>
<p>If you came across a library that didn't work well with Preact 8, you should give it another go with X. The chances are high that everything works as expected ;)</p>
</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/JoviDeCroock" target="_blank" rel="noopener noreferrer">@JoviDeCroock</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
