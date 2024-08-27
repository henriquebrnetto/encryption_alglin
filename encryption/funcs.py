import numpy as np

def gerar_matrizes_de_permutacao(N : int) -> tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """

    permutations = (np.random.permutation(np.eye(N)), np.random.permutation(np.eye(N)))
    while (np.array_equal(permutations[0], np.eye(N)) or np.array_equal(permutations[1], np.eye(N)) or np.array_equal(permutations[0], permutations[1])):
        
        if np.array_equal(permutations[0], np.eye(N)):
            permutations = (np.random.permutation(np.eye(N)), permutations[1])
        
        if np.array_equal(permutations[1], np.eye(N)):
            permutations = (permutations[0], np.random.permutation(np.eye(N)))

        
        if np.array_equal(permutations[0], permutations[1]):
            rand = 1 if np.random.random() > 0.5 else 0
            permutations = (np.random.permutation(np.eye(N)) if rand == 0 else permutations[0],
                            np.random.permutation(np.eye(N)) if rand == 1 else permutations[1])
    return permutations


def encriptar_enigma(mensagem : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    """
    Encripta uma mensagem usando duas matrizes de permutação P e Q.
    """
    
    mensagem = np.array([ord(c) for c in mensagem])
    enc = P.dot(Q).dot(mensagem)
    return ''.join(np.array([chr(int(c)) for c in enc]))


def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    """
    Decripta uma mensagem encriptada usando duas matrizes de permutação P e Q.
    """
    
    mensagem_encriptada = np.array([ord(c) for c in mensagem_encriptada])
    dec = np.linalg.inv(Q).dot(np.linalg.inv(P)).dot(mensagem_encriptada)
    return ''.join(np.array([chr(int(c)) for c in dec]))