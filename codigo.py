def char_to_byte(char):
  return format(ord(char), '08b')

def word_to_bytes(word):
  return ' '.join(format(ord(char), '08b') for char in word)

def byte_to_char(byte):
  char = chr(int(byte, 2))
  ascii_value = ord(char)
  return f'{char}-{ascii_value}'

def main():
  while True:
      print("Ingrese una opción:")
      print("1. Convertir letra a binario")
      print("2. Convertir palabra a binario")
      print("3. Convertir binario a letra y valor ASCII")
      print("4. Salir")

      opcion = input("Opción: ")

      if opcion == '1':
          letra = input("Ingrese una letra: ")
          if len(letra) == 1:
              print(f"Representación en byte de '{letra}': {char_to_byte(letra)}")
          else:
              print("Debe ingresar solo una letra.")

      elif opcion == '2':
          palabra = input("Ingrese una palabra: ")
          print(f"Representación en byte de '{palabra}': {word_to_bytes(palabra)}")

      elif opcion == '3':
          binario = input("Ingrese una representación binaria (8 bits): ")
          if len(binario) == 8 and all(c in '01' for c in binario):
              print(f"Representación ASCII de '{binario}': {byte_to_char(binario)}")
          else:
              print("Debe ingresar una representación binaria válida de 8 bits.")

      elif opcion == '4':
          print("Saliendo del programa...")
          break

      else:
          print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
  main()
