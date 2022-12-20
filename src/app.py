import configparser
import logging
import os
import sys


class App:
    INI_FILE = "app.ini"

    def __load_ini_file(self, filename):
        full_path = os.path.abspath(os.path.join("./src", filename))
        path_config_file = full_path if os.path.isfile(full_path) else \
            os.path.abspath(os.path.join(
                os.path.dirname(sys.executable), filename))
        self.config = configparser.ConfigParser()
        if self.config.read(path_config_file):
            return True
        else:
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                filename='logs/app.log', filemode='w',)
            logging.error("Não foi possível carregar o arquivo de configuração em {}".format(
                path_config_file))
            return False

    def __init__(self):
        if self.__load_ini_file(self.INI_FILE):
            self.__run()

    def __run(self):
        print(self.config["app"]["app_version"])
