from datetime import datetime, timedelta
import random


def generate_spade_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2  # Ensure 2 MANUAL and 2 AUTO modes
        random.shuffle(modes)

        # Track whether NAIKAN BET LALU has appeared
        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)  # Choose position for NAIKAN BET LALU

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 25, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 19)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            # Store the result
            hasil_gabungan = f"{angka} {mode} {dc}"

            # Randomly choose whether to include "NAIKAN BET LALU" if it hasn't appeared yet
            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        # Append "HENTIKAN PUTAR OTOMATIS\nKEMENANGAN FREE SPIN ✔️" to the end of the game results
        game_results.append("HENTIKAN PUTAR OTOMATIS\nKEMENANGAN FREE SPIN ✔️")

        results.append((game_name, game_results))

    return results


def generate_habanero_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2  # Ensure 2 MANUAL and 2 AUTO modes
        random.shuffle(modes)

        # Track whether NAIKAN BET LALU has appeared
        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)  # Choose position for NAIKAN BET LALU

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 30, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 20)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            # Store the result
            hasil_gabungan = f"{angka} {mode} {dc}"

            # Randomly choose whether to include "NAIKAN BET LALU" if it hasn't appeared yet
            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        # 100% chance of including "ULANGI SAMPAI 2X"
        game_results.append("ULANGI SAMPAI 2X")

        results.append((game_name, game_results))

    return results


# Rename the functions to avoid conflicts
def pilih_random_angka_manual_pg():
    return random.randint(11, 19)


def pilih_random_angka_auto_pg():
    choices = [10, 20, 30, 50]
    return random.choice(choices)


def pilih_random_angka_pg(mode):
    if mode == "MANUAL":
        return pilih_random_angka_manual_pg()
    elif mode == "AUTO":
        return pilih_random_angka_auto_pg()


def pilih_random_simbol_pg():
    symbols = ["❌✅❌", "❌❌✅", "✅❌❌", "✅❌✅", "❌✅✅", "❌❌❌"]
    return random.choice(symbols)


def pilih_random_dc_pg():
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

# Ask the user if they want to add HABANERO or SPADE GAMING games
mau_nambah = input("Mau Nambah Game HABANERO atau SPADE GAMING? (hab/spd/tidak): ")
preferred_game_list_hb = []
preferred_game_list_spd = []

if mau_nambah.lower() == "hab":
    preferred_games_hb = input("HAB Mau Game Apa Bossku? (Pisahkan dengan koma): ")
    preferred_game_list_hb = [game.strip() for game in preferred_games_hb.split(',')]
elif mau_nambah.lower() == "spd":
    preferred_games_spd = input("SPD Mau Game Apa Bossku? (Pisahkan dengan koma): ")
    preferred_game_list_spd = [game.strip() for game in preferred_games_spd.split(',')]

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

        # Track whether NAIKAN BET LALU has appeared
        naikann_bet_lalu_appeared = False

        results = []
        for _ in range(2):  # Ensure 2 "MANUAL" choices
            angka = pilih_random_angka_pg("MANUAL")
            simbol = pilih_random_simbol_pg()
            mode = "MANUAL"
            dc = pilih_random_dc_pg()
            results.append((angka, simbol, mode, dc))

        for _ in range(2):  # Ensure 2 "AUTO" choices
            angka = pilih_random_angka_pg("AUTO")
            simbol = pilih_random_simbol_pg()
            mode = "AUTO"
            dc = pilih_random_dc_pg()
            results.append((angka, simbol, mode, dc))

        # Shuffle the results
        random.shuffle(results)

        # Randomly choose the position for "NAIKAN BET LALU"
        naikan_bet_lalu_position = random.randint(2, 4)

        # Write the results for the current game to the file
        for i, hasil in enumerate(results, start=1):
            angka, simbol, mode, dc = hasil
            hasil_gabungan = f"{angka}X {simbol} {mode} {dc}\n"

            # Insert "NAIKAN BET LALU" if it's the chosen position
            if i == naikan_bet_lalu_position and not naikann_bet_lalu_appeared:
                file.write("NAIKAN BET LALU\n")
                naikann_bet_lalu_appeared = True

            file.write(hasil_gabungan)

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

    # Write the HABANERO label to the file
    if preferred_game_list_hb:
        file.write("\n🔥 HABANERO 🔥\n")

        # Generate and write Habanero results to the file
        generated_results_hb = generate_habanero_results(preferred_game_list_hb)

        for game_name, game_results in generated_results_hb:
            file.write(f"\n🎯 {game_name}\n")
            for result in game_results:
                file.write(result + "\n")

    # Write the SPADE GAMING label to the file if SPADE GAMING games are chosen
    if preferred_game_list_spd:
        file.write("\n🔥 SPADE GAMING 🔥\n")

        # Display results for each preferred Spade Gaming game
        for game_name in preferred_game_list_spd:
            file.write(f"\n🎯 {game_name}\n")

            # Generate and write Spade Gaming results to the file
            generated_results_spd = generate_spade_results([game_name])

            for game_name, game_results in generated_results_spd:
                for result in game_results:
                    file.write(result + "\n")

     # Write the note to the file
    file.write("\n\nNote: bet sesuai saldo anda, ingat tetap santai dan jangan terbawa suasana.\n")               

# Confirmation message
print("Hasil telah disimpan dalam file 'hasil.txt'.")
