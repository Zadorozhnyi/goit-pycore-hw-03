import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Check input parameters
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        print ("Error input parameters")
        return []

    # Generate unique random numbers in a given range
    ticket_numbers = random.sample(range(min, max + 1), quantity)

    # Return sorted list of numbers
    return sorted(ticket_numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)