import os

def ler_codigo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return f.read()

def extrair_nome_arquivo(caminho_arquivo):
    return os.path.splitext(os.path.basename(caminho_arquivo))[0]
