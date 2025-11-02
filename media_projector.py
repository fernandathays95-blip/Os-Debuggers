import sys
import cv2
import os

# --- CONFIGURAÇÃO DE SEGURANÇA E ÉTICA ---
SENHA_DE_REDE_MESTRE = "SUA_SENHA_SECRETA_DO_MESTRE" # MUDAR ISSO!
# ----------------------------------------

def projetar_video_seguro():
    """Lógica principal: Autenticação, dupla confirmação e projeção de vídeo."""
    
    # --- Passo 1: Autenticação de Segurança (Senha da Rede) ---
    print("---------------------------------------")
    print("🔒 INÍCIO DO PROTOCOLO DE AUTORIZAÇÃO 🔒")
    print("Ferramenta dos Debuggers (Projeção de Mídia)")
    print("---------------------------------------")
    
    senha_digitada = input("Digite a SENHA DA REDE MESTRE para autorizar a projeção: ")
    
    if senha_digitada != SENHA_DE_REDE_MESTRE:
        print("\n❌ ACESSO NEGADO! Chave de segurança incorreta. Encerrando por ética.")
        sys.exit(0)
    
    print("\n✅ ACESSO AUTORIZADO! Início da configuração de projeção.")

    # --- Passo 2: Seleção e Verificação do Arquivo ---
    caminho_video = input("Digite o caminho COMPLETO do arquivo de vídeo (.mp4, .avi, etc.) para projetar: ")
    
    if not os.path.exists(caminho_video):
        print(f"\n❌ ERRO: Arquivo não encontrado no caminho: {caminho_video}")
        sys.exit(0)
        
    print(f"\nArquivo selecionado: {os.path.basename(caminho_video)}")
    print("Preparando para enviar para a tela conectada via adaptador HDMI simulado...")
    
    # --- Passo 3: Dupla Confirmação de Segurança ("Dois Cliques") ---
    print("\n⚠️ DUPLA CONFIRMAÇÃO DE SEGURANÇA ⚠️")
    
    # Confirmação 1
    confirmacao1 = input("PRIMEIRO CLIQUE: Confirme que o cabo está conectado e que deseja iniciar (S/N): ").upper()
    if confirmacao1 != 'S':
        print("Cancelado na primeira confirmação. Encerrando.")
        sys.exit(0)

    # Confirmação 2
    confirmacao2 = input("SEGUNDO CLIQUE: Confirmação FINAL para iniciar a projeção AGORA (S/N): ").upper()
    if confirmacao2 != 'S':
        print("Cancelado na confirmação final. Encerrando.")
        sys.exit(0)
        
    print("\n⏯️ INICIANDO PROJEÇÃO... (O vídeo abrirá em uma nova janela)")
    
    # --- Passo 4: Execução (Projeção) ---
    cap = cv2.VideoCapture(caminho_video)
    
    if not cap.isOpened():
        print("❌ ERRO: Não foi possível abrir o arquivo de vídeo. Verifique o formato.")
        sys.exit(0)

    # Loop de reprodução
    while True:
        ret, frame = cap.read()
        
        if not ret:
            # Fim do vídeo
            break
            
        # Exibe o frame na janela
        cv2.imshow('Projetor dos Debuggers', frame)
        
        # Espera por 25ms ou se a tecla 'q' for pressionada (para sair)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()
    
    print("\nProjeção de vídeo finalizada.")


# Inicia o script
if __name__ == "__main__":
    projetar_video_seguro()
