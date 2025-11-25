# Source: https://docs.oxla.com/troubleshooting-optimization/error-handling.md

# Error Handling

## Overview

Learn more about the common errors and how to resolve them. Below you can find a list of the common errors you may encounter while connecting or running the Oxla server and their resolutions.

### Undefined Volume and Invalid Compose Project

If you encounter an error like this:

` service "oxla_node" refers to undefined volume local_csvs: invalid compose project`

Please follow these steps:

1. Change the directory where you store the docker-compose configuration file by executing this command

```typescript  theme={null}
cd your_folder_name
```

2. Open the docker-compose configuration file

```typescript  theme={null}
vim your_file_name.yml
```

3. Remove `local_csvs:/local_csvs`in your docker compose file

### Too Many Open Files

If you encounter an error as follows when deploying Oxla server:

```typescript  theme={null}
Jan 24 13:58:26 server[XXXXXX]: 2023-01-24 13:58:26.301 ERROR [229223] [network::StateHandlerManager>::start@241] could not accept incoming connection because:
Jan 24 13:58:26 server[XXXXXX]: --------------------------------------------------------------------------------
Jan 24 13:58:26 server[XXXXXX]: Too many open files
```

Please follow these steps:

1. Change the directory where you store the docker compose configuration file by executing this command

```typescript  theme={null}
cd your_folder_name
```

2. Open the docker compose configuration file

```typescript  theme={null}
vim your_file_name.yml
```

3. Ensure that your docker compose file has the correct limit set

```typescript  theme={null}
ulimits:
      nofile:
        soft: 40000
        hard: 40000
```

### Command Not Recognized - psql

If you encounter an error like this:

`'psql' is not recognized as an internal or external command, operable program, or batch file`

Please follow these steps:

**For Windows**

1. Open the **PostgreSQL** folder > **scripts** and then open the command prompt on your computer:

![open command prompt](https://archbee-image-uploads.s3.amazonaws.com/S_lGBDD7H53z1OcF8Kc79/80jZhU63tk1pglP_V-Oti_ezcom-maker-26.gif)

```typescript  theme={null}
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\PostgreSQL\14\scripts>
```

2. Run the following command: cd `"C:\Program Files\PostgreSQL\14\bin"`

```typescript  theme={null}
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\PostgreSQL\14\scripts> cd "C:\Program Files\PostgreSQL\14\bin"
```

3. Last but not least, execute the following command to run the Oxla server: psql -h 44.210.23.203\`\`

```typescript  theme={null}
(c) Microsoft Corporation. All rights reserved. 

C:\Program Files\PostgreSQL\14\scripts> cd "C:\Program Files\PostgreSQL\14\bin" 

C:\Program Files\PostgreSQL\14\bin> psql.exe -h 44.210.23.203
```

### Encoding Is Not Supported

If you encounter an error like this:

`Psql: error: connection to server at "44.210.23.203", port 5432 failed: FATAL: WIN1252 encoding is not supported`

Please follow these steps:

1. Run the following command:

```typescript  theme={null}
SET PGCLIENTENCODING=UTF8
```

2. Then, activate the code page with the command below:

```typescript  theme={null}
chcp 65001Command
```

You will get the following output:

```typescript  theme={null}
Active code page: 65001
```

3. Execute the following command to run the Oxla server: `psql -h 44.210.23.203`

```typescript  theme={null}
C:\Program Files\PostgreSQL\14\bin>SET PGCLIENTENCODING=UTF8

C:\Program Files\PostgreSQL\14\bin>chcp 65001
Active code page: 65001

C:\Program Files\PostgreSQL\14\bin>psql.exe -h 44.210.23.203
```

### Missing Argument

If you encounter an error like this:

`Psql: warning: extra command-line argument "44.210.23.203" ignored`

Re-check the command. Keep an eye on each component, even the symbols and uppercase/lowercase words.

### Command Not Found - psql

If you encounter an error like this:

`Psql.exe: command not found`

Download and install PostgreSQL on your computer:

* **For Windows,** download PostgreSQL from [here](https://www.postgresql.org/download/).
* **For Linux**, install PostgreSQL by following the steps [here](https://www.postgresql.org/download/linux/ubuntu/).
* **For Mac**, install PostgreSQL through terminal using brew: `mac$ brew install postgresql`.

![Installing PostgreSQL](https://archbee-image-uploads.s3.amazonaws.com/S_lGBDD7H53z1OcF8Kc79/l5eN2BdKhfjiciegK3d1P_imageedit24068984245.png)
