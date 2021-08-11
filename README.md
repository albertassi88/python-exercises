## Guia de configuração do ambiente Python

## Python
### O que é?
#### Python é uma linguagem de programação com foco em legibilidade e produtividade, criada para escrever código bom e fácil de manter de maneira rápida.
### Para que serve?
#### É uma linguagem bastante versátil, e hoje em dia é amplamente utilizada para escrever sistemas web, integrações entre sistemas, automatizar tarefas e muitas outras coisas.
### Como instalar?
#### Versões mais atuais do ubuntu (ou similares) já vem com o python 3 instalado, e inclusive, a partir da versão 17.10, essa passa a ser a versão padrão do sistema.
### Caso python 3 não esteja instalado, utilize: 
#### sudo apt install python3 .
### Vamos verificar se deu tudo certo?
#### Abra um terminal e digite python3 --version.



-------------------------------------------------
## Pyenv (opcional)
### O que é?
#### É comum que pessoas desenvolvedoras Python precisem trabalhar com versões diferentes da linguagem, seja na atuação em múltiplos projetos, seja para estudar novas funcionalidades da linguagem que ainda estão em fase de desenvolvimento ou testes. O pyenv nos ajuda a lidar com isso!.
### Segundo a descrição do projeto:
#### “O Pyenv permite alternar facilmente entre várias versões do Python. É simples, discreto e segue a tradição UNIX de ferramentas de propósito único que fazem uma coisa bem.” Em outras palavras, podemos ter quantas versões da linguagem quisermos ou forem necessárias, instaladas em nosso sistema. É um papel análogo ao node_modules , do JavaScript!
### Instalação em Linux e MacOS
#### Certifique-se de que a lib curl está instalada em seu sistema, baixe e instale o pyenv:
#### curl https://pyenv.run | bash
### Reinicie seu shell para que as mudanças tenham efeito:
#### exec $SHELL
### Certifique-se de que as seguintes linhas estão no seu arquivo de configuração .bashrc, caso não estejam, faça a inclusão no final do arquivo:
#### export PATH="$HOME/.pyenv/bin:$PATH"
#### eval "$(pyenv init -)"
#### eval "$(pyenv virtualenv-init -)"
### Como usar?
### Para listar tudo que se pode instalar com o pyenv , faça:
#### pyenv install -l
### Instale uma versão do Python, por exemplo, 3.9.1:
#### pyenv install 3.9.1
### Faça com que a versão que você acabou de instalar, seja a versão global de seu sistema:
#### pyenv global 3.9.1
### Verifique se essa versão foi setada:
#### pyenv global
### Liste todas as versões que já foram baixadas:
#### pyenv versions



-------------------------------------------------
## Pip
### O que é?
#### Pip é o gerenciador de pacotes do python. É um cliente de linha de comandos utilizado para controle das depêndencias do projeto.
### Para que serve?
#### Utilizaremos o pip para controlar a versão das bibliotecas utilizadas para desenvolvimento do sistema. O pip nos permite baixar uma versão específica de uma biblioteca como por exemplo python3 -m pip install fastapi==0.43.0 .
### Como instalar?
#### Esta ferramenta não vem por padrão no sistema operacional Ubuntu e pode ser instalada utilizando o comando:
#### sudo apt install python3-pip .
### Vamos verificar se deu tudo certo?
#### Abra um terminal e digite python3 -m pip --version 



-------------------------------------------------
## Venv
### O que é?
#### Responsável por criar ambientes virtuais Python e provê um isolamento dos pacotes instalados e suas respectivas versões. É um cliente de linha de comando que auxilia na separação de ambientes para diferentes projetos.
### Para que serve?
#### Iniciamos um projeto que tem uma biblioteca na versão 1.4 , e de repente, um novo projeto é iniciado na versão 2.0 . O que fazer? Será que são compatíveis? E se eu atualizo o sistema e a versão antiga para de funcionar?
#### É onde o venv entra, ele serve para isolar ambientes entre projetos, ou seja, eu consigo ter dois projetos rodando, em dois ambientes diferentes, com versões diferentes da mesma biblioteca.
### Como instalar?
#### Versões atuais do Ubuntu já vem com python 3 instalado. Para as mais antigas utilize o comando: 
#### sudo apt install python3-venv .
### Vamos verificar se deu tudo certo?
#### Em um terminal digite python3 -m venv -h



