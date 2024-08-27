# encryption_alglin
Encryption functions for Linear Algebra project.

Este pacote possui 3 funções:

- gerar_matrizes_de_permutacao:  
    Nesta função o input é um número inteiro, e o output são duas matrizes identidade com permutações aleatórias nas posições des valor 1.

    $$
    \begin{equation}
    A  \in {\rm I\!R}^{3x3}
    \end{equation}
    $$

    $$
    
    A =
    \begin{equation}
    \begin{pmatrix}
    1      & 0       & 0  \\
    0      & 1       & 0  \\
    0      & 0       & 1  \\
    \end{pmatrix}
    \end{equation}

    $$

    $$
    
    gerarMatrizesDePermutacao(A) =
    \begin{equation}
    \begin{drcases}
    \begin{pmatrix}
    0      & 1       & 0  \\
    0      & 0       & 1  \\
    1      & 0       & 0  \\
    \end{pmatrix}
    ,
    \begin{pmatrix}
    0      & 1       & 0  \\
    1      & 0       & 0  \\
    0      & 0       & 1  \\
    \end{pmatrix}
    \end{drcases}
    \end{equation}

    $$