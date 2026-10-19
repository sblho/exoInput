

#faire un programme qui récupère l'année de naissance de l'utilisateur et son prénom et qui affiche une phrase du type : "Bonjour PRENOM, vous êtes né(e) en ANNEE_DE_NAISSANCE et vous avez AGE ans.
#faire un  print dynamique avec les variables prénom et année de naissance

prenom = input("Quel est votre prénom ? ")
année_naissance = int(input("Quelle est votre année de naissance ? "))
age = 2026 - année_naissance
print(f"Bonjour {prenom}, vous êtes né(e) en {année_naissance} et vous avez {age} ans.")
