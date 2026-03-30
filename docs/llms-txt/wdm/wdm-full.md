<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="generator" content="docs.rs 0.0.0 (a68728e7 2026-03-08 )"><link rel="canonical" href="https://docs.rs/crate/wdm/latest" /><link rel="stylesheet" href="/-/static/vendored.css?0-0-0-a68728e7-2026-03-08" media="all" />
        <link rel="stylesheet" href="/-/static/style.css?0-0-0-a68728e7-2026-03-08" media="all" />
        <link rel="stylesheet" href="/-/static/font-awesome.css?0-0-0-a68728e7-2026-03-08" media="all" />

        <link rel="search" href="/-/static/opensearch.xml" type="application/opensearchdescription+xml" title="Docs.rs" />

        <title>wdm 0.1.0 - Docs.rs</title><script nonce="Z1b0OFZ+sVwYIVEsosUuepE9r8IwWIqMcLD4yViqqNdD4uqr">(function() {
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
})();</script><script defer type="text/javascript" nonce="Z1b0OFZ+sVwYIVEsosUuepE9r8IwWIqMcLD4yViqqNdD4uqr" src="/-/static/menu.js?0-0-0-a68728e7-2026-03-08"></script>
        <script defer type="text/javascript" nonce="Z1b0OFZ+sVwYIVEsosUuepE9r8IwWIqMcLD4yViqqNdD4uqr" src="/-/static/index.js?0-0-0-a68728e7-2026-03-08"></script>
    </head>

    <body class="">
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
            "name": "wdm",
            "version": "0.1.0"
        }
    </script><li class="pure-menu-item">
            <a href="/crate/wdm/latest" class="pure-menu-link crate-name" title="Decentralized WordPress Plugin Dependency Manager">
                <span class="fa fa-solid fa-cube " aria-hidden="true"></span>
                <span class="title">wdm-0.1.0</span>
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
</div>
    
    <div class="docsrs-package-container">
        <div class="container">
            <div class="description-container">
                

                
                <h1 id="crate-title">
                    wdm 0.1.0
                    <span id="clipboard" class="svg-clipboard" title="Copy crate name and version information"></span>
                </h1>

                
                <div class="description">Decentralized WordPress Plugin Dependency Manager</div>


                <div class="pure-menu pure-menu-horizontal">
                    <ul class="pure-menu-list">
                        
                        <li class="pure-menu-item"><a href="/crate/wdm/latest"
                                class="pure-menu-link pure-menu-active">
                                <span class="fa fa-solid fa-cube " aria-hidden="true"></span>
                                <span class="title"> Crate</span>
                            </a>
                        </li>

                        
                        <li class="pure-menu-item">
                            <a href="/crate/wdm/latest/source/"
                                class="pure-menu-link">
                                <span class="fa fa-regular fa-folder-open " aria-hidden="true"></span>
                                <span class="title"> Source</span>
                            </a>
                        </li>

                        
                        <li class="pure-menu-item">
                            <a href="/crate/wdm/latest/builds"
                                class="pure-menu-link">
                                <span class="fa fa-solid fa-gears " aria-hidden="true"></span>
                                <span class="title"> Builds</span>
                            </a>
                        </li>

                        
                        <li class="pure-menu-item">
                            <a href="/crate/wdm/latest/features"
                               class="pure-menu-link">
                                <span class="fa fa-solid fa-flag " aria-hidden="true"></span>
                                <span class="title">Feature flags</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div></div>
    </div>
