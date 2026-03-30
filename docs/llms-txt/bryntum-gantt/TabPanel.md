# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/TabPanel.md

# [TabPanel](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel)

A tab panel widget which displays a collection of tabs, each of which can contain other widgets or HTML/text. This widget has a [tab bar](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar) on top of its contents, and each [Tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab) can be customized using the [tab](https://bryntum.com/docs/gantt/api/#Core/widget/Tab#config-tab) config.

```
const tabPanel = new TabPanel({
 items: {
     firstTab : {
         title: 'First',
         items: {
             name : { type: 'textfield', label: 'Name' },
             ...
         }
     },
     settingsTab : {
         title: 'Settings',
         tab : {
             // Show an icon in the tab
             icon : 'fa fa-cog'
         },
         items: {
             ...
         }
     }
 }
});
```

The tab selector buttons are focusable elements. `Enter` or `Space` activates a tab, and moves focus into the newly visible tab item.

Adding non tab items to the tab bar
-----------------------------------

The [TabBar](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar) is a subclass of the Toolbar, meaning you can add additional widgets to it. You can add either [tab-specific items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-tabBarItems) only shown for the active tab, or you can add static extra items that are shown for all tabs.

Demo showing tab-specific extra items using [tabBarItems](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-tabBarItems).

Demo showing static extra items using [items](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar#config-items)

Tabs can be drag-dropped
------------------------

You can easily let users reorder the tabs by setting [enableReordering](https://bryntum.com/docs/gantt/api/#Core/widget/TabBar#config-enableReordering) to `true`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[activeTab](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-activeTab)
The index of the initially active tab.

[animateTabChange](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-animateTabChange)
Specifies whether to slide tabs in and out of visibility.

[autoHeight](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-autoHeight)
Set the height of all tabs to match the tab with the highest content.

[tabBar](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-tabBar)
Additional configuration for the tab bar.

Use this to add more non-tab items to the bar:

```
new TabPanel({
   tabBar : {
      items : {
         spacer : '->', // Spacer which moves next item to the right
         button : { type : 'button', text : 'MyButton' }
      }
   }
});
```

[tabMinWidth](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-tabMinWidth)
Min width of a tab title. 0 means no minimum width. This is default.

[tabMaxWidth](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#config-tabMaxWidth)
Max width of a tab title. 0 means no maximum width. This is default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTabPanel](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#property-isTabPanel)
Identifies an object as an instance of [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) class, or subclass thereof.

[isTabPanel](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#property-isTabPanel-static)
Identifies an object as an instance of [TabPanel](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel) class, or subclass thereof.

[activeTab](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#property-activeTab)
The index of the initially active tab.

[activeIndex](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#property-activeIndex)
The active tab index. Setting must be done through [activeTab](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel#property-activeTab)

[activeItem](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#property-activeItem)
The active child widget. Setting must be done through [activeTab](https://bryntum.com/docs/gantt/api/#Core/widget/TabPanel#property-activeTab)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeTabChange](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#event-beforeTabChange)
The active tab is about to be changed. Return `false` to prevent this.

[tabChange](https://bryntum.com/docs/gantt/api/Core/widget/TabPanel#event-tabChange)
The active tab has changed.
