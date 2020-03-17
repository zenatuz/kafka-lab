# Lab de Kafka + Python rodando em Docker
Repositório com exemplo de configuração para rodar o Kafka localmente com Docker.

> O **Dockerfile** foi utilizado apenas como ambiente de desenvolvimento da aplicação de exemplo **producer/consumer** em python usando o recurso de desenvolvimento em Container do Visual Studio Code - [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers). 

---
## Iniciando os containers

Para iniciar o projeto, edite o arquivo docker-compose e substitua a variável abaixo com o ip da sua máquina:

```yaml
    KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://<IP_PARA_LISTENER>:9092
```

Também edite a aplicação (**app/app.py**), e substitua as variáveis com os valores abaixo:

```python
server='seu_ip:9092'
topic='topico_desejado'
```

Após isso, no diretório do projeto, digite
```bash
docker-compose up -d
```

Para verificar se os containers estão rodando, digite:
```bash
docker-compose ps
```

---

## Conectando-se ao Kafka

Caso queira validar a conexão ao Kafka, pode-se utilizar de clientes como o [https://www.conduktor.io/](https://www.conduktor.io/) ou ainda uma console web como o [https://github.com/yahoo/CMAK](https://github.com/yahoo/CMAK). 

Todas essas ferramentas permitirão a conexão ao Kafka, onde será possível gerenciar tópicos, visualizar informações ou consumir um determinado tópico em tempo real.

### Testando com a aplicação em Python no diretório ```./app```

Para testar com a aplicação python, digite:

```shell
docker-compose exec python /usr/local/bin/python /app/app.py
```

> Esse exemplo de aplicação produz e consome objetos no Kafka.

----

## Documentação e Repositório base 
Utilizei como documentação e consulta o repositório da Bitnami [https://github.com/bitnami/bitnami-docker-kafka](https://github.com/bitnami/bitnami-docker-kafka).