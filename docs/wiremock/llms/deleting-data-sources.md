# Source: https://docs.wiremock.io/data-sources/deleting-data-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Deleting Data Sources

> How to remove data sources from your account

## Deleting a Data Source

Data sources can be deleted from your organisation. To delete a data source:

* Navigate to the [Data sources page](https://app.wiremock.io/data-sources).
* Click on the delete icon for the data source you want to remove.

<p>
  <img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=2b43075e5e9ee32ce5e41e1b1ee0f542" alt="Delete a data source" title="Delete a data source" data-og-width="662" width="662" data-og-height="464" height="464" data-path="images/screenshots/data-sources/delete-data-source.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=0f81d616132d1f70c7906d6ba041fc1b 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=28b92645b71e09282c6873fad7ca4c87 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=5d1530fcc0333e658a99a5052943b8ff 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ba3ea9477d5e8f83c1d1fd813fbb947f 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=e01d7acad5932dfebbd91eb39c00748f 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=2ea57e3569c41860ec3b2c74c28b0aa3 2500w" />
</p>

Clicking on the delete icon will open a confirmation dialog. Click the `Confirm` button to confirm the deletion or
`Cancel` to close the dialog without deleting the data source.

<p>
  <img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7f14d6ba4b5328766941a023127c58b8" alt="Delete data source confirmation" title="Delete data source confirmation" data-og-width="667" width="667" data-og-height="252" height="252" data-path="images/screenshots/data-sources/delete-data-source-confirmation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ca0f074f57d21b9c089292a8961139d9 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=293161cb2543324682b01368d5bcee8a 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=0a8e48226d4de70c726c04d76147265d 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7fbce4b40b881936335fc27f2f39e235 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=49cd1b7d5fa5d6fc7cdcc9afaead36e3 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-confirmation.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=025815fe2b91ff01aecee1ecc20dd98b 2500w" />
</p>

Clicking `Confirm` will delete the data source, but it will not remove the data source from any stubs that are using it.
These stubs will continue to reference the deleted data source, but will act as if no data was returned when the data
source is queried. See below for more details on stub matching and response templating when a data source is deleted.

When a data source is deleted, any data source limits you may have reached will be re-evaluated. If you have any
disabled data sources, they will be re-enabled if you now have available capacity within your data source limits. You
can read more about [plan limits and disabled data sources here](./plan-limits).

Any stubs that are using the deleted data source will now have a warning message displayed on the stub informing you
that `The data source that this stub was referencing no longer exists.`  You will also see a warning icon next to
the data source summary in the stub form.

<p>
  <img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f33f9cc4db8bea01f7a0a3c9661f0ef2" alt="Data source stub warning icon" title="Data source stub warning icon" data-og-width="409" width="409" data-og-height="183" height="183" data-path="images/screenshots/data-sources/delete-data-source-stub-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ccee93ae5feb90a4fd907b8b44f22798 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d08065216f6ef6c47aa6558d08fa6dfd 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=99e0245c77da2a7e3bbbdd89f9524fd4 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f09438c0eedeff810c307ea437d275c9 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=625fa46de2a8cccf32807af74582f871 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-icon.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=cb6d26a84befdb320bacd3fcf66922cc 2500w" />
</p>

If you have other data sources within your organisation you can attach one of these to the stub to replace the deleted
data source. If you do not have another data source that you can use, you will need to update the stub to remove the
reference to the deleted data source.

You can do this by clicking on the delete icon next to the data source in the stub form.

<p>
  <img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=271956367e5f40a91176e2fb2d402556" alt="Delete data source stub warning" title="Delete data source stub warning" data-og-width="1001" width="1001" data-og-height="344" height="344" data-path="images/screenshots/data-sources/delete-data-source-stub-notice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f2119adaadfafcad267718bb2d8f0da2 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=8189da81f085cdd915f98aad7bd0c914 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=dec9087056c2ddbe6dd639726555d394 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=b645dca43c36cf9ef1f9f48bdd0a49bf 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=dd82f0ccf6aff390fdbfd7ca811e2f86 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/delete-data-source-stub-notice.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=22056ed1b54df76fc3dfb492ae136f5b 2500w" />
</p>

### Stub Matching

If a stub is using a data source that has been deleted, the stub will no longer match incoming requests if the
`Matches stub only if data is found` tick box is checked on the Stub form. If this tick box is not checked, the stub
will continue to match incoming requests, but the data source will not be queried.

### Data source response templating

If a data source is deleted, any response templates that are using the data source will no longer be able to access the
data source data. The response template will still be rendered, but the data source data will not be available.
