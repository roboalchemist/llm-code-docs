# Source: https://www.npmjs.com/package/@types/jest-axe?activeTab=dependents

Title: @types/jest-axe

URL Source: https://www.npmjs.com/package/@types/jest-axe?activeTab=dependents

Markdown Content:
3.5.9•Public•Published 2 years ago

* [Readme](https://www.npmjs.com/package/@types/jest-axe?activeTab=readme)
* [Code Beta](https://www.npmjs.com/package/@types/jest-axe?activeTab=code)
* [2 Dependencies](https://www.npmjs.com/package/@types/jest-axe?activeTab=dependencies)
* [36 Dependents](https://www.npmjs.com/package/@types/jest-axe?activeTab=dependents)
* [18 Versions](https://www.npmjs.com/package/@types/jest-axe?activeTab=versions)

Installation
------------

> `npm install --save @types/jest-axe`

Summary
-------

This package contains type definitions for jest-axe ([https://github.com/nickcolley/jest-axe](https://github.com/nickcolley/jest-axe)).

Details
-------

Files were exported from [https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest-axe](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest-axe).

[index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jest-axe/index.d.ts)
------------------------------------------------------------------------------------------------------

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

### Additional Details

* Last updated: Mon, 27 Nov 2023 11:35:43 GMT
* Dependencies: [@types/jest](https://npmjs.com/package/@types/jest), [axe-core](https://npmjs.com/package/axe-core)

Credits
-------

These definitions were written by [erbridge](https://github.com/erbridge).

Dependents [(36)](https://www.npmjs.com/browse/depended/@types/jest-axe)
------------------------------------------------------------------------

* [@traefik-labs/faency](https://www.npmjs.com/package/%40traefik-labs%2Ffaency)
* [@orchard9ai/testing-utils](https://www.npmjs.com/package/%40orchard9ai%2Ftesting-utils)
* [@baic/yolk-test](https://www.npmjs.com/package/%40baic%2Fyolk-test)
* [voluptatesporro](https://www.npmjs.com/package/voluptatesporro)
* [@compositive/testing](https://www.npmjs.com/package/%40compositive%2Ftesting)
* [@lg-tools/test](https://www.npmjs.com/package/%40lg-tools%2Ftest)
* [pers-tsc-gen](https://www.npmjs.com/package/pers-tsc-gen)
* [@project44-manifest/react-test-utils](https://www.npmjs.com/package/%40project44-manifest%2Freact-test-utils)
* [@project44-manifest/test-utils](https://www.npmjs.com/package/%40project44-manifest%2Ftest-utils)
* [@natsuo/test-utils](https://www.npmjs.com/package/%40natsuo%2Ftest-utils)
* [bohe-ui](https://www.npmjs.com/package/bohe-ui)
* [wdxantd](https://www.npmjs.com/package/wdxantd)
* [vitau](https://www.npmjs.com/package/vitau)
* [@easyfeedback/test-utils](https://www.npmjs.com/package/%40easyfeedback%2Ftest-utils)
* [@knkui/scripts](https://www.npmjs.com/package/%40knkui%2Fscripts)
* [@traefiklabs/faency](https://www.npmjs.com/package/%40traefiklabs%2Ffaency)
* [@nature-ui/test-utils](https://www.npmjs.com/package/%40nature-ui%2Ftest-utils)
* [@hazelcast/test-helpers](https://www.npmjs.com/package/%40hazelcast%2Ftest-helpers)
* [@hd-toolkit/jest-config-react](https://www.npmjs.com/package/%40hd-toolkit%2Fjest-config-react)
* [@rakoon-badshah/my-newaxe](https://www.npmjs.com/package/%40rakoon-badshah%2Fmy-newaxe)
* [@rakoon-badshah/my-axe](https://www.npmjs.com/package/%40rakoon-badshah%2Fmy-axe)
* [brainly-style-guide](https://www.npmjs.com/package/brainly-style-guide)
* [@fluentui/internal-tooling](https://www.npmjs.com/package/%40fluentui%2Finternal-tooling)
* [@elliemae/pui-cli](https://www.npmjs.com/package/%40elliemae%2Fpui-cli)
* [@stardust-ui/internal-tooling](https://www.npmjs.com/package/%40stardust-ui%2Finternal-tooling)
* [and more...](https://www.npmjs.com/browse/depended/@types/jest-axe)
