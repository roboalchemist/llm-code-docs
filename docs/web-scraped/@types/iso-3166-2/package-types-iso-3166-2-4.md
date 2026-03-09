# Source: https://www.npmjs.com/package/@types/iso-3166-2?activeTab=dependents

Title: @types/iso-3166-2

URL Source: https://www.npmjs.com/package/@types/iso-3166-2?activeTab=dependents

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

Dependents [(4)](https://www.npmjs.com/browse/depended/@types/iso-3166-2)
-------------------------------------------------------------------------

* [@regen-network/web-components](https://www.npmjs.com/package/%40regen-network%2Fweb-components)
* [@joystream/metadata-protobuf](https://www.npmjs.com/package/%40joystream%2Fmetadata-protobuf)
* [and more...](https://www.npmjs.com/browse/depended/@types/iso-3166-2)
