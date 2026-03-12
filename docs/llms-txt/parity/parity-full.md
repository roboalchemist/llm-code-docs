<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="generator" content="rustdoc"><meta name="description" content="Parity is a trait for indicating whether a number is odd or even."><title>parity - Rust</title><script>if(window.location.protocol!=="file:")document.head.insertAdjacentHTML("beforeend","SourceSerif4-Regular-6b053e98.ttf.woff2,FiraSans-Italic-81dc35de.woff2,FiraSans-Regular-0fe48ade.woff2,FiraSans-MediumItalic-ccf7e434.woff2,FiraSans-Medium-e1aa3f0a.woff2,SourceCodePro-Regular-8badfe75.ttf.woff2,SourceCodePro-Semibold-aa29a496.ttf.woff2".split(",").map(f=>`<link rel="preload" as="font" type="font/woff2"href="/-/rustdoc.static/${f}">`).join(""))</script><link rel="stylesheet" href="/-/rustdoc.static/normalize-9960930a.css"><link rel="stylesheet" href="/-/static/vendored.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/rustdoc.static/rustdoc-ca0dd0c4.css"><meta name="rustdoc-vars" data-root-path="../" data-static-root-path="/-/rustdoc.static/" data-current-crate="parity" data-themes="" data-resource-suffix="-20251101-1.93.0-nightly-bd3ac0330" data-rustdoc-version="1.93.0-nightly (bd3ac0330 2025-11-01)" data-channel="nightly" data-search-js="search-5c29b3b5.js" data-stringdex-js="stringdex-c3e638e9.js" data-settings-js="settings-c38705f0.js" ><script src="/-/rustdoc.static/storage-e2aeef58.js"></script><script defer src="../crates-20251101-1.93.0-nightly-bd3ac0330.js"></script><script defer src="/-/rustdoc.static/main-ce535bd0.js"></script><noscript><link rel="stylesheet" href="/-/rustdoc.static/noscript-263c88ec.css"></noscript><link rel="alternate icon" type="image/png" href="/-/rustdoc.static/favicon-32x32-eab170b8.png"><link rel="icon" type="image/svg+xml" href="/-/rustdoc.static/favicon-044be391.svg"><link rel="stylesheet" href="/-/static/rustdoc-2025-08-20.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/static/font-awesome.css?0-0-0-a68728e7-2026-03-08" media="all" />

<link rel="search" href="/-/static/opensearch.xml" type="application/opensearchdescription+xml" title="Docs.rs" />

