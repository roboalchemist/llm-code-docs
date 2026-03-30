<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="generator" content="rustdoc"><meta name="description" content="Rust bindings to RenderDoc, a popular graphics debugger."><title>renderdoc - Rust</title><script>if(window.location.protocol!=="file:")document.head.insertAdjacentHTML("beforeend","SourceSerif4-Regular-6b053e98.ttf.woff2,FiraSans-Italic-81dc35de.woff2,FiraSans-Regular-0fe48ade.woff2,FiraSans-MediumItalic-ccf7e434.woff2,FiraSans-Medium-e1aa3f0a.woff2,SourceCodePro-Regular-8badfe75.ttf.woff2,SourceCodePro-Semibold-aa29a496.ttf.woff2".split(",").map(f=>`<link rel="preload" as="font" type="font/woff2"href="/-/rustdoc.static/${f}">`).join(""))</script><link rel="stylesheet" href="/-/rustdoc.static/normalize-9960930a.css"><link rel="stylesheet" href="/-/static/vendored.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/rustdoc.static/rustdoc-ca0dd0c4.css"><meta name="rustdoc-vars" data-root-path="../" data-static-root-path="/-/rustdoc.static/" data-current-crate="renderdoc" data-themes="" data-resource-suffix="-20251108-1.93.0-nightly-fb23dd3c6" data-rustdoc-version="1.93.0-nightly (fb23dd3c6 2025-11-08)" data-channel="nightly" data-search-js="search-8e3fad08.js" data-stringdex-js="stringdex-c3e638e9.js" data-settings-js="settings-c38705f0.js" ><script src="/-/rustdoc.static/storage-e2aeef58.js"></script><script defer src="../crates-20251108-1.93.0-nightly-fb23dd3c6.js"></script><script defer src="/-/rustdoc.static/main-ce535bd0.js"></script><noscript><link rel="stylesheet" href="/-/rustdoc.static/noscript-263c88ec.css"></noscript><link rel="alternate icon" type="image/png" href="/-/rustdoc.static/favicon-32x32-eab170b8.png"><link rel="icon" type="image/svg+xml" href="/-/rustdoc.static/favicon-044be391.svg"><link rel="stylesheet" href="/-/static/rustdoc-2025-08-20.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/static/font-awesome.css?0-0-0-a68728e7-2026-03-08" media="all" />

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
            "name": "renderdoc",
            "version": "0.12.1"
        }
    </script><li class="pure-menu-item pure-menu-has-children">
            <a href="#" class="pure-menu-link crate-name" title="RenderDoc application bindings for Rust">
                <span class="fa fa-solid fa-cube " aria-hidden="true"></span>
                <span class="title">renderdoc-0.12.1</span>
            </a><div class="pure-menu-children package-details-menu">
                
                <ul class="pure-menu-list menu-item-divided">
                    <li class="pure-menu-heading" id="crate-title">
                        renderdoc 0.12.1
                        <span id="clipboard" class="svg-clipboard" title="Copy crate name and version information"></span>
                    </li><li class="pure-menu-item">
                        <a href="/renderdoc/0.12.1/renderdoc/" class="pure-menu-link description" id="permalink" title="Get a link to this specific version"><span class="fa fa-solid fa-link " aria-hidden="true"></span> Permalink
                        </a>
                    </li><li class="pure-menu-item">
                        <a href="/crate/renderdoc/latest" class="pure-menu-link description" title="See renderdoc in docs.rs">
                            <span class="fa fa-solid fa-cube " aria-hidden="true"></span> Docs.rs crate page
                        </a>
                    </li><li class="pure-menu-item">
                            <span class="pure-menu-link description"><span class="fa fa-solid fa-scale-unbalanced-flip " aria-hidden="true"></span>
                            <a href="https://spdx.org/licenses/MIT" class="pure-menu-sublink">MIT</a> OR <a href="https://spdx.org/licenses/Apache-2.0" class="pure-menu-sublink">Apache-2.0</a></span>
                        </li></ul>

                <div class="pure-g menu-item-divided">
                    <div class="pure-u-1-2 right-border">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Links</li>

                            <li class="pure-menu-item">
                                    <a href="https://github.com/ebkalderon/renderdoc-rs" class="pure-menu-link">
                                        <span class="fa fa-solid fa-house " aria-hidden="true"></span> Homepage
                                    </a>
                                </li><li class="pure-menu-item">
                                    <a href="https://github.com/ebkalderon/renderdoc-rs" class="pure-menu-link">
                                        <span class="fa fa-solid fa-code-branch " aria-hidden="true"></span> Repository
                                    </a>
                                </li><li class="pure-menu-item">
                                <a href="https://crates.io/crates/renderdoc" class="pure-menu-link" title="See renderdoc in crates.io">
                                    <span class="fa fa-solid fa-cube " aria-hidden="true"></span> crates.io
                                </a>
                            </li>

                            
                            <li class="pure-menu-item">
                                <a href="/crate/renderdoc/latest/source/" title="Browse source of renderdoc-0.12.1" class="pure-menu-link">
                                    <span class="fa fa-solid fa-folder-open " aria-hidden="true"></span> Source
                                </a>
                            </li>
                        </ul>
                    </div><div class="pure-u-1-2">
                        <ul class="pure-menu-list" id="topbar-owners">
                            <li class="pure-menu-heading">Owners</li><li class="pure-menu-item">
                                    <a href="https://crates.io/users/ebkalderon" class="pure-menu-link">
                                        <span class="fa fa-solid fa-user " aria-hidden="true"></span> ebkalderon
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
                                        <li class="pure-menu-item"><a href="/bitflags/^2.0/" class="pure-menu-link">
                bitflags ^2.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/float-cmp/^0.9/" class="pure-menu-link">
                float-cmp ^0.9
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/glutin/^0.30/" class="pure-menu-link">
                glutin ^0.30
                
                    <i class="dependencies normal">normal</i>
                    
                        <i>optional</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/libloading/^0.8/" class="pure-menu-link">
                libloading ^0.8
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/once_cell/^1.0/" class="pure-menu-link">
                once_cell ^1.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/renderdoc-sys/^1.1.0/" class="pure-menu-link">
                renderdoc-sys ^1.1.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/winit/^0.28/" class="pure-menu-link">
                winit ^0.28
                
                    <i class="dependencies normal">normal</i>
                    
                        <i>optional</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/pollster/^0.3/" class="pure-menu-link">
                pollster ^0.3
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/wgpu/^0.15/" class="pure-menu-link">
                wgpu ^0.15
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/wgpu-subscriber/^0.1.0/" class="pure-menu-link">
                wgpu-subscriber ^0.1.0
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/winit/^0.28/" class="pure-menu-link">
                winit ^0.28
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/winapi/^0.3/" class="pure-menu-link">
                winapi ^0.3
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/wio/^0.2/" class="pure-menu-link">
                wio ^0.2
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li>
                                    </ul>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <div class="pure-u-1-2">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Versions</li>

                            <li class="pure-menu-item">
                                <div class="pure-menu pure-menu-scrollable sub-menu" id="releases-list" tabindex="-1" data-url="/crate/renderdoc/latest/menus/releases/renderdoc/">
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
                                    <a href="/crate/renderdoc/latest" class="pure-menu-link">
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

                
                <ul class="pure-menu-children" id="platforms" data-url="/crate/renderdoc/latest/menus/platforms/renderdoc/"><li class="pure-menu-item">
            <a href="/crate/renderdoc/latest/target-redirect/aarch64-unknown-linux-gnu/renderdoc/" class="pure-menu-link" data-fragment="retain" rel="nofollow">aarch64-unknown-linux-gnu</a>
        </li><li class="pure-menu-item">
            <a href="/crate/renderdoc/latest/target-redirect/i686-pc-windows-msvc/renderdoc/" class="pure-menu-link" data-fragment="retain" rel="nofollow">i686-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/renderdoc/latest/target-redirect/x86_64-pc-windows-msvc/renderdoc/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/renderdoc/latest/target-redirect/renderdoc/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-unknown-linux-gnu</a>
        </li></ul>
            </li><li class="pure-menu-item">
                <a href="/crate/renderdoc/latest/features" title="Browse available feature flags of renderdoc-0.12.1" class="pure-menu-link">
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

