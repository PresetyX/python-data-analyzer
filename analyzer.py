import pandas as pd
import os

def load_data(folder_path):
    """
    Carrega todos os arquivos CSV de uma pasta e os combina em um único DataFrame.
    """
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    if not all_files:
        raise ValueError("Nenhum arquivo CSV encontrado na pasta especificada.")
    
    df_list = []
    for filename in all_files:
        df_list.append(pd.read_csv(filename))
        
    # Concatena todos os dataframes da lista em um só
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def clean_data(df):
    """
    Limpa e pré-processa o DataFrame.
    """
    # Renomeia colunas para um padrão único
    df = df.rename(columns={
        'product_name': 'product',
        'item': 'product',
        'price': 'price',
        'value': 'price',
        'order_date': 'date'
    })

    # 1. Lida com valores faltando: remove linhas onde o preço está nulo
    df.dropna(subset=['price'], inplace=True)
    
    # 2. Corrige tipos de dados
    df['price'] = pd.to_numeric(df['price'])
    df['date'] = pd.to_datetime(df['date'])
    
    # 3. Padroniza texto: converte categorias para minúsculas
    df['category'] = df['category'].str.lower()
    
    # 4. Remove duplicatas
    df.drop_duplicates(subset=['order_id'], inplace=True)
    
    return df

def analyze_data(df):
    """
    Realiza análises no DataFrame limpo.
    """
    total_revenue = df['price'].sum()
    average_price = df['price'].mean()
    
    # Encontra o produto mais vendido (pela quantidade de vezes que aparece)
    best_selling_product = df['product'].mode()[0]
    
    # Vendas por categoria
    sales_by_category = df.groupby('category')['price'].sum().sort_values(ascending=False)
    
    analysis_results = {
        'total_revenue': total_revenue,
        'average_price': average_price,
        'best_selling_product': best_selling_product,
        'sales_by_category': sales_by_category
    }
    return analysis_results

def generate_report(results):
    """
    Gera um relatório formatado no console.
    """
    print("\n--- Relatório de Análise de Vendas ---")
    print(f"\nReceita Total: R$ {results['total_revenue']:.2f}")
    print(f"Preço Médio do Produto: R$ {results['average_price']:.2f}")
    print(f"Produto Mais Vendido: {results['best_selling_product']}")
    
    print("\n--- Vendas por Categoria ---")
    print(results['sales_by_category'].to_string(float_format="R$ {:,.2f}".format))
    print("\n--- Fim do Relatório ---")

def main():
    """
    Função principal que orquestra o processo.
    """
    data_folder = 'data'
    
    print("Iniciando processo de análise de dados...")
    
    try:
        # Etapa 1: Carregar os dados
        print(f"1. Carregando dados da pasta '{data_folder}'...")
        raw_df = load_data(data_folder)
        
        # Etapa 2: Limpar os dados
        print("2. Limpando e preparando os dados...")
        cleaned_df = clean_data(raw_df)
        
        # Etapa 3: Analisar os dados
        print("3. Realizando análise...")
        analysis = analyze_data(cleaned_df)
        
        # Etapa 4: Gerar o relatório
        print("4. Gerando relatório final...")
        generate_report(analysis)
        
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    main()
