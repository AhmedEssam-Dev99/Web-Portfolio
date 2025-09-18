import json
import os

# ===========================
# 📚 BOOK LIBRARY MANAGER
# ===========================

def get_list_items(prompt):
    """Helper function to collect a list of items from user input.
    Rejects inputs that are ONLY numbers.
    """
    items = []
    print(f"\n{prompt}")
    print("-" * 40)
    while True:
        item = input("📘 Enter item (or press ENTER to finish): ").strip()

        if item == "":
            break

        # 🚫 Decline if input is ONLY digits
        if item.isdigit():
            print("❌ Invalid input: Please enter a real book title, not just a number.")
            continue

        # 🔄 Prevent duplicates
        if item in items:
            print("⚠️  You already added this. Try another!")
            continue

        items.append(item)
        print(f"✅ Added: {item}")

    return items

def display_library_and_wishlist(books, wishlist):
    """Display current library and wishlist."""
    print("\n" + "="*50)
    print("📚 CURRENT LIBRARY:")
    print(" → " + ", ".join(books) if books else "Empty 😢")
    print("\n🌟 WISHLIST:")
    print(" → " + ", ".join(wishlist) if wishlist else "Empty 🎁")
    print("="*50 + "\n")

def save_data(books, wishlist, filename="library_data.json"):
    """Save books and wishlist to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'books': books, 'wishlist': wishlist}, f, indent=4)
    print(f"💾 Data saved to {filename}")

def load_data(filename="library_data.json"):
    """Load books and wishlist from a JSON file if it exists."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('books', []), data.get('wishlist', [])
    return [], []

# ===========================
# 🚀 PROGRAM START
# ===========================

print("\n" + "="*60)
print("            📚 WELCOME TO BOOK MANAGER 📚")
print("      Manage your library, wishlist & more!")
print("="*60)

# Ask if user wants to load saved data
if os.path.exists("library_data.json"):
    choice = input("\n📂 Found saved data. Load it? (y/n): ").strip().lower()
    if choice == 'y':
        books, wishlist = load_data()
        print("✅ Loaded your saved library and wishlist!")
    else:
        books = get_list_items("📚 Build Your Library")
        wishlist = get_list_items("🌟 Build Your Wishlist")
else:
    books = get_list_items("📚 Build Your Library")
    wishlist = get_list_items("🌟 Build Your Wishlist")

# Main interaction loop
while True:
    display_library_and_wishlist(books, wishlist)

    print("\n🛠️  What would you like to do?")
    print("1️⃣  ➜ Acquire a book from wishlist")
    print("2️⃣  ➜ Donate/remove a book from library")
    print("3️⃣  ➜ Add more books to library")
    print("4️⃣  ➜ Add more books to wishlist")
    print("5️⃣  ➜ Save progress to file")
    print("6️⃣  ➜ Exit")
    print()

    choice = input("👉 Choose an option (1-6) or press ENTER to exit: ").strip()

    if choice == "" or choice == "6":
        print("\n🙏 Thank you for using Book Manager! Happy reading! 📖")
        break

    elif choice == "1":
        if not wishlist:
            print("📭 Your wishlist is empty. Nothing to acquire!")
            continue

        while True:
            book = input(f"\nEnter the name of the book you acquired from wishlist {wishlist}:\n").strip()
            if book.isdigit():
                print("❌ Please enter a real book title, not just a number.")
                continue
            break

        if book in wishlist:
            wishlist.remove(book)
            books.append(book)
            print(f"🎉 Moved '{book}' from wishlist to library!")
        else:
            print(f"⚠️  '{book}' is not in your wishlist. Choose from: {wishlist}")

    elif choice == "2":
        if not books:
            print("📭 Your library is empty. Nothing to donate!")
            continue

        while True:
            book = input(f"\nEnter the name of the book you want to donate from library {books}:\n").strip()
            if book.isdigit():
                print("❌ Please enter a real book title, not just a number.")
                continue
            break

        if book in books:
            books.remove(book)
            print(f"💝 Donated '{book}'. Library updated!")
        else:
            print(f"⚠️  '{book}' is not in your library. Choose from: {books}")

    elif choice == "3":
        new_books = get_list_items("➕ Add More Books to Your Library")
        books.extend(new_books)
        print(f"✅ Added {len(new_books)} new book(s) to library!")

    elif choice == "4":
        new_wishes = get_list_items("➕ Add More Books to Your Wishlist")
        wishlist.extend(new_wishes)
        print(f"✅ Added {len(new_wishes)} new wish(es)!")

    elif choice == "5":
        save_data(books, wishlist)

    else:
        print("❌ Invalid option. Please choose 1-6.")

# Optional: Auto-save on exit
save_choice = input("\n💾 Would you like to save your data before exiting? (y/n): ").strip().lower()
if save_choice == 'y':
    save_data(books, wishlist)