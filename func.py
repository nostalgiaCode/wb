import requests

def message_split(message):
    request=message.split()
    list_length=len(request)
    id=int(request[list_length-1])
    request.pop()
    request=' '.join(request)
    return request, id

def searchwb(message):
    input=message_split(message)
    product_name=input[0]
    target_id=input[1]
    reached_the_end=False
    reached_the_target=False
    page_number=0
    position=0
    while(reached_the_end==False) and (reached_the_target==False):
        position=0
        page_number=page_number+1
        url = f'https://search.wb.ru/exactmatch/sng/common/v4/search?appType=1&curr=rub&dest=82&page={str(page_number)}&query={product_name}&regions=4,68,102,70,69,30,86,40,1,66,110,22,31,48,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        response = requests.get(url)
        data = response.json()
        if len(data)==0:
            return 'Не найдено'
        else:
            try:    
                data = data['data']['products']
                for test_item in data:
                    position=position+1
                    if(target_id==test_item['id']):
                        return f'Страница {page_number} место {position}'
            except:
                return "Запрос сформулирован некорректно! Введите поисковый запрос и артикул!"