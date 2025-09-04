
import pyvisa

class DMM6500:
	"""
	DMM6500儀器設定
	__init() : pyvisa -> rm.open_resource
	as_dcv() : 量測電壓設定
	meas_voltage() : 量測電壓命令及讀值
	close() : close儀器
	"""
	
    def __init__(self, resource):
        self.rm = pyvisa.ResourceManager()
        self.dev = self.rm.open_resource(resource, timeout=8000)
	
    def as_dcv(self):
        d = self.dev
        d.write("*RST"); 
        d.write("STAT:CLE"); 
        return self
    def meas_voltage(self): return float(self.dev.query(":MEAS:VOLT:DC?"))
    def close(self): self.dev.close()
