import configparser
import logging
import os
import sys


class App:
    INI_FILE = "app.ini"
    WORDS_FILE = "words.txt"

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
            logging.error(f"Couldn't load file in {path_config_file}")
            return False

    def __load_words_file(self, filename):
        try:
            full_path = os.path.abspath(os.path.join("./src/utils/", filename))
            path_words_file = full_path if os.path.isfile(full_path) else \
                os.path.abspath(os.path.join(
                    os.path.dirname(sys.executable), filename))
            self.words = open(path_words_file, 'r', encoding='utf-8')
            return True
        except Exception as e:
            logging.error(f"Failed to open words file: {e}", exc_info=True)
            return False

    def __init__(self):
        if self.__load_ini_file(self.INI_FILE):
            if self.__load_words_file(self.WORDS_FILE):
                self.__run()

    def __run(self):
        try:
            print(
                f'{self.config["app"]["app_name"]} - {self.config["app"]["app_version"]}\nDeveloped by: {self.config["app"]["app_authors"]}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            self.words.close()
