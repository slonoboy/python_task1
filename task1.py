def permutation(str, start, end):
    if start==end:
        print ("".join(str))
    else:
        for i in range(start, end+1):
            str[start], str[i] = str[i], str[start]
            permutation(str, start+1, end)
            str[start], str[i] = str[i], str[start]


ls = input("Enter symbols separating by space\n")
ls = ls.split()
permutation(ls, 0, len(ls)-1)
