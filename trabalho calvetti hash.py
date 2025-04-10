import hashlib

# Função para gerar o hash
def gerar_hash(texto, algoritmo="sha256"):
    # Criar o objeto hash de acordo com o algoritmo escolhido
    hash_obj = hashlib.new(algoritmo)
    
    # Passar o texto para o hash (precisa ser convertido para bytes)
    hash_obj.update(texto.encode('utf-8'))
    
    # Retornar o hash em formato hexadecimal
    return hash_obj.hexdigest()

# Exemplo de uso
texto = "Exemplo de texto para gerar o hash"
hash_gerado = gerar_hash(texto)

print(f"Texto: {texto}")
print(f"Hash SHA-256: {hash_gerado}")
