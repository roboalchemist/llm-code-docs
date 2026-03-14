# Integrating Polars With an SQL Database Using Efficient Caching

             %%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#FFF5E6', 'secondaryColor': '#FFF5E6' }}}%%
 graph LR;
     source[Source system]
     dw[Data Warehouse]
     csv[Local .csv]
     ds[Data application]
     source-->|data pipeline|dw-->|SQL query|csv-->|read_csv|ds
     dw-->|cached Patito<br>integration|ds