<div class="container package-page-container">
        <div class="pure-g">
            <div class="pure-u-1 pure-u-sm-7-24 pure-u-md-5-24">
                <div class="pure-menu package-menu">
                    <ul class="pure-menu-list"><li class="pure-menu-heading">Links</li>
                        
                        <li class="pure-menu-item">
                            <a href="https://crates.io/crates/wdm" class="pure-menu-link"
                                title="See wdm on crates.io">
                                <span class="fa fa-solid fa-cube " aria-hidden="true"></span> crates.io
                            </a>
                        </li>

                        <li class="pure-menu-heading">Dependencies</li>
                        <li class="pure-menu-item">
                            <div class="pure-menu pure-menu-scrollable sub-menu">
                                <ul class="pure-menu-list">
                                    
                                    <li class="pure-menu-item"><a href="/crate/clap/^4.0" class="pure-menu-link">
                clap ^4.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/reqwest/^0.11" class="pure-menu-link">
                reqwest ^0.11
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/semver/^1.0" class="pure-menu-link">
                semver ^1.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/serde/^1.0" class="pure-menu-link">
                serde ^1.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/serde_json/^1.0" class="pure-menu-link">
                serde_json ^1.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/serde_yaml/^0.9" class="pure-menu-link">
                serde_yaml ^0.9
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/sha2/^0.10" class="pure-menu-link">
                sha2 ^0.10
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/zip/^0.6" class="pure-menu-link">
                zip ^0.6
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/assert_cmd/^2.0" class="pure-menu-link">
                assert_cmd ^2.0
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/predicates/^2.1" class="pure-menu-link">
                predicates ^2.1
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/crate/tempdir/^0.3" class="pure-menu-link">
                tempdir ^0.3
                
                    <i class="dependencies dev">dev</i>
                    
                
            </a>
        </li>
                                </ul>
                            </div>
                        </li>

                        <li class="pure-menu-heading">Versions</li>
                        <li class="pure-menu-item">
                            <div class="pure-menu pure-menu-scrollable sub-menu">
                                <ul class="pure-menu-list">
                                    
                                    
        
         
        <li class="pure-menu-item">
            <a
                href="/crate/wdm/0.1.0"
                
                rel="nofollow"
                class="pure-menu-link warn"
                 title="wdm-0.1.0 is not a library"
                
            ><span class="fa fa-solid fa-triangle-exclamation " aria-hidden="true"></span><b>0.1.0</b> (2024-10-12)</a>
        </li>
                                </ul>
                            </div>
                        </li>

                        
                        <li class="pure-menu-heading">Owners</li>
                        <li class="pure-menu-item"><a href="https://crates.io/users/vcanales">
                                    <img src="https://avatars.githubusercontent.com/u/1157901?v=4" alt="vcanales" class="owner">
                                </a></li>
                    </ul>
                </div>
            </div>

            <div class="pure-u-1 pure-u-sm-17-24 pure-u-md-19-24 package-details" id="main">
                <div class="warning">
                        wdm-0.1.0 is not a library.
                    </div>

                <h1>wdm-cli</h1>
