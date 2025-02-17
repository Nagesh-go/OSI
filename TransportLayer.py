class TransportLayer:
    def __init__(self):
        self.seq_num = 0

    def create_segment(self, data):
        segment = f"TCP:{self.seq_num}:{data}"
        self.seq_num += 1
        return segment

    def extract_data(self, segment):
        if segment.startswith("TCP:"):
            _, seq_num, data = segment.split(":", 2)
            return int(seq_num), data
        else:
            raise ValueError("Invalid TCP segment")
