# Evaluacion Final documentacion parte practica


El programa ofrece las siguientes opciones a través de un menú:
1. **Generar representación en byte de un carácter:** Si el usuario ingresa un carácter, el programa retorna su representación binaria.
2. **Generar representación en byte de una palabra:** Si el usuario ingresa una palabra, el programa retorna la representación binaria de cada carácter.
3. **Generar representación ASCII de un byte:** Si el usuario ingresa un byte en formato binario, el programa retorna su carácter ASCII correspondiente y su valor en decimal.
4. **El usuario no quiere hacer nada**: si el usuario no quiere hacer nada, el programa retorna un mensaje que indique que salio del programa.

luego de crear el codigo lo agrego a una carpeta donde empiezo a usar git bash:
1.  **cree una llave ssh**
   ssh-keygen -t ed25519 -C "cristiandavidgarcia10@gmail.com"
2. **creo mi creo mi nombre de usuario y mi correo**
   git config --global user.name "cristian"
   git config --global user.email "cristiandavidgarcia10@gmail.com"
3. **clono mi repositorio**
   git clone add origin git@github.com:jimk14/Evaluacion-Final.git
4. **creo una rama para colocar el codigo**
   git branch "codigo"
5. **agrago el codigo**
   git add .\codigo.py
6.**hago el commit**
   git commit -m "codigo"
7. **hago el push**
   git push origin codigo
8. **cambio a la rama main que viene por defecto**
   git checkout main
9.**realizo el merge del codigo**
   git merge codigo

# git ignore

1. **creo una rama para colocar el .gitignore**
   git branch "gitignore"
2. **agrago el .gitignore**
   git add .\.gitignore
3.**hago el commit**
   git commit -m "gitignore"
4. **hago el push**
   git push origin gitignore
5. **cambio a la rama main que viene por defecto**
   git checkout main
6.**realizo el merge del codigo**
   git merge gitignore
7.**hago el pull request**




 
