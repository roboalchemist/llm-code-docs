# Source: https://www.npmjs.com/package/@types/iso-3166-2?activeTab=versions

Title: @types/iso-3166-2

URL Source: https://www.npmjs.com/package/@types/iso-3166-2?activeTab=versions

Markdown Content:
1.0.4•Public•Published 8 months ago

* [Readme](https://www.npmjs.com/package/@types/iso-3166-2?activeTab=readme)
* [Code Beta](https://www.npmjs.com/package/@types/iso-3166-2?activeTab=code)
* [0 Dependencies](https://www.npmjs.com/package/@types/iso-3166-2?activeTab=dependencies)
* [4 Dependents](https://www.npmjs.com/package/@types/iso-3166-2?activeTab=dependents)
* [6 Versions](https://www.npmjs.com/package/@types/iso-3166-2?activeTab=versions)

> `npm install --save @types/iso-3166-2`

This package contains type definitions for iso-3166-2 ([https://github.com/olahol/iso-3166-2.js](https://github.com/olahol/iso-3166-2.js)).

Files were exported from [https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/iso-3166-2](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/iso-3166-2).

export namespace CountryInfo {
    interface Partial {
        name: string;
        sub: SubdivisionInfo.Map;
    }
    interface Full extends Partial {
        code: string;
    }

    interface Map {
        // full data if this country has been retrieved with country() at least once
        [code: string]: Full | Partial;
    }
}
export type CountryInfo = CountryInfo.Full;

export namespace SubdivisionInfo {
    interface Partial {
        type: string;
        name: string;
    }
    interface Full extends Partial {
        countryName: string;
        countryCode: string;
        code: string;
        regionCode: string;
    }

    interface Map {
        // full data if this subdivision has been retrieved with subdivision() at least once
        [code: string]: Full | Partial;
    }
}
export type SubdivisionInfo = SubdivisionInfo.Full;

export function subdivision(
    countryCodeOrFullSubdivisionCode: string,
    subdivisionCodeOrName?: string,
): SubdivisionInfo | null;

export function country(countryCodeOrName: string): CountryInfo | null;

export const data: CountryInfo.Map;

// map of alpha 3 codes to alpha 2 codes
export const codes: {
    [alpha3: string]: string;
};

* Last updated: Fri, 11 Jul 2025 18:41:32 GMT
* Dependencies: none

These definitions were written by [Matt Rollins](https://github.com/sicilica), and [Emily Klassen](https://github.com/forivall).

Versions
--------

### Current Tags

| Version | Downloads (Last 7 Days) | Tag |
| --- | --- | --- |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts2.8 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts2.9 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.0 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.1 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.2 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.3 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.4 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.5 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.6 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.7 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.8 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts3.9 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts4.0 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts4.1 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts4.2 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts4.3 |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | ts4.4 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.6 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.3 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.8 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.9 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | latest |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.1 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.2 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.4 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.5 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts5.7 |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | ts6.0 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts4.5 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts4.6 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts4.7 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts4.8 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts4.9 |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | ts5.0 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.0 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.1 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.2 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.3 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.4 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.5 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.6 |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | ts2.7 |

### Version History

| Version | Downloads (Last 7 Days) | Published |
| --- | --- | --- |
| [1.0.4](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.4) | 13,453 | 8 months ago |
| [1.0.3](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.3) | 12,203 | 2 years ago |
| [1.0.2](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.2) | 2 | 2 years ago |
| [1.0.1](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.1) | 2 | 2 years ago |
| [1.0.0](https://www.npmjs.com/package/@types/iso-3166-2/v/1.0.0) | 232,790 | 6 years ago |
| [0.6.0](https://www.npmjs.com/package/@types/iso-3166-2/v/0.6.0) | 5 | 9 years ago |
