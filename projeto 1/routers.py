from asyncio import gather
from converter import sync_converter, async_converter
from fastapi import APIRouter, Path, Query
from schemas import ConverterInput, ConverterOutput

router = APIRouter(prefix='/converter')

# Path parameter -> Faz parte do caminho

# Query parameter -> Segue depois da interrogação
# Ex.: https://example.com/from_currency=BRL/?to_currencies=USD,EUR&price=15

# Body parameter -> Não usado nesse projeto


@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')

    result = []
    for currency in to_currencies:
        response = sync_converter(from_currency=from_currency,
                                  to_currency=currency,
                                  price=price)
        result.append(response)
    
    return result


@router.get('/async/{from_currency}')
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'),
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price: float = Query(gt=0)
):
    to_currencies = to_currencies.split(',')

    coroutines = []
    for currency in to_currencies:
        coro = async_converter(from_currency=from_currency,
                               to_currency=currency,
                               price=price)
        coroutines.append(coro)
    result = await gather(*coroutines)
    return result


@router.get('/async/v2/{from_currency}', response_model=ConverterOutput)
async def async_converter_router(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$')
):
    to_currencies = body.to_currencies
    price = body.price

    coroutines = []
    for currency in to_currencies:
        coro = async_converter(from_currency=from_currency,
                               to_currency=currency,
                               price=price)
        coroutines.append(coro)
    result = await gather(*coroutines)

    return ConverterOutput(
        message="success",
        data=result
    )
