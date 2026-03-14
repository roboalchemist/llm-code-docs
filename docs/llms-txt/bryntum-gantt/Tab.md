# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Tab.md

# [Tab](https://bryntum.com/docs/gantt/api/Core/widget/Tab)

This widget class is used to present items in a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) on its [tabBar](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar). A reference to this widget is stored via the [tab](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-tab) config on the tab panel's items.

```
new TabPanel({
    appendTo : targetElement,
    height   : '25em',
    items    : {
        profile : {
           title : 'User profile',
+          tab : {
+                icon : 'fa fa-user',
+          },
           items : {
                firstname : { type : 'text', label : 'First name', style : 'margin:2em 1em' },
                surname  : { type : 'text', label : 'Last name', style : 'margin:2em 1em' }
            }
        },
        settings : {
            title : 'Settings',
+           tab : {
+               icon : 'fa fa-gear',
+           },
            items : {
                infoWidget : {
                    type  : 'widget',
                    style : 'padding:1em',
                    html  : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                }
            }
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[active](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-active)
This config is set to `true` when this tab represents the `activeTab` of a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). It is managed by the tab panel and should not be set directly.

[index](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-index)
This config is set to the ordinal position of this tab in the [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). It is managed by the tab panel and should not be set directly.

[isFirst](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-isFirst)
This config is set to `true` when this tab represents the first tab of a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). It is managed by the tab panel and should not be set directly.

[isLast](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-isLast)
This config is set to `true` when this tab represents the last tab of a [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel). It is managed by the tab panel and should not be set directly.

[item](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-item)
The [Widget](https://bryntum.com/docs/gantt/api/#Core/widget/Widget) in the [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) corresponding to this tab. It is managed by the tab panel and should not be set directly.

[tabPanel](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-tabPanel)
The tab panel that owns this tab.

[titleProperty](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-titleProperty)
The config property on this tab that will be set to the value of the [titleSource](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-titleSource) property of this tab's [item](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-item).

By default, the [text](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-text) property of the tab is set to the [title](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-title) property of its [item](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-item).

[titleSource](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-titleSource)
The config property on this tab's [item](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-item) that is used to set the value of the [titleProperty](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-titleProperty) of this tab.

By default, the [text](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-text) property of the tab is set to the [title](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#config-title) property of its [item](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-item).

[closable](https://bryntum.com/docs/gantt/api/Core/widget/Tab#config-closable)
Set to `true` to show a close icon to remove the tab from the owning TabPanel

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTab](https://bryntum.com/docs/gantt/api/Core/widget/Tab#property-isTab)
Identifies an object as an instance of [Tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab) class, or subclass thereof.

[isTab](https://bryntum.com/docs/gantt/api/Core/widget/Tab#property-isTab-static)
Identifies an object as an instance of [Tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab) class, or subclass thereof.

[index](https://bryntum.com/docs/gantt/api/Core/widget/Tab#property-index)
The ordinal position of this tab in the [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel).

[closable](https://bryntum.com/docs/gantt/api/Core/widget/Tab#property-closable)
Set to `true` to show a close icon to remove the tab from the owning TabPanel
