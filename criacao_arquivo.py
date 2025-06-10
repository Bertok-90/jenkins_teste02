from numero_aleatorio import numero
from menssagem import mensagem
#
with open('arquivo_log.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('             FILE TESTE PARA JENKINS FILE          \n')
    arquivo.write('\n    - O numero sorteado aleatoriamente => %s\n'%numero)
    arquivo.write('\n    - A mesagem que consta na variavel no arquivo de mensagem => %s'%mensagem)