<p><strong>DISCLAIMER: This project is currently in progress and under active development. Features, documentation, and functionality may change or be incomplete.</strong></p>
<p><strong>wdm-cli</strong> is a command-line tool for managing WordPress plugin dependencies. It provides a decentralized alternative that empowers authors with control over where they store their plugins and gives users more granular control over their dependencies. With <strong>wdm-cli</strong>, you can specify exact versions, repositories (including private ones), and manage your WordPress projects' dependencies with greater flexibility.</p>
<h2>Table of Contents</h2>
<ul>
<li><a href="#features">Features</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#getting-started">Getting Started</a>
<ul>
<li><a href="#initialize-wdm-in-your-project">Initialize wdm in Your Project</a></li>
<li><a href="#setting-the-wordpress-path">Setting the WordPress Path</a></li>
</ul>
</li>
<li><a href="#usage">Usage</a>
<ul>
<li><a href="#adding-dependencies">Adding Dependencies</a></li>
<li><a href="#installing-dependencies">Installing Dependencies</a></li>
<li><a href="#using-private-repositories">Using Private Repositories</a></li>
<li><a href="#updating-dependencies">Updating Dependencies</a></li>
<li><a href="#removing-dependencies">Removing Dependencies</a></li>
</ul>
</li>
<li><a href="#configuration">Configuration</a></li>
<li><a href="#examples">Examples</a></li>
<li><a href="#contributing">Contributing</a></li>
<li><a href="#license">License</a></li>
</ul>
<hr />
<h2>Features</h2>
<ul>
<li><strong>Decentralized Dependency Management</strong>: Authors can store plugins in their own repositories, including private ones, giving them full control.</li>
<li><strong>Granular Control</strong>: Users can specify exact versions and repositories, allowing for precise dependency management.</li>
<li><strong>Private Repository Support</strong>: Access private GitHub repositories using tokens defined as environment variables.</li>
<li><strong>Multiple Token Support</strong>: Manage multiple private dependencies that require different tokens.</li>
<li><strong>Lockfile Support</strong>: Keeps track of exact versions installed to ensure consistent environments.</li>
<li><strong>Easy Installation</strong>: Install all dependencies with a single command.</li>
<li><strong>Uninstallation</strong>: Remove dependencies cleanly from your project.</li>
</ul>
<h2>Installation</h2>
<p>You can install <strong>wdm-cli</strong> using Cargo, the Rust package manager:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">cargo</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install wdm-cli</span>
</span></code></pre>
<p>Alternatively, you can clone the repository and build it manually:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">git</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> clone https://github.com/vcanales/wdm-cli.git</span>
<span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-support syntax-function syntax-cd syntax-shell">cd</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> wdm-cli</span>
<span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">cargo</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> build<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>release</span></span>
</span></code></pre>
<p>This will create an executable in <code>target/release/wdm</code>, which you can move to a directory in your PATH.</p>
<h2>Getting Started</h2>
<h3>Initialize wdm in Your Project</h3>
<p>Navigate to your WordPress project directory and initialize <strong>wdm</strong>:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> init</span>
</span></code></pre>
<p>This command creates a <code>wdm.yml</code> file in your current directory, which will hold your dependencies and configuration.</p>
<h3>Setting the WordPress Path</h3>
<p>By default, <strong>wdm</strong> expects your WordPress installation to be in the current directory. If your WordPress installation is located elsewhere, you can set the <code>wordpress_path</code> in the <code>wdm.yml</code> file:</p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml"><span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">config</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span>
  <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">wordpress_path</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-quoted syntax-double syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-yaml">&quot;</span>/path/to/your/wordpress<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-yaml">&quot;</span></span>
