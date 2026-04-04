# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/api.md

# API

It is also possible to access the GraphML information via a Pentaho Server API. There are REST endpoints available to retrieve the lineage related artifacts.

Below are some example `curl` commands which exercise the REST endpoints available on the Pentaho Server. These calls use basic authentication. For more information on the various ways to authenticate with the Pentaho Server, see **Authenticate with the server before making service calls** in the Pentaho REST API documentation.

For more detailed information about the REST endpoints available, you can go to the Pentaho Wiki to view the [attached Enunciate file](https://help.pentaho.com/@api/deki/files/20549/metaverse-enunciate.zip?revision=1).

* **Get all lineage related artifacts**

  ```
  curl --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/all

  ```
* **Get all lineage from a given date forward**

  ```
  curl --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/all/20150706

  ```
* **Get all lineage between 2 dates**

  ```
  curl --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/all/20150101/20150706
  ```
* **Get all of the lineage artifacts for a specific file in the DI repo**

  ```
  curl --request POST --header "Content-Type: application/json" --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" --data '{"path": "/LOCAL DI REPO/home/admin/dataGrid-dummy"}' http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/file
  ```
* **Get all lineage related artifacts for a specific file in the DI repo between 2 dates**

  ```
  curl --request POST --header "Content-Type: application/json" --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" --data '{"path": "/LOCAL DI REPO/home/admin/dataGrid-dummy"}' http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/file/20150701/20150707
  ```
* **Invalid date request**

  ```
  curl --header "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" http://localhost:8080/pentaho/osgi/cxf/lineage/api/download/all/20159999
  ```