<script type="text/javascript">(function() {
    function applyTheme(theme) {
        if (theme) {
            document.documentElement.dataset.docsRsTheme = theme;
        }
    }

    window.addEventListener("storage", ev => {
        if (ev.key === "rustdoc-theme") {
            applyTheme(ev.newValue);
        }
    });

    // see ./storage-change-detection.html for details
    window.addEventListener("message", ev => {
        if (ev.data && ev.data.storage && ev.data.storage.key === "rustdoc-theme") {
            applyTheme(ev.data.storage.value);
        }
    });

    applyTheme(window.localStorage.getItem("rustdoc-theme"));
})();</script></head><body class="rustdoc-page">
<div class="nav-container">
    <div class="container">
        <div class="pure-menu pure-menu-horizontal" role="navigation" aria-label="Main navigation">
            <form action="/releases/search"
                  method="GET"
                  id="nav-search-form"
                  class="landing-search-form-nav  ">

                
                <a href="/" class="pure-menu-heading pure-menu-link docsrs-logo" aria-label="Docs.rs">
                    <span title="Docs.rs"><span class="fa fa-solid fa-cubes " aria-hidden="true"></span></span>
                    <span class="title">Docs.rs</span>
                </a><ul class="pure-menu-list">
    <script id="crate-metadata" type="application/json">
        
        {
            "name": "parity",
            "version": "0.1.0"
        }
    </script><li class="pure-menu-item pure-menu-has-children">
            <a href="#" class="pure-menu-link crate-name" title="Provides is_even and is_odd methods for primitive numeric types">
                <span class="fa fa-solid fa-cube " aria-hidden="true"></span>
                <span class="title">parity-0.1.0</span>
            </a><div class="pure-menu-children package-details-menu">
                
                <ul class="pure-menu-list menu-item-divided">
                    <li class="pure-menu-heading" id="crate-title">
                        parity 0.1.0
                        <span id="clipboard" class="svg-clipboard" title="Copy crate name and version information"></span>
                    </li><li class="pure-menu-item">
                        <a href="/parity/0.1.0/parity/" class="pure-menu-link description" id="permalink" title="Get a link to this specific version"><span class="fa fa-solid fa-link " aria-hidden="true"></span> Permalink
                        </a>
                    </li><li class="pure-menu-item">
                        <a href="/crate/parity/latest" class="pure-menu-link description" title="See parity in docs.rs">
                            <span class="fa fa-solid fa-cube " aria-hidden="true"></span> Docs.rs crate page
                        </a>
                    </li><li class="pure-menu-item">
                            <span class="pure-menu-link description"><span class="fa fa-solid fa-scale-unbalanced-flip " aria-hidden="true"></span>
                            <a href="https://spdx.org/licenses/CC0-1.0" class="pure-menu-sublink">CC0-1.0</a></span>
                        </li></ul>

                <div class="pure-g menu-item-divided">
                    <div class="pure-u-1-2 right-border">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Links</li>

                            <li class="pure-menu-item">
                                    <a href="https://github.com/richardscollin/parity" class="pure-menu-link">
                                        <span class="fa fa-solid fa-code-branch " aria-hidden="true"></span> Repository
                                    </a>
                                </li><li class="pure-menu-item">
                                <a href="https://crates.io/crates/parity" class="pure-menu-link" title="See parity in crates.io">
                                    <span class="fa fa-solid fa-cube " aria-hidden="true"></span> crates.io
                                </a>
                            </li>

                            
                            <li class="pure-menu-item">
                                <a href="/crate/parity/latest/source/" title="Browse source of parity-0.1.0" class="pure-menu-link">
                                    <span class="fa fa-solid fa-folder-open " aria-hidden="true"></span> Source
                                </a>
                            </li>
                        </ul>
                    </div><div class="pure-u-1-2">
                        <ul class="pure-menu-list" id="topbar-owners">
                            <li class="pure-menu-heading">Owners</li><li class="pure-menu-item">
                                    <a href="https://crates.io/users/richardscollin" class="pure-menu-link">
                                        <span class="fa fa-solid fa-user " aria-hidden="true"></span> richardscollin
                                    </a>
                                </li></ul>
                    </div>
                </div>

                <div class="pure-g menu-item-divided">
                    <div class="pure-u-1-2 right-border">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Dependencies</li>

                            
                            <li class="pure-menu-item">
                                <div class="pure-menu pure-menu-scrollable sub-menu" tabindex="-1">
                                    <ul class="pure-menu-list">
                                        
                                    </ul>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <div class="pure-u-1-2">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Versions</li>

                            <li class="pure-menu-item">
                                <div class="pure-menu pure-menu-scrollable sub-menu" id="releases-list" tabindex="-1" data-url="/crate/parity/latest/menus/releases/parity/">
                                    <span class="rotate"><span class="fa fa-solid fa-spinner " aria-hidden="true"></span></span>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
                    
                    
                    <div class="pure-g">
                        <div class="pure-u-1">
                            <ul class="pure-menu-list">
                                <li>
                                    <a href="/crate/parity/latest" class="pure-menu-link">
                                        <b>100%</b>
                                        of the crate is documented
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div></div>
        </li><li class="pure-menu-item pure-menu-has-children">
                <a href="#" class="pure-menu-link" aria-label="Platform">
                    <span class="fa fa-solid fa-gears " aria-hidden="true"></span>
                    <span class="title">Platform</span>
                </a>

                
                <ul class="pure-menu-children" id="platforms" data-url="/crate/parity/latest/menus/platforms/parity/"><li class="pure-menu-item">
            <a href="/crate/parity/latest/target-redirect/aarch64-apple-darwin/parity/" class="pure-menu-link" data-fragment="retain" rel="nofollow">aarch64-apple-darwin</a>
        </li><li class="pure-menu-item">
            <a href="/crate/parity/latest/target-redirect/aarch64-unknown-linux-gnu/parity/" class="pure-menu-link" data-fragment="retain" rel="nofollow">aarch64-unknown-linux-gnu</a>
        </li><li class="pure-menu-item">
            <a href="/crate/parity/latest/target-redirect/i686-pc-windows-msvc/parity/" class="pure-menu-link" data-fragment="retain" rel="nofollow">i686-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/parity/latest/target-redirect/x86_64-pc-windows-msvc/parity/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/parity/latest/target-redirect/parity/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-unknown-linux-gnu</a>
        </li></ul>
            </li><li class="pure-menu-item">
                <a href="/crate/parity/latest/features" title="Browse available feature flags of parity-0.1.0" class="pure-menu-link">
                    <span class="fa fa-solid fa-flag " aria-hidden="true"></span>
                    <span class="title">Feature flags</span>
                </a>
            </li>
        
    
</ul><div class="spacer"></div>
                
                

