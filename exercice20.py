adresse_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
#1. première adresse
print("1)Première adresse :", adresse_ip[0])
# 2. Dernière adresse
print("2)Dernière adresse :", adresse_ip[-1])
# 3. Troisième adresse
print("3)Troisième adresse :", adresse_ip[2])
# 4. Ajout "172.31.0.1"
adresse_ip.append("172.31.0.1")
print("4)Après ajout :", adresse_ip)
# 5. Suppression "200.100.50.1"
if "200.100.50.1" in adresse_ip:
    adresse_ip.remove("200.100.50.1")
print("5)Après suppression :", adresse_ip)
# 6. Nombre d'adresses restantes
print("6)Nombre d'adresses :", len(adresse_ip))
# 7. Vérifier présence de "192.168.0.1"
if "192.168.0.1" in adresse_ip:
    print("7)oui l'adresse 192.168.0.1 présent ")
else:
    print("7)Non l'adresse 192.168.0.1 n'est pas présent")
# 8. Classe de "10.0.0.1" (classe A car 1-126)
print("8)Classe de 10.0.0.1 : Classe A")
# 9. Trier la liste par ordre croissant
trier_ips = sorted(adresse_ip, key=lambda x: [int(i) for i in x.split('.')])
print("9)Liste triée :", trier_ips)
# 10. Vérifier si toutes sont de classe C
def classe(ip):
    premier = int(ip.split('.')[0])
    if 1 <= premier <= 126:
        return "A"
    elif 128 <= premier <= 191:
        return "B"
    elif 192 <= premier <= 223:
        return "C"
    else:
        return "Autre"

toutes_c = all(classe(ip) == "C" for ip in adresse_ip)
if toutes_c:
    print("10)Oui, toutes en classes C")
else:
    print("10)Non, n'est pas toutes en classes C")
# 11. Compter les adresses publiques
def est_publique(ip):
    premier, deuxieme = [int(i) for i in ip.split('.')[:2]]
    # privées
    if premier == 10:
        return False
    if premier == 172 and 16 <= deuxieme <= 31:
        return False
    if premier == 192 and deuxieme == 168:
        return False
    if premier == 169 and deuxieme == 254:
        return False
    return True

nb_publiques = sum(1 for ip in adresse_ip if est_publique(ip))
print("11) Nombre d'adresses publiques :",nb_publiques )


