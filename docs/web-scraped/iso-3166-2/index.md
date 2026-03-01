# Source: https://iso3166-2.readthedocs.io/

Title: Welcome to ISO 3166-2’s documentation 🌎! — iso3166-2 1.5.2 documentation

URL Source: https://iso3166-2.readthedocs.io/

Markdown Content:
[![Image 1: iso3166_2](https://img.shields.io/pypi/v/iso3166-2)](https://pypi.org/project/iso3166-2/)[![Image 2: pytest](https://github.com/amckenna41/iso3166-2/workflows/Building%20and%20Testing/badge.svg)](https://github.com/amckenna41/iso3166-2/actions?query=workflow:Building%20and%20Testing)[![Image 3: License: MIT](https://img.shields.io/github/license/amckenna41/iso3166-2)](https://opensource.org/licenses/MIT)[![Image 4: codecov](https://codecov.io/gh/amckenna41/iso3166-2/branch/main/graph/badge.svg)](https://codecov.io/gh/amckenna41/iso3166-2)![Image 5: https://upload.wikimedia.org/wikipedia/commons/3/3d/Flag-map_of_the_world_%282017%29.png](https://upload.wikimedia.org/wikipedia/commons/3/3d/Flag-map_of_the_world_%282017%29.png)
Introduction[](https://iso3166-2.readthedocs.io/#introduction "Link to this heading")
--------------------------------------------------------------------------------------

**iso3166-2** is a lightweight custom-built Python package, and accompanying RESTfulAPI, that can be used to access all of the world’s ISO 3166-2 subdivision data. Here, subdivision can be used interchangeably with regions/states/provinces etc. Currently, the package and API supports data from **250** countries/territories, according to the ISO 3166-1 standard. The software uses another custom-built Python package called [iso3166-updates](https://github.com/amckenna41/iso3166-updates) to ensure all the subdivision data is **accurate, reliable and up-to-date**. The ISO 3166-2 was first published in 1998 and as of December 2025 there are **5,046** codes defined in it.

The ISO 3166-2 standard is part of the broader ISO 3166 family, maintained by the International Organization for Standardization (ISO). It provides codes for the names of the principal subdivisions (e.g., provinces or states) of all countries that have codes defined in ISO 3166-1. These codes are widely used in geopolitics, logistics, statistics, and software systems for consistent country and region identification.

There are 7 main data attributes available for each subdivision/subdivision code within the **iso3166-2** software:

*   **Name** - subdivision name, as it is commonly known in English

*   **Local/other name** - subdivision name in local language or any alternative names its known by

*   **Latitude/Longitude** - subdivision coordinates

*   **Flag** - subdivision flag from the custom-built [iso3166-flags](https://github.com/amckenna41/iso3166-flags) repo

*   **Parent Code** - subdivision’s parent code

*   **Type** - subdivision type, e.g. region, state, canton, parish etc

*   **History** - historical updates/changes to the subdivision and its data, from the custom-built [iso3166-updates](https://github.com/amckenna41/iso3166-updates) repo

Bespoke Features[](https://iso3166-2.readthedocs.io/#bespoke-features "Link to this heading")
----------------------------------------------------------------------------------------------

There are three main attributes supported by the software that make it stand out and add a significant amount of value and data per subdivision, in comparison to some the other iso3166-2 datasets, these are the **local/other name**, **flag** and **history** attributes.

### Local/other name[](https://iso3166-2.readthedocs.io/#local-other-name "Link to this heading")

The `localOtherName` attribute is built from a custom dataset of local language variants and alternative names/nicknames for the **over 5000** subdivisions. In total there are **>3700** local/other names for the **>5000** subdivisions. Primarily the attribute contains local language translations for the subdivisions related to the subdivision, but many also include **nicknames** and **other variants** that the subdivision may be known by, either locally or globally.

For each local/other name, the **ISO 639** 3 letter language code is used to identify the language of the name. Some translations do not have available ISO 639 codes, therefore the [Glottolog](https://glottolog.org/) or other databases (e.g [IETF](https://support.elucidat.com/hc/en-us/articles/6068623875217-IETF-language-tags)) language codes are used. Some example local/other name entries are:

*   **Sindh (Pakistan PK-SD)** - “سِنْدھ (urd), Sindh (eng), SD (eng), Mehran/Gateway (eng), Bab-ul-Islam/Gateway of Islam (eng)”

*   **Central Singapore (Singapore SG-01)** - “Pusat Singapura (msa), 新加坡中部 (zho), மத்திய சிங்கப்பூர் (tam)”

*   **Bobonaro (East Timor TL-BO)** - “Bobonaru (tet), Buburnaru (tet), Tall eucalypt (eng)”

*   **Wyoming (USA US-WY)** - “Equality State (eng), Cowboy State (eng), Big Wyoming (eng)”

The full dataset of local/other names is available in the repo here [local_other_names.csv](https://github.com/amckenna41/iso3166-2/iso3166_2_resources/local_other_names.csv).

### Flags[](https://iso3166-2.readthedocs.io/#flags "Link to this heading")

The other equally important and bespoke/unique attribute that the software package supports is the `flag` attribute, which is a link to the subdivision’s flag on the [iso3166-flags](https://github.com/amckenna41/iso3166-flags) repo. This is another **custom-built** repository, (alongside [iso3166-2](https://github.com/amckenna41/iso3166-2) and [iso3166-updates](https://github.com/amckenna41/iso3166-updates)) that stores a rich and comprehensive dataset of over **2800** official individual subdivision flags, alongside ~250 ISO 3166-1 country/territory flags.

The flags repo uses the [iso3166-2](https://github.com/amckenna41/iso3166-2) software to get the full list of ISO 3166-2 subdivision codes which is kept up-to-date and accurate via the [iso3166-updates](https://github.com/amckenna41/iso3166-updates) software.

❤️ iso3166-2 🤝 iso3166-updates 🤝 iso3166-flags ❤️

### History[](https://iso3166-2.readthedocs.io/#history "Link to this heading")

The `history` attribute has any applicable historical updates/changes to the individual subdivisions. The data source for this is another custom-built software package previously mentioned called [iso3166-updates](https://github.com/amckenna41/iso3166-updates). This package keeps track of all the published changes that the ISO make to the ISO 3166 standard which include addition of new subdivisions, deletion of existing subdivisions or amendments to existing subdivisions. Thus [iso3166-updates](https://github.com/amckenna41/iso3166-updates) helps ensure that the data in the iso3166-2 package is also kept **up-to-date** and **accurate**. If any updates are found for the subdivision a short description of the change, it’s publication date as well as its source will be included.

❤️ iso3166-2 🤝 iso3166-updates ❤️

Upcoming Features[](https://iso3166-2.readthedocs.io/#upcoming-features "Link to this heading")
------------------------------------------------------------------------------------------------

There are several new features and attributes that are currently being worked on and will be added to the software package in the near future. These include: * **Demographics** - addition of key demographic data attributes such as area, population, population density etc for each subdivision * **Enhanced Geo Data** - addition of more detailed geo data attributes such as bounding box and geojson (these attributes are exportable via the custom scripts but yet to be implemented into the dataset)

Version[](https://iso3166-2.readthedocs.io/#version "Link to this heading")
----------------------------------------------------------------------------

The **iso3166-2** software is currently at version [v1.8.2](https://pypi.org/project/iso3166-2/).

Last Updated[](https://iso3166-2.readthedocs.io/#last-updated "Link to this heading")
--------------------------------------------------------------------------------------

The ISO 3166-2 data was last updated on **June 2025**. A log of the latest ISO 3166-2 updates can be seen in the [UPDATES.md](https://github.com/amckenna41/iso3166-2/blob/main/UPDATES.MD) file in the repository.

License[](https://iso3166-2.readthedocs.io/#license "Link to this heading")
----------------------------------------------------------------------------

**iso3166-2** is distributed under the [MIT](https://github.com/amckenna41/iso3166-2/blob/main/LICENSE) license.

Contributing[](https://iso3166-2.readthedocs.io/#contributing "Link to this heading")
--------------------------------------------------------------------------------------

If you have found a bug or an issue in the software or API then please raise an issue on the repository’s [Issues](https://github.com/amckenna41/iso3166-2/issues/) tab.

If you would like to contribute any functional/feature changes to the software, please make a pull request on the [repository](https://github.com/amckenna41/iso3166-2/).

Any other queries or issues, please contact me via email: [amckenna41@qub.ac.uk](mailto:amckenna41%40qub.ac.uk).

Credits[](https://iso3166-2.readthedocs.io/#credits "Link to this heading")
----------------------------------------------------------------------------

The Python software and accompanying API are solely developed and maintained by [me](https://github.com/amckenna41) 😁.

Note

A demo of the software and accompanying API is available [here](https://colab.research.google.com/drive/1btfEx23bgWdkUPiwdwlDqKkmUp1S-_7U?usp=sharing)!

A Medium article about the **iso3166-2** software and API is available [here](https://ajmckenna69.medium.com/iso3166-2-71a13d9157f7)!

Contents[](https://iso3166-2.readthedocs.io/#contents "Link to this heading")
------------------------------------------------------------------------------

*   [Usage](https://iso3166-2.readthedocs.io/en/latest/usage.html)
    *   [Installation](https://iso3166-2.readthedocs.io/en/latest/usage.html#installation)
    *   [Get all subdivision data for all countries](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-all-subdivision-data-for-all-countries)
    *   [Get all subdivision data for a country using its ISO 3166-1 alpha codes](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-all-subdivision-data-for-a-country-using-its-iso-3166-1-alpha-codes)
    *   [Get list of all subdivision codes](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-list-of-all-subdivision-codes)
    *   [Get list of all subdivision names](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-list-of-all-subdivision-names)
    *   [Searching for a subdivision](https://iso3166-2.readthedocs.io/en/latest/usage.html#searching-for-a-subdivision)
    *   [Adding custom subdivisions](https://iso3166-2.readthedocs.io/en/latest/usage.html#adding-custom-subdivisions)
    *   [Get all subdivision data but with subset of available attributes](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-all-subdivision-data-but-with-subset-of-available-attributes)
    *   [Get the total number of subdivision objects](https://iso3166-2.readthedocs.io/en/latest/usage.html#get-the-total-number-of-subdivision-objects)
    *   [Remove attributes from subdivision data](https://iso3166-2.readthedocs.io/en/latest/usage.html#remove-attributes-from-subdivision-data)
    *   [Check for the latest Subdivision data](https://iso3166-2.readthedocs.io/en/latest/usage.html#check-for-the-latest-subdivision-data)

*   [API](https://iso3166-2.readthedocs.io/en/latest/api.html)
    *   [Query String Parameters](https://iso3166-2.readthedocs.io/en/latest/api.html#query-string-parameters)
    *   [Get subdivision data for ALL countries](https://iso3166-2.readthedocs.io/en/latest/api.html#get-subdivision-data-for-all-countries)
    *   [Get subdivision data per country, using its ISO 3166-1 alpha code (alpha-2, alpha-3, numeric)](https://iso3166-2.readthedocs.io/en/latest/api.html#get-subdivision-data-per-country-using-its-iso-3166-1-alpha-code-alpha-2-alpha-3-numeric)
    *   [Get all subdivision data for a specific subdivision, using its subdivision code](https://iso3166-2.readthedocs.io/en/latest/api.html#get-all-subdivision-data-for-a-specific-subdivision-using-its-subdivision-code)
    *   [Get all subdivision data for a specific country, using its name](https://iso3166-2.readthedocs.io/en/latest/api.html#get-all-subdivision-data-for-a-specific-country-using-its-name)
    *   [Search for a specific subdivision, using its subdivision name or local/other names](https://iso3166-2.readthedocs.io/en/latest/api.html#search-for-a-specific-subdivision-using-its-subdivision-name-or-local-other-names)
    *   [Search for subdivision geography](https://iso3166-2.readthedocs.io/en/latest/api.html#search-for-subdivision-geography)
    *   [Get list of all subdivision codes per country](https://iso3166-2.readthedocs.io/en/latest/api.html#get-list-of-all-subdivision-codes-per-country)

*   [Changelog](https://iso3166-2.readthedocs.io/en/latest/changelog.html)
    *   [v1.8.1/v.1.8.2 - February 2026](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-8-1-v-1-8-2-february-2026)
    *   [v1.8.0 - September 2025](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-8-0-september-2025)
    *   [v1.7.0 - 1.7.2 - July 2025](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-7-0-1-7-2-july-2025)
    *   [v1.6.1 - June 2024](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-6-1-june-2024)
    *   [v1.6.0 - June 2024](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-6-0-june-2024)
    *   [v1.5.4 - March 2024](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-5-4-march-2024)
    *   [v1.4.0 - December 2023](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-4-0-december-2023)
    *   [v1.3.0 - December 2023](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-3-0-december-2023)
    *   [v1.2.0 and earlier](https://iso3166-2.readthedocs.io/en/latest/changelog.html#v1-2-0-and-earlier)

[Back to top ↑](https://iso3166-2.readthedocs.io/#welcome-to-iso-3166-2-s-documentation)
