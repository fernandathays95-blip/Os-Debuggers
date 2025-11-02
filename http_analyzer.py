import requests
import sys

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def analisar_cabecalhos(url):
    """Realiza uma requisição GET e analisa os cabeçalhos de segurança."""
    try:
        # Define um User-Agent para identificação ética (White Hat)
        headers = {
            'User-Agent': 'Debuggers-Ethical-Header-Analyzer/1.0',
            'Accept-Encoding': 'gzip, deflate'
        }
        
        # Faz a requisição sem seguir redirecionamentos para analisar o primeiro destino
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        
    except requests.exceptions.RequestException as e:
        return f"❌ ERRO DE CONEXÃO: Não foi possível conectar à URL. Detalhes: {e}"

    # Cabeçalhos de Segurança Chave para a Análise
    cabecalhos_seguranca = {
        "Strict-Transport-Security": "Proteção contra Downgrade de Protocolo (HSTS).",
        "Content-Security-Policy": "Prevenção contra XSS e injeção de dados.",
        "X-Content-Type-Options": "Prevenção de MIME-Sniffing.",
        "X-Frame-Options": "Prevenção contra Clickjacking.",
        "Referrer-Policy": "Controle de informações de referência.",
        "Permissions-Policy": "Controle de acesso a APIs do navegador.",
        "X-XSS-Protection": "Configuração de proteção contra XSS.",
        "Server": "Identificação do Servidor (Recomendado ocultar/generalizar)."
    }

    analise = f"\n--- 🌐 Análise de Cabeçalhos HTTP para {url} ---\n"
    analise += f"Status Code (HTTP): {response.status_code}\n"
    
    
    analise += "\n--- CABEÇALHOS DE SEGURANÇA (Debuggers Review) ---\n"
    
    # Checa a presença e o valor dos cabeçalhos de segurança
    for cabecalho, descricao in cabecalhos_seguranca.items():
        valor = response.headers.get(cabecalho)
        
        if valor:
            analise += f"✅ {cabecalho}: {valor} (OK: {descricao})\n"
        else:
            analise += f"❌ {cabecalho}: AUSENTE (FALHA: {descricao})\n"
            
    analise += "\n--- OUTROS CABEÇALHOS RECEBIDOS ---\n"
    
    # Exibe todos os outros cabeçalhos para contexto
    for chave, valor in response.headers.items():
        if chave not in cabecalhos_seguranca:
            analise += f"   {chave}: {valor}\n"

    analise += "----------------------------------------------------"
    return analise

def iniciar_analisador_seguro():
    """Lógica principal: Autenticação e análise."""
    
    # --- Passo 1: Autenticação de Segurança ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Analisador HTTP)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar a análise: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO! Analisador de Cabeçalhos pronto.")
    
    # --- Passo 2: Configuração do Alvo ---
    url_alvo = input("Digite a URL COMPLETA para análise (ex: https://www.google.com): ")
    
    if not url_alvo.startswith(('http://', 'https://')):
        url_alvo = 'https://' + url_alvo
        
    print(f"\nIniciando análise ética de cabeçalhos em: {url_alvo}")
    
    resultado = analisar_cabecalhos(url_alvo)
    print(resultado)

if __name__ == "__main__":
    iniciar_analisador_seguro()
