""" Krunal Patel SDEV 300 """

def calculate_sum_and_range(numbers):
    """ calculate sum and find range in a list """
    if not all(isinstance(x, (int, float)) for x in numbers):
        print("Error")
        return
    total_sum = sum(numbers)
    total_range = max(numbers) - min(numbers)
    print(f"Sum = {total_sum}, Range = {total_range}")

calculate_sum_and_range([34])
