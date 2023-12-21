# Ubuntu PostgreSQL Setup

### WORK IN PROGRESS...

Simple script that can install, check version/status and enable/disable PostgreSQL on Ubuntu. Still needs config `UFW`
and config `Remote Access` menu.

![image](https://github.com/vytautasmatukynas/PostgreSQL-Setup-Ubuntu-Python/assets/51360361/96e7fcc7-fdcf-4f8b-98c4-e7980e38a66e)

### Setup PostgreSQL:

![image](https://github.com/vytautasmatukynas/PostgreSQL-Setup-Ubuntu-Python/assets/51360361/8f7f7b82-8b37-4618-8ab7-c6ada750020a)

Download GPG key: `wget -qO /etc/apt/trusted.gpg.d/pgdg.asc https://www.postgresql.org/media/keys/ACCC4CF8.asc -y`

Add repository: `echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -sc)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list -y`

Install PostgreSQL:  `apt update -y` `apt install -y postgresql postgresql-contrib`

Check PostgreSQL status: `systemctl status postgresql`

Check PostgreSQL version: `psql --version`


### PostgreSQL service actions:

![image](https://github.com/vytautasmatukynas/PostgreSQL-Setup-Ubuntu-Python/assets/51360361/e6cee18f-a33d-4e78-8287-9b01e23db8d1)

Enable PostgreSQL service: `systemctl enable postgresql`

Start PostgreSQL service: `systemctl start postgresql`

Stop PostgreSQL service: `systemctl stop postgresql`

Restart PostgreSQL service: `systemctl restart postgresql`

Check PostgreSQL status: `systemctl status postgresql`

Check PostgreSQL version: `psql --version`
