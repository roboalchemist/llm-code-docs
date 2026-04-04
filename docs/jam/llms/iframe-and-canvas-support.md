# Source: https://jam.dev/docs/record-a-jam/instant-replay/iframe-and-canvas-support.md

# iFrame & canvas support

Instant Replay is designed to keep website performance fast and lightweight, while still capturing bugs on the go, which means that Instant Replay ignores the heaviest HTML elements: iframe & canvas.&#x20;

That means if you capture an Instant Replay of a bug on a page that has iframe or canvas elements, you’ll see a black box in the resulting Instant Replay where those elements are.

Internally at Jam, we’ve gone back and forth on what is the best way to handle these heavier HTML elements, and what we’ve found time and time again is that our users prefer not to have them captured, than to have a more laggy experience. Having said that, we’re open to feedback and curious what you think. If you’d like to share any feedback, please reach out to us at <hello@jam.dev>.
