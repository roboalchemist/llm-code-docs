# Source: https://docs.zapier.com/platform/manage/input-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change input form field key

## Change scenario

You want to change the key of one or more form field inputs within a trigger, action, or search.

## Impact to users

Modifying the key of a form field input is a breaking change.

Unless precautions are taken, changing the key of an existing form field input will break the field's mapping within the step using it. The previously-mapped value will be dropped, resulting in missed data and/or errors.

## Best practices

* Avoid changing form field input keys

If your API endpoint needs a different property in the request, consider changing the property key instead of modifying the form field input's key.

Form field input keys do not necessarily need to match the properties expected by your API.

Let's say you have a form field input with the key `first_name` (right) and are sending the field's value to your API using a property with the same name, `first_name` (left):

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=1b2c72947c043b94a206a8d4019abdf0" data-og-width="723" width="723" data-og-height="142" height="142" data-path="images/cf7d34d12c1a1c42f75a89815409d20e.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=dc3ecc67468dbb20f0276057b0242508 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=c19aafd9fb692aaf85ab2013e93a199b 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ca920916a0439841026f36ce559fdfa6 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a9349a2b18340b3d84b5a7569a409e21 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=7ce291b1ab4d0bf8f55f7f43c54790a8 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/cf7d34d12c1a1c42f75a89815409d20e.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=66c12c404ce5ebe9379edfa890cce53b 2500w" />
</Frame>

```bash  theme={null}
body: {
  first_name: bundle.inputData.first_name; // original
}
```

Then, your API changes and expects the request property to be `firstname` (one word) instead. As shown below, you can change the request property key (left) as needed (`firstname`) while still referring to the form field input (right) based on its original key (`first_name`):

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=7b9d3749c41fc928367fdbb130b048ed" data-og-width="684" width="684" data-og-height="138" height="138" data-path="images/b6b1776d964f52eed12d64ff264b8cac.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=4a338292eda3e343f841fc11a492f559 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=93c874a0b41f9602d5959e212b2e2cd2 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=212ce579712794d365f3eae0275d5f1b 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=247b46894363d3b640a409695b35f9c1 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=dfdba22c1321f6af8da95fe64f6b24e0 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b6b1776d964f52eed12d64ff264b8cac.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=5e2bc635799791cc5c32902491273042 2500w" />
</Frame>

```bash  theme={null}
body: {
  firstname: bundle.inputData.first_name; // new - request key and field key can differ
}
```

* Handle both the old and new keys

If it's not possible to simply change a hardcoded request property's key:

We recommend that you design the trigger or action to handle both the old and new key

Using the same example above, let's say that instead of hardcoding your request properties, you were spreading `bundle.inputData` into the body of the API request, so there was a one-to-one relationship between field keys and request properties.

```bash  theme={null}
body: {
  ...bundle.inputData // original - request keys tied to field keys
}
```

Instead of changing form field input keys, you can use Code Mode (Platform UI) or code (Platform CLI) to modify the request.

For example, below, we create a new object, payload, with all the fields from `bundle.inputData` AND the updated property, `firstname`. Then we delete the old property, `first_name`, and send the updated object in the request:

```js  theme={null}
// copy bundle, add updated property
const payload = { ...bundle.inputData, firstname: bundle.inputData.first_name };

// delete old property
delete payload.first_name;

body = {
  ...payload, // send updated payload
};
```

With this approach, or one like it, you can change the request as needed without modifying field keys and breaking users' mappings.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
