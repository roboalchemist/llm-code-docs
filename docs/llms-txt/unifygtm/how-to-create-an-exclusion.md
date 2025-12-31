# Source: https://docs.unifygtm.com/tutorials/how-to-create-an-exclusion.md

# How to Create an Exclusion

> Prevent Unify from actioning on specific companies or people.

1. Excluding current customers
2. Exclude people who have unsubscribed from outbound campaigns

## How to create an exclusion

Let’s walk through how to exclude all Active Salesforce accounts.

### 1. Go to Exclusions in Settings

Navigate to [Settings > Exclusions](https://app.unifygtm.com/dashboard/settings/organization/exclusions) and click `New exclusion`

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=845a080c7721d5f7fe40346ef6d7d8d2" alt="Exclusions 1.png" data-og-width="2000" width="2000" data-og-height="1072" height="1072" data-path="images/49.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=532d5fff3ddfd64d71af29056b9e74d6 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=6ba8f95fe6ce78961e25a7f462b0e0d2 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=d07511e3e0f012ef76f938243473ed02 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b3ef267b0e0e5944f16af9507b561d8d 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=cf502fd2dcc3cb1bcab63c3f64429b93 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/49.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=e1c0d7b3c5cec3456d1a7d0fa44b0335 2500w" /></Frame>

## 2. Select Companies or People

Select `Companies` in this case

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=282fa34dd20b99f5612b70c9971544d4" alt="Untitled" data-og-width="2000" width="2000" data-og-height="1070" height="1070" data-path="images/50.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b5bea2b48c375b79ed49e633676b8c8d 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=5a527600534a520896c7738ee94fa565 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b2e5c59fce112c8499ca782247eae15d 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=c335a8af79e893bd973123c5344e4cdd 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=ee3b230678279ab16606abfe6f7b197c 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/50.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=27d74d1b0670c039ab1b36b3947858af 2500w" /></Frame>

## 3. Define criterion to filter

In this example, we’re creating an exclusion called `Current Customers` that excludes companies with Salesforce `Account Status` equal to `Active`

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=49da7ff94d49ccb761f25da55bc2f558" alt="Exclusions 2.png" data-og-width="2000" width="2000" data-og-height="2069" height="2069" data-path="images/51.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=28a2bca511b10431aa57c7cbe1b262cd 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4c15a9192bc040d2da38884fa35b7bbf 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=772befa106f43f8e046e7377a64a3af3 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=03e674cfae3ed4535033439b149067cf 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=4ec850505735d3537b1992b85ed485a1 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/51.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=6c6a5e3ecf999d335279f0185071147d 2500w" /></Frame>

## 4. Hit Save

Here you’ll see an overview of your new exclusion. These lists will automatically be excluded from targeting.

<Frame><img src="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=5f8049145d8c1e9fe72e6d09a4e6064a" alt="Exclusions 2.png" data-og-width="2000" width="2000" data-og-height="1077" height="1077" data-path="images/52.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=280&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=8fa09380d3ef8860d43e26ae7243aab6 280w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=560&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=23dce421576b5f6fc29ceb3e638f45c7 560w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=840&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=b4b10bedc60fa86a8a2c55d8ea0144ff 840w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=1100&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=115b0c00106f2002216890bd2b5206ad 1100w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=1650&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=cc939bf1aeef4ec04c0b4813694d79c3 1650w, https://mintcdn.com/unify-19/4OhjWaiyXHWcw8Ko/images/52.png?w=2500&fit=max&auto=format&n=4OhjWaiyXHWcw8Ko&q=85&s=47f55c8d43e176f9f2d169e62668ed1d 2500w" /></Frame>

## Upload exclusions from a CSV

Let's walk through how to set up an exclusion using a CSV of companies or people.

### 1. Create a column in your CSV called "Status"

Populate the "Status" column with the same value across all the rows in your CSV. This value usually indicates the type of contact you are excluding. Examples can include "Active Customer", "Competitor", etc.

### 2. Upload these contacts in the companies or people tab

If you're uploading companies, you'll need to include both the company name and domain. If you're uploading people, you'll need to include one of the following set of fields:

* Email
* First Name, Last Name, and Company Domain
* LinkedIn URL

### 3. Map the CSV fields to the Unify fields

You'll select the fields you want to map into Unify. Make sure to select "Status" field from Unify when mapping that same column from your CSV. The Unify "Status" field should then populate with the values you populated in the CSV under the column. Once these are mapped, you can finish the upload.

### 4. Create a new exclusion and add the "Status" field in the conditions

You'll then switch over into the "Exclusions" tab in your settings and create a new exclusion. Under either the people or companies filters, you will select the Unify status column and add the value from your CSV (i.e. "Active Customer"). Once you save this exclusion, this list should be excluded from future audiences and Plays moving forward!

***

Note that if you would like to add more companies or contacts to this exclusion list in the feature, you'll need to follow the same process as above and make sure the "Status" field is correctly mapped. This should automatically pull in the new exclusion after uploaded if the "Status" value is the same value in the filter.
