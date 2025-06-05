#take inputs of m & n (input method takes the input from users as a string while executing)

m = input("input m value?")  # m is a variable of data type of assigned value

n = input("input n value?")  # python variables have dynamic data types

#typecast if necessary

m_int =int(m) # cast string m to int m, like that we can cast it to float(m), str(m), bool(m)

n_int=int(n) # to know the datatype of variable use type(variable)   

#type(2) -> int, type(2.0) -> float, type("3") -> str(string), type(true) ->bool

#logic or transformation (Arithmetic operators)

m_root_n = n_int**(1/m_int) 

# 3**4 ->81 power, 12/5 -> 2.4, 12//5 -> 2( divisor without decimal), 12%5 = 2(reminder)

#3+4=7, 3-4=-1, 3*4=12

#print the output data

print(f"{m} root of {n} is {m_root_n}")

#print(m,"root of",n,"is",m_root_m)

#print("%d root of %d is %d"%(m,n,m_root_n))

'''Any thing placed in 3 single or double quotes is considered as comment. generally used for multiple line code'''

"""print syntax 

default parameters -> print("Hello", "World", sep=" ", end="\n", flush=False, file=sys.stdout)

output displaying if file-> print("Hello", "World", sep="-", end="!", flush=True, file=open("output.txt", "w"))

"""
