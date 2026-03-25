<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="generator" content="rustdoc"><meta name="description" content="API documentation for the Rust `mailparse` crate."><title>mailparse - Rust</title><script>if(window.location.protocol!=="file:")document.head.insertAdjacentHTML("beforeend","SourceSerif4-Regular-6b053e98.ttf.woff2,FiraSans-Italic-81dc35de.woff2,FiraSans-Regular-0fe48ade.woff2,FiraSans-MediumItalic-ccf7e434.woff2,FiraSans-Medium-e1aa3f0a.woff2,SourceCodePro-Regular-8badfe75.ttf.woff2,SourceCodePro-Semibold-aa29a496.ttf.woff2".split(",").map(f=>`<link rel="preload" as="font" type="font/woff2"href="/-/rustdoc.static/${f}">`).join(""))</script><link rel="stylesheet" href="/-/rustdoc.static/normalize-9960930a.css"><link rel="stylesheet" href="/-/static/vendored.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/rustdoc.static/rustdoc-e56847b5.css"><meta name="rustdoc-vars" data-root-path="../" data-static-root-path="/-/rustdoc.static/" data-current-crate="mailparse" data-themes="" data-resource-suffix="-20250919-1.92.0-nightly-0be8e1608" data-rustdoc-version="1.92.0-nightly (0be8e1608 2025-09-19)" data-channel="nightly" data-search-js="search-e256b49e.js" data-stringdex-js="stringdex-061df703.js" data-settings-js="settings-c38705f0.js" ><script src="/-/rustdoc.static/storage-e2aeef58.js"></script><script defer src="../crates-20250919-1.92.0-nightly-0be8e1608.js"></script><script defer src="/-/rustdoc.static/main-6dc2a7f3.js"></script><noscript><link rel="stylesheet" href="/-/rustdoc.static/noscript-263c88ec.css"></noscript><link rel="alternate icon" type="image/png" href="/-/rustdoc.static/favicon-32x32-eab170b8.png"><link rel="icon" type="image/svg+xml" href="/-/rustdoc.static/favicon-044be391.svg"><link rel="stylesheet" href="/-/static/rustdoc-2025-08-20.css?0-0-0-a68728e7-2026-03-08" media="all" /><link rel="stylesheet" href="/-/static/font-awesome.css?0-0-0-a68728e7-2026-03-08" media="all" />

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
            "name": "mailparse",
            "version": "0.16.1"
        }
    </script><li class="pure-menu-item pure-menu-has-children">
            <a href="#" class="pure-menu-link crate-name" title="A simple parser for MIME e-mail messages">
                <span class="fa fa-solid fa-cube " aria-hidden="true"></span>
                <span class="title">mailparse-0.16.1</span>
            </a><div class="pure-menu-children package-details-menu">
                
                <ul class="pure-menu-list menu-item-divided">
                    <li class="pure-menu-heading" id="crate-title">
                        mailparse 0.16.1
                        <span id="clipboard" class="svg-clipboard" title="Copy crate name and version information"></span>
                    </li><li class="pure-menu-item">
                        <a href="/mailparse/0.16.1/mailparse/" class="pure-menu-link description" id="permalink" title="Get a link to this specific version"><span class="fa fa-solid fa-link " aria-hidden="true"></span> Permalink
                        </a>
                    </li><li class="pure-menu-item">
                        <a href="/crate/mailparse/latest" class="pure-menu-link description" title="See mailparse in docs.rs">
                            <span class="fa fa-solid fa-cube " aria-hidden="true"></span> Docs.rs crate page
                        </a>
                    </li><li class="pure-menu-item">
                            <span class="pure-menu-link description"><span class="fa fa-solid fa-scale-unbalanced-flip " aria-hidden="true"></span>
                            <a href="https://spdx.org/licenses/0BSD" class="pure-menu-sublink">0BSD</a></span>
                        </li></ul>

                <div class="pure-g menu-item-divided">
                    <div class="pure-u-1-2 right-border">
                        <ul class="pure-menu-list">
                            <li class="pure-menu-heading">Links</li>

                            <li class="pure-menu-item">
                                    <a href="https://github.com/staktrace/mailparse/blob/master/README.md" class="pure-menu-link">
                                        <span class="fa fa-solid fa-house " aria-hidden="true"></span> Homepage
                                    </a>
                                </li><li class="pure-menu-item">
                                    <a href="https://github.com/staktrace/mailparse" class="pure-menu-link">
                                        <span class="fa fa-solid fa-code-branch " aria-hidden="true"></span> Repository
                                    </a>
                                </li><li class="pure-menu-item">
                                <a href="https://crates.io/crates/mailparse" class="pure-menu-link" title="See mailparse in crates.io">
                                    <span class="fa fa-solid fa-cube " aria-hidden="true"></span> crates.io
                                </a>
                            </li>

                            
                            <li class="pure-menu-item">
                                <a href="/crate/mailparse/latest/source/" title="Browse source of mailparse-0.16.1" class="pure-menu-link">
                                    <span class="fa fa-solid fa-folder-open " aria-hidden="true"></span> Source
                                </a>
                            </li>
                        </ul>
                    </div><div class="pure-u-1-2">
                        <ul class="pure-menu-list" id="topbar-owners">
                            <li class="pure-menu-heading">Owners</li><li class="pure-menu-item">
                                    <a href="https://crates.io/users/staktrace" class="pure-menu-link">
                                        <span class="fa fa-solid fa-user " aria-hidden="true"></span> staktrace
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
                                        <li class="pure-menu-item"><a href="/charset/^0.1.3/" class="pure-menu-link">
                charset ^0.1.3
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/data-encoding/^2.6.0/" class="pure-menu-link">
                data-encoding ^2.6.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/quoted_printable/^0.5.0/" class="pure-menu-link">
                quoted_printable ^0.5.0
                
                    <i class="dependencies normal">normal</i>
                    
                
            </a>
        </li><li class="pure-menu-item"><a href="/ouroboros/^0.17.0/" class="pure-menu-link">
                ouroboros ^0.17.0
                
                    <i class="dependencies dev">dev</i>
                    
                
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
                                <div class="pure-menu pure-menu-scrollable sub-menu" id="releases-list" tabindex="-1" data-url="/crate/mailparse/latest/menus/releases/mailparse/">
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
                                    <a href="/crate/mailparse/latest" class="pure-menu-link">
                                        <b>87.21%</b>
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

                
                <ul class="pure-menu-children" id="platforms" data-url="/crate/mailparse/latest/menus/platforms/mailparse/"><li class="pure-menu-item">
            <a href="/crate/mailparse/latest/target-redirect/i686-pc-windows-msvc/mailparse/" class="pure-menu-link" data-fragment="retain" rel="nofollow">i686-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/mailparse/latest/target-redirect/i686-unknown-linux-gnu/mailparse/" class="pure-menu-link" data-fragment="retain" rel="nofollow">i686-unknown-linux-gnu</a>
        </li><li class="pure-menu-item">
            <a href="/crate/mailparse/latest/target-redirect/x86_64-apple-darwin/mailparse/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-apple-darwin</a>
        </li><li class="pure-menu-item">
            <a href="/crate/mailparse/latest/target-redirect/x86_64-pc-windows-msvc/mailparse/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-pc-windows-msvc</a>
        </li><li class="pure-menu-item">
            <a href="/crate/mailparse/latest/target-redirect/mailparse/" class="pure-menu-link" data-fragment="retain" rel="nofollow">x86_64-unknown-linux-gnu</a>
        </li></ul>
            </li><li class="pure-menu-item">
                <a href="/crate/mailparse/latest/features" title="Browse available feature flags of mailparse-0.16.1" class="pure-menu-link">
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

