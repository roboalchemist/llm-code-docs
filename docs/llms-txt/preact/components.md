# Source: https://preactjs.com/guide/v10/components#error-boundaries

# Source: https://preactjs.com/guide/v10/components#fragments

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Components – Preact Guide</title>
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
	<meta name="description" content="Components are the heart of any Preact application. Learn how to create them and use them to compose UIs together">
<meta property="og:url" content="https://preactjs.com/guide/v10/components">
<meta property="og:title" content="Components – Preact Guide">
<meta property="og:description" content="Components are the heart of any Preact application. Learn how to create them and use them to compose UIs together">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/components.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16  ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/components.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/components" can-edit><div class="markup"><h1>Components</h1><p>Components represent the basic building block in Preact. They are fundamental in making it easy to build complex UIs from little building blocks. They're also responsible for attaching state to our rendered output.</p>
<p>There are two kinds of components in Preact, which we'll talk about in this guide.</p>
<hr>
<nav><ul><li><a href="#functional-components">Functional Components</a></li><li><a href="#class-components">Class Components</a><ul><li><a href="#lifecycle-methods">Lifecycle Methods</a></li><li><a href="#error-boundaries">Error Boundaries</a></li></ul></li><li><a href="#fragments">Fragments</a></li></ul></nav><hr>

				<h2 id="functional-components">
					<a class="fragment-link" href="#functional-components">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Functional Components (#functional-components)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Functional Components</span>
				</h2><p>Functional components are plain functions that receive <code>props</code> as the first argument. The function name <strong>must</strong> start with an uppercase letter in order for them to work in JSX.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">MyComponent</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">My name is </span><span class="token punctuation">{</span>props<span class="token punctuation">.</span>name<span class="token punctuation">}</span><span class="token plain-text">.</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">// Usage</span>
<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">MyComponent</span></span> <span class="token attr-name">name</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>John Doe<span class="token punctuation">&quot;</span></span> <span class="token punctuation">/></span></span><span class="token punctuation">;</span>

<span class="token comment">// Renders: &lt;div>My name is John Doe.&lt;/div></span>
<span class="token function">render</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> document<span class="token punctuation">.</span>body<span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCgpmdW5jdGlvbiBNeUNvbXBvbmVudChwcm9wcykgewoJcmV0dXJuIDxkaXY%2BTXkgbmFtZSBpcyB7cHJvcHMubmFtZX0uPC9kaXY%2BOwp9CgovLyBVc2FnZQpjb25zdCBBcHAgPSA8TXlDb21wb25lbnQgbmFtZT0iSm9obiBEb2UiIC8%2BOwoKLy8gUmVuZGVyczogPGRpdj5NeSBuYW1lIGlzIEpvaG4gRG9lLjwvZGl2PgpyZW5kZXIoQXBwLCBkb2N1bWVudC5ib2R5KTs%3D">Run in REPL</a>
				</div>
			<blockquote>
<p>Note in earlier versions they were known as <code>&quot;Stateless Components&quot;</code>. This doesn't hold true anymore with the <a href="/guide/v10/hooks">hooks-addon</a>.</p>
</blockquote>

				<h2 id="class-components">
					<a class="fragment-link" href="#class-components">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Class Components (#class-components)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Class Components</span>
				</h2><p>Class components can have state and lifecycle methods. The latter are special methods, that will be called when a component is attached to the DOM or destroyed for example.</p>
<p>Here we have a simple class component called <code>&lt;Clock></code> that displays the current time:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">class</span> <span class="token class-name">Clock</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	<span class="token function">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">super</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token keyword">this</span><span class="token punctuation">.</span>state <span class="token operator">=</span> <span class="token punctuation">{</span> <span class="token literal-property property">time</span><span class="token operator">:</span> Date<span class="token punctuation">.</span><span class="token function">now</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">}</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token comment">// Lifecycle: Called whenever our component is created</span>
	<span class="token function">componentDidMount</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token comment">// update time every second</span>
		<span class="token keyword">this</span><span class="token punctuation">.</span>timer <span class="token operator">=</span> <span class="token function">setInterval</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
			<span class="token keyword">this</span><span class="token punctuation">.</span><span class="token function">setState</span><span class="token punctuation">(</span><span class="token punctuation">{</span> <span class="token literal-property property">time</span><span class="token operator">:</span> Date<span class="token punctuation">.</span><span class="token function">now</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token comment">// Lifecycle: Called just before our component will be destroyed</span>
	<span class="token function">componentWillUnmount</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token comment">// stop when not renderable</span>
		<span class="token function">clearInterval</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">.</span>timer<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">let</span> time <span class="token operator">=</span> <span class="token keyword">new</span> <span class="token class-name">Date</span><span class="token punctuation">(</span><span class="token keyword">this</span><span class="token punctuation">.</span>state<span class="token punctuation">.</span>time<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">toLocaleTimeString</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>span</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>time<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgQ29tcG9uZW50LCByZW5kZXIgfSBmcm9tICdwcmVhY3QnOwoKCmNsYXNzIENsb2NrIGV4dGVuZHMgQ29tcG9uZW50IHsKCWNvbnN0cnVjdG9yKCkgewoJCXN1cGVyKCk7CgkJdGhpcy5zdGF0ZSA9IHsgdGltZTogRGF0ZS5ub3coKSB9OwoJfQoKCS8vIExpZmVjeWNsZTogQ2FsbGVkIHdoZW5ldmVyIG91ciBjb21wb25lbnQgaXMgY3JlYXRlZAoJY29tcG9uZW50RGlkTW91bnQoKSB7CgkJLy8gdXBkYXRlIHRpbWUgZXZlcnkgc2Vjb25kCgkJdGhpcy50aW1lciA9IHNldEludGVydmFsKCgpID0%2BIHsKCQkJdGhpcy5zZXRTdGF0ZSh7IHRpbWU6IERhdGUubm93KCkgfSk7CgkJfSwgMTAwMCk7Cgl9CgoJLy8gTGlmZWN5Y2xlOiBDYWxsZWQganVzdCBiZWZvcmUgb3VyIGNvbXBvbmVudCB3aWxsIGJlIGRlc3Ryb3llZAoJY29tcG9uZW50V2lsbFVubW91bnQoKSB7CgkJLy8gc3RvcCB3aGVuIG5vdCByZW5kZXJhYmxlCgkJY2xlYXJJbnRlcnZhbCh0aGlzLnRpbWVyKTsKCX0KCglyZW5kZXIoKSB7CgkJbGV0IHRpbWUgPSBuZXcgRGF0ZSh0aGlzLnN0YXRlLnRpbWUpLnRvTG9jYWxlVGltZVN0cmluZygpOwoJCXJldHVybiA8c3Bhbj57dGltZX08L3NwYW4%2BOwoJfQp9CgpyZW5kZXIoPENsb2NrIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			
				<h3 id="lifecycle-methods">
					<a class="fragment-link" href="#lifecycle-methods">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Lifecycle Methods (#lifecycle-methods)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Lifecycle Methods</span>
				</h3><p>In order to have the clock's time update every second, we need to know when <code>&lt;Clock></code> gets mounted to the DOM. <em>If you've used HTML5 Custom Elements, this is similar to the <code>attachedCallback</code> and <code>detachedCallback</code> lifecycle methods.</em> Preact invokes the following lifecycle methods if they are defined for a Component:</p>
<table>
<thead>
<tr>
<th>Lifecycle method</th>
<th>When it gets called</th>
</tr>
</thead>
<tbody><tr>
<td><code>componentWillMount()</code></td>
<td>(deprecated) before the component gets mounted to the DOM</td>
</tr>
<tr>
<td><code>componentDidMount()</code></td>
<td>after the component gets mounted to the DOM</td>
</tr>
<tr>
<td><code>componentWillUnmount()</code></td>
<td>prior to removal from the DOM</td>
</tr>
<tr>
<td><code>componentWillReceiveProps(nextProps, nextContext)</code></td>
<td>before new props get accepted <em>(deprecated)</em></td>
</tr>
<tr>
<td><code>getDerivedStateFromProps(nextProps, prevState)</code></td>
<td>just before <code>shouldComponentUpdate</code>. Return object to update state or <code>null</code> to skip update. Use with care.</td>
</tr>
<tr>
<td><code>shouldComponentUpdate(nextProps, nextState, nextContext)</code></td>
<td>before <code>render()</code>. Return <code>false</code> to skip render</td>
</tr>
<tr>
<td><code>componentWillUpdate(nextProps, nextState, nextContext)</code></td>
<td>before <code>render()</code> <em>(deprecated)</em></td>
</tr>
<tr>
<td><code>getSnapshotBeforeUpdate(prevProps, prevState)</code></td>
<td>called just after <code>render()</code>, but before changes are flushed to the DOM. Return value is passed to <code>componentDidUpdate</code>.</td>
</tr>
<tr>
<td><code>componentDidUpdate(prevProps, prevState, snapshot)</code></td>
<td>after <code>render()</code></td>
</tr>
</tbody></table>
<p>Here's a visual overview of how they relate to each other (originally posted in <a href="https://web.archive.org/web/20191118010106/https://twitter.com/dan_abramov/status/981712092611989509" target="_blank" rel="noopener noreferrer">a tweet</a> by Dan Abramov):</p>
<p><img loading="lazy" decoding="async" src="/guide/components-lifecycle-diagram.png" alt="Diagram of component lifecycle methods"></p>

				<h3 id="error-boundaries">
					<a class="fragment-link" href="#error-boundaries">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Error Boundaries (#error-boundaries)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Error Boundaries</span>
				</h3><p>An error boundary is a component that implements either <code>componentDidCatch()</code> or the static method <code>getDerivedStateFromError()</code> (or both). These are special methods that allow you to catch any errors that happen during rendering and are typically used to provide nicer error messages or other fallback content and save information for logging purposes. It's important to note that error boundaries cannot catch all errors and those thrown in event handlers or asynchronous code (like a <code>fetch()</code> call) need to be handled separately.</p>
<p>When an error is caught, we can use these methods to react to any errors and display a nice error message or any other fallback content.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">class</span> <span class="token class-name">ErrorBoundary</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	<span class="token function">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">super</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token keyword">this</span><span class="token punctuation">.</span>state <span class="token operator">=</span> <span class="token punctuation">{</span> <span class="token literal-property property">errored</span><span class="token operator">:</span> <span class="token boolean">false</span> <span class="token punctuation">}</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token keyword">static</span> <span class="token function">getDerivedStateFromError</span><span class="token punctuation">(</span><span class="token parameter">error</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token punctuation">{</span> <span class="token literal-property property">errored</span><span class="token operator">:</span> <span class="token boolean">true</span> <span class="token punctuation">}</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">componentDidCatch</span><span class="token punctuation">(</span><span class="token parameter">error<span class="token punctuation">,</span> errorInfo</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token function">errorReportingService</span><span class="token punctuation">(</span>error<span class="token punctuation">,</span> errorInfo<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token parameter">props<span class="token punctuation">,</span> state</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">if</span> <span class="token punctuation">(</span>state<span class="token punctuation">.</span>errored<span class="token punctuation">)</span> <span class="token punctuation">{</span>
			<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Something went badly wrong</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span>
		<span class="token keyword">return</span> props<span class="token punctuation">.</span>children<span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgQ29tcG9uZW50LCByZW5kZXIgfSBmcm9tICdwcmVhY3QnOwoKY2xhc3MgRXJyb3JCb3VuZGFyeSBleHRlbmRzIENvbXBvbmVudCB7Cgljb25zdHJ1Y3RvcigpIHsKCQlzdXBlcigpOwoJCXRoaXMuc3RhdGUgPSB7IGVycm9yZWQ6IGZhbHNlIH07Cgl9CgoJc3RhdGljIGdldERlcml2ZWRTdGF0ZUZyb21FcnJvcihlcnJvcikgewoJCXJldHVybiB7IGVycm9yZWQ6IHRydWUgfTsKCX0KCgljb21wb25lbnREaWRDYXRjaChlcnJvciwgZXJyb3JJbmZvKSB7CgkJZXJyb3JSZXBvcnRpbmdTZXJ2aWNlKGVycm9yLCBlcnJvckluZm8pOwoJfQoKCXJlbmRlcihwcm9wcywgc3RhdGUpIHsKCQlpZiAoc3RhdGUuZXJyb3JlZCkgewoJCQlyZXR1cm4gPHA%2BU29tZXRoaW5nIHdlbnQgYmFkbHkgd3Jvbmc8L3A%2BOwoJCX0KCQlyZXR1cm4gcHJvcHMuY2hpbGRyZW47Cgl9Cn0KCnJlbmRlcig8RXJyb3JCb3VuZGFyeSAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK">Run in REPL</a>
				</div>
			
				<h2 id="fragments">
					<a class="fragment-link" href="#fragments">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Fragments (#fragments)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Fragments</span>
				</h2><p>A <code>Fragment</code> allows you to return multiple elements at once. They solve the limitation of JSX where every &quot;block&quot; must have a single root element. You'll often encounter them in combination with lists, tables or with CSS flexbox where any intermediate element would otherwise affect styling.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> Fragment<span class="token punctuation">,</span> render <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">TodoItems</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">A</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">B</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">C</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">const</span> App <span class="token operator">=</span> <span class="token punctuation">(</span>
	<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>ul</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">TodoItems</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">D</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>li</span><span class="token punctuation">></span></span><span class="token plain-text">
	</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>ul</span><span class="token punctuation">></span></span>
<span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token function">render</span><span class="token punctuation">(</span>App<span class="token punctuation">,</span> container<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token comment">// Renders:</span>
<span class="token comment">// &lt;ul></span>
<span class="token comment">//   &lt;li>A&lt;/li></span>
<span class="token comment">//   &lt;li>B&lt;/li></span>
<span class="token comment">//   &lt;li>C&lt;/li></span>
<span class="token comment">//   &lt;li>D&lt;/li></span>
<span class="token comment">// &lt;/ul></span></code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgRnJhZ21lbnQsIHJlbmRlciB9IGZyb20gJ3ByZWFjdCc7CgpmdW5jdGlvbiBUb2RvSXRlbXMoKSB7CglyZXR1cm4gKAoJCTxGcmFnbWVudD4KCQkJPGxpPkE8L2xpPgoJCQk8bGk%2BQjwvbGk%2BCgkJCTxsaT5DPC9saT4KCQk8L0ZyYWdtZW50PgoJKTsKfQoKY29uc3QgQXBwID0gKAoJPHVsPgoJCTxUb2RvSXRlbXMgLz4KCQk8bGk%2BRDwvbGk%2BCgk8L3VsPgopOwoKcmVuZGVyKEFwcCwgY29udGFpbmVyKTsKLy8gUmVuZGVyczoKLy8gPHVsPgovLyAgIDxsaT5BPC9saT4KLy8gICA8bGk%2BQjwvbGk%2BCi8vICAgPGxpPkM8L2xpPgovLyAgIDxsaT5EPC9saT4KLy8gPC91bD4%3D">Run in REPL</a>
				</div>
			<p>Note that most modern transpilers allow you to use a shorter syntax for <code>Fragments</code>. The shorter one is a lot more common and is the one you'll typically encounter.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token comment">// This:</span>
<span class="token keyword">const</span> Foo <span class="token operator">=</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span><span class="token plain-text">foo</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token comment">// ...is the same as this:</span>
<span class="token keyword">const</span> Bar <span class="token operator">=</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span></span><span class="token punctuation">></span></span><span class="token plain-text">foo</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span></span><span class="token punctuation">></span></span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>You can also return arrays from your components:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Columns</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">[</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>td</span><span class="token punctuation">></span></span><span class="token plain-text">Hello</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>td</span><span class="token punctuation">></span></span><span class="token punctuation">,</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>td</span><span class="token punctuation">></span></span><span class="token plain-text">World</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>td</span><span class="token punctuation">></span></span><span class="token punctuation">]</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<p>Don't forget to add keys to <code>Fragments</code> if you create them in a loop:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Glossary</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dl</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token punctuation">{</span>props<span class="token punctuation">.</span>items<span class="token punctuation">.</span><span class="token function">map</span><span class="token punctuation">(</span><span class="token parameter">item</span> <span class="token operator">=></span> <span class="token punctuation">(</span>
				<span class="token comment">// Without a key, Preact has to guess which elements have</span>
				<span class="token comment">// changed when re-rendering.</span>
				<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Fragment</span></span> <span class="token attr-name">key</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>item<span class="token punctuation">.</span>id<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
					</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dt</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>item<span class="token punctuation">.</span>term<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dt</span><span class="token punctuation">></span></span><span class="token plain-text">
					</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>dd</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>item<span class="token punctuation">.</span>description<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dd</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Fragment</span></span><span class="token punctuation">></span></span>
			<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">}</span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>dl</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/siddharthkp" target="_blank" rel="noopener noreferrer">@siddharthkp</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
