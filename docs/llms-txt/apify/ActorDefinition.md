# Source: https://docs.apify.com/api/client/js/reference/interface/ActorDefinition.md

# ActorDefinition<!-- -->

Actor definition from the `.actor/actor.json` file.

Contains the Actor's configuration, input schema, and other metadata.

## Index[**](#Index)

### Properties

* [**actorSpecification](#actorSpecification)
* [**buildTag](#buildTag)
* [**changelog](#changelog)
* [**dockerContextDir](#dockerContextDir)
* [**dockerfile](#dockerfile)
* [**environmentVariables](#environmentVariables)
* [**input](#input)
* [**maxMemoryMbytes](#maxMemoryMbytes)
* [**minMemoryMbytes](#minMemoryMbytes)
* [**name](#name)
* [**readme](#readme)
* [**storages](#storages)
* [**usesStandbyMode](#usesStandbyMode)
* [**version](#version)

## Properties<!-- -->[**](#Properties)

### [**](#actorSpecification)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L826)actorSpecification

**actorSpecification: number

### [**](#buildTag)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L829)optionalbuildTag

**buildTag?

<!-- -->

: string

### [**](#changelog)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L835)optionalchangelog

**changelog?

<!-- -->

: null | string

### [**](#dockerContextDir)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L832)optionaldockerContextDir

**dockerContextDir?

<!-- -->

: string

### [**](#dockerfile)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L831)optionaldockerfile

**dockerfile?

<!-- -->

: string

### [**](#environmentVariables)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L830)optionalenvironmentVariables

**environmentVariables?

<!-- -->

: Record\<string, string>

### [**](#input)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L834)optionalinput

**input?

<!-- -->

: null | object

### [**](#maxMemoryMbytes)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L840)optionalmaxMemoryMbytes

**maxMemoryMbytes?

<!-- -->

: number

### [**](#minMemoryMbytes)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L839)optionalminMemoryMbytes

**minMemoryMbytes?

<!-- -->

: number

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L827)name

**name: string

### [**](#readme)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L833)optionalreadme

**readme?

<!-- -->

: null | string

### [**](#storages)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L836)optionalstorages

**storages?

<!-- -->

: { dataset?

<!-- -->

: object }

#### Type declaration

* ##### optionaldataset?<!-- -->: object

### [**](#usesStandbyMode)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L841)optionalusesStandbyMode

**usesStandbyMode?

<!-- -->

: boolean

### [**](#version)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L828)version

**version: string
