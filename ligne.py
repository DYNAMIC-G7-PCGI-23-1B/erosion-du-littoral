def ligne(type) :
    if type == "falaise" or type == "roche" :
        # Stagnation dans 9 cas sur 10. Recul faible dans 1 cas sur 10
        return "0/1/9/0/0"
    if type == "sable" :
        # Stagnation dans 4 cas sur 10. Recul faible dans 2 cas sur 10. Avancée faible dans 2 cas sur 10.
        # Recul fort dans 1 cas sur 10. Avancée forte dans 1 cas sur 10
        return "1/2/4/2/1"
    if type == "vase" :
        # Stagnation dans 6 cas sur 10. Avancée faible dans 2 cas sur 10. Avancée forte dans 1 cas sur 10.
        # Recul faible dans 1 cas sur 10.
        return "0/1/6/2/1"