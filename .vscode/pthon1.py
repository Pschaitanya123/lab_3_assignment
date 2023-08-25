def sort_table(data, sort_param):
    if sort_param == "P_ID":
        return sorted(data, key=lambda x: x[0])
    elif sort_param == "Process":
        return sorted(data, key=lambda x: x[1])
    elif sort_param == "Start Time":
        return sorted(data, key=lambda x: x[2])
    elif sort_param == "Priority":
        return sorted(data, key=lambda x: (x[3], x[0]))  # Sort by priority, then by P_ID
    else:
        print("Invalid sorting parameter.")
        return data

flight_table = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low")
]

print("Flight Table:")
print("P_ID\tProcess\tStart Time\tPriority")
for row in flight_table:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

sorting_param = input("Enter the sorting parameter (P_ID/Process/Start Time/Priority): ").strip()
sorted_table = sort_table(flight_table, sorting_param)

print("\nSorted Flight Table:")
print("P_ID\tProcess\tStart Time\tPriority")
for row in sorted_table:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")
