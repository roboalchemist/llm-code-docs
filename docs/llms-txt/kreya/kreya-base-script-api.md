# Source: https://kreya.app/docs/scripting-and-tests/general/kreya-base-script-api.md

# Kreya base script API reference

The following Kreya APIs are available in all Kreya scripts and Kreya operation scripts under the `kreya` namespace. These can be accessed directly through the `kreya` object:

```
kreya.trace('Hello world!');
```

## Variables[​](#variables "Direct link to Variables")

### environment[​](#environment "Direct link to environment")

```
const environment: EnvironmentContainerScriptApi;
```

[EnvironmentContainerScriptApi](#environmentcontainerscriptapi)<br /><!-- -->Gets APIs related to the Kreya environment.

***

### faker[​](#faker "Direct link to faker")

```
const faker: FakerScriptApi;
```

[FakerScriptApi](#fakerscriptapi)<br /><!-- -->The faker API to generate fake data.

***

### preview[​](#preview "Direct link to preview")

```
const preview: PreviewScriptApi;
```

[PreviewScriptApi](#previewscriptapi)<br /><!-- -->Gets APIs to preview files in Kreya.

***

### snapshot[​](#snapshot "Direct link to snapshot")

```
const snapshot: SnapshotScriptApi;
```

[SnapshotScriptApi](#snapshotscriptapi)<br /><!-- -->Gets APIs to assert snapshots.

***

### variables[​](#variables-1 "Direct link to variables")

```
const variables: UserVariablesScriptApi;
```

[UserVariablesScriptApi](#uservariablesscriptapi)<br /><!-- -->Gets the storage to set and retrieve custom variables, which are accessible in other operations and via templating.

## Functions[​](#functions "Direct link to Functions")

### sleep()[​](#sleep "Direct link to sleep()")

```
function sleep(millisecondsTimeout: number): void;
```

Sleeps for a certain length of time.

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter             | Type     | Description            |
| --------------------- | -------- | ---------------------- |
| `millisecondsTimeout` | `number` | Milliseconds to sleep. |

#### Returns[​](#returns "Direct link to Returns")

`void`

***

### test()[​](#test "Direct link to test()")

#### Call Signature[​](#call-signature "Direct link to Call Signature")

```
function test(name: string, ok: boolean): void;
```

Reports a test result.

##### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter | Type      | Description                      |
| --------- | --------- | -------------------------------- |
| `name`    | `string`  | A descriptive name of the test.  |
| `ok`      | `boolean` | Whether the test was successful. |

##### Returns[​](#returns-1 "Direct link to Returns")

`void`

#### Call Signature[​](#call-signature-1 "Direct link to Call Signature")

```
function test(name: string, callback: () => void): Promise<void>;
```

Runs a test.

##### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter  | Type         | Description                                                                      |
| ---------- | ------------ | -------------------------------------------------------------------------------- |
| `name`     | `string`     | A descriptive name of the test.                                                  |
| `callback` | () => `void` | The test code. The test is considered successful if the callback does not throw. |

##### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-2 "Direct link to Call Signature")

```
function test(name: string, callback: () => boolean): Promise<void>;
```

Runs a test.

##### Parameters[​](#parameters-3 "Direct link to Parameters")

| Parameter  | Type            | Description                                              |
| ---------- | --------------- | -------------------------------------------------------- |
| `name`     | `string`        | A descriptive name of the test.                          |
| `callback` | () => `boolean` | The test code returning whether the test was successful. |

##### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-3 "Direct link to Call Signature")

```
function test(name: string, callback: () => Promise<void>): Promise<void>;
```

Runs a test.

##### Parameters[​](#parameters-4 "Direct link to Parameters")

| Parameter  | Type                    | Description                                                                      |
| ---------- | ----------------------- | -------------------------------------------------------------------------------- |
| `name`     | `string`                | A descriptive name of the test.                                                  |
| `callback` | () => `Promise`<`void`> | The test code. The test is considered successful if the callback does not throw. |

##### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-4 "Direct link to Call Signature")

```
function test(name: string, callback: () => Promise<boolean>): Promise<void>;
```

Runs a test.

##### Parameters[​](#parameters-5 "Direct link to Parameters")

| Parameter  | Type                       | Description                                              |
| ---------- | -------------------------- | -------------------------------------------------------- |
| `name`     | `string`                   | A descriptive name of the test.                          |
| `callback` | () => `Promise`<`boolean`> | The test code returning whether the test was successful. |

##### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-5 "Direct link to Call Signature")

```
function test(name: string, callback: () => void): void;
```

Runs a test.

##### Parameters[​](#parameters-6 "Direct link to Parameters")

| Parameter  | Type         | Description                     |
| ---------- | ------------ | ------------------------------- |
| `name`     | `string`     | A descriptive name of the test. |
| `callback` | () => `void` | The test code.                  |

##### Returns[​](#returns-6 "Direct link to Returns")

`void`

***

### trace()[​](#trace "Direct link to trace()")

```
function trace(message: any): void;
```

Adds a trace message to the Kreya trace log.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

| Parameter | Type  | Description         |
| --------- | ----- | ------------------- |
| `message` | `any` | The message to log. |

#### Returns[​](#returns-7 "Direct link to Returns")

`void`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### EnvironmentContainerScriptApi[​](#environmentcontainerscriptapi "Direct link to EnvironmentContainerScriptApi")

```
type EnvironmentContainerScriptApi = {
  active: EnvironmentScriptApi;
};
```

APIs related to the Kreya environment.

#### Properties[​](#properties "Direct link to Properties")

##### active[​](#active "Direct link to active")

```
readonly active: EnvironmentScriptApi;
```

Access to the active Kreya environment.

***

### EnvironmentScriptApi[​](#environmentscriptapi "Direct link to EnvironmentScriptApi")

```
type EnvironmentScriptApi = {
  content: {
  };
  id: string;
  name: string;
};
```

APIs to access the environment.

#### Properties[​](#properties-1 "Direct link to Properties")

##### content[​](#content "Direct link to content")

```
readonly content: {
};
```

Gets the content JSON of the environment.

##### id[​](#id "Direct link to id")

```
readonly id: string;
```

Gets the unique id of the environment.

##### name[​](#name "Direct link to name")

```
readonly name: string;
```

Gets the name of the environment.

***

### FakerAddress[​](#fakeraddress "Direct link to FakerAddress")

```
type FakerAddress = {
  locale: string;
  random: FakerRandomizer;
  buildingNumber: string;
  cardinalDirection: string;
  city: string;
  cityPrefix: string;
  citySuffix: string;
  country: string;
  countryCode: string;
  county: string;
  direction: string;
  fullAddress: string;
  latitude: number;
  longitude: number;
  ordinalDirection: string;
  secondaryAddress: string;
  state: string;
  stateAbbr: string;
  streetAddress: string;
  streetName: string;
  streetSuffix: string;
  zipCode: string;
};
```

Methods for generating an address.

#### Properties[​](#properties-2 "Direct link to Properties")

##### locale[​](#locale "Direct link to locale")

```
locale: string;
```

##### random[​](#random "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods "Direct link to Methods")

##### buildingNumber()[​](#buildingnumber "Direct link to buildingNumber()")

```
buildingNumber(): string;
```

Get a building number.

###### Returns[​](#returns-8 "Direct link to Returns")

`string`

A random building number.

##### cardinalDirection()[​](#cardinaldirection "Direct link to cardinalDirection()")

```
cardinalDirection(useAbbreviation?: boolean): string;
```

Generates a cardinal direction. IE: North, South, E, W.

###### Parameters[​](#parameters-8 "Direct link to Parameters")

| Parameter          | Type      | Description                                     |
| ------------------ | --------- | ----------------------------------------------- |
| `useAbbreviation?` | `boolean` | When true, directions such as West turn into W. |

###### Returns[​](#returns-9 "Direct link to Returns")

`string`

A random cardinal direction

##### city()[​](#city "Direct link to city()")

```
city(): string;
```

Get a city name.

###### Returns[​](#returns-10 "Direct link to Returns")

`string`

A random city name.

##### cityPrefix()[​](#cityprefix "Direct link to cityPrefix()")

```
cityPrefix(): string;
```

Get a city prefix.

###### Returns[​](#returns-11 "Direct link to Returns")

`string`

A random city prefix.

##### citySuffix()[​](#citysuffix "Direct link to citySuffix()")

```
citySuffix(): string;
```

Get a city suffix.

###### Returns[​](#returns-12 "Direct link to Returns")

`string`

A random city suffix.

##### country()[​](#country "Direct link to country()")

```
country(): string;
```

Get a country.

###### Returns[​](#returns-13 "Direct link to Returns")

`string`

A random country.

##### countryCode()[​](#countrycode "Direct link to countryCode()")

```
countryCode(): string;
```

Get a random ISO 3166-1 country code.

###### Returns[​](#returns-14 "Direct link to Returns")

`string`

A random country code.

##### county()[​](#county "Direct link to county()")

```
county(): string;
```

Get a county.

###### Returns[​](#returns-15 "Direct link to Returns")

`string`

A random county.

##### direction()[​](#direction "Direct link to direction()")

```
direction(useAbbreviation?: boolean): string;
```

Generates a cardinal or ordinal direction. IE: Northwest, South, SW, E.

###### Parameters[​](#parameters-9 "Direct link to Parameters")

| Parameter          | Type      | Description                                           |
| ------------------ | --------- | ----------------------------------------------------- |
| `useAbbreviation?` | `boolean` | When true, directions such as Northwest turn into NW. |

###### Returns[​](#returns-16 "Direct link to Returns")

`string`

A random cardinal or ordinal direction.

##### fullAddress()[​](#fulladdress "Direct link to fullAddress()")

```
fullAddress(): string;
```

Get a full address like Street, City, Country.

###### Returns[​](#returns-17 "Direct link to Returns")

`string`

A random full address.

##### latitude()[​](#latitude "Direct link to latitude()")

```
latitude(min?: number, max?: number): number;
```

Get a Latitude.

###### Parameters[​](#parameters-10 "Direct link to Parameters")

| Parameter | Type     | Description        |
| --------- | -------- | ------------------ |
| `min?`    | `number` | The minimum value. |
| `max?`    | `number` | The maximum value. |

###### Returns[​](#returns-18 "Direct link to Returns")

`number`

A random latitude value.

##### longitude()[​](#longitude "Direct link to longitude()")

```
longitude(min?: number, max?: number): number;
```

Get a Longitude.

###### Parameters[​](#parameters-11 "Direct link to Parameters")

| Parameter | Type     | Description        |
| --------- | -------- | ------------------ |
| `min?`    | `number` | The minimum value. |
| `max?`    | `number` | The maximum value. |

###### Returns[​](#returns-19 "Direct link to Returns")

`number`

A random longitude value.

##### ordinalDirection()[​](#ordinaldirection "Direct link to ordinalDirection()")

```
ordinalDirection(useAbbreviation?: boolean): string;
```

Generates an ordinal direction. IE: Northwest, Southeast, SW, NE.

###### Parameters[​](#parameters-12 "Direct link to Parameters")

| Parameter          | Type      | Description                                           |
| ------------------ | --------- | ----------------------------------------------------- |
| `useAbbreviation?` | `boolean` | When true, directions such as Northwest turn into NW. |

###### Returns[​](#returns-20 "Direct link to Returns")

`string`

A random ordinal direction.

##### secondaryAddress()[​](#secondaryaddress "Direct link to secondaryAddress()")

```
secondaryAddress(): string;
```

Get a secondary address like 'Apt. 2' or 'Suite 321'.

###### Returns[​](#returns-21 "Direct link to Returns")

`string`

A random secondary address.

##### state()[​](#state "Direct link to state()")

```
state(): string;
```

Get a random state state.

###### Returns[​](#returns-22 "Direct link to Returns")

`string`

A random state.

##### stateAbbr()[​](#stateabbr "Direct link to stateAbbr()")

```
stateAbbr(): string;
```

Get a state abbreviation.

###### Returns[​](#returns-23 "Direct link to Returns")

`string`

An abbreviation for a random state.

##### streetAddress()[​](#streetaddress "Direct link to streetAddress()")

```
streetAddress(useFullAddress?: boolean): string;
```

Get a street address.

###### Parameters[​](#parameters-13 "Direct link to Parameters")

| Parameter         | Type      | Description |
| ----------------- | --------- | ----------- |
| `useFullAddress?` | `boolean` | .           |

###### Returns[​](#returns-24 "Direct link to Returns")

`string`

A random street address.

##### streetName()[​](#streetname "Direct link to streetName()")

```
streetName(): string;
```

Get a street name.

###### Returns[​](#returns-25 "Direct link to Returns")

`string`

A random street name.

##### streetSuffix()[​](#streetsuffix "Direct link to streetSuffix()")

```
streetSuffix(): string;
```

Get a street suffix.

###### Returns[​](#returns-26 "Direct link to Returns")

`string`

A random street suffix.

##### zipCode()[​](#zipcode "Direct link to zipCode()")

```
zipCode(format?: string): string;
```

Get a zipcode.

###### Parameters[​](#parameters-14 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                                       |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `format?` | `string` | If a format is provided it will fill the format with letters and numbers. Example "???? ##" can become "QYTE 78". |

###### Returns[​](#returns-27 "Direct link to Returns")

`string`

A random zipcode.

***

### FakerCommerce[​](#fakercommerce "Direct link to FakerCommerce")

```
type FakerCommerce = {
  locale: string;
  random: FakerRandomizer;
  categories: string[];
  color: string;
  department: string;
  ean13: string;
  ean8: string;
  price: string;
  product: string;
  productAdjective: string;
  productDescription: string;
  productMaterial: string;
  productName: string;
};
```

Methods relating to commerce.

#### Properties[​](#properties-3 "Direct link to Properties")

##### locale[​](#locale-1 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-1 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-1 "Direct link to Methods")

##### categories()[​](#categories "Direct link to categories()")

```
categories(num: number): string[];
```

Get random product categories.

###### Parameters[​](#parameters-15 "Direct link to Parameters")

| Parameter | Type     | Description                               |
| --------- | -------- | ----------------------------------------- |
| `num`     | `number` | The amount of categories to be generated. |

###### Returns[​](#returns-28 "Direct link to Returns")

`string`\[]

A collection of random product categories.

##### color()[​](#color "Direct link to color()")

```
color(): string;
```

Get a random color.

###### Returns[​](#returns-29 "Direct link to Returns")

`string`

A random color.

##### department()[​](#department "Direct link to department()")

```
department(max?: number, returnMax?: boolean): string;
```

Get a random commerce department.

###### Parameters[​](#parameters-16 "Direct link to Parameters")

| Parameter    | Type      | Description                                                                                                            |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| `max?`       | `number`  | The maximum amount of departments                                                                                      |
| `returnMax?` | `boolean` | If true the method returns the max amount of values, otherwise the number of categories returned is between 1 and max. |

###### Returns[​](#returns-30 "Direct link to Returns")

`string`

A random commerce department.

##### ean13()[​](#ean13 "Direct link to ean13()")

```
ean13(): string;
```

Get a random EAN-13 barcode number.

###### Returns[​](#returns-31 "Direct link to Returns")

`string`

A random EAN-13 barcode number.

##### ean8()[​](#ean8 "Direct link to ean8()")

```
ean8(): string;
```

Get a random EAN-8 barcode number.

###### Returns[​](#returns-32 "Direct link to Returns")

`string`

A random EAN-8 barcode number.

##### price()[​](#price "Direct link to price()")

```
price(
   min?: number, 
   max?: number, 
   decimals?: number, 
   symbol?: string): string;
```

Get a random product price.

###### Parameters[​](#parameters-17 "Direct link to Parameters")

| Parameter   | Type     | Description                               |
| ----------- | -------- | ----------------------------------------- |
| `min?`      | `number` | The minimum price.                        |
| `max?`      | `number` | The maximum price.                        |
| `decimals?` | `number` | How many decimals the number may include. |
| `symbol?`   | `string` | The symbol in front of the price.         |

###### Returns[​](#returns-33 "Direct link to Returns")

`string`

A randomly generated price.

##### product()[​](#product "Direct link to product()")

```
product(): string;
```

Get a random product.

###### Returns[​](#returns-34 "Direct link to Returns")

`string`

A random product.

##### productAdjective()[​](#productadjective "Direct link to productAdjective()")

```
productAdjective(): string;
```

Random product adjective.

###### Returns[​](#returns-35 "Direct link to Returns")

`string`

A random product adjective.

##### productDescription()[​](#productdescription "Direct link to productDescription()")

```
productDescription(): string;
```

Random product description.

###### Returns[​](#returns-36 "Direct link to Returns")

`string`

A random product description.

##### productMaterial()[​](#productmaterial "Direct link to productMaterial()")

```
productMaterial(): string;
```

Random product material.

###### Returns[​](#returns-37 "Direct link to Returns")

`string`

A random product material.

##### productName()[​](#productname "Direct link to productName()")

```
productName(): string;
```

Get a random product name.

###### Returns[​](#returns-38 "Direct link to Returns")

`string`

A random product name.

***

### FakerCompany[​](#fakercompany "Direct link to FakerCompany")

```
type FakerCompany = {
  locale: string;
  random: FakerRandomizer;
  bs: string;
  catchPhrase: string;
  companyName: string;
  companySuffix: string;
};
```

Generates a random company name and phrases

#### Properties[​](#properties-4 "Direct link to Properties")

##### locale[​](#locale-2 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-2 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-2 "Direct link to Methods")

##### bs()[​](#bs "Direct link to bs()")

```
bs(): string;
```

Get a company BS phrase.

###### Returns[​](#returns-39 "Direct link to Returns")

`string`

A random company BS phrase.

##### catchPhrase()[​](#catchphrase "Direct link to catchPhrase()")

```
catchPhrase(): string;
```

Get a company catch phrase.

###### Returns[​](#returns-40 "Direct link to Returns")

`string`

A random company catch phrase.

##### companyName()[​](#companyname "Direct link to companyName()")

###### Call Signature[​](#call-signature-6 "Direct link to Call Signature")

```
companyName(formatIndex?: number): string;
```

Get a company name.

###### Parameters[​](#parameters-18 "Direct link to Parameters")

| Parameter      | Type     | Description                                              |
| -------------- | -------- | -------------------------------------------------------- |
| `formatIndex?` | `number` | 0: name + suffix, 1: name-name, 2: name, name and name." |

###### Returns[​](#returns-41 "Direct link to Returns")

`string`

A random company name.

###### Call Signature[​](#call-signature-7 "Direct link to Call Signature")

```
companyName(format: string): string;
```

Get a company name. The format can use any name.\* and company.\* methods.

###### Parameters[​](#parameters-19 "Direct link to Parameters")

| Parameter | Type     | Description                                            |
| --------- | -------- | ------------------------------------------------------ |
| `format`  | `string` | Example: "{{name.lastName}} {{company.companySuffix}}" |

###### Returns[​](#returns-42 "Direct link to Returns")

`string`

A random company name in the given format.

##### companySuffix()[​](#companysuffix "Direct link to companySuffix()")

```
companySuffix(): string;
```

Get a company suffix. "Inc" and "LLC" etc.

###### Returns[​](#returns-43 "Direct link to Returns")

`string`

A random company suffix.

***

### FakerCurrency[​](#fakercurrency "Direct link to FakerCurrency")

```
type FakerCurrency = {
  code: string;
  description: string;
  symbol: string;
};
```

Represents a currency

#### Properties[​](#properties-5 "Direct link to Properties")

##### code[​](#code "Direct link to code")

```
code: string;
```

The currency code. IE: USD.

##### description[​](#description "Direct link to description")

```
description: string;
```

The long for description of the currency. IE: "US Dollar"

##### symbol[​](#symbol "Direct link to symbol")

```
symbol: string;
```

The currency symbol. IE: $

***

### FakerDatabase[​](#fakerdatabase "Direct link to FakerDatabase")

```
type FakerDatabase = {
  locale: string;
  random: FakerRandomizer;
  collation: string;
  column: string;
  engine: string;
  type: string;
};
```

Generates some random database stuff.

#### Properties[​](#properties-6 "Direct link to Properties")

##### locale[​](#locale-3 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-3 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-3 "Direct link to Methods")

##### collation()[​](#collation "Direct link to collation()")

```
collation(): string;
```

Generates a collation.

###### Returns[​](#returns-44 "Direct link to Returns")

`string`

A random collation.

##### column()[​](#column "Direct link to column()")

```
column(): string;
```

Generates a column name.

###### Returns[​](#returns-45 "Direct link to Returns")

`string`

A random column name.

##### engine()[​](#engine "Direct link to engine()")

```
engine(): string;
```

Generates a storage engine.

###### Returns[​](#returns-46 "Direct link to Returns")

`string`

A random storage engine.

##### type()[​](#type "Direct link to type()")

```
type(): string;
```

Generates a column type.

###### Returns[​](#returns-47 "Direct link to Returns")

`string`

A random column type.

***

### FakerDate[​](#fakerdate "Direct link to FakerDate")

```
type FakerDate = {
  locale: string;
  random: FakerRandomizer;
  between: Date;
  future: Date;
  month: string;
  past: Date;
  recent: Date;
  soon: Date;
  timeZoneString: string;
  weekday: string;
};
```

Methods for generating dates

#### Properties[​](#properties-7 "Direct link to Properties")

##### locale[​](#locale-4 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-4 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-4 "Direct link to Methods")

##### between()[​](#between "Direct link to between()")

```
between(start: Date, end: Date): Date;
```

Get a random `DateTime` between `start` and `end`.

###### Parameters[​](#parameters-20 "Direct link to Parameters")

| Parameter | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| `start`   | `Date` | is used from this parameter. |
| `end`     | `Date` | End time                     |

###### Returns[​](#returns-48 "Direct link to Returns")

`Date`

##### future()[​](#future "Direct link to future()")

```
future(yearsToGoForward?: number, refDate?: Date): Date;
```

Get a `DateTime` in the future between `refDate` and `yearsToGoForward`.

###### Parameters[​](#parameters-21 "Direct link to Parameters")

| Parameter           | Type     | Description          |
| ------------------- | -------- | -------------------- |
| `yearsToGoForward?` | `number` | . Default is 1 year. |
| `refDate?`          | `Date`   | .                    |

###### Returns[​](#returns-49 "Direct link to Returns")

`Date`

##### month()[​](#month "Direct link to month()")

```
month(abbreviation?: boolean, useContext?: boolean): string;
```

Get a random month.

###### Parameters[​](#parameters-22 "Direct link to Parameters")

| Parameter       | Type      | Description |
| --------------- | --------- | ----------- |
| `abbreviation?` | `boolean` |             |
| `useContext?`   | `boolean` |             |

###### Returns[​](#returns-50 "Direct link to Returns")

`string`

##### past()[​](#past "Direct link to past()")

```
past(yearsToGoBack?: number, refDate?: Date): Date;
```

Get a `DateTime` in the past between `refDate` and `yearsToGoBack`.

###### Parameters[​](#parameters-23 "Direct link to Parameters")

| Parameter        | Type     | Description          |
| ---------------- | -------- | -------------------- |
| `yearsToGoBack?` | `number` | . Default is 1 year. |
| `refDate?`       | `Date`   | .                    |

###### Returns[​](#returns-51 "Direct link to Returns")

`Date`

##### recent()[​](#recent "Direct link to recent()")

```
recent(days?: number, refDate?: Date): Date;
```

Get a random `DateTime` within the last few days.

###### Parameters[​](#parameters-24 "Direct link to Parameters")

| Parameter  | Type     | Description                |
| ---------- | -------- | -------------------------- |
| `days?`    | `number` | Number of days to go back. |
| `refDate?` | `Date`   | .                          |

###### Returns[​](#returns-52 "Direct link to Returns")

`Date`

##### soon()[​](#soon "Direct link to soon()")

```
soon(days?: number, refDate?: Date): Date;
```

Get a `DateTime` that will happen soon.

###### Parameters[​](#parameters-25 "Direct link to Parameters")

| Parameter  | Type     | Description |
| ---------- | -------- | ----------- |
| `days?`    | `number` | ahead.      |
| `refDate?` | `Date`   | .           |

###### Returns[​](#returns-53 "Direct link to Returns")

`Date`

##### timeZoneString()[​](#timezonestring "Direct link to timeZoneString()")

```
timeZoneString(): string;
```

Get a timezone string. Eg: America/Los\_Angeles

###### Returns[​](#returns-54 "Direct link to Returns")

`string`

##### weekday()[​](#weekday "Direct link to weekday()")

```
weekday(abbreviation?: boolean, useContext?: boolean): string;
```

Get a random weekday.

###### Parameters[​](#parameters-26 "Direct link to Parameters")

| Parameter       | Type      | Description |
| --------------- | --------- | ----------- |
| `abbreviation?` | `boolean` |             |
| `useContext?`   | `boolean` |             |

###### Returns[​](#returns-55 "Direct link to Returns")

`string`

***

### FakerFinance[​](#fakerfinance "Direct link to FakerFinance")

```
type FakerFinance = {
  locale: string;
  random: FakerRandomizer;
  account: string;
  accountName: string;
  amount: number;
  bic: string;
  bitcoinAddress: string;
  creditCardCvv: string;
  currency: FakerCurrency;
  ethereumAddress: string;
  iban: string;
  litecoinAddress: string;
  routingNumber: string;
  transactionType: string;
};
```

Provides financial randomness.

#### Properties[​](#properties-8 "Direct link to Properties")

##### locale[​](#locale-5 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-5 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-5 "Direct link to Methods")

##### account()[​](#account "Direct link to account()")

```
account(length?: number): string;
```

Get an account number. Default length is 8 digits.

###### Parameters[​](#parameters-27 "Direct link to Parameters")

| Parameter | Type     | Description                       |
| --------- | -------- | --------------------------------- |
| `length?` | `number` | The length of the account number. |

###### Returns[​](#returns-56 "Direct link to Returns")

`string`

##### accountName()[​](#accountname "Direct link to accountName()")

```
accountName(): string;
```

Get an account name. Like "savings", "checking", "Home Loan" etc..

###### Returns[​](#returns-57 "Direct link to Returns")

`string`

##### amount()[​](#amount "Direct link to amount()")

```
amount(
   min?: number, 
   max?: number, 
   decimals?: number): number;
```

Get a random amount. Default 0 - 1000.

###### Parameters[​](#parameters-28 "Direct link to Parameters")

| Parameter   | Type     | Description                |
| ----------- | -------- | -------------------------- |
| `min?`      | `number` | Min value. Default 0.      |
| `max?`      | `number` | Max value. Default 1000.   |
| `decimals?` | `number` | Decimal places. Default 2. |

###### Returns[​](#returns-58 "Direct link to Returns")

`number`

##### bic()[​](#bic "Direct link to bic()")

```
bic(): string;
```

Generates Bank Identifier Code (BIC) code.

###### Returns[​](#returns-59 "Direct link to Returns")

`string`

##### bitcoinAddress()[​](#bitcoinaddress "Direct link to bitcoinAddress()")

```
bitcoinAddress(): string;
```

Generates a random Bitcoin address.

###### Returns[​](#returns-60 "Direct link to Returns")

`string`

##### creditCardCvv()[​](#creditcardcvv "Direct link to creditCardCvv()")

```
creditCardCvv(): string;
```

Generate a credit card CVV.

###### Returns[​](#returns-61 "Direct link to Returns")

`string`

##### currency()[​](#currency "Direct link to currency()")

```
currency(includeFundCodes?: boolean): FakerCurrency;
```

Get a random currency.

###### Parameters[​](#parameters-29 "Direct link to Parameters")

| Parameter           | Type      | Description |
| ------------------- | --------- | ----------- |
| `includeFundCodes?` | `boolean` |             |

###### Returns[​](#returns-62 "Direct link to Returns")

[`FakerCurrency`](#fakercurrency)

##### ethereumAddress()[​](#ethereumaddress "Direct link to ethereumAddress()")

```
ethereumAddress(): string;
```

Generate a random Ethereum address.

###### Returns[​](#returns-63 "Direct link to Returns")

`string`

##### iban()[​](#iban "Direct link to iban()")

```
iban(formatted?: boolean, countryCode?: string): string;
```

Generates an International Bank Account Number (IBAN).

###### Parameters[​](#parameters-30 "Direct link to Parameters")

| Parameter      | Type      | Description                                                                                                      |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| `formatted?`   | `boolean` | Formatted IBAN containing spaces.                                                                                |
| `countryCode?` | `string`  | A two letter ISO3166 country code. Throws an exception if the country code is not found or is an invalid length. |

###### Returns[​](#returns-64 "Direct link to Returns")

`string`

##### litecoinAddress()[​](#litecoinaddress "Direct link to litecoinAddress()")

```
litecoinAddress(): string;
```

Generate a random Litecoin address.

###### Returns[​](#returns-65 "Direct link to Returns")

`string`

##### routingNumber()[​](#routingnumber "Direct link to routingNumber()")

```
routingNumber(): string;
```

Generates an ABA routing number with valid check digit.

###### Returns[​](#returns-66 "Direct link to Returns")

`string`

##### transactionType()[​](#transactiontype "Direct link to transactionType()")

```
transactionType(): string;
```

Get a transaction type: "deposit", "withdrawal", "payment", or "invoice".

###### Returns[​](#returns-67 "Direct link to Returns")

`string`

***

### FakerHacker[​](#fakerhacker "Direct link to FakerHacker")

```
type FakerHacker = {
  locale: string;
  random: FakerRandomizer;
  abbreviation: string;
  adjective: string;
  ingVerb: string;
  noun: string;
  phrase: string;
  verb: string;
};
```

Hackerish words

#### Properties[​](#properties-9 "Direct link to Properties")

##### locale[​](#locale-6 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-6 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-6 "Direct link to Methods")

##### abbreviation()[​](#abbreviation "Direct link to abbreviation()")

```
abbreviation(): string;
```

Returns an abbreviation.

###### Returns[​](#returns-68 "Direct link to Returns")

`string`

A random abbreviation.

##### adjective()[​](#adjective "Direct link to adjective()")

```
adjective(): string;
```

Returns a adjective.

###### Returns[​](#returns-69 "Direct link to Returns")

`string`

A random adjective.

##### ingVerb()[​](#ingverb "Direct link to ingVerb()")

```
ingVerb(): string;
```

Returns a verb ending with -ing.

###### Returns[​](#returns-70 "Direct link to Returns")

`string`

A random -ing verb.

##### noun()[​](#noun "Direct link to noun()")

```
noun(): string;
```

Returns a noun.

###### Returns[​](#returns-71 "Direct link to Returns")

`string`

A random noun.

##### phrase()[​](#phrase "Direct link to phrase()")

```
phrase(): string;
```

Returns a phrase.

###### Returns[​](#returns-72 "Direct link to Returns")

`string`

A random phrase.

##### verb()[​](#verb "Direct link to verb()")

```
verb(): string;
```

Returns a verb.

###### Returns[​](#returns-73 "Direct link to Returns")

`string`

A random verb.

***

### FakerImages[​](#fakerimages "Direct link to FakerImages")

```
type FakerImages = {
  locale: string;
  random: FakerRandomizer;
  dataUri: string;
  loremFlickrUrl: string;
  picsumUrl: string;
  placeholderUrl: string;
  placeImgUrl: string;
};
```

Generates images URLs.

#### Properties[​](#properties-10 "Direct link to Properties")

##### locale[​](#locale-7 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-7 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-7 "Direct link to Methods")

##### dataUri()[​](#datauri "Direct link to dataUri()")

```
dataUri(
   width: number, 
   height: number, 
   htmlColor?: string): string;
```

Get a SVG data URI image with a specific width and height.

###### Parameters[​](#parameters-31 "Direct link to Parameters")

| Parameter    | Type     | Description                                                                             |
| ------------ | -------- | --------------------------------------------------------------------------------------- |
| `width`      | `number` | Width of the image.                                                                     |
| `height`     | `number` | Height of the image.                                                                    |
| `htmlColor?` | `string` | An html color in named format 'grey', RGB format 'rgb(r,g,b)', or hex format '#888888'. |

###### Returns[​](#returns-74 "Direct link to Returns")

`string`

##### loremFlickrUrl()[​](#loremflickrurl "Direct link to loremFlickrUrl()")

```
loremFlickrUrl(
   width?: number, 
   height?: number, 
   keywords?: string, 
   grascale?: boolean, 
   matchAllKeywords?: boolean, 
   lockId?: number): string;
```

Get an image from <https://loremflickr.com> service.

###### Parameters[​](#parameters-32 "Direct link to Parameters")

| Parameter           | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `width?`            | `number`  | The image width.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `height?`           | `number`  | The image height.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `keywords?`         | `string`  | Space or comma delimited list of keywords you want the picture to contain. IE: "cat, dog" for images with cats and dogs.                                                                                                                                                                                                                                                                                                                                            |
| `grascale?`         | `boolean` | Grayscale the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `matchAllKeywords?` | `boolean` | True tries to match an image with all specified keywords. False tries to match an image with any specified keyword.                                                                                                                                                                                                                                                                                                                                                 |
| `lockId?`           | `number`  | Deterministic image id. By default, this method generates URLs with image lock ids. So, if a random seed is set, repeat runs of this method will generate the same lock id sequence for images. If you want explicit control over the lock id, you can pass it as a parameter here. Additionally, if you don't want any lock ids, pass -1 for this parameter this method will generate a URL that will result in a new random image every time the HTTP URL is hit. |

###### Returns[​](#returns-75 "Direct link to Returns")

`string`

##### picsumUrl()[​](#picsumurl "Direct link to picsumUrl()")

```
picsumUrl(
   width?: number, 
   height?: number, 
   grayscale?: boolean, 
   blur?: boolean, 
   imageId?: number): string;
```

Get an image from the <https://picsum.photos> service.

###### Parameters[​](#parameters-33 "Direct link to Parameters")

| Parameter    | Type      | Description                                                 |
| ------------ | --------- | ----------------------------------------------------------- |
| `width?`     | `number`  | Width of the image.                                         |
| `height?`    | `number`  | Height of the image.                                        |
| `grayscale?` | `boolean` | Grayscale (no color) image.                                 |
| `blur?`      | `boolean` | Blurry image.                                               |
| `imageId?`   | `number`  | Optional Image ID found here <https://picsum.photos/images> |

###### Returns[​](#returns-76 "Direct link to Returns")

`string`

##### placeholderUrl()[​](#placeholderurl "Direct link to placeholderUrl()")

```
placeholderUrl(
   width: number, 
   height: number, 
   text?: string, 
   backColor?: string, 
   textColor?: string, 
   format?: string): string;
```

Get an image from <https://placehold.co> service.

###### Parameters[​](#parameters-34 "Direct link to Parameters")

| Parameter    | Type     | Description                                                          |
| ------------ | -------- | -------------------------------------------------------------------- |
| `width`      | `number` | Width of the image.                                                  |
| `height`     | `number` | Height of the image.                                                 |
| `text?`      | `string` |                                                                      |
| `backColor?` | `string` | HTML color code for the background color.                            |
| `textColor?` | `string` | HTML color code for the foreground (text) color.                     |
| `format?`    | `string` | Image format. Supported values: 'jpg', 'jpeg', 'png', 'gif', 'webp'. |

###### Returns[​](#returns-77 "Direct link to Returns")

`string`

##### placeImgUrl()[​](#placeimgurl "Direct link to placeImgUrl()")

```
placeImgUrl(
   width?: number, 
   height?: number, 
   category?: string): string;
```

Get an image from the <https://placeimg.com> service.

###### Parameters[​](#parameters-35 "Direct link to Parameters")

| Parameter   | Type     | Description            |
| ----------- | -------- | ---------------------- |
| `width?`    | `number` | Width of the image.    |
| `height?`   | `number` | Height of the image.   |
| `category?` | `string` | for string categories. |

###### Returns[​](#returns-78 "Direct link to Returns")

`string`

***

### FakerInternet[​](#fakerinternet "Direct link to FakerInternet")

```
type FakerInternet = {
  locale: string;
  random: FakerRandomizer;
  avatar: string;
  color: string;
  domainName: string;
  domainSuffix: string;
  domainWord: string;
  email: string;
  exampleEmail: string;
  ip: string;
  ipv6: string;
  mac: string;
  password: string;
  port: number;
  protocol: string;
  url: string;
  urlRootedPath: string;
  urlWithPath: string;
  userAgent: string;
  userName: string;
  userNameUnicode: string;
};
```

Random Internet things like email addresses

#### Properties[​](#properties-11 "Direct link to Properties")

##### locale[​](#locale-8 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-8 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-8 "Direct link to Methods")

##### avatar()[​](#avatar "Direct link to avatar()")

```
avatar(ipfsGatewayRootUrl?: string): string;
```

Generates a legit Internet URL avatar from twitter accounts.

###### Parameters[​](#parameters-36 "Direct link to Parameters")

| Parameter             | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ipfsGatewayRootUrl?` | `string` | A root IPFS Gateway URL. Default is '<https://ipfs.io>'. Other examples include passing '<https://gateway.pinata.cloud>' or '<https://dweb.link>', or any other public IPFS gateway found here: <https://ipfs.github.io/public-gateway-checker/>. This parameter is used in case the default public IPFS gateway used in Bogus (<https://ipfs.io>) goes down or an alternative IPFS public or private gateway is needed. |

###### Returns[​](#returns-79 "Direct link to Returns")

`string`

A string containing a URL avatar from twitter accounts. This URL parameter should not contain any trailing '/'.

##### color()[​](#color-1 "Direct link to color()")

```
color(
   baseRed?: number, 
   baseGreen?: number, 
   baseBlue?: number, 
   grayscale?: boolean): string;
```

Gets a random aesthetically pleasing color near the base RGB. See [here](http://stackoverflow.com/questions/43044/algorithm-to-randomly-generate-an-aesthetically-pleasing-color-palette).

###### Parameters[​](#parameters-37 "Direct link to Parameters")

| Parameter    | Type      | Description               |
| ------------ | --------- | ------------------------- |
| `baseRed?`   | `number`  | Red base color            |
| `baseGreen?` | `number`  | Green base color          |
| `baseBlue?`  | `number`  | Blue base color           |
| `grayscale?` | `boolean` | Output a gray scale color |

###### Returns[​](#returns-80 "Direct link to Returns")

`string`

A random color.

##### domainName()[​](#domainname "Direct link to domainName()")

```
domainName(): string;
```

Generates a random domain name.

###### Returns[​](#returns-81 "Direct link to Returns")

`string`

A random domain name.

##### domainSuffix()[​](#domainsuffix "Direct link to domainSuffix()")

```
domainSuffix(): string;
```

Generates a domain name suffix like .com, .net, .org

###### Returns[​](#returns-82 "Direct link to Returns")

`string`

A random domain suffix.

##### domainWord()[​](#domainword "Direct link to domainWord()")

```
domainWord(): string;
```

Generates a domain word used for domain names.

###### Returns[​](#returns-83 "Direct link to Returns")

`string`

A random domain word.

##### email()[​](#email "Direct link to email()")

```
email(
   firstName?: string, 
   lastName?: string, 
   provider?: string, 
   uniqueSuffix?: string): string;
```

Generates an email address.

###### Parameters[​](#parameters-38 "Direct link to Parameters")

| Parameter       | Type     | Description                                                                                                     |
| --------------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `firstName?`    | `string` | Always use this first name.                                                                                     |
| `lastName?`     | `string` | Sometimes used depending on randomness. See 'UserName'.                                                         |
| `provider?`     | `string` | Always use the provider.                                                                                        |
| `uniqueSuffix?` | `string` | value each time before calling this method to ensure that email accounts that are generated are totally unique. |

###### Returns[​](#returns-84 "Direct link to Returns")

`string`

An email address

##### exampleEmail()[​](#exampleemail "Direct link to exampleEmail()")

```
exampleEmail(firstName?: string, lastName?: string): string;
```

Generates an example email with @example.com.

###### Parameters[​](#parameters-39 "Direct link to Parameters")

| Parameter    | Type     | Description                       |
| ------------ | -------- | --------------------------------- |
| `firstName?` | `string` | Optional: first name of the user. |
| `lastName?`  | `string` | Optional: last name of the user.  |

###### Returns[​](#returns-85 "Direct link to Returns")

`string`

An example email ending with @example.com.

##### ip()[​](#ip "Direct link to ip()")

```
ip(): string;
```

Gets a random IPv4 address string.

###### Returns[​](#returns-86 "Direct link to Returns")

`string`

A random IPv4 address.

##### ipv6()[​](#ipv6 "Direct link to ipv6()")

```
ipv6(): string;
```

Generates a random IPv6 address string.

###### Returns[​](#returns-87 "Direct link to Returns")

`string`

A random IPv6 address.

##### mac()[​](#mac "Direct link to mac()")

```
mac(separator?: string): string;
```

Gets a random mac address.

###### Parameters[​](#parameters-40 "Direct link to Parameters")

| Parameter    | Type     | Description                                          |
| ------------ | -------- | ---------------------------------------------------- |
| `separator?` | `string` | The string the mac address should be separated with. |

###### Returns[​](#returns-88 "Direct link to Returns")

`string`

A random mac address.

##### password()[​](#password "Direct link to password()")

```
password(
   length?: number, 
   memorable?: boolean, 
   regexPattern?: string, 
   prefix?: string): string;
```

Generates a random password.

###### Parameters[​](#parameters-41 "Direct link to Parameters")

| Parameter       | Type      | Description                                    |
| --------------- | --------- | ---------------------------------------------- |
| `length?`       | `number`  | Length of the password.                        |
| `memorable?`    | `boolean` | A memorable password (ie: all lower case).     |
| `regexPattern?` | `string`  | Regex pattern that the password should follow. |
| `prefix?`       | `string`  | Password prefix.                               |

###### Returns[​](#returns-89 "Direct link to Returns")

`string`

A random password.

##### port()[​](#port "Direct link to port()")

```
port(): number;
```

Generates a random port number.

###### Returns[​](#returns-90 "Direct link to Returns")

`number`

A random port number

##### protocol()[​](#protocol "Direct link to protocol()")

```
protocol(): string;
```

Returns a random protocol. HTTP or HTTPS.

###### Returns[​](#returns-91 "Direct link to Returns")

`string`

A random protocol.

##### url()[​](#url "Direct link to url()")

```
url(): string;
```

Generates a random URL.

###### Returns[​](#returns-92 "Direct link to Returns")

`string`

A random URL.

##### urlRootedPath()[​](#urlrootedpath "Direct link to urlRootedPath()")

```
urlRootedPath(fileExt?: string): string;
```

Get a rooted URL path like: /foo/bar. Optionally with file extension.

###### Parameters[​](#parameters-42 "Direct link to Parameters")

| Parameter  | Type     | Description                                       |
| ---------- | -------- | ------------------------------------------------- |
| `fileExt?` | `string` | is null, then a rooted URL directory is returned. |

###### Returns[​](#returns-93 "Direct link to Returns")

`string`

Returns a rooted URL path like: /foo/bar; optionally with a file extension.

##### urlWithPath()[​](#urlwithpath "Direct link to urlWithPath()")

```
urlWithPath(
   protocol?: string, 
   domain?: string, 
   fileExt?: string): string;
```

Get an absolute URL with random path.

###### Parameters[​](#parameters-43 "Direct link to Parameters")

| Parameter   | Type     | Description                                              |
| ----------- | -------- | -------------------------------------------------------- |
| `protocol?` | `string` | Protocol part of the URL, random if null                 |
| `domain?`   | `string` | Domain part of the URL, random if null                   |
| `fileExt?`  | `string` | The file extension to use in the path, directory if null |

###### Returns[​](#returns-94 "Direct link to Returns")

`string`

An URL with a random path.

##### userAgent()[​](#useragent "Direct link to userAgent()")

```
userAgent(): string;
```

Generates a random user agent.

###### Returns[​](#returns-95 "Direct link to Returns")

`string`

A random user agent.

##### userName()[​](#username "Direct link to userName()")

```
userName(firstName?: string, lastName?: string): string;
```

Generates user names.

###### Parameters[​](#parameters-44 "Direct link to Parameters")

| Parameter    | Type     | Description                                          |
| ------------ | -------- | ---------------------------------------------------- |
| `firstName?` | `string` | First name is always part of the returned user name. |
| `lastName?`  | `string` | Last name may or may not be used.                    |

###### Returns[​](#returns-96 "Direct link to Returns")

`string`

A random user name.

##### userNameUnicode()[​](#usernameunicode "Direct link to userNameUnicode()")

```
userNameUnicode(firstName?: string, lastName?: string): string;
```

Generates a user name preserving Unicode characters.

###### Parameters[​](#parameters-45 "Direct link to Parameters")

| Parameter    | Type     | Description                                          |
| ------------ | -------- | ---------------------------------------------------- |
| `firstName?` | `string` | First name is always part of the returned user name. |
| `lastName?`  | `string` | Last name may or may not be used.                    |

###### Returns[​](#returns-97 "Direct link to Returns")

`string`

***

### FakerLorem[​](#fakerlorem "Direct link to FakerLorem")

```
type FakerLorem = {
  locale: string;
  random: FakerRandomizer;
  letter: string;
  lines: string;
  paragraph: string;
  paragraphs: string;
  sentence: string;
  sentences: string;
  slug: string;
  text: string;
  word: string;
  words: string[];
};
```

Generates plain old boring text.

#### Properties[​](#properties-12 "Direct link to Properties")

##### locale[​](#locale-9 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-9 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-9 "Direct link to Methods")

##### letter()[​](#letter "Direct link to letter()")

```
letter(num?: number): string;
```

Get a character letter.

###### Parameters[​](#parameters-46 "Direct link to Parameters")

| Parameter | Type     | Description                         |
| --------- | -------- | ----------------------------------- |
| `num?`    | `number` | The number of characters to return. |

###### Returns[​](#returns-98 "Direct link to Returns")

`string`

##### lines()[​](#lines "Direct link to lines()")

```
lines(lineCount?: number, separator?: string): string;
```

Get lines of lorem.

###### Parameters[​](#parameters-47 "Direct link to Parameters")

| Parameter    | Type     | Description                                                |
| ------------ | -------- | ---------------------------------------------------------- |
| `lineCount?` | `number` | The amount of lines to generate. Defaults between 1 and 5. |
| `separator?` | `string` | The string to separate the lines.                          |

###### Returns[​](#returns-99 "Direct link to Returns")

`string`

##### paragraph()[​](#paragraph "Direct link to paragraph()")

```
paragraph(min?: number): string;
```

Get a paragraph.

###### Parameters[​](#parameters-48 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `min?`    | `number` | method.     |

###### Returns[​](#returns-100 "Direct link to Returns")

`string`

##### paragraphs()[​](#paragraphs "Direct link to paragraphs()")

###### Call Signature[​](#call-signature-8 "Direct link to Call Signature")

```
paragraphs(count?: number, separator?: string): string;
```

Get a specified number of paragraphs.

###### Parameters[​](#parameters-49 "Direct link to Parameters")

| Parameter    | Type     | Description                        |
| ------------ | -------- | ---------------------------------- |
| `count?`     | `number` | Number of paragraphs.              |
| `separator?` | `string` | The string to separate paragraphs. |

###### Returns[​](#returns-101 "Direct link to Returns")

`string`

###### Call Signature[​](#call-signature-9 "Direct link to Call Signature")

```
paragraphs(
   min: number, 
   max: number, 
   separator?: string): string;
```

Get a random number of paragraphs between `min` and `max`.

###### Parameters[​](#parameters-50 "Direct link to Parameters")

| Parameter    | Type     | Description                            |
| ------------ | -------- | -------------------------------------- |
| `min`        | `number` | Minimum number of paragraphs.          |
| `max`        | `number` | Maximum number of paragraphs.          |
| `separator?` | `string` | The string to separate the paragraphs. |

###### Returns[​](#returns-102 "Direct link to Returns")

`string`

##### sentence()[​](#sentence "Direct link to sentence()")

```
sentence(wordCount?: number, range?: number): string;
```

Get a random sentence of specific number of words.

###### Parameters[​](#parameters-51 "Direct link to Parameters")

| Parameter    | Type     | Description                                                                    |
| ------------ | -------- | ------------------------------------------------------------------------------ |
| `wordCount?` | `number` | Get a sentence with wordCount words. Defaults between 3 and 10.                |
| `range?`     | `number` | Add anywhere between 0 to 'range' additional words to wordCount. Default is 0. |

###### Returns[​](#returns-103 "Direct link to Returns")

`string`

##### sentences()[​](#sentences "Direct link to sentences()")

```
sentences(sentenceCount?: number, separator?: string): string;
```

Get some sentences.

###### Parameters[​](#parameters-52 "Direct link to Parameters")

| Parameter        | Type     | Description                       |
| ---------------- | -------- | --------------------------------- |
| `sentenceCount?` | `number` | The number of sentences.          |
| `separator?`     | `string` | The string to separate sentences. |

###### Returns[​](#returns-104 "Direct link to Returns")

`string`

##### slug()[​](#slug "Direct link to slug()")

```
slug(wordcount?: number): string;
```

Slugify lorem words.

###### Parameters[​](#parameters-53 "Direct link to Parameters")

| Parameter    | Type     | Description                     |
| ------------ | -------- | ------------------------------- |
| `wordcount?` | `number` | The amount of words to slugify. |

###### Returns[​](#returns-105 "Direct link to Returns")

`string`

##### text()[​](#text "Direct link to text()")

```
text(): string;
```

Get random text on a random lorem methods.

###### Returns[​](#returns-106 "Direct link to Returns")

`string`

##### word()[​](#word "Direct link to word()")

```
word(): string;
```

Get a random lorem word.

###### Returns[​](#returns-107 "Direct link to Returns")

`string`

##### words()[​](#words "Direct link to words()")

```
words(num?: number): string[];
```

Get an array of random lorem words.

###### Parameters[​](#parameters-54 "Direct link to Parameters")

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `num?`    | `number` | The number of random lorem words to return. |

###### Returns[​](#returns-108 "Direct link to Returns")

`string`\[]

***

### FakerMusic[​](#fakermusic "Direct link to FakerMusic")

```
type FakerMusic = {
  locale: string;
  random: FakerRandomizer;
  genre: string;
};
```

#### Properties[​](#properties-13 "Direct link to Properties")

##### locale[​](#locale-10 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-10 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-10 "Direct link to Methods")

##### genre()[​](#genre "Direct link to genre()")

```
genre(): string;
```

Get a music genre

###### Returns[​](#returns-109 "Direct link to Returns")

`string`

***

### FakerName[​](#fakername "Direct link to FakerName")

```
type FakerName = {
  item: FakerName;
  locale: string;
  random: FakerRandomizer;
  findName: string;
  firstName: string;
  fullName: string;
  jobArea: string;
  jobDescriptor: string;
  jobTitle: string;
  jobType: string;
  lastName: string;
  prefix: string;
  suffix: string;
};
```

Methods for generating names

#### Properties[​](#properties-14 "Direct link to Properties")

##### item[​](#item "Direct link to item")

```
readonly item: FakerName;
```

##### locale[​](#locale-11 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-11 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-11 "Direct link to Methods")

##### findName()[​](#findname "Direct link to findName()")

```
findName(
   firstName?: string, 
   lastName?: string, 
   withPrefix?: boolean, 
   withSuffix?: boolean): string;
```

Gets a full name.

###### Parameters[​](#parameters-55 "Direct link to Parameters")

| Parameter     | Type      | Description          |
| ------------- | --------- | -------------------- |
| `firstName?`  | `string`  | Use this first name. |
| `lastName?`   | `string`  | use this last name.  |
| `withPrefix?` | `boolean` | Add a prefix?        |
| `withSuffix?` | `boolean` | Add a suffix?        |

###### Returns[​](#returns-110 "Direct link to Returns")

`string`

##### firstName()[​](#firstname "Direct link to firstName()")

```
firstName(): string;
```

Get a first name. Getting a gender specific name is only supported on locales that support it.

###### Returns[​](#returns-111 "Direct link to Returns")

`string`

##### fullName()[​](#fullname "Direct link to fullName()")

```
fullName(): string;
```

Get a full name, concatenation of calling FirstName and LastName.

###### Returns[​](#returns-112 "Direct link to Returns")

`string`

##### jobArea()[​](#jobarea "Direct link to jobArea()")

```
jobArea(): string;
```

Get a job area expertise.

###### Returns[​](#returns-113 "Direct link to Returns")

`string`

##### jobDescriptor()[​](#jobdescriptor "Direct link to jobDescriptor()")

```
jobDescriptor(): string;
```

Get a job description.

###### Returns[​](#returns-114 "Direct link to Returns")

`string`

##### jobTitle()[​](#jobtitle "Direct link to jobTitle()")

```
jobTitle(): string;
```

Gets a random job title.

###### Returns[​](#returns-115 "Direct link to Returns")

`string`

##### jobType()[​](#jobtype "Direct link to jobType()")

```
jobType(): string;
```

Get a type of job.

###### Returns[​](#returns-116 "Direct link to Returns")

`string`

##### lastName()[​](#lastname "Direct link to lastName()")

```
lastName(): string;
```

Get a last name. Getting a gender specific name is only supported on locales that support it.

###### Returns[​](#returns-117 "Direct link to Returns")

`string`

##### prefix()[​](#prefix "Direct link to prefix()")

```
prefix(): string;
```

Gets a random prefix for a name.

###### Returns[​](#returns-118 "Direct link to Returns")

`string`

##### suffix()[​](#suffix "Direct link to suffix()")

```
suffix(): string;
```

Gets a random suffix for a name.

###### Returns[​](#returns-119 "Direct link to Returns")

`string`

***

### FakerPhoneNumbers[​](#fakerphonenumbers "Direct link to FakerPhoneNumbers")

```
type FakerPhoneNumbers = {
  locale: string;
  random: FakerRandomizer;
  phoneNumber: string;
  phoneNumberFormat: string;
};
```

Generates phone numbers

#### Properties[​](#properties-15 "Direct link to Properties")

##### locale[​](#locale-12 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-12 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-12 "Direct link to Methods")

##### phoneNumber()[​](#phonenumber "Direct link to phoneNumber()")

```
phoneNumber(format?: string): string;
```

Get a phone number.

###### Parameters[​](#parameters-56 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                                       |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `format?` | `string` | Format of phone number in any format. Replaces # characters with numbers. IE: '###-###-####' or '(###) ###-####'. |

###### Returns[​](#returns-120 "Direct link to Returns")

`string`

A random phone number.

##### phoneNumberFormat()[​](#phonenumberformat "Direct link to phoneNumberFormat()")

```
phoneNumberFormat(phoneFormatsArrayIndex?: number): string;
```

Gets a phone number based on the locale's phone\_number.formats\[] array index.

###### Parameters[​](#parameters-57 "Direct link to Parameters")

| Parameter                 | Type     | Description                                                                |
| ------------------------- | -------- | -------------------------------------------------------------------------- |
| `phoneFormatsArrayIndex?` | `number` | The array index as defined in the locale's phone\_number.formats\[] array. |

###### Returns[​](#returns-121 "Direct link to Returns")

`string`

A random phone number.

***

### FakerRandomizer[​](#fakerrandomizer "Direct link to FakerRandomizer")

```
type FakerRandomizer = {
  alphaNumeric: string;
  bool: boolean;
  byte: number;
  bytes: Uint8Array;
  char: string;
  chars: string[];
  clampString: string;
  decimal: number;
  digits: number[];
  double: number;
  even: number;
  float: number;
  guid: Guid;
  hash: string;
  hexadecimal: string;
  int: number;
  long: number;
  number: number;
  odd: number;
  randomLocale: string;
  replace: string;
  replaceNumbers: string;
  replaceSymbols: string;
  sByte: number;
  short: number;
  string: string;
  string2: string;
  uInt: number;
  uLong: number;
  uShort: number;
  utf16String: string;
  uuid: Guid;
  word: string;
  words: string;
  wordsArray: string[];
};
```

A randomizer that randomizes things.

#### Methods[​](#methods-13 "Direct link to Methods")

##### alphaNumeric()[​](#alphanumeric "Direct link to alphaNumeric()")

```
alphaNumeric(length: number): string;
```

Returns a random set of alpha numeric characters 0-9, a-z.

###### Parameters[​](#parameters-58 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `length`  | `number` |             |

###### Returns[​](#returns-122 "Direct link to Returns")

`string`

##### bool()[​](#bool "Direct link to bool()")

###### Call Signature[​](#call-signature-10 "Direct link to Call Signature")

```
bool(): boolean;
```

Get a random boolean.

###### Returns[​](#returns-123 "Direct link to Returns")

`boolean`

###### Call Signature[​](#call-signature-11 "Direct link to Call Signature")

```
bool(weight: number): boolean;
```

Get a random boolean.

###### Parameters[​](#parameters-59 "Direct link to Parameters")

| Parameter | Type     | Description                                  |
| --------- | -------- | -------------------------------------------- |
| `weight`  | `number` | The probability of true. Ranges from 0 to 1. |

###### Returns[​](#returns-124 "Direct link to Returns")

`boolean`

##### byte()[​](#byte "Direct link to byte()")

```
byte(min?: number, max?: number): number;
```

Generate a random byte between 0 and 255.

###### Parameters[​](#parameters-60 "Direct link to Parameters")

| Parameter | Type     | Description                                     |
| --------- | -------- | ----------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default byte.MinValue 0   |
| `max?`    | `number` | Max value, inclusive. Default byte.MaxValue 255 |

###### Returns[​](#returns-125 "Direct link to Returns")

`number`

##### bytes()[​](#bytes "Direct link to bytes()")

```
bytes(count: number): Uint8Array;
```

Get a random sequence of bytes.

###### Parameters[​](#parameters-61 "Direct link to Parameters")

| Parameter | Type     | Description                |
| --------- | -------- | -------------------------- |
| `count`   | `number` | The size of the byte array |

###### Returns[​](#returns-126 "Direct link to Returns")

`Uint8Array`

##### char()[​](#char "Direct link to char()")

```
char(min?: string, max?: string): string;
```

Generate a random char between MinValue and MaxValue.

###### Parameters[​](#parameters-62 "Direct link to Parameters")

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `min?`    | `string` | Min value, inclusive. Default char.MinValue |
| `max?`    | `string` | Max value, inclusive. Default char.MaxValue |

###### Returns[​](#returns-127 "Direct link to Returns")

`string`

##### chars()[​](#chars "Direct link to chars()")

```
chars(
   min?: string, 
   max?: string, 
   count?: number): string[];
```

Generate a random chars between MinValue and MaxValue.

###### Parameters[​](#parameters-63 "Direct link to Parameters")

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `min?`    | `string` | Min value, inclusive. Default char.MinValue |
| `max?`    | `string` | Max value, inclusive. Default char.MaxValue |
| `count?`  | `number` | The length of chars to return               |

###### Returns[​](#returns-128 "Direct link to Returns")

`string`\[]

##### clampString()[​](#clampstring "Direct link to clampString()")

```
clampString(
   str: string, 
   min?: number, 
   max?: number): string;
```

Clamps the length of a string between min and max characters. If the string is below the minimum, the string is appended with random characters up to the minimum length. If the string is over the maximum, the string is truncated at maximum characters; additionally, if the result string ends with whitespace, it is replaced with a random characters.

###### Parameters[​](#parameters-64 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `str`     | `string` |             |
| `min?`    | `number` |             |
| `max?`    | `number` |             |

###### Returns[​](#returns-129 "Direct link to Returns")

`string`

##### decimal()[​](#decimal "Direct link to decimal()")

```
decimal(min?: number, max?: number): number;
```

Get a random decimal, between 0.0 and 1.0.

###### Parameters[​](#parameters-65 "Direct link to Parameters")

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| `min?`    | `number` | Minimum, inclusive. Default 0.0 |
| `max?`    | `number` | Maximum, exclusive. Default 1.0 |

###### Returns[​](#returns-130 "Direct link to Returns")

`number`

##### digits()[​](#digits "Direct link to digits()")

```
digits(
   count: number, 
   minDigit?: number, 
   maxDigit?: number): number[];
```

Get a random sequence of digits.

###### Parameters[​](#parameters-66 "Direct link to Parameters")

| Parameter   | Type     | Description              |
| ----------- | -------- | ------------------------ |
| `count`     | `number` | How many                 |
| `minDigit?` | `number` | minimum digit, inclusive |
| `maxDigit?` | `number` | maximum digit, inclusive |

###### Returns[​](#returns-131 "Direct link to Returns")

`number`\[]

##### double()[​](#double "Direct link to double()")

```
double(min?: number, max?: number): number;
```

Get a random double, between 0.0 and 1.0.

###### Parameters[​](#parameters-67 "Direct link to Parameters")

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| `min?`    | `number` | Minimum, inclusive. Default 0.0 |
| `max?`    | `number` | Maximum, exclusive. Default 1.0 |

###### Returns[​](#returns-132 "Direct link to Returns")

`number`

##### even()[​](#even "Direct link to even()")

```
even(min?: number, max?: number): number;
```

Returns a random even number. If the range does not contain any even numbers, an `ArgumentException` is thrown.

###### Parameters[​](#parameters-68 "Direct link to Parameters")

| Parameter | Type     | Description            |
| --------- | -------- | ---------------------- |
| `min?`    | `number` | Lower bound, inclusive |
| `max?`    | `number` | Upper bound, inclusive |

###### Returns[​](#returns-133 "Direct link to Returns")

`number`

##### float()[​](#float "Direct link to float()")

```
float(min?: number, max?: number): number;
```

Get a random float, between 0.0 and 1.0.

###### Parameters[​](#parameters-69 "Direct link to Parameters")

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| `min?`    | `number` | Minimum, inclusive. Default 0.0 |
| `max?`    | `number` | Maximum, inclusive. Default 1.0 |

###### Returns[​](#returns-134 "Direct link to Returns")

`number`

##### guid()[​](#guid "Direct link to guid()")

```
guid(): Guid;
```

Get a random GUID.

###### Returns[​](#returns-135 "Direct link to Returns")

[`Guid`](#guid-2)

##### hash()[​](#hash "Direct link to hash()")

```
hash(length?: number, upperCase?: boolean): string;
```

Return a random hex hash. Default 40 characters, aka SHA-1.

###### Parameters[​](#parameters-70 "Direct link to Parameters")

| Parameter    | Type      | Description                                                       |
| ------------ | --------- | ----------------------------------------------------------------- |
| `length?`    | `number`  | The length of the hash string. Default, 40 characters, aka SHA-1. |
| `upperCase?` | `boolean` | Returns the hex string with uppercase characters.                 |

###### Returns[​](#returns-136 "Direct link to Returns")

`string`

##### hexadecimal()[​](#hexadecimal "Direct link to hexadecimal()")

```
hexadecimal(length?: number, prefix?: string): string;
```

Generates a random hexadecimal string.

###### Parameters[​](#parameters-71 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `length?` | `number` |             |
| `prefix?` | `string` |             |

###### Returns[​](#returns-137 "Direct link to Returns")

`string`

##### int()[​](#int "Direct link to int()")

```
int(min?: number, max?: number): number;
```

Generate a random int between MinValue and MaxValue.

###### Parameters[​](#parameters-72 "Direct link to Parameters")

| Parameter | Type     | Description                                |
| --------- | -------- | ------------------------------------------ |
| `min?`    | `number` | Min value, inclusive. Default int.MinValue |
| `max?`    | `number` | Max value, inclusive. Default int.MaxValue |

###### Returns[​](#returns-138 "Direct link to Returns")

`number`

##### long()[​](#long "Direct link to long()")

```
long(min?: number, max?: number): number;
```

Generate a random long between MinValue and MaxValue.

###### Parameters[​](#parameters-73 "Direct link to Parameters")

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default long.MinValue |
| `max?`    | `number` | Max value, inclusive. Default long.MaxValue |

###### Returns[​](#returns-139 "Direct link to Returns")

`number`

##### number()[​](#number "Direct link to number()")

###### Call Signature[​](#call-signature-12 "Direct link to Call Signature")

```
number(max: number): number;
```

Get an int from 0 to max.

###### Parameters[​](#parameters-74 "Direct link to Parameters")

| Parameter | Type     | Description             |
| --------- | -------- | ----------------------- |
| `max`     | `number` | Upper bound, inclusive. |

###### Returns[​](#returns-140 "Direct link to Returns")

`number`

###### Call Signature[​](#call-signature-13 "Direct link to Call Signature")

```
number(min?: number, max?: number): number;
```

Get an int from min to max.

###### Parameters[​](#parameters-75 "Direct link to Parameters")

| Parameter | Type     | Description            |
| --------- | -------- | ---------------------- |
| `min?`    | `number` | Lower bound, inclusive |
| `max?`    | `number` | Upper bound, inclusive |

###### Returns[​](#returns-141 "Direct link to Returns")

`number`

##### odd()[​](#odd "Direct link to odd()")

```
odd(min?: number, max?: number): number;
```

Returns a random odd number. If the range does not contain any odd numbers, an `ArgumentException` is thrown.

###### Parameters[​](#parameters-76 "Direct link to Parameters")

| Parameter | Type     | Description            |
| --------- | -------- | ---------------------- |
| `min?`    | `number` | Lower bound, inclusive |
| `max?`    | `number` | Upper bound, inclusive |

###### Returns[​](#returns-142 "Direct link to Returns")

`number`

##### randomLocale()[​](#randomlocale "Direct link to randomLocale()")

```
randomLocale(): string;
```

Returns a random locale.

###### Returns[​](#returns-143 "Direct link to Returns")

`string`

##### replace()[​](#replace "Direct link to replace()")

```
replace(format: string): string;
```

Replaces symbols with numbers and letters. # = number, ? = letter, \* = number or letter. IE: ###???\* -> 283QED4. Letters are uppercase.

###### Parameters[​](#parameters-77 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `format`  | `string` |             |

###### Returns[​](#returns-144 "Direct link to Returns")

`string`

##### replaceNumbers()[​](#replacenumbers "Direct link to replaceNumbers()")

```
replaceNumbers(format: string, symbol?: string): string;
```

Replaces symbols with numbers. IE: ### -> 283

###### Parameters[​](#parameters-78 "Direct link to Parameters")

| Parameter | Type     | Description                                                            |
| --------- | -------- | ---------------------------------------------------------------------- |
| `format`  | `string` | The string format                                                      |
| `symbol?` | `string` | The symbol to search for in format that will be replaced with a number |

###### Returns[​](#returns-145 "Direct link to Returns")

`string`

##### replaceSymbols()[​](#replacesymbols "Direct link to replaceSymbols()")

```
replaceSymbols(
   format: string, 
   symbol: string, 
   func: () => string): string;
```

Replaces each character instance in a string. Func is called each time a symbol is encountered.

###### Parameters[​](#parameters-79 "Direct link to Parameters")

| Parameter | Type           | Description                                                                                                      |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------- |
| `format`  | `string`       | The string with symbols to replace.                                                                              |
| `symbol`  | `string`       | The symbol to search for in the string.                                                                          |
| `func`    | () => `string` | The function that produces a character for replacement. Invoked each time the replacement symbol is encountered. |

###### Returns[​](#returns-146 "Direct link to Returns")

`string`

##### sByte()[​](#sbyte "Direct link to sByte()")

```
sByte(min?: number, max?: number): number;
```

Generate a random sbyte between -128 and 127.

###### Parameters[​](#parameters-80 "Direct link to Parameters")

| Parameter | Type     | Description                                       |
| --------- | -------- | ------------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default sbyte.MinValue -128 |
| `max?`    | `number` | Max value, inclusive. Default sbyte.MaxValue 127  |

###### Returns[​](#returns-147 "Direct link to Returns")

`number`

##### short()[​](#short "Direct link to short()")

```
short(min?: number, max?: number): number;
```

Generate a random short between MinValue and MaxValue.

###### Parameters[​](#parameters-81 "Direct link to Parameters")

| Parameter | Type     | Description                                         |
| --------- | -------- | --------------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default short.MinValue -32768 |
| `max?`    | `number` | Max value, inclusive. Default short.MaxValue 32767  |

###### Returns[​](#returns-148 "Direct link to Returns")

`number`

##### string()[​](#string "Direct link to string()")

###### Call Signature[​](#call-signature-14 "Direct link to Call Signature")

```
string(
   length?: number, 
   minChar?: string, 
   maxChar?: string): string;
```

Get a string of characters of a specific length. Uses `Int32)`. Note: This method can return ill-formed UTF16 Unicode strings with unpaired surrogates. Use `Boolean)` for technically valid Unicode.

###### Parameters[​](#parameters-82 "Direct link to Parameters")

| Parameter  | Type     | Description                                                                                  |
| ---------- | -------- | -------------------------------------------------------------------------------------------- |
| `length?`  | `number` | The exact length of the result string. If null, a random length is chosen between 40 and 80. |
| `minChar?` | `string` | Min character value, inclusive. Default char.MinValue                                        |
| `maxChar?` | `string` | Max character value, inclusive. Default char.MaxValue                                        |

###### Returns[​](#returns-149 "Direct link to Returns")

`string`

###### Call Signature[​](#call-signature-15 "Direct link to Call Signature")

```
string(
   minLength: number, 
   maxLength: number, 
   minChar?: string, 
   maxChar?: string): string;
```

Get a string of characters between `minLength` and `maxLength`. Uses `Int32)`. Note: This method can return ill-formed UTF16 Unicode strings with unpaired surrogates. Use `Boolean)` for technically valid Unicode.

###### Parameters[​](#parameters-83 "Direct link to Parameters")

| Parameter   | Type     | Description                                           |
| ----------- | -------- | ----------------------------------------------------- |
| `minLength` | `number` | Lower-bound string length. Inclusive.                 |
| `maxLength` | `number` | Upper-bound string length. Inclusive.                 |
| `minChar?`  | `string` | Min character value, inclusive. Default char.MinValue |
| `maxChar?`  | `string` | Max character value, inclusive. Default char.MaxValue |

###### Returns[​](#returns-150 "Direct link to Returns")

`string`

##### string2()[​](#string2 "Direct link to string2()")

###### Call Signature[​](#call-signature-16 "Direct link to Call Signature")

```
string2(length: number, chars?: string): string;
```

Get a string of characters with a specific length drawing characters from `chars`. The returned string may contain repeating characters from the `chars` string.

###### Parameters[​](#parameters-84 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                           |
| --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `length`  | `number` | The length of the string to return.                                                                   |
| `chars?`  | `string` | The pool of characters to draw from. The returned string may contain repeat characters from the pool. |

###### Returns[​](#returns-151 "Direct link to Returns")

`string`

###### Call Signature[​](#call-signature-17 "Direct link to Call Signature")

```
string2(
   minLength: number, 
   maxLength: number, 
   chars?: string): string;
```

Get a string of characters with a specific length drawing characters from `chars`. The returned string may contain repeating characters from the `chars` string.

###### Parameters[​](#parameters-85 "Direct link to Parameters")

| Parameter   | Type     | Description                                                                                           |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `minLength` | `number` | The minimum length of the string to return, inclusive.                                                |
| `maxLength` | `number` | The maximum length of the string to return, inclusive.                                                |
| `chars?`    | `string` | The pool of characters to draw from. The returned string may contain repeat characters from the pool. |

###### Returns[​](#returns-152 "Direct link to Returns")

`string`

##### uInt()[​](#uint "Direct link to uInt()")

```
uInt(min?: number, max?: number): number;
```

Generate a random uint between MinValue and MaxValue.

###### Parameters[​](#parameters-86 "Direct link to Parameters")

| Parameter | Type     | Description                                 |
| --------- | -------- | ------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default uint.MinValue |
| `max?`    | `number` | Max value, inclusive. Default uint.MaxValue |

###### Returns[​](#returns-153 "Direct link to Returns")

`number`

##### uLong()[​](#ulong "Direct link to uLong()")

```
uLong(min?: number, max?: number): number;
```

Generate a random ulong between MinValue and MaxValue.

###### Parameters[​](#parameters-87 "Direct link to Parameters")

| Parameter | Type     | Description                                  |
| --------- | -------- | -------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default ulong.MinValue |
| `max?`    | `number` | Max value, inclusive. Default ulong.MaxValue |

###### Returns[​](#returns-154 "Direct link to Returns")

`number`

##### uShort()[​](#ushort "Direct link to uShort()")

```
uShort(min?: number, max?: number): number;
```

Generate a random ushort between MinValue and MaxValue.

###### Parameters[​](#parameters-88 "Direct link to Parameters")

| Parameter | Type     | Description                                         |
| --------- | -------- | --------------------------------------------------- |
| `min?`    | `number` | Min value, inclusive. Default ushort.MinValue 0     |
| `max?`    | `number` | Max value, inclusive. Default ushort.MaxValue 65535 |

###### Returns[​](#returns-155 "Direct link to Returns")

`number`

##### utf16String()[​](#utf16string "Direct link to utf16String()")

```
utf16String(
   minLength?: number, 
   maxLength?: number, 
   excludeSurrogates?: boolean): string;
```

Get a string of valid UTF16 Unicode characters. This method returns a string where each character IsLetterOrDigit() is true.

###### Parameters[​](#parameters-89 "Direct link to Parameters")

| Parameter            | Type      | Description                                            |
| -------------------- | --------- | ------------------------------------------------------ |
| `minLength?`         | `number`  | The minimum length of the string to return, inclusive. |
| `maxLength?`         | `number`  | The maximum length of the string to return, inclusive. |
| `excludeSurrogates?` | `boolean` | Excludes surrogate pairs from the returned string.     |

###### Returns[​](#returns-156 "Direct link to Returns")

`string`

##### uuid()[​](#uuid "Direct link to uuid()")

```
uuid(): Guid;
```

Get a random GUID. Alias for Randomizer.Guid().

###### Returns[​](#returns-157 "Direct link to Returns")

[`Guid`](#guid-2)

##### word()[​](#word-1 "Direct link to word()")

```
word(): string;
```

Returns a single word or phrase in English.

###### Returns[​](#returns-158 "Direct link to Returns")

`string`

##### words()[​](#words-1 "Direct link to words()")

```
words(count?: number): string;
```

Gets some random words and phrases in English.

###### Parameters[​](#parameters-90 "Direct link to Parameters")

| Parameter | Type     | Description                    |
| --------- | -------- | ------------------------------ |
| `count?`  | `number` | Number of times to call Word() |

###### Returns[​](#returns-159 "Direct link to Returns")

`string`

##### wordsArray()[​](#wordsarray "Direct link to wordsArray()")

###### Call Signature[​](#call-signature-18 "Direct link to Call Signature")

```
wordsArray(min: number, max: number): string[];
```

Get a range of words in an array (English).

###### Parameters[​](#parameters-91 "Direct link to Parameters")

| Parameter | Type     | Description                    |
| --------- | -------- | ------------------------------ |
| `min`     | `number` | Minimum word count, inclusive. |
| `max`     | `number` | Maximum word count, inclusive. |

###### Returns[​](#returns-160 "Direct link to Returns")

`string`\[]

###### Call Signature[​](#call-signature-19 "Direct link to Call Signature")

```
wordsArray(count: number): string[];
```

Get a specific number of words in an array (English).

###### Parameters[​](#parameters-92 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `count`   | `number` |             |

###### Returns[​](#returns-161 "Direct link to Returns")

`string`\[]

***

### FakerScriptApi[​](#fakerscriptapi "Direct link to FakerScriptApi")

```
type FakerScriptApi = {
  address: FakerAddress;
  commerce: FakerCommerce;
  company: FakerCompany;
  database: FakerDatabase;
  date: FakerDate;
  finance: FakerFinance;
  hacker: FakerHacker;
  image: FakerImages;
  internet: FakerInternet;
  lorem: FakerLorem;
  music: FakerMusic;
  name: FakerName;
  phone: FakerPhoneNumbers;
  random: FakerRandomizer;
  system: FakerSystem;
  vehicle: FakerVehicle;
};
```

The faker methods to generate fake, but realistic, data.

#### Properties[​](#properties-16 "Direct link to Properties")

##### address[​](#address "Direct link to address")

```
readonly address: FakerAddress;
```

Methods for generating an address.

##### commerce[​](#commerce "Direct link to commerce")

```
readonly commerce: FakerCommerce;
```

Methods relating to commerce.

##### company[​](#company "Direct link to company")

```
readonly company: FakerCompany;
```

Methods for generating random company names and phrases.

##### database[​](#database "Direct link to database")

```
readonly database: FakerDatabase;
```

Generates some random database stuff.

##### date[​](#date "Direct link to date")

```
readonly date: FakerDate;
```

Methods for generating dates.

##### finance[​](#finance "Direct link to finance")

```
readonly finance: FakerFinance;
```

Provides financial randomness.

##### hacker[​](#hacker "Direct link to hacker")

```
readonly hacker: FakerHacker;
```

Hackerish words.

##### image[​](#image "Direct link to image")

```
readonly image: FakerImages;
```

Generates images URLs.

##### internet[​](#internet "Direct link to internet")

```
readonly internet: FakerInternet;
```

Random Internet things like email addresses.

##### lorem[​](#lorem "Direct link to lorem")

```
readonly lorem: FakerLorem;
```

Generates plain old boring text.

##### music[​](#music "Direct link to music")

```
readonly music: FakerMusic;
```

Methods for generating music related stuff.

##### name[​](#name-1 "Direct link to name")

```
readonly name: FakerName;
```

Methods for generating names.

##### phone[​](#phone "Direct link to phone")

```
readonly phone: FakerPhoneNumbers;
```

Generates phone numbers.

##### random[​](#random-13 "Direct link to random")

```
readonly random: FakerRandomizer;
```

A randomizer that randomizes things.

##### system[​](#system "Direct link to system")

```
readonly system: FakerSystem;
```

Generates fake data for many computer systems properties.

##### vehicle[​](#vehicle "Direct link to vehicle")

```
readonly vehicle: FakerVehicle;
```

Methods for generating vehicle information.

***

### FakerSystem[​](#fakersystem "Direct link to FakerSystem")

```
type FakerSystem = {
  locale: string;
  random: FakerRandomizer;
  androidId: string;
  applePushToken: string;
  blackBerryPin: string;
  commonFileExt: string;
  commonFileName: string;
  commonFileType: string;
  directoryPath: string;
  fileExt: string;
  fileName: string;
  filePath: string;
  fileType: string;
  mimeType: string;
  semver: string;
};
```

Generates fake data for many computer systems properties

#### Properties[​](#properties-17 "Direct link to Properties")

##### locale[​](#locale-13 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-14 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-14 "Direct link to Methods")

##### androidId()[​](#androidid "Direct link to androidId()")

```
androidId(): string;
```

Get a random GCM registration ID.

###### Returns[​](#returns-162 "Direct link to Returns")

`string`

A random GCM registration ID.

##### applePushToken()[​](#applepushtoken "Direct link to applePushToken()")

```
applePushToken(): string;
```

Get a random Apple Push Token.

###### Returns[​](#returns-163 "Direct link to Returns")

`string`

A random Apple Push Token.

##### blackBerryPin()[​](#blackberrypin "Direct link to blackBerryPin()")

```
blackBerryPin(): string;
```

Get a random BlackBerry Device PIN.

###### Returns[​](#returns-164 "Direct link to Returns")

`string`

A random BlackBerry Device PIN.

##### commonFileExt()[​](#commonfileext "Direct link to commonFileExt()")

```
commonFileExt(): string;
```

Returns a commonly used file extension.

###### Returns[​](#returns-165 "Direct link to Returns")

`string`

A commonly used file extension.

##### commonFileName()[​](#commonfilename "Direct link to commonFileName()")

```
commonFileName(ext?: string): string;
```

Generates a random file name with a common file extension. Extension can be overwritten with `ext`.

###### Parameters[​](#parameters-93 "Direct link to Parameters")

| Parameter | Type     | Description                                |
| --------- | -------- | ------------------------------------------ |
| `ext?`    | `string` | The extensions to be used for a file name. |

###### Returns[​](#returns-166 "Direct link to Returns")

`string`

A random file name with a common extension or `ext`.

##### commonFileType()[​](#commonfiletype "Direct link to commonFileType()")

```
commonFileType(): string;
```

Returns a commonly used file type.

###### Returns[​](#returns-167 "Direct link to Returns")

`string`

A commonly used file type.

##### directoryPath()[​](#directorypath "Direct link to directoryPath()")

```
directoryPath(): string;
```

Get a random directory path (Unix).

###### Returns[​](#returns-168 "Direct link to Returns")

`string`

A random Unix directory path.

##### fileExt()[​](#fileext "Direct link to fileExt()")

```
fileExt(mimeType?: string): string;
```

Gets a random extension for the given mime type.

###### Parameters[​](#parameters-94 "Direct link to Parameters")

| Parameter   | Type     | Description |
| ----------- | -------- | ----------- |
| `mimeType?` | `string` |             |

###### Returns[​](#returns-169 "Direct link to Returns")

`string`

A random extension for the given mime type.

##### fileName()[​](#filename "Direct link to fileName()")

```
fileName(ext?: string): string;
```

Get a random file name.

###### Parameters[​](#parameters-95 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                    |
| --------- | -------- | ---------------------------------------------------------------------------------------------- |
| `ext?`    | `string` | The extension the file name will have. If null is provided, a random extension will be picked. |

###### Returns[​](#returns-170 "Direct link to Returns")

`string`

A random file name with the given `ext` or a random extension

##### filePath()[​](#filepath "Direct link to filePath()")

```
filePath(): string;
```

Get a random file path (Unix).

###### Returns[​](#returns-171 "Direct link to Returns")

`string`

A random Unix file path.

##### fileType()[​](#filetype "Direct link to fileType()")

```
fileType(): string;
```

Returns any file type available as mime-type.

###### Returns[​](#returns-172 "Direct link to Returns")

`string`

Any file type available as mime-type.

##### mimeType()[​](#mimetype "Direct link to mimeType()")

```
mimeType(): string;
```

Get a random mime type.

###### Returns[​](#returns-173 "Direct link to Returns")

`string`

A random mime type.

##### semver()[​](#semver "Direct link to semver()")

```
semver(): string;
```

Get a random semver version string.

###### Returns[​](#returns-174 "Direct link to Returns")

`string`

A random semver version string.

***

### FakerVehicle[​](#fakervehicle "Direct link to FakerVehicle")

```
type FakerVehicle = {
  locale: string;
  random: FakerRandomizer;
  fuel: string;
  manufacturer: string;
  model: string;
  type: string;
  vin: string;
};
```

Methods for generating vehicle information

#### Properties[​](#properties-18 "Direct link to Properties")

##### locale[​](#locale-14 "Direct link to locale")

```
locale: string;
```

##### random[​](#random-15 "Direct link to random")

```
random: FakerRandomizer;
```

#### Methods[​](#methods-15 "Direct link to Methods")

##### fuel()[​](#fuel "Direct link to fuel()")

```
fuel(): string;
```

Get a vehicle fuel type. IE: Electric, Gasoline, Diesel.

###### Returns[​](#returns-175 "Direct link to Returns")

`string`

##### manufacturer()[​](#manufacturer "Direct link to manufacturer()")

```
manufacturer(): string;
```

Get a vehicle manufacture name. IE: Toyota, Ford, Porsche.

###### Returns[​](#returns-176 "Direct link to Returns")

`string`

##### model()[​](#model "Direct link to model()")

```
model(): string;
```

Get a vehicle model. IE: Camry, Civic, Accord.

###### Returns[​](#returns-177 "Direct link to Returns")

`string`

##### type()[​](#type-1 "Direct link to type()")

```
type(): string;
```

Get a vehicle type. IE: Minivan, SUV, Sedan.

###### Returns[​](#returns-178 "Direct link to Returns")

`string`

##### vin()[​](#vin "Direct link to vin()")

```
vin(strict?: boolean): string;
```

Generate a vehicle identification number (VIN).

###### Parameters[​](#parameters-96 "Direct link to Parameters")

| Parameter | Type      | Description                                                                    |
| --------- | --------- | ------------------------------------------------------------------------------ |
| `strict?` | `boolean` | Limits the acceptable characters to alpha numeric uppercase except I, O and Q. |

###### Returns[​](#returns-179 "Direct link to Returns")

`string`

***

### Guid[​](#guid-1 "Direct link to Guid")

```
type Guid = {
  variant: number;
  version: number;
  toString: string;
};
```

#### Properties[​](#properties-19 "Direct link to Properties")

##### variant[​](#variant "Direct link to variant")

```
readonly variant: number;
```

##### version[​](#version "Direct link to version")

```
readonly version: number;
```

#### Methods[​](#methods-16 "Direct link to Methods")

##### toString()[​](#tostring "Direct link to toString()")

```
toString(): string;
```

###### Returns[​](#returns-180 "Direct link to Returns")

`string`

***

### PreviewScriptApi[​](#previewscriptapi "Direct link to PreviewScriptApi")

```
type PreviewScriptApi = {
  file: Promise<void>;
  html: Promise<void>;
  pdf: Promise<void>;
};
```

Functions to view previews of files inside Kreya.

#### Methods[​](#methods-17 "Direct link to Methods")

##### file()[​](#file "Direct link to file()")

```
file(path: string, name?: string): Promise<void>;
```

Opens a preview tab in Kreya and displays a preview of the provided file.

###### Parameters[​](#parameters-97 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                                 |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| `path`    | `string` | The path to the file. Needs to be in the directory of the Kreya project or any subdirectory.                |
| `name?`   | `string` | The name of the preview. If the same name is used as with a previous call, the previous preview is updated. |

###### Returns[​](#returns-181 "Direct link to Returns")

`Promise`<`void`>

##### html()[​](#html "Direct link to html()")

```
html(data: string, name?: string): Promise<void>;
```

Opens a preview tab in Kreya and displays the provided data as HTML.

###### Parameters[​](#parameters-98 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                                 |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| `data`    | `string` | The data.                                                                                                   |
| `name?`   | `string` | The name of the preview. If the same name is used as with a previous call, the previous preview is updated. |

###### Returns[​](#returns-182 "Direct link to Returns")

`Promise`<`void`>

##### pdf()[​](#pdf "Direct link to pdf()")

```
pdf(data: Uint8Array, name?: string): Promise<void>;
```

Opens a preview tab in Kreya and displays the provided data as a PDF.

###### Parameters[​](#parameters-99 "Direct link to Parameters")

| Parameter | Type         | Description                                                                                                 |
| --------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| `data`    | `Uint8Array` | The data.                                                                                                   |
| `name?`   | `string`     | The name of the preview. If the same name is used as with a previous call, the previous preview is updated. |

###### Returns[​](#returns-183 "Direct link to Returns")

`Promise`<`void`>

***

### SnapshotScriptApi[​](#snapshotscriptapi "Direct link to SnapshotScriptApi")

```
type SnapshotScriptApi = {
  verifyFile: Promise<void>;
  verifyJson: Promise<void>;
  verifyObjectAsJson: Promise<void>;
  verifyText: Promise<void>;
};
```

Functions to assert snapshots.

#### Methods[​](#methods-18 "Direct link to Methods")

##### verifyFile()[​](#verifyfile "Direct link to verifyFile()")

###### Call Signature[​](#call-signature-20 "Direct link to Call Signature")

```
verifyFile(path: string): Promise<void>;
```

Asserts a snapshot file. Only text-based files are supported.

###### Parameters[​](#parameters-100 "Direct link to Parameters")

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| `path`    | `string` | The path to the file to assert. |

###### Returns[​](#returns-184 "Direct link to Returns")

`Promise`<`void`>

###### Call Signature[​](#call-signature-21 "Direct link to Call Signature")

```
verifyFile(name: string, path: string): Promise<void>;
```

Asserts a snapshot file. Only text-based files are supported.

###### Parameters[​](#parameters-101 "Direct link to Parameters")

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| `name`    | `string` | The name of the snapshot.       |
| `path`    | `string` | The path to the file to assert. |

###### Returns[​](#returns-185 "Direct link to Returns")

`Promise`<`void`>

##### verifyJson()[​](#verifyjson "Direct link to verifyJson()")

```
verifyJson(name: string, json: string): Promise<void>;
```

Asserts a string as a JSON snapshot.

###### Parameters[​](#parameters-102 "Direct link to Parameters")

| Parameter | Type     | Description                |
| --------- | -------- | -------------------------- |
| `name`    | `string` | The name of the snapshot.  |
| `json`    | `string` | The JSON string to assert. |

###### Returns[​](#returns-186 "Direct link to Returns")

`Promise`<`void`>

##### verifyObjectAsJson()[​](#verifyobjectasjson "Direct link to verifyObjectAsJson()")

```
verifyObjectAsJson(name: string, obj: any): Promise<void>;
```

Asserts an object as a JSON snapshot.

###### Parameters[​](#parameters-103 "Direct link to Parameters")

| Parameter | Type     | Description                |
| --------- | -------- | -------------------------- |
| `name`    | `string` | The name of the snapshot.  |
| `obj`     | `any`    | The JSON object to assert. |

###### Returns[​](#returns-187 "Direct link to Returns")

`Promise`<`void`>

##### verifyText()[​](#verifytext "Direct link to verifyText()")

```
verifyText(name: string, text: string): Promise<void>;
```

Asserts a string snapshot.

###### Parameters[​](#parameters-104 "Direct link to Parameters")

| Parameter | Type     | Description               |
| --------- | -------- | ------------------------- |
| `name`    | `string` | The name of the snapshot. |
| `text`    | `string` | The string to assert.     |

###### Returns[​](#returns-188 "Direct link to Returns")

`Promise`<`void`>

***

### UserVariablesScriptApi[​](#uservariablesscriptapi "Direct link to UserVariablesScriptApi")

```
type UserVariablesScriptApi = {
  clear: void;
  delete: void;
  get: any;
  has: boolean;
  keys: Iterable<string>;
  set: void;
};
```

The storage to set and retrieve custom variables, which are accessible in other operations and via templating.

#### Methods[​](#methods-19 "Direct link to Methods")

##### clear()[​](#clear "Direct link to clear()")

```
clear(): void;
```

Clears/deletes ALL variables.

###### Returns[​](#returns-189 "Direct link to Returns")

`void`

##### delete()[​](#delete "Direct link to delete()")

```
delete(key: string): void;
```

Deletes the specified variable.

###### Parameters[​](#parameters-105 "Direct link to Parameters")

| Parameter | Type     | Description              |
| --------- | -------- | ------------------------ |
| `key`     | `string` | The key of the variable. |

###### Returns[​](#returns-190 "Direct link to Returns")

`void`

##### get()[​](#get "Direct link to get()")

```
get(key: string): any;
```

Gets the value of a variable.

###### Parameters[​](#parameters-106 "Direct link to Parameters")

| Parameter | Type     | Description              |
| --------- | -------- | ------------------------ |
| `key`     | `string` | The key of the variable. |

###### Returns[​](#returns-191 "Direct link to Returns")

`any`

The value of the variable or undefined if the variable does not exist.

##### has()[​](#has "Direct link to has()")

```
has(key: string): boolean;
```

Checks whether the specified variable exists.

###### Parameters[​](#parameters-107 "Direct link to Parameters")

| Parameter | Type     | Description              |
| --------- | -------- | ------------------------ |
| `key`     | `string` | The key of the variable. |

###### Returns[​](#returns-192 "Direct link to Returns")

`boolean`

True when the variable exists, otherwise false.

##### keys()[​](#keys "Direct link to keys()")

```
keys(): Iterable<string>;
```

Returns the keys of all stored variables.

###### Returns[​](#returns-193 "Direct link to Returns")

`Iterable`<`string`>

The keys of all stored variables.

##### set()[​](#set "Direct link to set()")

```
set(key: string, value: any): void;
```

Sets a variable. Setting undefined as a value deletes the variable.

###### Parameters[​](#parameters-108 "Direct link to Parameters")

| Parameter | Type     | Description                |
| --------- | -------- | -------------------------- |
| `key`     | `string` | The key of the variable.   |
| `value`   | `any`    | The value of the variable. |

###### Returns[​](#returns-194 "Direct link to Returns")

`void`
