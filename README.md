# Implementation_Digital_Envelope
Um dos propósitos do trabalho é que a implementação funcione como um protocolo, de modo que seja possível criar chaves, assinar ou verificar assinaturas por outros programas. Além disso, é necessário permitir o uso de diferentes algoritmos, simulando a flexibilidade de alguns protocolos.

![image](https://github.com/claudiney63/Implementation_Digital_Envelope/assets/40923082/17bf6852-d6cd-4d56-9869-63e485e0a985)

# Implementação de um programa de assinatura digital

# Grupo:
Clauidney Ryan da Silva

Ellem Almeida Amorim

Vinícius Alves de Moura

# Execução
Preparação do ambiente

python -m venv .venv

# Ativação do ambinte virtual
# Windows >
```
python -m venv .venv
```
```
.venv\Scripts\activate
```
```
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```
# Linux >
source .venv/bin/activate
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Menu:
```console
Selecione uma opção:
[1] - Criar um par de chaves RSA;
[2] - Criar um envelope;
[3] - Abrir envelope;
[4] - Visualizar arquivos criptografados;
[5] - Sair.
~
```
Opção 1: Criar um par de chaves RSA

Inserir o prefixo dos arquivos da chaves, por padrão (quando nenhum prefixo é inserido) elas tem os nomes (*public_key.pem* e *private_key.pem*), caso, por exemplo, seja inserido o prefixo "*ellem*", os nomes serão salvos como (*ellem_public_key.pem* e *ellem_private_key.pem*)
```console
Prefixo do arquivo (opcional):
~
```
