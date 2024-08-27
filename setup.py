from setuptools import setup, find_packages

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="encryption",  # Substitua pelo nome do seu pacote
    version="0.1.0",
    author="Henrique Bucci",
    author_email="henriquebrn@al.insper.edu.br",
    description="Um pacote com funções de encriptação e decriptação de mensagens.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henriquebrnetto/encryption_alglin",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(),  # Encontra automaticamente todos os pacotes no diretório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # Versão mínima do Python suportada
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],
)