import os
from datetime import datetime, timedelta
import random

def generate_filename(base_name):
    counter = 1
    while True:
        filename = f"{base_name}-{counter}.txt"
        if not os.path.exists(filename):
            return filename
        counter += 1

def read_games_from_file(file_path):
    with open(file_path, 'r') as file:
        games = [line.strip() for line in file.readlines()]
    return games

def get_random_games(file_path, count=3):
    games = read_games_from_file(file_path)
    return random.sample(games, count)

def generate_spade_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2  
        random.shuffle(modes)

        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 25, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 19)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            hasil_gabungan = f"{angka} {mode} {dc}"

            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        game_results.append("HENTIKAN PUTAR OTOMATIS\nKEMENANGAN FREE SPIN ✔️")

        results.append((game_name, game_results))

    return results

def generate_habanero_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2  
        random.shuffle(modes)

        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 30, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 20)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            hasil_gabungan = f"{angka} {mode} {dc}"

            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        game_results.append("ULANGI SAMPAI 2X")

        results.append((game_name, game_results))

    return results

def generate_mcg_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2
        random.shuffle(modes)

        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 25, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 19)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            hasil_gabungan = f"{angka} {mode} {dc}"

            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        game_results.append("ULANGI SAMPAI 2X")

        results.append((game_name, game_results))

    return results

def generate_nlc_results(preferred_games):
    results = []

    for game_name in preferred_games:
        game_results = []
        modes = ["MANUAL", "AUTO"] * 2
        random.shuffle(modes)

        naikan_bet_lalu_appeared = False
        bet_lalu_position = random.randint(2, 4)

        for i, mode in enumerate(modes, start=1):
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 25, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 19)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            hasil_gabungan = f"{angka} {mode} {dc}"

            if i == bet_lalu_position and not naikan_bet_lalu_appeared:
                game_results.append("NAIKAN BET LALU")
                naikan_bet_lalu_appeared = True

            game_results.append(hasil_gabungan)

        results.append((game_name, game_results))

    return results

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

print("\033[92m" + """
██████╗  ██████╗ ██╗      █████╗      ██████╗  █████╗  ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██║     ██╔══██╗    ██╔════╝ ██╔══██╗██╔════╝██╔═══██╗██╔══██╗
██████╔╝██║   ██║██║     ███████║    ██║  ███╗███████║██║     ██║   ██║██████╔╝
██╔═══╝ ██║   ██║██║     ██╔══██║    ██║   ██║██╔══██║██║     ██║   ██║██╔══██╗
██║     ╚██████╔╝███████╗██║  ██║    ╚██████╔╝██║  ██║╚██████╗╚██████╔╝██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                                                                              
              ┌П┐(ಠ_ಠ)┌П┐ Created by: SEO-SEOAN ┌П┐(ಠ_ಠ)┌П┐ 
==================================================================================                                                                              
""")

pola_situs = input("POLA UNTUK SITUS ? : ")

# Read games from files and choose 3 random games for each provider
preferred_game_list_pragmatic = get_random_games('pragmatic.txt')
preferred_game_list_pg = get_random_games('pgsoft.txt')
preferred_game_list_hb = []
preferred_game_list_spd = []
preferred_game_list_mcg = []
preferred_game_list_nlc = []

mau_nambah = input("Mau Nambah Game HAB,SPD,MCG,NLC? (hab/spd/mcg/nlc/tidak): ")
if mau_nambah.lower() == "hab":
    preferred_game_list_hb = get_random_games('habanero.txt')
elif mau_nambah.lower() == "spd":
    preferred_game_list_spd = get_random_games('spade.txt')
elif mau_nambah.lower() == "mcg":
    preferred_game_list_mcg = get_random_games('micro.txt')
elif mau_nambah.lower() == "nlc":
    preferred_game_list_nlc = get_random_games('nolimitcity.txt')

current_date = datetime.now()
formatted_date = current_date.strftime("%d %B %Y")

