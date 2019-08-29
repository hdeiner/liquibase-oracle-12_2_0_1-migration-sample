#!/usr/bin/env python
import os

os.system('figlet -w 160 -f standard "Migrate to Database Version 2"')

os.system('echo "classpath=lib/ojdbc-12.2.0.1.jar" > liquibase.properties')
os.system('echo "driver=oracle.jdbc.driver.OracleDriver" >> liquibase.properties')
os.system('echo "url=jdbc:oracle:thin:@localhost:1521:ORCLCDB" >> liquibase.properties')
os.system('echo "username=sys as sysdba" >> liquibase.properties')
os.system('echo "password=Oradoc_db1" >> liquibase.properties')

os.system('cp src/main/db/IMDB-schema-v2.xml src/main/db/IMDB-schema.xml')
os.system('liquibase --changeLogFile=src/main/db/IMDB-schema.xml update')
os.system('liquibase --changeLogFile=src/main/db/IMDB-schema.xml dbdoc docs/dbdoc/v2')

os.system('rm liquibase.properties')
os.system('rm src/main/db/IMDB-schema.xml')
