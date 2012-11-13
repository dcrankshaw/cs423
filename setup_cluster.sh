#! /bin/bash

set -x verbose

if [ -e /mnt/xldb_tmp ]
then
	sudo chown scidb /mnt/xldb_tmp
else
	sudo mkdir /mnt/xldb_tmp
	sudo chown scidb /mnt/xldb_tmp
fi

sudo /etc/init.d/postgresql-8.4 restart
sudo cp /etc/postgresql/8.4/main/pg_hba.conf ~/
sudo chown scidb ~/pg_hba.conf

for idx in {1..8}
do
	WORKER="worker_$idx"
	scp /etc/hosts $WORKER:~/
	scp /opt/scidb/12.7/etc/config.ini $WORKER:~/
	scp ~/pg_hba.conf $WORKER:~/
	scp setup_node.sh $WORKER:~/
	ssh $WORKER sudo ~/setup_node.sh
done
