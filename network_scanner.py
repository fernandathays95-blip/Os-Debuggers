import sys
from scapy.all import Ether, ARP, srp

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def censurar_ip(ip_completo):
    """Censura os dois últimos octetos do IP para fins de segurança."""
    try:
        partes = ip_completo.split('.')
        # Retorna os dois primeiros octetos + censura
        return f"{partes[0]}.{partes[1]}.***.***"
    except:
        return "IP Inválido"

def iniciar_scanner_seguro():
    """Lógica principal: Autenticação, varredura e saída censurada."""
    
    # --- Passo 1: Autenticação de Segurança ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Apenas White Hat)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar o scanner: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO! Iniciando scanner de rede.")
    
    # --- Passo 2: Configuração e Execução do Scan ---
    # Solicita o intervalo da rede (ex: 192.168.1.0/24)
    target_range = input("Digite o ALVO da rede (formato CIDR, ex: 192.168.1.0/24): ")
    
    print(f"\nVarrendo {target_range}. Aguarde...")
    
    # Cria o pacote ARP para a varredura
    pacote_arp = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_range)
    
    # Envia e recebe as respostas (timeout de 1 segundo)
    try:
        resultado_scan, sem_resposta = srp(pacote_arp, timeout=1, verbose=False)
    except OSError as e:
        print(f"\n🚨 ERRO: Não foi possível enviar os pacotes. Execute como administrador/root. Detalhes: {e}")
        sys.exit(1)
        
    dispositivos = []
    
    # Processa os resultados
    for enviado, recebido in resultado_scan:
        ip = recebido.psrc
        mac = recebido.hwsrc
        
        dispositivos.append({
            'ip_censurado': censurar_ip(ip),
            'mac_completo': mac
        })

    # --- Passo 3: Exibição Segura dos Resultados ---
    print("\n----------------------------------------------------")
    print(f"📡 Dispositivos encontrados ({len(dispositivos)} no total):")
    print("----------------------------------------------------")
    print("    IP CENSURADO      |      MAC (Identificador)")
    print("----------------------|---------------------------")
    
    for disp in dispositivos:
        print(f"{disp['ip_censurado']:<20} | {disp['mac_completo']}")
        
    print("----------------------------------------------------")
    print("🔒 Fim do Scanner. IPs exibidos com os dois últimos octetos censurados para segurança.")

# Inicia o script
if __name__ == "__main__":
    iniciar_scanner_seguro()