filename = generate_filename("hasil")

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"🎰 INFO POLA GACOR {pola_situs} {formatted_date} 🎰\n")

    file.write("\n🔥 PRAGMATIC 🔥\n")
    for idx, game_name in enumerate(preferred_game_list_pragmatic, start=1):
        file.write(f"\n🎯 {game_name}\n")
        naikann_bet_lalu_appeared = False

        results = []
        for _ in range(2):  
            angka = pilih_random_angka_pg("MANUAL")
            simbol = pilih_random_simbol_pg()
            mode = "MANUAL"
            dc = pilih_random_dc_pg()
            results.append((angka, simbol, mode, dc))

        for _ in range(2): 
            angka = pilih_random_angka_pg("AUTO")
            simbol = pilih_random_simbol_pg()
            mode = "AUTO"
            dc = pilih_random_dc_pg()
            results.append((angka, simbol, mode, dc))

        random.shuffle(results)

        naikan_bet_lalu_position = random.randint(2, 4)

        for i, hasil in enumerate(results, start=1):
            angka, simbol, mode, dc = hasil
            hasil_gabungan = f"{angka}X {simbol} {mode} {dc}\n"

            if i == naikan_bet_lalu_position and not naikann_bet_lalu_appeared:
                file.write("NAIKAN BET LALU\n")
                naikann_bet_lalu_appeared = True

            file.write(hasil_gabungan)

    file.write("\n🔥 PG SOFT 🔥\n")
    for game_name in preferred_game_list_pg:
        file.write(f"\n🎯 {game_name}\n")
        modes = ["MANUAL", "AUTO"] * 2 
        random.shuffle(modes)

        naikan_bet_lalu_appeared = False

        for mode in modes:
            if mode == "AUTO":
                angka = random.choice([f"{num}X" for num in [10, 30, 50]])
            elif mode == "MANUAL":
                angka = random.choice([f"{num}X" for num in range(11, 20)])
            dc = random.choice(["TURBO ON", "TURBO OFF"])

            hasil_gabungan = f"{angka} {mode} {dc}\n"
            file.write(hasil_gabungan)

            if not naikan_bet_lalu_appeared and random.random() < 0.5:
                file.write("NAIKAN BET LALU\n")
                naikan_bet_lalu_appeared = True

        if random.random() < 0.5:
            file.write("ULANGI SAMPAI 2X\n")

    if preferred_game_list_hb:
        file.write("\n🔥 HABANERO 🔥\n")
        generated_results_hb = generate_habanero_results(preferred_game_list_hb)
        for game_name, game_results in generated_results_hb:
            file.write(f"\n🎯 {game_name}\n")
            for result in game_results:
                file.write(result + "\n")

    if preferred_game_list_spd:
        file.write("\n🔥 SPADE GAMING 🔥\n")
        generated_results_spd = generate_spade_results(preferred_game_list_spd)
        for game_name, game_results in generated_results_spd:
            file.write(f"\n🎯 {game_name}\n")
            for result in game_results:
                file.write(result + "\n")

    if preferred_game_list_mcg:
        file.write("\n🔥 MICROGAMING 🔥\n")
        generated_results_mcg = generate_mcg_results(preferred_game_list_mcg)
        for game_name, game_results in generated_results_mcg:
            file.write(f"\n🎯 {game_name}\n")
            for result in game_results:
                file.write(result + "\n")

    if preferred_game_list_nlc:
        file.write("\n🔥 NO LIMIT CITY 🔥\n")
        generated_results_nlc = generate_nlc_results(preferred_game_list_nlc)
        for game_name, game_results in generated_results_nlc:
            file.write(f"\n🎯 {game_name}\n")
            for result in game_results:
                file.write(result + "\n")

    file.write("\n\nNote: bet sesuai saldo anda, ingat tetap santai dan jangan terbawa suasana.\n")

print(f"Hasil telah disimpan dalam file '{filename}'.")
