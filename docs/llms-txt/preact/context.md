# Source: https://preactjs.com/guide/v10/context#createcontext

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Context – Preact Guide</title>
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
	<meta name="description" content="Context allows you to pass props through intermediate components. This documents describes both the new and the old API">
<meta property="og:url" content="https://preactjs.com/guide/v10/context">
<meta property="og:title" content="Context – Preact Guide">
<meta property="og:description" content="Context allows you to pass props through intermediate components. This documents describes both the new and the old API">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/context.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/context.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/context" can-edit><div class="markup"><h1>Context</h1><p>Context is a way to pass data through the component tree without having to pass it through every component in-between via props. In a nutshell, it allows components anywhere in the hierarchy to subscribe to a value and get notified when it changes, bringing pub-sub-style updates to Preact.</p>
<p>It's not uncommon to run into situations in which a value from a grandparent component (or higher) needs to be passed down to a child, often without the intermediate component needing it. This process of passing down props is often referred to as &quot;prop drilling&quot; and can be cumbersome, error-prone, and just plain repetitive, especially as the application grows and more values have to be passed through more layers. This is one of the key issues Context aims to address by providing a way for a child to subscribe to a value higher up in the component tree, accessing the value without it being passed down as a prop.</p>
<p>There are two ways to use context in Preact: via the newer <code>createContext</code> API and the legacy context API. These days there's very few reasons to ever reach for the legacy API but it's documented here for completeness.</p>
<hr>
<nav><ul><li><a href="#modern-context-api">Modern Context API</a><ul><li><a href="#creating-a-context">Creating a Context</a></li><li><a href="#setting-up-a-provider">Setting up a Provider</a></li><li><a href="#using-the-context">Using the Context</a></li><li><a href="#updating-the-context">Updating the Context</a></li></ul></li><li><a href="#legacy-context-api">Legacy Context API</a></li></ul></nav><hr>

				<h2 id="modern-context-api">
					<a class="fragment-link" href="#modern-context-api">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Modern Context API (#modern-context-api)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Modern Context API</span>
				</h2>
				<h3 id="creating-a-context">
					<a class="fragment-link" href="#creating-a-context">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Creating a Context (#creating-a-context)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Creating a Context</span>
				</h3><p>To create a new context, we use the <code>createContext</code> function. This function takes an initial state as an argument and returns an object with two component properties: <code>Provider</code>, to make the context available to descendants, and <code>Consumer</code>, to access the context value (primarily in class components).</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> createContext <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact'</span><span class="token punctuation">;</span>

<span class="token keyword">export</span> <span class="token keyword">const</span> Theme <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'light'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">export</span> <span class="token keyword">const</span> User <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token punctuation">{</span> <span class="token literal-property property">name</span><span class="token operator">:</span> <span class="token string">'Guest'</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token keyword">export</span> <span class="token keyword">const</span> Locale <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			
				<h3 id="setting-up-a-provider">
					<a class="fragment-link" href="#setting-up-a-provider">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Setting up a Provider (#setting-up-a-provider)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Setting up a Provider</span>
				</h3><p>Once we've created a context, we must make it available to descendants using the <code>Provider</code> component. The <code>Provider</code> must be given a <code>value</code> prop, representing the initial value of the context.</p>
<blockquote>
<p>The initial value set from <code>createContext</code> is only used in the absence of a <code>Provider</code> above the consumer in the tree. This may be helpful for testing components in isolation, as it avoids the need for creating a wrapping <code>Provider</code> around your component.</p>
</blockquote>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> createContext <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact'</span><span class="token punctuation">;</span>

<span class="token keyword">export</span> <span class="token keyword">const</span> Theme <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'light'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Theme.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>dark<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Theme.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<blockquote>
<p><strong>Tip:</strong> You can have multiple providers of the same context throughout your app but only the closest one to the consumer will be used.</p>
</blockquote>

				<h3 id="using-the-context">
					<a class="fragment-link" href="#using-the-context">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Using the Context (#using-the-context)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Using the Context</span>
				</h3><p>There are three ways to consume a context, largely dependent on your preferred component style: <code>static contextType</code> (class components), the <code>useContext</code> hook (function components/hooks), and <code>Context.Consumer</code> (all components), .</p>
<div><div class="_tabs_1dgk4_1" role="tablist" aria-label="API Styles" aria-orientation="horizontal"><button class="_tab_1dgk4_1" role="tab" id="tab-P0-0-contextType" aria-controls="panel-P0-0-contextType" aria-selected="true" tabindex="0">contextType</button><button class="_tab_1dgk4_1" role="tab" id="tab-P0-0-useContext" aria-controls="panel-P0-0-useContext" aria-selected="false" tabindex="-1">useContext</button><button class="_tab_1dgk4_1" role="tab" id="tab-P0-0-Context.Consumer" aria-controls="panel-P0-0-Context.Consumer" aria-selected="false" tabindex="-1">Context.Consumer</button></div><div role="tabpanel" id="panel-P0-0-contextType" aria-labelledby="tab-P0-0-contextType" tabindex="0"><div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> ThemePrimary <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'#673ab8'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">class</span> <span class="token class-name">ThemedButton</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	<span class="token keyword">static</span> contextType <span class="token operator">=</span> ThemePrimary<span class="token punctuation">;</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">const</span> theme <span class="token operator">=</span> <span class="token keyword">this</span><span class="token punctuation">.</span>context<span class="token punctuation">;</span>
		<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">background</span><span class="token operator">:</span> theme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Themed Button</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePrimary.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>#8f61e1<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">ThemePrimary.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBjcmVhdGVDb250ZXh0LCBDb21wb25lbnQgfSBmcm9tICdwcmVhY3QnOwoKY29uc3QgU29tZUNvbXBvbmVudCA9IHByb3BzID0%2BIHByb3BzLmNoaWxkcmVuOwoKY29uc3QgVGhlbWVQcmltYXJ5ID0gY3JlYXRlQ29udGV4dCgnIzY3M2FiOCcpOwoKY2xhc3MgVGhlbWVkQnV0dG9uIGV4dGVuZHMgQ29tcG9uZW50IHsKCXN0YXRpYyBjb250ZXh0VHlwZSA9IFRoZW1lUHJpbWFyeTsKCglyZW5kZXIoKSB7CgkJY29uc3QgdGhlbWUgPSB0aGlzLmNvbnRleHQ7CgkJcmV0dXJuIDxidXR0b24gc3R5bGU9e3sgYmFja2dyb3VuZDogdGhlbWUgfX0%2BVGhlbWVkIEJ1dHRvbjwvYnV0dG9uPjsKCX0KfQoKZnVuY3Rpb24gQXBwKCkgewoJcmV0dXJuICgKCQk8VGhlbWVQcmltYXJ5LlByb3ZpZGVyIHZhbHVlPSIjOGY2MWUxIj4KCQkJPFNvbWVDb21wb25lbnQ%2BCgkJCQk8VGhlbWVkQnV0dG9uIC8%2BCgkJCTwvU29tZUNvbXBvbmVudD4KCQk8L1RoZW1lUHJpbWFyeS5Qcm92aWRlcj4KCSk7Cn0KCnJlbmRlcig8QXBwIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div></div><div role="tabpanel" id="panel-P0-0-useContext" aria-labelledby="tab-P0-0-useContext" tabindex="0" hidden><div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> ThemePrimary <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'#673ab8'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">ThemedButton</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> theme <span class="token operator">=</span> <span class="token function">useContext</span><span class="token punctuation">(</span>ThemePrimary<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">background</span><span class="token operator">:</span> theme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Themed Button</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePrimary.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>#8f61e1<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">ThemePrimary.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBjcmVhdGVDb250ZXh0IH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlQ29udGV4dCB9IGZyb20gJ3ByZWFjdC9ob29rcyc7Cgpjb25zdCBTb21lQ29tcG9uZW50ID0gcHJvcHMgPT4gcHJvcHMuY2hpbGRyZW47Cgpjb25zdCBUaGVtZVByaW1hcnkgPSBjcmVhdGVDb250ZXh0KCcjNjczYWI4Jyk7CgpmdW5jdGlvbiBUaGVtZWRCdXR0b24oKSB7Cgljb25zdCB0aGVtZSA9IHVzZUNvbnRleHQoVGhlbWVQcmltYXJ5KTsKCXJldHVybiA8YnV0dG9uIHN0eWxlPXt7IGJhY2tncm91bmQ6IHRoZW1lIH19PlRoZW1lZCBCdXR0b248L2J1dHRvbj47Cn0KCmZ1bmN0aW9uIEFwcCgpIHsKCXJldHVybiAoCgkJPFRoZW1lUHJpbWFyeS5Qcm92aWRlciB2YWx1ZT0iIzhmNjFlMSI%2BCgkJCTxTb21lQ29tcG9uZW50PgoJCQkJPFRoZW1lZEJ1dHRvbiAvPgoJCQk8L1NvbWVDb21wb25lbnQ%2BCgkJPC9UaGVtZVByaW1hcnkuUHJvdmlkZXI%2BCgkpOwp9CgpyZW5kZXIoPEFwcCAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK">Run in REPL</a>
				</div></div><div role="tabpanel" id="panel-P0-0-Context.Consumer" aria-labelledby="tab-P0-0-Context.Consumer" tabindex="0" hidden><div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> ThemePrimary <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'#673ab8'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">ThemedButton</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePrimary.Consumer</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token punctuation">{</span><span class="token parameter">theme</span> <span class="token operator">=></span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">background</span><span class="token operator">:</span> theme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Themed Button</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token punctuation">}</span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">ThemePrimary.Consumer</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePrimary.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>#8f61e1<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">ThemePrimary.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBjcmVhdGVDb250ZXh0IH0gZnJvbSAncHJlYWN0JzsKCmNvbnN0IFNvbWVDb21wb25lbnQgPSBwcm9wcyA9PiBwcm9wcy5jaGlsZHJlbjsKCmNvbnN0IFRoZW1lUHJpbWFyeSA9IGNyZWF0ZUNvbnRleHQoJyM2NzNhYjgnKTsKCmZ1bmN0aW9uIFRoZW1lZEJ1dHRvbigpIHsKCXJldHVybiAoCgkJPFRoZW1lUHJpbWFyeS5Db25zdW1lcj4KCQkJe3RoZW1lID0%2BIDxidXR0b24gc3R5bGU9e3sgYmFja2dyb3VuZDogdGhlbWUgfX0%2BVGhlbWVkIEJ1dHRvbjwvYnV0dG9uPn0KCQk8L1RoZW1lUHJpbWFyeS5Db25zdW1lcj4KCSk7Cn0KCmZ1bmN0aW9uIEFwcCgpIHsKCXJldHVybiAoCgkJPFRoZW1lUHJpbWFyeS5Qcm92aWRlciB2YWx1ZT0iIzhmNjFlMSI%2BCgkJCTxTb21lQ29tcG9uZW50PgoJCQkJPFRoZW1lZEJ1dHRvbiAvPgoJCQk8L1NvbWVDb21wb25lbnQ%2BCgkJPC9UaGVtZVByaW1hcnkuUHJvdmlkZXI%2BCgkpOwp9CgpyZW5kZXIoPEFwcCAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK">Run in REPL</a>
				</div></div></div>


				<h3 id="updating-the-context">
					<a class="fragment-link" href="#updating-the-context">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Updating the Context (#updating-the-context)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Updating the Context</span>
				</h3><p>Static values can be useful, but more often than not, we want to be able to update the context value dynamically. To do so, we leverage standard component state mechanisms:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> ThemePrimary <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">ThemedButton</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">{</span> theme <span class="token punctuation">}</span> <span class="token operator">=</span> <span class="token function">useContext</span><span class="token punctuation">(</span>ThemePrimary<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">background</span><span class="token operator">:</span> theme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Themed Button</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">ThemePicker</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">{</span> theme<span class="token punctuation">,</span> setTheme <span class="token punctuation">}</span> <span class="token operator">=</span> <span class="token function">useContext</span><span class="token punctuation">(</span>ThemePrimary<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span>
			<span class="token attr-name">type</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>color<span class="token punctuation">&quot;</span></span>
			<span class="token attr-name">value</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>theme<span class="token punctuation">}</span></span>
			<span class="token attr-name">onChange</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token parameter">e</span> <span class="token operator">=></span> <span class="token function">setTheme</span><span class="token punctuation">(</span>e<span class="token punctuation">.</span>currentTarget<span class="token punctuation">.</span>value<span class="token punctuation">)</span><span class="token punctuation">}</span></span>
		<span class="token punctuation">/></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>theme<span class="token punctuation">,</span> setTheme<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token string">'#673ab8'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePrimary.Provider</span></span> <span class="token attr-name">value</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> theme<span class="token punctuation">,</span> setTheme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
				</span><span class="token punctuation">{</span><span class="token string">' - '</span><span class="token punctuation">}</span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemePicker</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">ThemePrimary.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBjcmVhdGVDb250ZXh0IH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlQ29udGV4dCwgdXNlU3RhdGUgfSBmcm9tICdwcmVhY3QvaG9va3MnOwoKY29uc3QgU29tZUNvbXBvbmVudCA9IHByb3BzID0%2BIHByb3BzLmNoaWxkcmVuOwoKY29uc3QgVGhlbWVQcmltYXJ5ID0gY3JlYXRlQ29udGV4dChudWxsKTsKCmZ1bmN0aW9uIFRoZW1lZEJ1dHRvbigpIHsKCWNvbnN0IHsgdGhlbWUgfSA9IHVzZUNvbnRleHQoVGhlbWVQcmltYXJ5KTsKCXJldHVybiA8YnV0dG9uIHN0eWxlPXt7IGJhY2tncm91bmQ6IHRoZW1lIH19PlRoZW1lZCBCdXR0b248L2J1dHRvbj47Cn0KCmZ1bmN0aW9uIFRoZW1lUGlja2VyKCkgewoJY29uc3QgeyB0aGVtZSwgc2V0VGhlbWUgfSA9IHVzZUNvbnRleHQoVGhlbWVQcmltYXJ5KTsKCXJldHVybiAoCgkJPGlucHV0CgkJCXR5cGU9ImNvbG9yIgoJCQl2YWx1ZT17dGhlbWV9CgkJCW9uQ2hhbmdlPXtlID0%2BIHNldFRoZW1lKGUuY3VycmVudFRhcmdldC52YWx1ZSl9CgkJLz4KCSk7Cn0KCmZ1bmN0aW9uIEFwcCgpIHsKCWNvbnN0IFt0aGVtZSwgc2V0VGhlbWVdID0gdXNlU3RhdGUoJyM2NzNhYjgnKTsKCXJldHVybiAoCgkJPFRoZW1lUHJpbWFyeS5Qcm92aWRlciB2YWx1ZT17eyB0aGVtZSwgc2V0VGhlbWUgfX0%2BCgkJCTxTb21lQ29tcG9uZW50PgoJCQkJPFRoZW1lZEJ1dHRvbiAvPgoJCQkJeycgLSAnfQoJCQkJPFRoZW1lUGlja2VyIC8%2BCgkJCTwvU29tZUNvbXBvbmVudD4KCQk8L1RoZW1lUHJpbWFyeS5Qcm92aWRlcj4KCSk7Cn0KCnJlbmRlcig8QXBwIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			
				<h2 id="legacy-context-api">
					<a class="fragment-link" href="#legacy-context-api">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Legacy Context API (#legacy-context-api)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Legacy Context API</span>
				</h2><p>This API is considered legacy and should be avoided in new code, it has known issues and only exists for backwards-compatibility reasons.</p>
<p>One of the key differences between this API and the new one is that this API cannot update a child when a component in-between the child and the provider aborts rendering via <code>shouldComponentUpdate</code>. When this happens, the child <strong>will not</strong> received the updated context value, often resulting in tearing (part of the UI using the new value, part using the old).</p>
<p>To pass down a value through the context, a component needs to have the <code>getChildContext</code> method, returning the intended context value. Descendants can then access the context via the second argument in function components or <code>this.context</code> in class-based components.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">ThemedButton</span><span class="token punctuation">(</span><span class="token parameter">_props<span class="token punctuation">,</span> context</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">style</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">{</span> <span class="token literal-property property">background</span><span class="token operator">:</span> context<span class="token punctuation">.</span>theme <span class="token punctuation">}</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Themed Button</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">class</span> <span class="token class-name">App</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	<span class="token function">getChildContext</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token punctuation">{</span>
			<span class="token literal-property property">theme</span><span class="token operator">:</span> <span class="token string">'#673ab8'</span>
		<span class="token punctuation">}</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token punctuation">(</span>
			<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">SomeOtherComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
					</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">ThemedButton</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">SomeOtherComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
		<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmNvbnN0IFNvbWVPdGhlckNvbXBvbmVudCA9IHByb3BzID0%2BIHByb3BzLmNoaWxkcmVuOwoKZnVuY3Rpb24gVGhlbWVkQnV0dG9uKF9wcm9wcywgY29udGV4dCkgewoJcmV0dXJuIDxidXR0b24gc3R5bGU9e3sgYmFja2dyb3VuZDogY29udGV4dC50aGVtZSB9fT5UaGVtZWQgQnV0dG9uPC9idXR0b24%2BOwp9CgpjbGFzcyBBcHAgZXh0ZW5kcyBDb21wb25lbnQgewoJZ2V0Q2hpbGRDb250ZXh0KCkgewoJCXJldHVybiB7CgkJCXRoZW1lOiAnIzY3M2FiOCcKCQl9OwoJfQoKCXJlbmRlcigpIHsKCQlyZXR1cm4gKAoJCQk8ZGl2PgoJCQkJPFNvbWVPdGhlckNvbXBvbmVudD4KCQkJCQk8VGhlbWVkQnV0dG9uIC8%2BCgkJCQk8L1NvbWVPdGhlckNvbXBvbmVudD4KCQkJPC9kaXY%2BCgkJKTsKCX0KfQoKcmVuZGVyKDxBcHAgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKSk7Cg%3D%3D">Run in REPL</a>
				</div>
			</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/leerob" target="_blank" rel="noopener noreferrer">@leerob</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
