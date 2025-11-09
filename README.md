# 📘 README — Transcrição de Áudio com Whisper

## 🧠 Descrição

- Este script permite transcrever ficheiros de áudio em texto usando o modelo Whisper da OpenAI.
O Whisper é uma rede neural de reconhecimento automático de fala, capaz de converter fala em texto em vários idiomas, incluindo o português.

## ⚙️ Funcionalidades

- Verifica se o ficheiro de áudio existe.

- Usa o modelo tiny do Whisper (mais leve e rápido).

- Transcreve o áudio especificado.

- Guarda o texto transcrito num ficheiro .txt.

## 🧩 Requisitos

Antes de correr o script, certifica-te de que tens o Python 3.9+ e as seguintes bibliotecas instaladas:

```
pip install openai-whisper
pip install torch
pip install ffmpeg-python
```

Também é necessário ter o **FFmpeg** instalado no sistema (**Whisper** depende dele para ler ficheiros de áudio):

Windows:
Baixa e instala de[ https://ffmpeg.org/download.html]( https://ffmpeg.org/download.html) [ https://ffmpeg.org/download.html]( https://ffmpeg.org/download.html)https://ffmpeg.org/download.html

Depois adiciona a pasta bin ao PATH do sistema.

## 📝 Como usar

Abre o ficheiro **trasncricao.py.**

1. Substitui os caminhos:

```
path = r"caminho do ficheiro"        # Caminho do ficheiro de áudio
with open(r"caminho", "w", encoding="utf-8") as f:  # Caminho para guardar o texto

```

2. Executa:

```
python trasncricao.py
```

3. O texto transcrito será mostrado no terminal e guardado no ficheiro de saída.

## 🧑‍💻 Autor

*Catarina Costa — 7 de novembro de 2025*
