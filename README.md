# 🛠️ Sistema Inteligente de Recomendação de Manutenção Preventiva com Machine Learning

Este repositório apresenta um sistema inteligente para recomendação de manutenção preventiva em equipamentos industriais. Utiliza técnicas avançadas de Machine Learning e sensores IoT para prever quando equipamentos precisam de manutenção, evitando paradas inesperadas e otimizando a eficiência operacional.

---

## 📊 Visão Geral do Projeto

O projeto envolve as seguintes etapas principais:

1. **Análise exploratória e pré-processamento dos dados**
2. **Avaliação e comparação de cinco estratégias para balanceamento de classes**
3. **Treinamento e validação de modelos (Random Forest e LightGBM)**
4. **Deploy do melhor modelo em uma aplicação web com Streamlit**

---

## 📁 Estrutura do Projeto

```
.
├── web_ml_manutencao_industrial.ipynb  # Notebook com pré-processamento, treinamento e avaliação
├── web_ml_manutencao_industrial_app.py # Aplicação web para deploy com Streamlit
├── requirements.txt                    # Dependências do projeto
├── dataset-ml.csv                      # Dataset fictício com dados dos sensores
├── modelos/                            # Diretório para modelos treinados
├── padronizadores/                     # Diretório para padronizadores (scalers)
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- Python **3.11.5** (recomendado)
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Imbalanced-learn
- JupyterLab
- Joblib

Consulte o arquivo `requirements.txt` para versões específicas.

---

## 🚀 Como Executar o Projeto Localmente

### 1. 🔁 Clone o repositório

```bash
git clone https://github.com/ede1000son/sistema-recomendacao-manutencao-ml
cd sistema-recomendacao-manutencao-ml
```

### 2. 📦 Crie e ative o ambiente virtual

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. 📥 Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. ▶️ Execute o notebook (pipeline de ML)

```bash
jupyter lab web_ml_manutencao_industrial.ipynb
```

### 5. 🚀 Deploy da aplicação web com Streamlit

```bash
streamlit run web_ml_manutencao_industrial_app.py
```

Acesse a aplicação no endereço fornecido pelo Streamlit (geralmente `http://localhost:8501`).

---

## 🧪 Avaliação dos Modelos

O notebook inclui uma avaliação detalhada das estratégias de balanceamento testadas e métricas de desempenho dos modelos como acurácia, precisão, recall e F1-score. O melhor modelo selecionado é salvo e utilizado na aplicação web.

---

## 🌐 Funcionalidades da Aplicação Web

- **Entrada de dados**: Permite inserir valores dos sensores em tempo real.
- **Recomendação instantânea**: Exibe se a manutenção é necessária e a probabilidade associada à previsão.

---

## 📈 Possíveis Melhorias Futuras

- Integração com sistemas IoT para coleta automatizada de dados.
- Implementação de alerta automático para equipes de manutenção.
- Expansão do dataset com dados reais para aprimorar a precisão do modelo.
- Engenharia de parâmetros para otimizar entrada de dados.
- Otimização de hiperparâmetros dos modelos.
- Histórico de previsões com registro de resultados anteriores.
- Inclusão de gráficos com indicativo visual da probabilidade de manutenção.

---

## 👨‍💻 Autor

**Edemilson Fernandes Vieira**  
Especialista em Machine Learning e Análise de Dados.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

