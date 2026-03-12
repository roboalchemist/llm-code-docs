# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/running-pdi-cli-on-aws/load-and-push-the-pentaho-docker-image-to-ecr-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/installing-the-carte-server-on-aws/load-and-push-the-pentaho-docker-image-to-ecr-reuse.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/installing-the-platform-or-pdi-server-on-aws/load-and-push-the-pentaho-docker-image-to-ecr-reuse.md

# Load and push the Pentaho Docker image to ECR

Select and tag the Pentaho Docker image and then push it to the ECR registry.

1. Navigate to the image directory containing the Pentaho `tar.gz` files.
2. Select and load the `tar.gz` file into the local registry by running the following command:

   ```
   docker load -i <pentaho-image>.tar.gz
   ```
3. Record the name of the source image that was loaded into the registry by using the following command:

   ```
   docker images
   ```
4. Tag the source image so it can be pushed to the cloud platform by using the following command:

   ```
   docker tag <source-image>:<tag> <target-repository>:<tag>
   ```
5. Push the image file into the ECR registry using the following Docker command:

   ```
   docker push <target-repository>:<tag>
   ```

   The AWS Management Console displays the uploaded image URI.

   For general AWS instructions on how to push an image to AWS, see [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html).
6. Record the newly created ECR repository URI in the [Worksheet for AWS hyperscaler](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/running-pdi-cli-on-aws/worksheet-for-aws-hyperscaler-common).
