import pandas as pd 


tabela_df= {
    "Nome" : ["Kauã", "Felipe"],
    "Idade" : ["19", "18"],
    "Curso" : ["CC", "CC"]
}

dataframe = pd.DataFrame(tabela_df)

#adicionando novos Nomes, idades e cursos
novos_nomes = {
    "Nome" : ["Hugo", "Rosas"], 
    "Idade" : ["17", "15"],
    "Curso" : ["CC", "CC"]
}

novos_nomes_df = pd.DataFrame(novos_nomes)

dataframe = dataframe._append(novos_nomes_df, ignore_index=True)


#Edição de tabela
print("\nAntes da edição:\n")
print(dataframe)


dataframe.loc[dataframe['Nome'] == 'Hugo', 'Idade'] = '18'

print("\nDepois da edição \n")
print(dataframe)

#adicionar colunas
#tabela_df.loc[:, "Imposto"] = 0
#print(tabela_df)


#Excluindo tabela ou linha:

dataframe = dataframe.drop(index=1).reset_index(drop=True)
print("\nDepois de excluir\n")
print(dataframe)


dataframe.to_excel("./tabela.xlsx")
