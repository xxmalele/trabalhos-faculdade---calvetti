from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Função para criptografar os dados
def criptografar(texto, chave):
    # Gerar um vetor de inicialização (IV) aleatório (necessário para o modo CBC)
    iv = os.urandom(16)  # AES usa IV de 16 bytes

    # Criar o objeto de cifra AES no modo CBC (Cipher Block Chaining)
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Completar o texto com padding para que seu tamanho seja múltiplo de 16 (tamanho do bloco AES)
    padding = 16 - len(texto) % 16
    texto_completo = texto + chr(padding) * padding

    # Criptografar o texto
    texto_criptografado = encryptor.update(texto_completo.encode('utf-8')) + encryptor.finalize()

    # Retornar o texto criptografado e o IV utilizado
    return iv + texto_criptografado  # Concatenamos o IV com o texto criptografado

# Função para descriptografar os dados
def descriptografar(texto_criptografado, chave):
    # O IV é armazenado nos primeiros 16 bytes do texto criptografado
    iv = texto_criptografado[:16]
    texto_criptografado = texto_criptografado[16:]

    # Criar o objeto de cifra AES no modo CBC
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografar o texto
    texto_descriptografado = decryptor.update(texto_criptografado) + decryptor.finalize()

    # Remover o padding (último byte indica o número de caracteres de padding)
    padding = texto_descriptografado[-1]
    return texto_descriptografado[:-padding].decode('utf-8')

# Exemplo de uso
chave = os.urandom(32)  # Gerar uma chave de 256 bits (32 bytes) para o AES
texto = "Texto confidencial que precisa ser criptografado."

# Criptografando o texto
texto_criptografado = criptografar(texto, chave)
print(f"Texto Criptografado: {texto_criptografado.hex()}")

# Descriptografando o texto
texto_descriptografado = descriptografar(texto_criptografado, chave)
print(f"Texto Descriptografado: {texto_descriptografado}")
