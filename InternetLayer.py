class InternetLayer:
    def encapsulate(self, data):
        packet = f"IP:{data}"
        return packet

    def decapsulate(self, packet):
        if packet.startswith("IP:"):
            return packet[3:]
        else:
            raise ValueError("Invalid IP packet")
