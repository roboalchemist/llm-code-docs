# Source: https://docs.unifygtm.com/reference/integrations/salesforce/default-values.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/default-values.md

# Source: https://docs.unifygtm.com/reference/integrations/salesforce/default-values.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/default-values.md

# Source: https://docs.unifygtm.com/reference/integrations/salesforce/default-values.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/default-values.md

# Configure Default Values

> Learn how to set default values writing to HubSpot.

# Overview

When Unify creates or updates records in HubSpot, it will populate each HubSpot
property using the value in the corresponding Unify field. However, you can also
specify *default values* to be used as a fallback. This can useful in a few
different scenarios:

1. You may have custom fields in HubSpot that require a value
2. You may want to write a custom value to a field that is not available in the
   field mappings
3. You may want to dynamically set a value in different Plays or Play actions

You can set global default values from [Settings -> Integrations -> HubSpot](https://app.unifygtm.com/dashboard/settings/integrations/hubspot).
These will be used for all writes to HubSpot unless overridden in a Play or by a
field mapping.

<Frame caption="Set global default values on a per-field basis.">
  <img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=aaa689bbc60b7a8d96ef4294044b814a" data-og-width="2304" width="2304" data-og-height="1571" height="1571" data-path="images/reference/integrations/hubspot/default-values.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=f8595b78abe9cec841b9b341cad7b7bc 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=156578b3d0b21623cfccebff86a0c185 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=8d2e877576e45a7d3f668f1ab42bab0c 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=533989b50347e9e6cd3dbcf537090c70 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=40e26b62cec9048074a62941e9b91a8c 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/reference/integrations/hubspot/default-values.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b1a95246e5eb7557efde6323b13cfaf8 2500w" />
</Frame>

To learn how to set default values at the Play level instead, see the [Sync to HubSpot](/reference/plays/actions#sync-to-hubspot)
action reference.
