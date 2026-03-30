# Source: https://docs.axonius.com/docs/servicenow-showing-adv-settings-json-fields-in-basic-view.md

# ServiceNow - Showing JSON Fields in Basic View

<HTMLBlock>
  {`
  <style>
  .rm-Markdown .img img {
    float: none !important;  
  }
  </style>
  `}
</HTMLBlock>

<br />

You can configure fields that generally appear in JSON to appear in Basic view. Configure for Devices, Business Applications, Databases and Users separately as required. Use the plus sign to add an entry to each field. The system validates the content you enter.

<br />

<Image align="left" alt="AdvancedFieldsBasic" border={true} width="500px" src="https://files.readme.io/24dc07e9c742b90178faa7e1afe4872c2b4c2f546fd55d35db44bc07b7b2b706-image.png" className="border" />

<br />

<Image align="left" alt="ServiceNow JSONFieldsBasic Users" border={true} width="500px" src="https://files.readme.io/ddf5e313b889483227b7917cd10b8c45af34c9314110941d88bc30567985a767-image.png" className="border" />

Enter fields in the following JSON format:

```json
[
  {
      "label":"My First Field", 
      "raw_field": "field_a",
      "field_type": "str"
  },
  {
      "label":"My Second Field",
      "raw_field": "field_b",
      "field_type": "int"
  },
  {
      "label":"My third Field -  Application Name",
      "raw_field": "application/name",
      "field_type": "str"
  },
  {
      "label":"My third Field -  Application Number",
      "raw_field": "application/number",
      "field_type": "int"
  }
]
```

* **label** - the name for the field you want to appear in the basic view
* **raw\_field** - the name of the field as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table)
* **field\_type** -the field type as  it appears in JSON format. The following field types are supported. int, string, datetime, float, bool. You can write them in the following ways:

  `'int', 'string', 'str', 'date', 'datetime', 'float', 'bool', 'boolean'`