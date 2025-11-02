import hashlib
import os
import secrets
import string
import sys

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def gerar_hash(texto, algoritmo='sha256'):
    """Gera um hash criptográfico a partir de uma string de texto."""
    h = hashlib.new(algoritmo)
    h.update(texto.encode('utf-8'))
    return h.hexdigest()

def gerar_senha_forte(comprimento=16):
    """Gera uma senha forte e aleatória."""
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    
    # Garante que a senha contenha pelo menos um de cada tipo para ser forte
    while True:
        senha = ''.join(secrets.choice(alfabeto) for i in range(comprimento))
        if (any(c.islower() for c in senha) and
                any(c.isupper() for c in senha) and
                any(c.isdigit() for c in senha) and
                any(c in string.punctuation for c in senha)):
            break
    return senha

def iniciar_gerador_seguro():
    """Lógica principal: Autenticação e seleção de função."""
    
    # --- Passo 1: Autenticação de Segurança ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Hashes e Senhas)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO! Gerador de Segurança pronto.")
    
    # --- Passo 2: Seleção de Função ---
    print("\nEscolha a funcionalidade:")
    print("1: Gerar HASH de texto (para verificação de integridade)")
    print("2: Gerar Senha Forte (para criar credenciais seguras)")
    
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == '1':
        texto = input("Digite o texto para ser *hashed*: ")
        algoritmo = input("Escolha o algoritmo (sha256, sha512, md5, etc.): ") or 'sha256'
        
        resultado_hash = gerar_hash(texto, algoritmo)
        
        print("\n------------------- RESULTADO HASH ------------------")
        print(f"Texto Original: {texto}")
        print(f"Algoritmo:      {algoritmo}")
        print(f"Hash Gerado:    {resultado_hash}")
        print("-----------------------------------------------------")
        
    elif escolha == '2':
        try:
            comprimento = int(input("Digite o comprimento desejado da senha (recomendado 16 ou mais): ") or 16)
        except ValueError:
            print("Comprimento inválido. Usando 16 por padrão.")
            comprimento = 16
            
        senha = gerar_senha_forte(comprimento)
        
        print("\n------------------ SENHA FORTE GERADA -----------------")
        print(f"Comprimento: {comprimento}")
        print(f"SENHA:       {senha}")
        print("-----------------------------------------------------")
        print("⚠️ COPIE A SENHA IMEDIATAMENTE. Ela não será armazenada.")
        
    else:
        print("Escolha inválida. Encerrando.")

if __name__ == "__main__":
    iniciar_gerador_seguro()
