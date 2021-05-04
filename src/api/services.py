from src.core.tables import crete_after_quiz


async def service_back_call(data_dict: dict):
    try:
        crete_after_quiz(name=data_dict['name'], phone=data_dict['phone'], type_number=0)
        return True
    except Exception as e:
        return str(e)


async def service_after_quiz(data_dict: dict):
    try:
        crete_after_quiz(data_dict['name'], data_dict['phone'], data_dict['parameter1'],
                         data_dict['parameter2'], data_dict['parameter3'], data_dict['parameter4'],type_number=1)
        return True
    except Exception as e:
        print(e)
        return str(e)
