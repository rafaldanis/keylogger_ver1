import configparser

class GetConfiguration:

    def initFile(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def getItems(self, section):
        config = self.initFile()
        return config.items(section)

