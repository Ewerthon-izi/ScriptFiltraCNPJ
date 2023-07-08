from ast import List
from tkinter.tix import COLUMN
import pandas as pd

empresas = pd.read_csv("Script R/cnpjreceita_r_2023/dados_junho/dados_processados/estabele.CSV")

#convertendo para string os campos cnpj(caso estaja int remove os 0 a esquerda)

empresas['cnpj_basico'] = empresas['cnpj_basico'].astype('string')
empresas['cnpj_ordem'] = empresas['cnpj_ordem'].astype('string')
empresas['cnpj_dv'] = empresas['cnpj_dv'].astype('string')
empresas['situacao_cadastral'] = empresas['situacao_cadastral'].astype('string')
empresas['date_situacao_cadastral'] = empresas['date_situacao_cadastral'].astype('string')
empresas['motivo_situacao_cadastral'] = empresas['motivo_situacao_cadastral'].astype('string')
empresas['cep'] = empresas['cep'].astype('string')
empresas['municipio'] = empresas['municipio'].astype('string')
empresas['cnae_fiscal_principal'] = empresas['cnae_fiscal_principal'].astype('string')

#cnae zero a esquerda

#,data,cnpj_basico,identificador_matriz_filial,nome_fantasia,situacao_cadastral,date_situacao_cadastral,
# motivo_situacao_cadastral,nome_cidade_no_exterior,codigo_pais,date_inicio_atividade,cnae_fiscal_principal,cnae_fiscal_secundaria,
# tipo_logradouro,logradouro,numero,complemento,bairro,cep,uf,municipio,ddd,telefone_1,ddd2,telefone_2,ddd_fax,fax,correio_eletronico,situacao_especial,
# date_situacao_especial

# tamanho das partes do cnpj

tam_basico = 8
tam_ordem = 4
tam_dv = 2
tam_situacaoCadastral = 2
tam_date = 8
tam_cep = 8
tam_municipio = 4
tam_motivo_situacao = 2
tam_cnae = 7

print(empresas)

# expressoes lambdas para adicionar 0 a esquerda para prencher os cnpjs

empresas['cnpj_basico'] = empresas['cnpj_basico'].map(lambda x: x.zfill(tam_basico))

empresas['cnpj_ordem'] = empresas['cnpj_ordem'].map(lambda x: x.zfill(tam_ordem))

empresas['cnpj_dv'] = empresas['cnpj_dv'].map(lambda x: x.zfill(tam_dv))

empresas['situacao_cadastral'] = empresas['situacao_cadastral'].map(lambda x: x.zfill(tam_situacaoCadastral))

empresas['date_situacao_cadastral'] = empresas['date_situacao_cadastral'].map(lambda x: x.zfill(tam_date))

empresas['motivo_situacao_cadastral'] = empresas['motivo_situacao_cadastral'].map(lambda x: x.zfill(tam_motivo_situacao))

empresas['cep'] = empresas['cep'].map(lambda x: x.zfill(tam_cep))

empresas['municipio'] = empresas['municipio'].map(lambda x: x.zfill(tam_municipio))

empresas['cnae_fiscal_principal'] = empresas['cnae_fiscal_principal'].map(lambda x: x.zfill(tam_municipio))

empresas['cnpj_basico'] = empresas['cnpj_basico'].map(str) + empresas['cnpj_ordem'].map(str) + empresas['cnpj_dv'].map(str)

empresas.drop(columns=["cnpj_ordem", "cnpj_dv","ddd2", "telefone_2" ,"ddd_fax", "fax"], inplace = True)

empresas.rename(columns={'cnpj_basico':'cnpj'}, inplace = True)

empresas.to_csv("Script R/cnpjreceita_r_2023/dados_junho/dados_processados/ajuste_cnpj", sep=',', encoding='utf-8')