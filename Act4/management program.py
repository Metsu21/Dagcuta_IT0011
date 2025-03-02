import csv

records, current_file = [], None

def load_records(file_name):
    recs = []
    try:
        with open(file_name, 'r', newline='') as f:
            for row in csv.reader(f):
                if len(row) < 5: continue
                try:
                    recs.append((row[0], (row[1], row[2]), float(row[3]), float(row[4])))
                except ValueError:
                    continue
        print(f"Loaded {len(recs)} record(s) from {file_name}.")
    except Exception as e:
        print("Error loading file:", e)
    return recs

def save_records(file_name, recs):
    try:
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            for r in recs:
                writer.writerow([r[0], r[1][0], r[1][1], r[2], r[3]])
        print("Records saved to", file_name)
    except Exception as e:
        print("Error saving file:", e)

def show_all(recs):
    print("{:<10} {:<15} {:<15} {:<18} {:<15}".format("ID", "First Name", "Last Name", "Class Standing", "Major Exam"))
    print("-" * 75)
    for r in recs:
        print("{:<10} {:<15} {:<15} {:<18} {:<15}".format(r[0], r[1][0], r[1][1], r[2], r[3]))

def weighted(r): 
    return 0.6 * r[2] + 0.4 * r[3]

def show_student_record(recs):
    sid = input("Enter Student ID: ")
    for r in recs:
        if r[0] == sid:
            print(f"\nID: {r[0]}\nFirst Name: {r[1][0]}\nLast Name: {r[1][1]}\nClass Standing: {r[2]}\nMajor Exam: {r[3]}\nWeighted Grade: {weighted(r)}")
            return
    print("Record not found.")

def add_record(recs):
    sid = input("Enter Student ID (6 digits): ")
    if len(sid) != 6 or not sid.isdigit():
        return print("Invalid Student ID.")
    fn = input("Enter First Name: ")
    ln = input("Enter Last Name: ")
    try:
        cs = float(input("Enter Class Standing grade: "))
        me = float(input("Enter Major Exam grade: "))
    except:
        return print("Invalid grade input.")
    recs.append((sid, (fn, ln), cs, me))
    print("Record added.")

def edit_record(recs):
    sid = input("Enter Student ID to edit: ")
    for i, r in enumerate(recs):
        if r[0] == sid:
            fn = input("New First Name (leave blank to keep current): ") or r[1][0]
            ln = input("New Last Name (leave blank to keep current): ") or r[1][1]
            try:
                cs = float(input("New Class Standing grade (leave blank to keep current): ") or r[2])
                me = float(input("New Major Exam grade (leave blank to keep current): ") or r[3])
            except:
                return print("Invalid grade input.")
            recs[i] = (sid, (fn, ln), cs, me)
            print("Record updated.")
            return
    print("Record not found.")

def delete_record(recs):
    sid = input("Enter Student ID to delete: ")
    for i, r in enumerate(recs):
        if r[0] == sid:
            if input(f"Delete record for {r[1][0]} {r[1][1]}? (y/n): ").lower() == 'y':
                recs.pop(i)
                print("Record deleted.")
            return
    print("Record not found.")

def main():
    global records, current_file
    while True:
        print("==================================")
        print("    Student Record Management ")
        print("==================================")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        c = input("Choice (1-11): ")
        if c == '1':
            current_file = input("Enter file name: ")
            records = load_records(current_file)
        elif c == '2':
            if current_file: save_records(current_file, records)
            else: print("No file open. Use Save As.")
        elif c == '3':
            current_file = input("Enter new file name: ")
            save_records(current_file, records)
        elif c == '4':
            show_all(records)
        elif c == '5':
            show_all(sorted(records, key=lambda r: r[1][1]))
        elif c == '6':
            show_all(sorted(records, key=weighted))
        elif c == '7':
            show_student_record(records)
        elif c == '8':
            add_record(records)
        elif c == '9':
            edit_record(records)
        elif c == '10':
            delete_record(records)
        elif c == '11':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
