import os
import sys
import time
import subprocess

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def simular_caos_cmd(nome_membro):
    """Executa comandos visuais inofensivos em um novo CMD."""
    
    # Comandos visuais e inofensivos para simular atividade
    comandos_caoticos = [
        "color 0a", # Muda para a cor verde de 'Hacker'
        f"title C.H.A.O.S. - Intrusão Ativa por {nome_membro}",
        "echo ----------------------------------------------------",
        "echo Iniciando processo de varredura e injecao de dados...",
        "echo [200] Conexao com o kernel estabelecida.",
        "tree C:\\ /f /a", # Comando que gera muita saída rapidamente
        "echo ----------------------------------------------------",
        "ping 127.0.0.1 -n 5 > NUL", # Pequena pausa
        "echo [404] Falha ao encontrar dados. Tentando desvio...",
        "dir /s /b C:\\Windows\\System32\\*.exe", # Varre arquivos do sistema (sem modificar)
        "echo Comando Perigoso >> NUL", # Simula a digitação de algo perigoso
        "echo ----------------------------------------------------",
        "echo [301] Redirecionamento completo. Executando etapa final..."
    ]

    # Cria um script temporário para rodar os comandos sequencialmente
    script_path = "temp_chaos.bat"
    with open(script_path, "w") as f:
        # Adiciona o aviso de parada no final
        f.write("@echo off\n")
        for cmd in comandos_caoticos:
            f.write(cmd + "\n")
        f.write("echo. & echo. & echo -------------------------------")
        f.write("echo | AVISO ÉTICO: Teste visual finalizado |")
        f.write("echo -------------------------------")
        f.write("timeout /t 10\n") # Espera 10 segundos antes de fechar o CMD
        f.write("exit\n")

    # Abre o novo CMD e executa o script (simulando a abertura 'do nada')
    subprocess.Popen(['cmd.exe', '/c', script_path])
    time.sleep(1) # Pequena pausa para o novo CMD aparecer

    # O Debugger deve remover o script após o uso:
    try:
         os.remove(script_path)
    except Exception as e:
         pass


def iniciar_simulador_seguro():
    """Lógica principal: Autenticação, permissão e simulação."""
    
    # --- Passo 1: Autenticação de Segurança (Debugger) ---
    print("---------------------------------------")
    print("🔒 PROTOCOLO MESTRE DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Simulador de Intrusão)")
    print("---------------------------------------")
    
    senha_mestre = input("Digite a SENHA DA REDE MESTRE: ")
    
    if senha_mestre != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança Debugger incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO!")
    
    # --- Passo 2: Protocolo de Permissão do Dispositivo ---
    print("\n⚠️ PROTOCOLO ÉTICO: Permissão para Invasão Visual.")
    senha_alvo = input("Digite a SENHA REAL DO WINDOWS para confirmar a permissão de teste: ")
    nome_membro = input("Digite o nome do Membro para aparecer no CMD: ")

    if not senha_alvo:
        print("Senha do dispositivo alvo vazia. Encerrando por falta de autorização ética.")
        sys.exit(0)
    
    # --- Passo 3: Início da Simulação ---
    print("\n💥 INICIANDO INTRUSÃO CAÓTICA VISUAL...")
    print("Várias janelas CMD (inofensivas) serão abertas para simular o caos.")
    
    # Abre múltiplas janelas CMD para o efeito caótico
    for i in range(3):
        simular_caos_cmd(nome_membro)
        time.sleep(0.5)

    # --- Passo 4: Simulação de Reinicialização e Aviso ---
    print("\n----------------------------------------------------")
    print("Sinal do Kernel: Comandos executados. Forçando REINICIALIZAÇÃO...")
    print("... (Aqui o Windows reiniciaria em um ataque real) ...")
    time.sleep(3) # Pausa dramática
    print("WINDOWS REINICIADO E DE VOLTA AO NORMAL.")
    print("----------------------------------------------------")
    print("AVISO FINAL: Nenhum arquivo foi modificado. Este foi apenas um teste visual.")

if __name__ == "__main__":
    iniciar_simulador_seguro()
