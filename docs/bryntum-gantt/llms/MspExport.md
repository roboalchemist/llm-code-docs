# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/MspExport.md

# [MspExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport)

A feature that allows exporting Gantt to Microsoft Project without involving a server.

[Microsoft Project XML specification](https://bryntum.com/docs/gantt/api/https://docs.microsoft.com/en-us/office-project/xml-data-interchange/introduction-to-project-xml-data)

This feature supports exporting to an XML format that can be imported by MS Project Professional 2013 / 2019.

Here is an example of how to add the feature:

```
const gantt = new Gantt({
    features : {
        mspExport : {
            // Choose the filename for the exported file
            filename : 'Gantt Export'
        }
    }
});
```

And how to trigger an export:

```
gantt.features.mspExport.export({
    filename : 'Gantt Export'
})
```

Processing of exported data
---------------------------

Use the [dataCollected](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/MspExport#event-dataCollected) event to process exported data before it is written to the XML-file:

```
// set listener on Gantt construction step
const gantt = new Gantt({
    ---
    features : {
        mspExport : {
            listeners : {
                dataCollected : ({ data }) => {
                    // patch <Project><Name> tag content
                    data.Name = 'My Cool Project';
                }
            }
        }
    }
});

// set listener at runtime
gantt.features.mspExport.on({
    dataCollected : ({ data }) => {
        // patch <Project><Name> tag content
        data.Name = 'My Cool Project';
    }
})
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[filename](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#config-filename)
Name of the exported file (including extension)

[dateFormat](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#config-dateFormat)
Defines how dates are formatted for MS Project. Information about formats can be found in [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper)

[timeFormat](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#config-timeFormat)
Defines how time is formatted for MSProject. Information about formats can be found in [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper)

[msProjectVersion](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#config-msProjectVersion)
Defines the version used for MSProject (2013 or 2019)

[replaceResourceNameCommas](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#config-replaceResourceNameCommas)
Specify `true` to replace commas in resource names with semicolons.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMspExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#property-isMspExport)
Identifies an object as an instance of [MspExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/MspExport) class, or subclass thereof.

[isMspExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#property-isMspExport-static)
Identifies an object as an instance of [MspExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/MspExport) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[generateExportData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-generateExportData)
Generate the export data to generate the XML.

[export](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-export)
Generates and downloads the .XML file.

[convertToXml](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-convertToXml)
Convert Object data to XML.

[getMsProjectConfig](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getMsProjectConfig)
Get the XML configurations in MS Project format.

[getCalendarData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getCalendarData)
Formats an individual calendar to MS Project format.

[prepareCalendarsData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-prepareCalendarsData)
Prepares calendars data. Clones project calendars and makes individual calendar for each resource.

[getCalendarsData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getCalendarsData)
Format Calendars from Gantt to MS Project format.

[formatWeekDays](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-formatWeekDays)
Format intervals to MS project format for the WeekDays property.

[collectProjectTasks](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-collectProjectTasks)
Format intervals to MS project format for the WorkWeeks property.

[getTaskData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getTaskData)
Formats a tasks to MS Project format.

[getTasksData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getTasksData)
Format Tasks from Gantt to MS Project format.

[getResourcesData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getResourcesData)
Format Resources from Gantt to MS Project format.

[getAssignmentsData](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-getAssignmentsData)
Format Assignments from Gantt to MS Project format.

[convertDurationToMspDuration](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#function-convertDurationToMspDuration-static)
Convert to MS Project Span Date Time format.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeMspExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#event-beforeMspExport)
Fires on the owning Gantt before export starts. Return `false` to cancel the export.

[dataCollected](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#event-dataCollected)
Fires when project data is collected to an object that is going to be exported as XML text.

The event can be used to modify exported data before it is written to the XML-file:

```
const gantt = new Gantt({
    ---
    features : {
        mspExport : {
            listeners : {
                // listener to process exported data
                dataCollected : ({ data }) => {
                    // patch <Project><Name> tag content
                    data.Name = 'My Cool Project';
                }
            }
        }
    }
});
```

[mspExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/MspExport#event-mspExport)
Fires on the owning Gantt when project content is exported to XML, before the XML is downloaded by the browser.
