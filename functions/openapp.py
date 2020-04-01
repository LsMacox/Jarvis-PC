import os
import subprocess
import platform

alias = {
    'google chrome': ['гугл', 'google', 'хром', 'хроме', 'google chrome', 'гугл хром', 'гугл хроме'],
    'wps pdf': [''],
    'skype preview': ['skype'],
    'avocode': [''],
    'atom': [''],
    'crossover': [''],
    'mysql workbench': [''],
    'terminal': [''],
    'electerm': [''],
    'музыка': [''],
    'компьютер': [''],
    'transmission': [''],
    'team': [''],
    'phpstorm': [''],
    'корзина': [''],
    'календарь': [''],
    'калькулятор': [''],
    'восстановление': [''],
    'remmina': [''],
    'oracle vm virtualbox': [''],
    'discord': [''],
    'app store': [''],
    'снимок': [''],
    'редактор': [''],
    'диктофон': [''],
    'pycharm professional': [''],
    'менеджр пакетов synaptic': [''],
    'файловый менеджр': [''],
    'центр управления': [''],
    'запись с экрана': [''],
    'idle 3': [''],
    'arduino ide': [''],
    'filezilla': [''],
    'менеджер пакетов': [''],
    'медиаплеер vlc': [''],
    'adobe photoshop cs6': [''],
    'visual studio code': [''],
}


class OpenApps:
    def __init__(self, name):
        self.name = name
        self.app_name = self.get_app_name();
        self.path = ''

    def os_check(self, name):
        if platform.system().lower() == name:
            return True
        else:
            return False

    def get_app_name(self):
        app_name = ''
        for alia in alias:
            for synonym in alias[alia]:
                if synonym == self.name:
                    app_name = alia.lower()
                    break
        return app_name

    def get_linux_path(self, static_path):
        files = os.listdir(static_path)
        for file in files:
            if file.find('.desktop') != -1:
                with open(os.path.join(static_path, file), 'r', encoding='utf-8', errors='ignore') as f:
                    for num, line in enumerate(f):
                        line = line.lower()
                        if line.find('name=' + self.app_name) != -1:
                            self.path = static_path + file
                            for path in f:
                                if path.lower().find('exec=') != -1:
                                    path = path.replace('Exec=', '')
                                    path = path.replace('exec=', '')
                                    self.path = path
                                    break
                                else:
                                    self.path = False

    def get_linux_app_path(self):
        static_path_1 = "/usr/share/applications/"

        if os.path.exists(static_path_1):
            self.get_linux_path(static_path_1)

    def start(self):
        if self.os_check('linux'):
            self.get_linux_app_path()

        try:
            if self.path:
                cmd = 'nohup ' + self.path
                subprocess.Popen(cmd, shell=True)
        except UnboundLocalError:
            print('App not found')

