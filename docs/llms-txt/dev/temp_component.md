# Source: https://dev.writer.com/home/temp_component.md

# Column test

export const DynamicImage = ({type}) => <div>
        <img src={`/framework/public/components/${type}.png`} />
    </div>;

export const description = "A layout component that organises its child components in columns. Must be inside a Column Container component.";


export const component = {
  type: 'column'
};


export const writer = {
  name: "Column",
  description,
  allowedParentTypes: ["columns", "repeater"],
  allowedChildrenTypes: ["*"],
  category: "Layout",
  fields: {
    title: {
      name: "Title",
      type: "Text"
    },
    width: {
      name: "Width (factor)",
      default: "1",
      init: "1",
      type: "Number",
      desc: "Relative size when compared to other columns in the same container. A column of width 2 will be double the width of one with width 1.",
      category: "Style"
    },
    isSticky: {
      name: "Sticky",
      default: "no",
      type: "Text",
      options: {
        yes: "Yes",
        no: "No"
      },
      category: "Style"
    },
    isCollapsible: {
      name: "Collapsible",
      default: "no",
      type: "Text",
      options: {
        yes: "Yes",
        no: "No"
      },
      category: "Style"
    },
    startCollapsed: {
      name: "Start collapsed",
      type: "Text",
      category: "Style",
      default: "no",
      options: {
        yes: "Yes",
        no: "No"
      },
      desc: "Only applied when the column is collapsible."
    }
  }
};


## Fields

<p>
  {description}
</p>

<DynamicImage type={component.type} />

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Options</th>
    </tr>
  </thead>

  <tbody>
    {Object.values(writer.fields).map((field, index) => (
            <tr key={index}>
                <td>{field.name}</td>
                <td>{field.type}</td>
                <td>{field.desc || 'N/A'}</td>
                <td>{field.options ? Object.values(field.options).join(", ") : 'N/A'}</td>
            </tr>
            ))}
  </tbody>
</table>

## Low code usage

This component can be declared directly in Python, using [backend-driven UI](/framework/backend-driven-ui).

```python  theme={null}
ui.Column(content={
        "title": "", # str 
        "width": "1", # Union[float, str] 
        "isSticky": "no", # str [yes, no]
        "isCollapsible": "no", # str [yes, no]
        "startCollapsed": "no", # str [yes, no]
        "separatorColor": "", # str 
        "contentPadding": "", # str 
        "contentHAlign": "", # str 
        "contentVAlign": "", # str 
        "cssClasses": "", # str 
    }
)
```
