import time
import random
import string
import sys

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def gerar_tentativa(comprimento_max):
    """Gera uma string aleatória para simular uma tentativa de senha."""
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    # Usa um comprimento aleatório entre 1 e o máximo para simular várias tentativas
    comprimento = random.randint(1, comprimento_max) 
    return ''.join(random.choice(alfabeto) for _ in range(comprimento))

def iniciar_teste_forca_bruta():
    """Lógica principal: Autenticação, obtenção de senha e simulação."""
    
    # --- Passo 1: Autenticação de Segurança (Debugger) ---
    print("---------------------------------------")
    print("🔒 PROTOCOLO MESTRE DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Teste de Força Bruta)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar a ferramenta: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança Debugger incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO!")
    
    # --- Passo 2: Protocolo de Segurança do Dispositivo Alvo ---
    print("\n⚠️ PROTOCOLO ÉTICO: Teste de autorização do alvo.")
    senha_alvo = input("Digite a SENHA REAL DO DISPOSITIVO (Windows/Android) para dar permissão: ")
    
    if not senha_alvo:
        print("Senha do dispositivo alvo vazia. Encerrando por falta de autorização ética.")
        sys.exit(0)

    print(f"\nTeste autorizado. Senha alvo de {len(senha_alvo)} caracteres definida.")
    
    # --- Passo 3: Simulação de Brute Force ---
    tentativas = 0
    encontrada = ""
    start_time = time.time()
    
    print("\nSimulando Força Bruta (Tentativas em andamento)...")
    print("Aguarde (isso pode levar um tempo, dependendo da sua sorte no teste!).")
    
    # Define o comprimento máximo para a geração de tentativas
    comprimento_max = max(10, len(senha_alvo) + 2) 

    while encontrada != senha_alvo:
        encontrada = gerar_tentativa(comprimento_max)
        tentativas += 1
        
        # Mostra o progresso de tempos em tempos
        if tentativas % 500000 == 0:
            print(f"[{time.strftime('%H:%M:%S')}] Tentativas: {tentativas:,} | Última Tentativa: {encontrada[:15]}...")

        # Para evitar travar a máquina em senhas muito longas
        if tentativas > 10000000:
             print("\n⚠️ AVISO: Mais de 10 milhões de tentativas. Interrompendo simulação para evitar sobrecarga. Sua senha é forte!")
             break


    end_time = time.time()
    duracao = end_time - start_time
    
    # --- Passo 4: Resultados ---
    print("\n----------------------------------------------------")
    if encontrada == senha_alvo:
        print("🔓 DISPOSITIVO DESBLOQUEADO (SIMULADO)!")
        print(f"  Senha alvo: {senha_alvo}")
    else:
        print("🛑 SIMULAÇÃO INTERROMPIDA. A senha é muito longa/complexa para esta simulação.")

    print(f"  Tentativas Totais: {tentativas:,}")
    print(f"  Tempo de Duração: {duracao:.2f} segundos")
    print("----------------------------------------------------")
    print("\nAVISO ÉTICO: Este teste mostra a vulnerabilidade. A conexão por cabo foi simulada.")

if __name__ == "__main__":
    iniciar_teste_forca_bruta()
