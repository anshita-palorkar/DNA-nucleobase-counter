print("Welcome to the DNA nucelotide counter!")
start = 0
while start != "no":
    start = input("Press any key to start; 'no' to quit ")
    if start == "no":
        break
    else:
        dna = input("Enter DNA sequence: ").lower()
        num_a = dna.count('a')
        num_t = dna.count('t')
        num_g = dna.count('g')
        num_c = dna.count('c')
        print("\nAdenosine: %d \nThymine: %d \nGuanine: %d \nCytosine: %d\n" % (num_a, num_t, num_g, num_c))

print("See you later!")
