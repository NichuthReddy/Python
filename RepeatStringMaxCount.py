"""
Input: abca, 8 ; Output:a, bca, abcabcab, 2
Input: nic,8 ; Output: ,nic, nicnicni, 2
Input: nnann,11 ; Output: nn, ann, nnannannann, 3
Input: nnan,13 ; Output: n, nan, nnannannannan, 4
"""
input_string=input("enter substring: ")
string_length=int(input("end string length: "))

prefix=""
for i,j in zip(range(0,len(input_string)//2),range(-1,-len(input_string)//2,-1)):
    if input_string[i]==input_string[j] :
        prefix+=input_string[i]
    else:
        break;

repeat_string=input_string[len(prefix):]
prstring=(string_length-len(prefix))//len(repeat_string) #repeated string length to be multiplied
output_string=prefix+repeat_string*(prstring+2) # +2 is to fill the extra characters
print("common prefix:",prefix)
print("repeat string:",repeat_string)
print("output string:",output_string[:string_length])
print("input count in ouput string:",prstring)
