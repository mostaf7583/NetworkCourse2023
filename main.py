from network import NetworkLayer
from receiver import ReceiverProcess
from sender import SenderProcess, RDTSender
import sys

if __name__ == '__main__':
   
# make adummy args
    args = {'msg': 'TEST', 'rel': '0.7', 'delay': '0', 'debug': '0', 'pkt': '1', 'ack': '1'}
    print(sys.argv)
    msg = args['msg']
    prob_to_deliver = float(args['rel'])
    delay = int(args['delay'])
    debug = bool(int(args['debug']))
    corrupt_pkt = True
    corrupt_ack = True
    if debug:
        corrupt_pkt = bool(int(args['pkt']))
        corrupt_ack = bool(int(args['ack']))

    SenderProcess.set_outgoing_data(msg)

    print(f'Sender is sending:{SenderProcess.get_outgoing_data()}')

    network_serv = NetworkLayer(reliability=prob_to_deliver, delay=delay, pkt_corrupt=corrupt_pkt,
                                ack_corrupt=corrupt_ack)

    rdt_sender = RDTSender(network_serv)
    
    rdt_sender.rdt_send(SenderProcess.get_outgoing_data())

    print(f'Receiver received: {ReceiverProcess.get_buffer()}')
