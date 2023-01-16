from playwright.async_api import async_playwright
import asyncio

'''
    Retorna a descrição de um notebook
'''
async def get_description(item):
    atributo = await item.query_selector('p')
    return await atributo.inner_text()


async def main():
    '''
    Acessa ao site indicado e extrai os dados dos notebooks_lenovo lenovo
    '''
    async with async_playwright() as pw:

        #inicia o Browser
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')

        #seleciona todos os notebooks do site
        notebooks = await page.query_selector_all('.caption')
        notebooks_lenovo = []
        for item in notebooks:

            #consulta a marca do notebook
            atributos = await item.query_selector_all('h4')
            titulo = await atributos[1].inner_text()

            #verifica se o notebook é Lenovo
            if 'Lenovo' in titulo:
                
                notebooks_lenovo.append({
                    'nome': titulo,
                    'preco': await atributos[0].inner_text(),
                    'descricao': await get_description(item)
                })
            
        # print(notebooks_lenovo)
        await browser.close()
        return notebooks_lenovo
 
def scrap():
    result = asyncio.run(main())
    print(result)
    return result