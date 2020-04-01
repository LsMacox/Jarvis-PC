var recognizer = new window.webkitSpeechRecognition();

recognizer.start();

recognizer.onresult = function(event) {
    let result = event.results[event.resultIndex];
    if (result.isFinal) {
        console.log('Вы сказали: ' + result[0].transcript);
        send_recognition_fetch_data(result[0].transcript);
    } else {
        console.log('Промежуточный результат: ', result[0].transcript);
    }
};

recognizer.onend = function(event) {
    recognizer.start();
}
