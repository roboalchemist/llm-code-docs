# Source: https://docs.unifygtm.com/reference/integrations/hubspot/property-options.md

# Property Options

> Find the options for a property in HubSpot.

# Explanation

Properties in HubSpot have a different name displayed in the UI than the value
used at the API level. For most properties, the dropdown options you see in the
UI will be the same as the values you see in Unify.

However, certain properties in HubSpot have options which Unify cannot access.
At the moment, this is a known HubSpot limitation. The steps outlined here can
help to work around the issue.

## Workaround

In order to support using these options for filtering in audiences and
exclusions, you can perform the following steps. This article uses the
**Lifecycle Stage** property on **Company** as an example, but the same steps
should work for other properties and objects.

In HubSpot, navigate to **CRM -> Companies** and select **Actions -> Edit properties**.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1921ca6a6c8d55cbe9d43acfda23c093" alt="Properties" data-og-width="3298" width="3298" data-og-height="1714" height="1714" data-path="images/hubspot-15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cb84e181083f2a5aa6e1d050b061f50c 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=34fd18fd3ff5007da248bb9a7917f662 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b7af8a6eaa29372d0bc23cc0357af5eb 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=55d3b96a59c51c3589af704058b58996 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e037c750bd4283be6e54094508de2015 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-15.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=55f96b586d13b40ba54922318ac7b127 2500w" /></Frame>

Search for the property by its name (in this case, **Lifecycle Stage**) and
select the property.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=519d64e0d1ec74d5a7d96e410ba61329" alt="Properties" data-og-width="3302" width="3302" data-og-height="1714" height="1714" data-path="images/hubspot-16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=136d46eea58da98c324d552bebfe8696 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e17ad0bb1f63e7b81e927f77d51f80fb 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b9b5a6678ff7d622bc2c46b6604e4543 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1aa4aedb46d2347fdfb91a45c702c9bb 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=272408e3a45c8334a94692c47a1b5d71 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-16.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=5b33588249be5ece6a58f94f036cce7b 2500w" /></Frame>

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=0d963831c638fb28c9225523fb8c5152" alt="Lifecycle Stage" data-og-width="3298" width="3298" data-og-height="1792" height="1792" data-path="images/hubspot-17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=1b9529099ee842f5a418e94457890137 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=97a854999d38b97118510c700404474b 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b2608ac2ef23901d301d3346f471dbc2 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=4f464626c9348d5455a68d895317ddbe 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=cea16da7f9e709328f9bbf75596b6f2b 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-17.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=908021c15ba68f3bdd212fa05aee1974 2500w" /></Frame>

Navigate to **Field type**. You will see a list of options, with **LABEL** and
**INTERNAL NAME** values alongside the number of records that have that value.
You may want to copy these values to a secure separate location for easy future
reference. If you wish to filter records in Unify to a specific **LABEL** value,
you can do so by using the corresponding **INTERNAL NAME** value.

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=7528480a7063625b527e922cc47e7cdc" alt="Property Options" data-og-width="3298" width="3298" data-og-height="1786" height="1786" data-path="images/hubspot-18.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=071d437228946b1005d30fba272c56df 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ee6268904afc051100a16e51e37ddb7d 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fa926371f1a86f89e5a62da4f679a314 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=b9befe41a4c33178cd771f1fdaae0faa 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=ae5eb877ea8b9fbd522428c47700fcda 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-18.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=935e6d8848a6824f39a35b887b79c9ad 2500w" /></Frame>

Here's what that looks like in Unify for the **LABEL** value "Lead" and
therefore **INTERNAL NAME** value "lead":

<Frame><img src="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=d215e8246b62ba7121cd5b390cb3634b" alt="Filtering in Unify" data-og-width="2162" width="2162" data-og-height="1344" height="1344" data-path="images/hubspot-19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=280&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=fc07816aded5d8d2282800d8df4afbbd 280w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=560&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=e6e3fd5ca0ea1a83bbb3aee4c69a12af 560w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=840&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=813d146fbd8b2f32a2e0eb79299246a1 840w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=1100&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=82a9f4aab37b80ebc14935910b3084d5 1100w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=1650&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=68951146227379c3d98fe99bc6e29ac4 1650w, https://mintcdn.com/unify-19/Y_pp7r30tEdafKDG/images/hubspot-19.png?w=2500&fit=max&auto=format&n=Y_pp7r30tEdafKDG&q=85&s=a4c07b50efe8e6f61b5591c7d433bdfe 2500w" /></Frame>
