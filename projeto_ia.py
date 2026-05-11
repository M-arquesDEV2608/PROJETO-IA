import time
from colorama import Fore, Style, init

# Inicializa as cores no terminal
init(autoreset=True)

# 1. BANCO DE DADOS CULTURAL LOCAL (Corrigido para ter chaves iguais)
DATABASE_CULTURAL = {
    "ritmos": [
        {
            "nome": "Maracatu", 
            "origem": "Raízes Afro-brasileiras", 
            "dica": "Tente usar uma batida 4/4 com ênfase no bumbo."
        }
    ],
    "estetica": [
        {
            "nome": "Folia de Reis", 
            "origem": "Cultura Popular Brasileira", 
            "dica": "Use filtros de alta saturação e máscaras espelhadas."
        }
    ]
}

def middleware_cultural(input_usuario):
    sugestao_encontrada = None
    
    # Lógica de detecção
    if "musica" in input_usuario.lower() or "ritmo" in input_usuario.lower():
        sugestao_encontrada = DATABASE_CULTURAL["ritmos"][0]
    elif "video" in input_usuario.lower() or "cor" in input_usuario.lower():
        sugestao_encontrada = DATABASE_CULTURAL["estetica"][0]

    return sugestao_encontrada

# --- SIMULAÇÃO DA INTERFACE ---
print(f"{Fore.CYAN}=== SISTEMA DE IDENTIDADE PERSISTENTE v1.0 ===\n")
print("Status: IA Onipresente Ativa")
print("-" * 45)

pergunta = "Estou criando um vídeo sobre a cultura brasileira e quero cores vibrantes."
print(f"{Fore.WHITE}Usuário está digitando: {Style.BRIGHT}'{pergunta}'")

print(f"\n{Fore.YELLOW}Analisando contexto...")
time.sleep(1.5)

sugestao = middleware_cultural(pergunta)

if sugestao:
    print(f"\n{Fore.MAGENTA}[ASSISTENTE DE IDENTIDADE LOCAL]")
    # Agora todas as sugestões usam 'nome', 'dica' e 'origem'
    print(f"{Fore.GREEN}Sugestão Detectada: {sugestao['nome']}")
    print(f"{Fore.WHITE}Por que usar: {sugestao['dica']}")
    print(f"{Fore.CYAN}Link de Referência: {sugestao['origem']}")
else:
    print("\n[IA] Continue seu trabalho. Nenhuma sobreposição cultural detectada.")

print("\n" + "-" * 45)