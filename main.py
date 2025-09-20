from agent.chains import criar_cadeia
from agent.utils import ler_codigo, extrair_nome_arquivo
import os
import re
import subprocess
from datetime import datetime

def gerar_testes(caminho_arquivo):
    cadeia = criar_cadeia()
    codigo = ler_codigo(caminho_arquivo)
    nome = extrair_nome_arquivo(caminho_arquivo)

    print("\n Enviando código para o modelo:")
    print(codigo)

    resposta = cadeia.invoke({"code": codigo})

    print("\n Resposta bruta do modelo:")
    print(repr(resposta))

    # Extrai o conteúdo da resposta
    if hasattr(resposta, "content"):
        bruto = resposta.content
    elif isinstance(resposta, dict) and "content" in resposta:
        bruto = resposta["content"]
    else:
        bruto = str(resposta)

    # Extrai apenas o código Python entre os blocos ```python ... ```
    padrao = r"```python\n(.*?)```"
    match = re.search(padrao, bruto, re.DOTALL)

    if match:
        conteudo = match.group(1)
    else:
        print("\n Nenhum bloco de código Python encontrado. Salvando conteúdo bruto.")
        conteudo = bruto

    # Adiciona import robusto para garantir que o teste funcione
    import_linha = (
        "import sys\n"
        "import os\n"
        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'examples')))\n"
        f"from {nome} import {nome}\n"
        "import pytest\n\n"
    )
    conteudo = import_linha + conteudo.strip()

    print(f"\n Conteúdo final para test_{nome}.py:\n")
    print(conteudo)

    if "def test_" in conteudo:
        os.makedirs("tests", exist_ok=True)
        caminho_saida = f"tests/test_{nome}.py"
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"\n Arquivo salvo em: {caminho_saida}")
    else:
        print("\n Nenhum teste foi detectado no conteúdo. Verifique o prompt ou a resposta.")

    return nome  # retorna o nome do arquivo para usar no relatório

if __name__ == "__main__":
    nome_modulo = gerar_testes("examples/soma.py")

    # Gera timestamp para o nome do arquivo
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"resultado_testes_{nome_modulo}_{timestamp}.txt"

    # Executa os testes e salva a saída
    print(f"\n Executando pytest e salvando em {nome_arquivo}...")
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        subprocess.run(["pytest", "tests/"], stdout=f, stderr=subprocess.STDOUT)

    print(f"\n Resultado salvo em: {nome_arquivo}")
