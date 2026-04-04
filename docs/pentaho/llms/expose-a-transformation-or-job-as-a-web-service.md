# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/expose-a-transformation-or-job-as-a-web-service.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/expose-a-transformation-or-job-as-a-web-service.md

# Expose a transformation or job as a web service

You can run a PDI transformation or job as part of a web-service by developing one of the following implementations:

* Write a servlet that maps incoming parameters for a [transformation step](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/sample-class-scenarios#run-transformations) or [job entry](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/sample-class-scenarios#run-jobs) and executes them as part of the request cycle.
* Use the Carte server or the Pentaho Server directly by building a transformation that writes its output to the HTTP response of the Carte server. Then, specify the **Pass Output to Servlet** option in the Text Output, XML Output, JSON Output, or scripting steps to write output to the HTTP response. For an example, run the `pentaho/design-tools/data-integration/samples/transformations/Servlet Data Example.ktr` sample transformation on Carte.
