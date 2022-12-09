# Vim, seu melhor amigo :sparkles: :technologist:

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
[Apple Lisa](https://pt.wikipedia.org/wiki/Apple_Lisa), em 1983).

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

Se eu te convenci, esses são os passos para você aprender o Vim (e qualquer outro editor de
texto):

- Começe com um tutorial (ou seja, esse mini curso)
- Use o editor para qualquer edição de código ou texto (mesmo que ao início
as coisas pareçam meio lentas)
- Aprenda constantemente e quando necessário, pois se você pensa que há
uma maneira de fazer algo de forma mais eficiente, muito provavelmente você está certo.
- ***Não decore nada***. Aprenda pelo **uso** do editor e suas necessidades com ele.
- Seja curioso. De vez em quando se pergunte: _o Vim pode fazer isso?_ Para isso, o Google
será seu melhor amigo: não só para aprender Vim, mas para diversas outras coisas.

> **Nota**: Nós forneceremos vários conteúdos extras para você seguir e se aprofundar.

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

# Fundamentos

## Modos do Vim

Diferente da maioria dos editores de texto/código que existem por aí, Vim tem o que se chama de
_modos_. O design do Vim é baseado na ideia de que um programador passa a maior parte do
seu tempo lendo, navegando e editando pequenos trechos de código, ao invés de escrever
continuamente grandes textos. Por isso o Vim possui múltiplos modos de operação:

- Normal: para se mover num texto e fazer edições
- Insert: para inserir texto
- Replace: para substituição de texto
- Visual (plain, line, block): para selecionar blocos de texto
- Command-line: para rodar um comando 

Teclas tem diferentes significados dependendo em qual modo você está. Por exemplo,
a letra `x` no modo _Insert_ significa literalmente o caractere 'x', mas no modo
_Normal_, essa tecla deleta o caractere debaixo do cursor, assim como no modo
_Visual_, que deleta o texto selecionado.

Em sua configuração padrão, Vim mostra em qual modo você está bem na parte
inferior esquerda. Seu modo inicial/padrão é o modo _Normal_ (quando você abre o editor).
Geralmente, você passará a maior parte do seu tempo entre os modos _Normal_ e _Insert_.

Para trocar de um modo para outro, você aperta a tecla `<ESC>`, indo para o modo _Normal_.
Do modo Normal, você vai para o modo Insert com `i`, para o modo Replace com `R`, para o modo
Visual com `v`, Visual Line com `V` ('v' maiúsculo), Visual Block com `<C-v>` (Ctrl-v, às vezes também escrito
como `^V`), e modo Command-line com `:`.

Sim, eu sei, isso tudo parece muito complicado. Mas não se preocupe, pois os modos do Vim
se tornarão algo bem familiar: e na verdade você os achará geniais.

Responda rápido: qual tecla te coloca no modo Normal e qual te tira de qualquer modo?

### Modo Normal

O modo Normal é o centro de tudo, pois é ele que te leva a todos os outros modos. Assim,
permaneça nesse o máximo possível, e troque para outro modo quando necessário.
Pense no modo Normal como onde você esculpe seu código/texto, seja lendo-o ou então
fazendo pequenas mudanças. Para ter certeza que você está no modo Normal, aperte
`<ESC>` e veja seu canto inferior à esquerda, onde aparecerá `NORMAL`.

> Por usarmos muito o `<ESC>` geralmente é bom mapeá-lo para outra tecla,
como o `<CAPSLOCK>`: essa tecla está na posição de nossos dedos no teclado chamada
__Home Row__. Não se preocupe com isso por enquanto.

### Modo Command-line

> **Nota**:
Os comandos do Vim são mnemônicos e, na maioria da vezes, fáceis de lembrar

Em modo Normal, você entra nesse modo apertando `:`.
Seu cursor pulará para a linha de comando na parte inferior da tela ao pressionar `:`.
Este modo tem muitas funcionalidades, incluindo abrir, salvar e fechar arquivos, assim como
[sair do Vim](https://twitter.com/iamdevloper/status/435555976687923200).

- `:q` (ou `:quit`) - para sair de um arquivo não modificado
- `:q!` - forçar a saída de um arquivo (modificado ou não)
- `:w` (ou `:write`) - salva o arquivo
- `:x` - salva o arquivo e sai ao mesmo tempo
(equivalente a `:wq` ou então `ZZ`)

### Modo Insert

Estando no modo Normal, há diversas formas de entrar no modo Insert:

- `i` ou `a` - para inserir texto antes do cursor ou depois do cursor, respectivamente
- `I` ou `A` - para inserir texto no começo ou no final da linha, respectivamente
> Lembre-se do `i` como `insert` e do `a` como `append`
- `o` ou `O` -  respectivamente, cria uma linha abaixo ou acima de onde você está e te coloca em modo Insert 
> Lembre-se do `<Shift>` quando for inserir _acima_ de onde você está
(o Shift é uma setinha para cima)

### Modo Visual

Você pode selecionar um pedaço de texto/código de diferentes formas:

- `v` - para selecionar o caractere abaixo do cursor
- `V` - para selecionar toda a linha em que o cursor está
- `<C-v>` - seguido de movimentos, seleciona um bloco de texto

Mas calma, o que são movimentos? Antes de saber os movimentos, vamos entender uma ideia chave do Vim.

## A interface do Vim é uma linguagem de programação

A ideia mais importante no Vim é que a própria interface do Vim é uma linguagem 
de programação. Teclas (com nomes mnemônicos) são comandos, e esses comandos expressam
ideias (pense no Vim realmente como uma linguagem, com verbos, substantivos e adjetivos). 
Isso permite movimentos e edições eficientes, especialmente quando os comandos se tornam 
[memória muscular](https://en.wikipedia.org/wiki/Muscle_memory).

### Movimentos

Repetindo, você deve passar a maior parte do tempo no modo Normal, usando comandos 
de movimento para navegar no arquivo. Os movimentos no Vim também são chamados de
“substantivos”, porque se referem a pedaços de texto.

- Movimentos básicos: 
    - `h` - direita
    - `j` - baixo
    - `k` - cima
    - `l` - esquerda
> Dica: o `j` se parece com uma seta pra baixo, não? 

- Palavras:
    - `w` - vai pro começo da próxima palavra
    - `b` - volta pro começo da palavra anterior
    - `e` - vai pro final da próxima palavra

- Linhas:
    - `0` - começo da linha
    - `^<Space>` - primeiro caractere da linha
    - `$` - final da linha

- Tela:
    - `H` - topo da tela
    - `M` - meio da tela
    - `L` - final da tela

- Scroll:
    - `<C-u>` - para cima (_**u**p_)
    - `<C-d>` - para baixo (_**d**own_)

- Arquivo:
    - `gg` - começo do arquivo
    - `G` - final do arquivo
    - `50%` - metade do arquivo (`100%` seria equivalente a `G`)

- Número da linha:
    - `:{n}` ou `{n}G` - vai para a linha de número `n`
> Você não tem que digitar os "{", apenas digite `10G`, por ex.

- Correspondência:
    - `%` - encontra o próximo `(`, `[` ou `{`

- Encontre:
    - `f{caractere}` - Posiciona o cursor em cima do `caractere`
    - `t{caractere}` - Posiciona o cursor antes do `caractere`
    - `F{caractere}` - Faz o mesmo que `f` mas de trás pra frente
    - `T{caractere}` - Faz o mesmo que `t` mas de trás pra frente 
    - `,` para o próximo item e `;` para o anterior

- Busca:
    - `/{expressão}` - Busca pelo item encontrado pela `expressão` regular
    - `n` para o próximo item e `N` para o anterior

### Edições

Tudo o que você fazia com o mouse agora você faz com o teclado usando comandos
de edição que compõem com comandos de movimento. Aqui é onde a interface do Vim
começa a parecer uma linguagem de programação. Os comandos de edição do Vim também 
são chamados de “verbos”, porque os verbos agem sobre substantivos.

- `d{movimento}` - Deleta tudo fornecido pelo `movimento`
    - Por exemplo, `dw` apaga a próxima palavra, `d0` apaga tudo até o começo da linha, `d$` até o final, etc
- `c{movimento}` - Muda tudo fornecido pelo `movimento`
    - `cw`, por exemplo, muda a próxima palavra
    - O mesmo que `d{movimento}` seguido de `i`
- `x` - Deleta o caractere sob o cursor (igual a `dl`)
- `s` - Muda o caractere sob o cursor (igual a `cl`)
- Modo Visual + manipulação
    - Selecione o texto, `d` para apagá-lo ou `c` para mudá-lo
- `u` para desfazer e `<C-r>` para refazer
- `y` - Copia o caractere/texto
- `p` - Cola o caractere/texto copiado
> **Nota**: `p` também cola o texto que foi deletado

### Contagens

Você pode combinar substantivos e verbos com uma contagem, que executará
uma determinada ação várias vezes.

- `3w` move 3 palavras para frente
- `5j` move cinco linhas para baixo
- `7dw` deleta 7 palavras

### Agora vamos à prática!

Siga os seguintes passos:

1. Clique nesse [link](/exercicios.txt) para acessar o arquivo
2. Sobre o botão `Raw` clique com o botão direito de seu mouse e selecione `Salvar link como`
3. Escolha o diretório `Downloads`

Dentro de seu terminal mova-se para Downloads com:
```bash
cd ~/Downloads
```
Abra seu arquivo:
```bash
vim exercicios.txt
```

## Buffers, windows e tabs

### Buffers

## Modo Vim em outros programas

### Por quê?

Já sabemos que o Vim não é exatamente fácil de ser usado no primeiro contato e que o
aprendizado leva algum tempo. Também sabemos que há toda uma filosofia por trás do
uso do Vim na edição de textos e que, uma vez que o usuário esteja familiarizado,
poderá colher os frutos do seu aprendizado editando texto de forma cada vez mais
eficaz e eficiente. 

Sabendo que grande parte do dia-a-dia de qualquer pessoa na Internet envolve escrever
textos, e que essa pessoa já utilize o Vim para programação, por quê não usar o Vim
e os seus comandos também em um navegador, gerenciador de arquivos... Ou até em um
player de música? Tratando-se de programação, o céu é o limite.

### Como isso funciona?

Podemos dividir o funcionamento do "modo Vim" nas aplicações em duas formas de
implementação: embutida na aplicação e através de plug-in.

Há aplicações que são intencionalmente criadas para serem operadas através de
atalhos semelhantes ao Vim. Nessa categoria encontraremos aplicações que nós
normalmente não conhecemos e que podem (ou não) ter todos os recursos que
esperamos, já que tendem a ser projetos menores e desenvolvidos especialmente
para ter um modo Vim.

Já outras aplicações podem ser estendidas, permitindo que desenvolvedores criem 
plug-ins que adicionam o modo Vim a elas. Essa característica é especialmente útil 
nos casos em que uma aplicação não é desenvolvida com o modo Vim em mente, mas que
a presença dele seria interessante. 

### Quais aplicações são compatíveis?

Temos uma listagem bastante completa de aplicações que ou possuem o modo Vim ou
permitem que ele seja adicionado no site [Big Pile of Vim-like](https://vim.reversed.top/apps).

Os destaques incluem:
- [NeoMutt](https://vim.reversed.top/item/neomutt): cliente de e-mails com modo Vim por padrão.
- [Ranger](https://vim.reversed.top/item/ranger): gerenciador de arquivos com modo Vim por padrão.
- [apvlv](https://vim.reversed.top/item/apvlv): visualizador de PDFs e ePUBs no estilo do Vim.
- [cmus](https://vim.reversed.top/item/cmus): um player de música não tão minimalista com modo Vim.
- [Vimium](https://vim.reversed.top/item/vimium-chrome): adiciona o modo Vim ao Chrome.
- [Vimium-FF](https://vim.reversed.top/item/vimium): adiciona o modo Vim ao Firefox.
