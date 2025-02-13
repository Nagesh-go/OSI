import time

class OSIModel:
    def __init__(self, data):
        self.data = data
        self.encoded_data = None
        self.encrypted_data = None
        self.packet = None
        self.frame = None
        self.bits = None

    # Layer 7: Application Layer
    def application_layer(self):
        print(f"Application Layer: Sending message -> '{self.data}'")
        self.encoded_data = self.data.encode("utf-8")  # Encoding text to bytes
        time.sleep(1)
        self.presentation_layer()

    # Layer 6: Presentation Layer
    def presentation_layer(self):
        print(f"Presentation Layer: Encoding data -> {self.encoded_data}")
        self.encrypted_data = self.encoded_data[::-1]  # Simple encryption (reverse string)
        time.sleep(1)
        self.session_layer()

    # Layer 5: Session Layer
    def session_layer(self):
        print(f"Session Layer: Establishing session...")
        time.sleep(1)
        self.transport_layer()

    # Layer 4: Transport Layer
    def transport_layer(self):
        print(f"Transport Layer: Segmenting data...")
        self.packet = f"Header|{self.encrypted_data}|Footer"
        time.sleep(1)
        self.network_layer()

    # Layer 3: Network Layer
    def network_layer(self):
        print(f"Network Layer: Adding IP addresses...")
        self.frame = f"Src: 192.168.1.1 | Dest: 192.168.1.2 | {self.packet}"
        time.sleep(1)
        self.data_link_layer()

    # Layer 2: Data Link Layer
    def data_link_layer(self):
        print(f"Data Link Layer: Adding MAC addresses...")
        self.bits = f"Src-MAC: AA:BB:CC:DD | Dest-MAC: 11:22:33:44 | {self.frame}"
        time.sleep(1)
        self.physical_layer()

    # Layer 1: Physical Layer
    def physical_layer(self):
        print(f"Physical Layer: Transmitting bits -> {self.bits}")
        time.sleep(1)
        print("\nData sent successfully!\n")
        print("Now reversing the process (Decapsulation)...\n")
        time.sleep(1)
        self.decapsulation()

    # Decapsulation (Reverse Process)
    def decapsulation(self):
        print("Physical Layer: Receiving bits...")
        time.sleep(1)
        print("Data Link Layer: Extracting MAC addresses...")
        time.sleep(1)
        print("Network Layer: Extracting IP addresses...")
        time.sleep(1)
        print("Transport Layer: Reassembling segments...")
        time.sleep(1)
        print(f"Presentation Layer: Decrypting data -> {self.encrypted_data[::-1].decode('utf-8')}")
        time.sleep(1)
        print(f"Application Layer: Message received -> '{self.data}'")


# Run the OSI Model Simulation
if __name__ == "__main__":
    message = input("Enter a message to send: ")
    osi = OSIModel(message)
    osi.application_layer()
