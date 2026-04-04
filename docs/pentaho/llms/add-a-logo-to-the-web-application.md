# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-the-pentaho-user-console/add-a-logo-to-the-web-application.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/add-a-logo-to-the-web-application.md

# Add a logo to the web application

You can customize the Pentaho web application to display a logo. The best way to do this is to edit the `Mantle.jsp` file in the `pentaho/server/pentaho-server/tomcat/webapps/pentaho/mantle/` folder.

In this example, the logo is added to the header on the right, but you can add it to the left or as a banner on the top or bottom of the page.

```xml
<div id="pucWrapper" cellspacing="0" cellpadding="0"  style="width: 100%; height: 100%;">
        <div id="pucHeader" cellspacing="0" cellpadding="0">
		...
		<div id="logo" style="float: right; padding-right:10px"><IMG src="mantle/logo.png"></IMG></div>
		...
```

The `logo.png` is used as the graphic within the `pucHeader` div.
