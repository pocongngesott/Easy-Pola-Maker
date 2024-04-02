import random
from datetime import datetime, timedelta

def pilih_random_angka_manual():
    return random.randint(11, 19)

def pilih_random_angka_auto():
    choices = [10, 20, 30, 50]
    return random.choice(choices)

def pilih_random_angka(mode):
    if mode == "MANUAL":
        return pilih_random_angka_manual()
    elif mode == "AUTO":
        return pilih_random_angka_auto()

def pilih_random_simbol():
    symbols = ["❌✅❌", "❌❌✅", "✅❌❌", "✅❌✅", "❌✅✅", "❌❌❌"]
    return random.choice(symbols)

def pilih_random_dc():
    return random.choice(["DC OFF", "DC ON"])

# Display ASCII art banner for POLA GACOR in the terminal
print("""
██████╗  ██████╗ ██╗      █████╗      ██████╗  █████╗  ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██║     ██╔══██╗    ██╔════╝ ██╔══██╗██╔════╝██╔═══██╗██╔══██╗
██████╔╝██║   ██║██║     ███████║    ██║  ███╗███████║██║     ██║   ██║██████╔╝
██╔═══╝ ██║   ██║██║     ██╔══██║    ██║   ██║██╔══██║██║     ██║   ██║██╔══██╗
██║     ╚██████╔╝███████╗██║  ██║    ╚██████╔╝██║  ██║╚██████╗╚██████╔╝██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                                                                              
              ┌П┐(ಠ_ಠ) ┌П┐ Created by: SEO-SEOAN ┌П┐(ಠ_ಠ) ┌П┐ 
==================================================================================                                                                              
""")

# Ask for POLA UNTUK SITUS
pola_situs = input("POLA UNTUK SITUS ? : ")
# Ask for preferred games with updated question prompt
preferred_games_pragmatic = input("PP Mau Game Apa Bossku? (Pisahkan dengan koma): ")
preferred_game_list_pragmatic = [game.strip() for game in preferred_games_pragmatic.split(',')]

# Ask the user for the names of the games
preferred_games_pg = input("PG Mau Game Apa Bossku? (Pisahkan dengan koma): ")
preferred_game_list_pg = [game.strip() for game in preferred_games_pg.split(',')]

# Get the current date and adjust it to the next day
current_date = datetime.now() + timedelta(days=1)
formatted_date = current_date.strftime("%d %B %Y")

# Open hasil.txt file in write mode with utf-8 encoding
with open("hasil.txt", "w", encoding="utf-8") as file:
    # Write the INFO POLA GACOR to the file
    file.write(f"🎰 INFO POLA GACOR {pola_situs} {formatted_date} 🎰\n")

    # Write the PRAGMATIC label to the file
    file.write("\n🔥 PRAGMATIC 🔥\n")

    # Display results for each preferred PRAGMATIC game
    for idx, game_name in enumerate(preferred_game_list_pragmatic, start=1):
        file.write(f"\n🎯 {game_name}\n")

        results = []
        for _ in range(2):  # Ensure 2 "MANUAL" choices
            angka = pilih_random_angka("MANUAL")
            simbol = pilih_random_simbol()
            mode = "MANUAL"
            dc = pilih_random_dc()
            results.append((angka, simbol, mode, dc))

        for _ in range(2):  # Ensure 2 "AUTO" choices
            angka = pilih_random_angka("AUTO")
            simbol = pilih_random_simbol()
            mode = "AUTO"
            dc = pilih_random_dc()
            results.append((angka, simbol, mode, dc))

        # Shuffle the results
        random.shuffle(results)

        # Randomly choose the position for "NAIKAN BET LALU"
        bet_lalu_position = random.randint(1, 3)

        # Write the results for the current game to the file
        for i, hasil in enumerate(results, start=1):
            angka, simbol, mode, dc = hasil
            hasil_gabungan = f"{angka}X {simbol} {mode} {dc}\n"
            file.write(hasil_gabungan)

            # Insert "NAIKAN BET LALU" if it's the chosen position
            if i == bet_lalu_position:
                file.write("NAIKAN BET LALU\n")

    # Write the PG SOFT label to the file
    file.write("\n🔥 PG SOFT 🔥\n")

    # Display results for each preferred PG game
    for game_name in preferred_game_list_pg:
        file.write(f"\n🎯 {game_name}\n")
        modes = ["MANUAL", "AUTO"] * 2  # Ensure 2 MANUAL and 2 AUTO modes
        random.shuffle(modes)

        # Track whether NAIKAN BET LALU has appeared
        naikan_bet_lalu_appeared = False

        for mode in modes:
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 30, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 20)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            # Write the result to the file
            hasil_gabungan = f"{angka} {mode} {dc}\n"
            file.write(hasil_gabungan)

            # Randomly choose whether to write "NAIKAN BET LALU" if it hasn't appeared yet
            if not naikan_bet_lalu_appeared and random.random() < 0.5:
                file.write("NAIKAN BET LALU\n")
                naikan_bet_lalu_appeared = True

        # 50/50 chance of writing "ULANGI SAMPAI 2X"
        if random.random() < 0.5:
            file.write("ULANGI SAMPAI 2X\n")

    # Write the note to the file
    file.write("\n\nNote: bet sesuai saldo anda, ingat tetap santai dan jangan terbawa suasana.\n")

# Confirmation message
print("Hasil telah disimpan dalam file 'hasil.txt'.")
