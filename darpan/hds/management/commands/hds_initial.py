from django.core.management.base import BaseCommand, CommandError
from hds.models import Gate, Channel 
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate with initial data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete poll instead of closing it',
        )

    
    def handle(self, *args, **options):
        if options['delete']:
           
            print(Gate.objects.all().delete())
            print(Channel.objects.all().delete())
            print("All deleted")
        else:
            self.create_gates()
            self.create_channels()
            
            
    
    @transaction.atomic
    def create_gates(self):
        for g in Gate.GATES:
            number, name = g
            gate = Gate(number=number, name=name)
            gate.save()
            print(gate)
            
            
    @transaction.atomic
    def create_channels(self):
       for channel in Channel.CHANNELS:
            (1, 8), 'Inspiration', 'A creative Role Model', 'Individual'
            gates, name, title, circuit_group, circuit = channel
            g1, g2 = gates
            gate1 = Gate.objects.get(number=g1)
            gate2 = Gate.objects.get(number=g2)
            channel = Channel(gate1=gate1, gate2=gate2, name=name, title=title, circuit_group=circuit_group, circuit=circuit)
            channel.save()
            print(channel)
