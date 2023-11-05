## Comandos básicos para usar o linux

> Quando for indicado um nome entre <>, é possível alterá-lo. Por exemplo, para acessar um diretório, posso usar o comando `cd <diretorio>`. Se estou no diretório inicial (`~`) e quero acessar os Documentos, basta utilizar `cd Documentos`.

- `cd <diretorio>`: entra no diretório indicado.
- `ls <diretorio>`: lista o diretório indicado. Se nada for indicado, lista o diretório atual.
- `touch <arquivo>`: cria um arquivo em branco
- `gedit <arquivo>`: abre o arquivo no bloco de notas. Se o arquivo não existir, ele é criado. (Lembrem-se de que é preciso salvar o arquivo depois de editar. Isso pode ser feito com o comando `Ctrl S` no teclado, por exemplo).

> No terminal, para ver qual o diretório atual, basta observar o que está escrito antes do local para digitar. Por exemplo, no meu caso, os Documentos são indicados como `gian@gian-PC:~/Documentos$ █ `. Cada `/` indica um diretório. Nesse caso, Documentos está dentro da pasta padrão (*home*, ou `~`).

## Executando e testando os programas

Depois que vocês escrevem o código usando o editor de texto e salvam, é preciso executá-lo. Como estamos utilizando *python*, basta usar o comando 

```
python3 <arquivo_codigo>
```

Se o programa precisar de entrada (como é o caso dos problemas da OBI), o jeito mais simples de testar é:

1. Criar e editar um arquivo de entrada (por exemplo, `entrada.txt`). Nele, deve ser colocada um entrada dada no enunciado do problema.
2. Executar o comando 
```
python3 <arquivo_codigo>  <  entrada.txt
``` 
## Encontrando questões

Vamos utilizar o <a href="https://www.beecrowd.com.br/judge/en/login"> https://www.beecrowd.com.br/judge/en/login </a>. Depois de colocar a conta e chegar na página inicial, basta ir em **Problemas**, selecionar uma das diversas categorias mostradas e escolher uma questão na lista apresentada.

> Inicialmente, entrem na categoria **Iniciante**.


## Submetendo o código de uma questão

Depois de abrir o problema, é possível ver, na lateral direita, um campo para digitar. Com isso, basta copiar o código e colar nesse campo (no teclado `Ctrl C` para copiar, e `Ctrl V` para colar). 

> Lembrem de selecionar a linguagem correta antes de enviar. Nesse caso, é preciso escolher Python (recomendo o `Python 3.9`).