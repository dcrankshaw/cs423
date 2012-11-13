#! /bin/bash

if [ -e /mnt/xldb_tmp ]
then
	chown scidb /mnt/xldb_tmp
else
	mkdir /mnt/xldb_tmp
	chown scidb /mnt/xldb_tmp
fi

mv ~/hosts /etc/hosts
mv ~/config.ini /opt/scidb/12.7/etc/

chmod 644 /etc/hosts /opt/scidb/12.7/etc/config.ini
chown root /etc/hosts /opt/scidb/12.7/etc/config.ini
chgrp root /etc/hosts /opt/scidb/12.7/etc/config.ini

mv ~/pg_hba.conf /etc/postgresql/8.4/main/
chmod 640 /etc/postgresql/8.4/main/pg_hba.conf
chown postgres /etc/postgresql/8.4/main/pg_hba.conf
chgrp postgres /etc/postgresql/8.4/main/pg_hba.conf

/etc/init.d/postgresql-8.4 restart

