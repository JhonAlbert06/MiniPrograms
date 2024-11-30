from pyrgb import RGBColor, DeviceManager

manager = DeviceManager()
keyboard = manager.get_device('keyboard')  # Ajusta según tu dispositivo

color = RGBColor(255, 182, 193)  # Rosado claro
keyboard.set_static(color)
