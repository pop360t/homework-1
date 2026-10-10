# Problem 1
def reverse(text):
    return str(text).upper()[::-1] # Converts to uppercase and reverses text

# Problem 2
def fill_gaps(text):
    return text.replace(" ", "_") # Replaces spaces with underscores

# Problem 3
def emoji_convert(text):
    emoji_dict = { # Maps symbols to emojis
        "<3": "❤️",
        ":o": "😮",
        ":)": "🙂",
        ":D": "😃",
        ":(": "🙁",
        ":p": "😛",
        ":P": "😛",
    }
    for emoticon, emoji in emoji_dict.items(): # Repeats for each item in emoji_dict
        text = text.replace(emoticon, emoji)
    return text

# Problem 4
def convert_temp():
    while True:
        celsius_input = input("Convert ºC to ºF: ").strip()
        try: # Ensures the user enters an actual number
            c_value = float(celsius_input)
            f_value = c_value * 1.8 + 32
            return f"{c_value:8.3f}ºC is equal to {f_value:.3f}ºF"
        except ValueError:
            print("Please enter a valid number") # Error message

def main(): # Main function which contains the menu loop
    while True:
        selection = input("\nWhich function would you like to run? (1, 2, 3, 4) — Enter 'q' to quit\n").strip()
        if selection == "1":
            print(reverse(input("Enter something to reverse: ")))
        elif selection == "2":
            print(fill_gaps(input("Enter text to replace spaces with underscores: ")))
        elif selection == "3":
            print(emoji_convert(input("Enter symbols to turn them into emojis: ")))
        elif selection == "4":
            print(convert_temp())
        elif selection == "q":
            print("=" * 25)
            break
        else:
            print("Enter a valid selection")

if __name__ == "__main__":
    main() # Calls main
