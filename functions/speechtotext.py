import os
import json
import urllib.request
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

# yandex config
FOLDER_ID = "b1gnono54f2f4177ahp9" # Идентификатор каталога
IAM_TOKEN = "CggVAgAAABoBMxKABLOkXgUHld843J9zb_AV6YXtKkQPMSnLcL5cP8Dtr47yJA8T6rAXGVBZmxy1Nudmg8eOTfsmBYuHBbJZ14zy514ACpCSvRwtseRYqmbh2MTzafdTQeAKwuSiWX5QGnIWOxwNh9nzn3N6a_lfo9GqhuPQten6Xgu2wbgk6UNmmAXWBVs7nFIU-HsLbM_g_BgrZ6zrNMJBWFIeOMSXXS512tO78DZe1RY_GD0xXB0eEunEzyqeP2iBrzVFHx_bnohvf-QdSgzY53-5X8JADFMXJIktf3ymIZ_UunLeczhXXoQ2XJYjtPCFHWZSKoF2uAQQRnLjzoMhFaPQbgSYRAJacrtoBlJb8JGkcGPeZk-7m5wjwpTvU7NZkaZpmAvxO6q_MbQbO4uBI7K3HSUlYG8ShRmBdD5jON28lFG0VJAZSEkMlbHt3-XFaDcFq2SiLuO1aBeF1-hMprmz0_LpSC3Nqmy48N1XCJVwtJg6Lkiw21dofnDItKaW61s_-t9ekPOf6DNSI7p4aCZO72wqMbCaqoTiDz4fGQ8CwCEq9LZRJ-l5SXDN4AzimZzo3UT7L9eKHpvXMACPzqYSslMis9mOlQ-rlHcWkt74A5LJIAXQYWDGOXiUfnLyeolN1NWXMd5xrnrZUoxLl6kZIdRAkK7cPrINoYMQSOnKfAHrCLmwPUXVGiQQwoe17wUYgtm37wUiFgoUYWplMW9zdDdldWtmdmxqN29xNm8=" # IAM-токен


def yandex():
    # get speech.ogg
    with open("speech.ogg", "rb") as f:
        data = f.read()

    # url conf
    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)
    return decodedData.get("result").lower()

def sphinx():
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
        lm=False,
        jsgf=os.path.join(model_path, 'grammar.jsgf'),
        dic=os.path.join(model_path, 'russian.dict')
    )
    def speech():
        for phrase in speech:
            return phrase
