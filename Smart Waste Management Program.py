import json
import os

waste_file="waste_history.json"

#default waste items
waste_items={
    "plastic bottle":{"category":"recyclable","bin":"blue","method":"send for plastic recycling"},
    "newspaper":{"category":"paper","bin":"blue","method":"send for paper recycling"},
    "cardboard":{"category":"paper","bin":"blue","method":"send for paper recycling"},
    "banana peel":{"category":"organic","bin":"green","method":"composting"},
    "vegetable waste":{"category":"organic","bin":"green","method":"composting"},
    "food waste":{"category":"organic","bin":"green","method":"composting"},
    "glass bottle":{"category":"glass","bin":"blue","method":"send for glass recycling"},
    "metal can":{"category":"metal","bin":"blue","method":"send for metal recycling"},
    "battery":{"category":"hazardous","bin":"red","method":"special hazardous waste disposal"},
    "medicine":{"category":"hazardous","bin":"red","method":"special medical waste disposal"},
    "used tissue":{"category":"general","bin":"black","method":"dispose as general waste"},
    "chips packet":{"category":"non-recyclable","bin":"black","method":"dispose as general waste"},
    "broken ceramic":{"category":"general","bin":"black","method":"dispose as general waste"}
}


def load_history():
    if os.path.exists(waste_file):
        try:
            with open(waste_file,"r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_history(history):
    with open(waste_file,"w") as file:
        json.dump(history,file,indent=4)


history=load_history()


#display available waste items
def show_waste_items():
    print("\n========== Waste Items ==========")

    for item in waste_items:
        print("-",item)


#sort a waste item
def sort_waste():
    print("\n========== Waste Sorter ==========")

    item=input("Enter the waste item: ").strip().lower()

    if item in waste_items:
        data=waste_items[item]

        print("\nWaste item:",item)
        print("Category  :",data["category"])
        print("Bin       :",data["bin"].upper())
        print("Disposal  :",data["method"])

        record={
            "item":item,
            "category":data["category"],
            "bin":data["bin"]
        }

        history.append(record)
        save_history(history)

    else:
        print("\nWaste item not found.")
        print("You can add it using the Add Waste Item option.")


#add a new waste item
def add_waste_item():
    print("\n========== Add Waste Item ==========")

    item=input("Enter waste item name: ").strip().lower()

    if not item:
        print("Item name cannot be empty.")
        return

    if item in waste_items:
        print("This waste item already exists.")
        return

    print("\nCategories:")
    print("1. Recyclable")
    print("2. Paper")
    print("3. Organic")
    print("4. Glass")
    print("5. Metal")
    print("6. Hazardous")
    print("7. Non-recyclable")
    print("8. General")

    choice=input("Enter category number: ").strip()

    categories={
        "1":"recyclable",
        "2":"paper",
        "3":"organic",
        "4":"glass",
        "5":"metal",
        "6":"hazardous",
        "7":"non-recyclable",
        "8":"general"
    }

    if choice not in categories:
        print("Invalid category.")
        return

    category=categories[choice]

    #select bin according to category
    if category in ["recyclable","paper","glass","metal"]:
        bin_name="blue"

    elif category=="organic":
        bin_name="green"

    elif category=="hazardous":
        bin_name="red"

    else:
        bin_name="black"

    method=input("Enter disposal method: ").strip()

    if not method:
        method="dispose according to local waste guidelines"

    waste_items[item]={
        "category":category,
        "bin":bin_name,
        "method":method
    }

    print("\nWaste item added successfully!")
    print("Recommended bin:",bin_name)


#search for a waste item
def search_waste():
    print("\n========== Search Waste ==========")

    search=input("Enter waste item to search: ").strip().lower()

    found=[]

    for item in waste_items:
        if search in item:
            found.append(item)

    if not found:
        print("No matching waste item found.")
        return

    print("\nMatching items:")

    for item in found:
        data=waste_items[item]

        print("\nItem:",item)
        print("Category:",data["category"])
        print("Bin:",data["bin"].upper())
        print("Disposal:",data["method"])


#show waste statistics
def statistics():
    print("\n========== Waste Statistics ==========")

    if not history:
        print("No waste has been sorted yet.")
        return

    category_count={}
    bin_count={}

    for record in history:

        category=record["category"]
        bin_name=record["bin"]

        if category in category_count:
            category_count[category]+=1
        else:
            category_count[category]=1

        if bin_name in bin_count:
            bin_count[bin_name]+=1
        else:
            bin_count[bin_name]=1

    print("\nTotal waste sorted:",len(history))

    print("\nBy category:")

    for category,count in category_count.items():
        print(category,":",count)

    print("\nBy bin:")

    for bin_name,count in bin_count.items():
        print(bin_name.upper(),"bin:",count)


#view sorting history
def view_history():
    print("\n========== Sorting History ==========")

    if not history:
        print("No sorting history available.")
        return

    for i,record in enumerate(history,1):
        print(
            i,
            ".",
            record["item"],
            "->",
            record["bin"].upper(),
            "bin",
            "(" + record["category"] + ")"
        )


#clear history
def clear_history():
    global history

    print("\n========== Clear History ==========")

    if not history:
        print("History is already empty.")
        return

    choice=input(
        "Are you sure you want to clear history? (yes/no): "
    ).strip().lower()

    if choice=="yes":
        history=[]
        save_history(history)
        print("History cleared successfully.")

    else:
        print("History was not cleared.")


#main menu
def main():

    while True:

        print("\n")
        print("==========================================")
        print("        SMART WASTE SORTER SYSTEM")
        print("==========================================")

        print("\n1. Sort Waste")
        print("2. Show Waste Items")
        print("3. Search Waste")
        print("4. Add Waste Item")
        print("5. View Sorting History")
        print("6. Waste Statistics")
        print("7. Clear History")
        print("8. Exit")

        choice=input("\nEnter your choice: ").strip()

        if choice=="1":
            sort_waste()

        elif choice=="2":
            show_waste_items()

        elif choice=="3":
            search_waste()

        elif choice=="4":
            add_waste_item()

        elif choice=="5":
            view_history()

        elif choice=="6":
            statistics()

        elif choice=="7":
            clear_history()

        elif choice=="8":
            print("\nThank you for using Smart Waste Sorter!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()
