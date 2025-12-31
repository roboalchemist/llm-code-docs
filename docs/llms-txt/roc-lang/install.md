# Source: https://www.roc-lang.org/install#additional-learning-resources

# Source: https://www.roc-lang.org/install

<!DOCTYPE html><html  lang="en" class="no-js"><head><meta  charset="utf-8"><title>Install | Roc</title><meta  name="description" content="How to install the Roc programming language."><meta  name="viewport" content="width=device-width"><link  rel="icon" href="/favicon.svg"><link  rel="prefetch" href="/repl/roc_repl_wasm.js"><link  rel="stylesheet" href="/site.css"><link  rel="mask-icon" href="/favicon.svg" color="#7d59dd"><script>document.documentElement.className = document.documentElement.className.replace('no-js', '');</script></head><body  class="article-layout"><header  id="top-bar"><nav  aria-label="primary"><a  id="nav-home-link" href="/" title="The Roc Programming Language Homepage"><svg  viewBox="0 -6 51 58" xmlns="http://www.w3.org/2000/svg" aria-labelledby="logo-link" role="img" class="roc-logo"><title  id="logo-link">Return to Roc Home</title><polygon  role="presentation" points="0,0 23.8834,3.21052 37.2438,19.0101 45.9665,16.6324 50.5,22 45,22 44.0315,26.3689 26.4673,39.3424 27.4527,45.2132 17.655,53 23.6751,22.7086"></polygon></svg><span  class="home-link-text">Roc</span></a><div  id="top-bar-links"><a  href="/tutorial">Tutorial</a><a  href="/install">Install</a><a  href="/examples">Examples</a><a  href="/community">Community</a><a  href="/docs">Docs</a><a  href="/donate">Donate</a></div></nav></header><main><h1>Install</h1>
<p>Roc is a very young language with many incomplete features and known bugs. It doesn't even have a numbered release yet, but it does have <a href="https://github.com/roc-lang/roc/releases">nightly builds</a> that you can download, if you'd like to try it out without <a href="https://github.com/roc-lang/roc/blob/main/BUILDING_FROM_SOURCE.md">building from source</a>! There are also <a href="https://hub.docker.com/u/roclang">official Docker images</a> if you prefer to run Roc within a container.</p>
<div class="banner">
    Roc is a <b>Work in Progress!</b> See the <a href="/plans">plans</a> page for more information.
</div>
<p>There are currently a few known OS-specific issues:</p>
<ul>
<li><strong>macOS:</strong> There are no known compatibility issues, but the compiler doesn't run as fast as it does on Linux or Windows, because we don't (yet) do our own linking like we do on those targets. (Linking works similarly on Linux and Windows, but the way macOS does it is both different and significantly more complicated.)</li>
<li><strong>Windows:</strong> There are some known Windows-specific compiler bugs, and probably some other unknown ones because more people have tried out Roc on Mac and Linux than on Windows.</li>
<li><strong>Linux:</strong> The nightlies are built with glibc, so they aren't usable on distros that don't use glibc, like Alpine. In the future we plan to build Linux releases with <a href="https://wiki.musl-libc.org/">musl libc</a> to address this, but this requires <a href="https://wiki.musl-libc.org/building-llvm.html">building LLVM from source with musl</a>.</li>
<li><strong>Other operating systems:</strong> Roc has not been built on any other operating systems. <a href="https://github.com/roc-lang/roc/blob/main/BUILDING_FROM_SOURCE.md">Building from source</a> on another OS might work, but you might very well be the first person ever to try it!</li>
</ul>
<h3 id="getting-started"><a href="#getting-started">Getting Started</a></h3>
<p>Here are some Getting Started guides for different operating systems:</p>
<!-- TODO detect current OS with browser and only show link for that, provide other button for others  -->
<ul>
<li><a href="/install/linux_x86_64">Linux x86-64</a></li>
<li><a href="/install/linux_arm64">Linux arm64</a></li>
<li><a href="/install/nix">Nix Linux/MacOS</a></li>
<li><a href="/install/macos_apple_silicon">MacOS Apple Silicon</a></li>
<li><a href="/install/macos_x86_64">MacOS x86-64</a></li>
<li><a href="/install/windows">Windows</a></li>
<li><a href="/install/other">Other Systems</a></li>
</ul>
<h3 id="editor-extensions"><a href="#editor-extensions">Editor Extensions/Plugins</a></h3>
<ul>
<li><a href="https://visualstudio.microsoft.com/#vscode-section">Visual Studio Code</a>
<ul>
<li>Features: syntax highlighting, completion, type hints, jump to source</li>
<li>syntax highlighting, completion, type hints, jump to source</li>
<li>install the <a href="https://marketplace.visualstudio.com/items?itemName=IvanDemchenko.roc-lang-unofficial">Roc Plugin</a>
<ul>
<li>âmake sure to follow <a href="https://github.com/ivan-demchenko/roc-vscode-unofficial?tab=readme-ov-file#configuring-language-server">&quot;Configuring language server&quot;</a>.</li>
<li>It would be a fantastic contribution for the language server to be set up automatically. If you'd like to help with this, just make a post in <a href="https://roc.zulipchat.com/#narrow/stream/316715-contributing/topic/new.20contributors">the &quot;new contributors&quot; topic on Zulip</a> and say hello!</li>
</ul>
</li>
</ul>
</li>
<li><a href="https://zed.dev/download">Zed</a>, since Version 0.133.5
<ul>
<li>Features: syntax highlighting, completion, type hints, jump to source</li>
<li>search and install roc extension (action <code>zed: extensions</code>)</li>
<li>in case of errors look into the Zed log (action <code>zed: open log</code>)</li>
</ul>
</li>
<li>For other editors like Vim, Helix or Emacs, see <a href="https://github.com/faldor20/tree-sitter-roc">tree-sitter-roc</a></li>
</ul>
<h3 id="tutorial"><a href="#tutorial">Tutorial</a></h3>
<p>Once you've installed <code>roc</code>, check out the <a href="/tutorial">tutorial</a> to learn how to Roc!</p>
<p><a class="btn-small" href="/tutorial">Start Tutorial</a></p>
<h3 id="additional-learning-resources"><a href="#additional-learning-resources">Additional Learning Resources</a></h3>
<p>If you are looking for more resources to learn about Roc, check out the following:</p>
<ul>
<li><a href="/examples">Roc Examples</a></li>
<li><a href="/docs#guides">Roc Guides</a></li>
<li><a href="/docs#language-reference">Roc Language Reference</a></li>
<li><a href="https://exercism.org/tracks/roc">Roc Exercism Track</a></li>
</ul>
</main><footer><div  id="footer"><div  id="gh-link"><a  id="gh-centered-link" href="https://github.com/roc-lang/roc"><svg  viewBox="0 0 98 96" height="25" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" role="img" id="gh-logo"><path  d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"></path></svg><span  id="gh-link-text">roc-lang/roc</span></a></div></div></footer></body></html>