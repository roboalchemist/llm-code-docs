# Source: https://adempiere.gitbook.io/docs/system-administration/installation/install-adempiere-easily-with-docker.md

# Install ADempiere easily with Docker

## Install Docker for your operating system

To install Docker on MacOS see <https://docs.docker.com/docker-for-mac/install/>

To Install Docker on Window see <https://docs.docker.com/docker-for-windows/install/>

To Install Docker on Debian Linux see <https://docs.docker.com/engine/install/debian/>

Verify that docker is installed :

```bash
docker --version
Docker version 20.10.2, build 2291f61
```

## Install Docker Compose for your operating system

To install Docker <https://docs.docker.com/compose/install/>

```bash
docker-compose --version
docker-compose version 1.27.4, build 40524192
```

## Install git for your operating system

to Install git see <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

```
git --version
git version 2.24.3 (Apple Git-128)
```

## Clone the ADempiere Docker Repository

```bash
git clone https://github.com/adempiere/adempiere-docker.git
```

## Setup ADempiere Docker Install

Open a shell command terminal and run the following statements:

Edit and modify the default settings for the PostgreSQL database&#x20;

```bash
cd adempiere-docker
cat .env
#  Copyright (C) 2010-2017, OpenUp S.A. , http://www.openup.com.uy
#  Copyright (C) 2003-2017, e-Evolution Consultants S.A. , http://www.e-evolution.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  Email: raul.capecce@openupsolutions.com, http://openupsolutions.com , http://github.com/rcapecce
#  Email: victor.perez@e-evolution.com, http://www.e-evolution.com , http://github.com/e-Evolution
ADEMPIERE_DB_PORT=55432
ADEMPIERE_DB_PASSWORD=adempiere
ADEMPIERE_DB_ADMIN_PASSWORD=postgres
PG_VERSION=12.2
vi .env
```

Edit and modify the default setting for the ADempiere

```bash
cd adempiere
cat .env
#  Copyright (C) 2003-2017, e-Evolution Consultants S.A. , http://www.e-evolution.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.ce
#  Email: victor.perez@e-evolution.com, http://www.e-evolution.com , http://github.com/e-Evolution
ADEMPIERE_WEB_PORT=8274
ADEMPIERE_SSL_PORT=4444
ADEMPIERE_VERSION=3.9.3
# ATENTION If is "Y" it will be replace de actual defined database with a empty ADempiere seed
ADEMPIERE_DB_INIT=Y
vi .env
```

Deployment ADempiere using the application shell script

```bash
cd ..
pwd 
# From the adempiere-docker directory execute
./application.sh adempiere up -d --build
# Wait a few minutes while the ADempiere Server installation is done 
docker ps |grep postgres
# The output should show something like 
e70086fe9f89   dd4fa36a9c2f             "docker-entrypoint.s…"   11 months ago       Up 4 minutes       0.0.0.0:55432->5432/tcp                          postgres122_db_1
docker ps |grep adempiere
# The output should show something like 
fe8cc0a49e77   adempiere                "/bin/sh -c '/root/s…"   11 months ago       Up 8 minutes       0.0.0.0:4444->4444/tcp, 0.0.0.0:8274->8888/tcp   adempiere
docker logs adempiere
```

Based on the configuration of ./adempiere/.env, docker will show the available ports where the ADempiere services were deployed 0.0.0.0:4444->4444/tcp, 0.0.0.0:8274->8888/tcp

If everything goes well up to here, open the following url <http://0.0.0.0:8274/webui/> in the browser of your choice

![](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSddzYa7tn_S04R8MXb%2Fimage.png?alt=media\&token=4e28fab1-a1ab-4e76-887a-bbea9497fa27)

To access use the username and password GardenAdmin

![ADempiere Role](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSde6O7b-3YoftgH9Xj%2Fimage.png?alt=media\&token=94cd9bd8-33cb-416f-a1b1-db50629f2e83)

Congratulations now you can evaluate and try adempiere locally

![ADempiere Main Screen](https://115176873-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LJxaiQNjqdt96N_RNRP%2F-MSdW1uWbSW0MAlM0YCL%2F-MSdeFUqxc225QbXWUpu%2Fimage.png?alt=media\&token=bfb56f31-c28e-49e1-b51f-70379ecdf838)

{% hint style="danger" %}
The deployment in Docker is done for didactic purposes, for a production installation requires specific adjustments in the database and memory parameters
{% endhint %}

## See Also

[Github ADempiere Docker Repository](https://github.com/adempiere/adempiere-docker/blob/master/README.md)
