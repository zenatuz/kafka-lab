# Lab de Kafka + Python rodando em Docker
Repositório com exemplo de configuração para rodar o Kafka localmente com Docker.

> O **Dockerfile** foi utilizado apenas para desenvolvimento da aplicação de exemplo em python **(ainda em desenvolvimento)**, que irá se conectar ao stream do Kafka

---
## Iniciando os containers

Para iniciar o projeto, edite o arquivo docker-compose e substitua a variável abaixo com o ip da sua máquina:

>```KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://<IP_PARA_LISTENER>:9092```

Após isso, no diretório do projeto, digite
> ```docker-compose up -d```

Para verificar se os containers estão rodando, digite:
> ```docker-compose ps```

Para se conectar a um container, digite:
> ```docker-compose exec <NOME_DO_SERVIÇO> /bin/bash```

---

## Conectando-se ao Kafka

Caso queira validar a conexão ao Kafka, sem um código, pode-se utilizar de clientes como o [https://www.conduktor.io/](https://www.conduktor.io/) ou [http://www.kafkatool.com/](http://www.kafkatool.com/) ou ainda uma console web como o [https://github.com/yahoo/CMAK](https://github.com/yahoo/CMAK). 

Todas essas ferramentas permitirão a conexão ao Kafka, onde será possível gerenciar tópicos, visualizar informações ou consumir um determinado tópico em tempo real.

----

## Documentação e Repositório base 
Utilizei como documentação e consulta o repositório da Bitnami [https://github.com/bitnami/bitnami-docker-kafka](https://github.com/bitnami/bitnami-docker-kafka).