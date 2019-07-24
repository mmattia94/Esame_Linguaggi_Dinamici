# Esame_Linguaggi_Dinamici
Esame Linguaggi Dinamici 2018/19 Miceli Mattia 83475 10/7/19

REQUIREMENTS
------------
Il progetto è stato testato con Django (versione 2.1) e Python (version 3.5).

Installazione di alcune dipendenze nel caso non siano già presenti nel sistema

```
$$ apt-get install python3.5
$$ apt-get install python3-pip
$$ pip3 install django==2.1
$$ pip3 install setuptools
$ python3 -m pip install PyMySQL
```

DATABASE SETTINGS
-----------------
Come database è stato scelto MySQL 8.
Per installarlo in ambiente linux seguire la guida ufficiale a questo url: https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/

NB: nonostante in ambiente Windows funzioni tutto correttamente, in Debian 9, si sono riscontrati alcuni problemi in fase di creazione delle tabelle e popolamento si quest'ultime.

Di seguito sono riportati i comandi essenziali (presenti anche nella guida)
```
$$ wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
$$ sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb 
$$ sudo apt update
$$ sudo apt-get install mysql-server
$$ sudo mysql_secure_installation
$$ sudo systemctl status mysql
$$ sudo systemctl enable mysql
$$ sudo apt-get update
$$ sudo apt-get install default-libmysqlclient-dev
$$ sudo apt-get install libmysqlclient18
$$ sudo apt-get install mysql-workbench 
```
Lanciare un'istanza di mysql e creare lo user 'admin' con password 'admin', utilizzato nei settings del progetto (oppure cambiare i settings per utilizzare un utente già esistente)
```
$$ sudo mysql -u root -p 
```

Copiare lo script seguente:
```
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

FINAL SETUP
-----------
```
$$ cd ./LD
$$ pip install -e .
python3 manage.py makemigrations
python3 manage.py migrate

python3
>>import campionato
>>campionato.campionato("2015-16.json")
>>campionato.campionato("2015-16.json")

mysql -p < campionato_calcio_opzioni.sql
$$ python manage.py runserver
```

Il progetto dovrebbe ora essere raggiungibile all'indirizzo "http://127.0.0.1:8000/Campionato"

AUTHOR
------
Mattia Miceli


