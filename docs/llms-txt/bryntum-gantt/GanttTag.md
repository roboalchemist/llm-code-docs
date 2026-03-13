# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/customElements/GanttTag.md

# [GanttTag](https://bryntum.com/docs/gantt/api/Gantt/customElements/GanttTag)

Import this file to be able to use the tag `<bryntum-gantt>` to create a Gantt chart.

This is more of a proof of concept than a ready to use class. The dataset of the `<data>` and `<bryntum-gantt>` tags is applied to record and Gantt configs respectively, which means that you can pass any documented config there, not only the ones demonstrated here. Dataset attributes are translated as follows:

* `data-view-preset` -> `viewPreset`
* `data-start-date` -> `startDate` etc.

```
<bryntum-gantt data-view-preset="weekAndDay" data-start-date="2018-04-02" data-end-date="2018-04-09">
     <column data-type="name">Name</column>
     <project data-load-url="/projectdata">Name</project>
     <feature data-name="nonWorkingTime"></feature>
     <feature data-name="timeRanges" data-show-current-timeline="true"></feature>
</bryntum-gantt>
```

To get styling correct, supply the path to the theme you want to use and to the folder that holds Font Awesome:

```
<bryntum-gantt stylesheet="resources/gantt.stockholm.css" fa-path="resources/fonts">
</bryntum-gantt>
```

NOTE: Remember to call [destroy](https://bryntum.com/docs/gantt/api/#Gantt/customElements/GanttTag#function-destroy) before removing this web component from the DOM to avoid memory leaks.
