## Instalação e inicialização

```
docker-compose up --build

```
O serviço estará em: http://localhost:8000/

## Autenticação

Primeiro crie o usuário:

```
docker-compose run --rm local python app/manage.py createsuperuser
```

Após adicione no header:

```
{'Authorization': 'JWT <token>'}
```

## Documentação

http://localhost:8000/swagger/
