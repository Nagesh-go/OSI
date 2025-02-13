# OSI Model
This repository contains a Python-based simulation of the OSI (Open Systems Interconnection) Model, demonstrating how data is transmitted and received across seven layers of networking.


📜 OSI Model Layers Implemented
1️⃣ Application Layer → Accepts user input (message).
2️⃣ Presentation Layer → Encodes & encrypts data.
3️⃣ Session Layer → Establishes a session for communication.
4️⃣ Transport Layer → Segments data into smaller units.
5️⃣ Network Layer → Adds IP addressing for routing.
6️⃣ Data Link Layer → Adds MAC addressing for device-to-device delivery.
7️⃣ Physical Layer → Converts data into binary bits for transmission.


🚀 How to Run the Simulation
1️⃣ Clone the Repository
git clone https://github.com/your-username/OSI-Simulation.git
cd OSI-Simulation

2️⃣ Run the Python Script
python3 osi_simulation.py


3️⃣ Enter a Message and Observe the Output
Enter a message to send: Hello
Application Layer: Sending message -> 'Hello'
Presentation Layer: Encoding data -> b'Hello'
...
Physical Layer: Transmitting bits -> 1010101010

4️⃣ Reverse Process (Decapsulation)
Physical Layer: Receiving bits...
Presentation Layer: Decoding data -> 'Hello'
Application Layer: Message received -> 'Hello'

