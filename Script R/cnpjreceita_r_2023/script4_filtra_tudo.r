
#usando a lista de cnpj's obtidos no script 03, devo agora filtrar todas as tabelas 
#buscando o cnpj

library(data.table)
library(dplyr)

cnpjs <- read.csv("dados_junho/dados_processados/cnpj_save.CSV")  
output_folder <- "dados_junho/dados_processados/"
caminho_dados <- "dados_junho/dados_processamento/estabelecimentos/"

# filtrar socios -----------------------------------------------------------------------------------------------------




#filtrar estabelecimentos----------------------------------------------------------------------------------------------


estabele_to_filter <- list.files(caminho_dados, pattern = ".*\\ESTABELE") #pegando as tabelas para filtrar

  estabele_lista <- list()
  for(i in 1:length(estabele_to_filter)){
    df <- fread(file.path(caminho_dados, estabele_to_filter[i]),  encoding="Latin-1", header = FALSE)
    #df <- df[,-1] #contador atrapalhando
    estabele_lista[[i]] <- inner_join(cnpjs, df, by = c("x"="V1"))
  }
  
  
  estabele_df <- do.call("rbind", estabele_lista)
  colnames(estabele_df) <- 
    c("cnpj_basico","cnpj_ordem","cnpj_dv","identificador_matriz_filial","nome_fantasia",
      "situacao_cadastral","date_situacao_cadastral","motivo_situacao_cadastral","nome_cidade_no_exterior",
      "codigo_pais","date_inicio_atividade","cnae_fiscal_principal","cnae_fiscal_secundaria",
      "tipo_logradouro","logradouro","numero","complemento","bairro","cep","uf","municipio",
      "ddd","telefone_1","ddd2","telefone_2","ddd_fax","fax","correio_eletronico","situacao_especial","date_situacao_especial")
  
  
  estabele_df$data <- "06/2023"
  estabele_df <- estabele_df%>% select(data, everything())
  write.csv(estabele_df, file=paste0(output_folder,"/","estabele.csv"), row.names = F)
  
  rm(df, estabele_df, estabele_lista, estabele_to_filter, file)
  
 

  
  