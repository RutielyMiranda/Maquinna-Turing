##### Aluna: Rutiely Miranda de Sousa
##### Matricula: 20181BCC0035
##### Profº Thiago Freire
##### Materia: Teoria da Computação

### Código de implementação da Máquina de Turing

#### Foi definida uma máquina de Turing, que complementa uma entrada binária na fita, ou seja, uma entrada "1100011", por exemplo, será transformada em "0011100".

1. Σ = {0, 1}
2. Q = {init, final}
3. q 0 = inicial
4. q f = final

### Como rodar o código

#### Você pode usar o Run Python File do VSCode ou python init.py -> init refere-se ao nome do arquivo. Isso é executado no terminal da sua máquina, não esqueça de baixar o python.

Escolhi essa linguagem porque nunca estudei ela, foi um pouco dificil aprender um pouquinho dela nesse curto espaço de tempo. Pode ser até uma linguagem fácil, mas foi complexo pra mim aprender em pouco tempo. Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.

##### Breve explicação:

| (inicialização, 0) = (inicialização, 1, R) |
|-----------------------------------------------|
| Se a máquina estiver no estado "init" e um 0 |
| for lido pelo cabeçote, um 1 será escrito, o |
| estado mudará para "init" (então, na |
| verdade, não mudará) e o cabeçote será movido |
| um campo para o certo. |

| (inicialização, 1) = (inicialização, 0, R) |
|-----------------------------------------------|
| Se a máquina estiver no estado "init" e um 1 |
|for lido pelo cabeçote, um 0 será escrito, o |
| estado mudará para "init" (então, na verdade, |
| não mudará) e o cabeçote será movido um campo |
| para o certo. |

| δ(inicial,b) = (final, b, N) |
|-----------------------------------------------|
| Se um espaço em branco ("b"), definindo o |
| final da string de entrada, for lido, a TM |
| atingirá o estado final "final" e parará. |
