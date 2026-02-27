def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(seed_type.capitalize(), " seeds: ", quantity,
              " packets available")
    elif (unit == "grams"):
        print(seed_type.capitalize(), " seeds: ", quantity,
              " grams total")
    elif (unit == "area"):
        print(seed_type.capitalize(), " seeds: covers ", quantity,
              " square meters")
    else:
        print(seed_type.capitalize(), " seeds: ", quantity,
              " Unknown unit type")
