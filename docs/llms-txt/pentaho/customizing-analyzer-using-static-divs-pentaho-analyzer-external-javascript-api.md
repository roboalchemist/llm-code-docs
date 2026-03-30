# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/customizing-analyzer-using-static-divs-pentaho-analyzer-external-javascript-api.md

# Customizing Analyzer Using Static Divs

To allow for customization of the Analyzer report view, divs have been added to certain attach points in the application. This allows users who embed Analyzer to have the ability to programmatically customize the application. Each div has its own hard-coded ID for retrieval using any means of DOM manipulation.

## List of Available Divs

The following is a list of the available divs with examples.

## Toolbar Div

This div is located on the Analyzer toolbar. It allows for the addition of new buttons and customization of existing buttons on the toolbar.

```javascript
<div class="reportBtn" id="analyzer-custom-btn"></div>
Code Sample:
<script type="text/javascript">
 
function changeText(text)
{
elem = document.getElementById('analyzer-custom-btn');
elem.innerHTML = "My New Button";
}
</script>

```
