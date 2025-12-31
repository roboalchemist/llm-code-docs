# Source: https://upstash.com/docs/qstash/howto/roll-signing-keys.md

# Roll Your Signing Keys

Because your API needs to be publicly accessible from the internet, you should
make sure to verify the authenticity of each request.

Upstash provides a JWT with each request. This JWT is signed by your individual
secret signing keys. [Read more](/qstash/howto/signature).

We are using 2 signing keys:

* current: This is the key used to sign the JWT.
* next: This key will be used to sign after you have rolled your keys.

If we were using only a single key, there would be some time between when you
rolled your keys and when you can edit the key in your applications. In order to
minimize downtime, we use 2 keys and you should always try to verify with both
keys.

## What happens when I roll my keys?

When you roll your keys, the current key will be replaced with the next key and
a new next key will be generated.

```
currentKey = nextKey
nextKey = generateNewKey()
```

<Warning>
  Rolling your keys twice without updating your applications will cause your apps
  to reject all requests, because both the current and next keys will have been
  replaced.
</Warning>

## How to roll your keys

Rolling your keys can be done by going to the
[QStash UI](https://console.upstash.com/qstash) and clicking on the "Roll keys"
button.

<img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d94642cddf6fbb5b61929a31c8efee31" alt="" data-og-width="2008" width="2008" data-og-height="298" height="298" data-path="img/qstash/roll_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0754e3790b9dbcd40f9630bac6818fc5 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=eff2fb051bf97c992f5d8dcba4fd605e 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=116dd392bab3a652fb4b19417cc87e3b 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=65e6213926395514858b718cb13508bf 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=699c83e814b5f07d35e3364c97c1c9e4 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/roll_keys.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0c618e0b0c2d364d62fdacccd37b7cab 2500w" />
