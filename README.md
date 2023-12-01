Certainly! Below are Finite State Machine (FSM) diagrams for the sender and receiver sides of the Reliable Data Transfer (RDT) protocol:

### Sender FSM Diagram:



### Receiver FSM Diagram:

### Pseudo-Code for RDT Sender:
```
function rdt_send(process_buffer):
    for each data in process_buffer:
        checksum = get_checksum(data)
        pkt = make_pkt(sequence, data, checksum)
        pkt_clone = clone_packet(pkt)
        print('Sender:', pkt)
        reply = net_srv.udt_send(pkt)
        print('reply', reply)

        while is_corrupted(reply) or not is_expected_seq(reply, sequence):
            print('Sender: received corrupted packet:', reply)
            print('Sender: resending packet:', pkt)
            checksum = get_checksum(data)
            pkt = make_pkt(sequence, data, checksum)
            reply = net_srv.udt_send(pkt)

        if sequence == '0':
            sequence = '1'
        else:
            sequence = '0'

    print('Sender Done!')
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

![image](https://github.com/mostaf7583/NetworkCourse2023/assets/73074293/09b175f7-b081-4a28-822d-55423046be62)

### Contributers:
mostafa mohamed mostafa Ibraim sallam 
ID:49-6353
