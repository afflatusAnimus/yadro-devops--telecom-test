# yadro-devops--telecom-test

Тестовое задание на направление DevOps YADRO Impulse 2025 (Телеком-команда)

Задание на Ansible реализовано в виде роли.

## Запуск

* Перед запуском роли нужно настроить inventory/hosts.yml
* В случае использования на удаленном хосте скопировать на него SSH ключ через ssh-copy-id
* Далее задать в hosts файле ip хоста, порт, имя пользователя на хосте и путь к приватному ключу на master ноде, с которой будет происходить запуск роли
* Также либо в defaults/main.yml роли либо через флаг -e "user_name=юзернейм_на_хосте" нужно переопределить user_name на тот, который задан на целевом хосте
* Для запуска используем команду:

ansible-playbook playbook.yml -i inventory/hosts.yml -K

* Если не переопределено имя пользователя в defaults/main.yml, то задаем через флаг:

ansible-playbook playbook.yml -i inventory/hosts.yml -e "user_name=юзернейм_на_хосте" -K