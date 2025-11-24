# Source: https://www.aptible.com/docs/how-to-guides/platform-guides/scim-okta-guide.md

# Provisioning with Okta (SCIM)

> Aptible supports SCIM 2.0 provisioning through Okta using the Aptible SCIM integration. This setup enables you to automate user provisioning and de-provisioning for your organization.

With SCIM enabled, users won't have the option to leave your organization on their own, and won't be able to change their account email or password. Only organization owners have permission to remove team members. Only administrators in Okta have permission to use SCIM to change user account emails if they're associated with a domain your organization verified.

> 📘 Note

> You must be an Aptible organization owner to enable SCIM for your organization.

### Step 1: Create a SCIM Integration in Aptible

1. **Log in to Aptible**: Sign in to your Aptible account with OrganizationOwner privileges.
2. **Navigate to Provisioning**: Go to the 'Settings' section in your Aptible dashboard and select Provisioning

<img src="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=5260a9ef9a9db23bb071b37d227c3f4a" alt="" data-og-width="2798" width="2798" data-og-height="1610" height="1610" data-path="images/scim-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=280&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=071934bf1f70707bafb512a0cd4ae747 280w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=560&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=824ed9af14a135f5150b6d3a69185cd3 560w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=840&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=54b811abcf11736862deaa76eeaaab5b 840w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1100&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=fb58221cd08909817daaeaa58d5e7630 1100w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=1650&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=30b6e5063e17a311d283de916ad069c9 1650w, https://mintcdn.com/aptible/RWSo_H5DBAoWcXSD/images/scim-app-ui.png?w=2500&fit=max&auto=format&n=RWSo_H5DBAoWcXSD&q=85&s=e9b2db705777beebe884e66910bcf195 2500w" />

1. **Define Default Role**: Update the Default Aptible Role. New Users created by SCIM will be automatically assigned to this Role.
2. **Generate SCIM Token**: Aptible will provide a SCIM token, which you will need for the Okta configuration. Save this token securely; it will only be displayed once.

> 📘 Note

> Please note that the SCIM token has a validity of one year.

3. **Save the Changes**: Save the configuration.

### Step 2: **Enable SCIM in Okta with the SCIM test app**

