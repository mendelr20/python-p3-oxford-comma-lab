def oxford_comma(items):
    if len(items) == 1:
        str = ''.join(items)
    elif len(items) == 2:
        str = " and ".join(items)
    else:
        str = f"{', '.join(items[:-1])}, and {items[-1]}"
        
    return str
        