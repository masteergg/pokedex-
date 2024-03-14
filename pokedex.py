print('-'*50)
print('       Bem-vindo a pokedex by Kavin Yusuke    ')
print('-'*50)
# Faixa de entra visual
print('Type 1 to add a Pokemon')
print('Type 2 to remove a Pokemon')
print('Type 3 to view information about a Pokemon')

# Instruções para o usuário

pokemon_list = []

while True:
    verification = int(input('write a number according to your preference: '))
# Solicita ao usuario um numero de acordo com sua preferência    
    if verification == 1:
        # Uma verificação caso a variável verification receba 1 como resposta
        pokemon_name = input("What's your pokemon's name? ")
        pokemon_type = input('what type is this pokemon? ')

        pokemon_info = {'name': pokemon_name, 'type': pokemon_type}
        pokemon_list.append(pokemon_info)
         # Aqui criei um dicionário com as informações do Pokémon e adiciona as informaçôes a lista
        print('Pokemon added successfully')


    elif verification == 2:
        pokemon_name = input("Which Pokémon do you want to remove? ")
        pokemon_remove = None
        
        for pokemon in pokemon_list:
            if pokemon['name'] == pokemon_name:
                pokemon_to_remove = pokemon
                break
        
        if pokemon_remove:
            pokemon_list.remove(pokemon_remove)
            print('Pokemon removed successfully')
        else:
            print('Pokemon not found')

    elif verification == 3:
        pokemon_name = input("Which pokemon do you want to see the information? ")
        for pokemon in pokemon_list:
            if pokemon['name'] == pokemon_name:
                print('Name: ', pokemon['name'])
                print('Type: ', pokemon['type'])
                break
        else:
            print('Pokemon not found')

    else:
        print('Invalid option')
