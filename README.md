## Instalação e inicialização

```
docker-compose up --build

```
O serviço estará em: http://0.0.0.0:8000/

## Autenticação

Primeiro crie o usuário:

```
docker-compose run python app/manage.py createsuperuser
```

Após adicione no header:

```
{'Authorization': 'JWT <token>'}
```

## Documentação

http://0.0.0.0:8000/swagger/
