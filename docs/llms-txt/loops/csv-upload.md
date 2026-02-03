# Source: https://loops.so/docs/add-users/csv-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CSV Upload

> Easily add contacts to Loops by uploading a CSV file.

## Add new contacts via CSV

1. Select **Import** in the top right of the [Audience](https://app.loops.so/audience) page.

   <img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a2258dda1a3f0dfc2cb54f2659baf717" alt="" data-og-width="2280" width="2280" data-og-height="944" height="944" data-path="images/select-import-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1bb0e37853c22a71e914fbe1dcd04273 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=b5141dc9f08887c485d55e6cdebdfb9c 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=604a70f75dbc1b5fbc2205eba89201ac 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=5e4b48325ffac9aaff2baec53da52262 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d6ef329ae992515f1ccc0401664237b3 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/select-import-users.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=e1f45df944c09c63abe3764ace27868f 2500w" />

2. Hover on **CSV** and click **Upload CSV**. Download the [example formatted CSV](https://app.loops.so/loops_sample.csv) to get an idea of the columns we use. By default, we recommend using at least `Email`, `First Name`, `Last Name`, `User Group` and `Source` columns.

   <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f68da4c81e81193b87d77ab41ffc9d4e" alt="" data-og-width="1520" width="1520" data-og-height="1247" height="1247" data-path="images/import-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=041fa2852c0355cfe0c18576f35304f6 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=82154329482626b7436b8c222c738638 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=869f983532cb6f1f79ce14601d5f28ff 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9bc74f602357362086a1a91646fe94ef 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=81850b75bfb304519f6cfac51ddeb764 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/import-users.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=be9406c2e596c03ab7caa57d112e72a9 2500w" />

3. After uploading the CSV you'll have a chance to review any duplicates or missing information before finishing.

4. When the upload is finished, all the uploaded contacts can be viewed in the Audience page. That's it! 🎊

## Update contacts via CSV

You can also upload a CSV file to update your existing contacts in bulk.

You can either download a CSV from your Audience page in Loops, edit the data and re-upload it, or start with a new CSV file and just include the contacts and columns you want to update.

When updating contacts, Loops will first look for a matching contact using the value in the `User ID` column, then the `Email` column.

If a contact is found, Loops will update the contact using the data provided in the CSV file. If a contact is not found with either `User ID` or `Email` values, a new contact will be created using the data provided.

Note: If a contact is found using `User ID` and its email address does not match the provided `Email` value, the contact will not be updated and an error will be recorded.

## Trigger loops via CSV

You can use CSV uploads as a way to trigger loops on a group of new or existing contacts.

If you want to trigger loops for existing contacts, download a CSV from your [Audience page](https://app.loops.so/audience) then re-upload the file. Only include the contacts you want to trigger loops for in the CSV file.

After uploading the CSV, on the Review page select the **Trigger Loops** option. This will trigger all applicable loops you have set up with **Contact created** and **Contact updated** triggers.

If you select to add contacts to mailing lists on this same page as well as toggle **Trigger loops** ON, you will also trigger **Contact added to list** loops.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=15a27f0fbfbc0c5308ad9454e8f31d0c" alt="" data-og-width="2280" width="2280" data-og-height="1242" height="1242" data-path="images/csv-trigger-loops.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=571e1e50ac8999b917f4adff5a24ad7d 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=bb187f15d0937725397ddc04a8aef8a6 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=1c6d569826bac3d811869de7ee55fd89 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=098c752663a672893c03346397572a67 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b739497d09dc7853de7a1a6d6c5bfb81 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/csv-trigger-loops.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=468937d6d073e0d8ae96eef9eff9631b 2500w" />

## View previous CSV uploads

After uploading CSV files you can view a history of your uploads plus details for each file's rows.

On the [Audience page](https://app.loops.so/audience) click **Import contacts**, hover on **CSV** and click **Upload CSV**. On the next page click on **View imports**, which will show you a list of all of your past uploads.

Clicking on one of your uploads will let you view lists of all new, updated or duplicated contacts plus a list of any errors from the import.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b4491c021fc049fa4a280e439692949d" alt="" data-og-width="2280" width="2280" data-og-height="1419" height="1419" data-path="images/csv-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=aad4cea1c8ed2134190b940c13bab8c1 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=39c84097f9b261928c21297754d35e6e 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=960675817e9ae2fe8b12a26ecb4f9125 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6874981db9ea7a2861ed5f55a247b204 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=afaf8f6540caf2d46603db46c8d34204 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/csv-history.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=be9ee5cd8c6517d5fb9564cc6667b90b 2500w" />

## Important notes

* All contacts uploaded will be automatically marked as subscribed. If you want to mark imported contacts as unsubscribed add a "Subscribed" column into your CSV file and use `false` as the column value.
* The importer does not re-subscribe contacts who are marked as unsubscribed in your Audience.
* The default `Source` value for each uploaded contact will be "CSV Upload". You can change this by adding a `Source` column to your CSV file and specifying a custom value.
* Cells that are empty in the CSV file will not overwrite existing data in Loops. If you want to clear a field, you will need to provide a value of `null` in the CSV file (4 characters, all lowercase).
