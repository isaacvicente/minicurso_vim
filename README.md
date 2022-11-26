# Mini curso de Vim PET UFCG
<div align="center">
  <img src="/assets/vim.png" width= "100%" />
</div>

# Introdução

## O que é o Vim?

[Vim](https://www.vim.org/) é um editor de texto gratuito e open source
já instalado na maioria dos sistemas UNIX. Lançado em 1991, o Vim é um clone melhorado
do antigo [vi](https://en.wikipedia.org/wiki/Vi), de 1976.

Uma das principais características do Vim é que ele foi desenvolvido
para ser usado principalmente em uma interface de linha de comando, embora tenha
sua versão gráfica. Assim, para se navegar num texto ou editá-lo, usa-se espertas
combinações de teclas do teclado, o que facilitava a vida dos antigos usuários
de vi, época tal em que nem exista mouse para computadores pessoais.
> O mouse começou a ganhar popularidade com o lançamento do
[Apple Lisa](https://pt.wikipedia.org/wiki/Apple_Lisa), em 1983.

## Por que usar Vim?

É importante ressaltar que o Vim foi feito por programadores para programadores.
Logo, se você está lendo esse texto, muito provavelmente é um programador ou então
pretende ser. Isso não quer dizer, claro, que o Vim te fará um excelente programador
da noite pro dia (ou de uma semana pra outra).

Ao invés de pensar no curto ou médio prazo, imagine como você estará daqui a alguns meses,
ou até anos, depois de começar a usar o Vim para a maioria das tarefas. O começo será bem
incômodo, talvez estressante pra alguns, porém, com paciência e prática, você estará no
mesmo nível em que estava antes de usar o Vim. A partir daí, perceberá que muitos dos
comandos que precisou lembrar diversas vezes serão, agora, parte de sua
[memória muscular](https://en.wikipedia.org/wiki/Muscle_memory), e que aos poucos você
sente que nunca para de aprender.

Como programadores, passamos muito tempo editando código, e por isso, masterizar um editor
de texto é um grande investimento a ser feito. O Vim é, afinal de contas, uma ferramenta.
Ao decorrer da jornada, você perceberá que não é suficiente apenas saber o mínimo para
construir *X*, uma vez que estará se limitando a construir *Y*. Em outras palavras,
quanto mais sua caixinha de ferramentas expandir, mais oportunidades terá.
Ora, de que adianta dominar desenvolvimento web e não saber usar Git? Uma hora ou outra,
tal ferramenta será extremamente útil. Alguém poderia argumentar: *ah, mas não preciso saber
nenhum comando de Git, pois há várias interfaces gráficas pro Git onde posso fazer "tudo"
pelo mouse*. OK, espertinho, mas e se aparecer um problema (aqueles que aparecem na pior
hora possível) que seus clicks com o mouse são incapazes de resolver?

Perceba que é muito fácil depender de uma interface gráfica como essa, uma vez que não temos
que aprender muita coisa, não? Pois bem, é aí que mora o perigo: tendemos a, de certa forma,
sermos dominados pela ferramenta, e não o contrário. Assim, o programador que investiu seu
tempo realmente aprendendo Git (da linha de comando) com certeza saberá lidar melhor com o problema pois
mesmo que não saiba a resposta imediata, terá memória de conteúdos úteis que viu anteriormente,
os quais estão cheios de referências técnicas, isto é, a chave pro nosso problema muito
provavelmente estará lá.

Assim, *programadores curiosos se destacam em relação aos que não são*, já que investem tempo suficiente
pra dominarem o que usam. Finalmente, te rebato a pergunta: **e por que não usar Vim?**

## Filosofia do Vim

Por mais que isso te pareça estranho, é comum termos vários programas com suas filosofias próprias:
regras (abordagens) gerais que guiam o desenvolvimento de uma aplicação. Como muitos outros
softwares, Vim também tem sua filosofia.

Vim adere à filosofia de edição modal. Isso significa que ele fornece vários modos e o significado
das teclas muda de acordo com o modo. Você navega pelos arquivos no *modo normal*, insere texto no *modo
de inserção*, seleciona linhas no *modo visual*, acessa comandos no *modo de linha de comando* e assim por diante.
Isso pode parecer complicado no começo, mas tem uma grande vantagem: você não precisa quebrar os dedos segurando
várias teclas ao mesmo tempo, na maioria das vezes basta pressioná-las uma após a outra. Quanto mais comum
a tarefa, menos teclas são necessárias.

Um conceito relacionado que funciona bem com a edição modal são os operadores e movimentos. 
Os operadores iniciam uma determinada ação, por exemplo, alterar, remover ou selecionar texto.
Em seguida, você especifica a região do texto na qual deseja atuar usando um movimento.
Para alterar tudo entre parênteses, use `ci(` (leia alterar parênteses internos ou 
***c**hange **i**nner parentheses*). Para remover um parágrafo inteiro de texto, 
use `dap` (leia excluir ao redor do parágrafo ou ***d**elete **a**round **p**aragraph*).

Se você vir usuários avançados do Vim trabalhando, notará que eles falam a linguagem do Vim,
assim como os pianistas manuseiam seus instrumentos. Operações complexas são feitas usando
apenas alguns pressionamentos de tecla. Eles nem pensam mais nisso, pois a memória muscular
já assumiu o controle. Isso reduz a [carga cognitiva](https://pt.wikipedia.org/wiki/Esfor%C3%A7o_cognitivo)
e ajuda a focar na tarefa real.

O resultado final é um editor que pode corresponder à velocidade com que você pensa.
