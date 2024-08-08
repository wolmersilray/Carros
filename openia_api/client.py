import google.generativeai as genai




def get_car_ai_bio(brand, model, year):
    
    genai.configure(api_key= 'AIzaSyBDi_qNOMdnAGyPaUDJL_nttJNkug282oU')

    generation_config={
        "candidate_count": 1,
        "temperature": 1.0,
    }

    model= genai.GenerativeModel(
        'gemini-1.5-flash',
       generation_config= generation_config
        )

    prompt= ''''Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.
                Descreva especificações técnicas desse modelo de carro.
            '''
    prompt= prompt.format(brand, model, year)

    response= model.generate_content(
        contents=prompt,

        )

     # Verifique o tipo e conteúdo da resposta
    print(f"Tipo de resposta: {type(response)}")
    print(f"Conteúdo da resposta: {response}")

    # Acesse o texto gerado (ajuste conforme o formato da resposta)
    # Exemplo genérico:
    if hasattr(response, 'text'):
        return response.text
    elif hasattr(response, 'get_generated_text'):
        return response.get_generated_text()
    else:
        raise ValueError("Formato da resposta não reconhecido.")

