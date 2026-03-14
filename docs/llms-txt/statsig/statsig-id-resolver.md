# Source: https://docs.statsig.com/guides/statsig-id-resolver.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Statsig ID Resolver

## What is Statsig ID Resolver?

Statsig ID Resolver is an integration set up at the project level that brings your ID names into console. IDs are used everywhere within Console, but unless you are an ID Wizard it is hard to tell at a glance who or what an ID belongs to. Take Feature Gate rules for example:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver1.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=4b5f06aa7af48bdb6e3470d9b517b113" alt="Feature gate rules with raw user IDs" width="1238" height="226" data-path="images/id_resolver1.png" />
</Frame>

Each of the IDs shown represent a superhero with a name and other identifying information. After setting up ID Resolver you will be able to see an ID’s “name” next to each ID. In this example, the ID’s name is the superhero’s name followed by their publisher. You have the power to define “name” as whatever string is most useful for your project.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver2.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=5ffb63e0ad167166838811527b6842d7" alt="Feature gate rules with resolved ID names" width="1232" height="234" data-path="images/id_resolver2.png" />
</Frame>

Additionally, after setting up ID Resolver Autocomplete you can begin typing in an ID’s name and have it auto-resolve to the correct ID

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver3.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=f48b0a4bee4985b5914b777883e87949" alt="ID autocomplete functionality in action" width="1295" height="588" data-path="images/id_resolver3.png" />
</Frame>

ID Resolver can be used wherever you enter IDs, for example in Feature Gate rules, Overrides, Users tab, and Segment ID lists

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver_4.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=85f8c7aed8e1f4089ebff8b2482210ec" alt="ID resolver usage across console interfaces" width="1628" height="1368" data-path="images/id_resolver_4.png" />
</Frame>

## Step 1 - Create your ID Resolver Webhook

You will need to create and host your own webhook for this integration. This webhook should take in an `id` and a possibly null `unit_type` and return `name`. `unit_type` will come in the form of userID, stableID, or one of your custom ID types. The length of `name` should be under 100 characters.

```js  theme={null}
  const inputId = req.body.id as string | null;
  const unitType = req.body.unit_type as string | null;

  if (!inputId) {
    res.status(200).json({
      success: true,
      data: {
        name: "",
      },
    });
  }

  const result = IDResolverDatabase.find((d) => d.id === inputId);
  res.status(200).json({
    success: true,
    data: {
      name: result ? result.name + ", " + result.Publisher : "",
    },
  });
```

## Step 2 - Create your ID Resolver Autocomplete Webhook

This webhook should take in a `name` (the current partially typed name) and a possibly null `unit_type` and return the array `results` which contains potential matches in the shape of `{name: string, id: string}`. It should return at most 100 results, and the length per item should be under 100 characters.

```js  theme={null}
  const partialName = req.body.name as string | null;
  const unitType = req.body.unit_type as string | null;

  if (!partialName) {
    res.status(200).json({
      success: true,
      data: {
        results: [],
      },
    });
  }

  const results = IDResolverDatabase.filter((d) =>
    d.name.match(new RegExp(`^${partialName}`))
  ).limit(100);
  res.status(200).json({
    success: true,
    data: {
      results: results.map((result) => {
        return {
          name: result.name + ", (" + result.Publisher + ")",
          id: result.id,
        };
      }),
    },
  });
```

## Step 3 - Integrate your webhooks with Statsig

You can find Statsig ID Resolver under the Integrations tab within Project Settings

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver_setup_1.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=8b0fd37abf9fb76f83db79e3cdd047ce" alt="ID resolver integration setup screen" width="1477" height="763" data-path="images/id_resolver_setup_1.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/tmQg7nj9OLg4TK9Z/images/id_resolver_setup_2.png?fit=max&auto=format&n=tmQg7nj9OLg4TK9Z&q=85&s=9d9efcfdb8c82af6136058003cc1fd4f" alt="ID resolver webhook configuration interface" width="1636" height="1256" data-path="images/id_resolver_setup_2.png" />
</Frame>

### Secure Your Webhook With an API Key (Optional, But Recommended)

Statsig accepts an optional API key in the integration configuration. If you submit a string here, we will call your webhook with the HTTP Header "Authorization: Bearer \<apiKey>."

This can be any random string. Your server should reject any request that does not supply the same string you supplied when setting up the integration. One way to generate this is by running `openssl rand -hex 32`. Make sure to store and read this securely on your server.

*And that's it! You're off to the races with easier-to-recognize IDs throughout the Console.*


Built with [Mintlify](https://mintlify.com).