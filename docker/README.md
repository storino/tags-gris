Simples aplicação nginx conteinerizada.

Buildando e rodando:

```
sudo docker build -t lstorino/tag-docker .

sudo docker run -d -p 80:80 lstorino/tag-docker
```
Após isso, verificamos o conteúdo de index.html em http://localhost
