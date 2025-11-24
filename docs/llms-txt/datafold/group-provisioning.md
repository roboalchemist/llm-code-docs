# Source: https://docs.datafold.com/security/single-sign-on/saml/group-provisioning.md

> Automatically sync group membership with your SAML Identity Provider (IdP).

# null

## 1. Create desired groups in the IdP

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7b1a4b911b31f70a7d7db3b95739586c" data-og-width="2206" width="2206" data-og-height="1138" height="1138" data-path="images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=ea9ebef6fb14013d8e93b161c30a1c0f 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5d9c07e5cf547a9638b5c766696d95bd 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=7fd3d8be8c721165c57b80f415645e71 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=2c0eef63671955ee29df544c44c0be8a 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6ca9d7d82602d721f63b1b73bdb20a70 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/okta_groups-61f1b6cf7b4075477ff1275ceeea6d09.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=0234e8f1489f0f5e752db118555790b5 2500w" />
</Frame>

## 2. Assign the desired users to groups

Assign the relevant users to groups reflecting their roles and permissions.

## 3. Configure the SAML SSO provider

Configure your SAML SSO provider to include a `groups` attribute. This attribute should list all the groups you want to sync.

```Bash  theme={null}
  <saml2:Attribute Name="groups" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified"><saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">datafold_admin</saml2:AttributeValue><saml2:AttributeValue xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">datafold_read_write</saml2:AttributeValue></saml2:Attribute></saml2:AttributeStatement></saml2:Assertion></saml2p:Response>
```

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7754980607aca71912bd8372bd5500a4" data-og-width="1536" width="1536" data-og-height="580" height="580" data-path="images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0cb877d6a9f30c6c6ec70faa455c783c 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5b77cb7d1f4495562e6ee8878fc4ff60 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=52e4c47f3d047b82818692b39cd9afd2 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e00c227f7a09d308161b6b9420cb21db 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=53a08b08ee61f52f31390974cb5c63e0 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/saml_groups_attribute-00b426150ceab3149d619b067aee26fc.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=4f4c1fb489b45a227cf379b42065ab2c 2500w" />
</Frame>

## 4. Map IdP groups to Datafold groups

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=30af41ee0d9f1d6d35f0f5103e7df359" data-og-width="1534" width="1534" data-og-height="828" height="828" data-path="images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=aafe7736b71c01e627d381a3a92c86e5 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=95366201a0c794119c68cff9a4bf0152 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6799569133c31debca635d36199a38e 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2cf8a00fba05fd8832e016c6f636cd91 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9ab032dd79103de6d0d03629277a117b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_group-f66ae2d5b9f378e444f70d1b5851dfaf.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9e9ba0246f56f34ca8ee3fdd2a891000 2500w" />
</Frame>

The `datafold_admin` group, created in the IdP through [step 1](#1-create-desired-groups-in-the-idp), will be automatically synced. Users in this IdP group will also be members of the corresponding group in Datafold.

**Note:** Manual Datafold user group memberships will be overridden upon the user's next login to Datafold. Therefore, group memberships should be managed exclusively within the IdP once the `groups` attribute is configured.

## Example configuration

Here's how you might configure three groups to map to the three default Datafold groups, `admin`, `default` and `viewonly`:

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c2f082b931c0619c6c740eb0269f2a48" data-og-width="1934" width="1934" data-og-height="758" height="758" data-path="images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9615a1b078a16f35ccdefadf3ef858ad 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3244a994952564cdbdda2f48bb3bc5c9 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c83f2424d4872e9da9b7e613a5a3b95a 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b68cfadcee9109ac44efea44bec022e4 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4efb937d6fda70251701bcb3e0960e0e 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/datafold_groups-5e7f4e7afb9d99dee113a03b8599040a.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b1573c190d7ce95d53bb126532c0c02e 2500w" />
</Frame>
