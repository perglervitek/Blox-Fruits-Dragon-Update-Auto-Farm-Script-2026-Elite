import pymem
import pymem.process
import time

class GameMemory:
    def __init__(self):
        self.pm = None
        self.process_name = "RobloxPlayerBeta.exe"
        self.base_address = None

    def attach(self):
        try:
            self.pm = pymem.Pymem(self.process_name)
            module = pymem.process.module_from_name(self.pm.process_handle, "RobloxPlayerBeta.exe")
            self.base_address = module.lpBaseOfDll
            return True
        except Exception as e:
            print(f"[-] Failed to attach: {e}")
            return False

    def is_attached(self):
        return self.pm is not None and self.base_address is not None

    def read_integer(self, address):
        if not self.is_attached():
            return 0
        return self.pm.read_int(self.base_address + address)

    def write_integer(self, address, value):
        if not self.is_attached():
            return
        self.pm.write_int(self.base_address + address, value)

    def read_float(self, address):
        if not self.is_attached():
            return 0.0
        return self.pm.read_float(self.base_address + address)

    def write_float(self, address, value):
        if not self.is_attached():
            return
        self.pm.write_float(self.base_address + address, value)

    def read_boolean(self, address):
        if not self.is_attached():
            return False
        return self.pm.read_bool(self.base_address + address)

    def write_boolean(self, address, value):
        if not self.is_attached():
            return
        self.pm.write_bool(self.base_address + address, value)

    def close(self):
        if self.pm:
            self.pm.close_process()
            self.pm = None
            self.base_address = None
