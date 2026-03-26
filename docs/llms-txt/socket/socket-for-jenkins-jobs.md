# Source: https://docs.socket.dev/docs/socket-for-jenkins-jobs.md

# Socket for Jenkins Jobs

Socket fights vulnerabilities and provides visibility, defense-in-depth, and proactive supply chain protection for your open source dependencies. It is easy to integrate Socket into your Jenkins Build Process to provide an extra layer of security against Supply Chain Attacks.

## Adding Socket to your build process

### Requirements

In order to run the Socket CLI you will need the following installed in your Jenkins Runners/Agents

1. Python3
2. pip
3. git
4. python3.11-venv

**Example Dockerfile of Jenkins with requirements**

```dockerfile shell
FROM jenkins/jenkins:2.462.2-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli python3 python3-pip python3.11-venv
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
```

<br />

### Setting Socket API token

1. Create a Socket API Key ([Directions](https://docs.socket.dev/docs/create-socket-api-key-for-cicd))
2. Log into Jenkins
3. Go to Dashboard -> Manage Jenkins
4. Select `Credentials`

   <Image align="center" src="https://files.readme.io/a3fd9bc081db93aa94bf48243b3f98582c4c5aa18809e8b38a1a1669b46576c7-Screenshot_2024-09-24_at_9.21.33_PM.png" />
5. Go to `System`
6. `Global Credentials`
   1. Note: This can be whatever level that the Pipeline/Job that Socket will run in has access to
7. Select Add Credentials

   1. **Scope:** Select the level needed for Socket to have access to
   2. **Secret:** Paste the Socket API token
   3. **id:** SOCKET-API
   4. **Description:** Socket Security API token

      <Image align="center" src="https://files.readme.io/9642dca700324e32da8cababdb73c88f3d10d3a087def42ff9314b3e288880df-Screenshot_2024-09-24_at_9.19.43_PM.png" />
8. Click Create

### Example adding Socket as a Stage/Step in a Pipeline

1. Log into Jenkins
2. Select a Pipeline
3. Scroll down to `Pipeline`
4. Add the following stage
   ```
   stage('run-socket') {
         steps {
           script {
               withCredentials([string(credentialsId: 'SOCKET-API', variable: 'SOCKET_SECURITY_API_KEY')]) {
                   // Run Socket
                   sh "python3 -m venv .venv && PATH=.venv/bin:$PATH && pip install socketsecurity --upgrade && socketcli --target-path ./
               }
             }
          }
       }
   ```
5. Save

### Example adding Socket as a Build Step in a Job

1. Log into Jenkins
2. Select a job, in the example we selected `socket-example-job`

   <Image align="center" src="https://files.readme.io/daa59cc8c74590248fb829c8c35153c47cc52100eb1b67362a01d720aaf342ce-Screenshot_2024-09-24_at_8.41.00_PM.png" />
3. Select `Configure`
4. Scroll down to `Build Environment`
5. Select `Use secret text(s) or file(s)`
6. Configure a `Secret Text`

   1. **Variable:** `SOCKET_SECURITY_API_KEY`
   2. Credential should be the Socket API token

      <Image align="center" src="https://files.readme.io/633af4d6e5db9102da5a90689c0b420aded5aafc2571259e5508c0982348c1d2-Screenshot_2024-09-24_at_8.45.37_PM.png" />
7. Scroll down to Build Steps
8. Select `Add a build step`
9. Select `shell` for the type
10. Add the following shell script

    ```Text shell
    python3 -m venv .venv
    PATH=.venv/bin:$PATH
    pip install socketsecurity --upgrade
    socketcli --target_path .
    ```
11. Save

### Testing pipeline

1. Click `Build Now`
2. Check the console output

<Image align="center" src="https://files.readme.io/e4b76c77db65334bb8131c0aab10178bd67a1b67c6a2bc5278cd27baee4eefe9-Screenshot_2024-09-24_at_8.49.31_PM.png" />