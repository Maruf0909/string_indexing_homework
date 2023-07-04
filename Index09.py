def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s[0]=="0" or s[0]=="1" or s[0]=="2" or s[0]=="3" or s[0]=="4" or s[0]=="5" or s[0]=="6":
        return int(s)
    
    return -1
print(main("4"))