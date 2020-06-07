<div align="center">
  <h1>
    :recycle: <i>Ecoleta</i>
  </h1>

  <p>
    Projeto feito com ReactJS & JavaScript na semana do Next Level Week (NLW)
  </p>

  <img src="images/capa.png">
</div>

## :open_book: Sobre

Ecoleta é um projeto baseado na NLW. Ele conecta pessoas que querem ou não sabem a maneira certa de descartar o lixo com companias de reciclagem, descarte de óleo e etc. Esse lixo pode ser pilhas, residuos orgânicos, óleo e muito mais.

## :artificial_satellite: Tecnologias usadas

* Node.js
* JavaScript/TypeScript
* ReactJS
* React Native
* Expo


## :dart: Como usar

Para usar rodar as aplicações é nescessario ter instalado na sua maquina o (Node.js)[https://nodejs.org/en/download/] e o (Git)[https://git-scm.com/downloads]. Depois basta seguir os passos a seguir.

Antes de tudo, é nescessario você instalar as dependencias. Para isso basta rodar os seguintes comandos em seu terminal/prompt.

```shell
# Vai clonar a pasta do projeto para a sua maquina
git clone https://jefferson-calmon.github.io 

# Vai abrir a pasta do projeto
cd ecoleta

# Vai abrir um arquivo em lotes e instalar todas as dependencias. Esse processo vai demorar um pouco não feche o terminal.
install-dependencies.bat
```

Depois disto vamos iniciar o back-end.
Obs: Caso tenha queira instalar as dependencias manualmente veja (aqui)[] quais são nescessarias.

### Back-end

Para iniciar o back-end é muito simples. Execute os comandos abaixo.

``` shell
# Abrir a pasta do back-end
cd server

# Iniciar o back-end
npm run dev

# A API estara rodando na porta 3333 em localhost
```

Pronto!! O back-end já está rodando!! Agora você precisa iniciar o Front-end.

### Front-end

Para você poder acessar o site você precisa deixar ele online. Abra outro terminal e navegue até onde está a pasta do projeto ecoleta e execute os comandos abaixo. Obs: Não feche o terminal que está rodando o back-end.

```shell
# Vai abrir a pasta do site
cd web

# Vai iniciar um server local com o site.
npm start

# Depois disto vai abrir um página no seu navegador rodando o site.
```

Pronto!! Agora já temos o back-end e o site fucionando.

### Mobile

Para você testar o app será preciso instalar um app chamado (Expo)[https://play.google.com/store/apps/details?id=host.exp.exponent]. Ele irá servir como simulador para o app. 

Depois abra mais um terminal e execute os comandos abaixo.

````
# Vai abrir a pasta com os arquivos do mobile
cd mobile

Vai iniciar mais um servidor local 
npm start
```

Depois desses comandos ira abrir no seu navegador uma página com algumas informações. Abra o app do expo em seu celular e escaneie o QRcode. Proto!! Depois de carregar irá abrir o app.

## License

Este repositório usa a licensa MIT. Por favor leia a licensa.

Feito por Jefferson Ferrari :bomb: