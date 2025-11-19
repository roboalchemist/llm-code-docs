# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/action.md

# Source: https://docs.zapier.com/platform/build/action.md

# Source: https://docs.zapier.com/powered-by-zapier/api-reference/common-types/action.md

# Source: https://docs.zapier.com/platform/build/action.md

# Action

> Every Zap starts with a single trigger that watches for new or updated data, starting the user's workflow. Action steps then make use of that data.

Zapier actions create or update a single item in your app through API calls that include multiple details from user customized [input fields](/platform/build/add-fields).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=8d087aba0e45602060e48467c914ad96" alt="Zapier Action Visual Builder" data-og-width="980" width="980" data-og-height="963" height="963" data-path="images/57f28534d180f2a642ebe0be2e236c32.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=fcb42b22591c1cfc20c85323cb1f6682 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=4628c816fb5c92963a108793de53ea4f 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=bd4690eb95577fb50bb8b489f413a97d 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=68dff5405dda6e90297729bc8ae58039 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=3f659de5dbd9b8916071de4cd90d7d20 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/57f28534d180f2a642ebe0be2e236c32.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=57e6ab931ccad477f916e80ccde1ad7f 2500w" />
</Frame>

Zaps can have one or more actions.

There are two types of actions to select.

## 1. Create actions

Most Zapier integrations should at a minimum include create actions to let users add items to their app automatically. Common actions by app category [here](/platform/quickstart/must-have-triggers-and-actions) should be used for inspiration when building your app.

*Create* actions in Zaps can create new items in an app or update existing items. The output returned should be an object containing individual fields that will be parsed for mapping into subsequent Zap steps.

The [output returned](/platform/build/response-types) by a *create* should be an object containing individual fields about the item that was created such as IDs, details about the new item including a link if possible, and any other useful data about the record. Do not return just a `success` message.

Unsucessful actions should return `4xx` errors. If your API returns a `2xx` error, add custom code to your API call to replace it with a correct error.

Update actions should be separate from create actions.

Actions may create multiple items if needed, using the same data, though you will likely need to customize the API call code to create multiple items at once. Only do this for linked items, such as if an app stores customers and customer addresses separately. If the multiple items that need to be created are top-level, complex items in your app, they should be separate actions within Zapier. You can then link the two with a drop-down menu in the action to select the paired item, add a search action for users to find the specific item they need, and then let them match the items with the [*Use a Custom Value* option](https://help.zapier.com/hc/en-us/articles/8496241696141) in Zapier.

## 2. Search actions

*Search* actions find existing items in an app and can optionally be paired with *create* actions to [add a new item](/platform/build/search-or-create) if the search does not return a result.

Search actions let users do more with the data they've already added to your app; such as avoiding adding duplicate items or look up info about an item, for example weather, conversion, and contact lookup, to use in a subsequent step.

Most useful searches return one individual item that will likely be needed in another Zap step.

The [output returned](/platform/build/response-types) by a *search* should be a JSON-formatted array sorted with the best match first. Only the first item will be returned. For no match found, a `200` with an empty array must be returned. If your API returns a `404` error for searches without results, add custom code to your API call to replace it with an empty array.

## 3. Delete actions

Zapier recommends careful consideration of action steps that fully delete or remove data. To prevent data loss, action steps should only add or update data.

If you are considering adding a delete action to your app, consider alternative actions for items such as deactivating, unsubscribing, or canceling, instead of deleting items completely.

If you do add a delete action, make sure to include a `Copy` field to clarify to users that the action is irreversible once the API request is made.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
