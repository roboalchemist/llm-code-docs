# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/running-a-pdi-container-docker-deployment.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/running-a-pdi-container-docker-deployment.md

# Running a PDI container

You can use the PDI container to run transformations with the PDI [pan](https://help.hitachivantara.com/Documentation/Pentaho/9.3/Products/Use_Command_Line_Tools_to_Run_Transformations_and_Jobs) command and jobs with the PDI [kitchen](https://help.hitachivantara.com/Documentation/Pentaho/9.3/Products/Use_Command_Line_Tools_to_Run_Transformations_and_Jobs) command.

Once the PDI container is built, use the `docker compose` command with the `run` parameter to run a transformation or job with the PDI pan or kitchen command, as shown in the following example:

`docker compose -f generatedFiles/docker-compose/yml run pdi ./pan.sh /file:/opt/pentaho/data-integration/simpleTrans.ktr`

In this example, the PDI pan command runs the `simpleTrans.ktr` transformation located in the `pentaho/data-integration` directory. The container stops once the transformation or job is completed.