-------------------------------------------------
## Flake8
### O que é?
#### Flake8 é um programa de linha de comando que verifica seu código e busca por erros ou formatações que não seguem o guia de estilo padrão do python, conhecido como PEP-8 . Além disso também verifica a complexidade ciclamática do seu código.
### Para que serve?
#### É muito comum cometermos alguns erros de sintaxe, principalmente quando ainda estamos nos familiarizando com uma linguagem nova. Assim como durante o nosso dia a dia podemos esquecer algum código não utilizado. Esta ferramenta vai analisar o seu código e procurar possíveis erros, evitando assim que só ocorram no momento em que o código for executado. Esta ferramenta também aponta possíveis linhas que não estão seguindo o estilo de código definido para a linguagem python. Outra coisa bem comum quando estamos escrevendo código é que uma parte dele começa a se tornar tão complexa que há n caminhos por onde seu algoritmo pode seguir. Normalmente isto indica que devemos modificar o código para torná-lo mais simples e legível. O Flake8 irá apontar qual parte do seu código está complexa e que deve ser modificada. Esta ferramenta será integrada ao editor, dessa maneira, ao salvar o arquivo, teremos os erros encontrados apontados diretamente no mesmo.
### Como instalar?
#### O pacote flake8 pode ser instalado utilizando utilizando a ferramenta pip vista anteriormente. Vamos utilizar sudo neste caso para garantir que ela esteja disponível para todos os usuários do sistema operacional. Digite o comando abaixo:
#### sudo python3 -m pip install flake8
### Vamos verificar se deu tudo certo?
#### Digite o comando python3 -m flake8 --version



-------------------------------------------------
## Black
### O que é?
#### Black é o formatador de código Python intransigente. Ao usá-lo, você concorda em ceder o controle sobre as minúcias da formatação manual. Em troca, o black dá a você velocidade, determinismo e liberdade do irritante pycodestyle sobre formatação. Você economizará tempo e energia mental para assuntos mais importantes.
### Para que serve?
#### O black é um formatador automático de código, ele irá modificar o seu código seguindo o guia de estilo do Python. Iremos configurá-lo junto ao nosso editor para que a formatação seja feita através de um atalho do teclado como shift + ctrl + i .
### Como instalar?
#### O pacote black pode ser instalado utilizando utilizando a ferramenta pip vista anteriormente. Vamos utilizar sudo neste caso para garantir que ela esteja disponível para todos os usuários do sistema operacional. Digite o comando abaixo:
#### sudo python3 -m pip install black
### Vamos verificar se deu tudo certo?
#### Digite o comando python3 -m black --version



-------------------------------------------------
## VSCode(Python)
### O que é?
#### O VSCode é um editor de texto e possui uma excelente extensão para Python que pode ser instalada através da marketplace.
### Para que serve?
#### O plugin de Python para VSCode fornece auto-complete , integração com os linters vistos anteriormente, também é uma ferramenta para depuração de código.
### Como instalar?
#### Abra o VS Code Quick Open (Ctrl+P) , cole o comando a seguir e pressione enter:
#### ext install ms-python.python
#### Após instalar a extensão, digite ctrl + shift + p , vá em Preferences: Open Settings (JSON) e acrescente as seguintes configurações:
#### // ...
####     "python.linting.enabled": true,
####     "python.linting.flake8Enabled": true,
####     "python.formatting.blackArgs": [
####         "-l 79"
####     ],
####     "python.formatting.provider": "black",
#### // ...
### Vamos verificar se deu tudo certo?
#### Abra um arquivo com extensão .py no VSCode e digite o código lista = [1,2,3] . Salve o arquivo e um aviso de erro deve acontecer. Passando o mouse sobre a linha veremos que o erro é: missing whitespace after ','flake8(E231). Para corrigir e testar se o nosso formatador está funcionando corretamente, digite ctrl + shift + i . Após salvar novamente o erro deve ter desaparecido. Caso isto não aconteça certifique que tenha feitos os passos anteriormente para instalação do flake8 e black.



-------------------------------------------------
## CodeRunner
### O que é?
#### Extensão do VSCode que permite rodar códigos ou trechos de códigos em mais de 30 linguagens de programação e adicionar também comandos customizados.
### Para que serve?
#### Rodar trechos de códigos ou o código inteiro sem sair do VSCode.
### Como instalar?
#### Abra o VS Code Quick Open (Ctrl+P) , cole o comando a seguir e pressione enter:
#### ext install formulahendry.code-runner
#### Após instalar a extensão, digite ctrl + shift + p , vá em Preferences: Open Settings (JSON) e acrescente as seguintes configurações:
#### // ...
####     "code-runner.executorMap": {
####         "python": "python3 -u"
####     },
####     "code-runner.runInTerminal": true,
#### // ...
### Esta configuração garante que nosso script será executado utilizando a versão 3 do Python. Vamos verificar se deu tudo certo?
#### Escreva um pequeno código como print("Olá Mundo") e apertando ctrl + alt + N o código será executado.