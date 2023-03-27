contatos = ['11,Henrique,henri.salles1@gmail.com\n',
                '12,Ana,ana@ana.com.br\n',
                '13,Antonio,antonio@antonio.com\n'
                ]

try:
    with open('dados/contatos_escrita.csv', encoding='latin_1', mode ='a+') as arquivo1:

        for contato in contatos:
            arquivo1.write(contato)

        arquivo1.flush()
        arquivo1.seek(0)

        for linha in arquivo_contatos:
            print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem Permissão de escrita')
finally:
    arquivo_contatos.close()
