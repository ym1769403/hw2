import csv
my_file = input()
word_freq = {}

with open (my_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        for word in line:
            if word in word_freq:
                word_freq[word]+= 1
            else:
                word_freq[word] = 1

for key in word_freq.keys():
    print(key+' '+str(word_freq[key]))