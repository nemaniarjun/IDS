import random
from .BaseDevice import BaseDevice

class TrafficDevice(BaseDevice):
    def __init__(self, uuid, broker):
        self.tick_time = 90
        self.is_active = False
        BaseDevice.__init__(self, uuid, broker, 'Traffic')

    def process_command(self, data):
        print(data)

    def send_message(self):
        traffic_simulation = random.choices([(0, 50), (51, 125), (126, 175), (176, 200)], [25, 50, 15, 10])
        traffic_simulation_inflow = random.randrange(traffic_simulation[0][0], traffic_simulation[0][1])
        traffic_simulation_outflow = random.randrange(0, traffic_simulation_inflow)
        message = self.create_message({'type': 'Tick', 'value': (traffic_simulation_inflow - traffic_simulation_outflow)})
        
        # Publish to Self Topic
        self.client.publish(self.topic, message)

        # Also Publish to all Devices Topic
        self.client.publish("Devices", message)