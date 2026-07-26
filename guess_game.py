import random

def number_guessing_game():
    print("=== እንኳን ወደ ቁጥር ግምት ጨዋታ በሰላም መጡ! ===")
    print("ከ 1 እስከ 100 ያለውን ምስጢራዊ ቁጥር ለመገመት ይሞክሩ።\n")
    
    # ከ 1 እስከ 100 ያለ የዘፈቀደ ቁጥር መምረጥ
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("ግምትዎን ያስገቡ (ከ1-100): "))
            attempts += 1

            if user_guess < secret_number:
                print("❌ በጣም አነስተኛ ነው! ከፍ ያለ ቁጥር ይሞክሩ።\n")
            elif user_guess > secret_number:
                print("❌ በጣም ትልቅ ነው! ዝቅ ያለ ቁጥር ይሞክሩ።\n")
            else:
                guessed = True
                print(f"🎉 እንኳን ደስ አለዎት! በ {attempts} ሙከራ ቁጥሩን አግኝተዋል!")
        except ValueError:
            print("⚠️ እባክዎን ትክክለኛ ቁጥር ብቻ ያስገቡ!\n")

if __name__ == "__main__":
    number_guessing_game()
          
