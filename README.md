Certainly! Below are Finite State Machine (FSM) diagrams for the sender and receiver sides of the Reliable Data Transfer (RDT) protocol:

### Sender FSM Diagram:



### Receiver FSM Diagram:

### Pseudo-Code for RDT Sender:

```
procedure rdt_send(data):
    for each character in data:
        create_packet(sequence, character, calculate_checksum(character))
        send_packet_to_network_layer(packet)
        wait_for_ack_or_nak()

        while not received_ack_or_nak() or is_ack_or_nak_corrupted():
            resend_packet()

        switch_sequence_number()

    print("Sender Done!")
```

### Pseudo-Code for RDT Receiver:

```
procedure rdt_rcv(received_packet):
    if is_packet_corrupted(received_packet) or not is_expected_sequence(received_packet):
        send_ack_or_nak(flip_sequence(current_sequence))
        return

    deliver_data_to_application_layer(received_packet)
    send_ack_or_nak(current_sequence)
    switch_sequence()

    print("Receiver: received packet:", received_packet)
```

Note: The pseudo-code provided is a high-level representation and may need to be adapted based on the specific details and requirements of your RDT implementation.
###Contributers:
mostafa mohamed mostafa Ibraim sallam 
ID:49-6353
