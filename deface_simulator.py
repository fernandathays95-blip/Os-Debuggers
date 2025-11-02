import http.server
import socketserver
import socket
import sys

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
PORTA_SERVIDOR = 8080
# ----------------------------------------

def get_local_ip():
    """Tenta obter o IP local da máquina para acesso na rede."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Não precisa estar acessível, apenas tentar se conectar a um IP externo
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1 (Verifique a conexão de rede)'
    finally:
        s.close()
    return IP

def criar_pagina_html(nome_membro):
    """Gera o conteúdo HTML com a mensagem solicitada."""
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Debuggers - Alerta de Teste</title>
        <style>
            body {{ background-color: #1a1a2e; color: #e94560; font-family: monospace; text-align: center; padding-top: 20vh; }}
            h1 {{ font-size: 4em; color: #0f3460; }}
            h2 {{ font-size: 2em; color: #ffeb3b; }}
            .disclaimer {{ color: #ffffff; margin-top: 50px; border: 2px solid #e94560; padding: 20px; display: inline-block; max-width: 80%; }}
        </style>
    </head>
    <body>
        <h1>Hackeado por Os Debuggers</h1>
        <h2>Membro: {nome_membro}</h2>
        <div class="disclaimer">
            <p><strong>ATENÇÃO:</strong> Isso é apenas um teste de exposição web (Defacement Simulation), dentro dos nossos protocolos éticos.</p>
            <p><strong>Para PARAR:</strong> Simplesmente desconecte o cabo da internet ou feche esta ferramenta (Ctrl+C) no computador do membro.</p>
        </div>
    </body>
    </html>
    """
    return html_content.encode('utf-8')

def iniciar_servidor_seguro():
    """Lógica principal: Autenticação, configuração e início do servidor."""
    
    # --- Passo 1: Autenticação de Segurança ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Defacement Test)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO!")
    
    # --- Passo 2: Configuração e HTML ---
    nome_membro = input("Digite o NOME que deseja que apareça como Membro: ")
    
    html_data = criar_pagina_html(nome_membro)
    local_ip = get_local_ip()

    # Cria a classe de Handler personalizada para servir o HTML
    class RequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html_data)))
            self.end_headers()
            self.wfile.write(html_data)

    # --- Passo 3: Início do Servidor ---
    try:
        with socketserver.TCPServer(("", PORTA_SERVIDOR), RequestHandler) as httpd:
            print("-----------------------------------------------------------------")
            print(f"🌐 SERVIDOR WEB ATIVO em http://{local_ip}:{PORTA_SERVIDOR}")
            print("-----------------------------------------------------------------")
            print("Instruções de Teste:")
            print("1. Na 'outra tela', abra o navegador.")
            print(f"2. Digite o endereço acima: **http://{local_ip}:{PORTA_SERVIDOR}**")
            print("3. A mensagem de Defacement aparecerá.")
            print("\nAVISO ÉTICO: Pressione **Ctrl+C** a qualquer momento ou desconecte o cabo da internet para PARAR.")
            
            httpd.serve_forever()
            
    except PermissionError:
        print(f"\n❌ ERRO: Permissão negada. Verifique se a porta {PORTA_SERVIDOR} está livre ou se precisa de privilégios de administrador.")
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor encerrado pelo Debugger (Ctrl+C). Fim do Teste.")
    except Exception as e:
        print(f"\nErro fatal ao iniciar o servidor: {e}")

if __name__ == "__main__":
    iniciar_servidor_seguro()
