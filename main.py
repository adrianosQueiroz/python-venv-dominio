import sys
import os

def check_venv():
    # Verifica se o Python está rodando de dentro de uma pasta de venv
    is_venv = sys.prefix != sys.base_prefix
    
    print("-" * 30)
    print("🔍 VALIDADOR DE AMBIENTE VIRTUAL")
    print("-" * 30)
    
    if is_venv:
        print("✅ Status: Você ESTÁ em um ambiente virtual!")
        print(f"📍 Caminho do Venv: {sys.prefix}")
    else:
        print("❌ Status: Você NÃO está em um ambiente virtual.")
        print("⚠️ Cuidado: Instalando pacotes aqui, você sujará seu Python global.")

    print("-" * 30)
    print(f"🐍 Versão do Python: {sys.version.split()[0]}")

if __name__ == "__main__":
    check_venv()