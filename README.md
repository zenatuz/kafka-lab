# Lab de Kafka + Python rodando em Docker
Repositório com exemplo de configuração para rodar o Kafka localmente com Docker.

> O **Dockerfile** foi utilizado apenas para desenvolvimento da aplicação de exemplo em python **(ainda em desenvolvimento)**, que irá se conectar ao stream do Kafka

---

Para iniciar o projeto, edite o arquivo docker-compose e substitua a variável abaixo com o ip da sua máquina:

>```KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://<IP_PARA_LISTENER>:9092```

Após isso, no diretório do projeto, digite
> ```docker-compose up -d```

Para verificar se os containers estão rodando, digite:
> ```docker-compose ps```

Para se conectar a um container, digite:
> ```docker-compose exec <NOME_DO_SERVIÇO>```