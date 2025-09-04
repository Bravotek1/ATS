
import pyvisa

class Keithley2450:
	"""
	Keithley2450儀器設定
	__init() : pyvisa -> rm.open_resource
	as_voltage_source() : 當電壓源設定
	as_current_sink() : 當電流sink設定
	set_voltage() : 設定電壓
	set_sink_current() : 設定sink電流
	meas_current() : 量測電流命令及讀值
	meas_voltage() : 量測電壓命令及讀值
	close() : close儀器
	"""
	
    def __init__(self, resource):
        self.rm = pyvisa.ResourceManager()
        self.dev = self.rm.open_resource(resource, timeout=8000)

    def as_voltage_source(self, curr_limit=0.3):
        d=self.dev; d.write("*RST"); d.write("STAT:CLE");d.write(":SOUR:FUNC VOLT"); d.write(":SENS:FUNC 'CURR'")
        d.write(f":SOUR:VOLT:ILIM {curr_limit:.6f}"); d.write(":OUTP ON"); return self
    def as_current_sink(self, volt_limit=5.0):
        d=self.dev; d.write("*RST"); d.write("STAT:CLE");d.write(":SOUR:FUNC CURR"); d.write(":SENS:FUNC 'VOLT'")
        d.write(f":SOUR:CURR:VLIM {volt_limit:.6f}");d.write(":OUTP ON"); return self
    def set_voltage(self, v): self.dev.write(f":SOUR:VOLT {v}")
    def set_sink_current(self, i): self.dev.write(f":SOUR:CURR {i}")
    def meas_current(self): return float(self.dev.query(":MEAS:CURR?"))
    def meas_voltage(self): return float(self.dev.query(":MEAS:VOLT?"))
    def off(self):
        try: self.dev.write(":OUTP OFF")
        finally: self.dev.close()
