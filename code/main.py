import os
import srt
import wave
import json
from vosk import Model, KaldiRecognizer

model_name = "vosk-model-ru-0.42"
audio_name = "molniya_0_aud_1"


# Укажите путь к модели Vosk
model_path = "../models/" + model_name
audio_path = "../source/" + audio_name + ".wav"
result_path = "../result/captions_" + audio_name + ".srt"

# Загрузка модели
if not os.path.exists(model_path):
    print("Пожалуйста, скачайте и распакуйте модель Vosk.")
    exit(1)

model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

# Открытие аудиофайла
# with wave.open(audio_path, "rb") as wf:
#     if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
#         print("Аудиофайл должен быть в формате WAV с 16 кГц, моно.")
#         exit(1)

    # Обработка аудио и распознавание
    # subs = []
    # start_time = 0


wf = wave.open(audio_path, "rb")

if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("Аудиофайл должен быть в формате WAV с 16 кГц, моно.")
    exit(1)

print(rec.SrtResult(wf))


    # while True:
    #     data = wf.readframes(4000)
    #     if len(data) == 0:
    #         break
    #     if rec.AcceptWaveform(data):
    #         print("sr: " + rec.SrtResult(wf))
    #     else:
    #         print("pr: " + rec.PartialResult())
    #
    # print("fr: " + rec.FinalResult())



    # while True:
    #     data = wf.readframes(4000)
    #     if len(data) == 0:
    #         break
    #     if rec.AcceptWaveform(data):
    #         result = json.loads(rec.Result())
            # if 'text' in result and result['text']:
            #     end_time = start_time + 4  # Предположим, что каждая фраза длится 4 секунды
            #     subs.append(srt.Subtitle(index=len(subs)+1, start=srt.timedelta(seconds=start_time),
            #                               end=srt.timedelta(seconds=end_time),
            #                               content=result['text']))
            #     start_time = end_time


    # Добавление последнего результата
#     final_result = json.loads(rec.FinalResult())
#     if 'text' in final_result and final_result['text']:
#         end_time = start_time + 4
#         subs.append(srt.Subtitle(index=len(subs)+1, start=srt.timedelta(seconds=start_time),
#                                   end=srt.timedelta(seconds=end_time),
#                                   content=final_result['text']))
#
# # Запись субтитров в файл
# with open(result_path, "w") as f:
#     f.write(srt.compose(subs))
