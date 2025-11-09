#Catarina Costa - Author 
#7/11/2025

import whisper
import os

path = r"caminho do ficheiro"
print("Ficheiro existe:", os.path.exists(path))

model = whisper.load_model("tiny")

# Testar se o ffmpeg lê o áudio
try:
    result = model.transcribe(path, language="pt")
    print("Transcrição:", result["text"][:200])
except Exception as e:
    print("Erro:", e)



# Transcricao

import whisper

model = whisper.load_model("tiny")
result = model.transcribe(
    r"caminho do ficheiro",
    language="pt"
)

with open(r"caminho", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcrição concluída e guardada em Desktop!")
