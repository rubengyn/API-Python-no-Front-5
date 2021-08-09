# https://replit.com/@r_all/questao#code/correcao.py
import sys
entrada = sys.stdin.read()

# dividiar a entrada em duas listas
listas = entrada.split('###')

gabarito = listas[0].split('\n')
respostas = listas[1].split('\n')

# remover linhas duplicadas e linhas vazias
gabarito = list(dict.fromkeys(gabarito))
respostas = list(dict.fromkeys(respostas))
if '' in gabarito:
  lista_1.remove('')
if '' in respostas:  
  respostas.remove('')

# criar dicionario gabarito
dic_gab = dict()
for linha_gab in gabarito:
  # substituiu 2 espacos por 1
  linha_gab = linha_gab.replace('  ',' ')
  linha_gab = linha_gab.replace('  ',' ')
  
  # remove ponto
  linha_gab = linha_gab.replace('.','')

  # substitui Correto e incorreto
  linha_gab = linha_gab.replace('INCORRETA','E')
  linha_gab = linha_gab.replace('CORRETA','C')
  linha_gab = linha_gab.replace('ERRADO','E')
  linha_gab = linha_gab.replace('CERTO','C')
  
  
  # retirar espaço final de linha
  while(True):
    if linha_gab[-1] == ' ':
      linha_gab= linha_gab[:-1]
    else:
      break

  if ' ' in linha_gab:
    numero , letra = linha_gab.split(' ')
    dic_gab[numero] = letra
  else:
    next

# fazer correção
retorno = ''
for linha_resp in respostas:
  # substituiu 2 espacos por 1
  linha_resp = linha_resp.replace('  ',' ')
  linha_resp = linha_resp.replace('  ',' ')
  if ' ' in linha_resp:
    numero,letra = linha_resp.split(' ')
    if numero in dic_gab:
            
      if len(letra) == 1 or dic_gab[numero]!=letra[0:1]:
        retorno += str(numero+' '+letra[0]+'->'+dic_gab[numero]+'\n')

  else:
    next

print(retorno)
#print(dic_gab)