<iframe src="/-/storage-change-detection.html" width="0" height="0" style="display: none"></iframe><!--[if lte IE 11]><div class="warning">This old browser is unsupported and will most likely display funky things.</div><![endif]--><rustdoc-topbar><h2><a href="#">Crate mailparse</a></h2></rustdoc-topbar><nav class="sidebar"><div class="sidebar-crate"><h2><a href="../mailparse/index.html">mailparse</a><span class="version">0.16.1</span></h2></div><div class="sidebar-elems"><ul class="block"><li><a id="all-types" href="all.html">All Items</a></li></ul><section id="rustdoc-toc"><h3><a href="#modules">Crate Items</a></h3><ul class="block"><li><a href="#modules" title="Modules">Modules</a></li><li><a href="#structs" title="Structs">Structs</a></li><li><a href="#enums" title="Enums">Enums</a></li><li><a href="#traits" title="Traits">Traits</a></li><li><a href="#functions" title="Functions">Functions</a></li></ul></section><div id="rustdoc-modnav"></div></div></nav><div class="sidebar-resizer" title="Drag to resize sidebar"></div><main><div class="width-limiter"><section id="main-content" class="content"><div class="main-heading"><h1>Crate <span>mailparse</span>&nbsp;<button id="copy-path" title="Copy item path to clipboard">Copy item path</button></h1><rustdoc-toolbar></rustdoc-toolbar><span class="sub-heading"><a class="src" href="../src/mailparse/lib.rs.html#1-2189">Source</a> </span></div><h2 id="modules" class="section-header">Modules<a href="#modules" class="anchor">§</a></h2><dl class="item-table"><dt><a class="mod" href="body/index.html" title="mod mailparse::body">body</a></dt><dt><a class="mod" href="headers/index.html" title="mod mailparse::headers">headers</a></dt></dl><h2 id="structs" class="section-header">Structs<a href="#structs" class="anchor">§</a></h2><dl class="item-table"><dt><a class="struct" href="struct.GroupInfo.html" title="struct mailparse::GroupInfo">Group<wbr>Info</a></dt><dd>A representation of a group address. It has a name and
a list of mailboxes.</dd><dt><a class="struct" href="struct.MailAddrList.html" title="struct mailparse::MailAddrList">Mail<wbr>Addr<wbr>List</a></dt><dd>A simple wrapper around <code>Vec&lt;MailAddr&gt;</code>. This is primarily here so we can
implement the Display trait on it, and allow user code to easily convert
the return value from <code>addrparse</code> back into a string. However there are some
additional utility functions on this wrapper as well.</dd><dt><a class="struct" href="struct.MailHeader.html" title="struct mailparse::MailHeader">Mail<wbr>Header</a></dt><dd>A struct that represents a single header in the message.
It holds slices into the raw byte array passed to parse_mail, and so the
lifetime of this struct must be contained within the lifetime of the raw
input. There are additional accessor functions on this struct to extract
the data as Rust strings.</dd><dt><a class="struct" href="struct.MessageIdList.html" title="struct mailparse::MessageIdList">Message<wbr>IdList</a></dt><dd>A simple wrapper around <code>Vec&lt;String&gt;</code>. This is primarily here so we can
implement the Display trait on it, and allow user code to easily convert
the return value from <code>msgidparse</code> back into a string. This also allows
to add additional methods on this type in the future.</dd><dt><a class="struct" href="struct.ParsedContentDisposition.html" title="struct mailparse::ParsedContentDisposition">Parsed<wbr>Content<wbr>Disposition</a></dt><dd>A struct to hold a more structured representation of the Content-Disposition header.
This is provided mostly as a convenience since this metadata is usually
needed to interpret the message body properly.</dd><dt><a class="struct" href="struct.ParsedContentType.html" title="struct mailparse::ParsedContentType">Parsed<wbr>Content<wbr>Type</a></dt><dd>A struct to hold a more structured representation of the Content-Type header.
This is provided mostly as a convenience since this metadata is usually
needed to interpret the message body properly.</dd><dt><a class="struct" href="struct.ParsedMail.html" title="struct mailparse::ParsedMail">Parsed<wbr>Mail</a></dt><dd>Struct that holds the structured representation of the message. Note that
since MIME allows for nested multipart messages, a tree-like structure is
necessary to represent it properly. This struct accomplishes that by holding
a vector of other ParsedMail structures for the subparts.</dd><dt><a class="struct" href="struct.PartsIterator.html" title="struct mailparse::PartsIterator">Parts<wbr>Iterator</a></dt><dt><a class="struct" href="struct.SingleInfo.html" title="struct mailparse::SingleInfo">Single<wbr>Info</a></dt><dd>A representation of a single mailbox. Each mailbox has
a routing address <code>addr</code> and an optional display name.</dd></dl><h2 id="enums" class="section-header">Enums<a href="#enums" class="anchor">§</a></h2><dl class="item-table"><dt><a class="enum" href="enum.DispositionType.html" title="enum mailparse::DispositionType">Disposition<wbr>Type</a></dt><dd>The possible disposition types in a Content-Disposition header. A more
comprehensive list of IANA-recognized types can be found at
https://www.iana.org/assignments/cont-disp/cont-disp.xhtml. This library
only enumerates the types most commonly found in email messages, and
provides the <code>Extension</code> value for holding all other types.</dd><dt><a class="enum" href="enum.MailAddr.html" title="enum mailparse::MailAddr">Mail<wbr>Addr</a></dt><dd>An abstraction over the two different kinds of top-level addresses allowed
in email headers. Group addresses have a name and a list of mailboxes. Single
addresses are just a mailbox. Each mailbox consists of what you would consider
an email address (e.g. foo@bar.com) and optionally a display name (“Foo Bar”).
Groups are represented in email headers with colons and semicolons, e.g.
To: my-peeps: foo@peeps.org, bar@peeps.org;</dd><dt><a class="enum" href="enum.MailParseError.html" title="enum mailparse::MailParseError">Mail<wbr>Parse<wbr>Error</a></dt><dd>An error type that represents the different kinds of errors that may be
encountered during message parsing.</dd></dl><h2 id="traits" class="section-header">Traits<a href="#traits" class="anchor">§</a></h2><dl class="item-table"><dt><a class="trait" href="trait.MailHeaderMap.html" title="trait mailparse::MailHeaderMap">Mail<wbr>Header<wbr>Map</a></dt><dd>A trait that is implemented by the <a href="struct.MailHeader.html" title="struct mailparse::MailHeader">MailHeader</a> slice. These functions are
also available on Vec<MailHeader> which is returned by the parse_headers
function. It provides a map-like interface to look up header values by their
name.</dd></dl><h2 id="functions" class="section-header">Functions<a href="#functions" class="anchor">§</a></h2><dl class="item-table"><dt><a class="fn" href="fn.addrparse.html" title="fn mailparse::addrparse">addrparse</a></dt><dd>Convert an address field from an email header into a structured type.
This function handles the most common formatting of to/from/cc/bcc fields
found in email headers. Note that if you are attempting to parse the
value of a <code>MailHeader</code>, it is better (both for correctness and performance
to use the <code>addrparse_header</code> function instead of this one. Correctness
is impacted because of the way encoded words within the header are
processed; using <code>MailHeader::get_value()</code> will decode encoded words,
which may then contain characters like commas that affect how <code>addrparse</code>
parses the value. This can produce incorrect results in some cases; using
<code>addrparse_header</code> will avoid this problem.</dd><dt><a class="fn" href="fn.addrparse_header.html" title="fn mailparse::addrparse_header">addrparse_<wbr>header</a></dt><dd>Take a <code>MailHeader</code> that contains addresses in the value (e.g. from/to/cc/bcc)
and produce a structured type representing those addresses.</dd><dt><a class="fn" href="fn.dateparse.html" title="fn mailparse::dateparse">dateparse</a></dt><dd>Convert a date field from an email header into a UNIX epoch timestamp.
This function handles the most common formatting of date fields found in
email headers. It may fail to parse some of the more creative formattings.</dd><dt><a class="fn" href="fn.msgidparse.html" title="fn mailparse::msgidparse">msgidparse</a></dt><dd>Parse an email header into a structured type holding a list of message ids.
This function can be used to parse headers containing message IDs, such as
<code>Message-ID</code>, <code>In-Reply-To</code>, and <code>References</code>.
This function is currently mostly trivial (splits on whitespace and strips
angle-brackets) but may be enhanced in the future to strip comments (which
are technically allowed by the RFCs but never really used in practice).</dd><dt><a class="fn" href="fn.parse_content_disposition.html" title="fn mailparse::parse_content_disposition">parse_<wbr>content_<wbr>disposition</a></dt><dd>Helper method to parse a header value as a Content-Disposition header. The disposition
defaults to “inline” if no disposition parameter is provided in the header
value.</dd><dt><a class="fn" href="fn.parse_content_type.html" title="fn mailparse::parse_content_type">parse_<wbr>content_<wbr>type</a></dt><dd>Helper method to parse a header value as a Content-Type header. Note that
the returned object’s <code>params</code> map will contain a charset key if a charset
was explicitly specified in the header; otherwise the <code>params</code> map will not
contain a charset key. Regardless, the <code>charset</code> field will contain a
charset - either the one explicitly specified or the default of “us-ascii”.</dd><dt><a class="fn" href="fn.parse_header.html" title="fn mailparse::parse_header">parse_<wbr>header</a></dt><dd>Parse a single header from the raw data given.
This function takes raw byte data, and starts parsing it, expecting there
to be a MIME header key-value pair right at the beginning. It parses that
header and returns it, along with the index at which the next header is
expected to start. If you just want to parse a single header, you can ignore
the second component of the tuple, which is the index of the next header.
Error values are returned if the data could not be successfully interpreted
as a MIME key-value pair.</dd><dt><a class="fn" href="fn.parse_headers.html" title="fn mailparse::parse_headers">parse_<wbr>headers</a></dt><dd>Parses all the headers from the raw data given.
This function takes raw byte data, and starts parsing it, expecting there
to be zero or more MIME header key-value pair right at the beginning,
followed by two consecutive newlines (i.e. a blank line). It parses those
headers and returns them in a vector. The normal vector functions can be
used to access the headers linearly, or the MailHeaderMap trait can be used
to access them in a map-like fashion. Along with this vector, the function
returns the index at which the message body is expected to start. If you
just care about the headers, you can ignore the second component of the
returned tuple.
Error values are returned if there was some sort of parsing error.</dd><dt><a class="fn" href="fn.parse_mail.html" title="fn mailparse::parse_mail">parse_<wbr>mail</a></dt><dd>The main mail-parsing entry point.
This function takes the raw data making up the message body and returns a
structured version of it, which allows easily accessing the header and body
information as needed.</dd></dl></section></div></main></div></body></html>