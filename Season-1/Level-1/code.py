'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, InvalidOperation

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

TOTALAMOUNTLIMIT = Decimal('10000.00')

def validorder(order: Order):
    net = Decimal(0)
    total_payment = Decimal(0)
    
    for item in order.items:
        try:
            item_amount = Decimal(str(item.amount))
            item_quantity = int(item.quantity)
        except (ValueError, InvalidOperation):
            return "Invalid item values: %s" % item
        
        if item_quantity <= 0:
            return "Invalid item quantity: %s" % item.quantity

        if item.type == 'payment':
            total_payment += item_amount
            net += item_amount
        elif item.type == 'product':
            net -= item_amount * item_quantity
        else:
            return "Invalid item type: %s" % item.type

    if total_payment > TOTALAMOUNTLIMIT:
        return "Total amount payable for an order exceeded"

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id





