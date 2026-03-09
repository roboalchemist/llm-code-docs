# Source: https://www.npmjs.com/package/@types/jest-axe?activeTab=versions

Title: @types/jest-axe

URL Source: https://www.npmjs.com/package/@types/jest-axe?activeTab=versions

Markdown Content:
3.5.9•Public•Published 2 years ago

* [Readme](https://www.npmjs.com/package/@types/jest-axe?activeTab=readme)
* [Code Beta](https://www.npmjs.com/package/@types/jest-axe?activeTab=code)
* [2 Dependencies](https://www.npmjs.com/package/@types/jest-axe?activeTab=dependencies)
* [36 Dependents](https://www.npmjs.com/package/@types/jest-axe?activeTab=dependents)
* [18 Versions](https://www.npmjs.com/package/@types/jest-axe?activeTab=versions)

> `npm install --save @types/jest-axe`

This package contains type definitions for jest-axe ([https://github.com/nickcolley/jest-axe](https://github.com/nickcolley/jest-axe)).

Files were exported from [https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest-axe](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest-axe).

/// <reference types="jest" />

import { AxeResults, ImpactValue, Result, RunOptions, Spec } from "axe-core";

export interface JestAxeConfigureOptions extends RunOptions {
    globalOptions?: Spec | undefined;
    impactLevels?: ImpactValue[];
}

/**

* Version of the aXe verifier with defaults set.
*
* @remarks You can still pass additional options to this new instance;
* they will be merged with the defaults.
 */
export const axe: JestAxe;

/**

* Runs aXe on HTML.
*
* @param html Raw HTML string to verify with aXe.
* @param options Options to run aXe.
* @returns Promise for the results of running aXe.
 */
export type JestAxe = (html: Element | string, options?: RunOptions) => Promise<AxeResults>;

/**

* Creates a new aXe verifier function.
*
* @param options Options to run aXe.
* @returns New aXe verifier function.
 */
export function configureAxe(options?: JestAxeConfigureOptions): JestAxe;

/**

* Results from asserting whether aXe verification passed.
 */
export interface AssertionsResult {
    /**
* Actual checked aXe verification results.
 */
    actual: Result[];

    /**
* @returns Message from the Jest assertion.
 */
    message(): string;

    /**
* Whether the assertion passed.
 */
    pass: boolean;
}

/**

* Asserts an aXe-verified result has no violations.
*
* @param results aXe verification result, if not running via expect().
* @returns Jest expectations for the aXe result.
 */
export type IToHaveNoViolations = (results?: Partial<AxeResults>) => AssertionsResult;

export const toHaveNoViolations: {
    toHaveNoViolations: IToHaveNoViolations;
};

declare global {
    namespace jest {
        interface Matchers<R, T> {
            toHaveNoViolations(): R;
        }
    }

    // axe-core depends on a global Node
    interface Node {}
}

declare module "@jest/expect" {
    interface Matchers<R extends void | Promise<void>> {
        toHaveNoViolations(): R;
    }
}

* Last updated: Mon, 27 Nov 2023 11:35:43 GMT
* Dependencies: [@types/jest](https://npmjs.com/package/@types/jest), [axe-core](https://npmjs.com/package/axe-core)

These definitions were written by [erbridge](https://github.com/erbridge).

Versions
--------

### Current Tags

| Version | Downloads (Last 7 Days) | Tag |
| --- | --- | --- |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.8 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.7 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | latest |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts4.5 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts4.6 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts4.7 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts4.8 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts4.9 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.0 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.1 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.2 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.3 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.4 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.5 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.9 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts5.6 |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | ts6.0 |
| [3.5.5](https://www.npmjs.com/package/@types/jest-axe/v/3.5.5) | 106,395 | ts4.3 |
| [3.5.5](https://www.npmjs.com/package/@types/jest-axe/v/3.5.5) | 106,395 | ts4.4 |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | ts3.8 |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | ts3.9 |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | ts4.0 |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | ts4.1 |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | ts4.2 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.1 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.2 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.3 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.4 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.5 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.6 |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | ts3.7 |
| [3.2.1](https://www.npmjs.com/package/@types/jest-axe/v/3.2.1) | 1,837 | ts3.0 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.4 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.5 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.6 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.7 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.8 |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | ts2.9 |

### Version History

| Version | Downloads (Last 7 Days) | Published |
| --- | --- | --- |
| [3.5.9](https://www.npmjs.com/package/@types/jest-axe/v/3.5.9) | 886,799 | 2 years ago |
| [3.5.8](https://www.npmjs.com/package/@types/jest-axe/v/3.5.8) | 17,238 | 2 years ago |
| [3.5.7](https://www.npmjs.com/package/@types/jest-axe/v/3.5.7) | 7,289 | 2 years ago |
| [3.5.6](https://www.npmjs.com/package/@types/jest-axe/v/3.5.6) | 3,734 | 2 years ago |
| [3.5.5](https://www.npmjs.com/package/@types/jest-axe/v/3.5.5) | 106,395 | 3 years ago |
| [3.5.4](https://www.npmjs.com/package/@types/jest-axe/v/3.5.4) | 11,062 | 4 years ago |
| [3.5.3](https://www.npmjs.com/package/@types/jest-axe/v/3.5.3) | 17,641 | 4 years ago |
| [3.5.2](https://www.npmjs.com/package/@types/jest-axe/v/3.5.2) | 11,338 | 5 years ago |
| [3.5.1](https://www.npmjs.com/package/@types/jest-axe/v/3.5.1) | 2,482 | 5 years ago |
| [3.5.0](https://www.npmjs.com/package/@types/jest-axe/v/3.5.0) | 2,318 | 6 years ago |
| [3.2.2](https://www.npmjs.com/package/@types/jest-axe/v/3.2.2) | 1,440 | 6 years ago |
| [3.2.1](https://www.npmjs.com/package/@types/jest-axe/v/3.2.1) | 1,837 | 6 years ago |
| [3.2.0](https://www.npmjs.com/package/@types/jest-axe/v/3.2.0) | 6 | 6 years ago |
| [2.2.4](https://www.npmjs.com/package/@types/jest-axe/v/2.2.4) | 37 | 7 years ago |
| [2.2.3](https://www.npmjs.com/package/@types/jest-axe/v/2.2.3) | 302 | 7 years ago |
| [2.2.2](https://www.npmjs.com/package/@types/jest-axe/v/2.2.2) | 90 | 7 years ago |
| [2.2.1](https://www.npmjs.com/package/@types/jest-axe/v/2.2.1) | 1 | 8 years ago |
| [2.2.0](https://www.npmjs.com/package/@types/jest-axe/v/2.2.0) | 1 | 8 years ago |
