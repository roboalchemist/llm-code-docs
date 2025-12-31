# Source: https://preactjs.com/guide/v10/hooks

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="icon" href="/favicon.ico">
		<title>Hooks – Preact Guide</title>
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
	<meta name="description" content="Hooks in Preact allow you to compose behaviours together and re-use that logic in different components">
<meta property="og:url" content="https://preactjs.com/guide/v10/hooks">
<meta property="og:title" content="Hooks – Preact Guide">
<meta property="og:description" content="Hooks in Preact allow you to compose behaviours together and re-use that logic in different components">
<link rel="preload" href="/.netlify/functions/release?repo=preact" as="fetch" fetchpriority="low">
<link rel="preload" href="/contributors.json" as="fetch" fetchpriority="low">
<link rel="preload" href="/content/en/guide/v10/hooks.json" as="fetch" fetchpriority="low">
<script>ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga('set','dimension1','master');onerror=function(e,f,l,c){ga('send','event','exception',e,f+':'+l+':'+c)}</script></head>
	<body class="banner">
		<div id="app"><header class="_header_nxrmc_38 "><div class="_banner_nxrmc_1"><a href="https://www.stopputin.net/">We stand with Ukraine. <b>Show your support</b> 🇺🇦</a></div><div class="_outer_nxrmc_24"><div class="_inner_nxrmc_301"><nav><a href="/" class="home" aria-label="Home"><svg aria-label="Preact Logo" width="34px" height="34px" viewBox="-256 -256 512 512" style="display:inline-block; margin:-.25em 0 0; vertical-align:middle;"><path d="M0,-256 221.7025033688164,-128 221.7025033688164,128 0,256 -221.7025033688164,128 -221.7025033688164,-128z" fill="white"></path><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(52)"></ellipse><ellipse cx="0" cy="0" rx="75px" ry="196px" stroke-width="16px" stroke-dasharray="387 60" stroke-dashoffset="0" fill="none" stroke="#673ab8" transform="rotate(-52)"></ellipse><circle cx="0" cy="0" r="34" fill="#673ab8"></circle></svg>Preact</a><a href="/tutorial">Tutorial</a><a href="/guide/v10/getting-started" class="_current_nxrmc_92 ">Guide</a><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false">About</button><nav aria-label="submenu" aria-hidden="true"><a href="/about/we-are-using">Companies using Preact</a><a href="/about/libraries-addons">Libraries &amp; Add-ons</a><a href="/about/demos-examples">Demos &amp; Examples</a><a href="/about/project-goals">Project Goals</a><a href="/about/browser-support">Browser Support</a></nav></div><a href="/blog">Blog</a><a href="/repl">REPL</a></nav><div class="_search_nxrmc_479"><button type="button" aria-label="Search" class="DocSearch DocSearch-Button"><span class="DocSearch-Button-Container"><span class="DocSearch-Button-Placeholder">Search</span></span></button></div><div class="_social_nxrmc_321"><a href="https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0" class="_socialItem_nxrmc_357 _release_nxrmc_396">v11.0.0-beta.0</a><a class="_socialItem_nxrmc_357" aria-label="Browse the code on GitHub" href="https://github.com/preactjs/preact" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#github"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Twitter" href="https://twitter.com/preactjs" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 34 27.646"><use href="/icons.svg#twitter"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Follow us on Bluesky" href="https://bsky.app/profile/preactjs.com" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 568 501"><use href="/icons.svg#bluesky"></use></svg></a><a class="_socialItem_nxrmc_357" aria-label="Chat with us on Slack" href="http://chat.preactjs.com/" target="_blank" rel="noopener noreferrer"><svg aria-hidden="true" viewBox="0 0 512 512"><use href="/icons.svg#slack"></use></svg></a></div><div class="_translation_nxrmc_322"><div class="_navGroup_nxrmc_78" data-open="false"><button aria-haspopup="true" aria-expanded="false" aria-label="Select your language"><svg aria-hidden="true" viewBox="0 0 24 24"><use href="/icons.svg#i18n"></use></svg></button><nav aria-label="submenu" aria-hidden="true"></nav></div></div><div class="_hamburger_nxrmc_402" data-open="false"><div class="_hb1_nxrmc_444"></div><div class="_hb2_nxrmc_445"></div><div class="_hb3_nxrmc_446"></div></div></div></div><a href="https://opencollective.com/preact" target="_blank" rel="noopener noreferrer" class="_corner_1vho8_1"><div class="_cornerText_1vho8_31">Help<br>Support Us</div></a></header><main><loading-bar></loading-bar><!--$s--><div class="_page_sqynl_1 _withSidebar_sqynl_119"><div class="_outer_sqynl_111"><div class="_sidebarWrap_sqynl_115"><div class="_wrapper_14rnv_1" data-open="false"><button class="_toggle_14rnv_6">Guide</button><aside class="_sidebar_14rnv_58"><div class="_sidebarInner_14rnv_93"><label class="_root_1cgs3_1">Version: <select class="_select_1cgs3_8"><option value="v11">11.x (preview)</option><option selected value="v10">10.x (current)</option><option value="v8">8.x</option></select></label><nav class="_toc_1ttwe_1 "><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Introduction</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/getting-started" class="_link_1ttwe_16  ">Getting Started</a><a href="/guide/v10/whats-new" class="_link_1ttwe_16  ">What's new?</a><a href="/guide/v10/upgrade-guide" class="_link_1ttwe_16  ">Upgrading from 8.x</a><a href="/guide/v10/differences-to-react" class="_link_1ttwe_16  ">Differences to React</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Essentials</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/components" class="_link_1ttwe_16  ">Components</a><a href="/guide/v10/hooks" class="_link_1ttwe_16 _linkActive_1ttwe_43 ">Hooks</a><a href="/guide/v10/signals" class="_link_1ttwe_16  ">Signals</a><a href="/guide/v10/forms" class="_link_1ttwe_16  ">Forms</a><a href="/guide/v10/refs" class="_link_1ttwe_16  ">References</a><a href="/guide/v10/context" class="_link_1ttwe_16  ">Context</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Debug &amp; Test</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/debugging" class="_link_1ttwe_16  ">Debugging Tools</a><a href="/guide/v10/preact-testing-library" class="_link_1ttwe_16  ">Preact Testing Library</a><a href="/guide/v10/unit-testing-with-enzyme" class="_link_1ttwe_16  ">Unit Testing with Enzyme</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Advanced</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/api-reference" class="_link_1ttwe_16  ">API Reference</a><a href="/guide/v10/web-components" class="_link_1ttwe_16  ">Web Components</a><a href="/guide/v10/server-side-rendering" class="_link_1ttwe_16  ">Server-Side Rendering</a><a href="/guide/v10/options" class="_link_1ttwe_16  ">Option Hooks</a><a href="/guide/v10/typescript" class="_link_1ttwe_16  ">TypeScript</a><a href="/guide/v10/no-build-workflows" class="_link_1ttwe_16  ">No-Build Workflows</a></div><h3 class="_category_1ttwe_50 _level-2_1ttwe_79">Libraries</h3><div class="_accordionBody_1ttwe_68"><a href="/guide/v10/preact-iso" class="_link_1ttwe_16  ">preact-iso</a><a href="/guide/v10/preact-custom-element" class="_link_1ttwe_16  ">preact-custom-element</a><a href="/guide/v10/preact-root-fragment" class="_link_1ttwe_16  ">preact-root-fragment</a></div></nav></div></aside></div></div><div class="_inner_sqynl_59"><div class="_wrapper_1gw8e_1"><a class="_edit_1gw8e_13" href="https://github.com/preactjs/preact-www/tree/master/content/en/guide/v10/hooks.md" target="_blank" rel="noopener noreferrer">Edit this Page</a></div><content-region name="/guide/v10/hooks" can-edit><div class="markup"><h1>Hooks</h1><p>The Hooks API is an alternative way to write components in Preact. Hooks allow you to compose state and side effects, reusing stateful logic much more easily than with class components.</p>