<span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">dependencies</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-meta syntax-flow-sequence syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-sequence syntax-begin syntax-yaml">[</span><span class="syntax-punctuation syntax-definition syntax-sequence syntax-end syntax-yaml">]</span></span>
</span></code></pre>
<h2>Usage</h2>
<h3>Adding Dependencies</h3>
<p>To add a plugin to your project, use the <code>add</code> command:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>dependency-name<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-punctuation syntax-terminator syntax-file-descriptor syntax-shell">-</span>-version <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>version<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-punctuation syntax-terminator syntax-file-descriptor syntax-shell">-</span>-repo <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>repository<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-keyword syntax-control syntax-regexp syntax-set syntax-begin syntax-shell">[</span>-<span class="syntax-keyword syntax-operator syntax-word syntax-shell">-</span>token<span class="syntax-keyword syntax-operator syntax-word syntax-shell">-</span>env &lt;token<span class="syntax-keyword syntax-operator syntax-word syntax-shell">-</span>env<span class="syntax-keyword syntax-operator syntax-word syntax-shell">-</span>variable&gt;<span class="syntax-keyword syntax-control syntax-regexp syntax-set syntax-end syntax-shell">]</span></span>
</span></code></pre>
<ul>
<li><code>&lt;dependency-name&gt;</code>: The name you want to give to the dependency.</li>
<li><code>--version</code>: The version of the dependency. You can specify an exact version (e.g., <code>1.8.0</code>), <code>latest</code>, or a version requirement like <code>^1.0</code>.</li>
<li><code>--repo</code>: The repository where the dependency is stored in the format <code>owner/repo</code>.</li>
<li><code>--token-env</code> <em>(optional)</em>: The name of the environment variable that contains the GitHub token for accessing private repositories.</li>
</ul>
<p><strong>Examples:</strong></p>
<ol>
<li>
<p><strong>Adding a Public Dependency:</strong></p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add create-block-theme<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> latest<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> WordPress/create-block-theme</span>
</span></code></pre>
<p>This command adds the <code>create-block-theme</code> plugin from the <code>WordPress/create-block-theme</code> repository at the latest version.</p>
</li>
<li>
<p><strong>Adding a Private Dependency:</strong></p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> latest<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> yourusername/private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>token-env</span> WDM_TOKEN_PRIVATE_PLUGIN</span>
</span></code></pre>
<p>This command adds the <code>private-plugin</code> from your private repository, using the token stored in the <code>WDM_TOKEN_PRIVATE_PLUGIN</code> environment variable.</p>
</li>
</ol>
<h3>Installing Dependencies</h3>
<p>To install all dependencies listed in your <code>wdm.yml</code>, run:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install</span>
</span></code></pre>
<p>This command resolves the versions, downloads the dependencies, and installs them into your WordPress installation.</p>
<h3>Using Private Repositories</h3>
<p><strong>wdm-cli</strong> supports installing dependencies from private GitHub repositories. To access private repositories, you need to provide a GitHub Personal Access Token (PAT). Tokens should be defined as environment variables.</p>
<p>If you have multiple private dependencies that require different tokens, you can specify different environment variables for each dependency.</p>
<h4>Setting Up Tokens</h4>
<ol>
<li>
<p><strong>Create a GitHub Personal Access Token</strong></p>
<ul>
<li>Log in to your GitHub account.</li>
<li>Navigate to <strong>Settings</strong> &gt; <strong>Developer settings</strong> &gt; <strong>Personal access tokens</strong>.</li>
<li>Click <strong>Generate new token</strong>.</li>
<li>Select the scopes you need (usually <code>repo</code> for private repositories).</li>
<li>Generate the token and copy it.</li>
</ul>
</li>
<li>
<p><strong>Define Environment Variables</strong></p>
<ul>
<li>For each private dependency, define an environment variable with the token.</li>
<li>Use a naming convention that associates the token with the dependency.</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-storage syntax-modifier syntax-shell">export</span> <span class="syntax-variable syntax-other syntax-readwrite syntax-assignment syntax-shell">WDM_TOKEN_CUSTOM_PLUGIN</span><span class="syntax-keyword syntax-operator syntax-assignment syntax-shell">=</span><span class="syntax-string syntax-unquoted syntax-shell"><span class="syntax-string syntax-quoted syntax-double syntax-shell"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-shell">&quot;</span>your-token-for-custom-plugin<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-shell">&quot;</span></span></span></span>
<span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-storage syntax-modifier syntax-shell">export</span> <span class="syntax-variable syntax-other syntax-readwrite syntax-assignment syntax-shell">WDM_TOKEN_ANOTHER_PLUGIN</span><span class="syntax-keyword syntax-operator syntax-assignment syntax-shell">=</span><span class="syntax-string syntax-unquoted syntax-shell"><span class="syntax-string syntax-quoted syntax-double syntax-shell"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-shell">&quot;</span>your-token-for-another-plugin<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-shell">&quot;</span></span></span></span>
</span></code></pre>
</li>
</ol>
<h4>Adding Private Dependencies</h4>
<p>When adding a private dependency, specify the environment variable that contains the token using the <code>--token-env</code> option.</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>dependency-name<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-punctuation syntax-terminator syntax-file-descriptor syntax-shell">-</span>-version <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>version<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-punctuation syntax-terminator syntax-file-descriptor syntax-shell">-</span>-repo <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>repository<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span> <span class="syntax-punctuation syntax-terminator syntax-file-descriptor syntax-shell">-</span>-token-env <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>token-env-variable<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span>
</span></span></code></pre>
<ul>
<li><code>--token-env</code>: The name of the environment variable that contains the token for this dependency.</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> latest<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> yourusername/private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>token-env</span> WDM_TOKEN_CUSTOM_PLUGIN</span>
</span></code></pre>
<h4>Installing Private Dependencies</h4>
<p>When you run <code>wdm install</code>, <strong>wdm-cli</strong> will use the specified environment variables to access the private repositories.</p>
<p><strong>Important:</strong></p>
<ul>
<li>Ensure that the environment variables are set in your shell or CI environment before running <code>wdm install</code>.</li>
<li>Do not commit your tokens to version control. Use environment variables to keep your tokens secure.</li>
</ul>
<h3>Updating Dependencies</h3>
<p>If you want to update a dependency to a newer version, you can change the version in <code>wdm.yml</code> and run <code>wdm install</code> again.</p>
<p><strong>Example:</strong></p>
<ol>
<li>
<p>Edit <code>wdm.yml</code>:</p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml"><span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">dependencies</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span>
  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">name</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">private-plugin</span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">version</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-quoted syntax-double syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-yaml">&quot;</span>1.0.0<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-yaml">&quot;</span></span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">repo</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">yourusername/private-plugin</span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">token_env</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">WDM_TOKEN_CUSTOM_PLUGIN</span>
