def Add(numbers: str) -> int:
    if numbers == "":
        return 0
 
    numbers = numbers.replace("\n",",")
    nums = numbers.split(",")
 
    total = 0
    for n in nums:
        if(n==""):
            raise ValueError("Error")
        if not n.isdigit():
            raise ValueError("Error")
        total += int(n)
 
    return total