# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/installing-the-platform-or-pdi-server-on-aws/install-the-platform-or-pdi-server-on-aws.md

# Install the Platform or PDI Server on AWS

When the AWS environment is properly configured, you can proceed to install the Platform or PDI Server.

1. Retrieve the kubeconfig from the EKS cluster.

   In the workstation console, obtain the kubeconfig from the EKS cluster you created by using the following command:

   ```
   aws eks update-kubeconfig --name <my_eks_cluster_name> --region <my_EKS_region>
   ```
2. To configure the Platform or PDI Server YAML file, open the file `pentaho-server-aws-rds-<lb-type>.yaml` in the `yaml` project directory.

   | lb-type | When to use                                             |
   | ------- | ------------------------------------------------------- |
   | alb     | Use if you installed the AWS Application load balancer. |
   | nginx   | Use if you have installed the NGINX Ingress Controller. |
3. Update the Platform or PDI Server YAML file by copying the values that you recorded in the [Worksheet for AWS hyperscaler](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/running-pdi-cli-on-aws/worksheet-for-aws-hyperscaler-common).
4. Retrieve the Platform or PDI Server entry point URI information.

   The Platform or PDI Server entry point URI information can be retrieved by running either of the following commands on the workstation console:

   ```
   kubectl get ingress -n pentaho-server
   ```

   or

   ```
   echo $( kubectl get ingress -n pentaho-server -o jsonpath='{.items..hostname}' )
   ```

   The port number is 80 by default.
5. Deploy the Platform or PDI Server using the following command:

   ```
   kubectl apply -f <path to Pentaho deployment YAML>
   ```
6. Test the Platform or PDI Server by retrieving the LoadBalancer Ingress URI.

   To retreive the LoadBalancer Ingress URI, run the following command in the workstation console:

   ```
   echo $( kubectl get ingress -n pentaho-server -o jsonpath='{.items..hostname}' )
   ```

   **Note:** The port number for this load balancer is 80, not 8080.
7. Use the URI that you received in the previous step in a Pentaho-supported browser to open the Platform or PDI Server login window and access the Platform or PDI Server.

   | Field    | Default value |
   | -------- | ------------- |
   | Username | admin         |
   | Password | password      |
