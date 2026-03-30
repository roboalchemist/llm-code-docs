# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/communicate-the-olap-control-with-the-base.md

# Communicate the OLAP control with the base

Each and every control has an OlapDataManager property. Through this property, the control sends and receives information to and from the base. 

## Below steps explains how to load data in an OLAP control:

1. Give the connection information and OlapReport to the OlapDataManager.
2. Assign this OlapDataManager to the controlâs OlapDataManager property.
3. By invoking the controlâs DataBind() method virtually when setting the value for the OlapDataManager property, the data processing will begin and the output is displayed in the Control.
