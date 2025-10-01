#  Chatbot da Pizzaria

**Autor:** Leonardo Henrique Bernardes de Souza  
**Instituição:** Faculdade de Tecnologia (FATEC Franca)

##  Descrição do Projeto

Este projeto consiste em um chatbot de pizzaria desenvolvido em Python utilizando o framework Rasa. O objetivo é simular um atendimento automatizado capaz de:

-  Atender pedidos de pizza
-  Validar tamanhos e preços do cardápio
-  Simular entrega para um endereço informado pelo cliente

O chatbot pode ser treinado e executado localmente, permitindo interações realistas de um cliente com a pizzaria.

##  Tecnologias Utilizadas

- **Python 3.x**
- **Rasa Framework** (NLU + Core)
- **YAML** (configuração de intents, entidades e histórias)

##  Funcionalidades Implementadas

###  Consulta de Preços
- O cliente pode perguntar o preço de pizzas nos tamanhos **pequena**, **média** e **grande**
- O bot responde automaticamente com os valores definidos no cardápio

###  Simulação de Entrega
- O cliente informa um endereço
- O bot responde com o tempo estimado de entrega (aleatório entre 20 e 50 minutos)

###  Fluxo de Conversação
- Intents definidas em `nlu.yml`
- Ações personalizadas em `actions.py`
- Histórias em `stories.yml`
- Regras em `rules.yml`


##  Como Executar o Projeto

### 1. Clone o repositório ou extraia os arquivos:
```bash
git clone https://github.com/Leonardo-henriqu2/chatbot-pizzaria.git
cd chatbot-rasa-main