</span></code></pre>
</li>
<li>
<p>Change the version to <code>&quot;1.1.0&quot;</code> or <code>&quot;latest&quot;</code>:</p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml"><span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">dependencies</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span>
  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">name</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">private-plugin</span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">version</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-quoted syntax-double syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-yaml">&quot;</span>latest<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-yaml">&quot;</span></span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">repo</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">yourusername/private-plugin</span>
    <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">token_env</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">WDM_TOKEN_CUSTOM_PLUGIN</span>
</span></code></pre>
</li>
<li>
<p>Run the install command:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install</span>
</span></code></pre>
</li>
</ol>
<h3>Removing Dependencies</h3>
<p>To remove a dependency from your project, use the <code>remove</code> command:</p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> remove <span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&lt;</span>dependency-name<span class="syntax-keyword syntax-operator syntax-assignment syntax-redirection syntax-shell">&gt;</span>
</span></span></code></pre>
<p><strong>Example:</strong></p>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> remove private-plugin</span>
</span></code></pre>
<p>This command removes <code>private-plugin</code> from your <code>wdm.yml</code> and uninstalls it from your WordPress installation.</p>
<h2>Configuration</h2>
<p>Below is a table detailing all the supported fields in the <code>wdm.yml</code> configuration file for <strong>wdm-cli</strong>, including their default values.</p>
<table>
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>Required</strong></th>
<th><strong>Default Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>config</code></td>
<td>Object</td>
<td>Contains configuration settings for <strong>wdm-cli</strong>.</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td><code>config.wordpress_path</code></td>
<td>String</td>
<td>Specifies the file system path to your WordPress installation. Defaults to the current directory if not set.</td>
<td>Yes</td>
<td>Current working directory (<code>.</code>)</td>
</tr>
<tr>
<td><code>dependencies</code></td>
<td>Array</td>
<td>Lists all the dependencies (plugins/themes) managed by <strong>wdm-cli</strong>.</td>
<td>Yes</td>
<td>Empty array <code>[]</code></td>
</tr>
<tr>
<td><code>dependencies[].name</code></td>
<td>String</td>
<td>The unique name you assign to the dependency.</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td><code>dependencies[].version</code></td>
<td>String</td>
<td>The version of the dependency. Can be an exact version (e.g., <code>1.8.0</code>), <code>latest</code>, or a version requirement like <code>^1.0</code>.</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td><code>dependencies[].repo</code></td>
<td>String</td>
<td>The GitHub repository of the dependency in the format <code>owner/repo</code>.</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td><code>dependencies[].token_env</code></td>
<td>String</td>
<td><em>(Optional)</em> The name of the environment variable that contains the GitHub token for accessing private repositories.</td>
<td>No</td>
<td>N/A</td>
</tr>
</tbody>
</table>
<h3>Detailed Descriptions</h3>
<h4>1. <code>config</code> Object</h4>
<ul>
<li>
<p><strong><code>wordpress_path</code></strong></p>
<ul>
<li><strong>Type:</strong> String</li>
<li><strong>Description:</strong> Defines the absolute or relative path to your WordPress installation directory. If not specified, <strong>wdm-cli</strong> assumes the current working directory is the WordPress path.</li>
<li><strong>Required:</strong> Yes</li>
<li><strong>Default Value:</strong> Current working directory (<code>.</code>)</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml"><span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">config</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span>
  <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">wordpress_path</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-quoted syntax-double syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-yaml">&quot;</span>/var/www/html/wordpress<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-yaml">&quot;</span></span>
