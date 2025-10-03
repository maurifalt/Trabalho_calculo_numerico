# Resolução de EDO por Diferenças Finitas

Este projeto resolve o seguinte problema de valor de contorno usando o **método das diferenças finitas**:

\[
y'' = 3xy' - y + x, \quad y(0) = 0, \; y(1) = 0, \; h = 0.25
\]

O código gera os valores aproximados de `y(x)` e plota o gráfico da solução numérica.

---

## 📦 Pré-requisitos

Antes de rodar o código, certifique-se de ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

Você pode instalar as dependências com:

```bash
pip install numpy matplotlib

referências:

BURDEN, R.; FAIRES, J. D. Análise numérica. ["s.l: s.n."].
