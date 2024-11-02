import os
import srt
import wave
import json
import datetime
from vosk import Model, KaldiRecognizer

model_name = "vosk-model-ru-0.42"
audio_name = "molniya_0_aud_1"
words_per_line = 7


# Укажите путь к модели Vosk
model_path = "../models/" + model_name
audio_path = "../source/" + audio_name + ".wav"
result_path = "../result/captions_" + audio_name + ".srt"

# Загрузка модели
if not os.path.exists(model_path):
    print("Пожалуйста, скачайте, распакуйте модель Vosk и добавьте в папку 'models' проекта.")
    exit(1)

wf = wave.open(audio_path, "rb")

if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("Аудиофайл должен быть в формате WAV, моно.")
    exit(1)


model = Model(model_path)
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)


results = []
while True:
    data = wf.readframes(4000)
    
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        results.append(rec.Result())
        print("r: " + rec.Result())
    else:
        results.append(rec.PartialResult())
        print("pr: " + rec.PartialResult())

results.append(rec.FinalResult())
print("fr: " + rec.FinalResult())

subs = []
for res in results:
    j_res = json.loads(res)

    if not "result" in j_res:
        continue

    words = j_res["result"]

    for j in range(0, len(words), words_per_line):
        line = words[j: j + words_per_line]
        s = srt.Subtitle(index=len(subs),
                         content=" ".join([l["word"] for l in line]),
                         start=datetime.timedelta(seconds=line[0]["start"]),
                         end=datetime.timedelta(seconds=line[-1]["end"]))
        subs.append(s)

# Запись субтитров в файл
with open(result_path, "w") as f:
    f.write(srt.compose(subs))
