from exemplo1 import frutas

print("\nOperações com listas:")
frutas.append("morango")
print("Após append:", frutas)

frutas.remove("banana")
print("\nApós remove:", frutas)

frutas[1] = "kiwi"
print("\nApós modificação:", frutas)

nova_lista = frutas + ["uva", "manga"]
print("\nApós concatenação:", nova_lista)
