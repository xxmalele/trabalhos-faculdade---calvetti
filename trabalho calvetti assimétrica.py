from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Função para gerar chaves pública e privada RSA
def gerar_chaves():
    # Gerar a chave privada RSA
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Obter a chave pública correspondente
    chave_publica = chave_privada.public_key()

    return chave_privada, chave_publica

# Função para criptografar dados com a chave pública
def criptografar_dado(chave_publica, dado):
    # Criptografar o dado com a chave pública utilizando PKCS1v15
    dado_criptografado = chave_publica.encrypt(
        dado.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return dado_criptografado

# Função para descriptografar dados com a chave privada
def descriptografar_dado(chave_privada, dado_criptografado):
    # Descriptografar o dado com a chave privada utilizando OAEP
    dado_descriptografado = chave_privada.decrypt(
        dado_criptografado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return dado_descriptografado.decode('utf-8')

# Função principal
def main():
    # Gerando as chaves pública e privada
    chave_privada, chave_publica = gerar_chaves()

    # Perguntar ao usuário o que deseja criptografar
    texto_original = input("Digite o texto que deseja criptografar: ")

    # Criptografando o texto com a chave pública
    texto_criptografado = criptografar_dado(chave_publica, texto_original)
    print(f"Texto Criptografado (em formato bytes): {texto_criptografado}")

    # Descriptografando o texto com a chave privada
    texto_descriptografado = descriptografar_dado(chave_privada, texto_criptografado)
    print(f"Texto Descriptografado: {texto_descriptografado}")

if __name__ == "__main__":
    main()
