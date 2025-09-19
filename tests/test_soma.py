import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'examples')))
from soma import soma
import pytest

import pytest

def test_soma_sucesso():
    assert soma(2, 3) == 5

def test_soma_sucesso_negativo():
    assert soma(-1, -1) == -2

def test_soma_sucesso_zero():
    assert soma(0, 0) == 0

def test_soma_falha_diferente():
    assert soma(1, 2) != 3

def test_soma_falha_excecao():
    with pytest.raises(TypeError):
        soma("a", "b")