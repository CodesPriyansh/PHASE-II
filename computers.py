#create the base class - Computer
class Computer:
    def __init__(self, brand, model, memory, processor, operating_system, connectivity):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.processor = processor
        self.operating_system = operating_system
        self.connectivity = connectivity
        
    #methods
    def get_brand_model(self):
        return f"Brand is {self.brand} and Model is {self.model}."
    
    def start(self):
        return "Computer started."
    
    def stop(self):
        return "Computer shutdown."
    
    def connect_peripheral(self):
        return f"Peripheral '{self.connectivity}' connected successfully."
    
#create derived class - DesktopComputer
class DesktopComputer(Computer):
    def __init__(self, brand, model, memory, processor, operating_system, connectivity, form_factor, graphics_card):
        Computer.__init__(self, brand, model, memory, processor, operating_system, connectivity)
        self.form_factor = form_factor
        self.graphics_card = graphics_card
        
    #methods
    
    def upgrade_graphics(self, new_graphics_card):
        old_graphics_card = self.graphics_card
        old_graphics_card = new_graphics_card
        return f"Graphics card upgraded from '{old_graphics_card}' to '{new_graphics_card}'."
    
    def add_storage(self, additional_storage):
        self.memory += additional_storage
        
#create derived class - LaptopComputer
class LaptopComputer(Computer):
    def __init__(self, brand, model, memory, processor, operating_system, connectivity, screen_size, battery_life):
        Computer.__init__(self, brand, model, memory, processor, operating_system, connectivity)
        self.screen_size = screen_size
        self.battery_life = battery_life
        
    #methods
    def adjust_brightness(self, brightness):
        return f"brightness: {brightness} has been adjusted."
    
    def extend_battery_life(self, add_battery_life):
        self.battery_life += add_battery_life 
        
#create derived class - TabletComputer
class TabletComputer(Computer):
    def __init__(self, brand, model, memory, processor, operating_system, connectivity, touchscreen_type, weight):
        Computer.__init__(self, brand, model, memory, processor, operating_system, connectivity)
        self.touchscreen_type = touchscreen_type
        self.weight = weight
        
    #methods
    def rotate_screen(self, orientation):
        return f"Screen orientation rotated to {orientation}."
    
    def install_apps(self, app_name):
        return f"{app_name} is being installed..."
    
#create derived class - ServerComputer
class ServerComputer(Computer):
    def __init__(self, brand, model, memory, processor, operating_system, connectivity, rack_mountable, maximum_users):
        Computer.__init__(self, brand, model, memory, processor, operating_system, connectivity)
        self.rack_mountable = rack_mountable
        self.maximum_users = maximum_users
        
    #methods
    def configure_networking(self, network_settings):
        return f"Networking configured with settings: {network_settings}."
    
    def manage_services(self, services):
        return f"Services {', '.join(services)} managed successfully."
    
#create derived class - EmbeddedComputer
class EmbeddedComputer(Computer):
    def __init__(self, brand, model, memory, processor, operating_system, connectivity, embedded_system_type, integration_method):
        Computer.__init__(self, brand, model, memory, processor, operating_system, connectivity)
        self.embedded_system_type = embedded_system_type
        self.integration_method = integration_method
        
    #methods
    def control_devices(self, devices):
        return f"Devices {', '.join(devices)} controlled successfully."
    
    def monitor_sensors(self, sensors):
        return f"Sensors {', '.join(sensors)} monitored."


# Create an instance of DesktopComputer
my_desktop = DesktopComputer(brand="ExampleBrand", model="DesktopModel", memory= 64,processor="Intel Core i7",
                              operating_system="Windows 10", connectivity="Wi-Fi", form_factor="Tower",
                              graphics_card="NVIDIA GeForce RTX 3080")

# Start the desktop computer
print(my_desktop.start())

# Upgrade graphics card
print(my_desktop.upgrade_graphics("NVIDIA GeForce RTX 3090"))

# Add storage
my_desktop.add_storage(additional_storage=512)  # Add 512GB storage

# Create an instance of LaptopComputer
my_laptop = LaptopComputer(brand="ExampleBrand", model="LaptopModel", memory="16GB", processor="Intel Core i5",
                            operating_system="Windows 10", connectivity="Wi-Fi", screen_size="15.6 inches",
                            battery_life=8)  # Assuming 8 hours battery life

# Adjust brightness
print(my_laptop.adjust_brightness(brightness=80))

# Extend battery life
my_laptop.extend_battery_life(add_battery_life=120)  # Extend by 2 hours

# Create an instance of TabletComputer
my_tablet = TabletComputer(brand="ExampleBrand", model="TabletModel", memory="4GB", processor="ARM Cortex-A53",
                            operating_system="Android", connectivity="Wi-Fi", touchscreen_type="Capacitive",
                            weight="500g")

# Rotate screen orientation
print(my_tablet.rotate_screen(orientation="landscape"))

# Install apps
print(my_tablet.install_apps("Web Browser"))

# Create an instance of ServerComputer
my_server = ServerComputer(brand="ExampleBrand", model="ServerModel", memory="64GB", processor="Intel Xeon",
                            operating_system="Linux", connectivity="Ethernet", rack_mountable=True,
                            maximum_users=100)

# Configure networking
print(my_server.configure_networking(network_settings={"IP Address": "192.168.1.10", "Subnet Mask": "255.255.255.0"}))

# Manage services
print(my_server.manage_services(services=["Web Server", "Database Server"]))

# Create an instance of EmbeddedComputer
my_embedded = EmbeddedComputer(brand="ExampleBrand", model="EmbeddedModel", memory="1GB", processor="ARM Cortex-A7",
                                operating_system="Linux", connectivity="UART", embedded_system_type="Industrial Control",
                                integration_method="Embedded into Machinery")

# Control devices
print(my_embedded.control_devices(devices=["Motor", "Sensor"]))

# Monitor sensors
print(my_embedded.monitor_sensors(sensors=["Temperature Sensor", "Pressure Sensor"]))


        
    
    
        
        
    
        
        