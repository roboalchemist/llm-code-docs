Source: https://docs.slack.dev/changelog/2016/08/23/token-lengthening

# Token lengthening

August 23, 2016

Beginning next month, newly issued tokens will be longer than previously issued tokens.

Until now, we haven't documented the string length of tokens, so we hope you've used caution when preparing your token storage apparatuses.

## What's changing? {#whats-changing}

* Recently issued user tokens, bot user tokens, and test token strings will be longer than those you've typically encountered.
* Newer tokens will be at least twenty characters longer.
* We advise future-proofing your storage and anticipating tokens as long as 255 characters.

### The tokens of today {#the-tokens-of-today}

Here's a representative string of token lengths you encounter today:

```text
xoxb-96219857393-62330539414-22147117595-9d8cfc0f59
```text

### The tokens of tomorrow {#the-tokens-of-tomorrow}

Once lengthened, newly issued tokens may look something more like:

```text
xoxb-96219857393-62330539414-22147117595-9d8cfc0f596f1ed002ab5595859014e
```text

### The tokens of an almost impossible future {#the-tokens-of-an-almost-impossible-future}

To future-proof your storage techniques, anticipate token strings as long as 255 characters, like the following:

```text
xoxb-96219857393-62330539414-22147117595-9d8cfc0f596f1ed002ab5595859014e9afbbb6a18d5616343e5d5f4351ee3bbc837cf5ed9a9131bc21e85a4d5524d04dc57c59bf6bc7b9371f80e0ddde614b25bc092faa123bb38fa2c195adc171a7d17282ebbc08e2d4bc456c8135e49a3a6f64a3df0f6406e7f8237b64
```text

Or even filled with yet more incomprehensible line noise:

```text
8d8d5b8317b3778096fa75c4f1563269d8cfc0f596f1ed002ab595859014e9afbbb6a18d5616343e5d5f4351ee3bbc837cf5ed9a9131bc21e85a4d5524d04dc57c59bf6bc7b9371f80e0ddde614b25bc092faa123bb38fa2c195adc171a7d17282ebbc08e2d4bc456c8135e49a3a6f64a3df0f6406e7f8237b64
```text

## What isn't changing? {#what-isnt-changing}

* It's "same as it ever was" for the tokens already awarded to you.
* A token is still a string of characters. They aren't suddenly complex objects, minerals, or vegetables.

## How do I prepare? {#how-do-i-prepare}

If you store tokens in a database or other storage container, verify that you're ready for longer tokens. To best prepare for unknown futures, anticipate a string as long as 255 characters, such as the `VARCHAR(255)` or `TINYTEXT` data types.

We strongly recommend not relying on any perceived semantics found in token strings.

## When is this happening? {#when-is-this-happening}

We'd like to lengthen token strings next month, on or around **September 20th, 2016**.

Please review your token storage habits and, if necessary, make the needed modifications. Have questions or concerns? We're happy to help! Feel free to contact us [here](https://slack.com/help/requests/new).

## Tags:

* [Announcement](/changelog/tags/announcement)
