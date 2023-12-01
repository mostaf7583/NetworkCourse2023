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
function rdt_rcv(rcv_pkt):
    if (is_corrupted(rcv_pkt) || !is_expected_seq(rcv_pkt, sequence)):
        print("Receiver: received corrupted packet:", rcv_pkt)
        return make_reply_pkt(flipped, ord(flipped))

    if (sequence == '0'):
        sequence = '1'
    else:
        sequence = '0'

    ReceiverProcess.deliver_data(rcv_pkt['data'])
    print("Receiver: received packet:", rcv_pkt)

    reply_pkt = make_reply_pkt(sequence, ord(sequence))
    return reply_pkt
```

Here's a breakdown of the pseudocode:

1. **Check for corrupted or unexpected packet:**
   - If the packet is corrupted or not the expected sequence, print an error message.
   - Create and return a reply packet with the flipped sequence number.

2. **Update the sequence number:**
   - Toggle the sequence number between '0' and '1'.

3. **Deliver data to the application layer:**
   - Pass the received packet's data to the ReceiverProcess.deliver_data function.

4. **Print the received packet data:**
   - Display a message indicating the received packet.

5. **Create the reply packet:**
   - Generate a reply packet using the updated sequence number and its ASCII code value.

6. **Return the reply packet:**
   - Send the generated reply packet back to the sender.

###Contributers:
mostafa mohamed mostafa Ibraim sallam 
ID:49-6353