</span></code></pre>
</li>
</ul>
<h4>2. <code>dependencies</code> Array</h4>
<p>Each item in the <code>dependencies</code> array represents a plugin that you want to manage with <strong>wdm-cli</strong>.</p>
<ul>
<li>
<p><strong><code>name</code></strong></p>
<ul>
<li><strong>Type:</strong> String</li>
<li><strong>Description:</strong> A unique identifier for the dependency within your project. This name is used to reference the dependency in <strong>wdm-cli</strong> commands.</li>
<li><strong>Required:</strong> Yes</li>
<li><strong>Default Value:</strong> N/A</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml"><span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">dependencies</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span>
  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">name</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">custom-plugin</span>
</span></code></pre>
</li>
<li>
<p><strong><code>version</code></strong></p>
<ul>
<li><strong>Type:</strong> String</li>
<li><strong>Description:</strong> Specifies the version of the dependency to install. It can be:
<ul>
<li>An exact version number (e.g., <code>1.8.0</code>)</li>
<li><code>latest</code> to fetch the most recent version</li>
<li>A semantic version requirement (e.g., <code>^1.0</code>)</li>
</ul>
</li>
<li><strong>Required:</strong> Yes</li>
<li><strong>Default Value:</strong> N/A</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml">  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">version</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-quoted syntax-double syntax-yaml"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-yaml">&quot;</span>^1.8.0<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-yaml">&quot;</span></span>
</span></code></pre>
</li>
<li>
<p><strong><code>repo</code></strong></p>
<ul>
<li><strong>Type:</strong> String</li>
<li><strong>Description:</strong> The GitHub repository where the dependency is hosted, formatted as <code>owner/repo</code>.</li>
<li><strong>Required:</strong> Yes</li>
<li><strong>Default Value:</strong> N/A</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml">  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">repo</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">yourusername/custom-plugin</span>
</span></code></pre>
</li>
<li>
<p><strong><code>token_env</code></strong></p>
<ul>
<li><strong>Type:</strong> String</li>
<li><strong>Description:</strong> <em>(Optional)</em> The name of the environment variable that holds the GitHub Personal Access Token (PAT) required to access private repositories.</li>
<li><strong>Required:</strong> No</li>
<li><strong>Default Value:</strong> N/A</li>
</ul>
<p><strong>Example:</strong></p>
<pre><code class="language-yaml"><span class="syntax-source syntax-yaml">  <span class="syntax-punctuation syntax-definition syntax-block syntax-sequence syntax-item syntax-yaml">-</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml"><span class="syntax-entity syntax-name syntax-tag syntax-yaml">token_env</span></span><span class="syntax-punctuation syntax-separator syntax-key-value syntax-mapping syntax-yaml">:</span> <span class="syntax-string syntax-unquoted syntax-plain syntax-out syntax-yaml">WDM_TOKEN_CUSTOM_PLUGIN</span>
</span></code></pre>
</li>
</ul>
<hr />
<h2>Examples</h2>
<h3>Adding and Installing a Private Plugin from a Personal Repository</h3>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Set up the environment variable with your token</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-storage syntax-modifier syntax-shell">export</span> <span class="syntax-variable syntax-other syntax-readwrite syntax-assignment syntax-shell">WDM_TOKEN_CUSTOM_PLUGIN</span><span class="syntax-keyword syntax-operator syntax-assignment syntax-shell">=</span><span class="syntax-string syntax-unquoted syntax-shell"><span class="syntax-string syntax-quoted syntax-double syntax-shell"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-shell">&quot;</span>your-token-for-custom-plugin<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-shell">&quot;</span></span></span></span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Initialize wdm</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> init</span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Add a private plugin from your own repository</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> ^1.0<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> yourusername/private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>token-env</span> WDM_TOKEN_CUSTOM_PLUGIN</span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Install all dependencies</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install</span>
</span></code></pre>
<h3>Using Multiple Private Dependencies with Different Tokens</h3>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Set up environment variables for each token</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-storage syntax-modifier syntax-shell">export</span> <span class="syntax-variable syntax-other syntax-readwrite syntax-assignment syntax-shell">WDM_TOKEN_CUSTOM_PLUGIN</span><span class="syntax-keyword syntax-operator syntax-assignment syntax-shell">=</span><span class="syntax-string syntax-unquoted syntax-shell"><span class="syntax-string syntax-quoted syntax-double syntax-shell"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-shell">&quot;</span>your-token-for-custom-plugin<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-shell">&quot;</span></span></span></span>
<span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-storage syntax-modifier syntax-shell">export</span> <span class="syntax-variable syntax-other syntax-readwrite syntax-assignment syntax-shell">WDM_TOKEN_ANOTHER_PLUGIN</span><span class="syntax-keyword syntax-operator syntax-assignment syntax-shell">=</span><span class="syntax-string syntax-unquoted syntax-shell"><span class="syntax-string syntax-quoted syntax-double syntax-shell"><span class="syntax-punctuation syntax-definition syntax-string syntax-begin syntax-shell">&quot;</span>your-token-for-another-plugin<span class="syntax-punctuation syntax-definition syntax-string syntax-end syntax-shell">&quot;</span></span></span></span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Add the first private plugin</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> ^1.0<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> yourusername/private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>token-env</span> WDM_TOKEN_CUSTOM_PLUGIN</span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Add the second private plugin</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> add another-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>version</span> ^2.0<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>repo</span> anotheruser/private-plugin<span class="syntax-variable syntax-parameter syntax-option syntax-shell"><span class="syntax-punctuation syntax-definition syntax-parameter syntax-shell"> --</span>token-env</span> WDM_TOKEN_ANOTHER_PLUGIN</span>

