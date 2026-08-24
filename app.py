import os
import time
from google import genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. CHAVE DE ACESSO E CLIENTE GEMINI
# Busca do ambiente ou utiliza a chave definida
CHAVE_API = os.getenv("GEMINI_API_KEY", "SUA_CHAVE_AQUI")

client = genai.Client(api_key=CHAVE_API)

# 2. FUNÇÃO SELENIUM (Busca automatizada no Google e Redes Sociais)
def buscar_dados_com_selenium(termo_busca):
    print(f"\n🌐 [Selenium] Abrindo o Google Chrome para buscar: '{termo_busca}'...")
    
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--disable-blink-features=AutomationControlled")
    opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=opcoes)
    resultados_crus = []
    
    try:
        driver.get("https://google.com")
        time.sleep(2)
        
        campo_busca = driver.find_element(By.NAME, "q")
        campo_busca.send_keys(termo_busca)
        campo_busca.send_keys(Keys.ENTER)
        time.sleep(4)
        
        itens = driver.find_elements(By.CSS_SELECTOR, "div.g")
        
        for item in itens[:8]:
            try:
                titulo = item.find_element(By.TAG_NAME, "h3").text
                link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                if titulo and link:
                    resultados_crus.append(f"- Título: {titulo}\n  Link: {link}")
            except:
                continue
                
    except Exception as e:
        print(f"⚠️ Erro no robô: {e}")
    finally:
        driver.quit()
        
    return "\n".join(resultados_crus) if resultados_crus else "Nenhum link encontrado."

# 3. EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    nicho = "inauguração de lojas ou novas clínicas"
    localizacao = "Belém, Castanhal e regiao PA"
    
    print(f"\n### 🚀 Iniciando Prospecção para: {nicho} ###\n")
    
    termo = f"{nicho} em {localizacao}"
    dados_da_web = buscar_dados_com_selenium(termo)
    
    prompt_inteligente = f"""
    Você é um Analista de Inteligência de Mercado sênior focado em validação factual.
    Análise OS DADOS BRUTOS capturados pelo Selenium e crie um relatório de prospecção comercial.
    
    DADOS CAPTURADOS PELA BUSCA:
    {dados_da_web}
    
    REGRAS ANTI-ALUCINAÇÃO (CRÍTICO - RIGOR FACTUAL):
    1. Baseie-se ESTRITAMENTE nos dados capturados fornecidos acima. Jamais invente nomes de empresas, links, locais, telefones ou contatos que não estejam presentes de forma explícita no texto recebido.
    2. Se os dados capturados forem insuficientes para confirmar a existência de um lead ou nicho, informe categoricamente que não há dados suficientes para aquela entrada.
    3. Para o "Diagnóstico de Oportunidade Digital", fundamente a necessidade do lead APENAS no contexto real capturado (ex: ausência de site próprio no link retornado, dependência exclusiva de notícias/portais de terceiros, falta de canal direto de agendamento). Não invente dores fictícias ou hipotéticas que contradigam os fatos observados.
    
    SUA TAREFA:
  SUA TAREFA:
Filtre e selecione NO MÁXIMO as 5 melhores oportunidades reais dos dados capturados que correspondam ao nicho de '{nicho}' na região de '{localizacao}'.
Se houver menos de 5 leads válidos, retorne apenas os que forem reais e confirme que não há mais opções.
    
    FORMATO DA RESPOSTA:
    Para cada lead válido encontrado nos dados, retorne exatamente:
    - Nome do Negócio Local:
    - Ramo de Atuação:
    - Cidade/Localização:
    - Link / Referência da Web:
    - Diagnóstico de Oportunidade Digital (Fundamentado nos dados reais):
    """
    
    print("\n🧠 [Gemini] Processando os dados capturados e gerando o relatório...")
    
    try:
        resposta_gemini = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_inteligente,
        )
        
        print("\n\n################################################")
        print("## 🎉 RELATÓRIO FINAL DE LEADS GERADO COM SUCESSO ##")
        print("################################################\n")
        print(resposta_gemini.text)
        
    except Exception as erro:
        print(f"\n❌ Falha com o Gemini: {erro}")
