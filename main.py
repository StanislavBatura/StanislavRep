elements_number = int(input("Liczba elementow do wyslania: "))
counter = 1
total_weight = 0
max_weight_element = 0
max_weight_number = 0
package = 0
container = 0


while counter <= elements_number:
    weight_element = int(input(f"Podaj wage elementu {counter} [kg] "))
    total_weight += weight_element
    container += weight_element

    if weight_element < 1:
        break
    if weight_element > 10:
        break

    if container >= 20:
        package += 1
        container = 0

    if container < 20 and counter == elements_number:
        package += 1

    if weight_element > max_weight_element:
        max_weight_element = weight_element
        max_weight_number = counter

    if weight_element == 0:
        break

    counter += 1

print(f"summa kilogramow {total_weight} kg")
print(f"element {max_weight_number} mial najwiencej kg: {max_weight_element}")
print(f"Iloszcz paczek: {package}")
print(f"Liczba pustych kg {package * 20 - total_weight}")
print(f"Paczka {1} miala najwiencej pustych kg: {1}")
