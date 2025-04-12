# 🔐 Secret Auction Program (Silent Bidding Game)

This is a simple **Python-based silent auction** tool that collects anonymous bids and determines the highest bidder. Built for beginner coders learning about dictionaries, loops, and user input handling.

---

## 🛠 Features

- Accepts multiple bids using a loop
- Stores each bid securely in a dictionary
- Clears the screen (simulated with line breaks) to keep bids hidden
- Determines and displays the highest bidder
- Uses ASCII art from the `art` module for visual flair

---

## 📦 Requirements

- Python 3.x  
- `art` module for displaying the logo

Install it with:

```bash
pip install art
```

---

## 📁 Project Structure

```
secret_auction/
├── auction.py        # Main script with the auction logic
└── art.py            # Contains ASCII logo (logo variable)
```

---

## ▶️ How to Run

```bash
python auction.py
```

You'll be prompted to:

1. Enter your name  
2. Enter your bid  
3. Indicate if there are more bidders  

Each bidder's information remains private thanks to screen clearing.

---

## 🧠 How It Works

```python
dict[name] = bid
```

All bids are stored in a dictionary with names as keys and bid amounts as values. Once all bids are collected, the program scans for the **highest bidder** and announces the winner.

---

## 💡 Example Output

```plaintext
Enter your name: Alice
Enter your Bit $: 200
Are there any other bidders? Type 'yes or 'no': yes

[Screen Clears]

Enter your name: Bob
Enter your Bit $: 350
Are there any other bidders? Type 'yes or 'no': no

The winner is Bob with a bid of $350
```

---

## 🔧 Potential Improvements

- Use the `os` module to clear the terminal more cleanly (`os.system('clear' or 'cls')`)
- Add input validation for numeric bids
- Store bids in a file or database
- Allow ties or bid increments
- GUI version for enhanced UX


## 👨‍💻 Author

Built with ❤️ by Parth Koshti
