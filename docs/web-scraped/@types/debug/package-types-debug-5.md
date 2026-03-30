# Source: https://www.npmjs.com/package/@types/debug?activeTab=versions

Title: @types/debug

URL Source: https://www.npmjs.com/package/@types/debug?activeTab=versions

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

Versions
--------

### Current Tags

| Version | Downloads (Last 7 Days) | Tag |
| --- | --- | --- |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.8 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.7 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | latest |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts4.5 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts4.6 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts4.7 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts4.8 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts4.9 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.0 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.1 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.2 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.3 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.4 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.5 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.9 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts5.6 |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | ts6.0 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts3.6 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts3.7 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts3.8 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts3.9 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts4.0 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts4.1 |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | ts4.2 |
| [4.1.8](https://www.npmjs.com/package/@types/debug/v/4.1.8) | 860,120 | ts4.3 |
| [4.1.8](https://www.npmjs.com/package/@types/debug/v/4.1.8) | 860,120 | ts4.4 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.0 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.1 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.2 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.3 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.4 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.5 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.6 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.7 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.8 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts2.9 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.0 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.1 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.2 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.3 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.4 |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | ts3.5 |

### Version History

| Version | Downloads (Last 7 Days) | Published |
| --- | --- | --- |
| [4.1.12](https://www.npmjs.com/package/@types/debug/v/4.1.12) | 26,862,133 | 2 years ago |
| [4.1.11](https://www.npmjs.com/package/@types/debug/v/4.1.11) | 26,072 | 2 years ago |
| [4.1.10](https://www.npmjs.com/package/@types/debug/v/4.1.10) | 84,318 | 2 years ago |
| [4.1.9](https://www.npmjs.com/package/@types/debug/v/4.1.9) | 244,380 | 2 years ago |
| [4.1.8](https://www.npmjs.com/package/@types/debug/v/4.1.8) | 860,120 | 3 years ago |
| [4.1.7](https://www.npmjs.com/package/@types/debug/v/4.1.7) | 1,386,852 | 5 years ago |
| [4.1.6](https://www.npmjs.com/package/@types/debug/v/4.1.6) | 5,010 | 5 years ago |
| [4.1.5](https://www.npmjs.com/package/@types/debug/v/4.1.5) | 474,291 | 7 years ago |
| [4.1.4](https://www.npmjs.com/package/@types/debug/v/4.1.4) | 8,024 | 7 years ago |
| [4.1.3](https://www.npmjs.com/package/@types/debug/v/4.1.3) | 1,112 | 7 years ago |
| [4.1.2](https://www.npmjs.com/package/@types/debug/v/4.1.2) | 1,172 | 7 years ago |
| [4.1.1](https://www.npmjs.com/package/@types/debug/v/4.1.1) | 1,771 | 7 years ago |
| [4.1.0](https://www.npmjs.com/package/@types/debug/v/4.1.0) | 377 | 7 years ago |
| [0.0.31](https://www.npmjs.com/package/@types/debug/v/0.0.31) | 147,372 | 7 years ago |
| [0.0.30](https://www.npmjs.com/package/@types/debug/v/0.0.30) | 426,633 | 9 years ago |
| [0.0.29](https://www.npmjs.com/package/@types/debug/v/0.0.29) | 45,871 | 9 years ago |
| [0.0.28](https://www.npmjs.com/package/@types/debug/v/0.0.28) | 1 | 10 years ago |
| [0.0.27-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.27-alpha) | 1 | 10 years ago |
| [0.0.26-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.26-alpha) | 1 | 10 years ago |
| [0.0.25-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.25-alpha) | 1 | 10 years ago |
| [0.0.24-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.24-alpha) | 2 | 10 years ago |
| [0.0.23-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.23-alpha) | 2 | 10 years ago |
| [0.0.22-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.22-alpha) | 1 | 10 years ago |
| [0.0.21-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.21-alpha) | 1 | 10 years ago |
| [0.0.16-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.16-alpha) | 1 | 10 years ago |
| [0.0.15-alpha](https://www.npmjs.com/package/@types/debug/v/0.0.15-alpha) | 1 | 10 years ago |