<p>If you've worked with class components in Preact for a while, you may be familiar with patterns like &quot;render props&quot; and &quot;higher order components&quot; that try to solve these challenges. These solutions have tended to make code harder to follow and more abstract. The hooks API makes it possible to neatly extract the logic for state and side effects, and also simplifies unit testing that logic independently from the components that rely on it.</p>
<p>Hooks can be used in any component, and avoid many pitfalls of the <code>this</code> keyword relied on by the class components API. Instead of accessing properties from the component instance, hooks rely on closures. This makes them value-bound and eliminates a number of stale data problems that can occur when dealing with asynchronous state updates.</p>
<p>There are two ways to import hooks: from <code>preact/hooks</code> or <code>preact/compat</code>.</p>
<hr>
<nav><ul><li><a href="#introduction">Introduction</a></li><li><a href="#the-dependency-argument">The dependency argument</a></li><li><a href="#stateful-hooks">Stateful hooks</a><ul><li><a href="#usestate">useState</a></li><li><a href="#usereducer">useReducer</a></li></ul></li><li><a href="#memoization">Memoization</a><ul><li><a href="#usememo">useMemo</a></li><li><a href="#usecallback">useCallback</a></li></ul></li><li><a href="#refs">Refs</a><ul><li><a href="#useref">useRef</a></li><li><a href="#useimperativehandle">useImperativeHandle</a></li></ul></li><li><a href="#usecontext">useContext</a></li><li><a href="#side-effects">Side-Effects</a><ul><li><a href="#useeffect">useEffect</a></li><li><a href="#uselayouteffect">useLayoutEffect</a></li><li><a href="#useerrorboundary">useErrorBoundary</a></li></ul></li><li><a href="#utility-hooks">Utility hooks</a><ul><li><a href="#useid">useId</a></li><li><a href="#usedebugvalue">useDebugValue</a></li></ul></li><li><a href="#compat-specific-hooks">Compat-specific hooks</a><ul><li><a href="#usesyncexternalstore">useSyncExternalStore</a></li><li><a href="#usedeferredvalue">useDeferredValue</a></li><li><a href="#usetransition">useTransition</a></li><li><a href="#useinsertioneffect">useInsertionEffect</a></li></ul></li></ul></nav><hr>

				<h2 id="introduction">
					<a class="fragment-link" href="#introduction">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Introduction (#introduction)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Introduction</span>
				</h2><p>The easiest way to understand hooks is to compare them to equivalent class-based Components.</p>
<p>We'll use a simple counter component as our example, which renders a number and a button that increases it by one:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">class</span> <span class="token class-name">Counter</span> <span class="token keyword">extends</span> <span class="token class-name">Component</span> <span class="token punctuation">{</span>
	state <span class="token operator">=</span> <span class="token punctuation">{</span>
		<span class="token literal-property property">value</span><span class="token operator">:</span> <span class="token number">0</span>
	<span class="token punctuation">}</span><span class="token punctuation">;</span>

	<span class="token function-variable function">increment</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token keyword">this</span><span class="token punctuation">.</span><span class="token function">setState</span><span class="token punctuation">(</span><span class="token parameter">prev</span> <span class="token operator">=></span> <span class="token punctuation">(</span><span class="token punctuation">{</span> <span class="token literal-property property">value</span><span class="token operator">:</span> prev<span class="token punctuation">.</span>value <span class="token operator">+</span> <span class="token number">1</span> <span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">;</span>

	<span class="token function">render</span><span class="token punctuation">(</span><span class="token parameter">props<span class="token punctuation">,</span> state</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token punctuation">(</span>
			<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Counter: </span><span class="token punctuation">{</span>state<span class="token punctuation">.</span>value<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token keyword">this</span><span class="token punctuation">.</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
		<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBDb21wb25lbnQgfSBmcm9tICdwcmVhY3QnOwoKY2xhc3MgQ291bnRlciBleHRlbmRzIENvbXBvbmVudCB7CglzdGF0ZSA9IHsKCQl2YWx1ZTogMAoJfTsKCglpbmNyZW1lbnQgPSAoKSA9PiB7CgkJdGhpcy5zZXRTdGF0ZShwcmV2ID0%2BICh7IHZhbHVlOiBwcmV2LnZhbHVlICsgMSB9KSk7Cgl9OwoKCXJlbmRlcihwcm9wcywgc3RhdGUpIHsKCQlyZXR1cm4gKAoJCQk8ZGl2PgoJCQkJPHA%2BQ291bnRlcjoge3N0YXRlLnZhbHVlfTwvcD4KCQkJCTxidXR0b24gb25DbGljaz17dGhpcy5pbmNyZW1lbnR9PkluY3JlbWVudDwvYnV0dG9uPgoJCQk8L2Rpdj4KCQkpOwoJfQp9CgpyZW5kZXIoPENvdW50ZXIgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKSk7Cg%3D%3D">Run in REPL</a>
				</div>
			<p>Now, here's an equivalent function component built with hooks:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Counter</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>value<span class="token punctuation">,</span> setValue<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> increment <span class="token operator">=</span> <span class="token function">useCallback</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token function">setValue</span><span class="token punctuation">(</span>value <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>value<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Counter: </span><span class="token punctuation">{</span>value<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgdXNlU3RhdGUsIHVzZUNhbGxiYWNrIH0gZnJvbSAncHJlYWN0L2hvb2tzJzsKaW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmZ1bmN0aW9uIENvdW50ZXIoKSB7Cgljb25zdCBbdmFsdWUsIHNldFZhbHVlXSA9IHVzZVN0YXRlKDApOwoJY29uc3QgaW5jcmVtZW50ID0gdXNlQ2FsbGJhY2soKCkgPT4gewoJCXNldFZhbHVlKHZhbHVlICsgMSk7Cgl9LCBbdmFsdWVdKTsKCglyZXR1cm4gKAoJCTxkaXY%2BCgkJCTxwPkNvdW50ZXI6IHt2YWx1ZX08L3A%2BCgkJCTxidXR0b24gb25DbGljaz17aW5jcmVtZW50fT5JbmNyZW1lbnQ8L2J1dHRvbj4KCQk8L2Rpdj4KCSk7Cn0KCnJlbmRlcig8Q291bnRlciAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK">Run in REPL</a>
				</div>
			<p>At this point they seem pretty similar, however we can further simplify the hooks version.</p>
<p>Let's extract the counter logic into a custom hook, making it easily reusable across components:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">useCounter</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>value<span class="token punctuation">,</span> setValue<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> increment <span class="token operator">=</span> <span class="token function">useCallback</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token function">setValue</span><span class="token punctuation">(</span>value <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>value<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">{</span> value<span class="token punctuation">,</span> increment <span class="token punctuation">}</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">// First counter</span>
<span class="token keyword">function</span> <span class="token function">CounterA</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">{</span> value<span class="token punctuation">,</span> increment <span class="token punctuation">}</span> <span class="token operator">=</span> <span class="token function">useCounter</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Counter A: </span><span class="token punctuation">{</span>value<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">// Second counter which renders a different output.</span>
<span class="token keyword">function</span> <span class="token function">CounterB</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">{</span> value<span class="token punctuation">,</span> increment <span class="token punctuation">}</span> <span class="token operator">=</span> <span class="token function">useCounter</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>h1</span><span class="token punctuation">></span></span><span class="token plain-text">Counter B: </span><span class="token punctuation">{</span>value<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">I'm a nice counter</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgdXNlU3RhdGUsIHVzZUNhbGxiYWNrIH0gZnJvbSAncHJlYWN0L2hvb2tzJzsKaW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmZ1bmN0aW9uIHVzZUNvdW50ZXIoKSB7Cgljb25zdCBbdmFsdWUsIHNldFZhbHVlXSA9IHVzZVN0YXRlKDApOwoJY29uc3QgaW5jcmVtZW50ID0gdXNlQ2FsbGJhY2soKCkgPT4gewoJCXNldFZhbHVlKHZhbHVlICsgMSk7Cgl9LCBbdmFsdWVdKTsKCXJldHVybiB7IHZhbHVlLCBpbmNyZW1lbnQgfTsKfQoKLy8gRmlyc3QgY291bnRlcgpmdW5jdGlvbiBDb3VudGVyQSgpIHsKCWNvbnN0IHsgdmFsdWUsIGluY3JlbWVudCB9ID0gdXNlQ291bnRlcigpOwoJcmV0dXJuICgKCQk8ZGl2PgoJCQk8cD5Db3VudGVyIEE6IHt2YWx1ZX08L3A%2BCgkJCTxidXR0b24gb25DbGljaz17aW5jcmVtZW50fT5JbmNyZW1lbnQ8L2J1dHRvbj4KCQk8L2Rpdj4KCSk7Cn0KCi8vIFNlY29uZCBjb3VudGVyIHdoaWNoIHJlbmRlcnMgYSBkaWZmZXJlbnQgb3V0cHV0LgpmdW5jdGlvbiBDb3VudGVyQigpIHsKCWNvbnN0IHsgdmFsdWUsIGluY3JlbWVudCB9ID0gdXNlQ291bnRlcigpOwoJcmV0dXJuICgKCQk8ZGl2PgoJCQk8aDE%2BQ291bnRlciBCOiB7dmFsdWV9PC9oMT4KCQkJPHA%2BSSdtIGEgbmljZSBjb3VudGVyPC9wPgoJCQk8YnV0dG9uIG9uQ2xpY2s9e2luY3JlbWVudH0%2BSW5jcmVtZW50PC9idXR0b24%2BCgkJPC9kaXY%2BCgkpOwp9CgpyZW5kZXIoCgk8ZGl2PgoJCTxDb3VudGVyQSAvPgoJCTxDb3VudGVyQiAvPgoJPC9kaXY%2BLAoJZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpCik7Cg%3D%3D">Run in REPL</a>
				</div>
			<p>Note that both <code>CounterA</code> and <code>CounterB</code> are completely independent of each other. They both use the <code>useCounter()</code> custom hook, but each has its own instance of that hook's associated state.</p>
<blockquote>
<p>Thinking this looks a little strange? You're not alone!</p>
<p>It took many of us a while to grow accustomed to this approach.</p>
</blockquote>

				<h2 id="the-dependency-argument">
					<a class="fragment-link" href="#the-dependency-argument">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: The dependency argument (#the-dependency-argument)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>The dependency argument</span>
				</h2><p>Many hooks accept an argument that can be used to limit when a hook should be updated. Preact inspects each value in a dependency array and checks to see if it has changed since the last time a hook was called. When the dependency argument is not specified, the hook is always executed.</p>
<p>In our <code>useCounter()</code> implementation above, we passed an array of dependencies to <code>useCallback()</code>:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">useCounter</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>value<span class="token punctuation">,</span> setValue<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> increment <span class="token operator">=</span> <span class="token function">useCallback</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token function">setValue</span><span class="token punctuation">(</span>value <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>value<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span> <span class="token comment">// &lt;-- the dependency array</span>
	<span class="token keyword">return</span> <span class="token punctuation">{</span> value<span class="token punctuation">,</span> increment <span class="token punctuation">}</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<p>Passing <code>value</code> here causes <code>useCallback</code> to return a new function reference whenever <code>value</code> changes.
This is necessary in order to avoid &quot;stale closures&quot;, where the callback would always reference the first render's <code>value</code> variable from when it was created, causing <code>increment</code> to always set a value of <code>1</code>.</p>
<blockquote>
<p>This creates a new <code>increment</code> callback every time <code>value</code> changes.
For performance reasons, it's often better to use a <a href="#usestate">callback</a> to update state values rather than retaining the current value using dependencies.</p>
</blockquote>

				<h2 id="stateful-hooks">
					<a class="fragment-link" href="#stateful-hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Stateful hooks (#stateful-hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Stateful hooks</span>
				</h2><p>Here we'll see how we can introduce stateful logic into functional components.</p>
<p>Prior to the introduction of hooks, class components were required anywhere state was needed.</p>

				<h3 id="usestate">
					<a class="fragment-link" href="#usestate">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useState (#usestate)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useState</span>
				</h3><p>This hook accepts an argument, this will be the initial state. When
invoked this hook returns an array of two variables. The first being
the current state and the second being the setter for our state.</p>
<p>Our setter behaves similar to the setter of our classic state.
It accepts a value or a function with the currentState as argument.</p>
<p>When you call the setter and the state is different, it will trigger
a rerender starting from the component where that useState has been used.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useState <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/hooks'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> <span class="token function-variable function">Counter</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> setCount<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> <span class="token function-variable function">increment</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">setCount</span><span class="token punctuation">(</span>count <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token comment">// You can also pass a callback to the setter</span>
	<span class="token keyword">const</span> <span class="token function-variable function">decrement</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">setCount</span><span class="token punctuation">(</span><span class="token parameter">currentCount</span> <span class="token operator">=></span> currentCount <span class="token operator">-</span> <span class="token number">1</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Count: </span><span class="token punctuation">{</span>count<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>increment<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Increment</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>decrement<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Decrement</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmltcG9ydCB7IHVzZVN0YXRlIH0gZnJvbSAncHJlYWN0L2hvb2tzJzsKCmNvbnN0IENvdW50ZXIgPSAoKSA9PiB7Cgljb25zdCBbY291bnQsIHNldENvdW50XSA9IHVzZVN0YXRlKDApOwoJY29uc3QgaW5jcmVtZW50ID0gKCkgPT4gc2V0Q291bnQoY291bnQgKyAxKTsKCS8vIFlvdSBjYW4gYWxzbyBwYXNzIGEgY2FsbGJhY2sgdG8gdGhlIHNldHRlcgoJY29uc3QgZGVjcmVtZW50ID0gKCkgPT4gc2V0Q291bnQoY3VycmVudENvdW50ID0%2BIGN1cnJlbnRDb3VudCAtIDEpOwoKCXJldHVybiAoCgkJPGRpdj4KCQkJPHA%2BQ291bnQ6IHtjb3VudH08L3A%2BCgkJCTxidXR0b24gb25DbGljaz17aW5jcmVtZW50fT5JbmNyZW1lbnQ8L2J1dHRvbj4KCQkJPGJ1dHRvbiBvbkNsaWNrPXtkZWNyZW1lbnR9PkRlY3JlbWVudDwvYnV0dG9uPgoJCTwvZGl2PgoJKTsKfTsKCnJlbmRlcig8Q291bnRlciAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK">Run in REPL</a>
				</div>
			<blockquote>
<p>When our initial state is expensive it's better to pass a function instead of a value.</p>
</blockquote>

				<h3 id="usereducer">
					<a class="fragment-link" href="#usereducer">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useReducer (#usereducer)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useReducer</span>
				</h3><p>The <code>useReducer</code> hook has a close resemblance to <a href="https://redux.js.org/" target="_blank" rel="noopener noreferrer">redux</a>. Compared to <a href="#usestate">useState</a> it's easier to use when you have complex state logic where the next state depends on the previous one.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useReducer <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/hooks'</span><span class="token punctuation">;</span>

<span class="token keyword">const</span> initialState <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">;</span>
<span class="token keyword">const</span> <span class="token function-variable function">reducer</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token parameter">state<span class="token punctuation">,</span> action</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
	<span class="token keyword">switch</span> <span class="token punctuation">(</span>action<span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">case</span> <span class="token string">'increment'</span><span class="token operator">:</span>
			<span class="token keyword">return</span> state <span class="token operator">+</span> <span class="token number">1</span><span class="token punctuation">;</span>
		<span class="token keyword">case</span> <span class="token string">'decrement'</span><span class="token operator">:</span>
			<span class="token keyword">return</span> state <span class="token operator">-</span> <span class="token number">1</span><span class="token punctuation">;</span>
		<span class="token keyword">case</span> <span class="token string">'reset'</span><span class="token operator">:</span>
			<span class="token keyword">return</span> <span class="token number">0</span><span class="token punctuation">;</span>
		<span class="token keyword">default</span><span class="token operator">:</span>
			<span class="token keyword">throw</span> <span class="token keyword">new</span> <span class="token class-name">Error</span><span class="token punctuation">(</span><span class="token string">'Unexpected action'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">Counter</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token comment">// Returns the current state and a dispatch function to</span>
	<span class="token comment">// trigger an action</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> dispatch<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useReducer</span><span class="token punctuation">(</span>reducer<span class="token punctuation">,</span> initialState<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token punctuation">{</span>count<span class="token punctuation">}</span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">dispatch</span><span class="token punctuation">(</span><span class="token string">'increment'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">+1</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">dispatch</span><span class="token punctuation">(</span><span class="token string">'decrement'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">-1</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">dispatch</span><span class="token punctuation">(</span><span class="token string">'reset'</span><span class="token punctuation">)</span><span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">reset</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmltcG9ydCB7IHVzZVJlZHVjZXIgfSBmcm9tICdwcmVhY3QvaG9va3MnOwoKY29uc3QgaW5pdGlhbFN0YXRlID0gMDsKY29uc3QgcmVkdWNlciA9IChzdGF0ZSwgYWN0aW9uKSA9PiB7Cglzd2l0Y2ggKGFjdGlvbikgewoJCWNhc2UgJ2luY3JlbWVudCc6CgkJCXJldHVybiBzdGF0ZSArIDE7CgkJY2FzZSAnZGVjcmVtZW50JzoKCQkJcmV0dXJuIHN0YXRlIC0gMTsKCQljYXNlICdyZXNldCc6CgkJCXJldHVybiAwOwoJCWRlZmF1bHQ6CgkJCXRocm93IG5ldyBFcnJvcignVW5leHBlY3RlZCBhY3Rpb24nKTsKCX0KfTsKCmZ1bmN0aW9uIENvdW50ZXIoKSB7CgkvLyBSZXR1cm5zIHRoZSBjdXJyZW50IHN0YXRlIGFuZCBhIGRpc3BhdGNoIGZ1bmN0aW9uIHRvCgkvLyB0cmlnZ2VyIGFuIGFjdGlvbgoJY29uc3QgW2NvdW50LCBkaXNwYXRjaF0gPSB1c2VSZWR1Y2VyKHJlZHVjZXIsIGluaXRpYWxTdGF0ZSk7CglyZXR1cm4gKAoJCTxkaXY%2BCgkJCXtjb3VudH0KCQkJPGJ1dHRvbiBvbkNsaWNrPXsoKSA9PiBkaXNwYXRjaCgnaW5jcmVtZW50Jyl9PisxPC9idXR0b24%2BCgkJCTxidXR0b24gb25DbGljaz17KCkgPT4gZGlzcGF0Y2goJ2RlY3JlbWVudCcpfT4tMTwvYnV0dG9uPgoJCQk8YnV0dG9uIG9uQ2xpY2s9eygpID0%2BIGRpc3BhdGNoKCdyZXNldCcpfT5yZXNldDwvYnV0dG9uPgoJCTwvZGl2PgoJKTsKfQoKcmVuZGVyKDxDb3VudGVyIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			
				<h2 id="memoization">
					<a class="fragment-link" href="#memoization">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Memoization (#memoization)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Memoization</span>
				</h2><p>In UI programming there is often some state or result that's expensive to calculate. Memoization can cache the results of that calculation allowing it to be reused when the same input is used.</p>

				<h3 id="usememo">
					<a class="fragment-link" href="#usememo">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useMemo (#usememo)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useMemo</span>
				</h3><p>With the <code>useMemo</code> hook we can memoize the results of that computation and only recalculate it when one of the dependencies changes.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> memoized <span class="token operator">=</span> <span class="token function">useMemo</span><span class="token punctuation">(</span>
	<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">expensive</span><span class="token punctuation">(</span>a<span class="token punctuation">,</span> b<span class="token punctuation">)</span><span class="token punctuation">,</span>
	<span class="token comment">// Only re-run the expensive function when any of these</span>
	<span class="token comment">// dependencies change</span>
	<span class="token punctuation">[</span>a<span class="token punctuation">,</span> b<span class="token punctuation">]</span>
<span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<blockquote>
<p>Don't run any effectful code inside <code>useMemo</code>. Side-effects belong in <code>useEffect</code>.</p>
</blockquote>

				<h3 id="usecallback">
					<a class="fragment-link" href="#usecallback">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useCallback (#usecallback)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useCallback</span>
				</h3><p>The <code>useCallback</code> hook can be used to ensure that the returned function will remain referentially equal for as long as no dependencies have changed. This can be used to optimize updates of child components when they rely on referential equality to skip updates (e.g. <code>shouldComponentUpdate</code>).</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> onClick <span class="token operator">=</span> <span class="token function">useCallback</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> console<span class="token punctuation">.</span><span class="token function">log</span><span class="token punctuation">(</span>a<span class="token punctuation">,</span> b<span class="token punctuation">)</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>a<span class="token punctuation">,</span> b<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<blockquote>
<p>Fun fact: <code>useCallback(fn, deps)</code> is equivalent to <code>useMemo(() => fn, deps)</code>.</p>
</blockquote>

				<h2 id="refs">
					<a class="fragment-link" href="#refs">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Refs (#refs)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Refs</span>
				</h2><p><strong>Ref</strong>erences are stable, local values that persist across rerenders but don't cause rerenders themselves. See <a href="/guide/v10/refs">Refs</a> for more information &amp; examples.</p>

				<h3 id="useref">
					<a class="fragment-link" href="#useref">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useRef (#useref)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useRef</span>
				</h3><p>To create a stable reference to a DOM node or a value that persists between renders, we can use the <code>useRef</code> hook. It works similarly to <a href="/guide/v10/refs#createref">createRef</a>.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">Foo</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token comment">// Initialize useRef with an initial value of `null`</span>
	<span class="token keyword">const</span> input <span class="token operator">=</span> <span class="token function">useRef</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">const</span> <span class="token function-variable function">onClick</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> input<span class="token punctuation">.</span>current <span class="token operator">&amp;&amp;</span> input<span class="token punctuation">.</span>current<span class="token punctuation">.</span><span class="token function">focus</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">ref</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>input<span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>onClick<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Focus input</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgdXNlUmVmIH0gZnJvbSAncHJlYWN0L2hvb2tzJzsKaW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmZ1bmN0aW9uIEZvbygpIHsKCS8vIEluaXRpYWxpemUgdXNlUmVmIHdpdGggYW4gaW5pdGlhbCB2YWx1ZSBvZiBgbnVsbGAKCWNvbnN0IGlucHV0ID0gdXNlUmVmKG51bGwpOwoJY29uc3Qgb25DbGljayA9ICgpID0%2BIGlucHV0LmN1cnJlbnQgJiYgaW5wdXQuY3VycmVudC5mb2N1cygpOwoKCXJldHVybiAoCgkJPD4KCQkJPGlucHV0IHJlZj17aW5wdXR9IC8%2BCgkJCTxidXR0b24gb25DbGljaz17b25DbGlja30%2BRm9jdXMgaW5wdXQ8L2J1dHRvbj4KCQk8Lz4KCSk7Cn0KCnJlbmRlcig8Rm9vIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			<blockquote>
<p>Be careful not to confuse <code>useRef</code> with <code>createRef</code>.</p>
</blockquote>

				<h3 id="useimperativehandle">
					<a class="fragment-link" href="#useimperativehandle">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useImperativeHandle (#useimperativehandle)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useImperativeHandle</span>
				</h3><p>To mutate a ref that is passed into a child component we can use the <code>useImperativeHandle</code> hook. It takes three arguments: the ref to mutate, a function to execute that will return the new ref value, and a dependency array to determine when to rerun.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">MyInput</span><span class="token punctuation">(</span><span class="token parameter"><span class="token punctuation">{</span> inputRef <span class="token punctuation">}</span></span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> ref <span class="token operator">=</span> <span class="token function">useRef</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token function">useImperativeHandle</span><span class="token punctuation">(</span>
		inputRef<span class="token punctuation">,</span>
		<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
			<span class="token keyword">return</span> <span class="token punctuation">{</span>
				<span class="token comment">// Only expose `.focus()`, don't give direct access to the DOM node</span>
				<span class="token function">focus</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
					ref<span class="token punctuation">.</span>current<span class="token punctuation">.</span><span class="token function">focus</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
				<span class="token punctuation">}</span>
			<span class="token punctuation">}</span><span class="token punctuation">;</span>
		<span class="token punctuation">}</span><span class="token punctuation">,</span>
		<span class="token punctuation">[</span><span class="token punctuation">]</span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>label</span><span class="token punctuation">></span></span><span class="token plain-text">
			Name: </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">ref</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>ref<span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>label</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> inputRef <span class="token operator">=</span> <span class="token function">useRef</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">const</span> <span class="token function-variable function">handleClick</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		inputRef<span class="token punctuation">.</span>current<span class="token punctuation">.</span><span class="token function">focus</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">MyInput</span></span> <span class="token attr-name">inputRef</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>inputRef<span class="token punctuation">}</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>handleClick<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Click To Edit</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlUmVmLCB1c2VJbXBlcmF0aXZlSGFuZGxlLCB1c2VTdGF0ZSB9IGZyb20gJ3ByZWFjdC9ob29rcyc7CgpmdW5jdGlvbiBNeUlucHV0KHsgaW5wdXRSZWYgfSkgewoJY29uc3QgcmVmID0gdXNlUmVmKG51bGwpOwoJdXNlSW1wZXJhdGl2ZUhhbmRsZSgKCQlpbnB1dFJlZiwKCQkoKSA9PiB7CgkJCXJldHVybiB7CgkJCQkvLyBPbmx5IGV4cG9zZSBgLmZvY3VzKClgLCBkb24ndCBnaXZlIGRpcmVjdCBhY2Nlc3MgdG8gdGhlIERPTSBub2RlCgkJCQlmb2N1cygpIHsKCQkJCQlyZWYuY3VycmVudC5mb2N1cygpOwoJCQkJfQoJCQl9OwoJCX0sCgkJW10KCSk7CgoJcmV0dXJuICgKCQk8bGFiZWw%2BCgkJCU5hbWU6IDxpbnB1dCByZWY9e3JlZn0gLz4KCQk8L2xhYmVsPgoJKTsKfQoKZnVuY3Rpb24gQXBwKCkgewoJY29uc3QgaW5wdXRSZWYgPSB1c2VSZWYobnVsbCk7CgoJY29uc3QgaGFuZGxlQ2xpY2sgPSAoKSA9PiB7CgkJaW5wdXRSZWYuY3VycmVudC5mb2N1cygpOwoJfTsKCglyZXR1cm4gKAoJCTxkaXY%2BCgkJCTxNeUlucHV0IGlucHV0UmVmPXtpbnB1dFJlZn0gLz4KCQkJPGJ1dHRvbiBvbkNsaWNrPXtoYW5kbGVDbGlja30%2BQ2xpY2sgVG8gRWRpdDwvYnV0dG9uPgoJCTwvZGl2PgoJKTsKfQoKcmVuZGVyKDxBcHAgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKSk7Cg%3D%3D">Run in REPL</a>
				</div>
			
				<h2 id="usecontext">
					<a class="fragment-link" href="#usecontext">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useContext (#usecontext)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useContext</span>
				</h2><p>To access context in a functional component we can use the <code>useContext</code> hook, without any higher-order or wrapper components. The first argument must be the context object that's created from a <code>createContext</code> call.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> Theme <span class="token operator">=</span> <span class="token function">createContext</span><span class="token punctuation">(</span><span class="token string">'light'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">DisplayTheme</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> theme <span class="token operator">=</span> <span class="token function">useContext</span><span class="token punctuation">(</span>Theme<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Active theme: </span><span class="token punctuation">{</span>theme<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token comment">// ...later</span>
<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">Theme.Provider</span></span> <span class="token attr-name">value</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span>light<span class="token punctuation">&quot;</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">OtherComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span><span class="token class-name">DisplayTheme</span></span> <span class="token punctuation">/></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">OtherComponent</span></span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span><span class="token class-name">Theme.Provider</span></span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgcmVuZGVyLCBjcmVhdGVDb250ZXh0IH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlQ29udGV4dCB9IGZyb20gJ3ByZWFjdC9ob29rcyc7Cgpjb25zdCBPdGhlckNvbXBvbmVudCA9IHByb3BzID0%2BIHByb3BzLmNoaWxkcmVuOwoKY29uc3QgVGhlbWUgPSBjcmVhdGVDb250ZXh0KCdsaWdodCcpOwoKZnVuY3Rpb24gRGlzcGxheVRoZW1lKCkgewoJY29uc3QgdGhlbWUgPSB1c2VDb250ZXh0KFRoZW1lKTsKCXJldHVybiA8cD5BY3RpdmUgdGhlbWU6IHt0aGVtZX08L3A%2BOwp9CgovLyAuLi5sYXRlcgpmdW5jdGlvbiBBcHAoKSB7CglyZXR1cm4gKAoJCTxUaGVtZS5Qcm92aWRlciB2YWx1ZT0ibGlnaHQiPgoJCQk8T3RoZXJDb21wb25lbnQ%2BCgkJCQk8RGlzcGxheVRoZW1lIC8%2BCgkJCTwvT3RoZXJDb21wb25lbnQ%2BCgkJPC9UaGVtZS5Qcm92aWRlcj4KCSk7Cn0KCnJlbmRlcig8QXBwIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			
				<h2 id="side-effects">
					<a class="fragment-link" href="#side-effects">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Side-Effects (#side-effects)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Side-Effects</span>
				</h2><p>Side-Effects are at the heart of many modern Apps. Whether you want to fetch some data from an API or trigger an effect on the document, you'll find that the <code>useEffect</code> fits nearly all your needs. It's one of the main advantages of the hooks API, that it reshapes your mind into thinking in effects instead of a component's lifecycle.</p>

				<h3 id="useeffect">
					<a class="fragment-link" href="#useeffect">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useEffect (#useeffect)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useEffect</span>
				</h3><p>As the name implies, <code>useEffect</code> is the main way to trigger various side-effects. You can even return a cleanup function from your effect if one is needed.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token function">useEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
	<span class="token comment">// Trigger your effect</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token comment">// Optional: Any cleanup code</span>
	<span class="token punctuation">}</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>We'll start with a <code>Title</code> component which should reflect the title to the document, so that we can see it in the address bar of our tab in our browser.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">function</span> <span class="token function">PageTitle</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token function">useEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		document<span class="token punctuation">.</span>title <span class="token operator">=</span> props<span class="token punctuation">.</span>title<span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>props<span class="token punctuation">.</span>title<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>h1</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>props<span class="token punctuation">.</span>title<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>h1</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<p>The first argument to <code>useEffect</code> is an argument-less callback that triggers the effect. In our case we only want to trigger it, when the title really has changed. There'd be no point in updating it when it stayed the same. That's why we're using the second argument to specify our <a href="#the-dependency-argument">dependency-array</a>.</p>
<p>But sometimes we have a more complex use case. Think of a component which needs to subscribe to some data when it mounts and needs to unsubscribe when it unmounts. This can be accomplished with <code>useEffect</code> too. To run any cleanup code we just need to return a function in our callback.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token comment">// Component that will always display the current window width</span>
<span class="token keyword">function</span> <span class="token function">WindowWidth</span><span class="token punctuation">(</span><span class="token parameter">props</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>width<span class="token punctuation">,</span> setWidth<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">function</span> <span class="token function">onResize</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token function">setWidth</span><span class="token punctuation">(</span>window<span class="token punctuation">.</span>innerWidth<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>

	<span class="token function">useEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		window<span class="token punctuation">.</span><span class="token function">addEventListener</span><span class="token punctuation">(</span><span class="token string">'resize'</span><span class="token punctuation">,</span> onResize<span class="token punctuation">)</span><span class="token punctuation">;</span>
		<span class="token keyword">return</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> window<span class="token punctuation">.</span><span class="token function">removeEventListener</span><span class="token punctuation">(</span><span class="token string">'resize'</span><span class="token punctuation">,</span> onResize<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">Window width: </span><span class="token punctuation">{</span>width<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>
</code></pre>
					<a class="repl-link" href="/repl?code=aW1wb3J0IHsgdXNlU3RhdGUsIHVzZUVmZmVjdCB9IGZyb20gJ3ByZWFjdC9ob29rcyc7CmltcG9ydCB7IHJlbmRlciB9IGZyb20gJ3ByZWFjdCc7CgovLyBDb21wb25lbnQgdGhhdCB3aWxsIGFsd2F5cyBkaXNwbGF5IHRoZSBjdXJyZW50IHdpbmRvdyB3aWR0aApmdW5jdGlvbiBXaW5kb3dXaWR0aChwcm9wcykgewoJY29uc3QgW3dpZHRoLCBzZXRXaWR0aF0gPSB1c2VTdGF0ZSgwKTsKCglmdW5jdGlvbiBvblJlc2l6ZSgpIHsKCQlzZXRXaWR0aCh3aW5kb3cuaW5uZXJXaWR0aCk7Cgl9CgoJdXNlRWZmZWN0KCgpID0%2BIHsKCQl3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcigncmVzaXplJywgb25SZXNpemUpOwoJCXJldHVybiAoKSA9PiB3aW5kb3cucmVtb3ZlRXZlbnRMaXN0ZW5lcigncmVzaXplJywgb25SZXNpemUpOwoJfSwgW10pOwoKCXJldHVybiA8cD5XaW5kb3cgd2lkdGg6IHt3aWR0aH08L3A%2BOwp9CgpyZW5kZXIoPFdpbmRvd1dpZHRoIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D">Run in REPL</a>
				</div>
			<blockquote>
<p>The cleanup function is optional. If you don't need to run any cleanup code, you don't need to return anything in the callback that's passed to <code>useEffect</code>.</p>
</blockquote>

				<h3 id="uselayouteffect">
					<a class="fragment-link" href="#uselayouteffect">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useLayoutEffect (#uselayouteffect)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useLayoutEffect</span>
				</h3><p>Similar to <a href="#useeffect">`useEffect`</a>, <code>useLayoutEffect</code> is used to trigger side-effects but it will do so as soon as the component is diffed and before the browser has a chance to repaint. Commonly used for measuring DOM elements, this allows you to avoid flickering or pop-in that may occur if you use <code>useEffect</code> for such tasks.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useLayoutEffect<span class="token punctuation">,</span> useRef <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/hooks'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> hintRef <span class="token operator">=</span> <span class="token function">useRef</span><span class="token punctuation">(</span><span class="token keyword">null</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token function">useLayoutEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token keyword">const</span> hintWidth <span class="token operator">=</span> hintRef<span class="token punctuation">.</span>current<span class="token punctuation">.</span><span class="token function">getBoundingClientRect</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">.</span>width<span class="token punctuation">;</span>

		<span class="token comment">// We might use this width to position and center the hint on the screen, like so:</span>
		hintRef<span class="token punctuation">.</span>current<span class="token punctuation">.</span>style<span class="token punctuation">.</span>left <span class="token operator">=</span> <span class="token template-string"><span class="token template-punctuation string">`</span><span class="token interpolation"><span class="token interpolation-punctuation punctuation">${</span><span class="token punctuation">(</span>window<span class="token punctuation">.</span>innerWidth <span class="token operator">-</span> hintWidth<span class="token punctuation">)</span> <span class="token operator">/</span> <span class="token number">2</span><span class="token interpolation-punctuation punctuation">}</span></span><span class="token string">px</span><span class="token template-punctuation string">`</span></span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">return</span> <span class="token punctuation">(</span>
		<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span> <span class="token special-attr"><span class="token attr-name">style</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">&quot;</span><span class="token value css language-css"><span class="token property">display</span><span class="token punctuation">:</span> inline<span class="token punctuation">;</span> <span class="token property">position</span><span class="token punctuation">:</span> absolute</span><span class="token punctuation">&quot;</span></span></span> <span class="token attr-name">ref</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>hintRef<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">This is a hint</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
		</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="useerrorboundary">
					<a class="fragment-link" href="#useerrorboundary">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useErrorBoundary (#useerrorboundary)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useErrorBoundary</span>
				</h3><p>Whenever a child component throws an error you can use this hook to catch it and display a custom error UI to the user.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token comment">// error = The error that was caught or `undefined` if nothing errored.</span>
<span class="token comment">// resetError = Call this function to mark an error as resolved. It's</span>
<span class="token comment">//   up to your app to decide what that means and if it is possible</span>
<span class="token comment">//   to recover from errors.</span>
<span class="token keyword">const</span> <span class="token punctuation">[</span>error<span class="token punctuation">,</span> resetError<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useErrorBoundary</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>For monitoring purposes it's often incredibly useful to notify a service of any errors. For that we can leverage an optional callback and pass that as the first argument to <code>useErrorBoundary</code>.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> <span class="token punctuation">[</span>error<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useErrorBoundary</span><span class="token punctuation">(</span><span class="token parameter">error</span> <span class="token operator">=></span> <span class="token function">callMyApi</span><span class="token punctuation">(</span>error<span class="token punctuation">.</span>message<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<p>A full usage example may look like this:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> <span class="token function-variable function">App</span> <span class="token operator">=</span> <span class="token parameter">props</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>error<span class="token punctuation">,</span> resetError<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useErrorBoundary</span><span class="token punctuation">(</span><span class="token parameter">error</span> <span class="token operator">=></span>
		<span class="token function">callMyApi</span><span class="token punctuation">(</span>error<span class="token punctuation">.</span>message<span class="token punctuation">)</span>
	<span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token comment">// Display a nice error message</span>
	<span class="token keyword">if</span> <span class="token punctuation">(</span>error<span class="token punctuation">)</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token punctuation">(</span>
			<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>p</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>error<span class="token punctuation">.</span>message<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>p</span><span class="token punctuation">></span></span><span class="token plain-text">
				</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>button</span> <span class="token attr-name">onClick</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>resetError<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">Try again</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>button</span><span class="token punctuation">></span></span><span class="token plain-text">
			</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span>
		<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{</span>
		<span class="token keyword">return</span> <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">{</span>props<span class="token punctuation">.</span>children<span class="token punctuation">}</span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>div</span><span class="token punctuation">></span></span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span>
<span class="token punctuation">}</span><span class="token punctuation">;</span></code></pre>
					
				</div>
			<blockquote>
<p>If you've been using the class based component API in the past, then this hook is essentially an alternative to the <a href="/guide/v10/whats-new/#componentdidcatch">componentDidCatch</a> lifecycle method.
This hook was introduced with Preact 10.2.0.</p>
</blockquote>

				<h2 id="utility-hooks">
					<a class="fragment-link" href="#utility-hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Utility hooks (#utility-hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Utility hooks</span>
				</h2>
				<h3 id="useid">
					<a class="fragment-link" href="#useid">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useId (#useid)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useId</span>
				</h3><p>This hook will generate a unique identifier for each invocation and guarantees that these will be consistent when rendering both <a href="/guide/v10/server-side-rendering">on the server</a> and the client. A common use case for consistent IDs are forms, where <code>&lt;label></code>-elements use the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label#attr-for" target="_blank" rel="noopener noreferrer">`for`</a> attribute to associate them with a specific <code>&lt;input></code>-element. The <code>useId</code> hook isn't tied to just forms though and can be used whenever you need a unique ID.</p>
<blockquote>
<p>To make the hook consistent you will need to use Preact on both the server
as well as on the client.</p>
</blockquote>
<p>A full usage example may look like this:</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">const</span> <span class="token function-variable function">App</span> <span class="token operator">=</span> <span class="token parameter">props</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
  <span class="token keyword">const</span> mainId <span class="token operator">=</span> <span class="token function">useId</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
  <span class="token keyword">const</span> inputId <span class="token operator">=</span> <span class="token function">useId</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

  <span class="token function">useLayoutEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
    document<span class="token punctuation">.</span><span class="token function">getElementById</span><span class="token punctuation">(</span>inputId<span class="token punctuation">)</span><span class="token punctuation">.</span><span class="token function">focus</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span>

  <span class="token comment">// Display an input with a unique ID.</span>
  <span class="token keyword">return</span> <span class="token punctuation">(</span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>main</span> <span class="token attr-name">id</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>mainId<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
      </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>input</span> <span class="token attr-name">id</span><span class="token script language-javascript"><span class="token script-punctuation punctuation">=</span><span class="token punctuation">{</span>inputId<span class="token punctuation">}</span></span><span class="token punctuation">></span></span><span class="token plain-text">
    </span><span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>main</span><span class="token punctuation">></span></span><span class="token plain-text">
  )
};</span></code></pre>
					
				</div>
			<blockquote>
<p>This hook was introduced with Preact 10.11.0 and needs preact-render-to-string 5.2.4.</p>
</blockquote>

				<h3 id="usedebugvalue">
					<a class="fragment-link" href="#usedebugvalue">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useDebugValue (#usedebugvalue)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useDebugValue</span>
				</h3><p>Displays a custom label for use in the Preact DevTools browser extension. Useful for custom hooks to provide additional context about the state or value they represent.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useDebugValue<span class="token punctuation">,</span> useState <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/hooks'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">useCount</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> setCount<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token function">useDebugValue</span><span class="token punctuation">(</span>count <span class="token operator">></span> <span class="token number">0</span> <span class="token operator">?</span> <span class="token string">'Positive'</span> <span class="token operator">:</span> <span class="token string">'Negative'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> setCount<span class="token punctuation">]</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			<p>In your devtools, this will display as <code>useCount: &quot;Positive&quot;</code> or <code>useCount: &quot;Negative&quot;</code>, whereas previously it would've been just <code>useCount</code>.</p>
<p>Optionally, you can also pass a function as the second argument to <code>useDebugValue</code> for use as the &quot;formatter&quot;.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useDebugValue<span class="token punctuation">,</span> useState <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/hooks'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">useCount</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> setCount<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useState</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token function">useDebugValue</span><span class="token punctuation">(</span>count<span class="token punctuation">,</span> <span class="token parameter">c</span> <span class="token operator">=></span> <span class="token template-string"><span class="token template-punctuation string">`</span><span class="token string">Count: </span><span class="token interpolation"><span class="token interpolation-punctuation punctuation">${</span>c<span class="token interpolation-punctuation punctuation">}</span></span><span class="token template-punctuation string">`</span></span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">[</span>count<span class="token punctuation">,</span> setCount<span class="token punctuation">]</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h2 id="compat-specific-hooks">
					<a class="fragment-link" href="#compat-specific-hooks">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: Compat-specific hooks (#compat-specific-hooks)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>Compat-specific hooks</span>
				</h2><p>We offer some additional hooks only through the <code>preact/compat</code> package, as they are either stubbed-out implementations or are not part of the essential hooks API.</p>

				<h3 id="usesyncexternalstore">
					<a class="fragment-link" href="#usesyncexternalstore">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useSyncExternalStore (#usesyncexternalstore)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useSyncExternalStore</span>
				</h3><p>Allows you to subscribe to an external data source, such as a global state management library, browser APIs, or any other external (to Preact) data source.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useSyncExternalStore <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">subscribe</span><span class="token punctuation">(</span><span class="token parameter">cb</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token function">addEventListener</span><span class="token punctuation">(</span><span class="token string">'scroll'</span><span class="token punctuation">,</span> cb<span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token function">removeEventListener</span><span class="token punctuation">(</span><span class="token string">'scroll'</span><span class="token punctuation">,</span> cb<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> scrollY <span class="token operator">=</span> <span class="token function">useSyncExternalStore</span><span class="token punctuation">(</span>subscribe<span class="token punctuation">,</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> window<span class="token punctuation">.</span>scrollY<span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="usedeferredvalue">
					<a class="fragment-link" href="#usedeferredvalue">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useDeferredValue (#usedeferredvalue)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useDeferredValue</span>
				</h3><p>Stubbed-out implementation, immediately returns the value as Preact does not support concurrent rendering.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useDeferredValue <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token keyword">const</span> deferredValue <span class="token operator">=</span> <span class="token function">useDeferredValue</span><span class="token punctuation">(</span><span class="token string">'Hello, World!'</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="usetransition">
					<a class="fragment-link" href="#usetransition">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useTransition (#usetransition)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useTransition</span>
				</h3><p>Stubbed-out implementation as Preact does not support concurrent rendering.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useTransition <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token comment">// `isPending` will always be `false`</span>
	<span class="token keyword">const</span> <span class="token punctuation">[</span>isPending<span class="token punctuation">,</span> startTransition<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token function">useTransition</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">;</span>

	<span class="token keyword">const</span> <span class="token function-variable function">handleClick</span> <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token comment">// Immediately executes the callback, it's a no-op.</span>
		<span class="token function">startTransition</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
			<span class="token comment">// Transition code here</span>
		<span class="token punctuation">}</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
	<span class="token punctuation">}</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			
				<h3 id="useinsertioneffect">
					<a class="fragment-link" href="#useinsertioneffect">
						<svg width="16" height="16" viewBox="0 0 24 24" aria-label="Link to: useInsertionEffect (#useinsertioneffect)">
							<use href="/icons.svg#link"></use>
						</svg>
					</a>
					<span>useInsertionEffect</span>
				</h3><p>Stubbed-out implementation, matches <a href="#uselayouteffect">`useLayoutEffect`</a> in functionality.</p>

				<div class="highlight-container">
					<pre class="highlight"><code class="language-jsx"><span class="token keyword">import</span> <span class="token punctuation">{</span> useInsertionEffect <span class="token punctuation">}</span> <span class="token keyword">from</span> <span class="token string">'preact/compat'</span><span class="token punctuation">;</span>

<span class="token keyword">function</span> <span class="token function">App</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token punctuation">{</span>
	<span class="token function">useInsertionEffect</span><span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token operator">=></span> <span class="token punctuation">{</span>
		<span class="token comment">// Effect code here</span>
	<span class="token punctuation">}</span><span class="token punctuation">,</span> <span class="token punctuation">[</span>dependencies<span class="token punctuation">]</span><span class="token punctuation">)</span><span class="token punctuation">;</span>
<span class="token punctuation">}</span></code></pre>
					
				</div>
			</div></content-region><footer class="_footer_8z8ez_1"><div><p><label>Language: <select><option selected value="en">English</option><option value="de">German</option><option value="es">Spanish</option><option value="fr">French</option><option value="it">Italian</option><option value="ja">Japanese</option><option value="kr">Korean</option><option value="pt-br">Brazilian Portuguese</option><option value="ru">Русский</option><option value="tr">Turkish</option><option value="zh">简体中文</option></select><code>?lang=en</code></label></p><p style="line-height: 1">Built by a bunch of <a href="https://github.com/preactjs/preact/graphs/contributors" target="_blank" rel="noopener noreferrer">lovely people</a>  like <a href="https://github.com/kristoferbaxter" target="_blank" rel="noopener noreferrer">@kristoferbaxter</a>.</p></div></footer></div></div></div><!--/$s--></main><script type="isodata"></script><script async defer src="https://www.google-analytics.com/analytics.js"></script><script type="application/json" id="prerender-data">{"preactVersion":"11.0.0-beta.0","preactReleaseURL":"https://github.com/preactjs/preact/releases/tag/11.0.0-beta.0","preactOrgRepos":[{"html_url":"https://github.com/preactjs/preact","full_name":"preactjs/preact","stargazers_count":38228,"description":"⚛️ Fast 3kB React alternative with the same modern API. Components & Virtual DOM."},{"html_url":"https://github.com/preactjs/wmr","full_name":"preactjs/wmr","stargazers_count":4936,"description":"👩‍🚀 The tiny all-in-one development tool for modern web apps."},{"html_url":"https://github.com/preactjs/preact-cli","full_name":"preactjs/preact-cli","stargazers_count":4688,"description":"😺 Your next Preact PWA starts in 30 seconds."},{"html_url":"https://github.com/preactjs/signals","full_name":"preactjs/signals","stargazers_count":4331,"description":"Manage state with style in every framework"},{"html_url":"https://github.com/preactjs/awesome-preact","full_name":"preactjs/awesome-preact","stargazers_count":965,"description":"A curated list of amazingly awesome things regarding Preact ecosystem :star2:"}]}</script></div>
	</body>
</html>
