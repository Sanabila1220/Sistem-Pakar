RULES = {
    "1": {
        "name": "Lampu mati",
        "diagnosis": "Periksa lampu, sakelar, dan sambungan listrik."
    },
    "2": {
        "name": "MCB trip",
        "diagnosis": "Kemungkinan beban berlebih atau gangguan listrik."
    },
    "3": {
        "name": "Lampu redup",
        "diagnosis": "Kemungkinan tegangan rendah atau sambungan kurang baik."
    },
    "4": {
        "name": "Perangkat panas",
        "diagnosis": "Periksa ventilasi dan beban perangkat."
    }
}


def diagnose(choices):
    results = []

    if "1" in choices and "2" in choices:
        results.append(
            "Kemungkinan gangguan rangkaian atau beban berlebih."
        )

    for choice in sorted(choices):
        if choice in RULES and choice not in {"1", "2"}:
            results.append(RULES[choice]["diagnosis"])

    if not results:
        results.append("Gejala tidak valid atau belum dikenali.")

    return results


def run_expert_system():
    print("=== ELECTRICAL EXPERT SYSTEM ===")

    for key, rule in RULES.items():
        print(f'{key}. {rule["name"]}')

    raw = input("Masukkan nomor gejala (contoh: 1,2): ")
    choices = {x.strip() for x in raw.split(",")}
    choices &= set(RULES)

    print("\n=== HASIL DIAGNOSIS ===")
    for result in diagnose(choices):
        print("-", result)

    print("\nCatatan: Simulasi edukasi, bukan diagnosis keselamatan listrik.")