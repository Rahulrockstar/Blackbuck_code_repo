entries = []
duplicate_entries = []
with open('sucess.csv', 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[2] not in entries:
            entries.append(columns[2])
        else:
            duplicate_entries.append(columns[2])

if len(duplicate_entries) > 0:
    with open('out.txt', 'w') as out_file:
        with open('sucess.csv', 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if columns[2] in duplicate_entries:
                    print(line.strip())
                    out_file.write(line)
else:
    print("No repetitions")
