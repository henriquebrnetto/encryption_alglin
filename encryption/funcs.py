import numpy as np
import string

letras_acentuadas = ['á', 'à', 'â', 'ã', 'ä', 'é', 'è', 'ê', 'ë', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 'ô', 'õ', 'ö', 'ú', 'ù', 'û', 'ü', 'ç', 'Á', 'À', 'Â', 'Ã', 'Ä', 'É', 'È', 'Ê', 'Ë', 'Í', 'Ì', 'Î', 'Ï', 'Ó', 'Ò', 'Ô', 'Õ', 'Ö', 'Ú', 'Ù', 'Û', 'Ü', 'Ç']
alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace + ''.join(letras_acentuadas)

def transform_letter(letter) -> np.ndarray:
    """
    Transforma uma letra em um vetor one-hot.
    O vetor one-hot é um vetor de zeros com um 1 na posição da letra.

    Alphabet é um numpy array com todas as letras da mensagem e letras disponíveis para a criptografia.
    Se não for passado, ele é calculado automaticamente como as ocorrências únicas das letras da mensagem.
    """
    return np.array([1 if c == letter else 0 for c in alphabet])


def message_to_matrix(message : str) -> np.ndarray:
    """
    Transforma uma mensagem em uma matriz.
    Cada coluna da matriz é um vetor one-hot representando uma letra da mensagem.

    Alphabet é um numpy array com todas as letras da mensagem e letras disponíveis para a criptografia.
    Se não for passado, ele é calculado automaticamente como as ocorrências únicas das letras da mensagem.
    """

    return np.array([transform_letter(char) for char in message]).T

def matrix_to_message(matrix : np.ndarray) -> str:
    """
    Transforma uma matriz em uma mensagem.
    Cada coluna da matriz é um vetor one-hot representando uma letra da mensagem.

    Alphabet é um numpy array com todas as letras da mensagem e letras disponíveis para a criptografia.
    Se não for passado, ele é calculado automaticamente como as ocorrências únicas das letras da mensagem.
    """

    return ''.join([alphabet[np.argmax(col)] for col in matrix.T])


def gerar_matrizes_de_permutacao(N : int = len(alphabet)) -> tuple[np.ndarray, np.ndarray]:
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

    Alphabet é um numpy array com todas as letras da mensagem e letras disponíveis para a criptografia.
    Se não for passado, ele é calculado automaticamente como as ocorrências únicas das letras da mensagem.
    """

    message_matrix = message_to_matrix(mensagem)
    mult_matrix = P
    for i in range(np.shape(message_matrix)[1]):
        if i != 0:
            mult_matrix = Q.dot(mult_matrix)
        message_matrix[:, i] = mult_matrix.dot(message_matrix[:, i])

    return matrix_to_message(message_matrix)


def decriptar_enigma(mensagem_encriptada : str,
              P : np.ndarray,
              Q : np.ndarray) -> str:
    
    """
    Decripta uma mensagem encriptada usando duas matrizes de permutação P e Q.
    """
    
    message_matrix = message_to_matrix(mensagem_encriptada)

    mult_matrix = np.linalg.inv(P)
    Q = np.linalg.inv(Q)
    for i in range(np.shape(message_matrix)[1]):
        if i != 0:
            mult_matrix = mult_matrix.dot(Q)
        message_matrix[:, i] = mult_matrix.dot(message_matrix[:, i])

    return matrix_to_message(message_matrix)