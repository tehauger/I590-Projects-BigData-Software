import sys

def fizzbuzz(n):
    """
	Returns "fizz" if entry is a multiple of 2, "buzz" if entry is multiple of 3, "fizzbuzz" if entry is multiple of 2 and 3, and original number entry if a multiple of neither
	"""
x=(n/2.0)
y=(n/3.0)

if (x).is_integer() and (y).is_integer():
    return 'fizzbuzz'
elif (x).is_integer() :
    return 'fizz'
elif (y).is_integer():
    return 'buzz'
else:
    return n
    
if __name__ == '__main__':
    n=int(sys.argv[1])
    print fizzbuzz(n)
	
