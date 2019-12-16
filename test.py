#!python3
import irsdk
ir = irsdk.IRSDK()
ir.startup()
while 1:
    print(ir['Speed'])
