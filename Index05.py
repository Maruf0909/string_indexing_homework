def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    countr=0

    if s[0].isdigit():
        countr+=1
    if s[1].isdigit():
        countr+=1
    if s[2].isdigit():
        countr+=1
    if s[3].isdigit():
        countr+=1
    if s[4].isdigit():
        countr+=1
    return countr 
print(main("1xs40"))