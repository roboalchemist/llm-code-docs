# Source: https://www.npmjs.com/package/@types/debug?activeTab=dependents

Title: @types/debug

URL Source: https://www.npmjs.com/package/@types/debug?activeTab=dependents

Markdown Content:
@types/debug - npm
===============

skip to:[content](https://www.npmjs.com/package/@types/debug?activeTab=dependents#main)[package search](https://www.npmjs.com/package/@types/debug?activeTab=dependents#search)[sign in](https://www.npmjs.com/package/@types/debug?activeTab=dependents#signin)

❤

* [Pro](https://www.npmjs.com/products/pro)
* [Teams](https://www.npmjs.com/products/teams)
* [Pricing](https://www.npmjs.com/products)
* [Documentation](https://docs.npmjs.com/)

npm

[](https://www.npmjs.com/)

Search

[Sign Up](https://www.npmjs.com/signup)[Sign In](https://www.npmjs.com/login)

@types/debug

![Image 1: TypeScript icon, indicating that this package has built-in type declarations](https://static-production.npmjs.com/4a2a680dfcadf231172b78b1d3beb975.svg)
================================================================================================================================================================================

4.1.12•Public•Published 2 years ago

* [Readme](https://www.npmjs.com/package/@types/debug?activeTab=readme)
* [Code Beta](https://www.npmjs.com/package/@types/debug?activeTab=code)
* [1 Dependency](https://www.npmjs.com/package/@types/debug?activeTab=dependencies)
* [1475 Dependents](https://www.npmjs.com/package/@types/debug?activeTab=dependents)
* [26 Versions](https://www.npmjs.com/package/@types/debug?activeTab=versions)

Installation
============

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#installation)

> `npm install --save @types/debug`

Summary
=======

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#summary)

This package contains type definitions for debug ([https://github.com/debug-js/debug](https://github.com/debug-js/debug)).

Details
=======

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#details)

Files were exported from [https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug).

[index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug/index.d.ts)
---------------------------------------------------------------------------------------------------

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#indexdts)

undefinedts
declare var debug: debug.Debug & { debug: debug.Debug; default: debug.Debug };

export = debug;
export as namespace debug;

declare namespace debug {
    interface Debug {
        (namespace: string): Debugger;
        coerce: (val: any) => any;
        disable: () => string;
        enable: (namespaces: string) => void;
        enabled: (namespaces: string) => boolean;
        formatArgs: (this: Debugger, args: any[]) => void;
        log: (...args: any[]) => any;
        selectColor: (namespace: string) => string | number;
        humanize: typeof import("ms");

        names: RegExp[];
        skips: RegExp[];

        formatters: Formatters;

        inspectOpts?: {
            hideDate?: boolean | number | null;
            colors?: boolean | number | null;
            depth?: boolean | number | null;
            showHidden?: boolean | number | null;
        };
    }

    type IDebug = Debug;

    interface Formatters {
        [formatter: string]: (v: any) => string;
    }

    type IDebugger = Debugger;

    interface Debugger {
        (formatter: any, ...args: any[]): void;

        color: string;
        diff: number;
        enabled: boolean;
        log: (...args: any[]) => any;
        namespace: string;
        destroy: () => boolean;
        extend: (namespace: string, delimiter?: string) => Debugger;
    }
}
undefined

### Additional Details

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#additional-details)

* Last updated: Thu, 09 Nov 2023 03:06:57 GMT
* Dependencies: [@types/ms](https://npmjs.com/package/@types/ms)

Credits
=======

[](https://www.npmjs.com/package/@types/debug?activeTab=dependents#credits)

These definitions were written by [Seon-Wook Park](https://github.com/swook), [Gal Talmor](https://github.com/galtalmor), [John McLaughlin](https://github.com/zamb3zi), [Brasten Sager](https://github.com/brasten), [Nicolas Penin](https://github.com/npenin), [Kristian Brünn](https://github.com/kristianmitk), and [Caleb Gregory](https://github.com/calebgregory).

Dependents [(1475)](https://www.npmjs.com/browse/depended/@types/debug)
-----------------------------------------------------------------------

* [@iflow-mcp/agentrpc-agentrpc](https://www.npmjs.com/package/%40iflow-mcp%2Fagentrpc-agentrpc)
* [@aigne/model-base](https://www.npmjs.com/package/%40aigne%2Fmodel-base)
* [vobiz-jssip](https://www.npmjs.com/package/vobiz-jssip)
* [@waynevanson/vite-plugin-cargo](https://www.npmjs.com/package/%40waynevanson%2Fvite-plugin-cargo)
* [@md-oss/cache](https://www.npmjs.com/package/%40md-oss%2Fcache)
* [@md-oss/api-types](https://www.npmjs.com/package/%40md-oss%2Fapi-types)
* [@selie/puppeteer-extra](https://www.npmjs.com/package/%40selie%2Fpuppeteer-extra)
* [@selie/puppeteer-extra-plugin](https://www.npmjs.com/package/%40selie%2Fpuppeteer-extra-plugin)
* [@zorilla/puppeteer-extra-plugin](https://www.npmjs.com/package/%40zorilla%2Fpuppeteer-extra-plugin)
* [@zorilla/puppeteer-extra](https://www.npmjs.com/package/%40zorilla%2Fpuppeteer-extra)
* [p2p-cdn-live26-core](https://www.npmjs.com/package/p2p-cdn-live26-core)
* [p2p-cdn-lives-core](https://www.npmjs.com/package/p2p-cdn-lives-core)
* [ctap-beta](https://www.npmjs.com/package/ctap-beta)
* [bun-sfe-autoupdater](https://www.npmjs.com/package/bun-sfe-autoupdater)
* [@vcacanada/sequelize](https://www.npmjs.com/package/%40vcacanada%2Fsequelize)
* [@inkandswitch/patchwork-plugins](https://www.npmjs.com/package/%40inkandswitch%2Fpatchwork-plugins)
* [@inkandswitch/patchwork-filesystem](https://www.npmjs.com/package/%40inkandswitch%2Fpatchwork-filesystem)
* [@inkandswitch/patchwork-bootloader](https://www.npmjs.com/package/%40inkandswitch%2Fpatchwork-bootloader)
* [xc-render-server](https://www.npmjs.com/package/xc-render-server)
* [@iflow-mcp/figma-mcp-server](https://www.npmjs.com/package/%40iflow-mcp%2Ffigma-mcp-server)
* [@mcp-rag/client](https://www.npmjs.com/package/%40mcp-rag%2Fclient)
* [@mcp-rag/neo4j](https://www.npmjs.com/package/%40mcp-rag%2Fneo4j)
* [@rechakra/cli](https://www.npmjs.com/package/%40rechakra%2Fcli)
* [@gaios/plugins](https://www.npmjs.com/package/%40gaios%2Fplugins)
* [@gaios/filesystem](https://www.npmjs.com/package/%40gaios%2Ffilesystem)
* [@hcl-software/enchanted-web-components](https://www.npmjs.com/package/%40hcl-software%2Fenchanted-web-components)
* [@hcl-software/enchanted-icons-web-component](https://www.npmjs.com/package/%40hcl-software%2Fenchanted-icons-web-component)
* [@nxtmd/core](https://www.npmjs.com/package/%40nxtmd%2Fcore)
* [@nxtmd/sequelizeturso](https://www.npmjs.com/package/%40nxtmd%2Fsequelizeturso)
* [@nxtmd/sequelize-turso](https://www.npmjs.com/package/%40nxtmd%2Fsequelize-turso)
* [@woom-cache/core](https://www.npmjs.com/package/%40woom-cache%2Fcore)
* [@maths22/irc](https://www.npmjs.com/package/%40maths22%2Firc)
* [jssip-subscribe-fork](https://www.npmjs.com/package/jssip-subscribe-fork)
* [suplus-jssip](https://www.npmjs.com/package/suplus-jssip)
* [@cannypack-oss/sequelize](https://www.npmjs.com/package/%40cannypack-oss%2Fsequelize)
* [@cmdoss/file-manager](https://www.npmjs.com/package/%40cmdoss%2Ffile-manager)
* [@signageos/redis](https://www.npmjs.com/package/%40signageos%2Fredis)
* [@iamevan/builder-util](https://www.npmjs.com/package/%40iamevan%2Fbuilder-util)
* [@phystack/qr-run-react](https://www.npmjs.com/package/%40phystack%2Fqr-run-react)
* [@global-cache/core](https://www.npmjs.com/package/%40global-cache%2Fcore)
* [@mewtant/admob-ssv](https://www.npmjs.com/package/%40mewtant%2Fadmob-ssv)
* [@grampelberg/spotcheck](https://www.npmjs.com/package/%40grampelberg%2Fspotcheck)
* [@sie-js/sie-tool](https://www.npmjs.com/package/%40sie-js%2Fsie-tool)
* [@e0ipso/drupal-bridge-mcp](https://www.npmjs.com/package/%40e0ipso%2Fdrupal-bridge-mcp)
* [@novartc/jssip](https://www.npmjs.com/package/%40novartc%2Fjssip)
* [@loongdotjs/builder-util](https://www.npmjs.com/package/%40loongdotjs%2Fbuilder-util)
* [@regraf/i18n](https://www.npmjs.com/package/%40regraf%2Fi18n)
* [@alanlin-powered/builder-util](https://www.npmjs.com/package/%40alanlin-powered%2Fbuilder-util)
* [@durrtagnan/mediasoup-client](https://www.npmjs.com/package/%40durrtagnan%2Fmediasoup-client)
* [@jerfowler/agent-comm-mcp-server](https://www.npmjs.com/package/%40jerfowler%2Fagent-comm-mcp-server)
* [and more...](https://www.npmjs.com/browse/depended/@types/debug)

Package Sidebar
---------------

### Install

`npm i @types/debug`

### Repository

[github.com/DefinitelyTyped/DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)

### Homepage

[github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug)

### Weekly Downloads

30,575,520

### Version

4.1.12

### License

MIT

### Unpacked Size

6.45 kB

### Total Files

5

### Last publish

2 years ago

### Collaborators

* [![Image 2: types](https://www.npmjs.com/npm-avatar/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJVUkwiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci8zZTJiMzQyNjE2ODIyZjhlYWJjOWRkMzkzODQwZGI0YT9zaXplPTEwMCZkZWZhdWx0PXJldHJvIn0.EUOa_GBepJl2c81YEIz3BI_m3t-HTZSrDib9X7tvWjo)](https://www.npmjs.com/~types) types

[**Analyze security** with Socket](https://socket.dev/npm/package/%40types%2Fdebug)[**Check bundle size**](https://bundlephobia.com/package/%40types%2Fdebug)[**View package health**](https://snyk.io/advisor/npm-package/%40types%2Fdebug)[**Explore dependencies**](https://npmgraph.js.org/?q=%40types%2Fdebug)

[**Report** malware](https://www.npmjs.com/support?inquire=security&security-inquire=malware&package=%40types%2Fdebug&version=4.1.12)

Footer
------

[](https://github.com/npm)

[](https://github.com/)

### Support

* [Help](https://docs.npmjs.com/)
* [Advisories](https://github.com/advisories)
* [Status](http://status.npmjs.org/)
* [Contact npm](https://www.npmjs.com/support)

### Company

* [About](https://www.npmjs.com/about)
* [Blog](https://github.blog/tag/npm/)
* [Press](https://www.npmjs.com/press)

### Terms & Policies

* [Policies](https://www.npmjs.com/policies/)
* [Terms of Use](https://www.npmjs.com/policies/terms)
* [Code of Conduct](https://www.npmjs.com/policies/conduct)
* [Privacy](https://www.npmjs.com/policies/privacy)
