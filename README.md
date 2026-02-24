# 🐉 Taverna do Dragão Banguelo - Access Validator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

Este é um script temático desenvolvido em **Python** para validar a entrada de clientes em um estabelecimento medieval (Taverna), utilizando critérios de idade e regras de acompanhamento.

## 📝 Funcionalidades

O sistema solicita informações básicas para determinar a permissão de entrada:
1. **Nome do cliente**: Para personalização das mensagens.
2. **Idade**: Verificação obrigatória de faixa etária.
3. **Acompanhamento**: Condicional para menores de idade (16+).

### Regras de Negócio:
* **Entrada Permitida:** Clientes com 18 anos ou mais, OU clientes entre 16-17 anos que estejam acompanhados.
* **Entrada Negada:** Qualquer pessoa abaixo de 16 anos ou menores de 18 desacompanhados.

## 🧠 Conceitos Aplicados

Neste projeto, foram colocados em prática conceitos fundamentais de programação:

* **Manipulação de Input/Output:** Captura de dados do usuário e exibição de mensagens dinâmicas com `f-strings`.
* **Tratamento de Strings:** Uso de métodos como `.strip()` (remover espaços extras) e `.lower()` (padronização de caixa) para tornar o código mais resiliente a erros de digitação.
* **Conversão de Tipos (Type Casting):** Transformação de strings de entrada em inteiros (`int()`) para operações matemáticas.
* **Lógica Booleana e Operadores Lógicos:** Construção de expressões complexas utilizando `and`, `or` e parênteses para garantir a precedência correta das regras de negócio.
* **Estruturas Condicionais:** Implementação de controle de fluxo com `if` e `else`.

## 🚀 Como executar o projeto

Certifique-se de ter o [Python](https://www.python.org/) instalado.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/xtheredviper/tavern-access-validator.git](https://github.com/xtheredviper/tavern-access-validator.git)