The [SCIM 2.0 test app (Header Auth)](https://www.okta.com/integrations/scim-2-0-test-app-header-auth/) is available in the Okta Integration Network, allowing you to enable user provisioning directly through Okta.

Prior to enabling SCIM in Okta, you must configure SSO for your Aptible account

To set up provisioning with Okta, do the following:

1. Ensure you have the Aptible SCIM token generated in the previous step.
2. Open your Okta admin console in a new tab.
3. Go to **Applications**, and then select **Applications**.
4. Select **Browse App Catalog**.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=41c98723835d797a3a5bc23a98226a89" alt="" data-og-width="2670" width="2670" data-og-height="964" height="964" data-path="images/okta-select-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7d699e9f66b13e4ce502482664a84274 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b08e741f57ac7a9ab0c10c0ec0b37d43 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=36b59c184bf50a556381227330f26fba 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ed8ec5b70a631e7ad080702c0b6e79a5 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=568df4214380920b6d4c5f316a4ec53f 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-app.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7fe1c1e9adcab209a8b2fc2e9b0fea71 2500w" />

5. Search for "SCIM 2.0 Test App (Header Auth)". Select the app from the results, and then select **Add Integration**.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7c9d9bec82d1fe529f4b42fde9e440ef" alt="" data-og-width="2312" width="2312" data-og-height="1148" height="1148" data-path="images/okta-select-scim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=4baa93b8097f1c7b93beb4cf6735bda8 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6b40e6285ebe3aeb3794f56f5c90c5cb 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a2767821fe0606d649385b733c0d90b9 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2aebff838a0674fc46d2e7ebab2abf06 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ae45240e03cf288177ec06453e43a12e 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-select-scim.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=8cc3ac3bac7b670a7f80efe293c1ed21 2500w" />

6. In the **General Settings** tab, enter an app name you'll recognize later, and then select **Next**.
7. In the **Sign-On Options** tab, select **Done**.
8. In Okta, go to the newly created app, select **Provisioning**, then select **Configure API Integration**.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=8aef2726ad14bcbe8a9aa9f1e8772752" alt="" data-og-width="2008" width="2008" data-og-height="696" height="696" data-path="images/okta-enable-scim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2554d383cde9140ed6eb3691c16b7590 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5d406ef2162090fbc05f2f8bee32d823 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ebb644776e92da2e07740af36b3f8515 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=dde2eed0b6537eb19c30d4c1d8cf90d4 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=55500fb6fd5183fc6110556e67495108 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-scim.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6ab8c3bfda55d5e897cd4571c789236d 2500w" />

9. Select **Enable API integration**, and enter the following:
   * **Base URL** - Enter `https://auth.aptible.com/scim_v2`.
   * **API Token** - Enter your SCIM API key.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=cf836738e506b101b1a99e80a00654c2" alt="" data-og-width="3912" width="3912" data-og-height="2312" height="2312" data-path="images/okta-configure-scim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c6bf0f2dcb1c4e5f9d28db3b4a979cb5 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=0af00326f834adc06aab12b6afbb30bf 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=71d0cad87e0662845f5a1a003a31c45f 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=64f851e716c71342489d245a827b0fb2 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=edb90896b672468a9f166ebea200be42 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-configure-scim.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9108e2dd511aa0fda7718598e44c4d99 2500w" />

10. Select **Test API Credentials**. If successful, a verification message will appear.

    > If verification is unsuccessful, confirm that you have SCIM enabled for your team in Aptible, are using the correct SCIM API key, and that your API key's status is ACTIVE in your team authentication settings. If you continue to face issues, contact Aptible support for assistance.
11. Select **Save**. Then you can configure the SCIM 2.0 test app (Header Auth).

## Configure the SCIM test app

After you enable SCIM in Okta with the SCIM 2.0 test app (Header Auth), you can configure the app. The SCIM 2.0 test app (Header Auth) supports the provisioning features listed in the SCIM provisioning overview. The app also supports updating group information from Aptible to your IdP.

To turn these features on or off, do the following:

1. Go to the SCIM 2.0 test app (Header Auth) in Okta, select **Provisioning**, select **To App** on the left, then select **Edit**.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=23dcb8bf19d8219decaf0bab7e6171e5" alt="" data-og-width="2026" width="2026" data-og-height="1328" height="1328" data-path="images/okta-enable-crud.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=9537c98257f479c139992156a8507353 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b5e1aae7222ea49399bbfb6818c35860 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d1e7442b92b06a78f8915bcb49db689c 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=7ca444bbc811e0cb5501d88b08479fae 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6d3aec5c1bdca8eb8861b10af9433db0 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-enable-crud.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=52488d6fd7de3129e51039a96f88d33a 2500w" />

2. Select features to enable them or clear them to turn them off. Aptible supports the **Create users**, **Update User Attributes**, and **Deactivate Users** features. It doesn't support the **Sync Password** feature.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=66e467d52bc649df134f55b61e940f27" alt="" data-og-width="2046" width="2046" data-og-height="1780" height="1780" data-path="images/okta-crud-enabled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=6209cd9ab1d4b4a4f2d9d10ce6e4a517 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=952720b5d1625a1f78324d50a2b45409 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=d4533c09bfd406911a058cc27c82db41 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=76ca4c56f7b8b59eb40980328909fb46 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=5954f1e97537df93b3bd588737c2949d 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-crud-enabled.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=125e41d9650f32a28cdd5f342ed52f2b 2500w" />

3. Select **Save** to save your changes.

4. Make sure only the **Username**, **Given name**, **Family name, and Display Name** attributes are mapped. Display Name is used if provided. Otherwise, the system will fall back to givenName and familyName. Other attributes are ignored if they're mapped.

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f588742c39cac3c236b6a980de89e709" alt="" data-og-width="1524" width="1524" data-og-height="588" height="588" data-path="images/okta-attributes-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=cfe424911008638d3a95eaea3a1ac0db 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=8d168f2b426435d3417a5c76cae222dc 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=f298f0c5740ecbd16a7a8f6157feea1b 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=a29576ab4e3a4060be56e2d1e7598014 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=61cdb469a5952be83b41a24a76b6feb2 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-attributes-mapping.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=b36b77b9d90d63981fe33d7a3958a935 2500w" />

5. Select **Assignments**, then assign relevant people and groups to the app. Learn how to [assign people and groups to an app in Okta](https://help.okta.com/en-us/content/topics/apps/apps-assign-applications.htm?cshid=ext_Apps_Apps_Page-assign).

<img src="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=c4bf9f2869fbe09acd781f35b3e72013" alt="" data-og-width="1476" width="1476" data-og-height="1074" height="1074" data-path="images/okta-initiate-assignments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=280&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=346a48d22af6e733ae81dfba90a5c453 280w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=560&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=ca013b045e4abaa120e1231c42d8653b 560w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=840&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=bcfc0a221a648a38a3e2b867857a40cb 840w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=1100&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=2fb5e429a4cf20a9b2392b5dc0a2fbcb 1100w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=1650&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=41a366383f79994fd3936a61ad467ca4 1650w, https://mintcdn.com/aptible/opX5eNKf32ujRi0n/images/okta-initiate-assignments.png?w=2500&fit=max&auto=format&n=opX5eNKf32ujRi0n&q=85&s=510a574ebb7b45fb1b4840c3080bbbb9 2500w" />

## Step 3: Validate the SCIM Integration

1. **Validate User Provisioning**: Create a test user in Okta and verify that the user is provisioned in Aptible.
2. **Validate User De-provisioning**: Deactivate the test user in Okta and verify that the user is de-provisioned in Aptible.

By following these steps, you can successfully configure SCIM provisioning between Aptible and Okta to automate your organization's user management.
