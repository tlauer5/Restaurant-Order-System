from datetime import datetime
from django.test import TestCase
from .models import *

ALL_FIXTURES = [
    "waiters.json",
    "reservations.json",
    "tables.json",
    "chefs.json",
    "orders.json"
]

class WaitersTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_create_order(self):
        print("\nTESTCASE: Create Order (WaitersTests)")

        allOrders = Order.objects.filter()

        if not allOrders.exists():
            return

        numberOfOrdersBefore = allOrders.count()

        Order.objects.create(waiter_id=3,
                             table_id=13,
                             chef_id=None,
                             timestamp=datetime.now(),
                             status=Order.OrderStatus.UNASSIGNED,
                             dishId=63,
                             extraWishes='extra pepper')

        numberOfOrdersAfter = allOrders.count()

        if numberOfOrdersAfter > numberOfOrdersBefore:
            print('\nSuccessfully created new order!\n' +
                  'Orders before: ' + str(numberOfOrdersBefore) +
                  ' - Orders after: ' + str(numberOfOrdersAfter))

        print("\nEnd TESTCASE\n----------------------------------")

    def test_show_cooked_orders(self):
        print("\nTESTCASE: Show Cooked Orders (WaitersTests)")

        cookedOrders = Order.objects.filter(status=Order.OrderStatus.COOKED)

        for order in cookedOrders:
            print(order.info_for_waiter())

        print("\nEnd TESTCASE\n----------------------------------")

    def test_delete_order(self):
        print("\nTESTCASE: Delete Order (WaitersTests)")

        allOrders = Order.objects.filter()

        if not allOrders.exists():
            return

        numberOfOrdersBefore = allOrders.count()

        orderToDeletePk = 4

        Order.objects.filter(pk=orderToDeletePk).delete()

        numberOfOrdersAfter = allOrders.count()

        if numberOfOrdersAfter < numberOfOrdersBefore:
            print('\nSuccessfully deleted an order!\n' +
                  'Orders before: ' + str(numberOfOrdersBefore) +
                  ' - Orders after: ' + str(numberOfOrdersAfter))

        print("\nEnd TESTCASE\n----------------------------------")


    def test_create_reservation(self):
        print("\nTESTCASE: Create Reservation (WaitersTests)")

        allReservations = Reservation.objects.filter()

        if not allReservations.exists():
            return

        numberOfReservationsBefore = allReservations.count()

        firstTablePk, secondTablePk= 15, 16

        newReservation = Reservation.objects.create(customerName='Mayer',
                                                    timestamp="2022-05-27T18:00:00.00Z",
                                                    places=8)

        newReservation.table.set([firstTablePk, secondTablePk])

        numberOfReservationsAfter = allReservations.count()

        if numberOfReservationsAfter > numberOfReservationsBefore:
            print('\nSuccessfully created new reservation!\n' +
                  'Reservations before: ' + str(numberOfReservationsBefore) +
                  ' - Reservations after: ' + str(numberOfReservationsAfter))

        print("\nEnd TESTCASE\n----------------------------------")

class ChefsTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_show_unassigned_orders(self):
        print("\nTESTCASE: Show Unassigned Orders (ChefsTests)")

        unassignedOrders = Order.objects.filter(status=Order.OrderStatus.UNASSIGNED)

        for order in unassignedOrders:
            print(order.info_for_chef())

        print("\nEnd TESTCASE\n----------------------------------")

    def test_assign_order_to_chef(self):
        print("\nTESTCASE: Assign Order To Chef (ChefsTests)")

        newOrderPk = 1

        unassignedOrders = Order.objects.filter(status=Order.OrderStatus.UNASSIGNED)

        if not unassignedOrders.exists():
            return

        orderToAssignPk = unassignedOrders[0].pk

        # Current PK and Status
        print(Order.objects.filter(pk=orderToAssignPk)[0].info_for_chef())

        # Update PK and Status
        Order.objects.filter(pk=orderToAssignPk).update(chef=newOrderPk, status=Order.OrderStatus.IN_PROGRESS)

        # Updated PK and Status
        print(Order.objects.filter(pk=orderToAssignPk)[0].info_for_chef())

        print("\nEnd TESTCASE\n----------------------------------")


class AdminsTest(TestCase):
    fixtures = ALL_FIXTURES

    def test_create_new_waiter(self):
        print("\nTESTCASE: Create New Waiter (AdminsTests)")

        allWaiters = Waiter.objects.filter()

        numberOfWaitersBefore = allWaiters.count()

        if not allWaiters.exists():
            return

        Waiter.objects.create(surname="Mario",
                              lastname="Kluge")

        numberOfWaitersAfter = allWaiters.count()

        if numberOfWaitersAfter > numberOfWaitersBefore:
            print('\nSuccessfully created new Waiter!\n' +
                  'Waiters before: ' + str(numberOfWaitersBefore) +
                  ' - Waiters after: ' + str(numberOfWaitersAfter))

        print("\nEnd TESTCASE\n----------------------------------")
