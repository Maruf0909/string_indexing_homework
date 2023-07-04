def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum=0
    if s[0].isdigit():
        sum+= int(s[0])
    if s[1].isdigit():
        sum+= int(s[1])
    if s[2].isdigit():
        sum+= int(s[2])
    if s[3].isdigit():
        sum+= int(s[3])
    if s[4].isdigit():
        sum+= int(s[4])

    return sum
print(main("10007"))