<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Install all dependencies</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install</span>
</span></code></pre>
<h3>Updating a Private Plugin to a Specific Version</h3>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Update the version in wdm.yml</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Change the version of private-plugin to &quot;1.2.0&quot;</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span>
<span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Install the updated dependencies</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> install</span>
</span></code></pre>
<h3>Removing a Private Plugin</h3>
<pre><code class="language-bash"><span class="syntax-source syntax-shell syntax-bash"><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"><span class="syntax-punctuation syntax-definition syntax-comment syntax-begin syntax-shell">#</span></span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell"> Remove the private plugin</span><span class="syntax-comment syntax-line syntax-number-sign syntax-shell">
</span><span class="syntax-meta syntax-function-call syntax-shell"><span class="syntax-variable syntax-function syntax-shell">wdm</span></span><span class="syntax-meta syntax-function-call syntax-arguments syntax-shell"> remove private-plugin</span>
</span></code></pre>
<h2>Contributing</h2>
<p>Contributions are welcome! Please open an issue or submit a pull request on GitHub.</p>
<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
<p><strong>Disclaimer:</strong></p>
<p>When handling tokens and private repositories, always ensure you follow best security practices:</p>
<ul>
<li><strong>Never commit tokens to version control.</strong></li>
<li><strong>Use environment variables to manage sensitive information.</strong></li>
<li><strong>Limit the scopes and permissions of your tokens to only what is necessary.</strong></li>
</ul>


                </div>
        </div>
    </div></body>
</html>