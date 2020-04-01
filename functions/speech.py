import speechd

# tts conf
tts = speechd.SSIPClient('test')
tts.set_output_module('rhvoice')
tts.set_language('ru')
tts.set_rate(30)
tts.set_punctuation(speechd.PunctuationMode.SOME)