<ul class="pure-menu-list">
                    <li class="pure-menu-item pure-menu-has-children">
                        <a href="#" class="pure-menu-link" aria-label="docs.rs">docs.rs</a>
                        <ul class="pure-menu-children aligned-icons"><li class="pure-menu-item"><a class="pure-menu-link" href="/about"><span class="fa fa-solid fa-circle-info " aria-hidden="true"></span> About docs.rs</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/badges"><span class="fa fa-brands fa-fonticons " aria-hidden="true"></span> Badges</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/builds"><span class="fa fa-solid fa-gears " aria-hidden="true"></span> Builds</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/metadata"><span class="fa fa-solid fa-table " aria-hidden="true"></span> Metadata</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/redirections"><span class="fa fa-solid fa-road " aria-hidden="true"></span> Shorthand URLs</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/download"><span class="fa fa-solid fa-download " aria-hidden="true"></span> Download</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/about/rustdoc-json"><span class="fa fa-solid fa-file-code " aria-hidden="true"></span> Rustdoc JSON</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="/releases/queue"><span class="fa fa-solid fa-gears " aria-hidden="true"></span> Build queue</a></li><li class="pure-menu-item"><a class="pure-menu-link" href="https://foundation.rust-lang.org/policies/privacy-policy/#docs.rs" target="_blank"><span class="fa fa-solid fa-shield-halved " aria-hidden="true"></span> Privacy policy</a></li>
                        </ul>
                    </li>
                </ul>
                <ul class="pure-menu-list"><li class="pure-menu-item pure-menu-has-children">
                        <a href="#" class="pure-menu-link" aria-label="Rust">Rust</a>
                        <ul class="pure-menu-children">
                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://www.rust-lang.org/" target="_blank">Rust website</a></li>
                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://doc.rust-lang.org/book/" target="_blank">The Book</a></li>

                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://doc.rust-lang.org/std/" target="_blank">Standard Library API Reference</a></li>

                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://doc.rust-lang.org/rust-by-example/" target="_blank">Rust by Example</a></li>

                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://doc.rust-lang.org/cargo/guide/" target="_blank">The Cargo Guide</a></li>

                            <li class="pure-menu-item"><a class="pure-menu-link" href="https://doc.rust-lang.org/nightly/clippy" target="_blank">Clippy Documentation</a></li>
                        </ul>
                    </li>
                </ul>
                
                <div id="search-input-nav">
                    <label for="nav-search">
                        <span class="fa fa-solid fa-magnifying-glass " aria-hidden="true"></span>
                    </label>

                    
                    
                    <input id="nav-search" name="query" type="text" aria-label="Find crate by search query" tabindex="-1"
                        placeholder="Find crate"
                        >
                </div>
            </form>
        </div>
    </div>
</div><div class="rustdoc mod crate container-rustdoc" id="rustdoc_body_wrapper" tabindex="-1"><script async src="/-/static/menu.js?0-0-0-a68728e7-2026-03-08"></script>
<script async src="/-/static/index.js?0-0-0-a68728e7-2026-03-08"></script>

<iframe src="/-/storage-change-detection.html" width="0" height="0" style="display: none"></iframe><!--[if lte IE 11]><div class="warning">This old browser is unsupported and will most likely display funky things.</div><![endif]--><rustdoc-topbar><h2><a href="#">Crate parity</a></h2></rustdoc-topbar><nav class="sidebar"><div class="sidebar-crate"><h2><a href="../parity/index.html">parity</a><span class="version">0.1.0</span></h2></div><div class="sidebar-elems"><ul class="block"><li><a id="all-types" href="all.html">All Items</a></li></ul><section id="rustdoc-toc"><h3><a href="#traits">Crate Items</a></h3><ul class="block"><li><a href="#traits" title="Traits">Traits</a></li></ul></section><div id="rustdoc-modnav"></div></div></nav><div class="sidebar-resizer" title="Drag to resize sidebar"></div><main><div class="width-limiter"><section id="main-content" class="content"><div class="main-heading"><h1>Crate <span>parity</span>&nbsp;<button id="copy-path" title="Copy item path to clipboard">Copy item path</button></h1><rustdoc-toolbar></rustdoc-toolbar><span class="sub-heading"><a class="src" href="../src/parity/lib.rs.html#1-137">Source</a> </span></div><details class="toggle top-doc" open><summary class="hideme"><span>Expand description</span></summary><div class="docblock"><p><a href="trait.Parity.html" title="trait parity::Parity">Parity</a> is a trait for indicating whether a number is odd or even.</p>
</div></details><h2 id="traits" class="section-header">Traits<a href="#traits" class="anchor">§</a></h2><dl class="item-table"><dt><a class="trait" href="trait.Parity.html" title="trait parity::Parity">Parity</a></dt><dd>Provides an interface to check the evenness or oddness of a value.</dd></dl></section></div></main></div></body></html>