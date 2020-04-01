#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Jarvis
import os
import sys
import json
import datetime
import re
from fuzzywuzzy import fuzz
import time

# my module
import functions.openapp
from functions.speech import tts


# настройки
opts = {
    "alias": ('кеша','кеш','инокентий','иннокентий','кишун','киш',
              'кишаня', 'кяш', 'кяша','кэш','кэша', 'леша', 'лёша'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        'open_app': ('открой', 'открыть'),
        'hello': ('привет', 'приветствую', 'здравствуй', 'здарова', 'здорово', 'здрасте', 'здравствуйте'),
    }
}

class Jarvis:

    def callback(self, recognize):

        voice = recognize.lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()


            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            print('Речь после оброботки: ', end='')
            print(cmd)

            res_recognize = self.recognize_cmd(cmd)

            print(res_recognize)

            self.execute_cmd(res_recognize)

    def recognize_cmd(self, cmd):
        RC = {'cmd': '', 'percent': 70, 'app_name': ''}
        pattern = re.compile(r'\w+')
        for c,v in opts['cmds'].items():
            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if c == 'open_app' and str(pattern.findall(cmd)[0]) == str(x):
                    cmd = cmd.replace(x, "").strip()
                    RC['cmd'] = c
                    RC['app_name'] = cmd
                    RC['percent'] = 100
                elif vrt > RC['percent']:
                    RC['cmd'] = c
                    RC['percent'] = vrt

        return RC;

    def execute_cmd(self, res_recognize):
        if res_recognize['cmd'] == 'ctime':
            # сказать текущее время
            now = datetime.datetime.now()
            tts.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        elif res_recognize['cmd'] == 'radio':
            # воспроизвести радио
            os.system("D:\\Jarvis\\res\\radio_record.m3u")
        elif res_recognize['cmd'] == 'stupid1':
            # рассказать анекдот
            tts.speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
        elif res_recognize['cmd'] == 'open_app':
            print(res_recognize['app_name'])
            open_apps = functions.openapp.OpenApps(res_recognize['app_name'])
            open_apps.start()
        elif res_recognize['cmd'] == 'hello':
            tts.speak('Здравствуйте')
        else:
            tts.speak('Команда не распознана, повторите!')

