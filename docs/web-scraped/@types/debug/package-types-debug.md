# Source: https://www.npmjs.com/package/@types/debug

Title: @types/debug

URL Source: https://www.npmjs.com/package/@types/debug

Markdown Content:
4.1.12•Public•Published 2 years ago

* [Readme](https://www.npmjs.com/package/@types/debug?activeTab=readme)
* [Code Beta](https://www.npmjs.com/package/@types/debug?activeTab=code)
* [1 Dependency](https://www.npmjs.com/package/@types/debug?activeTab=dependencies)
* [1475 Dependents](https://www.npmjs.com/package/@types/debug?activeTab=dependents)
* [26 Versions](https://www.npmjs.com/package/@types/debug?activeTab=versions)

> `npm install --save @types/debug`

This package contains type definitions for debug ([https://github.com/debug-js/debug](https://github.com/debug-js/debug)).

Files were exported from [https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/debug).

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

* Last updated: Thu, 09 Nov 2023 03:06:57 GMT
* Dependencies: [@types/ms](https://npmjs.com/package/@types/ms)

These definitions were written by [Seon-Wook Park](https://github.com/swook), [Gal Talmor](https://github.com/galtalmor), [John McLaughlin](https://github.com/zamb3zi), [Brasten Sager](https://github.com/brasten), [Nicolas Penin](https://github.com/npenin), [Kristian Brünn](https://github.com/kristianmitk), and [Caleb Gregory](https://github.com/calebgregory).

Readme
------

### Keywords

none