<iframe src="/-/storage-change-detection.html" width="0" height="0" style="display: none"></iframe><!--[if lte IE 11]><div class="warning">This old browser is unsupported and will most likely display funky things.</div><![endif]--><rustdoc-topbar><h2><a href="#">Crate renderdoc</a></h2></rustdoc-topbar><nav class="sidebar"><div class="sidebar-crate"><h2><a href="../renderdoc/index.html">renderdoc</a><span class="version">0.12.1</span></h2></div><div class="sidebar-elems"><ul class="block"><li><a id="all-types" href="all.html">All Items</a></li></ul><section id="rustdoc-toc"><h3><a href="#structs">Crate Items</a></h3><ul class="block"><li><a href="#structs" title="Structs">Structs</a></li><li><a href="#enums" title="Enums">Enums</a></li><li><a href="#constants" title="Constants">Constants</a></li><li><a href="#traits" title="Traits">Traits</a></li><li><a href="#types" title="Type Aliases">Type Aliases</a></li></ul></section><div id="rustdoc-modnav"></div></div></nav><div class="sidebar-resizer" title="Drag to resize sidebar"></div><main><div class="width-limiter"><section id="main-content" class="content"><div class="main-heading"><h1>Crate <span>renderdoc</span>&nbsp;<button id="copy-path" title="Copy item path to clipboard">Copy item path</button></h1><rustdoc-toolbar></rustdoc-toolbar><span class="sub-heading"><a class="src" href="../src/renderdoc/lib.rs.html#1-129">Source</a> </span></div><details class="toggle top-doc" open><summary class="hideme"><span>Expand description</span></summary><div class="docblock"><p>Rust bindings to <a href="https://renderdoc.org/">RenderDoc</a>, a popular graphics debugger.</p>
<p>RenderDoc is a free and open source debugger for real-time graphics providing quick and easy
frame captures and detailed introspection of any application using <a href="https://www.vulkan.org/">Vulkan</a>, <a href="https://learn.microsoft.com/en-us/windows/win32/direct3d11/atoc-dx-graphics-direct3d-11">Direct3D 11</a>,
<a href="https://learn.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics">Direct3D 12</a>, <a href="https://www.khronos.org/opengl/">OpenGL</a>, and <a href="https://www.khronos.org/opengles/">OpenGL ES</a>.</p>
<p>These bindings require that RenderDoc be installed on the target machine, with either
<code>renderdoc.dll</code> or <code>librenderdoc.so</code> visible from your <code>$PATH</code>.</p>
<p>For more details on how to use this API to integrate your game or renderer with the RenderDoc
profiler, consult the upstream <a href="https://renderdoc.org/docs/in_application_api.html">in-application API</a> documentation.</p>
</div></details><h2 id="structs" class="section-header">Structs<a href="#structs" class="anchor">§</a></h2><dl class="item-table"><dt><a class="struct" href="struct.DevicePointer.html" title="struct renderdoc::DevicePointer">Device<wbr>Pointer</a></dt><dd>Raw mutable pointer to the API’s root handle.</dd><dt><a class="struct" href="struct.Error.html" title="struct renderdoc::Error">Error</a></dt><dd>Errors that can occur with the RenderDoc in-application API.</dd><dt><a class="struct" href="struct.OverlayBits.html" title="struct renderdoc::OverlayBits">Overlay<wbr>Bits</a></dt><dd>Bit flags for customizing the RenderDoc overlay.</dd><dt><a class="struct" href="struct.RenderDoc.html" title="struct renderdoc::RenderDoc">Render<wbr>Doc</a></dt><dd>An instance of the RenderDoc API with baseline version <code>V</code>.</dd></dl><h2 id="enums" class="section-header">Enums<a href="#enums" class="anchor">§</a></h2><dl class="item-table"><dt><a class="enum" href="enum.CaptureOption.html" title="enum renderdoc::CaptureOption">Capture<wbr>Option</a></dt><dd>RenderDoc capture options.</dd><dt><a class="enum" href="enum.InputButton.html" title="enum renderdoc::InputButton">Input<wbr>Button</a></dt><dd>User input key codes.</dd><dt><a class="enum" href="enum.V100.html" title="enum renderdoc::V100">V100</a></dt><dd>Requests a minimum version number of 1.0.0.</dd><dt><a class="enum" href="enum.V110.html" title="enum renderdoc::V110">V110</a></dt><dd>Requests a minimum version number of 1.1.0.</dd><dt><a class="enum" href="enum.V111.html" title="enum renderdoc::V111">V111</a></dt><dd>Requests a minimum version number of 1.1.1.</dd><dt><a class="enum" href="enum.V112.html" title="enum renderdoc::V112">V112</a></dt><dd>Requests a minimum version number of 1.1.2.</dd><dt><a class="enum" href="enum.V120.html" title="enum renderdoc::V120">V120</a></dt><dd>Requests a minimum version number of 1.2.0.</dd><dt><a class="enum" href="enum.V130.html" title="enum renderdoc::V130">V130</a></dt><dd>Requests a minimum version number of 1.3.0.</dd><dt><a class="enum" href="enum.V140.html" title="enum renderdoc::V140">V140</a></dt><dd>Requests a minimum version number of 1.4.0.</dd><dt><a class="enum" href="enum.V141.html" title="enum renderdoc::V141">V141</a></dt><dd>Requests a minimum version number of 1.4.1.</dd></dl><h2 id="constants" class="section-header">Constants<a href="#constants" class="anchor">§</a></h2><dl class="item-table"><dt><a class="constant" href="constant.SHADER_MAGIC_DEBUG_VALUE_BYTE_ARRAY.html" title="constant renderdoc::SHADER_MAGIC_DEBUG_VALUE_BYTE_ARRAY">SHADER_<wbr>MAGIC_<wbr>DEBUG_<wbr>VALUE_<wbr>BYTE_<wbr>ARRAY</a></dt><dd>Magic value used for when applications pass a path where shader debug information can be found
to match up with a stripped shader.</dd><dt><a class="constant" href="constant.SHADER_MAGIC_DEBUG_VALUE_TRUNCATED.html" title="constant renderdoc::SHADER_MAGIC_DEBUG_VALUE_TRUNCATED">SHADER_<wbr>MAGIC_<wbr>DEBUG_<wbr>VALUE_<wbr>TRUNCATED</a></dt><dd>Magic value used for when applications pass a path where shader debug information can be found
to match up with a stripped shader.</dd></dl><h2 id="traits" class="section-header">Traits<a href="#traits" class="anchor">§</a></h2><dl class="item-table"><dt><a class="trait" href="trait.HasPrevious.html" title="trait renderdoc::HasPrevious">HasPrevious</a></dt><dd>Trait for statically enforcing backwards compatibility.</dd><dt><a class="trait" href="trait.Version.html" title="trait renderdoc::Version">Version</a></dt><dd>Entry point into the RenderDoc API.</dd></dl><h2 id="types" class="section-header">Type Aliases<a href="#types" class="anchor">§</a></h2><dl class="item-table"><dt><a class="type" href="type.Entry.html" title="type renderdoc::Entry">Entry</a></dt><dd>Entry point for the RenderDoc API.</dd><dt><a class="type" href="type.WindowHandle.html" title="type renderdoc::WindowHandle">Window<wbr>Handle</a></dt><dd>Raw mutable pointer to the OS-provided window handle.</dd></dl></section></div></main></div></body></html>
