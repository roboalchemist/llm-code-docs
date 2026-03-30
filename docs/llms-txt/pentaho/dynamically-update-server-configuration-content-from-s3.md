# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/installing-the-platform-or-pdi-server-on-aws/dynamically-update-server-configuration-content-from-s3.md

# Dynamically update server configuration content from S3

If the content of the S3 bucket changed and you must reflect these changes in the Platform or PDI Server, follow these instructions:

Before deploying the Platform or PDI Server, set the value of the **allow\_live\_config** property in the file `pentaho-server-aws-rds.yaml` to **true**.

1. Navigate to the relevant directory, where the configuration needs to be updated.
2. Prepare the configuration update script in a later step by setting the `<config_command>` part of the script to one of the command options in the following table.

   | Command option | Description                                                                                                                  |
   | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
   | load\_from\_s3 | Copies the content of the bucket to the server’s `/home/pentaho/.kettle` directory.                                          |
   | restart        | Restarts the Platform or PDI Server without restarting the pod.                                                              |
   | update\_config | Executes `load_from_s3`, executes all the configuration and initialization scripts, and then executes the `restart` command. |

   **Note:** When using the `restart` or `update_config` command, a disruption occurs in the Platform or PDI Server's use of sticky sessions. Using the `restart` or `update_config` command causes a server restart that impacts the user sessions.
3. Run the configuration update script.

   **Note:** If you have multiple Platform or PDI Server replicas, remove the comment hashtag in front of `sleep 60`.

   ```
   for pod in $( kubectl get pods -o name -n pentaho-server )
   do
     	echo "Forwarding port on pod: $pod"
    	 pid=$( kubectl port-forward -n pentaho-server $pod 8090:8090 1>/dev/null & echo $! )
    	 while ! nc -z localhost 8090; do 
      		 sleep 0.1
     	done
    	 echo "Executing command ..."
    	 result=$( curl http://localhost:8090/<config_command> )
    	 echo "Command result: $result"
     echo "Killing port forward pid: $pid"
     	while $(kill -9 $pid 2>/dev/null); do 
     	  	sleep 1
    	done
     	# sleep 60
   done;
   ```
4. Verify that the servers restart properly.
