iq-test
-------

Ansible роли для установки и настройки кластера S3 Minio

Состав:

* ubuntu 16.04
* nginx
* keepalived
* Minio

Требования для деплоя:

* Vagrant
* VirtualBox
* Ansible >= 2.6
* Python 3


Деплой ВМ:

```
$ vagrant up
```

Деплой компонентов на ВМ:

```
$ ansible-playbook -i inventory/example.yaml deploy.yaml
```

Настройка доступов в S3 и генерация скриптов загрузки/выгрузки:

```
$ ansible-playbook -i inventory/example.yaml minio.yaml
```

Загрузка "плохого" и выгрузка "хорошего" изображения:

```
$ ./upload.py
$ ./download.py
```

В случае успеха, в корневом каталоге репозитория появится файл good.jpg с логотипом.
