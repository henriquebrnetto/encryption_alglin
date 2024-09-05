# encryption_alglin
Encryption functions for Linear Algebra project.

Este pacote possui 3 funções principais:

```
gerar_matrizes_de_permutacao:
```

- Nesta função o input é um número inteiro N (neste caso deve ser o tamanho das letras únicas disponíveis na sua mensagem), e o output são duas matrizes identidade NxN com permutações aleatórias.
- Se a função for chamada sem input, N será a quantidade de caracteres no Código ASCII + todos os caracteres com acento do português.

    $$
    \begin{equation}
    A  \in {\rm I\!R}^{NxN}
    \end{equation}
    $$
  
```
encriptar_enigma:
```

- O input desta função é a mensagem (string), e duas matrizes de transformação, P e Q (ambos numpy.array).
- É necessário ter um alfabeto definido para conseguir utilizar a função. Como temos um alfabeto pré-definido no início do arquivo com as funções, o usuário não deve se preocupar com isso.
- Sendo X a matriz que representa a mensagem original, e X' a matriz da palavra encriptada, o cálculo realizado é demonstrado a seguir:

    $$
    \begin{equation}
    X'_{*,i} = (Q^{(i-1)} \cdot P) \cdot X_{*,i}
    \end{equation}
    $$

```
decriptar_enigma:
```

- O input desta função é a mensagem encriptada (string), e as duas matrizes de transformação, P e Q (ambos numpy.array) utilizadas para encriptar a mensagem anteriormente.
- É necessário ter um alfabeto definido para conseguir utilizar a função. Como temos um alfabeto pré-definido no início do arquivo com as funções, o usuário não deve se preocupar com isso.
- Sendo X a matriz que representa a mensagem original, e X' a matriz da palavra encriptada, o cálculo realizado é demonstrado a seguir:

    $$
    \begin{equation}
    X_{*,i} =  P^{-1} \cdot (Q^{-1})^{(i-1)} \cdot X'_{*,i}
    \end{equation}
    $$



### Pip install

```
pip install git+https://github.com/henriquebrnetto/encryption_alglin.git
```

### Exemplo de uso das funções:

```
import encryption.funcs as enc

msg = 'Esta é uma mensagem secreta que será encriptada e decriptada pelo enigma'

# chamar a função 'gerar_matrizes_de_permutacao()' sem argumento é a mesma coisa que utilizar 'len(enc.alphabet)' como input
P, Q = enc.gerar_matrizes_de_permutacao()
#P, Q = enc.gerar_matrizes_de_permutacao(len(np.unique(list(msg))))

encrypt = enc.encriptar_enigma(msg, P, Q)
decrypt = enc.decriptar_enigma(encrypt, P, Q)
```

Utilizando o argumento 'len(np.unique(list(msg)))' na função 'gerar_matrizes_de_permutacao()' são criadas duas matrizes apenas com os caracteres únicos disponíveis na variável 'msg'.