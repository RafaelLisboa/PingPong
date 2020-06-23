![GifGame](https://github.com/RafaelLisboa/PingPong/blob/master/Ping-Pong-2020-06-22-23-19-11.gif)

# PingPong
O classico Ping Pong feito em Python e totalmente orientado a objeto
o projeto foi apenas para colocar meus aprendizado sobre o paradigma de Programação Orientada a Objetos em prática,
Foi um grande desafio, principalmente na parte de cálculos com eixos, mas foi muito satisfatório. 

# Funcionamento

O jogo foi dividido em 3 classes: Player, Bot e Game:

### Player
				 
  A classe player tem o papel de gerenciar as raquetes, ela controla a altura e o limite de movimentação. Através de metodos bem simples
	  ela recebe eventos que são disparados através do teclado e apartir destes eventos ela defini qual tecla foi digitada e move a raquete de acordo com a mesma,
  consultando sempre se a posição da raquete com este movimento irá utrapassar os limites da borda.
  Essa nova posição é passada através de um metodo também. Antes de iniciar o jogo são instanciados duas classes de player e caso o usuario deseje
  jogar multiplayer, as duas instancias são passadas a classe Game.
  
### Bot

  O Bot seria uma "Inteligencia Artificial", porém com a minima quantidade de inteligencia possível. Ela é uma sub-classe de Player e sobrescreve-a
  dispensando a necessidade de receber uma tecla especificica como paramentro para a movimentação da raquete, o funcionamento dela é bem simples
  caso a bola esteja proxima ao Bot, ele movimenta a raquete para a direção da bola, caso contrário ele permanece parado
  
### Game

  Essa é a classe mais importante do codigo, sendo ela a responsavel por criar a tela e gerenciar a bibilioteca Pygame, recebe como parametro duas instancias para 
  o desenho da raquete na tela, utilizando de metodos das classes acima para solicitar a nova coordenada das mesmas.
  Além de ser a responsável por desenhar a bola calcular suas colisões com a borda e com as raquetes ***A cada colisão a bola fica um pouco mais rapida***,
  ela também passa para as classes das raquetes qual o evento foi disparado.
  
  
  
