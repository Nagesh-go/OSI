from InternetLayer import InternetLayer
class ApplicationLayer:
    def __init__(self, transport):
        self.transport = transport
        self.internet_layer = InternetLayer()  # Create an instance of InternetLayer

    def send_message(self, message, network, connection):
        segment = self.transport.create_segment(message)
        packet = self.internet_layer.encapsulate(segment)  # Use the instance of InternetLayer
        network.send(connection, packet)

    def receive_message(self, network, connection):
        packet = network.receive(connection)
        segment = self.internet_layer.decapsulate(packet)  # Use the instance of InternetLayer
        _, data = self.transport.extract_data(segment)
        return data
